# Benchmark report: run `v3`, split `test`, treatment `antialgorithm`

- Tasks: 42  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, antialgorithm, bohemian  
- Generations analysed: 1008  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 1005/1008

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### antialgorithm vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 57.0% [50.4, 63.5] | 287 / 1 / 216 | 24 / 13 | 0.099 |
| unpredictable | 78.3% [71.5, 84.5] | 394 / 1 / 109 | 37 / 5 | 4.4e-07 |
| distinctive | 73.3% [66.4, 79.9] | 369 / 1 / 134 | 35 / 6 | 4.9e-06 |
| prefer | 60.6% [53.6, 68.1] | 305 / 1 / 198 | 25 / 12 | 0.047 |
| task | 43.1% [38.9, 47.2] | 161 / 112 / 231 | 14 / 24 | 0.14 |

- google/gemini-2.5-flash-lite: original 62%, unpredictable 88%, distinctive 87%, prefer 77%, task 58%

- openai/gpt-4o-mini: original 52%, unpredictable 69%, distinctive 60%, prefer 44%, task 29%
- Position check (prefer): treatment win rate 70% when shown as A (n=242), 52% when shown as B (n=262).

### antialgorithm vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 40.0% [34.4, 45.6] | 200 / 3 / 301 | 11 / 26 | 0.02 |
| unpredictable | 30.1% [24.8, 35.6] | 150 / 3 / 351 | 4 / 35 | 3.4e-07 |
| distinctive | 29.5% [24.4, 34.9] | 147 / 3 / 354 | 5 / 36 | 7.8e-07 |
| prefer | 27.4% [22.7, 32.0] | 137 / 2 / 365 | 3 / 37 | 1.9e-08 |
| task | 36.1% [30.8, 41.9] | 139 / 86 / 279 | 10 / 30 | 0.0022 |

- google/gemini-2.5-flash-lite: original 38%, unpredictable 39%, distinctive 39%, prefer 35%, task 37%

