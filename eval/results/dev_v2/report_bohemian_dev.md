# Benchmark report: run `dev_v2`, split `dev`, treatment `bohemian`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian, bohemian_v2b, core  
- Generations analysed: 360  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 359/360

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 52.8% [41.7, 63.2] | 76 / 0 / 68 | 6 / 5 | 1 |
| unpredictable | 73.6% [62.5, 84.0] | 106 / 0 / 38 | 9 / 2 | 0.065 |
| distinctive | 75.7% [64.6, 86.1] | 109 / 0 / 35 | 10 / 1 | 0.012 |
| prefer | 64.6% [52.1, 76.4] | 93 / 0 / 51 | 9 / 3 | 0.15 |
| task | 41.0% [32.3, 50.0] | 42 / 34 / 68 | 2 / 8 | 0.11 |

- google/gemini-2.5-flash-lite: original 60%, unpredictable 85%, distinctive 86%, prefer 75%, task 53%

- openai/gpt-4o-mini: original 46%, unpredictable 62%, distinctive 65%, prefer 54%, task 28%
- Position check (prefer): treatment win rate 84% when shown as A (n=58), 51% when shown as B (n=86).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 43.1% [36.8, 49.3] | 62 / 0 / 82 | 3 / 7 | 0.34 |
| unpredictable | 22.2% [13.9, 31.3] | 32 / 0 / 112 | 1 / 11 | 0.0063 |
| distinctive | 20.8% [13.2, 29.9] | 30 / 0 / 114 | 1 / 11 | 0.0063 |
| prefer | 26.4% [18.1, 36.1] | 38 / 0 / 106 | 1 / 10 | 0.012 |
| task | 35.4% [28.8, 41.0] | 36 / 30 / 78 | 0 / 11 | 0.00098 |

- google/gemini-2.5-flash-lite: original 43%, unpredictable 31%, distinctive 31%, prefer 32%, task 35%

- openai/gpt-4o-mini: original 43%, unpredictable 14%, distinctive 11%, prefer 21%, task 35%
- Position check (prefer): treatment win rate 37% when shown as A (n=78), 14% when shown as B (n=66).

