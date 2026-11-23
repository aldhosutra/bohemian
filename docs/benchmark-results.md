# Benchmark results

*Run 2026-11-23. Method: [`evaluation.md`](evaluation.md). Raw data: `eval/results/{v1,v2,v3,v4}/`. Per-run reports: `report_bohemian_{all,test,dev}.md`. Total API spend for all of it: **USD 3.55**.*

## Summary

**Current version: v4b**, a 1,090-word single-file rewrite of v3. On the 42 test tasks it uses about 3.8× fewer input tokens than v3 and about 30% fewer than Antialgorithm. It matches baseline length, has the best hard-limit pass rate of any arm (94.9%), and beats v3 on every judge-free measure. Judged preference is within a few points of v3: 68% vs baseline, 33% vs the one-liner, 57% vs Antialgorithm (the stronger judge: 85%, 48%, 48%). Its weakness is task fit by the cheap judges (45% vs baseline; the stronger judge gives 65%). Details in "v4: the lean rewrite" below.

The numbered findings below are for v3, the version benchmarked first. On 42 held-out test tasks, two generator models, and 3 samples per cell:

1. **Bohemian beats the same model with no skill.** In blinded pairwise comparison, judges preferred the Bohemian output **73%** of the time [95% CI 65–80], found it more distinctive **80%** [73–86] and less predictable **82%** [76–88]. Task fit was **unchanged** (53% [48–57]). Bohemian roughly halves cliché density, *including clichés the skill never names* (−50% held-out). Its outputs are 18% further from an "obvious answer" anchor, and 48% more varied across samples.
2. **Bohemian does not beat a one-line "be original" instruction according to the two cheap judges.** They preferred the one-liner's output (Bohemian prefer rate 37% [31–43]). A stronger judge, run on a random 40-pair subset, called it roughly even (Bohemian preferred 55%, task 56%; n=40, so the interval is wide). On judge-free measures Bohemian is slightly further from the obvious answer than the one-liner (typicality −3% [−5, −1]) and converges less across models (−5% [−8, −2]). Its cliché, diversity and specificity numbers are statistically indistinguishable from the one-liner's.
3. **Costs:** Bohemian misses hard length limits more often than baseline (89.8% vs 94.0% constraint pass), and its outputs are 20% longer. Judges favor longer outputs, which inflates part of the preference win. In length-matched pairs it still beats baseline (70%) and still loses to the one-liner (33%).
4. **Fiction is the weak category.** Against baseline, Bohemian's flash fiction is preferred only 42% of the time.
5. **Bohemian vs Antialgorithm (the skill it builds on): no clear winner, different strengths.** Head-to-head, the cheap judges preferred Bohemian 59% [52–65]; the stronger judge called it even (52%, n=40). Against the same references, judges rated Antialgorithm lower than Bohemian (vs baseline 61% vs 73% prefer, with task fit dropping to 43%; vs the one-liner 27% vs 37%; stronger judge 38% vs 55%). But Antialgorithm wins every judge-free originality measure: far fewer clichés, further from the obvious answer, more varied, and 20% shorter. Details below.
6. **No human evaluation has been run.** Every judgment above comes from LLM judges or automatic metrics. The blind human-review kit is built and tested; see "Human evaluation" below.

The honest bottom line: Bohemian reliably makes a model's creative output less predictable, less clichéd and more distinctive than default prompting, at the same task fit and coherence. Whether it beats a well-phrased one-line instruction is **not established**. The cheap judges say no, the stronger judge says roughly even, and no humans have weighed in.

## Setup

| | |
|---|---|
| Tasks | 54 (12 categories; 42 with deterministic constraints). Test split 42, dev split 12 |
| Generators | `deepseek/deepseek-v4.1-flash`, `anthropic/claude-haiku-5.5`; temperature 1.0, max_tokens 4000, reasoning off |
| Samples | 3 per (task, model, arm). 972 generations per run |
| Arms | baseline, one-liner, Bohemian. Only the system prompt differs; every arm is told to plan briefly in notes before a `<final>` block |
| Pairwise judges | `google/gemini-2.5-flash-lite`, `openai/gpt-4o-mini` (temperature 0, blind, randomized A/B). 2,592 judgments per run |
| Audit judge | `openai/gpt-5.4-mini` on 40–60 random test-split pairs per reference |
| Statistics | per-task paired; 95% bootstrap CI over tasks; exact sign tests |

