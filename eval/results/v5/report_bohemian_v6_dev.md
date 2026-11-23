# Benchmark report: run `v5`, split `dev`, treatment `bohemian_v6`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian_v4b, bohemian_v5, bohemian_v6  
- Generations analysed: 432  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 429/432

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v6 vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 66.0% [54.2, 77.1] | 95 / 0 / 49 | 9 / 2 | 0.065 |
| unpredictable | 69.4% [57.6, 80.6] | 100 / 0 / 44 | 9 / 2 | 0.065 |
| distinctive | 68.1% [56.9, 79.2] | 98 / 0 / 46 | 9 / 2 | 0.065 |
| prefer | 60.4% [50.0, 70.8] | 87 / 0 / 57 | 7 / 2 | 0.18 |
| task | 46.9% [39.9, 53.8] | 54 / 27 / 63 | 5 / 6 | 1 |

- google/gemini-2.5-flash-lite: original 69%, unpredictable 82%, distinctive 83%, prefer 78%, task 60%

- openai/gpt-4o-mini: original 62%, unpredictable 57%, distinctive 53%, prefer 43%, task 33%
- Position check (prefer): treatment win rate 70% when shown as A (n=80), 48% when shown as B (n=64).

### bohemian_v6 vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| unpredictable | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| distinctive | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| prefer | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |
| task | nan% [nan, nan] | 0 / 0 / 0 | 0 / 0 | 1 |

### bohemian_v6 vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 53.5% [43.1, 64.6] | 77 / 0 / 67 | 6 / 4 | 0.75 |
| unpredictable | 58.3% [49.3, 66.7] | 84 / 0 / 60 | 7 / 2 | 0.18 |
| distinctive | 59.4% [50.7, 67.7] | 85 / 1 / 58 | 8 / 1 | 0.039 |
| prefer | 58.3% [48.6, 67.4] | 84 / 0 / 60 | 5 / 1 | 0.22 |
| task | 55.9% [46.5, 65.6] | 69 / 23 / 52 | 6 / 4 | 0.75 |

- google/gemini-2.5-flash-lite: original 53%, unpredictable 47%, distinctive 51%, prefer 51%, task 50%

