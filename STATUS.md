# Experiment status: v4 "lean" Bohemian

**Only this tracker is committed.** Every experiment change listed below lives only in the working directory of the original machine (by the user's choice). Without that directory, restart v4 from this file: the skill on `main` is still the benchmarked v3 release.

**State:** v4b is the shipped skill (user decision), docs updated, not committed. **Next: v5, aimed at beating Antialgorithm clearly.** Plan below. Waiting for the user to approve the budget for v5.

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

- Spent: **USD 3.55** (see `eval/results/ledger.jsonl`). The user raised the cap from 3.00 to **4.00** for this experiment.
- The code default is still 3.00. Pass `BOHEMIAN_BUDGET_USD=4.00` on every command.
- The planned experiment is complete. USD 0.45 remains under the cap.

## Progress

- [x] Lean v4 `SKILL.md` written (snapshot: `eval/results/v4/skill_snapshot_v4/`).
- [x] Dev run of v4. Problem found: rewrites overran their length (constraint pass 89%).
- [x] One revision, **v4b** (the plan's first line now asks for the target length as a number). Dev constraint pass 97%. Snapshot: `eval/results/v4/skill_snapshot_v4b/`. This is the text now in `skills/bohemian/`.
- [x] Test-split run of v4b, judging, metrics and stronger-judge audit (`report_bohemian_v4b_test.md`, `audit_v4b.md`).
- [x] Fixed `tests/test_eval.py`, which assumed the skill text contains "tapestry". All 16 tests pass.
- [x] User decision: ship v4b. Docs updated (README, benchmark-results, architecture, methodology, evaluation, research, CONTRIBUTING); plugin version 0.2.0.
- [ ] Commit or push **only if the user asks.**

## Result: v4b against the criteria (test split, 42 tasks)

| # | Criterion | Result | |
|---|---|---|---|
| 1 | Input tokens below Antialgorithm's | 1,624 / 2,318 vs 2,422 / 3,236 (DeepSeek / Haiku); cost per call 15% / 9% lower | pass |
| 2 | Stronger judge prefers v4b over Antialgorithm | 48% (n=40). Cheap judges: 56.6% [51.9–61.5] | **fail** (even) |
| 3 | Judge-free gap to Antialgorithm narrows | typicality gap 0.057 → 0.033; all-cliché gap 0.179 → 0.153; diversity gap −0.047 → −0.004 | pass |
| 4 | Task fit vs baseline ≥ 50% | cheap judges 45.1% [40.1–49.9]; stronger judge 65% | **mixed** |
| 5 | Constraint pass ≥ 0.884 | 0.949, the best of all arms (baseline 0.940) | pass |

v4b vs v3: about 3.8× fewer input tokens; length now equal to baseline (v3 was +20%); better on every judge-free measure and on constraint pass. Judged preference: vs baseline 68% vs 73%, vs one-liner 33% vs 37%, stronger judge vs one-liner 48% vs 55%. Spend after the run: USD 3.55 of the 4.00 cap.

## Next: v5 plan (research notes in `docs/research.md`, "Research for v5")

Changes to test, one at a time on dev where possible:
1. **Tail pick:** plan lists 5 candidate directions with a rough probability that a typical model would write each, and picks from those under about 10% that still pass the brief (Verbalized Sampling).
2. **Script-free seed:** the plan begins with a short random string that steers the choice among tail candidates and the names and setting (String Seed of Thought).
3. **Names:** write down the first three names that come to mind and use none of them. Fixes "Mara" and "Vance".
4. **No named clichés in the skill text** (remove "embers, tides, lanterns, salt"): they may plant the words.

Bar for "clearly better than Antialgorithm", to be fixed before v5 judging:
- the stronger judge prefers v5 at least 60%, with the 95% CI above 50%, on at least 120 test pairs; plus a second strong judge from another family that agrees;
- typicality, diversity and all-cliché rate at least as good as Antialgorithm's;
- task fit vs Antialgorithm at least 50%; input tokens still below Antialgorithm's;
- confirmed on about 20 **new** tasks never used before (the 42-task test split has now been looked at for three comparisons);
- ideally, the blind human review (`eval/human/`).

Estimated cost about USD 1.10 (two dev rounds, test run, larger audits, new tasks). Needs the cap raised to about 5.00.

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
