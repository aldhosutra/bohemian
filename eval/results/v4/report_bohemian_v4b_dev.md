# Benchmark report: run `v4`, split `dev`, treatment `bohemian_v4b`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian_v4, bohemian_v4b  
- Generations analysed: 360  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 359/360

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v4b vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 56.3% [44.4, 68.8] | 81 / 0 / 63 | 6 / 6 | 1 |
| unpredictable | 68.8% [59.0, 78.5] | 99 / 0 / 45 | 10 / 2 | 0.039 |
| distinctive | 65.6% [56.2, 75.0] | 94 / 1 / 49 | 8 / 2 | 0.11 |
| prefer | 58.3% [50.0, 68.1] | 84 / 0 / 60 | 7 / 4 | 0.55 |
| task | 39.6% [32.3, 46.2] | 43 / 28 / 73 | 2 / 8 | 0.11 |

- google/gemini-2.5-flash-lite: original 64%, unpredictable 78%, distinctive 78%, prefer 74%, task 53%

- openai/gpt-4o-mini: original 49%, unpredictable 60%, distinctive 53%, prefer 43%, task 26%
- Position check (prefer): treatment win rate 69% when shown as A (n=72), 47% when shown as B (n=72).

### bohemian_v4b vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 41.7% [30.6, 53.5] | 60 / 0 / 84 | 3 / 8 | 0.23 |
| unpredictable | 19.4% [12.5, 25.7] | 28 / 0 / 116 | 0 / 12 | 0.00049 |
| distinctive | 21.5% [13.2, 29.9] | 31 / 0 / 113 | 0 / 12 | 0.00049 |
| prefer | 24.3% [16.0, 34.0] | 35 / 0 / 109 | 1 / 11 | 0.0063 |
| task | 32.3% [24.7, 41.0] | 36 / 21 / 87 | 1 / 11 | 0.0063 |

- google/gemini-2.5-flash-lite: original 39%, unpredictable 24%, distinctive 28%, prefer 26%, task 30%

- openai/gpt-4o-mini: original 44%, unpredictable 15%, distinctive 15%, prefer 22%, task 35%
- Position check (prefer): treatment win rate 41% when shown as A (n=74), 7% when shown as B (n=70).

### bohemian_v4b vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 58.3% [49.3, 67.4] | 84 / 0 / 60 | 7 / 4 | 0.55 |
| unpredictable | 59.0% [50.0, 67.4] | 85 / 0 / 59 | 8 / 3 | 0.23 |
| distinctive | 61.5% [51.4, 71.2] | 88 / 1 / 55 | 9 / 2 | 0.065 |
| prefer | 61.8% [53.5, 70.1] | 89 / 0 / 55 | 8 / 2 | 0.11 |
| task | 59.0% [52.1, 66.0] | 73 / 24 / 47 | 8 / 3 | 0.23 |

- google/gemini-2.5-flash-lite: original 58%, unpredictable 53%, distinctive 58%, prefer 57%, task 56%

