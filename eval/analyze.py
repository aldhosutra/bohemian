#!/usr/bin/env python3
"""Statistics and report for one benchmark run.

Unit of analysis is the TASK: every metric is first averaged over models and
samples within a task, then compared across arms with paired per-task
differences. 95% intervals are percentile bootstraps over tasks (10,000
resamples, fixed seed). "Better on X of Y tasks" is an exact two-sided sign test.

  python3 eval/analyze.py --run v1 [--treat bohemian] [--split all|dev|test]
"""
import argparse
import collections
import json
import math
from pathlib import Path

import numpy as np

EVAL = Path(__file__).resolve().parent
QUESTIONS = ["original", "unpredictable", "distinctive", "prefer", "task"]
DIMS = ["originality", "specificity", "distinctiveness", "coherence", "task_alignment", "creative_risk"]
RNG = np.random.default_rng(20261123)


def jl(path):
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()] if path.exists() else []


def boot(x, n=10000):
    x = np.asarray(x, dtype=float)
    if len(x) == 0:
        return float("nan"), float("nan"), float("nan")
    idx = RNG.integers(0, len(x), size=(n, len(x)))
    m = x[idx].mean(axis=1)
    return float(x.mean()), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def sign_test(diffs):
    pos = sum(1 for d in diffs if d > 1e-12)
    neg = sum(1 for d in diffs if d < -1e-12)
    n = pos + neg
    if n == 0:
        return pos, neg, 1.0
    k = min(pos, neg)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n * 2
    return pos, neg, min(1.0, p)


def kappa(a, b, labels):
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[l] * cb[l] for l in labels) / n ** 2
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")


def spearman(a, b):
    def rank(v):
        v = np.asarray(v, dtype=float)
        order = v.argsort()
        r = np.empty(len(v))
        r[order] = np.arange(len(v))
        for val in np.unique(v):
            r[v == val] = r[v == val].mean()
        return r
    if len(a) < 3:
        return float("nan")
    return float(np.corrcoef(rank(a), rank(b))[0, 1])


def per_task(rows, key, arm_field="arm"):
    acc = collections.defaultdict(list)
    for r in rows:
        v = r.get(key)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            continue
        acc[(r["task_id"], r[arm_field])].append(float(v))
    return {k: float(np.mean(v)) for k, v in acc.items()}


def paired(pt, treat, ref, tasks):
    diffs, t_vals, r_vals = [], [], []
    for tid in tasks:
        if (tid, treat) in pt and (tid, ref) in pt:
            diffs.append(pt[(tid, treat)] - pt[(tid, ref)])
            t_vals.append(pt[(tid, treat)])
            r_vals.append(pt[(tid, ref)])
    return diffs, t_vals, r_vals


