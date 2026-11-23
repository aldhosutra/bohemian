# Benchmark report: run `v3`, split `all`, treatment `bohemian`

- Tasks: 54  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 972  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 970/972

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 61.7% [55.3, 67.8] | 398 / 3 / 247 | 29 / 14 | 0.032 |
| unpredictable | 80.2% [75.1, 85.0] | 517 / 5 / 126 | 47 / 3 | 3.7e-11 |
| distinctive | 77.5% [72.0, 82.9] | 501 / 3 / 144 | 45 / 4 | 8.2e-10 |
| prefer | 69.7% [63.2, 76.1] | 450 / 3 / 195 | 39 / 10 | 3.8e-05 |
| task | 50.0% [46.2, 53.8] | 244 / 160 / 244 | 24 / 24 | 1 |

- google/gemini-2.5-flash-lite: original 68%, unpredictable 90%, distinctive 88%, prefer 83%, task 62%

- openai/gpt-4o-mini: original 55%, unpredictable 71%, distinctive 67%, prefer 56%, task 38%
- Position check (prefer): treatment win rate 81% when shown as A (n=326), 58% when shown as B (n=322).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 43.4% [39.0, 47.7] | 280 / 2 / 366 | 14 / 28 | 0.044 |
| unpredictable | 33.8% [28.9, 38.7] | 218 / 2 / 428 | 9 / 38 | 2.5e-05 |
| distinctive | 35.1% [29.8, 40.7] | 226 / 3 / 419 | 9 / 37 | 4.1e-05 |
| prefer | 34.0% [28.6, 39.6] | 220 / 1 / 427 | 8 / 41 | 2e-06 |
| task | 40.7% [35.8, 45.4] | 192 / 144 / 312 | 14 / 36 | 0.0026 |

- google/gemini-2.5-flash-lite: original 42%, unpredictable 38%, distinctive 38%, prefer 36%, task 42%

- openai/gpt-4o-mini: original 45%, unpredictable 30%, distinctive 32%, prefer 32%, task 40%
- Position check (prefer): treatment win rate 52% when shown as A (n=314), 17% when shown as B (n=334).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 84% | 0.68 |
| unpredictable | 73% | 0.47 |
| distinctive | 75% | 0.50 |
| prefer | 74% | 0.50 |
| task | 42% | 0.20 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.23 | 4.19 | 4.07 | +0.83 [+0.72, +0.95] (52↑/0↓) | -0.13 [-0.20, -0.05] (11↑/28↓) |
| specificity | 3.93 | 4.56 | 4.55 | +0.62 [+0.48, +0.77] (43↑/0↓) | -0.02 [-0.10, +0.06] (21↑/13↓) |
| distinctiveness | 3.31 | 4.23 | 4.15 | +0.84 [+0.70, +0.97] (51↑/0↓) | -0.07 [-0.15, -0.00] (14↑/27↓) |
| coherence | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | -0.01 [-0.02, +0.00] (0↑/1↓) | -0.01 [-0.02, +0.00] (0↑/1↓) |
| creative_risk | 2.37 | 3.41 | 3.32 | +0.95 [+0.79, +1.12] (49↑/0↓) | -0.09 [-0.18, +0.01] (17↑/26↓) |

Second judge (openai/gpt-4o-mini) on 324 outputs: Spearman ρ with the primary judge: originality 0.62, specificity 0.69, distinctiveness 0.67, coherence n/a, task_alignment n/a, creative_risk 0.75