### bohemian vs core

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| unpredictable | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| distinctive | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| prefer | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| task | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 81% | 0.61 |
| unpredictable | 76% | 0.54 |
| distinctive | 74% | 0.51 |
| prefer | 70% | 0.41 |
| task | 45% | 0.21 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | bohemian_v2b | core | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs core [95% CI] |
|---|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.11 | 4.12 | 4.08 | +0.76 [+0.50, +1.04] (11↑/0↓) | -0.33 [-0.50, -0.15] (1↑/9↓) | +0.03 [-0.11, +0.18] (4↑/3↓) |
| specificity | 4.04 | 4.57 | 4.51 | 4.43 | 4.46 | +0.47 [+0.25, +0.74] (10↑/0↓) | -0.06 [-0.21, +0.11] (1↑/4↓) | +0.06 [-0.13, +0.28] (5↑/4↓) |
| distinctiveness | 3.44 | 4.39 | 4.08 | 4.18 | 4.12 | +0.64 [+0.38, +0.94] (10↑/0↓) | -0.31 [-0.47, -0.12] (1↑/9↓) | -0.04 [-0.24, +0.15] (4↑/4↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.25 | 3.29 | 3.24 | +0.78 [+0.43, +1.14] (9↑/1↓) | -0.38 [-0.64, -0.10] (2↑/10↓) | +0.01 [-0.31, +0.38] (4↑/5↓) |

Second judge (openai/gpt-4o-mini) on 120 outputs: Spearman ρ with the primary judge: originality 0.59, specificity 0.63, distinctiveness 0.72, coherence n/a, task_alignment n/a, creative_risk 0.71

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; bohemian: origi 4.54, coher 5.00, task_ 5.00; bohemian_v2b: origi 4.54, coher 5.00, task_ 5.00; core: origi 4.58, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | bohemian_v2b | core | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs core [95% CI] |
|---|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 269.1 | 258.6 | 249.6 | +28.597 [-4.486, +68.100] +12% | -6.639 [-39.946, +29.931] -2% | +19.472 [-6.569, +53.222] +8% |
| constraint pass rate | 1.000 | 0.944 | 0.861 | 0.917 | 0.972 | -0.139 [-0.361, +0.000] -14% | -0.083 [-0.194, +0.000] -9% | -0.111 [-0.278, +0.000] -11% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.089 | 0.046 | 0.181 | -3.840 [-10.821, -0.122] -98% | +0.015 [-0.063, +0.099] +20% | -0.092 [-0.179, -0.005] -51% |
| clichés /100 words (shared with skill) | 0.105 | 0.038 | 0.038 | 0.046 | 0.112 | -0.067 [-0.139, -0.004] -64% | +0.001 [-0.037, +0.042] +1% | -0.073 [-0.143, -0.011] -66% |
| clichés /100 words (held-out) | 3.823 | 0.036 | 0.051 | 0.000 | 0.069 | -3.773 [-10.752, -0.080] -99% | +0.014 [-0.066, +0.101] +39% | -0.019 [-0.081, +0.050] -27% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.573 | 0.572 | 0.565 | -0.138 [-0.187, -0.094] -19% | -0.007 [-0.033, +0.017] -1% | +0.008 [-0.011, +0.028] +1% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.309 | 0.297 | 0.287 | -0.123 [-0.298, -0.015] -28% | -0.017 [-0.027, -0.010] -5% | +0.022 [+0.003, +0.050] +8% |
| semantic diversity across samples | 0.203 | 0.286 | 0.303 | 0.304 | 0.307 | +0.101 [+0.067, +0.134] +50% | +0.018 [-0.013, +0.047] +6% | -0.004 [-0.031, +0.027] -1% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.010 | 0.010 | 0.013 | -0.030 [-0.054, -0.011] -75% | -0.003 [-0.009, +0.003] -22% | -0.003 [-0.010, +0.002] -24% |
| cross-model similarity | 0.729 | 0.679 | 0.641 | 0.625 | 0.649 | -0.088 [-0.124, -0.053] -12% | -0.038 [-0.073, -0.001] -6% | -0.008 [-0.036, +0.017] -1% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 53% | 68% | 72% | 64% | 39% | 89% / 100% |
| deepseek/deepseek-v4.1-flash | 53% | 79% | 79% | 65% | 43% | 83% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 33% | 42% | 21% | n/a / n/a |
| brainstorm | 1 | 58% | 75% | 46% | 100% / 100% |
| character | 1 | 58% | 58% | 58% | n/a / n/a |
| fiction | 1 | 17% | 17% | 17% | n/a / n/a |
| headlines | 1 | 92% | 100% | 42% | 100% / 100% |
| marketing | 1 | 42% | 58% | 42% | n/a / n/a |
| naming | 1 | 75% | 92% | 33% | 100% / 100% |
| poetry | 1 | 42% | 42% | 25% | n/a / n/a |
| positioning | 1 | 67% | 75% | 50% | 100% / 100% |
| rewrite | 1 | 58% | 83% | 75% | 33% / 100% |
| short_story | 1 | 42% | 67% | 33% | n/a / n/a |
| story_concept | 1 | 50% | 67% | 50% | 83% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 17%, task 17%, original 17%. Constraint failures: 0. Judge: "Response A feels more fully realized, with a stronger emotional arc and more evocative descriptions, while still fulfilling the prompt's core request."
- **analogy-1**: prefer 42%, task 21%, original 33%. Constraint failures: 0. Judge: "Response A provides a more thorough and detailed explanation of the internet's workings using the postal analogy, covering key concepts like packets, routers, and addressing more comprehensively than Response B."
- **poetry-1**: prefer 42%, task 25%, original 42%. Constraint failures: 0. Judge: "Response A is more evocative and adheres more closely to the prompt's implied tone, while Response B is more concise and uses more surprising imagery."
- **short_story-1**: prefer 67%, task 33%, original 42%. Constraint failures: 0. Judge: "Response A presents a more engaging and relatable narrative that effectively captures the experience of a first day at a new job."
- **marketing-1**: prefer 58%, task 42%, original 42%. Constraint failures: 0. Judge: "Response A presents a more engaging advertisement for a household object while effectively highlighting its features."
- **story_concept-1**: prefer 67%, task 50%, original 50%. Constraint failures: 1. Judge: "Response B offers a more unique and compelling concept with a stronger sense of personal stakes for the protagonist, making it more distinctive and unpredictable."
- **character-1**: prefer 58%, task 58%, original 58%. Constraint failures: 0. Judge: "Response A presents a more straightforward and engaging protagonist for a mystery story, while Response B, though unique, is less accessible and may not align as closely with typical mystery conventions."
- **brainstorm-1**: prefer 75%, task 46%, original 58%. Constraint failures: 0. Judge: "Response A's ideas are more novel and address broader underserved markets, while Response B's ideas are more specific and have a more distinct voice."
