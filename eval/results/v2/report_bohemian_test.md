# Benchmark report: run `v2`, split `test`, treatment `bohemian`

- Tasks: 42  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 756  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 755/756

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 63.8% [56.5, 71.2] | 321 / 1 / 182 | 24 / 12 | 0.065 |
| unpredictable | 79.5% [73.2, 85.1] | 400 / 1 / 103 | 35 / 2 | 1e-08 |
| distinctive | 75.5% [69.1, 81.6] | 380 / 1 / 123 | 36 / 4 | 1.9e-07 |
| prefer | 69.5% [62.1, 76.7] | 350 / 1 / 153 | 30 / 7 | 0.00019 |
| task | 52.8% [47.7, 57.6] | 206 / 120 / 178 | 21 / 16 | 0.51 |

- google/gemini-2.5-flash-lite: original 69%, unpredictable 92%, distinctive 90%, prefer 85%, task 65%

- openai/gpt-4o-mini: original 58%, unpredictable 67%, distinctive 61%, prefer 55%, task 40%
- Position check (prefer): treatment win rate 77% when shown as A (n=268), 61% when shown as B (n=236).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 39.5% [34.1, 44.7] | 198 / 2 / 304 | 11 / 24 | 0.041 |
| unpredictable | 28.7% [24.0, 33.6] | 144 / 1 / 359 | 1 / 35 | 1.1e-09 |
| distinctive | 27.9% [22.3, 33.5] | 140 / 1 / 363 | 5 / 33 | 4.3e-06 |
| prefer | 31.1% [25.1, 37.6] | 156 / 1 / 347 | 5 / 31 | 1.3e-05 |
| task | 39.7% [34.6, 44.6] | 143 / 114 / 247 | 8 / 28 | 0.0012 |

- google/gemini-2.5-flash-lite: original 39%, unpredictable 31%, distinctive 32%, prefer 34%, task 38%

- openai/gpt-4o-mini: original 39%, unpredictable 26%, distinctive 24%, prefer 28%, task 41%
- Position check (prefer): treatment win rate 50% when shown as A (n=236), 15% when shown as B (n=268).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 85% | 0.70 |
| unpredictable | 70% | 0.41 |
| distinctive | 70% | 0.43 |
| prefer | 70% | 0.42 |
| task | 40% | 0.17 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 3.97 | +0.77 [+0.64, +0.90] (40↑/0↓) | -0.15 [-0.25, -0.06] (10↑/23↓) |
| specificity | 3.90 | 4.56 | 4.48 | +0.58 [+0.43, +0.74] (35↑/1↓) | -0.08 [-0.17, -0.00] (11↑/16↓) |
| distinctiveness | 3.28 | 4.18 | 4.06 | +0.79 [+0.65, +0.93] (39↑/1↓) | -0.12 [-0.19, -0.04] (8↑/20↓) |
| coherence | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | -0.01 [-0.03, +0.00] (0↑/2↓) | -0.01 [-0.03, +0.00] (0↑/2↓) |
| creative_risk | 2.34 | 3.35 | 3.18 | +0.85 [+0.65, +1.04] (37↑/3↓) | -0.16 [-0.28, -0.04] (10↑/23↓) |

Second judge (openai/gpt-4o-mini) on 252 outputs: Spearman ρ with the primary judge: originality 0.59, specificity 0.67, distinctiveness 0.62, coherence n/a, task_alignment n/a, creative_risk 0.73

