#!/usr/bin/env python3
"""Blinded LLM judging.

pairwise: for each (task, model, sample), compare a treatment output with a
  reference arm's output. Position (A/B) is assigned by a hash, so it is random
  but reproducible and balanced. Judges never see arm names or process notes.
absolute: score a single output 1-5 on six dimensions, with no comparison.

  python3 eval/judge.py --run v1 --pairs bohemian:baseline,bohemian:oneliner
"""
import argparse
import hashlib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.llm import BudgetExceeded, chat, spent  # noqa: E402

EVAL = Path(__file__).resolve().parent
JUDGES = ["google/gemini-2.5-flash-lite", "openai/gpt-4o-mini"]
QUESTIONS = ["original", "unpredictable", "distinctive", "prefer", "task"]
DIMENSIONS = ["originality", "specificity", "distinctiveness", "coherence", "task_alignment", "creative_risk"]

PAIRWISE_SYSTEM = """You are an experienced editor judging two responses to the same creative brief. You do not know who or what wrote them, and they may have been produced in different ways. Judge only the text.

Answer five questions. For each, answer "A", "B" or "tie".
- original: Which avoids familiar, overused, predictable ideas more? Novelty only counts if it still makes sense for the brief.
- unpredictable: Which made choices you would be less likely to predict before reading it?
- distinctive: Which has a recognizable character of its own, rather than reading like generic AI-written text?
- prefer: Which would you actually choose to use or publish for this brief?
- task: Which satisfies the brief better as it was actually asked, including any length, format or content requirements?

Do not reward length for its own sake. Do not reward strangeness that does not serve the brief. Use "tie" only when you truly cannot separate them.
Respond with ONLY JSON: {"original": "A|B|tie", "unpredictable": "A|B|tie", "distinctive": "A|B|tie", "prefer": "A|B|tie", "task": "A|B|tie", "why": "<one sentence>"}"""

ABSOLUTE_SYSTEM = """You are an experienced editor scoring one response to a creative brief. You do not know who or what wrote it. Score each dimension from 1 to 5 using the anchors.

- originality: 1 = the most obvious take, stock ideas throughout; 3 = some fresh choices in a familiar frame; 5 = ideas a reader would not have predicted, which still make sense for the brief.
- specificity: 1 = generic abstractions that would fit any similar piece; 3 = a mix; 5 = concrete, particular details that do real work.
- distinctiveness: 1 = reads like default AI-generated text (stock phrases, even rhythm, tidy moral); 3 = competent but anonymous; 5 = a recognizable voice and sensibility of its own.
- coherence: 1 = confusing or self-contradictory; 3 = mostly clear with lapses; 5 = fully clear, consistent and readable.
- task_alignment: 1 = ignores the brief or breaks its stated requirements; 3 = does the job with notable misses; 5 = does exactly what was asked, for the asked audience, within any stated length/format.
- creative_risk: 1 = plays completely safe; 3 = one or two less conventional choices; 5 = takes real creative risks. Rate risk regardless of whether it pays off.

Respond with ONLY JSON: {"originality": n, "specificity": n, "distinctiveness": n, "coherence": n, "task_alignment": n, "creative_risk": n, "why": "<one sentence>"}"""