- openai/gpt-4o-mini: original 58%, unpredictable 65%, distinctive 65%, prefer 67%, task 62%
- Position check (prefer): treatment win rate 83% when shown as A (n=72), 40% when shown as B (n=72).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 84% | 0.68 |
| unpredictable | 71% | 0.43 |
| distinctive | 70% | 0.41 |
| prefer | 72% | 0.45 |
| task | 54% | 0.30 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian_v4 | bohemian_v4b | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.07 | 4.03 | 4.18 | +0.83 [+0.57, +1.11] (12↑/0↓) | -0.26 [-0.40, -0.11] (1↑/9↓) | +0.11 [-0.07, +0.28] (7↑/2↓) |
| specificity | 4.04 | 4.57 | 4.65 | 4.42 | 4.54 | +0.50 [+0.25, +0.76] (8↑/0↓) | -0.03 [-0.14, +0.08] (3↑/4↓) | -0.11 [-0.22, +0.00] (1↑/6↓) |
| distinctiveness | 3.44 | 4.39 | 4.11 | 4.04 | 4.22 | +0.78 [+0.57, +1.01] (12↑/0↓) | -0.17 [-0.28, -0.06] (1↑/7↓) | +0.11 [-0.06, +0.26] (7↑/3↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | 4.99 | -0.01 [-0.04, +0.00] (0↑/1↓) | -0.01 [-0.04, +0.00] (0↑/1↓) | -0.01 [-0.04, +0.00] (0↑/1↓) |
| task_alignment | 5.00 | 5.00 | 4.94 | 4.97 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.06 [+0.00, +0.17] (1↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.36 | 3.35 | 3.35 | +0.88 [+0.61, +1.14] (12↑/0↓) | -0.28 [-0.50, -0.06] (2↑/10↓) | -0.01 [-0.24, +0.18] (5↑/2↓) |

Second judge (openai/gpt-4o-mini) on 120 outputs: Spearman ρ with the primary judge: originality 0.62, specificity 0.68, distinctiveness 0.67, coherence n/a, task_alignment n/a, creative_risk 0.69

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; antialgorithm: origi 4.58, coher 5.00, task_ 5.00; bohemian_v4: origi 4.67, coher 5.00, task_ 5.00; bohemian_v4b: origi 4.71, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian_v4 | bohemian_v4b | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 207.0 | 237.2 | 224.0 | -16.472 [-41.500, +5.445] -7% | -51.708 [-90.500, -19.375] -19% | +16.972 [-12.611, +52.794] +8% |
| constraint pass rate | 1.000 | 0.944 | 0.917 | 0.889 | 0.972 | -0.028 [-0.083, +0.000] -3% | +0.028 [-0.083, +0.167] +3% | +0.056 [-0.056, +0.194] +6% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.103 | 0.498 | 0.269 | -3.660 [-10.250, -0.150] -93% | +0.195 [-0.026, +0.602] +263% | +0.166 [-0.146, +0.619] +162% |
| clichés /100 words (shared with skill) | 0.029 | 0.013 | 0.084 | 0.055 | 0.025 | -0.004 [-0.050, +0.045] -13% | +0.012 [-0.014, +0.051] +98% | -0.059 [-0.195, +0.035] -70% |
| clichés /100 words (held-out) | 3.900 | 0.061 | 0.019 | 0.444 | 0.244 | -3.656 [-10.204, -0.137] -94% | +0.182 [-0.058, +0.600] +296% | +0.225 [-0.003, +0.631] +1195% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.514 | 0.570 | 0.553 | -0.158 [-0.208, -0.114] -22% | -0.028 [-0.060, +0.007] -5% | +0.038 [+0.021, +0.055] +7% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.283 | 0.301 | 0.305 | -0.128 [-0.340, +0.016] -30% | -0.022 [-0.069, +0.017] -7% | +0.022 [+0.008, +0.031] +8% |
| semantic diversity across samples | 0.203 | 0.285 | 0.365 | 0.320 | 0.335 | +0.133 [+0.084, +0.181] +66% | +0.050 [+0.003, +0.102] +17% | -0.030 [-0.064, +0.003] -8% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.006 | 0.009 | 0.009 | -0.031 [-0.058, -0.012] -78% | -0.004 [-0.009, +0.000] -32% | +0.003 [-0.000, +0.006] +42% |
| cross-model similarity | 0.729 | 0.679 | 0.593 | 0.625 | 0.624 | -0.105 [-0.158, -0.054] -14% | -0.055 [-0.102, -0.008] -8% | +0.031 [-0.006, +0.068] +5% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 56% | 58% | 58% | 54% | 41% | 100% / 100% |
| deepseek/deepseek-v4.1-flash | 57% | 79% | 73% | 62% | 38% | 94% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 25% | 42% | 17% | n/a / n/a |
| brainstorm | 1 | 92% | 75% | 50% | 100% / 100% |
| character | 1 | 67% | 42% | 21% | n/a / n/a |
| fiction | 1 | 75% | 50% | 46% | n/a / n/a |
| headlines | 1 | 83% | 100% | 50% | 100% / 100% |
| marketing | 1 | 58% | 67% | 54% | n/a / n/a |
| naming | 1 | 83% | 67% | 54% | 100% / 100% |
| poetry | 1 | 33% | 42% | 25% | n/a / n/a |
| positioning | 1 | 33% | 58% | 33% | 100% / 100% |
| rewrite | 1 | 42% | 42% | 42% | 100% / 100% |
| short_story | 1 | 42% | 58% | 42% | n/a / n/a |
| story_concept | 1 | 42% | 58% | 42% | 83% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **analogy-1**: prefer 42%, task 17%, original 25%. Constraint failures: 0. Judge: "Response A provides a clearer and more structured explanation of how the internet works, while Response B, though creative, is less direct and may confuse someone unfamiliar with technology."
- **character-1**: prefer 42%, task 21%, original 67%. Constraint failures: 0. Judge: "Response A provides a fully developed protagonist that fits the brief, while Response B is more of a meta-commentary on developing protagonists and only partially delivers on the prompt."
- **poetry-1**: prefer 42%, task 25%, original 33%. Constraint failures: 0. Judge: "Response B offers a more vivid and imaginative portrayal of the ocean, while Response A is more technical and less evocative."
- **rewrite-1**: prefer 42%, task 42%, original 42%. Constraint failures: 0. Judge: "Response A uses a more developed and consistent metaphor, offering a richer and more engaging rewrite of the original paragraph while still adhering to the core message."
- **positioning-1**: prefer 58%, task 33%, original 33%. Constraint failures: 0. Judge: "Response B is more comprehensive, offering a more detailed positioning statement and a tagline that better captures the essence of the brand's value proposition."
- **fiction-1**: prefer 50%, task 46%, original 75%. Constraint failures: 0. Judge: "Response B offers a more comprehensive exploration of loneliness and connection, aligning closely with the brief while showcasing unique character and emotional depth."
- **short_story-1**: prefer 58%, task 42%, original 42%. Constraint failures: 0. Judge: "Response A tells a more complete and satisfying story about a first day, while Response B is more atmospheric and character-driven but less resolved."
- **story_concept-1**: prefer 58%, task 42%, original 42%. Constraint failures: 1. Judge: "Response A offers a more immediately engaging and unique fantasy concept with a clearer narrative hook, while Response B is also strong but leans into a more common 'miracle as debt' trope."
