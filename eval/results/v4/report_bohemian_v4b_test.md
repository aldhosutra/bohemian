# Benchmark report: run `v4`, split `test`, treatment `bohemian_v4b`

- Tasks: 42  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian_v4, bohemian_v4b  
- Generations analysed: 1008  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 1006/1008

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v4b vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 61.1% [53.8, 68.3] | 307 / 2 / 195 | 26 / 12 | 0.034 |
| unpredictable | 80.6% [73.6, 86.9] | 405 / 2 / 97 | 34 / 3 | 1.2e-07 |
| distinctive | 75.4% [68.1, 82.5] | 379 / 2 / 123 | 30 / 6 | 7e-05 |
| prefer | 68.0% [60.0, 76.0] | 342 / 1 / 161 | 26 / 10 | 0.011 |
| task | 45.1% [40.1, 49.9] | 166 / 123 / 215 | 16 / 23 | 0.34 |

- google/gemini-2.5-flash-lite: original 66%, unpredictable 88%, distinctive 88%, prefer 82%, task 58%

- openai/gpt-4o-mini: original 56%, unpredictable 73%, distinctive 63%, prefer 54%, task 32%
- Position check (prefer): treatment win rate 77% when shown as A (n=246), 60% when shown as B (n=258).

### bohemian_v4b vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 46.8% [41.7, 52.0] | 235 / 2 / 267 | 15 / 22 | 0.32 |
| unpredictable | 34.1% [29.4, 38.9] | 171 / 2 / 331 | 4 / 34 | 6e-07 |
| distinctive | 35.1% [30.1, 40.2] | 176 / 2 / 326 | 6 / 29 | 0.00012 |
| prefer | 32.7% [27.8, 37.8] | 164 / 2 / 338 | 5 / 32 | 7.4e-06 |
| task | 39.3% [34.6, 43.8] | 141 / 114 / 249 | 8 / 29 | 0.00075 |

- google/gemini-2.5-flash-lite: original 47%, unpredictable 42%, distinctive 42%, prefer 40%, task 40%

- openai/gpt-4o-mini: original 47%, unpredictable 27%, distinctive 28%, prefer 26%, task 38%
- Position check (prefer): treatment win rate 50% when shown as A (n=274), 13% when shown as B (n=230).

### bohemian_v4b vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 50.4% [44.8, 56.0] | 253 / 2 / 249 | 15 / 14 | 1 |
| unpredictable | 53.6% [49.2, 58.1] | 269 / 2 / 233 | 22 / 14 | 0.24 |
| distinctive | 55.3% [50.5, 60.1] | 277 / 3 / 224 | 21 / 11 | 0.11 |
| prefer | 56.6% [51.9, 61.5] | 285 / 1 / 218 | 24 / 11 | 0.041 |
| task | 50.4% [45.7, 55.2] | 205 / 98 / 201 | 17 / 20 | 0.74 |

- google/gemini-2.5-flash-lite: original 50%, unpredictable 47%, distinctive 50%, prefer 52%, task 50%

- openai/gpt-4o-mini: original 50%, unpredictable 60%, distinctive 61%, prefer 61%, task 51%
- Position check (prefer): treatment win rate 79% when shown as A (n=236), 37% when shown as B (n=268).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 86% | 0.72 |
| unpredictable | 69% | 0.38 |
| distinctive | 69% | 0.39 |
| prefer | 70% | 0.41 |
| task | 43% | 0.20 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian_v4 | bohemian_v4b | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 4.04 | n/a | 4.03 | +0.83 [+0.69, +0.96] (40↑/0↓) | -0.10 [-0.19, -0.00] (10↑/20↓) | -0.01 [-0.10, +0.08] (14↑/15↓) |
| specificity | 3.90 | 4.56 | 4.58 | n/a | 4.54 | +0.64 [+0.48, +0.81] (36↑/1↓) | -0.02 [-0.15, +0.08] (13↑/11↓) | -0.04 [-0.12, +0.04] (12↑/17↓) |
| distinctiveness | 3.28 | 4.18 | 4.13 | n/a | 4.11 | +0.83 [+0.69, +0.97] (41↑/0↓) | -0.07 [-0.15, +0.01] (12↑/19↓) | -0.02 [-0.10, +0.06] (10↑/19↓) |
| coherence | 5.00 | 5.00 | 5.00 | n/a | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | n/a | 4.99 | -0.01 [-0.02, +0.00] (0↑/1↓) | -0.01 [-0.02, +0.00] (0↑/1↓) | +0.00 [-0.02, +0.03] (2↑/1↓) |
| creative_risk | 2.34 | 3.35 | 3.31 | n/a | 3.31 | +0.97 [+0.77, +1.18] (39↑/2↓) | -0.04 [-0.19, +0.10] (15↑/19↓) | -0.01 [-0.15, +0.14] (15↑/19↓) |

Second judge (openai/gpt-4o-mini) on 336 outputs: Spearman ρ with the primary judge: originality 0.56, specificity 0.63, distinctiveness 0.56, coherence n/a, task_alignment 0.50, creative_risk 0.66