## Versions tested

| Version | What changed | Why (all from dev-split evidence) |
|---|---|---|
| v1 | initial skill | — |
| v2 | steps declared non-optional; "original *and* good" + payoff test; "specific ≠ quiet"; list order is not a ranking, the bystander narrator named as a default; create mode returns one piece; count before showing; mode inferred from the request | Haiku skipped the method in 110/162 outputs; "displaced witness" appeared in 12 of 44 dev plans; Haiku returned 3 taglines when asked for one; rewrites overran length |
| v3 | an anchor is a launch point and the leap can be large; replaced "never ask what would be interesting" with "find the first interesting idea and go past it"; choose the strongest hook; restraint is not a house style; make it fully realized; never leak notes | the stronger judge's reasons on dev: Bohemian read as "smart but internally literary", "a premise sketch", while the one-liner was "more vivid", with "a stronger, more unusual premise"; one output leaked notes |
| v4 | single 1,072-word file: five-line plan, five-family table with cheap versions, short stock-move list instead of a cliché catalog, one paragraph per mode; names from the piece's world, numbers only when needed, endings that stop; never longer than the brief | v3 cost 2.6× Antialgorithm's input tokens for a small judged edge, and lost to it on every judge-free measure |
| v4b | the plan's first line asks for the target length as a number (for a rewrite, the original's word count) | v4 dev constraint pass 89%: rewrites ran to 2–3× the original's length |

An ablation on dev (SKILL.md alone, no reference files) did **not** do better against the one-liner (prefer 24% vs 31% for full v2), so the long lists of tells were not the problem.

## Results by version, test split (42 tasks)

Pairwise win rate of Bohemian (ties count half; both cheap judges; 95% CI over tasks):

| vs baseline | v1 | v2 | v3 | v4b |
|---|---|---|---|---|
| original | 61% [55–68] | 64% [57–71] | 65% [58–72] | 61% [54–68] |
| unpredictable | 77% [71–82] | 79% [73–85] | 82% [76–88] | 81% [74–87] |
| distinctive | 72% [66–77] | 75% [69–82] | 80% [73–86] | 75% [68–83] |
| prefer | 64% [58–71] | 70% [62–77] | **73% [65–80]** | 68% [60–76] |
| task | 51% [46–55] | 53% [48–58] | 53% [48–57] | 45% [40–50] |

| vs one-liner | v1 | v2 | v3 | v4b |
|---|---|---|---|---|
| original | 39% [34–45] | 39% [34–45] | 44% [38–49] | 47% [42–52] |
| unpredictable | 25% [20–30] | 29% [24–34] | 35% [29–41] | 34% [29–39] |
| distinctive | 26% [21–31] | 28% [22–34] | 38% [31–44] | 35% [30–40] |
| prefer | 26% [21–32] | 31% [25–38] | **37% [31–43]** | 33% [28–38] |
| task | 37% [32–42] | 40% [35–45] | 42% [36–47] | 39% [35–44] |

Stronger-judge audit (`gpt-5.4-mini`), random test-split pairs:

| | n | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|
| v2 vs baseline | 60 | 88% | 97% | 95% | 82% | 70% |
| v2 vs one-liner | 60 | 42% | 42% | 42% | 38% | 41% |
| v3 vs baseline | 40 | 90% | 98% | 100% | 92% | 61% |
| v3 vs one-liner | 40 | 49% | 38% | 48% | **55%** | 56% |
| v4b vs baseline | 40 | 88% | 95% | 95% | 85% | 65% |
| v4b vs one-liner | 40 | 48% | 45% | 48% | 48% | 48% |
| v4b vs Antialgorithm | 40 | 41% | 42% | 40% | 48% | 52% |

