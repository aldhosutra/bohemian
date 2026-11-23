#!/usr/bin/env python3
"""Stronger-judge audit of a random subset of pairwise comparisons.

The main judges are small, cheap models. This re-judges a random, task-stratified
sample of test-split pairs with a stronger model (same blind prompt, randomized
A/B by hash) and reports its win rates next to the cheap judges' verdicts on the
SAME pairs, plus agreement. It is a check on judge taste, not a replacement.

  python3 eval/audit.py --run v2 --per-ref 60
"""
import argparse
import collections
import json
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge import QUESTIONS, flip, pairwise  # noqa: E402
from lib.llm import spent  # noqa: E402

EVAL = Path(__file__).resolve().parent
AUDIT_JUDGE = "openai/gpt-5.4-mini"
VAL = {"treat": 1.0, "tie": 0.5, "ref": 0.0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--treat", default="bohemian")
    ap.add_argument("--refs", default="baseline,oneliner")
    ap.add_argument("--per-ref", type=int, default=60)
    ap.add_argument("--split", default="test")
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--judge", default=AUDIT_JUDGE, help="audit judge model")
    ap.add_argument("--suffix", default="", help="appended to output file names, e.g. _antialgorithm")
    args = ap.parse_args()
    run = EVAL / "results" / args.run
    tasks = {json.loads(l)["id"]: json.loads(l) for l in (EVAL / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    gens = {(g["task_id"], g["model"], g["arm"], g["sample"]): g["final"]
            for g in map(json.loads, (run / "generations.jsonl").read_text(encoding="utf-8").splitlines())}
    pw = [json.loads(l) for l in (run / "pairwise.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    rng = random.Random(args.seed)
    out = []
    for ref in args.refs.split(","):
        cells = sorted({(r["task_id"], r["model"], r["sample"]) for r in pw
                        if r["treat"] == args.treat and r["ref"] == ref and (args.split == "all" or tasks[r["task_id"]]["split"] == args.split)})
        by_task = collections.defaultdict(list)
        for c in cells:
            by_task[c[0]].append(c)
        tids = sorted(by_task)
        rng.shuffle(tids)
        picked = []
        while len(picked) < args.per_ref and any(by_task.values()):
            for t in tids:
                if by_task[t] and len(picked) < args.per_ref:
                    picked.append(by_task[t].pop(rng.randrange(len(by_task[t]))))

        def work(c):
            tid, model, s = c
            a, b = gens[(tid, model, args.treat, s)], gens[(tid, model, ref, s)]
            swapped = flip(tid, model, s, args.treat, ref + "|audit")
            r = pairwise(args.judge, tasks[tid], *((b, a) if swapped else (a, b)))
            if r is None:
                return None
            m = {"A": "ref", "B": "treat"} if swapped else {"A": "treat", "B": "ref"}
            return {"task_id": tid, "model": model, "sample": s, "ref": ref, "judge": args.judge,
                    **{q: ("tie" if r[q] == "tie" else m[r[q]]) for q in QUESTIONS}, "why": r["why"]}

        with ThreadPoolExecutor(8) as ex:
            out.extend(x for x in ex.map(work, picked) if x)
    (run / f"audit{args.suffix}.jsonl").write_text("\n".join(json.dumps(x) for x in out) + "\n", encoding="utf-8")

    cheap = collections.defaultdict(dict)
    for r in pw:
        cheap[(r["task_id"], r["model"], r["sample"], r["ref"])][r["judge"]] = r
    lines = [f"# Stronger-judge audit: {args.judge}, run `{args.run}`, {args.split} split\n",
             "Win rate of the treatment on the same pairs, by judge. Ties count half.\n",
             "| reference | n | judge | " + " | ".join(QUESTIONS) + " |", "|---|---|---|" + "---|" * len(QUESTIONS)]
    summary = {}
    for ref in args.refs.split(","):
        rows = [x for x in out if x["ref"] == ref]
        keys = [(x["task_id"], x["model"], x["sample"], ref) for x in rows]
        judges = sorted({j for k in keys for j in cheap[k]})
        summary[ref] = {}
        for name, verdicts in [(args.judge, rows)] + [(j, [cheap[k][j] for k in keys if j in cheap[k]]) for j in judges]:
            wr = {q: sum(VAL[v[q]] for v in verdicts) / max(1, len(verdicts)) for q in QUESTIONS}
            summary[ref][name] = wr
            lines.append(f"| {ref} | {len(verdicts)} | {name} | " + " | ".join(f"{100*wr[q]:.0f}%" for q in QUESTIONS) + " |")
        for j in judges:
            agree = [x["prefer"] == cheap[k][j]["prefer"] for x, k in zip(rows, keys) if j in cheap[k]]
            lines.append(f"\n- `prefer` agreement, audit judge vs {j} ({ref}): {100*sum(agree)/max(1,len(agree)):.0f}% of {len(agree)} pairs")
        lines.append("")
    (run / f"audit{args.suffix}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (run / f"audit_summary{args.suffix}.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print("\n".join(lines))
    print(f"spent ${spent():.4f}")


if __name__ == "__main__":
    main()
