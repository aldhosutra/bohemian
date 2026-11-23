# Benchmark report: run `v1`, split `dev`, treatment `bohemian`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 216  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 213/216

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 48.6% [38.9, 58.3] | 70 / 0 / 74 | 4 / 6 | 0.75 |
| unpredictable | 66.0% [54.9, 76.4] | 95 / 0 / 49 | 9 / 3 | 0.15 |
| distinctive | 64.6% [52.8, 75.0] | 93 / 0 / 51 | 9 / 3 | 0.15 |
| prefer | 53.5% [40.3, 66.0] | 77 / 0 / 67 | 7 / 4 | 0.55 |
| task | 36.8% [30.9, 42.7] | 39 / 28 / 77 | 1 / 9 | 0.021 |

- google/gemini-2.5-flash-lite: original 51%, unpredictable 79%, distinctive 76%, prefer 65%, task 51%

- openai/gpt-4o-mini: original 46%, unpredictable 53%, distinctive 53%, prefer 42%, task 22%
- Position check (prefer): treatment win rate 79% when shown as A (n=58), 36% when shown as B (n=86).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 41.0% [34.7, 47.9] | 59 / 0 / 85 | 1 / 7 | 0.07 |
| unpredictable | 26.4% [17.4, 34.7] | 38 / 0 / 106 | 0 / 11 | 0.00098 |
| distinctive | 26.4% [18.1, 34.7] | 38 / 0 / 106 | 0 / 11 | 0.00098 |
| prefer | 27.1% [17.4, 37.5] | 39 / 0 / 105 | 1 / 10 | 0.012 |
| task | 36.1% [29.2, 43.1] | 36 / 32 / 76 | 1 / 8 | 0.039 |

- google/gemini-2.5-flash-lite: original 40%, unpredictable 32%, distinctive 35%, prefer 33%, task 36%

- openai/gpt-4o-mini: original 42%, unpredictable 21%, distinctive 18%, prefer 21%, task 36%
- Position check (prefer): treatment win rate 37% when shown as A (n=78), 15% when shown as B (n=66).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 81% | 0.62 |
| unpredictable | 73% | 0.47 |
| distinctive | 73% | 0.48 |
| prefer | 75% | 0.50 |
| task | 43% | 0.17 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.07 | +0.72 [+0.46, +1.04] (12↑/0↓) | -0.38 [-0.56, -0.18] (1↑/8↓) |
| specificity | 4.04 | 4.57 | 4.51 | +0.47 [+0.21, +0.79] (9↑/0↓) | -0.06 [-0.21, +0.11] (2↑/5↓) |
| distinctiveness | 3.44 | 4.39 | 4.14 | +0.69 [+0.43, +1.00] (11↑/0↓) | -0.25 [-0.40, -0.10] (1↑/9↓) |
| coherence | 5.00 | 5.00 | 4.99 | -0.01 [-0.04, +0.00] (0↑/1↓) | -0.01 [-0.04, +0.00] (0↑/1↓) |
| task_alignment | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.32 | +0.85 [+0.51, +1.19] (11↑/0↓) | -0.31 [-0.51, -0.07] (3↑/8↓) |