def fmt(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{d}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--treat", default="bohemian")
    ap.add_argument("--split", default="all")
    args = ap.parse_args()
    run_dir = EVAL / "results" / args.run
    tasks_all = {t["id"]: t for t in jl(EVAL / "tasks.jsonl")}
    gens = jl(run_dir / "generations.jsonl")
    pw = jl(run_dir / "pairwise.jsonl")
    ab = jl(run_dir / "absolute.jsonl")
    met = json.loads((run_dir / "metrics.json").read_text(encoding="utf-8")) if (run_dir / "metrics.json").exists() else {}
    tasks = sorted(t for t in tasks_all if args.split == "all" or tasks_all[t]["split"] == args.split)
    tset = set(tasks)
    arms = sorted({g["arm"] for g in gens}, key=lambda a: (a != "baseline", a != "oneliner", a))
    treat = args.treat
    refs = [a for a in arms if a != treat and not a.startswith("bohemian")]
    models = sorted({g["model"] for g in gens})
    judges = sorted({r["judge"] for r in pw})
    summary = {"run": args.run, "split": args.split, "n_tasks": len(tasks), "arms": arms, "models": models,
               "judges": judges, "n_generations": sum(1 for g in gens if g["task_id"] in tset)}
    L = []
    L.append(f"# Benchmark report: run `{args.run}`, split `{args.split}`, treatment `{treat}`\n")
    L.append(f"- Tasks: {len(tasks)}  \n- Generator models: {', '.join(models)}  \n- Arms: {', '.join(arms)}  \n"
             f"- Generations analysed: {summary['n_generations']}  \n- Pairwise judges: {', '.join(judges)}\n")
    wrapped = [g["wrapped"] for g in gens if g["task_id"] in tset]
    L.append(f"- Outputs with a well-formed `<final>` block: {sum(wrapped)}/{len(wrapped)}\n")

    # 1. pairwise
    L.append("## 1. Blinded pairwise preference (treatment vs reference)\n")
    L.append("Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. "
             "Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.\n")
    summary["pairwise"] = {}
    for ref in refs:
        L.append(f"\n### {treat} vs {ref}\n")
        L.append("| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |")
        L.append("|---|---|---|---|---|")
        rows = [r for r in pw if r["treat"] == treat and r["ref"] == ref and r["task_id"] in tset]
        summary["pairwise"][ref] = {}
        for q in QUESTIONS:
            score = collections.defaultdict(list)
            c = collections.Counter(r[q] for r in rows)
            for r in rows:
                score[r["task_id"]].append({"treat": 1.0, "tie": 0.5, "ref": 0.0}[r[q]])
            per = [float(np.mean(v)) for v in score.values()]
            m, lo, hi = boot(per)
            pos, neg, p = sign_test([x - 0.5 for x in per])
            summary["pairwise"][ref][q] = {"win_rate": m, "ci": [lo, hi], "W": c["treat"], "T": c["tie"], "L": c["ref"],
                                           "tasks_above": pos, "tasks_below": neg, "p": p}
            L.append(f"| {q} | {100*m:.1f}% [{100*lo:.1f}, {100*hi:.1f}] | {c['treat']} / {c['tie']} / {c['ref']} | {pos} / {neg} | {p:.2g} |")
        for j in judges:
            jr = [r for r in rows if r["judge"] == j]
            if jr:
                wr = {q: np.mean([{"treat": 1, "tie": .5, "ref": 0}[r[q]] for r in jr]) for q in QUESTIONS}
                L.append(f"\n- {j}: " + ", ".join(f"{q} {100*wr[q]:.0f}%" for q in QUESTIONS))
        a_pos = [r for r in rows if r["treat_position"] == "A"]
        b_pos = [r for r in rows if r["treat_position"] == "B"]
        if a_pos and b_pos:
            fa = np.mean([{"treat": 1, "tie": .5, "ref": 0}[r["prefer"]] for r in a_pos])
            fb = np.mean([{"treat": 1, "tie": .5, "ref": 0}[r["prefer"]] for r in b_pos])
            L.append(f"- Position check (prefer): treatment win rate {100*fa:.0f}% when shown as A (n={len(a_pos)}), "
                     f"{100*fb:.0f}% when shown as B (n={len(b_pos)}).")

    # judge agreement
    L.append("\n### Judge agreement\n")
    summary["agreement"] = {}
    if len(judges) == 2:
        L.append("| question | % same verdict | Cohen's kappa |")
        L.append("|---|---|---|")
        idx = collections.defaultdict(dict)
        for r in pw:
            if r["task_id"] in tset and r["treat"] == treat:
                idx[(r["task_id"], r["model"], r["sample"], r["ref"])][r["judge"]] = r
        both = [v for v in idx.values() if len(v) == 2]
        for q in QUESTIONS:
            a = [v[judges[0]][q] for v in both]
            b = [v[judges[1]][q] for v in both]
            agree = np.mean([x == y for x, y in zip(a, b)]) if a else float("nan")
            k = kappa(a, b, ["treat", "tie", "ref"])
            summary["agreement"][q] = {"agree": float(agree), "kappa": k, "n": len(a)}
            L.append(f"| {q} | {100*agree:.0f}% | {fmt(k)} |")

    # 2. absolute
    L.append("\n## 2. Blinded absolute scores (1-5)\n")
    primary = judges[0] if judges else None
    summary["absolute"] = {}
    if ab and primary:
        rows = [r for r in ab if r["judge"] == primary and r["task_id"] in tset]
        L.append(f"Judge: {primary}, every output scored alone. Δ = treatment minus reference, per-task paired.\n")
        L.append("| dimension | " + " | ".join(arms) + " | " + " | ".join(f"Δ vs {r} [95% CI]" for r in refs) + " |")
        L.append("|---|" + "---|" * (len(arms) + len(refs)))
        for d in DIMS:
            pt = per_task(rows, d)
            means = {a: np.mean([v for (t, aa), v in pt.items() if aa == a]) if any(aa == a for (t, aa) in pt) else float("nan") for a in arms}
            cells = []
            summary["absolute"][d] = {"means": {a: float(means[a]) for a in arms}}
            for ref in refs:
                diffs, _, _ = paired(pt, treat, ref, tasks)
                m, lo, hi = boot(diffs)
                pos, neg, p = sign_test(diffs)
                summary["absolute"][d][f"vs_{ref}"] = {"delta": m, "ci": [lo, hi], "pct": 100 * m / means[ref] if means[ref] else None,
                                                     "better": pos, "worse": neg, "p": p}
                cells.append(f"{m:+.2f} [{lo:+.2f}, {hi:+.2f}] ({pos}↑/{neg}↓)")
            L.append(f"| {d} | " + " | ".join(fmt(means[a]) for a in arms) + " | " + " | ".join(cells) + " |")
        if len(judges) == 2:
            j2 = {(r["task_id"], r["model"], r["arm"], r["sample"]): r for r in ab if r["judge"] == judges[1] and r["task_id"] in tset}
            j1 = {(r["task_id"], r["model"], r["arm"], r["sample"]): r for r in rows}
            common = [k for k in j2 if k in j1]
            if common:
                L.append(f"\nSecond judge ({judges[1]}) on {len(common)} outputs: Spearman ρ with the primary judge: " +
                         ", ".join(f"{d} {fmt(spearman([j1[k][d] for k in common], [j2[k][d] for k in common]))}" for d in DIMS))
                L.append("\nSecond judge's own means on that subset: " + "; ".join(
                    f"{a}: " + ", ".join(f"{d[:5]} {fmt(np.mean([j2[k][d] for k in common if k[2]==a]))}" for d in ("originality", "coherence", "task_alignment"))
                    for a in arms if any(k[2] == a for k in common)))

    # 3. deterministic
    L.append("\n## 3. Judge-free metrics\n")
    L.append("Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; "
             "higher is better for semantic diversity and constraint pass rate.\n")
    po = [r for r in met.get("per_output", []) if r["task_id"] in tset]
    for r in po:
        r["constraint_pass_num"] = None if r["constraint_pass"] is None else float(r["constraint_pass"])
    pg = [r for r in met.get("per_group", []) if r["task_id"] in tset]
    cm = [r for r in met.get("cross_model", []) if r["task_id"] in tset]
    specs = [("words", po, "words"), ("constraint pass rate", po, "constraint_pass_num"),
             ("clichés /100 words (all)", po, "cliche_per100"), ("clichés /100 words (shared with skill)", po, "cliche_shared_per100"),
             ("clichés /100 words (held-out)", po, "cliche_heldout_per100"), ("typicality (cos to obvious answer)", po, "typicality"),
             ("intra-list similarity (list tasks)", po, "intra_list_sim"), ("semantic diversity across samples", pg, "semantic_diversity"),
             ("3-gram overlap across samples", pg, "ngram_overlap"), ("cross-model similarity", cm, "cross_model_sim")]
    L.append("| metric | " + " | ".join(arms) + " | " + " | ".join(f"Δ vs {r} [95% CI]" for r in refs) + " |")
    L.append("|---|" + "---|" * (len(arms) + len(refs)))
    summary["deterministic"] = {}
    for name, rows, key in specs:
        pt = per_task(rows, key)
        if not pt:
            continue
        means = {a: (np.mean([v for (t, aa), v in pt.items() if aa == a]) if any(aa == a for (t, aa) in pt) else float("nan")) for a in arms}
        cells = []
        summary["deterministic"][key] = {"means": {a: float(means[a]) for a in arms}}
        for ref in refs:
            diffs, _, _ = paired(pt, treat, ref, tasks)
            m, lo, hi = boot(diffs)
            pos, neg, p = sign_test(diffs)
            summary["deterministic"][key][f"vs_{ref}"] = {"delta": m, "ci": [lo, hi], "pct": 100 * m / means[ref] if means[ref] else None, "up": pos, "down": neg, "p": p}
            pct = f"{100*m/means[ref]:+.0f}%" if means[ref] else ""
            cells.append(f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}] {pct}")
        d = 1 if key == "words" else 3
        L.append(f"| {name} | " + " | ".join(fmt(means[a], d) for a in arms) + " | " + " | ".join(cells) + " |")

    # 4. per model
    L.append("\n## 4. Per generator model (pairwise vs baseline, both judges)\n")
    L.append("| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |")
    L.append("|---|---|---|---|---|---|---|")
    for m_ in models:
        rows = [r for r in pw if r["model"] == m_ and r["treat"] == treat and r["ref"] == "baseline" and r["task_id"] in tset]
        if not rows:
            continue
        wr = {q: np.mean([{"treat": 1, "tie": .5, "ref": 0}[r[q]] for r in rows]) for q in QUESTIONS}
        cp = {a: np.mean([r["constraint_pass"] for r in po if r["model"] == m_ and r["arm"] == a and r["constraint_pass"] is not None] or [float("nan")]) for a in (treat, "baseline")}
        L.append(f"| {m_} | " + " | ".join(f"{100*wr[q]:.0f}%" for q in QUESTIONS) + f" | {100*cp[treat]:.0f}% / {100*cp['baseline']:.0f}% |")

    # 5. per category
    L.append("\n## 5. Per category (pairwise vs baseline, both judges, both models)\n")
    L.append("| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |")
    L.append("|---|---|---|---|---|---|")
    cats = collections.defaultdict(list)
    for t in tasks:
        cats[tasks_all[t]["category"]].append(t)
    summary["categories"] = {}
    for cat, tids in sorted(cats.items()):
        rows = [r for r in pw if r["task_id"] in tids and r["treat"] == treat and r["ref"] == "baseline"]
        if not rows:
            continue
        wr = {q: np.mean([{"treat": 1, "tie": .5, "ref": 0}[r[q]] for r in rows]) for q in ("original", "prefer", "task")}
        cp = {a: [r["constraint_pass"] for r in po if r["task_id"] in tids and r["arm"] == a and r["constraint_pass"] is not None] for a in (treat, "baseline")}
        cps = " / ".join(f"{100*np.mean(cp[a]):.0f}%" if cp[a] else "n/a" for a in (treat, "baseline"))
        summary["categories"][cat] = {q: float(wr[q]) for q in wr}
        L.append(f"| {cat} | {len(tids)} | {100*wr['original']:.0f}% | {100*wr['prefer']:.0f}% | {100*wr['task']:.0f}% | {cps} |")

    # 6. failures
    L.append("\n## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)\n")
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in pw:
        if r["task_id"] in tset and r["treat"] == treat and r["ref"] == "baseline":
            for q in ("prefer", "task", "original"):
                per[r["task_id"]][q].append({"treat": 1, "tie": .5, "ref": 0}[r[q]])
    ranked = sorted(per, key=lambda t: (np.mean(per[t]["prefer"]) + np.mean(per[t]["task"])))
    fails = []
    for tid in ranked[:8]:
        whys = [r["why"] for r in pw if r["task_id"] == tid and r["treat"] == treat and r["ref"] == "baseline" and r["prefer"] == "ref"][:2]
        cfail = [r for r in po if r["task_id"] == tid and r["arm"] == treat and r["constraint_pass"] is False]
        fails.append({"task": tid, "prefer": float(np.mean(per[tid]["prefer"])), "task_win": float(np.mean(per[tid]["task"])),
                      "original": float(np.mean(per[tid]["original"])), "judge_reasons": whys,
                      "constraint_failures": [r["constraint_detail"] for r in cfail]})
        L.append(f"- **{tid}**: prefer {100*np.mean(per[tid]['prefer']):.0f}%, task {100*np.mean(per[tid]['task']):.0f}%, "
                 f"original {100*np.mean(per[tid]['original']):.0f}%. Constraint failures: {len(cfail)}. "
                 + (f"Judge: \"{whys[0]}\"" if whys else ""))
    summary["failures"] = fails
    (run_dir / f"summary_{treat}_{args.split}.json").write_text(json.dumps(summary, indent=1, default=float), encoding="utf-8")
    (run_dir / f"report_{treat}_{args.split}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