## v3 in detail, test split

### Pairwise (both cheap judges)

| vs baseline | win rate [95% CI] | W / T / L | tasks above / below 50% | sign test p |
|---|---|---|---|---|
| original | 65.2% [58.0, 72.3] | 327 / 3 / 174 | 25 / 9 | 0.009 |
| unpredictable | 82.2% [76.2, 88.0] | 412 / 5 / 87 | 37 / 2 | 3e-09 |
| distinctive | 79.9% [73.3, 85.8] | 401 / 3 / 100 | 36 / 3 | 4e-08 |
| prefer | 72.7% [65.2, 80.2] | 365 / 3 / 136 | 33 / 6 | 1e-05 |
| task | 52.7% [48.3, 56.7] | 203 / 125 / 176 | 21 / 16 | 0.51 |

| vs one-liner | win rate [95% CI] | W / T / L | tasks above / below 50% | sign test p |
|---|---|---|---|---|
| original | 43.7% [38.4, 48.8] | 219 / 2 / 283 | 12 / 21 | 0.16 |
| unpredictable | 35.3% [29.5, 41.4] | 177 / 2 / 325 | 9 / 27 | 0.004 |
| distinctive | 37.9% [31.3, 44.4] | 190 / 2 / 312 | 9 / 26 | 0.006 |
| prefer | 36.8% [30.6, 43.4] | 185 / 1 / 318 | 8 / 30 | 0.0005 |
| task | 41.6% [36.1, 46.9] | 154 / 111 / 239 | 10 / 28 | 0.005 |

### Absolute scores, 1–5 (Gemini, every output scored alone)

| | baseline | one-liner | Bohemian | Δ vs baseline [95% CI] | Δ vs one-liner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 4.06 | +0.85 [+0.73, +0.98] (+27%) | −0.07 [−0.14, 0.00] |
| specificity | 3.90 | 4.56 | 4.58 | +0.68 [+0.53, +0.84] (+17%) | +0.02 [−0.07, +0.10] |
| distinctiveness | 3.28 | 4.18 | 4.16 | +0.88 [+0.74, +1.04] (+27%) | −0.02 [−0.09, +0.06] |
| coherence | 5.00 | 5.00 | 5.00 | 0.00 | 0.00 |
| task alignment | 5.00 | 5.00 | 4.99 | −0.01 [−0.02, 0.00] | −0.01 [−0.02, 0.00] |
| creative risk | 2.34 | 3.35 | 3.31 | +0.98 [+0.79, +1.17] (+42%) | −0.03 [−0.14, +0.07] |

Coherence and task alignment sit at the ceiling for every arm. This judge does not separate them, so they show no loss rather than proving none exists. The second judge (GPT-4o-mini, 252 outputs) ranks outputs similarly: Spearman ρ 0.60 for originality, 0.71 for specificity, 0.64 for distinctiveness, 0.74 for creative risk.

### Judge-free metrics

| metric | baseline | one-liner | Bohemian | Δ vs baseline [95% CI] | Δ vs one-liner [95% CI] |
|---|---|---|---|---|---|
| clichés /100 words, all | 0.437 | 0.279 | 0.205 | −0.232 [−0.362, −0.123] (−53%) | −0.074 [−0.210, +0.027] |
| clichés /100 words, shared with skill | 0.095 | 0.054 | 0.034 | −0.061 [−0.133, −0.001] (−64%) | −0.020 [−0.056, +0.014] |
| clichés /100 words, **held out** | 0.342 | 0.225 | 0.171 | −0.171 [−0.294, −0.079] (−50%) | −0.054 [−0.190, +0.040] |
| typicality (cos to obvious answer) ↓ | 0.737 | 0.626 | 0.605 | −0.131 [−0.148, −0.116] (−18%) | −0.021 [−0.033, −0.008] (−3%) |
| semantic diversity across samples ↑ | 0.187 | 0.267 | 0.276 | +0.089 [+0.068, +0.111] (+48%) | +0.008 [−0.008, +0.025] |
| 3-gram overlap across samples ↓ | 0.056 | 0.015 | 0.017 | −0.039 [−0.067, −0.019] (−70%) | +0.001 [−0.002, +0.006] |
| cross-model similarity ↓ | 0.749 | 0.680 | 0.648 | −0.102 [−0.130, −0.075] (−14%) | −0.032 [−0.051, −0.014] (−5%) |
| similarity between items in one list ↓ | 0.428 | 0.356 | 0.360 | −0.068 [−0.128, −0.014] (−16%) | +0.004 [−0.014, +0.026] |
| constraint pass rate ↑ | 0.940 | 0.870 | 0.898 | −0.042 [−0.083, −0.005] (−4%) | +0.028 [−0.028, +0.088] |
| words | 169 | 194 | 203 | +34 [+19, +50] (+20%) | +9 [−3, +21] |