Second judge (openai/gpt-4o-mini) on 72 outputs: Spearman ρ with the primary judge: originality 0.63, specificity 0.65, distinctiveness 0.70, coherence 1.00, task_alignment n/a, creative_risk 0.77

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; bohemian: origi 4.62, coher 4.96, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 248.2 | +7.750 [-12.098, +27.375] +3% | -27.486 [-59.069, -0.777] -10% |
| constraint pass rate | 1.000 | 0.944 | 0.944 | -0.056 [-0.167, +0.000] -6% | +0.000 [+0.000, +0.000] +0% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.085 | -3.843 [-10.853, -0.107] -98% | +0.011 [-0.071, +0.098] +15% |
| clichés /100 words (shared with skill) | 0.105 | 0.038 | 0.066 | -0.039 [-0.126, +0.048] -37% | +0.029 [-0.027, +0.094] +76% |
| clichés /100 words (held-out) | 3.823 | 0.036 | 0.019 | -3.804 [-10.815, -0.106] -100% | -0.017 [-0.074, +0.029] -48% |
| typicality (cos to obvious answer) | 0.710 | 0.578 | 0.545 | -0.164 [-0.219, -0.117] -23% | -0.033 [-0.071, +0.010] -6% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.308 | -0.125 [-0.326, -0.006] -29% | -0.019 [-0.056, +0.004] -6% |
| semantic diversity across samples | 0.203 | 0.285 | 0.345 | +0.142 [+0.090, +0.199] +70% | +0.059 [+0.013, +0.113] +21% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.011 | -0.029 [-0.051, -0.011] -72% | -0.001 [-0.006, +0.004] -11% |
| cross-model similarity | 0.729 | 0.679 | 0.601 | -0.129 [-0.188, -0.076] -18% | -0.079 [-0.131, -0.036] -12% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 51% | 67% | 62% | 51% | 39% | 89% / 100% |
| deepseek/deepseek-v4.1-flash | 46% | 65% | 67% | 56% | 35% | 100% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 33% | 50% | 33% | n/a / n/a |
| brainstorm | 1 | 58% | 75% | 38% | 100% / 100% |
| character | 1 | 42% | 25% | 33% | n/a / n/a |
| fiction | 1 | 17% | 17% | 17% | n/a / n/a |
| headlines | 1 | 83% | 83% | 38% | 100% / 100% |
| marketing | 1 | 42% | 58% | 33% | n/a / n/a |
| naming | 1 | 50% | 58% | 38% | 100% / 100% |
| poetry | 1 | 42% | 25% | 25% | n/a / n/a |
| positioning | 1 | 75% | 83% | 54% | 100% / 100% |
| rewrite | 1 | 50% | 58% | 50% | 67% / 100% |
| short_story | 1 | 33% | 33% | 33% | n/a / n/a |
| story_concept | 1 | 58% | 75% | 50% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 17%, task 17%, original 17%. Constraint failures: 0. Judge: "Response A feels more fully realized, with a stronger emotional arc and a more developed sense of character and setting."
- **poetry-1**: prefer 25%, task 25%, original 42%. Constraint failures: 0. Judge: "Response A offers a more profound and evocative exploration of the ocean's memory and power, while Response B feels a bit too mundane and repetitive."
- **character-1**: prefer 25%, task 33%, original 42%. Constraint failures: 0. Judge: "Response A provides a more fully developed and immediately usable protagonist that fits the brief, while Response B is more experimental and less clearly defined."
- **short_story-1**: prefer 33%, task 33%, original 33%. Constraint failures: 0. Judge: "Response B provides a more relatable and engaging narrative that aligns closely with the brief, while Response A, though unique, focuses on a less conventional perspective that may not resonate as strongly with the theme of a first day at a new job."
- **analogy-1**: prefer 50%, task 33%, original 33%. Constraint failures: 0. Judge: "Response A's analogy is more comprehensive and better explains the concepts of packets, routers, and the decentralized nature of the internet, while Response B's analogy feels a bit more disjointed and less complete."
- **marketing-1**: prefer 58%, task 33%, original 42%. Constraint failures: 0. Judge: "Response A is more original and distinctive, offering a more creative and engaging take on the mundane object, while still fulfilling the brief effectively."
- **naming-1**: prefer 58%, task 38%, original 50%. Constraint failures: 0. Judge: "Response A provides more conventional and fitting names for a cleaning app, while Response B offers more abstract and less immediately relevant suggestions."
- **rewrite-1**: prefer 58%, task 50%, original 50%. Constraint failures: 2. Judge: "Response B offers a more vivid and unique interpretation of the motivational message, while Response A, though distinctive, feels more abstract and less aligned with the original intent."
