# Benchmark report: run `v5`, split `dev`, treatment `bohemian_v5`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian_v4b, bohemian_v5  
- Generations analysed: 360  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 358/360

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v5 vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 67.4% [56.2, 77.1] | 97 / 0 / 47 | 10 / 2 | 0.039 |
| unpredictable | 75.0% [64.6, 84.7] | 108 / 0 / 36 | 10 / 1 | 0.012 |
| distinctive | 74.3% [63.2, 84.7] | 107 / 0 / 37 | 11 / 1 | 0.0063 |
| prefer | 67.4% [56.9, 77.1] | 97 / 0 / 47 | 10 / 1 | 0.012 |
| task | 48.3% [39.2, 57.3] | 56 / 27 / 61 | 5 / 5 | 1 |

- google/gemini-2.5-flash-lite: original 68%, unpredictable 83%, distinctive 83%, prefer 81%, task 59%

- openai/gpt-4o-mini: original 67%, unpredictable 67%, distinctive 65%, prefer 54%, task 38%
- Position check (prefer): treatment win rate 76% when shown as A (n=80), 56% when shown as B (n=64).

### bohemian_v5 vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 37.5% [27.1, 46.5] | 54 / 0 / 90 | 3 / 9 | 0.15 |
| unpredictable | 22.2% [15.3, 28.5] | 32 / 0 / 112 | 0 / 12 | 0.00049 |
| distinctive | 22.2% [15.3, 29.2] | 32 / 0 / 112 | 0 / 12 | 0.00049 |
| prefer | 22.9% [14.6, 31.3] | 33 / 0 / 111 | 0 / 11 | 0.00098 |
| task | 32.3% [22.6, 41.7] | 35 / 23 / 86 | 1 / 10 | 0.012 |

- google/gemini-2.5-flash-lite: original 31%, unpredictable 28%, distinctive 28%, prefer 25%, task 31%

- openai/gpt-4o-mini: original 44%, unpredictable 17%, distinctive 17%, prefer 21%, task 33%
- Position check (prefer): treatment win rate 43% when shown as A (n=68), 5% when shown as B (n=76).

### bohemian_v5 vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 57.6% [45.8, 70.1] | 83 / 0 / 61 | 6 / 4 | 0.75 |
| unpredictable | 56.9% [47.9, 66.0] | 82 / 0 / 62 | 6 / 2 | 0.29 |
| distinctive | 61.8% [54.2, 69.4] | 89 / 0 / 55 | 8 / 1 | 0.039 |
| prefer | 61.8% [54.2, 68.8] | 89 / 0 / 55 | 9 / 1 | 0.021 |
| task | 56.2% [44.8, 67.7] | 70 / 22 / 52 | 6 / 3 | 0.51 |

- google/gemini-2.5-flash-lite: original 56%, unpredictable 51%, distinctive 53%, prefer 57%, task 57%

- openai/gpt-4o-mini: original 60%, unpredictable 62%, distinctive 71%, prefer 67%, task 56%
- Position check (prefer): treatment win rate 79% when shown as A (n=76), 43% when shown as B (n=68).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 86% | 0.72 |
| unpredictable | 72% | 0.45 |
| distinctive | 72% | 0.44 |
| prefer | 74% | 0.47 |
| task | 53% | 0.29 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian_v4b | bohemian_v5 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.07 | 4.18 | 4.13 | +0.78 [+0.51, +1.04] (11↑/1↓) | -0.32 [-0.49, -0.11] (1↑/9↓) | +0.06 [-0.11, +0.25] (4↑/5↓) |
| specificity | 4.04 | 4.57 | 4.65 | 4.54 | 4.56 | +0.51 [+0.31, +0.72] (9↑/0↓) | -0.01 [-0.14, +0.13] (2↑/4↓) | -0.10 [-0.29, +0.15] (1↑/7↓) |
| distinctiveness | 3.44 | 4.39 | 4.11 | 4.22 | 4.14 | +0.69 [+0.44, +0.94] (11↑/1↓) | -0.25 [-0.40, -0.07] (1↑/9↓) | +0.03 [-0.14, +0.19] (5↑/5↓) |
| coherence | 5.00 | 5.00 | 5.00 | 4.99 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.94 | 5.00 | 4.94 | -0.06 [-0.17, +0.00] (0↑/1↓) | -0.06 [-0.17, +0.00] (0↑/1↓) | +0.00 [-0.17, +0.17] (1↑/1↓) |
| creative_risk | 2.47 | 3.62 | 3.36 | 3.35 | 3.29 | +0.82 [+0.49, +1.17] (11↑/1↓) | -0.33 [-0.57, -0.06] (1↑/9↓) | -0.07 [-0.32, +0.18] (4↑/6↓) |

