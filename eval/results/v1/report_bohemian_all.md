# Benchmark report: run `v1`, split `all`, treatment `bohemian`

- Tasks: 54  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 972  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 964/972

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 58.5% [52.9, 64.0] | 377 / 4 / 267 | 29 / 17 | 0.1 |
| unpredictable | 74.5% [69.3, 79.2] | 480 / 5 / 163 | 43 / 5 | 1.4e-08 |
| distinctive | 70.1% [64.9, 75.2] | 452 / 5 / 191 | 43 / 9 | 2e-06 |
| prefer | 61.9% [56.0, 67.6] | 399 / 4 / 245 | 37 / 15 | 0.0032 |
| task | 47.5% [43.6, 51.5] | 232 / 152 / 264 | 20 / 30 | 0.2 |

- google/gemini-2.5-flash-lite: original 63%, unpredictable 85%, distinctive 84%, prefer 77%, task 59%

- openai/gpt-4o-mini: original 54%, unpredictable 64%, distinctive 56%, prefer 47%, task 36%
- Position check (prefer): treatment win rate 76% when shown as A (n=326), 48% when shown as B (n=322).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 39.8% [35.3, 44.2] | 257 / 2 / 389 | 9 / 34 | 0.00017 |
| unpredictable | 25.3% [20.9, 30.0] | 162 / 4 / 482 | 2 / 49 | 1.2e-12 |
| distinctive | 25.9% [21.7, 30.4] | 167 / 2 / 479 | 2 / 49 | 1.2e-12 |
| prefer | 26.6% [22.0, 31.4] | 172 / 1 / 475 | 4 / 47 | 2.4e-10 |
| task | 37.1% [32.9, 40.9] | 173 / 135 / 340 | 7 / 39 | 1.8e-06 |

- google/gemini-2.5-flash-lite: original 39%, unpredictable 30%, distinctive 31%, prefer 31%, task 35%

