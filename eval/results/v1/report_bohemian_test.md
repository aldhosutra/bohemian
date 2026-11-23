# Benchmark report: run `v1`, split `test`, treatment `bohemian`

- Tasks: 42  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 756  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 751/756

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 61.3% [54.8, 67.7] | 307 / 4 / 193 | 25 / 11 | 0.029 |
| unpredictable | 76.9% [71.1, 82.2] | 385 / 5 / 114 | 34 / 2 | 1.9e-08 |
| distinctive | 71.7% [66.0, 77.3] | 359 / 5 / 140 | 34 / 6 | 8.4e-06 |
| prefer | 64.3% [58.0, 70.5] | 322 / 4 / 178 | 30 / 11 | 0.0043 |
| task | 50.6% [46.1, 55.1] | 193 / 124 / 187 | 19 / 21 | 0.87 |

- google/gemini-2.5-flash-lite: original 66%, unpredictable 86%, distinctive 86%, prefer 80%, task 61%

- openai/gpt-4o-mini: original 56%, unpredictable 67%, distinctive 57%, prefer 48%, task 40%
- Position check (prefer): treatment win rate 75% when shown as A (n=268), 52% when shown as B (n=236).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 39.5% [34.0, 44.7] | 198 / 2 / 304 | 8 / 27 | 0.0019 |
| unpredictable | 25.0% [20.0, 30.5] | 124 / 4 / 376 | 2 / 38 | 1.5e-09 |
| distinctive | 25.8% [21.0, 31.0] | 129 / 2 / 373 | 2 / 38 | 1.5e-09 |
| prefer | 26.5% [21.3, 32.0] | 133 / 1 / 370 | 3 / 37 | 1.9e-08 |
| task | 37.4% [32.3, 42.2] | 137 / 103 / 264 | 6 / 31 | 4.1e-05 |

- google/gemini-2.5-flash-lite: original 38%, unpredictable 29%, distinctive 30%, prefer 31%, task 35%

