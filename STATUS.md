# Experiment status

**State (2026-11-23):** the shipped skill is **v4b** (`skills/bohemian/SKILL.md`, snapshot `eval/results/v4/skill_snapshot_v4b/`). Two later versions were tested and not shipped:

- **v5** ("tail pick"): more original, but both strong judges preferred Antialgorithm (46% and 40% for v5). Snapshot `eval/results/v5/skill_snapshot_v5/`.
- **v6** ("great first, then stands out"): got none of the rater's 12 blind poster picks, and no text gain. Snapshot `eval/results/v6/skill_snapshot_v6/`.

The strongest evidence so far is one rater's blind picks on posters and playable Shorts: v4b 12, Antialgorithm 5, no skill 2, other versions 1, over 20 sets (README, "Blind picks by a person"; data in `eval/results/v6/visual/`). Full history: `docs/devlog.md`. Results: `docs/benchmark-results.md`.

## Budget

USD 4.74 spent of the 4.85 cap (`eval/results/ledger.jsonl`). The code default is still 3.00; pass `BOHEMIAN_BUDGET_USD` explicitly. Another round needs the cap raised.

## Next ideas (not started)

- A blind panel of several people using the poster and Shorts review pages; this is the most trustworthy measure found so far.
- The 40-pair text review kit (`eval/human/`).
- If v4b is changed again, change it by one small step, judged by people's blind picks, not LLM judges.
- The 20 fresh tasks (`split: fresh`) are still unused.

## Gotchas

- The cliché lexicon splits "shared" and "held-out" entries by reading the current skill text, so rerunning `metrics.py` on an old run shifts those two columns. Compare arms on the **all-cliché** rate. (`eval/results/v5/metrics.json` was last computed with v6 in place.)
- `generate.py` reads the skill from `skills/bohemian/` by default; use `--skill-dir` with a snapshot and `--arm-label` for versions.
- LLM and vision judges disagreed with the human rater; calibrate any judge against human picks before trusting it.
- Tests: `python3 -m unittest discover -s tests`. Plugin check: `claude plugin validate .`.