- openai/gpt-4o-mini: original 54%, unpredictable 69%, distinctive 68%, prefer 65%, task 62%
- Position check (prefer): treatment win rate 88% when shown as A (n=68), 32% when shown as B (n=76).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 88% | 0.74 |
| unpredictable | 66% | 0.30 |
| distinctive | 64% | 0.27 |
| prefer | 67% | 0.34 |
| task | 48% | 0.23 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian_v4b | bohemian_v5 | bohemian_v6 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.07 | 4.18 | 4.13 | 4.14 | +0.79 [+0.53, +1.08] (12↑/0↓) | -0.31 [-0.43, -0.18] (0↑/10↓) | +0.07 [-0.15, +0.29] (6↑/4↓) |
| specificity | 4.04 | 4.57 | 4.65 | 4.54 | 4.56 | 4.57 | +0.53 [+0.28, +0.82] (10↑/0↓) | +0.00 [-0.10, +0.10] (3↑/3↓) | -0.08 [-0.26, +0.10] (1↑/5↓) |
| distinctiveness | 3.44 | 4.39 | 4.11 | 4.22 | 4.14 | 4.22 | +0.78 [+0.56, +1.01] (12↑/0↓) | -0.17 [-0.28, -0.06] (2↑/8↓) | +0.11 [-0.07, +0.32] (7↑/5↓) |
| coherence | 5.00 | 5.00 | 5.00 | 4.99 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.94 | 5.00 | 4.94 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.06 [+0.00, +0.17] (1↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.36 | 3.35 | 3.29 | 3.43 | +0.96 [+0.72, +1.19] (12↑/0↓) | -0.19 [-0.32, -0.07] (1↑/8↓) | +0.07 [-0.24, +0.36] (7↑/4↓) |

Second judge (openai/gpt-4o-mini) on 144 outputs: Spearman ρ with the primary judge: originality 0.62, specificity 0.59, distinctiveness 0.66, coherence n/a, task_alignment n/a, creative_risk 0.71

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; antialgorithm: origi 4.58, coher 5.00, task_ 5.00; bohemian_v4b: origi 4.71, coher 5.00, task_ 5.00; bohemian_v5: origi 4.71, coher 5.00, task_ 5.00; bohemian_v6: origi 4.62, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian_v4b | bohemian_v5 | bohemian_v6 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 207.0 | 224.0 | 231.3 | 227.1 | -13.347 [-42.084, +16.014] -6% | -48.583 [-89.348, -11.333] -18% | +20.097 [-15.432, +62.487] +10% |
| constraint pass rate | 1.000 | 0.944 | 0.917 | 0.972 | 0.944 | 0.972 | -0.028 [-0.083, +0.000] -3% | +0.028 [-0.083, +0.167] +3% | +0.056 [-0.056, +0.194] +6% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.103 | 0.269 | 0.114 | 0.138 | -3.791 [-10.782, -0.060] -96% | +0.063 [-0.024, +0.151] +86% | +0.035 [-0.071, +0.124] +34% |
| clichés /100 words (shared with skill) | 0.029 | 0.013 | 0.084 | 0.025 | 0.038 | 0.019 | -0.010 [-0.044, +0.013] -34% | +0.006 [-0.012, +0.027] +51% | -0.065 [-0.189, +0.007] -77% |
| clichés /100 words (held-out) | 3.900 | 0.061 | 0.019 | 0.244 | 0.076 | 0.119 | -3.781 [-10.766, -0.055] -97% | +0.057 [-0.034, +0.144] +93% | +0.100 [+0.039, +0.167] +530% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.514 | 0.553 | 0.520 | 0.556 | -0.155 [-0.202, -0.110] -22% | -0.025 [-0.063, +0.016] -4% | +0.041 [+0.011, +0.069] +8% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.283 | 0.305 | 0.312 | 0.297 | -0.135 [-0.333, -0.006] -31% | -0.029 [-0.063, -0.004] -9% | +0.014 [-0.001, +0.038] +5% |
| semantic diversity across samples | 0.203 | 0.285 | 0.365 | 0.335 | 0.360 | 0.336 | +0.134 [+0.096, +0.171] +66% | +0.051 [+0.007, +0.095] +18% | -0.029 [-0.056, +0.003] -8% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.006 | 0.009 | 0.007 | 0.010 | -0.030 [-0.051, -0.012] -75% | -0.003 [-0.008, +0.004] -20% | +0.004 [-0.001, +0.011] +67% |
| cross-model similarity | 0.729 | 0.679 | 0.593 | 0.624 | 0.606 | 0.613 | -0.116 [-0.162, -0.068] -16% | -0.066 [-0.111, -0.014] -10% | +0.020 [-0.011, +0.051] +3% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 61% | 61% | 61% | 50% | 39% | 100% / 100% |
| deepseek/deepseek-v4.1-flash | 71% | 78% | 75% | 71% | 55% | 94% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 67% | 67% | 54% | n/a / n/a |
| brainstorm | 1 | 75% | 83% | 62% | 100% / 100% |
| character | 1 | 83% | 58% | 67% | n/a / n/a |
| fiction | 1 | 25% | 33% | 25% | n/a / n/a |
| headlines | 1 | 100% | 100% | 54% | 100% / 100% |
| marketing | 1 | 50% | 67% | 46% | n/a / n/a |
| naming | 1 | 75% | 75% | 42% | 83% / 100% |
| poetry | 1 | 33% | 33% | 33% | n/a / n/a |
| positioning | 1 | 75% | 58% | 29% | 100% / 100% |
| rewrite | 1 | 67% | 50% | 50% | 100% / 100% |
| short_story | 1 | 58% | 50% | 46% | n/a / n/a |
| story_concept | 1 | 83% | 50% | 54% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 33%, task 25%, original 25%. Constraint failures: 0. Judge: "Response A offers a more developed narrative arc and a more hopeful, albeit bittersweet, conclusion, making it a more satisfying story for the brief."
- **poetry-1**: prefer 33%, task 33%, original 33%. Constraint failures: 0. Judge: "Response B offers a more vivid and engaging portrayal of the ocean, fulfilling the brief with greater creativity and depth."
- **positioning-1**: prefer 58%, task 29%, original 75%. Constraint failures: 0. Judge: "Response B provides a clearer brand identity and aligns more closely with the brief's requirements for positioning and tagline."
- **short_story-1**: prefer 50%, task 46%, original 58%. Constraint failures: 0. Judge: "Response B presents a more engaging and relatable narrative that aligns closely with the brief while showcasing distinctive character and unpredictability."
- **rewrite-1**: prefer 50%, task 50%, original 67%. Constraint failures: 0. Judge: "Response A maintains the motivational essence while offering a more distinctive and engaging rewrite."
- **story_concept-1**: prefer 50%, task 54%, original 83%. Constraint failures: 0. Judge: "Response B offers a more unique and compelling concept with higher stakes and a more developed character arc, while still adhering to the paragraph format."
- **marketing-1**: prefer 67%, task 46%, original 50%. Constraint failures: 0. Judge: "Response A offers a more novel and unexpected take on the brief, while Response B is more distinctive and aligns better with the advertisement format."
- **naming-1**: prefer 75%, task 42%, original 75%. Constraint failures: 1. Judge: "Response B offers more creative and relevant names that align well with the brief for a Mac cleaning application."
