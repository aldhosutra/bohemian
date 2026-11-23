# Benchmark report: run `v4`, split `dev`, treatment `bohemian_v4`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian_v4  
- Generations analysed: 288  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 287/288

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian_v4 vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 56.9% [46.5, 68.1] | 82 / 0 / 62 | 6 / 4 | 0.75 |
| unpredictable | 75.7% [66.0, 84.0] | 109 / 0 / 35 | 10 / 1 | 0.012 |
| distinctive | 72.9% [62.5, 81.9] | 105 / 0 / 39 | 10 / 1 | 0.012 |
| prefer | 62.5% [52.1, 73.6] | 90 / 0 / 54 | 8 / 3 | 0.23 |
| task | 46.9% [41.3, 52.8] | 51 / 33 / 60 | 3 / 6 | 0.51 |

- google/gemini-2.5-flash-lite: original 62%, unpredictable 86%, distinctive 86%, prefer 78%, task 55%

- openai/gpt-4o-mini: original 51%, unpredictable 65%, distinctive 60%, prefer 47%, task 39%
- Position check (prefer): treatment win rate 78% when shown as A (n=68), 49% when shown as B (n=76).

### bohemian_v4 vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 42.4% [33.3, 50.7] | 61 / 0 / 83 | 2 / 6 | 0.29 |
| unpredictable | 27.1% [20.8, 33.3] | 39 / 0 / 105 | 0 / 12 | 0.00049 |
| distinctive | 27.1% [20.1, 34.0] | 39 / 0 / 105 | 0 / 11 | 0.00098 |
| prefer | 29.2% [21.5, 36.8] | 42 / 0 / 102 | 0 / 10 | 0.002 |
| task | 37.8% [31.2, 44.1] | 38 / 33 / 73 | 1 / 9 | 0.021 |

- google/gemini-2.5-flash-lite: original 42%, unpredictable 35%, distinctive 35%, prefer 36%, task 38%

- openai/gpt-4o-mini: original 43%, unpredictable 19%, distinctive 19%, prefer 22%, task 38%
- Position check (prefer): treatment win rate 46% when shown as A (n=80), 8% when shown as B (n=64).

### bohemian_v4 vs antialgorithm

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 49.3% [41.0, 58.3] | 71 / 0 / 73 | 5 / 6 | 1 |
| unpredictable | 53.5% [45.8, 61.8] | 77 / 0 / 67 | 6 / 5 | 1 |
| distinctive | 62.2% [56.6, 68.1] | 89 / 1 / 54 | 11 / 1 | 0.0063 |
| prefer | 61.1% [55.6, 67.4] | 88 / 0 / 56 | 8 / 0 | 0.0078 |
| task | 56.9% [50.0, 64.6] | 70 / 24 / 50 | 8 / 2 | 0.11 |

- google/gemini-2.5-flash-lite: original 47%, unpredictable 44%, distinctive 52%, prefer 51%, task 53%