Second judge's own means on that subset: baseline: origi 4.19, coher 5.00, task_ 5.00; oneliner: origi 4.73, coher 5.00, task_ 5.00; bohemian: origi 4.63, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 185.0 | 212.3 | 216.2 | +31.170 [+18.416, +45.043] +17% | +3.929 [-7.093, +15.108] +2% |
| constraint pass rate | 0.948 | 0.881 | 0.913 | -0.036 [-0.071, -0.004] -4% | +0.032 [-0.016, +0.083] +4% |
| clichés /100 words (all) | 1.213 | 0.234 | 0.173 | -1.040 [-2.640, -0.179] -86% | -0.061 [-0.170, +0.021] -26% |
| clichés /100 words (shared with skill) | 0.097 | 0.050 | 0.034 | -0.063 [-0.123, -0.012] -65% | -0.016 [-0.046, +0.011] -32% |
| clichés /100 words (held-out) | 1.116 | 0.183 | 0.139 | -0.977 [-2.574, -0.128] -88% | -0.045 [-0.152, +0.030] -24% |
| typicality (cos to obvious answer) | 0.731 | 0.616 | 0.598 | -0.133 [-0.151, -0.118] -18% | -0.019 [-0.029, -0.007] -3% |
| intra-list similarity (list tasks) | 0.429 | 0.349 | 0.350 | -0.079 [-0.139, -0.025] -18% | +0.001 [-0.015, +0.019] +0% |
| semantic diversity across samples | 0.190 | 0.271 | 0.280 | +0.090 [+0.073, +0.108] +47% | +0.009 [-0.005, +0.023] +3% |
| 3-gram overlap across samples | 0.052 | 0.015 | 0.015 | -0.037 [-0.059, -0.020] -71% | +0.001 [-0.003, +0.004] +4% |
| cross-model similarity | 0.745 | 0.680 | 0.648 | -0.097 [-0.122, -0.074] -13% | -0.032 [-0.048, -0.016] -5% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 62% | 75% | 72% | 66% | 50% | 89% / 91% |
| deepseek/deepseek-v4.1-flash | 62% | 85% | 83% | 73% | 50% | 94% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 4 | 53% | 68% | 52% | 94% / 100% |
| brainstorm | 5 | 87% | 95% | 62% | 100% / 100% |
| character | 4 | 52% | 56% | 52% | 92% / 100% |
| fiction | 5 | 28% | 40% | 33% | 67% / 78% |
| headlines | 4 | 83% | 94% | 57% | 100% / 100% |
| marketing | 5 | 83% | 85% | 52% | 79% / 79% |
| naming | 5 | 75% | 80% | 43% | 100% / 100% |
| poetry | 5 | 60% | 62% | 51% | 92% / 100% |
| positioning | 4 | 60% | 73% | 54% | 92% / 100% |
| rewrite | 4 | 50% | 52% | 42% | 88% / 88% |
| short_story | 5 | 62% | 60% | 58% | 75% / 92% |
| story_concept | 4 | 40% | 71% | 43% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-5**: prefer 0%, task 4%, original 0%. Constraint failures: 0. Judge: "Response A establishes a stronger sense of place and character, while Response B feels a bit more generic and less evocative."
- **fiction-1**: prefer 33%, task 25%, original 25%. Constraint failures: 0. Judge: "Response A presents a more emotionally resonant and unique narrative that aligns closely with the brief about a lonely astronaut."
- **character-4**: prefer 25%, task 42%, original 58%. Constraint failures: 0. Judge: "Response A feels more fully realized, with a stronger sense of character and a more nuanced portrayal of the mentor-mentee relationship."
- **rewrite-1**: prefer 42%, task 25%, original 42%. Constraint failures: 0. Judge: "Response B is more distinctive and original, using stronger metaphors and a more evocative tone while still adhering to the original message."
- **rewrite-3**: prefer 33%, task 42%, original 58%. Constraint failures: 2. Judge: "Response A is more vivid and less predictable, using stronger imagery and more evocative language to convey Sarah's sadness and memories."
- **poetry-1**: prefer 42%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A presents a more cohesive and evocative exploration of the ocean, while Response B, though intriguing, feels less structured and impactful."
- **story_concept-2**: prefer 42%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A offers a more original and compelling premise with a stronger emotional core, while Response B's premise, though interesting, feels slightly less grounded and more predictable in its execution."
- **fiction-2**: prefer 33%, task 50%, original 50%. Constraint failures: 1. Judge: "Response B offers a more distinctive and unpredictable take on the brief, while Response A better satisfies the specific task of dividing up items in the kitchen."