- openai/gpt-4o-mini: original 41%, unpredictable 21%, distinctive 21%, prefer 22%, task 39%
- Position check (prefer): treatment win rate 42% when shown as A (n=314), 12% when shown as B (n=334).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 84% | 0.68 |
| unpredictable | 73% | 0.48 |
| distinctive | 72% | 0.46 |
| prefer | 72% | 0.45 |
| task | 43% | 0.18 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.23 | 4.19 | 3.98 | +0.74 [+0.62, +0.86] (51↑/2↓) | -0.22 [-0.31, -0.14] (9↑/36↓) |
| specificity | 3.93 | 4.56 | 4.48 | +0.54 [+0.40, +0.69] (45↑/3↓) | -0.09 [-0.19, +0.00] (13↑/18↓) |
| distinctiveness | 3.31 | 4.23 | 4.05 | +0.74 [+0.61, +0.87] (50↑/1↓) | -0.17 [-0.25, -0.10] (9↑/33↓) |
| coherence | 5.00 | 5.00 | 4.99 | -0.01 [-0.02, +0.00] (0↑/2↓) | -0.01 [-0.02, +0.00] (0↑/2↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | -0.01 [-0.02, +0.00] (0↑/1↓) | -0.01 [-0.02, +0.00] (0↑/1↓) |
| creative_risk | 2.37 | 3.41 | 3.17 | +0.81 [+0.65, +0.96] (49↑/1↓) | -0.23 [-0.33, -0.14] (11↑/34↓) |

Second judge (openai/gpt-4o-mini) on 324 outputs: Spearman ρ with the primary judge: originality 0.62, specificity 0.70, distinctiveness 0.64, coherence 1.00, task_alignment 0.71, creative_risk 0.74

Second judge's own means on that subset: baseline: origi 4.19, coher 5.00, task_ 5.00; oneliner: origi 4.73, coher 5.00, task_ 5.00; bohemian: origi 4.43, coher 4.99, task_ 4.96

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 185.0 | 212.3 | 199.4 | +14.333 [+5.892, +23.803] +8% | -12.907 [-24.500, -2.204] -6% |
| constraint pass rate | 0.948 | 0.881 | 0.901 | -0.048 [-0.087, -0.012] -5% | +0.020 [-0.032, +0.071] +2% |
| clichés /100 words (all) | 1.213 | 0.234 | 0.169 | -1.044 [-2.650, -0.171] -86% | -0.065 [-0.177, +0.021] -28% |
| clichés /100 words (shared with skill) | 0.097 | 0.050 | 0.049 | -0.049 [-0.112, +0.010] -50% | -0.002 [-0.035, +0.040] -3% |
| clichés /100 words (held-out) | 1.116 | 0.183 | 0.120 | -0.996 [-2.601, -0.136] -89% | -0.063 [-0.172, +0.006] -34% |
| typicality (cos to obvious answer) | 0.733 | 0.618 | 0.590 | -0.143 [-0.162, -0.125] -19% | -0.027 [-0.042, -0.013] -4% |
| intra-list similarity (list tasks) | 0.429 | 0.349 | 0.360 | -0.069 [-0.130, -0.016] -16% | +0.011 [-0.004, +0.026] +3% |
| semantic diversity across samples | 0.190 | 0.271 | 0.312 | +0.122 [+0.100, +0.146] +64% | +0.041 [+0.023, +0.059] +15% |
| 3-gram overlap across samples | 0.052 | 0.015 | 0.013 | -0.039 [-0.060, -0.023] -75% | -0.001 [-0.005, +0.002] -9% |
| cross-model similarity | 0.745 | 0.680 | 0.627 | -0.117 [-0.147, -0.091] -16% | -0.052 [-0.072, -0.033] -8% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 58% | 74% | 68% | 59% | 50% | 88% / 91% |
| deepseek/deepseek-v4.1-flash | 59% | 75% | 72% | 64% | 46% | 92% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 4 | 57% | 70% | 46% | 94% / 100% |
| brainstorm | 5 | 87% | 93% | 63% | 100% / 100% |
| character | 4 | 52% | 50% | 45% | 100% / 100% |
| fiction | 5 | 27% | 33% | 27% | 78% / 78% |
| headlines | 4 | 79% | 79% | 54% | 96% / 100% |
| marketing | 5 | 65% | 73% | 48% | 79% / 79% |
| naming | 5 | 68% | 66% | 41% | 97% / 100% |
| poetry | 5 | 55% | 52% | 52% | 75% / 100% |
| positioning | 4 | 69% | 65% | 55% | 96% / 100% |
| rewrite | 4 | 54% | 58% | 52% | 75% / 88% |
| short_story | 5 | 48% | 43% | 42% | 75% / 92% |
| story_concept | 4 | 42% | 62% | 47% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 17%, task 17%, original 17%. Constraint failures: 0. Judge: "Response A feels more fully realized, with a stronger emotional arc and a more developed sense of character and setting."
- **fiction-5**: prefer 25%, task 12%, original 8%. Constraint failures: 1. Judge: "Response A feels more complete and evocative, while Response B introduces an interesting backstory but feels less fully realized."
- **poetry-1**: prefer 25%, task 25%, original 42%. Constraint failures: 0. Judge: "Response A offers a more profound and evocative exploration of the ocean's memory and power, while Response B feels a bit too mundane and repetitive."
- **character-1**: prefer 25%, task 33%, original 42%. Constraint failures: 0. Judge: "Response A provides a more fully developed and immediately usable protagonist that fits the brief, while Response B is more experimental and less clearly defined."
- **fiction-3**: prefer 33%, task 29%, original 33%. Constraint failures: 0. Judge: "Response A presents a more cohesive narrative that aligns closely with the brief, while Response B, though interesting, feels more like a vignette than flash fiction."
- **short_story-2**: prefer 25%, task 38%, original 58%. Constraint failures: 1. Judge: "Response B presents a more engaging and unpredictable narrative that aligns closely with the brief's requirements."
- **short_story-1**: prefer 33%, task 33%, original 33%. Constraint failures: 0. Judge: "Response B provides a more relatable and engaging narrative that aligns closely with the brief, while Response A, though unique, focuses on a less conventional perspective that may not resonate as strongly with the theme of a first day at a new job."
- **short_story-3**: prefer 33%, task 38%, original 42%. Constraint failures: 0. Judge: "Response A offers a more compelling narrative with a stronger character arc and a more impactful ending, while Response B feels a bit more generic in its premise and execution."