- openai/gpt-4o-mini: original 41%, unpredictable 21%, distinctive 20%, prefer 20%, task 35%
- Position check (prefer): treatment win rate 42% when shown as A (n=264), 11% when shown as B (n=240).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 77% | 0.54 |
| unpredictable | 72% | 0.46 |
| distinctive | 69% | 0.42 |
| prefer | 67% | 0.37 |
| task | 43% | 0.15 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | antialgorithm | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|---|
| originality | 3.20 | 4.12 | 4.04 | 4.06 | +0.84 [+0.71, +0.97] (40↑/1↓) | -0.08 [-0.17, +0.00] (10↑/23↓) |
| specificity | 3.90 | 4.56 | 4.58 | 4.58 | +0.68 [+0.48, +0.88] (36↑/2↓) | +0.02 [-0.13, +0.13] (18↑/9↓) |
| distinctiveness | 3.28 | 4.18 | 4.13 | 4.16 | +0.85 [+0.71, +1.00] (41↑/1↓) | -0.05 [-0.14, +0.03] (14↑/20↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | 4.99 | -0.01 [-0.03, +0.00] (0↑/2↓) | -0.01 [-0.03, +0.00] (0↑/2↓) |
| creative_risk | 2.34 | 3.35 | 3.31 | 3.31 | +0.98 [+0.78, +1.17] (39↑/2↓) | -0.03 [-0.17, +0.10] (15↑/17↓) |

Second judge (openai/gpt-4o-mini) on 336 outputs: Spearman ρ with the primary judge: originality 0.54, specificity 0.67, distinctiveness 0.57, coherence n/a, task_alignment 0.71, creative_risk 0.68

Second judge's own means on that subset: baseline: origi 4.15, coher 5.00, task_ 5.00; oneliner: origi 4.69, coher 5.00, task_ 5.00; antialgorithm: origi 4.51, coher 5.00, task_ 4.98; bohemian: origi 4.62, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | antialgorithm | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|---|
| words | 169.2 | 194.1 | 169.1 | 203.0 | -0.071 [-17.365, +15.548] -0% | -25.028 [-49.191, -5.484] -13% |
| constraint pass rate | 0.940 | 0.870 | 0.884 | 0.898 | -0.056 [-0.088, -0.023] -6% | +0.014 [-0.042, +0.069] +2% |
| clichés /100 words (all) | 0.437 | 0.279 | 0.026 | 0.205 | -0.411 [-0.786, -0.159] -94% | -0.253 [-0.567, -0.052] -91% |
| clichés /100 words (shared with skill) | 0.095 | 0.054 | 0.019 | 0.034 | -0.076 [-0.151, -0.011] -80% | -0.035 [-0.070, +0.000] -65% |
| clichés /100 words (held-out) | 0.342 | 0.225 | 0.007 | 0.171 | -0.335 [-0.722, -0.092] -98% | -0.218 [-0.529, -0.019] -97% |
| typicality (cos to obvious answer) | 0.737 | 0.626 | 0.549 | 0.605 | -0.188 [-0.209, -0.167] -26% | -0.077 [-0.091, -0.064] -12% |
| intra-list similarity (list tasks) | 0.428 | 0.356 | 0.333 | 0.360 | -0.095 [-0.159, -0.038] -22% | -0.023 [-0.045, -0.001] -6% |
| semantic diversity across samples | 0.187 | 0.267 | 0.323 | 0.276 | +0.136 [+0.113, +0.161] +73% | +0.056 [+0.036, +0.077] +21% |
| 3-gram overlap across samples | 0.056 | 0.015 | 0.012 | 0.017 | -0.044 [-0.071, -0.024] -79% | -0.003 [-0.007, -0.000] -21% |
| cross-model similarity | 0.749 | 0.680 | 0.618 | 0.648 | -0.131 [-0.164, -0.101] -18% | -0.062 [-0.082, -0.042] -9% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 57% | 74% | 68% | 57% | 43% | 90% / 90% |
| deepseek/deepseek-v4.1-flash | 58% | 83% | 79% | 65% | 43% | 87% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 3 | 57% | 71% | 54% | 100% / 100% |
| brainstorm | 4 | 71% | 77% | 46% | 92% / 100% |
| character | 3 | 47% | 42% | 36% | 100% / 100% |
| fiction | 4 | 62% | 38% | 45% | 67% / 78% |
| headlines | 3 | 72% | 89% | 56% | 100% / 100% |
| marketing | 4 | 67% | 65% | 34% | 79% / 79% |
| naming | 4 | 81% | 90% | 49% | 100% / 100% |
| poetry | 4 | 31% | 50% | 34% | 83% / 100% |
| positioning | 3 | 61% | 67% | 62% | 78% / 100% |
| rewrite | 3 | 39% | 50% | 38% | 89% / 83% |
| short_story | 4 | 48% | 35% | 26% | 83% / 92% |
| story_concept | 3 | 42% | 58% | 44% | 89% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **short_story-3**: prefer 8%, task 17%, original 25%. Constraint failures: 0. Judge: "Response A tells a complete story with a clear beginning, middle, and end, while Response B feels more like a vignette or a character sketch."
- **fiction-5**: prefer 17%, task 17%, original 58%. Constraint failures: 1. Judge: "Response B is more evocative and sets a stronger mood, while still fulfilling the prompt's requirements."
- **character-3**: prefer 25%, task 25%, original 33%. Constraint failures: 0. Judge: "Response B presents a more dynamic and engaging character that aligns closely with the brief's requirement for a scene-stealing side character in a romantic comedy."
- **rewrite-3**: prefer 25%, task 25%, original 25%. Constraint failures: 2. Judge: "Response B offers a more vivid and emotionally resonant portrayal of Sarah's feelings, using unique imagery and a distinctive voice."
- **short_story-4**: prefer 33%, task 21%, original 33%. Constraint failures: 0. Judge: "Response A is more original, unpredictable, and distinctive, offering a richer narrative and a more profound lesson than Response B."
- **poetry-3**: prefer 42%, task 21%, original 33%. Constraint failures: 0. Judge: "Response A offers a more traditional and complete love poem, while Response B feels more like a fragment or a setup for a poem, though it has more unique imagery."
- **character-4**: prefer 33%, task 33%, original 33%. Constraint failures: 0. Judge: "Response B presents a more complete and engaging mentor character while adhering closely to the brief's requirements."
- **marketing-3**: prefer 42%, task 25%, original 42%. Constraint failures: 0. Judge: "Response A directly addresses the freelancer's pain points and offers clear solutions, while Response B is more poetic but less informative."