v2 was slightly better than v3 on the judge-free divergence measures (held-out clichés 0.137, semantic diversity 0.301), and v3 was better on the judges. v3's push toward vivid, fully realized pieces bought judge preference with a little divergence and some length.

### Per model (v3 vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (Bohemian / baseline) |
|---|---|---|---|---|---|---|
| claude-haiku-5.5 | 66% | 77% | 76% | 70% | 54% | 87% / 90% |
| deepseek-v4.1-flash | 65% | 88% | 84% | 75% | 52% | 93% / 98% |

Even with v2's wording, Haiku wrote planning notes in only 4 of 36 dev outputs when thinking was off. DeepSeek planned every time. Haiku still improved, so part of the effect comes from the skill text alone, without the method being run step by step.

### Per category (v3 vs baseline, prefer)

| brainstorm | headlines | marketing | naming | positioning | story concept | analogy | poetry | short story | rewrite | character | fiction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100% | 92% | 85% | 83% | 81% | 75% | 74% | 67% | 65% | 56% | 53% | **42%** |

## Bohemian vs Antialgorithm

Added after v3 at the user's request. [Antialgorithm](https://github.com/mankidev/antialgorithm) (commit `a6392c0`, MIT) ran as a fourth arm on the 42 test tasks, with the same models, settings, wrapper and judges. Its `SKILL.md` is used unmodified (`eval/competitors/antialgorithm/`), in the same preamble as Bohemian. `visuals.md` was left out, because the skill says to read it only for visual work and every task is text. Raw data: `eval/results/v3/` (`report_antialgorithm_test.md`, `audit_antialgorithm*.md`).

**Decision rule, written before any judging:** switch to Antialgorithm if, on the test split, the cheap judges prefer it head-to-head with a CI entirely above 50%, the stronger judge agrees, and it is not worse on task fit or constraint pass.

