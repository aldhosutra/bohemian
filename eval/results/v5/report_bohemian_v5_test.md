# Benchmark report: run `v5`, split `test`, treatment `bohemian_v5`

- Tasks: 42  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian_v4b, bohemian_v5  
- Generations analysed: 1260  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 1258/1260

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v5 vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 62.1% [55.9, 68.5] | 311 / 4 / 189 | 24 / 9 | 0.014 |
| unpredictable | 79.3% [72.6, 85.5] | 398 / 3 / 103 | 34 / 5 | 2.4e-06 |
| distinctive | 76.9% [70.4, 83.0] | 386 / 3 / 115 | 34 / 4 | 6e-07 |
| prefer | 66.8% [60.3, 73.4] | 335 / 3 / 166 | 29 / 9 | 0.0017 |
| task | 46.7% [43.1, 50.5] | 170 / 131 / 203 | 13 / 25 | 0.073 |

- google/gemini-2.5-flash-lite: original 66%, unpredictable 92%, distinctive 91%, prefer 84%, task 62%

- openai/gpt-4o-mini: original 58%, unpredictable 67%, distinctive 62%, prefer 49%, task 32%
- Position check (prefer): treatment win rate 71% when shown as A (n=246), 63% when shown as B (n=258).

### bohemian_v5 vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 42.2% [36.9, 47.5] | 210 / 5 / 289 | 10 / 26 | 0.011 |
| unpredictable | 37.4% [31.7, 43.1] | 186 / 5 / 313 | 10 / 29 | 0.0034 |
| distinctive | 35.4% [29.9, 41.0] | 176 / 5 / 323 | 7 / 29 | 0.00031 |
| prefer | 34.5% [29.0, 40.5] | 172 / 4 / 328 | 6 / 32 | 2.4e-05 |
| task | 39.4% [34.8, 44.1] | 145 / 107 / 252 | 6 / 33 | 1.4e-05 |

- google/gemini-2.5-flash-lite: original 42%, unpredictable 44%, distinctive 42%, prefer 41%, task 40%

- openai/gpt-4o-mini: original 42%, unpredictable 31%, distinctive 29%, prefer 28%, task 39%
- Position check (prefer): treatment win rate 59% when shown as A (n=240), 12% when shown as B (n=264).

### bohemian_v5 vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 55.9% [51.0, 60.5] | 281 / 1 / 222 | 21 / 9 | 0.043 |
| unpredictable | 57.2% [51.9, 62.5] | 288 / 1 / 215 | 24 / 9 | 0.014 |
| distinctive | 57.5% [52.0, 62.9] | 289 / 2 / 213 | 26 / 9 | 0.006 |
| prefer | 58.5% [53.4, 63.5] | 295 / 0 / 209 | 29 / 7 | 0.00031 |
| task | 54.0% [49.3, 58.5] | 221 / 102 / 181 | 21 / 15 | 0.41 |

- google/gemini-2.5-flash-lite: original 55%, unpredictable 53%, distinctive 54%, prefer 54%, task 52%

