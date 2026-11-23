# Experiment status: v4 "lean" Bohemian

**Only this tracker is committed.** Every experiment change listed below lives only in the working directory of the original machine (by the user's choice). Without that directory, restart v4 from this file: the skill on `main` is still the benchmarked v3 release.

**State:** PAUSED at 2026-11-23, by the user, because another session needs the OpenRouter credit. **Do not make API calls until the user says to resume.**

## Goal

Make Bohemian cheaper than Antialgorithm *and* more creative. v3 used about 2.6× Antialgorithm's input tokens. Judges preferred v3 slightly, but Antialgorithm won every judge-free originality measure. Background: `docs/benchmark-results.md#bohemian-vs-antialgorithm`.

## Success criteria (fixed before any v4 judging; also in `docs/devlog.md`)

On the 42-task test split:
1. v4 input tokens below Antialgorithm's (Antialgorithm: about 2,400 for DeepSeek and 3,200 for Haiku per call).
2. The stronger judge (`openai/gpt-5.4-mini`) prefers v4 over Antialgorithm head-to-head.
3. The judge-free gap to Antialgorithm narrows on clichés (all, per 100 words) and typicality.
4. v4's task-fit win rate against baseline is at least 50%.
5. v4's constraint pass rate is at least Antialgorithm's 0.884.

Revise only on the **dev** split (12 tasks). Look at the test split once, at the end.

## Working-directory changes

| Change | Revert with |
|---|---|
| `skills/bohemian/SKILL.md` rewritten as lean v4 (1,072 words, single file) | `git checkout -- skills/bohemian/SKILL.md` |
| `skills/bohemian/references/` deleted (v4 has no reference files) | `git checkout -- skills/bohemian/references` |
| `eval/results/v4/` new run: baseline, one-liner and Antialgorithm outputs and absolute scores copied from v3, plus new v4 outputs | `rm -r eval/results/v4` |
| `docs/devlog.md`: added a "v4 lean experiment" entry with the criteria | `git checkout -- docs/devlog.md` |
| `STATUS.md` (this file, committed) | `git rm STATUS.md` |

The v3 skill is also preserved in `eval/results/v3/skill_snapshot/`.

## Budget

- Spent: **USD 2.91** (see `eval/results/ledger.jsonl`). The user raised the cap from 3.00 to **4.00** for this experiment.
- The code default is still 3.00. Pass `BOHEMIAN_BUDGET_USD=4.00` on every command.
- Estimated remaining cost: finish dev about $0.08, test run about $0.45. Total stays under $4.

## Progress

- [x] Write lean v4 `SKILL.md`.
- [x] Set up the `eval/results/v4/` run with the reference arms.
- [~] Dev generation, interrupted: Antialgorithm 66 of 72 dev outputs, v4 63 of 72. Reruns skip finished outputs.
- [ ] Dev judging and metrics, then read the dev report. Revise v4 if needed, dev only. At most one or two rounds.
- [ ] Test-split generation and judging for v4.
- [ ] Stronger-judge audits on the test split.
- [ ] Check the five criteria. Token counts come from the request cache; the method is in the conversation, or recompute usage from `eval/.cache/chat` the way the v3 token comparison did.
- [ ] Update the docs (benchmark-results, README, devlog). Decide with the user: ship v4 or restore v3.
- [ ] Commit or push **only if the user asks.**

## Resume commands (run from the repo root)

```bash
export BOHEMIAN_BUDGET_USD=4.00

# 1. Finish dev generation, then judge, compute metrics and report
python3 eval/generate.py --run v4 --split dev --arms antialgorithm,bohemian --arm-label bohemian_v4 --workers 8
python3 eval/judge.py    --run v4 --pairs bohemian_v4:baseline,bohemian_v4:oneliner,bohemian_v4:antialgorithm --abs-arms bohemian_v4,antialgorithm --workers 8
python3 eval/metrics.py  --run v4
python3 eval/analyze.py  --run v4 --treat bohemian_v4 --split dev      # writes eval/results/v4/report_bohemian_v4_dev.md

# 2. If dev looks good: test split (if v4 was revised, use a new label, e.g. bohemian_v4b)
python3 eval/generate.py --run v4 --split test --arms bohemian --arm-label bohemian_v4 --workers 8
python3 eval/judge.py    --run v4 --pairs bohemian_v4:baseline,bohemian_v4:oneliner,bohemian_v4:antialgorithm --abs-arms bohemian_v4 --workers 8
python3 eval/metrics.py  --run v4
python3 eval/analyze.py  --run v4 --treat bohemian_v4 --split test
python3 eval/audit.py    --run v4 --treat bohemian_v4 --refs antialgorithm,baseline,oneliner --per-ref 40 --suffix _v4
```

## Gotchas

- **Do not rerun `metrics.py` or `analyze.py` on `v3`** while the v4 skill is in place. The cliché lexicon splits "shared" and "held-out" entries by reading the current skill text, so the saved v3 numbers would shift. Compare arms on the **all-cliché** rate, which does not depend on the skill text.
- If v4 is revised after dev results, give the new version a new `--arm-label` and snapshot it into `eval/results/v4/skill_snapshot/` (the way `v3/skill_snapshot` was made), so results map to exact text.
- `generate.py` reads the skill from `skills/bohemian/` by default (`--skill-dir` overrides).
- Tests: `python3 -m unittest discover -s tests`. Plugin check: `claude plugin validate .`.