**Head-to-head (Bohemian's win rate):**

| | cheap judges [95% CI] | stronger judge (n=40) |
|---|---|---|
| prefer | 58.8% [52.1–65.3] | 52% |
| original | 52.3% [46.1–58.3] | 49% |
| distinctive | 55.2% [48.5–61.7] | 50% |
| task | 54.1% [48.8–59.1] | 54% |

Bohemian is 20% longer than Antialgorithm. By length bucket: Bohemian longer → 70% prefer (n=224); within 10% → 61% (n=154); shorter → 37% (n=126). Part of the cheap judges' 59% is length.

**Against the shared references (prefer / task win rate of each skill):**

| | Antialgorithm | Bohemian |
|---|---|---|
| vs baseline, cheap judges | 61% / 43% | 73% / 53% |
| vs baseline, stronger judge (n=40) | 82% / 69% | 92% / 61% |
| vs one-liner, cheap judges | 27% / 36% | 37% / 42% |
| vs one-liner, stronger judge (n=40) | 38% / 32% | 55% / 56% |

**Judge-free (test split):**

| | baseline | one-liner | Antialgorithm | Bohemian |
|---|---|---|---|---|
| words | 169 | 194 | 169 | 203 |
| constraint pass | 0.940 | 0.870 | 0.884 | 0.898 |
| clichés /100 words (all) | 0.437 | 0.279 | **0.026** | 0.205 |
| typicality (lower = further from obvious) | 0.737 | 0.626 | **0.549** | 0.605 |
| semantic diversity across samples | 0.187 | 0.267 | **0.323** | 0.276 |
| cross-model similarity | 0.749 | 0.680 | **0.618** | 0.648 |
| intra-list similarity | 0.428 | 0.356 | **0.333** | 0.360 |

All Antialgorithm-vs-Bohemian differences in this table are significant except constraint pass (+1.4 points for Bohemian [−3.7, +6.0]). Antialgorithm's skill text names only one of the 162 lexicon entries, so its cliché rate is effectively all held-out for it. About half of the gap in raw hits (44 vs 20) is stock character names: Bohemian outputs used "Maya" 10 times and "Mara" 3 times across the test split, Antialgorithm used "Maya" once. Both still sprinkle exact clock times (12 and 14 hits).

**Outcome:** the rule's first condition fails (judges prefer Bohemian head-to-head, or call it even), so Bohemian stays. That is not a win for Bohemian either. Antialgorithm moves further from the default by every automatic measure, and judges find it slightly less satisfying and sometimes less on-brief. The two skills sit at different points of the same trade-off: Antialgorithm diverges more, Bohemian holds the brief and the payoff a little better. Neither is shown to beat the one-line instruction on judged quality.

## v4: the lean rewrite

Run `eval/results/v4/`, reusing the baseline, one-liner and Antialgorithm outputs from v3, so every arm saw identical tasks and settings. v4 was revised once on dev (to v4b), then run once on test. Success criteria were written down before any v4 judging (`docs/devlog.md`).

**Tokens and cost per call, test split:**

| | input (DeepSeek / Haiku) | output | cost per 1,000 calls |
|---|---|---|---|
| Antialgorithm | 2,422 / 3,236 | 487 / 368 | $0.44 / $0.51 |
| Bohemian v3 | 6,058 / 8,836 | 603 / 393 | $0.61 / $1.08 |
| **Bohemian v4b** | **1,624 / 2,318** | 445 / 459 | **$0.38 / $0.46** |

**Judge-free, test split:**

| | baseline | one-liner | Antialgorithm | v3 | **v4b** |
|---|---|---|---|---|---|
| words | 169 | 194 | 169 | 203 | 173 |
| constraint pass | 0.940 | 0.870 | 0.884 | 0.898 | **0.949** |
| clichés /100 words (all) | 0.437 | 0.279 | **0.026** | 0.205 | 0.179 |
| typicality | 0.737 | 0.626 | **0.549** | 0.605 | 0.582 |
| semantic diversity | 0.187 | 0.267 | **0.323** | 0.276 | 0.319 |
| cross-model similarity | 0.749 | 0.680 | **0.618** | 0.648 | 0.638 |
| intra-list similarity | 0.428 | 0.356 | **0.333** | 0.360 | 0.354 |

**v4b vs Antialgorithm, head-to-head:** cheap judges prefer v4b 56.6% [51.9–61.5] (24 tasks above 50%, 11 below; p = 0.04), task 50.4%. Both are now the same length, so this is not a length effect. Stronger judge: 48% (n=40).

**Criteria:**

| # | Criterion | Result |
|---|---|---|
| 1 | input tokens below Antialgorithm's | pass |
| 2 | stronger judge prefers v4b over Antialgorithm | fail (48%, even) |
| 3 | judge-free gap to Antialgorithm narrows | pass (typicality gap 0.057 → 0.033, diversity gap closed) |
| 4 | task fit vs baseline ≥ 50% | mixed (cheap judges 45%, stronger judge 65%) |
| 5 | constraint pass ≥ Antialgorithm's | pass (0.949) |

**Other observations:** Haiku wrote its plan in 92 of 162 v4b outputs, more than in any earlier version. Weakest categories vs baseline: character (39% prefer), fiction (40%), poetry (52%). Short stories now miss length limits more than baseline (67% vs 92%).

## Known measurement problems

- **Length bias.** v3 vs baseline, by relative length of the pair: Bohemian longer by >10% → prefer 81% (n=262); similar length → 70% (n=150); Bohemian shorter → 54% (n=92). Against the one-liner: 54% / 33% / 19%. Judges were told not to reward length and plainly still do. The length-matched numbers (70% vs baseline, 33% vs one-liner) are the cleanest estimate.
- **Position bias.** Gemini and GPT-4o-mini favor whichever response is shown first. v3 vs baseline: 82% when Bohemian was A, 62% when it was B. Assignment is balanced by hash, so the bias cancels in the averages but adds variance.
- **Judge taste.** The cheap judges reward ornamental, "evocative" language. The stronger audit judge was much more favorable to Bohemian against the one-liner than they were (55% vs about 30% prefer), with only 57–67% `prefer` agreement between them. Cheap judges disagree with each other on task fit (κ = 0.20).
- **Ceiling effects.** Absolute coherence and task alignment are 5.00 for almost everything.
- **Embedding nondeterminism.** Re-embedding identical baseline texts in a different batch moved typicality in the third decimal (0.740 vs 0.737).
- **The one-liner arm's word choice.** "Be original: avoid cliches and look past the first, most obvious idea" is a strong one-liner, deliberately. A weaker one-liner would flatter Bohemian.

## Failure cases (v3, test split, chosen by the report's automatic ranking)

| task | prefer vs baseline | what the judges said |
|---|---|---|
| fiction-5 (opening paragraph of a novel about a closing hardware store) | 0% | "Response A establishes a stronger sense of place and character, while Response B feels a bit more generic and less evocative." |
| character-4 (mentor character, about 150 words) | 25% | "Response A feels more fully realized, with a stronger sense of character." |
| rewrite-3 (make a sad passage vivid, same events) | 33% | 2 of 6 outputs over the word limit; "Response A is more vivid… stronger imagery." |
| story_concept-2 (heist premise) | 42% | "Response B's premise, though interesting, feels slightly less grounded and more predictable." |
| fiction-2 (siblings divide a kitchen, under 300 words) | 33% | "Response A better satisfies the specific task of dividing up items in the kitchen." |
| poetry-3 (city at night) | 50% | "Response B feels like a prose piece broken into lines, and its meta-commentary about the brief is unnecessary." |

Full texts of fiction-5 are in [`examples.md`](examples.md#failure-case). A recurring pattern: when the brief is a small, emotionally loaded scene, Bohemian's sideways angle reads as less immersive than the direct version.

## Spend

| | USD |
|---|---|
| Generation (3 full runs + 2 dev iterations + smoke tests) | 1.16 |
| Judging (pairwise, absolute, self-tests, audits) | 1.19 |
| Anchors + embeddings | 0.04 |
| Antialgorithm comparison (generation 0.12, judging and audits 0.33) | 0.45 |
| v4 / v4b (dev and test generation, judging, audits) | 0.71 |
| **Total** | **3.55** of the 4.00 cap (raised from 3.00 by the user for v4) |

## Human evaluation

**Not run.** `eval/human/build.py --run v3 --pairs 40` produces a blind review page and a separate key, and `eval/human/score.py` computes preference rates, sign tests and Fleiss' κ from reviewers' answer files. The kit is tested with a synthetic rater. Until human ratings exist, every claim on this page rests on LLM judges and automatic metrics, with the biases listed above.

## Reproducing

```bash
python3 eval/compare.py --runs v1,v2,v3 --split test   # the version tables above, from saved summaries
python3 eval/analyze.py --run v3 --split test          # the v3 detail tables
```

Both read saved results and make no API calls. Regenerating outputs needs an `OPENROUTER_API_KEY`. The request cache (`eval/.cache/`, 213 MB) is not committed, so a fresh rerun pays again (about USD 0.80 per full run). Because sampling at temperature 1.0 is not deterministic, it will give similar but not identical numbers.