def parse_json(text):
    m = re.search(r"\{.*\}", text, flags=re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except ValueError:
        return None


def flip(task_id, model, sample, a, b):
    h = hashlib.sha256(f"{task_id}|{model}|{sample}|{a}|{b}".encode()).digest()[0]
    return h % 2 == 1


def pairwise(judge, task, x, y):
    """x, y are texts. Returns dict question -> 'A'|'B'|'tie' in the A/B frame as shown."""
    user = f"BRIEF:\n{task['prompt']}\n\n=== RESPONSE A ===\n{x}\n\n=== RESPONSE B ===\n{y}"
    for attempt in range(3):
        raw, _ = chat(judge, PAIRWISE_SYSTEM, user, temperature=0, max_tokens=300, seed_index=attempt, tag="judge:pair")
        d = parse_json(raw)
        if d and all(str(d.get(q, "")).strip() in {"A", "B", "tie"} for q in QUESTIONS):
            return {q: d[q].strip() for q in QUESTIONS} | {"why": d.get("why", "")}
    return None


def absolute(judge, task, x):
    user = f"BRIEF:\n{task['prompt']}\n\n=== RESPONSE ===\n{x}"
    for attempt in range(3):
        raw, _ = chat(judge, ABSOLUTE_SYSTEM, user, temperature=0, max_tokens=300, seed_index=attempt, tag="judge:abs")
        d = parse_json(raw)
        try:
            if d and all(1 <= int(d[k]) <= 5 for k in DIMENSIONS):
                return {k: int(d[k]) for k in DIMENSIONS} | {"why": d.get("why", "")}
        except (KeyError, ValueError, TypeError):
            pass
    return None


def load(run):
    gens = [json.loads(l) for l in (EVAL / "results" / run / "generations.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    tasks = {json.loads(l)["id"]: json.loads(l) for l in (EVAL / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    return gens, tasks


def append_unique(path, rows_iter, key):
    done = set()
    if path.exists():
        for l in path.read_text(encoding="utf-8").splitlines():
            done.add(key(json.loads(l)))
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--pairs", default="bohemian:baseline,bohemian:oneliner")
    ap.add_argument("--abs-arms", default=None, help="arms to score absolutely (default: all arms in the pairs)")
    ap.add_argument("--abs-second-judge-samples", default="0", help="sample indices the second judge also scores absolutely")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    gens, tasks = load(args.run)
    out_dir = EVAL / "results" / args.run
    by = {(g["task_id"], g["model"], g["arm"], g["sample"]): g for g in gens}
    pairs = [tuple(p.split(":")) for p in args.pairs.split(",") if p]
    abs_arms = set(args.abs_arms.split(",")) if args.abs_arms else {a for p in pairs for a in p}
    second = {int(s) for s in args.abs_second_judge_samples.split(",") if s != ""}

    pw_path, abs_path = out_dir / "pairwise.jsonl", out_dir / "absolute.jsonl"
    pw_done = append_unique(pw_path, None, lambda r: (r["task_id"], r["model"], r["sample"], r["treat"], r["ref"], r["judge"]))
    abs_done = append_unique(abs_path, None, lambda r: (r["task_id"], r["model"], r["arm"], r["sample"], r["judge"]))

    jobs = []
    for (tid, model, arm, s), g in by.items():
        for treat, ref in pairs:
            if arm != treat or (tid, model, ref, s) not in by:
                continue
            for judge in JUDGES:
                if (tid, model, s, treat, ref, judge) not in pw_done:
                    jobs.append(("pw", judge, tid, model, s, treat, ref))
        if arm in abs_arms:
            for i, judge in enumerate(JUDGES):
                if i > 0 and s not in second:
                    continue
                if (tid, model, arm, s, judge) not in abs_done:
                    jobs.append(("abs", judge, tid, model, s, arm, None))
    print(f"{len(jobs)} judge calls to run; spent so far ${spent():.4f}")

    def work(job):
        kind, judge, tid, model, s, a, b = job
        task = tasks[tid]
        if kind == "abs":
            r = absolute(judge, task, by[(tid, model, a, s)]["final"])
            return kind, r and {"task_id": tid, "model": model, "arm": a, "sample": s, "judge": judge, **r}
        treat_text, ref_text = by[(tid, model, a, s)]["final"], by[(tid, model, b, s)]["final"]
        swapped = flip(tid, model, s, a, b)
        x, y = (ref_text, treat_text) if swapped else (treat_text, ref_text)
        r = pairwise(judge, task, x, y)
        if r is None:
            return kind, None
        to_treat = {"A": "ref", "B": "treat"} if swapped else {"A": "treat", "B": "ref"}
        out = {q: ("tie" if r[q] == "tie" else to_treat[r[q]]) for q in QUESTIONS}
        return kind, {"task_id": tid, "model": model, "sample": s, "treat": a, "ref": b, "judge": judge,
                      "treat_position": "B" if swapped else "A", **out, "why": r["why"]}

    n = 0
    with ThreadPoolExecutor(args.workers) as ex, pw_path.open("a", encoding="utf-8") as fp, abs_path.open("a", encoding="utf-8") as fa:
        futs = [ex.submit(work, j) for j in jobs]
        for fut in as_completed(futs):
            try:
                kind, r = fut.result()
            except BudgetExceeded as e:
                print("BUDGET STOP:", e)
                ex.shutdown(cancel_futures=True)
                break
            except Exception as e:
                print("error:", e)
                continue
            if r is None:
                print("unparseable judge reply; skipped")
                continue
            (fp if kind == "pw" else fa).write(json.dumps(r, ensure_ascii=False) + "\n")
            n += 1
            if n % 100 == 0:
                print(f"  {n}/{len(jobs)}  spent ${spent():.4f}")
    print(f"done: {n} judgments; spent ${spent():.4f}")


if __name__ == "__main__":
    main()