Second judge's own means on that subset: baseline: origi 4.15, coher 5.00, task_ 5.00; oneliner: origi 4.69, coher 5.00, task_ 5.00; bohemian: origi 4.50, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 169.2 | 194.1 | 190.6 | +21.448 [+11.000, +32.794] +13% | -3.508 [-15.972, +5.429] -2% |
| constraint pass rate | 0.940 | 0.870 | 0.884 | -0.056 [-0.106, -0.009] -6% | +0.014 [-0.037, +0.065] +2% |
| clichés /100 words (all) | 0.437 | 0.279 | 0.160 | -0.277 [-0.434, -0.144] -63% | -0.119 [-0.253, -0.026] -43% |
| clichés /100 words (shared with skill) | 0.095 | 0.054 | 0.023 | -0.072 [-0.143, -0.012] -76% | -0.031 [-0.064, +0.001] -57% |
| clichés /100 words (held-out) | 0.342 | 0.225 | 0.137 | -0.205 [-0.364, -0.082] -60% | -0.088 [-0.222, -0.004] -39% |
| typicality (cos to obvious answer) | 0.737 | 0.626 | 0.596 | -0.141 [-0.161, -0.122] -19% | -0.031 [-0.045, -0.016] -5% |
| intra-list similarity (list tasks) | 0.428 | 0.356 | 0.365 | -0.063 [-0.126, -0.008] -15% | +0.009 [-0.008, +0.030] +3% |
| semantic diversity across samples | 0.187 | 0.267 | 0.301 | +0.114 [+0.092, +0.137] +61% | +0.034 [+0.017, +0.050] +13% |
| 3-gram overlap across samples | 0.056 | 0.015 | 0.015 | -0.041 [-0.068, -0.021] -74% | -0.001 [-0.004, +0.004] -4% |
| cross-model similarity | 0.749 | 0.680 | 0.642 | -0.107 [-0.140, -0.078] -14% | -0.038 [-0.056, -0.020] -6% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 64% | 76% | 72% | 67% | 54% | 90% / 90% |
| deepseek/deepseek-v4.1-flash | 63% | 83% | 79% | 72% | 52% | 87% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 3 | 54% | 82% | 57% | 94% / 100% |
| brainstorm | 4 | 98% | 98% | 69% | 100% / 100% |
| character | 3 | 53% | 61% | 50% | 92% / 100% |
| fiction | 4 | 31% | 29% | 24% | 89% / 78% |
| headlines | 3 | 86% | 89% | 61% | 100% / 100% |
| marketing | 4 | 79% | 83% | 47% | 79% / 79% |
| naming | 4 | 75% | 71% | 52% | 100% / 100% |
| poetry | 4 | 75% | 67% | 62% | 75% / 100% |
| positioning | 3 | 64% | 78% | 60% | 78% / 100% |
| rewrite | 3 | 47% | 64% | 64% | 83% / 83% |
| short_story | 4 | 56% | 54% | 48% | 67% / 92% |
| story_concept | 3 | 36% | 64% | 44% | 89% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-5**: prefer 8%, task 8%, original 17%. Constraint failures: 0. Judge: "Response A feels more complete as an opening paragraph, establishing setting, character, and a sense of melancholy, while Response B is more focused on a specific interaction that feels less like an opening."
- **fiction-2**: prefer 17%, task 17%, original 42%. Constraint failures: 1. Judge: "Response B feels more emotionally resonant and captures the subtle grief and shared history of the siblings more effectively, while still fulfilling the prompt's requirements."
- **rewrite-3**: prefer 25%, task 42%, original 50%. Constraint failures: 2. Judge: "Response A is more vivid and less predictable, using stronger imagery and more evocative language while still adhering to the original events and emotional tone."
- **fiction-3**: prefer 42%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A offers a unique perspective on lost items in an airport, while Response B captures a poignant human interaction that aligns closely with the brief's emotional tone."
- **fiction-4**: prefer 50%, task 33%, original 33%. Constraint failures: 1. Judge: "Response A presents a more engaging and imaginative ghost story suitable for 10-year-olds, while Response B, though intriguing, lacks the warmth and clarity needed for the target audience."
- **story_concept-4**: prefer 50%, task 33%, original 33%. Constraint failures: 0. Judge: "Response A presents a more cohesive and imaginative world that aligns closely with the brief's requirements for a tabletop role-playing game setting."
- **naming-3**: prefer 42%, task 42%, original 33%. Constraint failures: 0. Judge: "Response B offers more unique and evocative names that better fit the brief's implied need for a memorable habit-tracking app, while both responses adhere to the formatting requirements."
- **marketing-4**: prefer 58%, task 29%, original 75%. Constraint failures: 3. Judge: "Response B is a more complete and inviting radio ad, fulfilling the brief's implied need for a compelling advertisement, whereas Response A is more of a stark, almost anti-advertising statement."
