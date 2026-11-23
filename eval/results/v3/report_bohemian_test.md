# Benchmark report: run `v3`, split `test`, treatment `bohemian`

- Tasks: 42  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian  
- Generations analysed: 1008  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 1005/1008

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 65.2% [58.0, 72.3] | 327 / 3 / 174 | 25 / 9 | 0.009 |
| unpredictable | 82.2% [76.2, 88.0] | 412 / 5 / 87 | 37 / 2 | 2.8e-09 |
| distinctive | 79.9% [73.3, 85.8] | 401 / 3 / 100 | 36 / 3 | 3.6e-08 |
| prefer | 72.7% [65.2, 80.2] | 365 / 3 / 136 | 33 / 6 | 1.4e-05 |
| task | 52.7% [48.3, 56.7] | 203 / 125 / 176 | 21 / 16 | 0.51 |

- google/gemini-2.5-flash-lite: original 72%, unpredictable 92%, distinctive 91%, prefer 86%, task 65%

- openai/gpt-4o-mini: original 58%, unpredictable 73%, distinctive 69%, prefer 59%, task 40%
- Position check (prefer): treatment win rate 82% when shown as A (n=268), 62% when shown as B (n=236).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 43.7% [38.4, 48.8] | 219 / 2 / 283 | 12 / 21 | 0.16 |
| unpredictable | 35.3% [29.5, 41.4] | 177 / 2 / 325 | 9 / 27 | 0.0039 |
| distinctive | 37.9% [31.3, 44.4] | 190 / 2 / 312 | 9 / 26 | 0.006 |
| prefer | 36.8% [30.6, 43.4] | 185 / 1 / 318 | 8 / 30 | 0.00047 |
| task | 41.6% [36.1, 46.9] | 154 / 111 / 239 | 10 / 28 | 0.0051 |

- google/gemini-2.5-flash-lite: original 43%, unpredictable 39%, distinctive 40%, prefer 38%, task 43%

- openai/gpt-4o-mini: original 44%, unpredictable 31%, distinctive 36%, prefer 35%, task 40%
- Position check (prefer): treatment win rate 58% when shown as A (n=236), 18% when shown as B (n=268).

### bohemian vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 52.3% [46.1, 58.3] | 263 / 1 / 240 | 22 / 14 | 0.24 |
| unpredictable | 54.3% [48.8, 59.8] | 273 / 1 / 230 | 23 / 15 | 0.26 |
| distinctive | 55.2% [48.5, 61.7] | 277 / 2 / 225 | 25 / 15 | 0.15 |
| prefer | 58.8% [52.1, 65.3] | 296 / 1 / 207 | 25 / 11 | 0.029 |
| task | 54.1% [48.8, 59.1] | 223 / 99 / 182 | 24 / 15 | 0.2 |

- google/gemini-2.5-flash-lite: original 52%, unpredictable 46%, distinctive 47%, prefer 52%, task 54%