Second judge's own means on that subset: baseline: origi 4.15, coher 5.00, task_ 5.00; oneliner: origi 4.69, coher 5.00, task_ 5.00; antialgorithm: origi 4.51, coher 5.00, task_ 4.98; bohemian_v4b: origi 4.60, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian_v4 | bohemian_v4b | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| words | 169.2 | 194.1 | 169.1 | n/a | 172.8 | +3.623 [-6.854, +13.528] +2% | -21.333 [-33.508, -10.476] -11% | +3.694 [-9.960, +21.143] +2% |
| constraint pass rate | 0.940 | 0.870 | 0.884 | n/a | 0.949 | +0.009 [-0.032, +0.051] +1% | +0.079 [+0.009, +0.148] +9% | +0.065 [+0.019, +0.106] +7% |
| clichés /100 words (all) | 0.437 | 0.279 | 0.026 | n/a | 0.179 | -0.259 [-0.520, -0.019] -59% | -0.101 [-0.229, -0.012] -36% | +0.153 [-0.001, +0.370] +585% |
| clichés /100 words (shared with skill) | 0.192 | 0.116 | 0.019 | n/a | 0.152 | -0.040 [-0.224, +0.149] -21% | +0.036 [-0.080, +0.197] +31% | +0.133 [-0.017, +0.355] +685% |
| clichés /100 words (held-out) | 0.245 | 0.163 | 0.007 | n/a | 0.027 | -0.218 [-0.371, -0.099] -89% | -0.137 [-0.279, -0.034] -84% | +0.020 [+0.003, +0.041] +296% |
| typicality (cos to obvious answer) | 0.737 | 0.626 | 0.549 | n/a | 0.582 | -0.155 [-0.175, -0.136] -21% | -0.044 [-0.059, -0.031] -7% | +0.033 [+0.020, +0.047] +6% |
| intra-list similarity (list tasks) | 0.428 | 0.356 | 0.333 | n/a | 0.354 | -0.074 [-0.130, -0.026] -17% | -0.002 [-0.013, +0.008] -1% | +0.021 [+0.004, +0.040] +6% |
| semantic diversity across samples | 0.187 | 0.267 | 0.323 | n/a | 0.319 | +0.132 [+0.110, +0.155] +71% | +0.052 [+0.031, +0.072] +19% | -0.004 [-0.026, +0.018] -1% |
| 3-gram overlap across samples | 0.056 | 0.015 | 0.012 | n/a | 0.010 | -0.046 [-0.074, -0.025] -82% | -0.005 [-0.009, -0.002] -32% | -0.002 [-0.004, +0.001] -14% |
| cross-model similarity | 0.749 | 0.680 | 0.618 | n/a | 0.638 | -0.111 [-0.142, -0.082] -15% | -0.042 [-0.058, -0.025] -6% | +0.020 [+0.002, +0.039] +3% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 59% | 79% | 72% | 66% | 44% | 94% / 90% |
| deepseek/deepseek-v4.1-flash | 63% | 83% | 79% | 70% | 46% | 96% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 3 | 58% | 85% | 60% | 100% / 100% |
| brainstorm | 4 | 92% | 96% | 60% | 100% / 100% |
| character | 3 | 47% | 39% | 38% | 100% / 100% |
| fiction | 4 | 40% | 40% | 34% | 83% / 78% |
| headlines | 3 | 92% | 92% | 50% | 100% / 100% |
| marketing | 4 | 69% | 77% | 38% | 92% / 79% |
| naming | 4 | 73% | 90% | 49% | 100% / 100% |
| poetry | 4 | 46% | 52% | 45% | 92% / 100% |
| positioning | 3 | 64% | 75% | 46% | 100% / 100% |
| rewrite | 3 | 39% | 44% | 29% | 94% / 83% |
| short_story | 4 | 56% | 65% | 46% | 67% / 92% |
| story_concept | 3 | 56% | 58% | 47% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **rewrite-3**: prefer 8%, task 0%, original 33%. Constraint failures: 1. Judge: "Response A uses more evocative imagery and sensory details to create a more vivid and less predictable portrayal of Sarah's sadness."
- **fiction-2**: prefer 17%, task 0%, original 0%. Constraint failures: 1. Judge: "Response A feels more emotionally resonant and captures the bittersweet nature of the task with a stronger narrative arc, while Response B is a bit more detached and less focused on the emotional core of the siblings' interaction."
- **fiction-5**: prefer 25%, task 25%, original 50%. Constraint failures: 1. Judge: "Response B provides a more engaging and emotionally resonant opening that aligns closely with the brief's theme of a family-run hardware store facing closure."
- **character-3**: prefer 33%, task 29%, original 33%. Constraint failures: 0. Judge: "Response A fully fleshes out a character with a clear gimmick, specific examples, and even a sample scene, making her feel more realized and ready to steal scenes. Response B offers a good concept but lacks the depth and illustrative detail to fully bring the character to life."
- **poetry-4**: prefer 33%, task 33%, original 17%. Constraint failures: 0. Judge: "Response A offers a more unique perspective on the city's nighttime activities, while Response B, though distinctive, leans towards more familiar imagery."
- **marketing-3**: prefer 42%, task 29%, original 58%. Constraint failures: 0. Judge: "Response A is more original and distinctive, offering a stronger headline and a more comprehensive paragraph that directly addresses the freelancer's pain points and the app's solutions."
- **story_concept-2**: prefer 33%, task 42%, original 42%. Constraint failures: 0. Judge: "Response B presents a more unique and imaginative premise, while Response A is more straightforward and conventional."
- **character-4**: prefer 33%, task 42%, original 33%. Constraint failures: 0. Judge: "Response A feels more complete as a character sketch, offering a clearer arc and a more resonant closing line, while Response B is more unique in its details but less focused on the mentor-mentee relationship."