- openai/gpt-4o-mini: original 40%, unpredictable 21%, distinctive 22%, prefer 22%, task 39%
- Position check (prefer): treatment win rate 44% when shown as A (n=236), 11% when shown as B (n=268).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 84% | 0.69 |
| unpredictable | 73% | 0.49 |
| distinctive | 71% | 0.45 |
| prefer | 71% | 0.44 |
| task | 42% | 0.19 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 3.95 | +0.75 [+0.61, +0.88] (39↑/2↓) | -0.17 [-0.27, -0.08] (8↑/28↓) |
| specificity | 3.90 | 4.56 | 4.46 | +0.56 [+0.40, +0.73] (36↑/3↓) | -0.10 [-0.22, +0.01] (11↑/13↓) |
| distinctiveness | 3.28 | 4.18 | 4.03 | +0.75 [+0.60, +0.90] (39↑/1↓) | -0.15 [-0.24, -0.06] (8↑/24↓) |
| coherence | 5.00 | 5.00 | 4.99 | -0.01 [-0.02, +0.00] (0↑/1↓) | -0.01 [-0.02, +0.00] (0↑/1↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | -0.01 [-0.02, +0.00] (0↑/1↓) | -0.01 [-0.02, +0.00] (0↑/1↓) |
| creative_risk | 2.34 | 3.35 | 3.13 | +0.79 [+0.62, +0.97] (38↑/1↓) | -0.21 [-0.32, -0.11] (8↑/26↓) |

Second judge (openai/gpt-4o-mini) on 252 outputs: Spearman ρ with the primary judge: originality 0.62, specificity 0.72, distinctiveness 0.62, coherence n/a, task_alignment 0.71, creative_risk 0.73

Second judge's own means on that subset: baseline: origi 4.15, coher 5.00, task_ 5.00; oneliner: origi 4.69, coher 5.00, task_ 5.00; bohemian: origi 4.37, coher 5.00, task_ 4.95

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 169.2 | 194.1 | 185.4 | +16.214 [+7.091, +26.790] +10% | -8.742 [-20.290, +1.853] -5% |
| constraint pass rate | 0.940 | 0.870 | 0.894 | -0.046 [-0.088, -0.005] -5% | +0.023 [-0.037, +0.083] +3% |
| clichés /100 words (all) | 0.437 | 0.279 | 0.193 | -0.244 [-0.400, -0.114] -56% | -0.086 [-0.224, +0.017] -31% |
| clichés /100 words (shared with skill) | 0.095 | 0.054 | 0.044 | -0.051 [-0.128, +0.021] -54% | -0.010 [-0.048, +0.040] -19% |
| clichés /100 words (held-out) | 0.342 | 0.225 | 0.149 | -0.193 [-0.347, -0.080] -56% | -0.076 [-0.210, +0.010] -34% |
| typicality (cos to obvious answer) | 0.740 | 0.629 | 0.603 | -0.137 [-0.157, -0.118] -18% | -0.026 [-0.041, -0.011] -4% |
| intra-list similarity (list tasks) | 0.428 | 0.356 | 0.376 | -0.052 [-0.106, -0.003] -12% | +0.020 [+0.008, +0.033] +6% |
| semantic diversity across samples | 0.187 | 0.267 | 0.303 | +0.116 [+0.092, +0.142] +62% | +0.036 [+0.017, +0.054] +13% |
| 3-gram overlap across samples | 0.056 | 0.015 | 0.014 | -0.042 [-0.069, -0.022] -75% | -0.001 [-0.005, +0.003] -8% |
| cross-model similarity | 0.749 | 0.680 | 0.635 | -0.114 [-0.148, -0.083] -15% | -0.045 [-0.067, -0.024] -7% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 59% | 76% | 69% | 62% | 53% | 88% / 90% |
| deepseek/deepseek-v4.1-flash | 63% | 78% | 74% | 67% | 49% | 91% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 3 | 65% | 76% | 50% | 94% / 100% |
| brainstorm | 4 | 94% | 98% | 70% | 100% / 100% |
| character | 3 | 56% | 58% | 49% | 100% / 100% |
| fiction | 4 | 29% | 38% | 29% | 78% / 78% |
| headlines | 3 | 78% | 78% | 60% | 94% / 100% |
| marketing | 4 | 71% | 77% | 52% | 79% / 79% |
| naming | 4 | 72% | 68% | 42% | 96% / 100% |
| poetry | 4 | 58% | 58% | 59% | 75% / 100% |
| positioning | 3 | 67% | 58% | 56% | 94% / 100% |
| rewrite | 3 | 56% | 58% | 53% | 78% / 83% |
| short_story | 4 | 52% | 46% | 45% | 75% / 92% |
| story_concept | 3 | 36% | 58% | 46% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-5**: prefer 25%, task 12%, original 8%. Constraint failures: 1. Judge: "Response A feels more complete and evocative, while Response B introduces an interesting backstory but feels less fully realized."
- **fiction-3**: prefer 33%, task 29%, original 33%. Constraint failures: 0. Judge: "Response A presents a more cohesive narrative that aligns closely with the brief, while Response B, though interesting, feels more like a vignette than flash fiction."
- **short_story-2**: prefer 25%, task 38%, original 58%. Constraint failures: 1. Judge: "Response B presents a more engaging and unpredictable narrative that aligns closely with the brief's requirements."
- **short_story-3**: prefer 33%, task 38%, original 42%. Constraint failures: 0. Judge: "Response A offers a more compelling narrative with a stronger character arc and a more impactful ending, while Response B feels a bit more generic in its premise and execution."
- **fiction-4**: prefer 50%, task 29%, original 33%. Constraint failures: 2. Judge: "Response A is more suitable for the brief as it directly involves a ghost and has a clear resolution, while Response B, though creative, is less focused on a traditional ghost story."
- **character-4**: prefer 42%, task 38%, original 67%. Constraint failures: 0. Judge: "Response B presents a more unique and engaging mentor character, while Response A better adheres to the brief's word count and structure."
- **positioning-2**: prefer 33%, task 50%, original 50%. Constraint failures: 0. Judge: "Response A is more comprehensive and directly addresses all parts of the brief without making assumptions or requiring clarification, while still being original and distinctive."
- **naming-4**: prefer 42%, task 42%, original 67%. Constraint failures: 0. Judge: "Response B offers more creative and relevant names that align well with the brief."