- openai/gpt-4o-mini: original 57%, unpredictable 61%, distinctive 61%, prefer 63%, task 56%
- Position check (prefer): treatment win rate 76% when shown as A (n=268), 39% when shown as B (n=236).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 84% | 0.69 |
| unpredictable | 69% | 0.37 |
| distinctive | 69% | 0.38 |
| prefer | 68% | 0.38 |
| task | 45% | 0.22 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian_v4b | bohemian_v5 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 4.04 | 4.03 | 4.12 | +0.91 [+0.77, +1.05] (41↑/0↓) | -0.01 [-0.12, +0.11] (15↑/19↓) | +0.08 [-0.01, +0.17] (22↑/12↓) |
| specificity | 3.90 | 4.56 | 4.58 | 4.54 | 4.56 | +0.66 [+0.48, +0.84] (36↑/1↓) | +0.00 [-0.13, +0.11] (15↑/12↓) | -0.02 [-0.08, +0.04] (12↑/13↓) |
| distinctiveness | 3.28 | 4.18 | 4.13 | 4.11 | 4.19 | +0.91 [+0.75, +1.07] (40↑/0↓) | +0.01 [-0.09, +0.10] (14↑/17↓) | +0.06 [-0.02, +0.14] (17↑/15↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | 4.99 | -0.01 [-0.04, +0.00] (0↑/1↓) | -0.01 [-0.04, +0.00] (0↑/1↓) | -0.01 [-0.04, +0.00] (0↑/1↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | 4.99 | 4.97 | -0.03 [-0.07, +0.00] (0↑/3↓) | -0.03 [-0.07, +0.00] (0↑/3↓) | -0.02 [-0.06, +0.02] (2↑/3↓) |
| creative_risk | 2.34 | 3.35 | 3.31 | 3.31 | 3.37 | +1.03 [+0.83, +1.24] (40↑/0↓) | +0.02 [-0.13, +0.17] (16↑/19↓) | +0.06 [-0.08, +0.19] (20↑/13↓) |

Second judge (openai/gpt-4o-mini) on 420 outputs: Spearman ρ with the primary judge: originality 0.56, specificity 0.61, distinctiveness 0.57, coherence 1.00, task_alignment 0.66, creative_risk 0.65

Second judge's own means on that subset: baseline: origi 4.15, coher 5.00, task_ 5.00; oneliner: origi 4.69, coher 5.00, task_ 5.00; antialgorithm: origi 4.51, coher 5.00, task_ 4.98; bohemian_v4b: origi 4.60, coher 5.00, task_ 5.00; bohemian_v5: origi 4.71, coher 4.98, task_ 4.99

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian_v4b | bohemian_v5 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| words | 169.2 | 194.1 | 169.1 | 172.8 | 181.9 | +12.742 [+2.135, +27.167] +8% | -12.214 [-25.536, -0.294] -6% | +12.813 [-4.861, +37.009] +8% |
| constraint pass rate | 0.940 | 0.870 | 0.884 | 0.949 | 0.926 | -0.014 [-0.046, +0.014] -1% | +0.056 [-0.000, +0.116] +6% | +0.042 [+0.009, +0.079] +5% |
| clichés /100 words (all) | 0.437 | 0.279 | 0.026 | 0.179 | 0.190 | -0.248 [-0.610, +0.039] -57% | -0.090 [-0.338, +0.075] -32% | +0.164 [+0.044, +0.330] +627% |
| clichés /100 words (shared with skill) | 0.039 | 0.013 | 0.015 | 0.010 | 0.060 | +0.020 [-0.058, +0.094] +51% | +0.047 [-0.001, +0.107] +354% | +0.045 [-0.003, +0.106] +308% |
| clichés /100 words (held-out) | 0.398 | 0.266 | 0.011 | 0.169 | 0.130 | -0.268 [-0.624, +0.014] -67% | -0.136 [-0.370, +0.001] -51% | +0.118 [+0.019, +0.285] +1034% |
| typicality (cos to obvious answer) | 0.737 | 0.626 | 0.549 | 0.582 | 0.571 | -0.166 [-0.185, -0.148] -23% | -0.056 [-0.070, -0.041] -9% | +0.022 [+0.007, +0.037] +4% |
| intra-list similarity (list tasks) | 0.428 | 0.356 | 0.333 | 0.354 | 0.348 | -0.080 [-0.145, -0.025] -19% | -0.008 [-0.026, +0.007] -2% | +0.015 [-0.002, +0.031] +4% |
| semantic diversity across samples | 0.187 | 0.267 | 0.323 | 0.319 | 0.335 | +0.149 [+0.124, +0.173] +80% | +0.068 [+0.050, +0.087] +25% | +0.012 [-0.009, +0.033] +4% |
| 3-gram overlap across samples | 0.056 | 0.015 | 0.012 | 0.010 | 0.011 | -0.045 [-0.073, -0.024] -80% | -0.004 [-0.008, +0.001] -26% | -0.001 [-0.004, +0.003] -6% |
| cross-model similarity | 0.749 | 0.680 | 0.618 | 0.638 | 0.619 | -0.130 [-0.165, -0.097] -17% | -0.060 [-0.079, -0.042] -9% | +0.001 [-0.020, +0.022] +0% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 62% | 74% | 72% | 62% | 44% | 91% / 90% |
| deepseek/deepseek-v4.1-flash | 63% | 84% | 82% | 71% | 50% | 94% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 3 | 64% | 71% | 57% | 100% / 100% |
| brainstorm | 4 | 75% | 90% | 55% | 100% / 100% |
| character | 3 | 47% | 47% | 39% | 92% / 100% |
| fiction | 4 | 50% | 46% | 38% | 78% / 78% |
| headlines | 3 | 81% | 89% | 50% | 100% / 100% |
| marketing | 4 | 79% | 77% | 42% | 79% / 79% |
| naming | 4 | 81% | 90% | 49% | 100% / 100% |
| poetry | 4 | 54% | 56% | 47% | 92% / 100% |
| positioning | 3 | 39% | 67% | 46% | 89% / 100% |
| rewrite | 3 | 50% | 61% | 50% | 89% / 83% |
| short_story | 4 | 65% | 48% | 46% | 92% / 92% |
| story_concept | 3 | 50% | 58% | 44% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **rewrite-3**: prefer 17%, task 33%, original 50%. Constraint failures: 2. Judge: "Response B is more vivid and less predictable, using stronger imagery and more evocative language while still adhering to the original events and emotional core."
- **character-4**: prefer 33%, task 25%, original 58%. Constraint failures: 0. Judge: "Response B offers a more unique and memorable mentor character with a stronger sense of place and a more intriguing backstory, while still fulfilling the prompt's requirements."
- **fiction-5**: prefer 42%, task 21%, original 50%. Constraint failures: 0. Judge: "Response B provides a clearer narrative and context for the hardware store's closure, making it more engaging and aligned with the brief."
- **fiction-2**: prefer 33%, task 33%, original 42%. Constraint failures: 2. Judge: "Response A provides a clearer narrative structure and emotional depth while adhering closely to the brief's requirements."
- **character-3**: prefer 42%, task 33%, original 25%. Constraint failures: 0. Judge: "Response A presents a more original and humorous character that fits the brief of a scene-stealing side character in a romantic comedy."
- **poetry-3**: prefer 42%, task 38%, original 42%. Constraint failures: 0. Judge: "Response A presents a more traditional and cohesive love poem, while Response B takes a more abstract approach that may not align as closely with the typical expectations of a love poem."
- **short_story-5**: prefer 50%, task 33%, original 58%. Constraint failures: 1. Judge: "Response A tells a complete, satisfying story with a clear beginning, middle, and end, fulfilling the prompt's requirements, while Response B is more fragmented and leaves the reader with an unresolved narrative."
- **marketing-3**: prefer 50%, task 33%, original 50%. Constraint failures: 1. Judge: "Response A is more original and distinctive, while still fulfilling the brief's requirements more effectively by providing a clear headline and paragraph structure."