- openai/gpt-4o-mini: original 53%, unpredictable 62%, distinctive 63%, prefer 66%, task 54%
- Position check (prefer): treatment win rate 79% when shown as A (n=234), 41% when shown as B (n=270).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 87% | 0.74 |
| unpredictable | 69% | 0.38 |
| distinctive | 73% | 0.45 |
| prefer | 74% | 0.48 |
| task | 46% | 0.24 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 4.04 | 4.06 | +0.85 [+0.73, +0.98] (41↑/0↓) | -0.07 [-0.14, +0.00] (11↑/20↓) | +0.02 [-0.07, +0.10] (17↑/15↓) |
| specificity | 3.90 | 4.56 | 4.58 | 4.58 | +0.68 [+0.53, +0.84] (36↑/0↓) | +0.02 [-0.07, +0.10] (18↑/7↓) | +0.00 [-0.10, +0.11] (12↑/14↓) |
| distinctiveness | 3.28 | 4.18 | 4.13 | 4.16 | +0.88 [+0.73, +1.04] (40↑/0↓) | -0.02 [-0.09, +0.06] (13↑/17↓) | +0.04 [-0.05, +0.13] (15↑/16↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | 4.99 | -0.01 [-0.02, +0.00] (0↑/1↓) | -0.01 [-0.02, +0.00] (0↑/1↓) | +0.00 [-0.01, +0.02] (1↑/1↓) |
| creative_risk | 2.34 | 3.35 | 3.31 | 3.31 | +0.98 [+0.79, +1.17] (38↑/0↓) | -0.03 [-0.13, +0.07] (16↑/17↓) | -0.00 [-0.15, +0.14] (19↑/18↓) |

Second judge (openai/gpt-4o-mini) on 336 outputs: Spearman ρ with the primary judge: originality 0.54, specificity 0.67, distinctiveness 0.57, coherence n/a, task_alignment 0.71, creative_risk 0.68

Second judge's own means on that subset: baseline: origi 4.15, coher 5.00, task_ 5.00; oneliner: origi 4.69, coher 5.00, task_ 5.00; antialgorithm: origi 4.51, coher 5.00, task_ 4.98; bohemian: origi 4.62, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|
| words | 169.2 | 194.1 | 169.1 | 203.0 | +33.849 [+19.417, +50.425] +20% | +8.893 [-2.941, +20.488] +5% | +33.921 [+12.020, +60.961] +20% |
| constraint pass rate | 0.940 | 0.870 | 0.884 | 0.898 | -0.042 [-0.083, -0.005] -4% | +0.028 [-0.028, +0.083] +3% | +0.014 [-0.037, +0.060] +2% |
| clichés /100 words (all) | 0.437 | 0.279 | 0.026 | 0.205 | -0.232 [-0.365, -0.122] -53% | -0.074 [-0.217, +0.027] -27% | +0.179 [+0.008, +0.486] +686% |
| clichés /100 words (shared with skill) | 0.095 | 0.054 | 0.019 | 0.034 | -0.061 [-0.135, -0.001] -64% | -0.020 [-0.056, +0.014] -37% | +0.015 [-0.009, +0.041] +79% |
| clichés /100 words (held-out) | 0.342 | 0.225 | 0.007 | 0.171 | -0.171 [-0.293, -0.081] -50% | -0.054 [-0.190, +0.039] -24% | +0.164 [+0.002, +0.469] +2299% |
| typicality (cos to obvious answer) | 0.737 | 0.626 | 0.549 | 0.605 | -0.131 [-0.148, -0.116] -18% | -0.021 [-0.033, -0.009] -3% | +0.057 [+0.045, +0.069] +10% |
| intra-list similarity (list tasks) | 0.428 | 0.356 | 0.333 | 0.360 | -0.068 [-0.128, -0.016] -16% | +0.004 [-0.014, +0.025] +1% | +0.027 [+0.006, +0.050] +8% |
| semantic diversity across samples | 0.187 | 0.267 | 0.323 | 0.276 | +0.089 [+0.068, +0.110] +48% | +0.008 [-0.008, +0.024] +3% | -0.047 [-0.067, -0.027] -15% |
| 3-gram overlap across samples | 0.056 | 0.015 | 0.012 | 0.017 | -0.039 [-0.067, -0.019] -70% | +0.001 [-0.003, +0.005] +10% | +0.005 [+0.000, +0.010] +39% |
| cross-model similarity | 0.749 | 0.680 | 0.618 | 0.648 | -0.102 [-0.130, -0.075] -14% | -0.032 [-0.051, -0.015] -5% | +0.030 [+0.012, +0.046] +5% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 66% | 77% | 76% | 70% | 54% | 87% / 90% |
| deepseek/deepseek-v4.1-flash | 65% | 88% | 84% | 75% | 52% | 93% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 3 | 60% | 74% | 57% | 94% / 100% |
| brainstorm | 4 | 96% | 100% | 70% | 100% / 100% |
| character | 3 | 53% | 53% | 50% | 92% / 100% |
| fiction | 4 | 29% | 42% | 35% | 67% / 78% |
| headlines | 3 | 81% | 92% | 57% | 100% / 100% |
| marketing | 4 | 90% | 85% | 51% | 79% / 79% |
| naming | 4 | 79% | 83% | 47% | 100% / 100% |
| poetry | 4 | 67% | 67% | 54% | 92% / 100% |
| positioning | 3 | 61% | 81% | 61% | 89% / 100% |
| rewrite | 3 | 53% | 56% | 47% | 83% / 83% |
| short_story | 4 | 67% | 65% | 61% | 75% / 92% |
| story_concept | 3 | 36% | 75% | 40% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-5**: prefer 0%, task 4%, original 0%. Constraint failures: 0. Judge: "Response A establishes a stronger sense of place and character, while Response B feels a bit more generic and less evocative."
- **character-4**: prefer 25%, task 42%, original 58%. Constraint failures: 0. Judge: "Response A feels more fully realized, with a stronger sense of character and a more nuanced portrayal of the mentor-mentee relationship."
- **rewrite-3**: prefer 33%, task 42%, original 58%. Constraint failures: 2. Judge: "Response A is more vivid and less predictable, using stronger imagery and more evocative language to convey Sarah's sadness and memories."
- **story_concept-2**: prefer 42%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A offers a more original and compelling premise with a stronger emotional core, while Response B's premise, though interesting, feels slightly less grounded and more predictable in its execution."
- **fiction-2**: prefer 33%, task 50%, original 50%. Constraint failures: 1. Judge: "Response B offers a more distinctive and unpredictable take on the brief, while Response A better satisfies the specific task of dividing up items in the kitchen."
- **rewrite-2**: prefer 42%, task 42%, original 42%. Constraint failures: 1. Judge: "Response A feels more authentic and directly addresses common pain points of small businesses with accounting software, while Response B is a bit too blunt and less descriptive."
- **poetry-3**: prefer 50%, task 42%, original 50%. Constraint failures: 0. Judge: "Response A feels more like a complete poem, whereas Response B feels like a prose piece broken into lines, and its meta-commentary about the brief is unnecessary."
- **analogy-2**: prefer 54%, task 46%, original 46%. Constraint failures: 0. Judge: "Response A is more original and distinctive by elaborating on the analogy to explain the 'why' behind compound interest, making it more impactful for a teenager."