Second judge (openai/gpt-4o-mini) on 120 outputs: Spearman ρ with the primary judge: originality 0.62, specificity 0.59, distinctiveness 0.69, coherence n/a, task_alignment n/a, creative_risk 0.71

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; antialgorithm: origi 4.58, coher 5.00, task_ 5.00; bohemian_v4b: origi 4.71, coher 5.00, task_ 5.00; bohemian_v5: origi 4.71, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian_v4b | bohemian_v5 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 207.0 | 224.0 | 231.3 | -9.167 [-38.833, +21.365] -4% | -44.403 [-80.098, -13.208] -16% | +24.278 [-8.986, +67.362] +12% |
| constraint pass rate | 1.000 | 0.944 | 0.917 | 0.972 | 0.944 | -0.056 [-0.111, +0.000] -6% | +0.000 [-0.111, +0.139] +0% | +0.028 [-0.111, +0.167] +3% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.103 | 0.269 | 0.114 | -3.814 [-10.809, -0.091] -97% | +0.040 [-0.061, +0.169] +54% | +0.012 [-0.054, +0.079] +11% |
| clichés /100 words (shared with skill) | 0.029 | 0.013 | 0.084 | 0.025 | 0.038 | +0.010 [+0.000, +0.027] +34% | +0.026 [+0.000, +0.062] +204% | -0.045 [-0.187, +0.049] -54% |
| clichés /100 words (held-out) | 3.900 | 0.061 | 0.019 | 0.244 | 0.076 | -3.824 [-10.788, -0.092] -98% | +0.014 [-0.081, +0.142] +24% | +0.057 [-0.018, +0.170] +304% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.514 | 0.553 | 0.520 | -0.191 [-0.248, -0.139] -27% | -0.060 [-0.099, -0.022] -10% | +0.006 [-0.024, +0.032] +1% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.283 | 0.305 | 0.312 | -0.120 [-0.324, +0.013] -28% | -0.014 [-0.054, +0.014] -4% | +0.029 [+0.017, +0.047] +10% |
| semantic diversity across samples | 0.203 | 0.285 | 0.365 | 0.335 | 0.360 | +0.158 [+0.110, +0.208] +78% | +0.075 [+0.032, +0.120] +26% | -0.005 [-0.043, +0.036] -1% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.006 | 0.009 | 0.007 | -0.033 [-0.059, -0.013] -83% | -0.006 [-0.014, +0.000] -47% | +0.001 [-0.002, +0.003] +10% |
| cross-model similarity | 0.729 | 0.679 | 0.593 | 0.624 | 0.606 | -0.124 [-0.192, -0.055] -17% | -0.074 [-0.128, -0.020] -11% | +0.013 [-0.036, +0.057] +2% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 67% | 71% | 69% | 64% | 44% | 100% / 100% |
| deepseek/deepseek-v4.1-flash | 68% | 79% | 79% | 71% | 52% | 89% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 58% | 75% | 38% | n/a / n/a |
| brainstorm | 1 | 83% | 92% | 71% | 100% / 100% |
| character | 1 | 67% | 58% | 67% | n/a / n/a |
| fiction | 1 | 33% | 25% | 17% | n/a / n/a |
| headlines | 1 | 92% | 92% | 50% | 83% / 100% |
| marketing | 1 | 92% | 75% | 62% | n/a / n/a |
| naming | 1 | 75% | 75% | 33% | 100% / 100% |
| poetry | 1 | 58% | 50% | 33% | n/a / n/a |
| positioning | 1 | 67% | 58% | 38% | 100% / 100% |
| rewrite | 1 | 67% | 58% | 50% | 100% / 100% |
| short_story | 1 | 83% | 83% | 67% | n/a / n/a |
| story_concept | 1 | 33% | 67% | 54% | 83% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 25%, task 17%, original 33%. Constraint failures: 0. Judge: "Response A provides a more cohesive narrative that aligns closely with the brief while also showcasing emotional depth and character development."
- **poetry-1**: prefer 50%, task 33%, original 58%. Constraint failures: 0. Judge: "Response B offers a more vivid and imaginative portrayal of the ocean, fulfilling the brief with greater creativity and depth."
- **positioning-1**: prefer 58%, task 38%, original 67%. Constraint failures: 0. Judge: "Response B offers more comprehensive options and a stronger, more differentiated positioning statement that addresses potential customer concerns."
- **naming-1**: prefer 75%, task 33%, original 75%. Constraint failures: 0. Judge: "Response B offers more creative and memorable names that align well with the brief's requirements."
- **rewrite-1**: prefer 58%, task 50%, original 67%. Constraint failures: 0. Judge: "Response B offers a more distinctive and engaging rewrite that maintains the motivational essence while avoiding clichés."
- **analogy-1**: prefer 75%, task 38%, original 58%. Constraint failures: 0. Judge: "Response A provides a more detailed and structured explanation that aligns closely with the brief's requirements."
- **story_concept-1**: prefer 67%, task 54%, original 33%. Constraint failures: 1. Judge: "Response A presents a more original and concise concept that aligns closely with the brief's requirements for a fantasy novel pitch."
- **character-1**: prefer 58%, task 67%, original 67%. Constraint failures: 0. Judge: "Response B presents a more unusual protagonist with a unique skill set, while Response A, though strong, is more predictable in its approach to the mystery genre."
