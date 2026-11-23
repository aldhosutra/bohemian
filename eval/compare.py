#!/usr/bin/env python3
"""Side-by-side table of skill versions from their analysis summaries.

  python3 eval/compare.py --runs v1,v2,v3 --split test
"""
import argparse
import json
from pathlib import Path

EVAL = Path(__file__).resolve().parent
QUESTIONS = ["original", "unpredictable", "distinctive", "prefer", "task"]
DET = [("constraint_pass_num", "constraint pass", 3), ("cliche_heldout_per100", "held-out clichés /100w", 3),
       ("typicality", "typicality", 3), ("semantic_diversity", "semantic diversity", 3), ("cross_model_sim", "cross-model sim", 3),
       ("words", "words", 0)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="v1,v2,v3")
    ap.add_argument("--split", default="test")
    args = ap.parse_args()
    runs = args.runs.split(",")
    S = {r: json.loads((EVAL / "results" / r / f"summary_bohemian_{args.split}.json").read_text()) for r in runs}
    out = [f"### Pairwise win rate of Bohemian, {args.split} split (both cheap judges; 95% CI over tasks)\n"]
    for ref in ("baseline", "oneliner"):
        out.append(f"\n**vs {ref}**\n\n| question | " + " | ".join(runs) + " |\n|---|" + "---|" * len(runs))
        for q in QUESTIONS:
            cells = []
            for r in runs:
                v = S[r]["pairwise"][ref][q]
                cells.append(f"{100*v['win_rate']:.0f}% [{100*v['ci'][0]:.0f}–{100*v['ci'][1]:.0f}]")
            out.append(f"| {q} | " + " | ".join(cells) + " |")
    out.append(f"\n**Judge-free metrics (Bohemian arm; baseline / one-liner for reference)**\n\n| metric | baseline | oneliner | " + " | ".join(runs) + " |\n|---|---|---|" + "---|" * len(runs))
    for key, name, d in DET:
        m0 = S[runs[-1]]["deterministic"][key]["means"]
        out.append(f"| {name} | {m0['baseline']:.{d}f} | {m0['oneliner']:.{d}f} | " + " | ".join(f"{S[r]['deterministic'][key]['means']['bohemian']:.{d}f}" for r in runs) + " |")
    audits = {r: EVAL / "results" / r / "audit_summary.json" for r in runs}
    if any(p.exists() for p in audits.values()):
        out.append("\n**Stronger-judge audit (openai/gpt-5.4-mini) on a random test-split subset**\n\n| run | reference | " + " | ".join(QUESTIONS) + " |\n|---|---|" + "---|" * len(QUESTIONS))
        for r, p in audits.items():
            if p.exists():
                a = json.loads(p.read_text())
                for ref, by in a.items():
                    wr = by.get("openai/gpt-5.4-mini")
                    if wr:
                        out.append(f"| {r} | {ref} | " + " | ".join(f"{100*wr[q]:.0f}%" for q in QUESTIONS) + " |")
    print("\n".join(out))


if __name__ == "__main__":
    main()