- openai/gpt-4o-mini: original 51%, unpredictable 62%, distinctive 72%, prefer 71%, task 61%
- Position check (prefer): treatment win rate 86% when shown as A (n=64), 41% when shown as B (n=80).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 85% | 0.70 |
| unpredictable | 72% | 0.44 |
| distinctive | 74% | 0.47 |
| prefer | 72% | 0.45 |
| task | 47% | 0.25 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian_v4 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.07 | 4.03 | +0.68 [+0.40, +0.99] (12↑/0↓) | -0.42 [-0.64, -0.18] (2↑/10↓) | -0.04 [-0.22, +0.15] (3↑/5↓) |
| specificity | 4.04 | 4.57 | 4.65 | 4.42 | +0.38 [+0.06, +0.74] (9↑/2↓) | -0.15 [-0.39, +0.07] (2↑/5↓) | -0.24 [-0.40, -0.10] (0↑/7↓) |
| distinctiveness | 3.44 | 4.39 | 4.11 | 4.04 | +0.60 [+0.33, +0.90] (11↑/0↓) | -0.35 [-0.57, -0.11] (2↑/10↓) | -0.07 [-0.24, +0.12] (2↑/6↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.94 | 4.97 | -0.03 [-0.08, +0.00] (0↑/1↓) | -0.03 [-0.08, +0.00] (0↑/1↓) | +0.03 [+0.00, +0.08] (1↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.36 | 3.35 | +0.87 [+0.53, +1.25] (12↑/0↓) | -0.28 [-0.54, -0.00] (2↑/9↓) | -0.01 [-0.24, +0.25] (4↑/5↓) |

Second judge (openai/gpt-4o-mini) on 96 outputs: Spearman ρ with the primary judge: originality 0.61, specificity 0.70, distinctiveness 0.68, coherence n/a, task_alignment n/a, creative_risk 0.70

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; antialgorithm: origi 4.58, coher 5.00, task_ 5.00; bohemian_v4: origi 4.67, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian_v4 | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] | Δ vs antialgorithm [95% CI] |
|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 207.0 | 237.2 | -3.264 [-25.862, +14.070] -1% | -38.500 [-70.612, -11.651] -14% | +30.181 [-7.611, +70.987] +15% |
| constraint pass rate | 1.000 | 0.944 | 0.917 | 0.889 | -0.111 [-0.278, +0.000] -11% | -0.056 [-0.111, +0.000] -6% | -0.028 [-0.194, +0.139] -3% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.103 | 0.498 | -3.430 [-9.749, +0.003] -87% | +0.424 [-0.054, +1.177] +573% | +0.396 [-0.005, +1.122] +385% |
| clichés /100 words (shared with skill) | 0.029 | 0.013 | 0.084 | 0.055 | +0.026 [-0.054, +0.114] +90% | +0.042 [-0.017, +0.122] +331% | -0.029 [-0.088, +0.013] -35% |
| clichés /100 words (held-out) | 3.900 | 0.061 | 0.019 | 0.444 | -3.456 [-9.724, -0.057] -89% | +0.382 [-0.064, +1.119] +622% | +0.425 [+0.002, +1.143] +2260% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.514 | 0.570 | -0.141 [-0.185, -0.101] -20% | -0.010 [-0.045, +0.029] -2% | +0.056 [+0.031, +0.078] +11% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.283 | 0.301 | -0.132 [-0.326, -0.016] -30% | -0.026 [-0.055, -0.007] -8% | +0.018 [-0.006, +0.045] +6% |
| semantic diversity across samples | 0.203 | 0.285 | 0.365 | 0.320 | +0.117 [+0.086, +0.147] +58% | +0.035 [+0.002, +0.066] +12% | -0.045 [-0.067, -0.022] -12% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.006 | 0.009 | -0.031 [-0.055, -0.012] -76% | -0.003 [-0.008, +0.001] -25% | +0.003 [+0.000, +0.007] +55% |
| cross-model similarity | 0.729 | 0.679 | 0.593 | 0.625 | -0.104 [-0.143, -0.064] -14% | -0.054 [-0.085, -0.018] -8% | +0.032 [+0.001, +0.064] +5% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 61% | 76% | 75% | 65% | 49% | 94% / 100% |
| deepseek/deepseek-v4.1-flash | 53% | 75% | 71% | 60% | 45% | 83% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 83% | 83% | 50% | n/a / n/a |
| brainstorm | 1 | 83% | 83% | 58% | 100% / 100% |
| character | 1 | 33% | 33% | 42% | n/a / n/a |
| fiction | 1 | 33% | 42% | 33% | n/a / n/a |
| headlines | 1 | 83% | 100% | 58% | 100% / 100% |
| marketing | 1 | 42% | 50% | 42% | n/a / n/a |
| naming | 1 | 50% | 58% | 33% | 100% / 100% |
| poetry | 1 | 33% | 42% | 33% | n/a / n/a |
| positioning | 1 | 75% | 75% | 46% | 100% / 100% |
| rewrite | 1 | 58% | 58% | 67% | 50% / 100% |
| short_story | 1 | 58% | 67% | 50% | n/a / n/a |
| story_concept | 1 | 50% | 58% | 50% | 83% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 42%, task 33%, original 33%. Constraint failures: 0. Judge: "Response A tells a more complete and satisfying story, while Response B feels more like a vignette with an unresolved ending."
- **poetry-1**: prefer 42%, task 33%, original 33%. Constraint failures: 0. Judge: "Response A provides a more traditional and evocative poem about the ocean, while Response B, though unique, strays from the poetic form and theme requested in the brief."
- **character-1**: prefer 33%, task 42%, original 33%. Constraint failures: 0. Judge: "Response A offers a more developed and unusual protagonist with a compelling flaw that directly impacts her ability to solve mysteries, creating richer narrative potential."
- **marketing-1**: prefer 50%, task 42%, original 42%. Constraint failures: 0. Judge: "Response B is a complete advertisement that fulfills the brief, while Response A is a set of notes and a plan that does not deliver the requested output."
- **naming-1**: prefer 58%, task 33%, original 50%. Constraint failures: 0. Judge: "Response B offers more creative and relevant names that directly relate to cleaning and Mac technology, whereas Response A's suggestions are more generic."
- **story_concept-1**: prefer 58%, task 50%, original 50%. Constraint failures: 1. Judge: "Response B offers a more unique and imaginative concept, while both responses adhere to the paragraph format."
- **short_story-1**: prefer 67%, task 50%, original 58%. Constraint failures: 0. Judge: "Response A tells a more complete and engaging story about a first day at a new job, while Response B feels more like a series of observations about a difficult onboarding process."
- **positioning-1**: prefer 75%, task 46%, original 75%. Constraint failures: 0. Judge: "Response A provides a clearer positioning statement and tagline that align well with the brief, while Response B is more abstract and less focused on the target audience."
