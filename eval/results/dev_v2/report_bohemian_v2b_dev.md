# Benchmark report: run `dev_v2`, split `dev`, treatment `bohemian_v2b`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian, bohemian_v2b, core  
- Generations analysed: 360  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 359/360

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v2b vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 66.0% [54.2, 77.1] | 95 / 0 / 49 | 9 / 3 | 0.15 |
| unpredictable | 75.7% [63.9, 86.1] | 109 / 0 / 35 | 10 / 2 | 0.039 |
| distinctive | 75.7% [63.2, 86.1] | 109 / 0 / 35 | 10 / 2 | 0.039 |
| prefer | 66.7% [55.6, 77.1] | 96 / 0 / 48 | 9 / 2 | 0.065 |
| task | 53.8% [44.4, 62.5] | 62 / 31 / 51 | 6 / 5 | 1 |

- google/gemini-2.5-flash-lite: original 76%, unpredictable 85%, distinctive 86%, prefer 83%, task 66%

- openai/gpt-4o-mini: original 56%, unpredictable 67%, distinctive 65%, prefer 50%, task 42%
- Position check (prefer): treatment win rate 79% when shown as A (n=78), 52% when shown as B (n=66).

### bohemian_v2b vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 51.4% [40.3, 62.5] | 74 / 0 / 70 | 5 / 5 | 1 |
| unpredictable | 28.5% [19.4, 38.2] | 41 / 0 / 103 | 1 / 10 | 0.012 |
| distinctive | 24.3% [16.0, 33.3] | 35 / 0 / 109 | 0 / 10 | 0.002 |
| prefer | 30.6% [22.2, 39.6] | 44 / 0 / 100 | 1 / 9 | 0.021 |
| task | 42.7% [35.1, 50.3] | 47 / 29 / 68 | 2 / 8 | 0.11 |

- google/gemini-2.5-flash-lite: original 51%, unpredictable 35%, distinctive 35%, prefer 38%, task 42%

- openai/gpt-4o-mini: original 51%, unpredictable 22%, distinctive 14%, prefer 24%, task 43%
- Position check (prefer): treatment win rate 45% when shown as A (n=84), 10% when shown as B (n=60).

