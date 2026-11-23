# Benchmark report: run `dev_v3`, split `dev`, treatment `bohemian`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 216  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 216/216

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 49.3% [40.3, 59.0] | 71 / 0 / 73 | 4 / 5 | 1 |
| unpredictable | 72.9% [63.2, 82.6] | 105 / 0 / 39 | 10 / 1 | 0.012 |
| distinctive | 69.4% [58.3, 80.6] | 100 / 0 / 44 | 9 / 1 | 0.021 |
| prefer | 59.0% [48.6, 70.1] | 85 / 0 / 59 | 6 / 4 | 0.75 |
| task | 40.6% [34.0, 47.2] | 41 / 35 / 68 | 3 / 8 | 0.23 |

- google/gemini-2.5-flash-lite: original 54%, unpredictable 82%, distinctive 81%, prefer 72%, task 54%

- openai/gpt-4o-mini: original 44%, unpredictable 64%, distinctive 58%, prefer 46%, task 27%
- Position check (prefer): treatment win rate 74% when shown as A (n=58), 49% when shown as B (n=86).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 42.4% [35.4, 49.3] | 61 / 0 / 83 | 2 / 7 | 0.18 |
| unpredictable | 28.5% [22.2, 34.7] | 41 / 0 / 103 | 0 / 11 | 0.00098 |
| distinctive | 25.3% [19.1, 31.9] | 36 / 1 / 107 | 0 / 11 | 0.00098 |
| prefer | 24.3% [17.4, 31.9] | 35 / 0 / 109 | 0 / 11 | 0.00098 |
| task | 37.8% [28.1, 47.2] | 38 / 33 / 73 | 4 / 8 | 0.39 |

- google/gemini-2.5-flash-lite: original 38%, unpredictable 32%, distinctive 31%, prefer 29%, task 37%

- openai/gpt-4o-mini: original 47%, unpredictable 25%, distinctive 19%, prefer 19%, task 39%
- Position check (prefer): treatment win rate 35% when shown as A (n=78), 12% when shown as B (n=66).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 78% | 0.55 |
| unpredictable | 75% | 0.51 |
| distinctive | 75% | 0.52 |
| prefer | 75% | 0.50 |
| task | 44% | 0.20 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.11 | +0.76 [+0.50, +1.06] (11↑/0↓) | -0.33 [-0.51, -0.17] (0↑/8↓) |
| specificity | 4.04 | 4.57 | 4.43 | +0.39 [+0.13, +0.71] (7↑/0↓) | -0.14 [-0.29, +0.00] (3↑/6↓) |
| distinctiveness | 3.44 | 4.39 | 4.11 | +0.67 [+0.42, +0.94] (11↑/0↓) | -0.28 [-0.43, -0.14] (1↑/10↓) |
| coherence | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.35 | +0.88 [+0.58, +1.18] (11↑/0↓) | -0.28 [-0.44, -0.11] (1↑/9↓) |

Second judge (openai/gpt-4o-mini) on 72 outputs: Spearman ρ with the primary judge: originality 0.67, specificity 0.64, distinctiveness 0.76, coherence n/a, task_alignment n/a, creative_risk 0.73

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; bohemian: origi 4.67, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 262.3 | +21.792 [-3.001, +46.222] +9% | -13.444 [-40.459, +8.432] -5% |
| constraint pass rate | 1.000 | 0.944 | 1.000 | +0.000 [+0.000, +0.000] +0% | +0.056 [+0.000, +0.167] +6% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.060 | -3.868 [-10.845, -0.142] -98% | -0.014 [-0.082, +0.056] -19% |
| clichés /100 words (shared with skill) | 0.105 | 0.038 | 0.036 | -0.069 [-0.161, +0.007] -66% | -0.002 [-0.034, +0.029] -5% |
| clichés /100 words (held-out) | 3.823 | 0.036 | 0.024 | -3.799 [-10.809, -0.106] -99% | -0.012 [-0.074, +0.048] -33% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.570 | -0.141 [-0.194, -0.096] -20% | -0.011 [-0.035, +0.013] -2% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.318 | -0.115 [-0.313, -0.011] -26% | -0.009 [-0.043, +0.027] -3% |
| semantic diversity across samples | 0.203 | 0.285 | 0.295 | +0.093 [+0.067, +0.118] +46% | +0.010 [-0.014, +0.036] +3% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.010 | -0.030 [-0.057, -0.010] -74% | -0.002 [-0.008, +0.002] -19% |
| cross-model similarity | 0.729 | 0.679 | 0.648 | -0.082 [-0.121, -0.043] -11% | -0.031 [-0.065, +0.000] -5% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 47% | 68% | 61% | 51% | 38% | 100% / 100% |
| deepseek/deepseek-v4.1-flash | 51% | 78% | 78% | 67% | 43% | 100% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 33% | 50% | 38% | n/a / n/a |
| brainstorm | 1 | 50% | 75% | 33% | 100% / 100% |
| character | 1 | 50% | 67% | 58% | n/a / n/a |
| fiction | 1 | 25% | 33% | 25% | n/a / n/a |
| headlines | 1 | 92% | 100% | 58% | 100% / 100% |
| marketing | 1 | 58% | 83% | 54% | n/a / n/a |
| naming | 1 | 58% | 67% | 29% | 100% / 100% |
| poetry | 1 | 33% | 42% | 38% | n/a / n/a |
| positioning | 1 | 58% | 50% | 33% | 100% / 100% |
| rewrite | 1 | 42% | 42% | 25% | 100% / 100% |
| short_story | 1 | 42% | 42% | 46% | n/a / n/a |
| story_concept | 1 | 50% | 58% | 50% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 33%, task 25%, original 25%. Constraint failures: 0. Judge: "Response A feels more original and distinctive, with a stronger emotional arc and a more satisfying resolution that better fulfills the brief."
- **rewrite-1**: prefer 42%, task 25%, original 42%. Constraint failures: 0. Judge: "Response B is more distinctive and original, using stronger metaphors and a more evocative tone while still adhering to the original message."
- **poetry-1**: prefer 42%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A feels more complete and evocative, while Response B is more original and has a stronger voice."
- **positioning-1**: prefer 50%, task 33%, original 58%. Constraint failures: 0. Judge: "Response A provides a more comprehensive and nuanced positioning statement that aligns closely with the brief's requirements."
- **short_story-1**: prefer 42%, task 46%, original 42%. Constraint failures: 0. Judge: "Response A feels more complete and satisfying, offering a clearer arc for the protagonist's first day, while Response B is more evocative and original in its details."
- **analogy-1**: prefer 50%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A provides a clearer and more structured explanation of how the internet works, while Response B introduces unexpected elements but lacks the same clarity."
- **naming-1**: prefer 67%, task 29%, original 58%. Constraint failures: 0. Judge: "Response B offers more creative and relevant names that align better with the brief for a Mac cleaning application."
- **brainstorm-1**: prefer 75%, task 33%, original 50%. Constraint failures: 0. Judge: "Response A presents more clearly defined startup ideas that align closely with the brief's requirements, while Response B, while creative, lacks the same level of clarity and focus on underserved markets."