### bohemian_v2b vs core

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
| original | 78% | 0.56 |
| unpredictable | 72% | 0.46 |
| distinctive | 69% | 0.41 |
| prefer | 64% | 0.32 |
| task | 45% | 0.21 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | bohemian_v2b | core | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs core [95% CI] |
|---|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.11 | 4.12 | 4.08 | +0.78 [+0.51, +1.06] (12↑/0↓) | -0.32 [-0.44, -0.19] (0↑/10↓) | +0.04 [-0.06, +0.14] (4↑/3↓) |
| specificity | 4.04 | 4.57 | 4.51 | 4.43 | 4.46 | +0.39 [+0.08, +0.71] (10↑/2↓) | -0.14 [-0.33, +0.01] (2↑/5↓) | -0.03 [-0.18, +0.13] (3↑/4↓) |
| distinctiveness | 3.44 | 4.39 | 4.08 | 4.18 | 4.12 | +0.74 [+0.47, +1.03] (11↑/0↓) | -0.21 [-0.35, -0.08] (1↑/8↓) | +0.06 [-0.10, +0.21] (4↑/3↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.25 | 3.29 | 3.24 | +0.82 [+0.53, +1.12] (12↑/0↓) | -0.33 [-0.50, -0.18] (0↑/9↓) | +0.06 [-0.18, +0.32] (5↑/5↓) |

Second judge (openai/gpt-4o-mini) on 120 outputs: Spearman ρ with the primary judge: originality 0.59, specificity 0.63, distinctiveness 0.72, coherence n/a, task_alignment n/a, creative_risk 0.71

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; bohemian: origi 4.54, coher 5.00, task_ 5.00; bohemian_v2b: origi 4.54, coher 5.00, task_ 5.00; core: origi 4.58, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | bohemian_v2b | core | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs core [95% CI] |
|---|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 269.1 | 258.6 | 249.6 | +18.097 [-6.833, +46.014] +8% | -17.139 [-51.570, +13.931] -6% | +8.972 [-12.611, +34.973] +4% |
| constraint pass rate | 1.000 | 0.944 | 0.861 | 0.917 | 0.972 | -0.083 [-0.194, +0.000] -8% | -0.028 [-0.083, +0.000] -3% | -0.056 [-0.111, +0.000] -6% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.089 | 0.046 | 0.181 | -3.883 [-10.867, -0.165] -99% | -0.028 [-0.089, +0.034] -38% | -0.135 [-0.258, -0.036] -75% |
| clichés /100 words (shared with skill) | 0.105 | 0.038 | 0.038 | 0.046 | 0.112 | -0.060 [-0.122, -0.007] -56% | +0.008 [-0.038, +0.058] +22% | -0.066 [-0.136, -0.001] -59% |
| clichés /100 words (held-out) | 3.823 | 0.036 | 0.051 | 0.000 | 0.069 | -3.823 [-10.808, -0.120] -100% | -0.036 [-0.084, +0.000] -100% | -0.069 [-0.148, -0.007] -100% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.573 | 0.572 | 0.565 | -0.139 [-0.194, -0.095] -20% | -0.009 [-0.034, +0.014] -2% | +0.007 [-0.013, +0.027] +1% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.309 | 0.297 | 0.287 | -0.135 [-0.326, -0.025] -31% | -0.029 [-0.056, -0.009] -9% | +0.010 [+0.004, +0.022] +3% |
| semantic diversity across samples | 0.203 | 0.286 | 0.303 | 0.304 | 0.307 | +0.102 [+0.066, +0.133] +50% | +0.019 [-0.012, +0.052] +7% | -0.003 [-0.033, +0.026] -1% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.010 | 0.010 | 0.013 | -0.030 [-0.055, -0.010] -74% | -0.002 [-0.008, +0.002] -19% | -0.003 [-0.010, +0.003] -21% |
| cross-model similarity | 0.729 | 0.679 | 0.641 | 0.625 | 0.649 | -0.105 [-0.136, -0.074] -14% | -0.055 [-0.087, -0.016] -8% | -0.024 [-0.048, +0.003] -4% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 62% | 72% | 74% | 65% | 50% | 94% / 100% |
| deepseek/deepseek-v4.1-flash | 69% | 79% | 78% | 68% | 58% | 89% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 83% | 83% | 75% | n/a / n/a |
| brainstorm | 1 | 58% | 67% | 50% | 100% / 100% |
| character | 1 | 67% | 33% | 42% | n/a / n/a |
| fiction | 1 | 42% | 33% | 38% | n/a / n/a |
| headlines | 1 | 83% | 83% | 62% | 100% / 100% |
| marketing | 1 | 100% | 92% | 75% | n/a / n/a |
| naming | 1 | 42% | 58% | 21% | 100% / 100% |
| poetry | 1 | 75% | 50% | 46% | n/a / n/a |
| positioning | 1 | 75% | 75% | 62% | 100% / 100% |
| rewrite | 1 | 75% | 75% | 67% | 67% / 100% |
| short_story | 1 | 67% | 83% | 67% | n/a / n/a |
| story_concept | 1 | 25% | 67% | 42% | 83% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 33%, task 38%, original 42%. Constraint failures: 0. Judge: "Response A is more original, unpredictable, and distinctive, offering a more developed narrative and character arc that better fulfills the brief."
- **character-1**: prefer 33%, task 42%, original 67%. Constraint failures: 0. Judge: "Response B offers a more unique and evocative protagonist, with a compelling internal conflict that directly serves the mystery genre."
- **naming-1**: prefer 58%, task 21%, original 42%. Constraint failures: 0. Judge: "Response B offers more creative and relevant names that align well with the brief for a Mac cleaning application."
- **poetry-1**: prefer 50%, task 46%, original 75%. Constraint failures: 0. Judge: "Response B offers a more unique perspective and richer imagery, while both responses fulfill the brief effectively."
- **story_concept-1**: prefer 67%, task 42%, original 25%. Constraint failures: 1. Judge: "Response A presents a more original and cohesive concept that aligns closely with the brief while showcasing unique elements and character depth."
- **brainstorm-1**: prefer 67%, task 50%, original 58%. Constraint failures: 0. Judge: "Response A presents more innovative and relevant ideas for underserved markets while maintaining clarity and coherence."
- **positioning-1**: prefer 75%, task 62%, original 75%. Constraint failures: 0. Judge: "Response A provides a clearer and more comprehensive positioning statement that aligns well with the brief, while Response B, though distinctive, is less effective in addressing the broader audience."
- **rewrite-1**: prefer 75%, task 67%, original 75%. Constraint failures: 2. Judge: "Response A uses more evocative and original metaphors, making it significantly more distinctive and engaging while still retaining the core message."
