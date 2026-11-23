# Benchmark report: run `dev_v2`, split `dev`, treatment `core`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian, bohemian_v2b, core  
- Generations analysed: 360  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 359/360

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### core vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 55.6% [48.6, 63.9] | 80 / 0 / 64 | 5 / 3 | 0.73 |
| unpredictable | 72.9% [63.2, 81.9] | 105 / 0 / 39 | 11 / 1 | 0.0063 |
| distinctive | 69.4% [59.7, 79.2] | 100 / 0 / 44 | 9 / 1 | 0.021 |
| prefer | 60.4% [51.4, 70.1] | 87 / 0 / 57 | 7 / 4 | 0.55 |
| task | 43.4% [37.8, 49.0] | 44 / 37 / 63 | 2 / 7 | 0.18 |

- google/gemini-2.5-flash-lite: original 61%, unpredictable 79%, distinctive 79%, prefer 78%, task 58%

- openai/gpt-4o-mini: original 50%, unpredictable 67%, distinctive 60%, prefer 43%, task 28%
- Position check (prefer): treatment win rate 66% when shown as A (n=68), 55% when shown as B (n=76).

### core vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 36.8% [27.1, 47.2] | 53 / 0 / 91 | 1 / 7 | 0.07 |
| unpredictable | 23.6% [16.0, 30.6] | 34 / 0 / 110 | 0 / 12 | 0.00049 |
| distinctive | 18.8% [9.7, 27.8] | 27 / 0 / 117 | 0 / 12 | 0.00049 |
| prefer | 24.3% [14.6, 34.0] | 35 / 0 / 109 | 0 / 11 | 0.00098 |
| task | 37.2% [26.7, 46.9] | 37 / 33 / 74 | 3 / 7 | 0.34 |

- google/gemini-2.5-flash-lite: original 35%, unpredictable 21%, distinctive 21%, prefer 25%, task 38%

- openai/gpt-4o-mini: original 39%, unpredictable 26%, distinctive 17%, prefer 24%, task 37%
- Position check (prefer): treatment win rate 40% when shown as A (n=68), 11% when shown as B (n=76).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 80% | 0.60 |
| unpredictable | 76% | 0.51 |
| distinctive | 78% | 0.57 |
| prefer | 68% | 0.37 |
| task | 37% | 0.13 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | bohemian_v2b | core | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.11 | 4.12 | 4.08 | +0.74 [+0.43, +1.07] (11↑/0↓) | -0.36 [-0.49, -0.22] (1↑/10↓) |
| specificity | 4.04 | 4.57 | 4.51 | 4.43 | 4.46 | +0.42 [+0.17, +0.75] (9↑/1↓) | -0.11 [-0.22, +0.01] (1↑/6↓) |
| distinctiveness | 3.44 | 4.39 | 4.08 | 4.18 | 4.12 | +0.68 [+0.40, +0.99] (11↑/0↓) | -0.26 [-0.40, -0.12] (1↑/9↓) |
| coherence | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.25 | 3.29 | 3.24 | +0.76 [+0.43, +1.12] (10↑/1↓) | -0.39 [-0.60, -0.17] (2↑/8↓) |

Second judge (openai/gpt-4o-mini) on 120 outputs: Spearman ρ with the primary judge: originality 0.59, specificity 0.63, distinctiveness 0.72, coherence n/a, task_alignment n/a, creative_risk 0.71

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; bohemian: origi 4.54, coher 5.00, task_ 5.00; bohemian_v2b: origi 4.54, coher 5.00, task_ 5.00; core: origi 4.58, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | bohemian_v2b | core | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 269.1 | 258.6 | 249.6 | +9.125 [-1.069, +19.986] +4% | -26.111 [-45.973, -8.152] -9% |
| constraint pass rate | 1.000 | 0.944 | 0.861 | 0.917 | 0.972 | -0.028 [-0.083, +0.000] -3% | +0.028 [+0.000, +0.083] +3% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.089 | 0.046 | 0.181 | -3.747 [-10.754, +0.002] -95% | +0.107 [+0.005, +0.236] +144% |
| clichés /100 words (shared with skill) | 0.105 | 0.038 | 0.038 | 0.046 | 0.112 | +0.006 [-0.108, +0.116] +6% | +0.074 [+0.008, +0.146] +196% |
| clichés /100 words (held-out) | 3.823 | 0.036 | 0.051 | 0.000 | 0.069 | -3.754 [-10.766, -0.064] -98% | +0.033 [-0.010, +0.104] +91% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.573 | 0.572 | 0.565 | -0.146 [-0.205, -0.096] -21% | -0.016 [-0.039, +0.010] -3% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.309 | 0.297 | 0.287 | -0.145 [-0.348, -0.028] -34% | -0.039 [-0.078, -0.013] -12% |
| semantic diversity across samples | 0.203 | 0.286 | 0.303 | 0.304 | 0.307 | +0.104 [+0.065, +0.145] +52% | +0.021 [-0.012, +0.055] +8% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.010 | 0.010 | 0.013 | -0.027 [-0.048, -0.011] -68% | +0.000 [-0.005, +0.006] +2% |
| cross-model similarity | 0.729 | 0.679 | 0.641 | 0.625 | 0.649 | -0.080 [-0.119, -0.039] -11% | -0.030 [-0.066, +0.007] -4% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 53% | 65% | 64% | 51% | 39% | 94% / 100% |
| deepseek/deepseek-v4.1-flash | 58% | 81% | 75% | 69% | 48% | 100% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 42% | 75% | 42% | n/a / n/a |
| brainstorm | 1 | 42% | 50% | 38% | 100% / 100% |
| character | 1 | 50% | 58% | 50% | n/a / n/a |
| fiction | 1 | 58% | 42% | 25% | n/a / n/a |
| headlines | 1 | 92% | 92% | 50% | 100% / 100% |
| marketing | 1 | 67% | 83% | 58% | n/a / n/a |
| naming | 1 | 67% | 67% | 33% | 100% / 100% |
| poetry | 1 | 50% | 42% | 33% | n/a / n/a |
| positioning | 1 | 42% | 42% | 38% | 100% / 100% |
| rewrite | 1 | 58% | 42% | 46% | 83% / 100% |
| short_story | 1 | 50% | 67% | 50% | n/a / n/a |
| story_concept | 1 | 50% | 67% | 58% | 100% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 42%, task 25%, original 58%. Constraint failures: 0. Judge: "Response B presents a more engaging and unique narrative that aligns closely with the brief while showcasing a distinct voice."
- **poetry-1**: prefer 42%, task 33%, original 50%. Constraint failures: 0. Judge: "Response A uses more evocative imagery and a stronger narrative voice, while Response B feels a bit too fragmented and less focused on the ocean itself."
- **positioning-1**: prefer 42%, task 38%, original 42%. Constraint failures: 0. Judge: "Response B provides a clearer brand identity and aligns more closely with the brief's focus on urban commuting."
- **brainstorm-1**: prefer 50%, task 38%, original 42%. Constraint failures: 0. Judge: "Response A provides clearer and more straightforward ideas that align closely with the brief's requirements, while Response B, though creative, is less predictable and distinctive but does not fulfill the brief as effectively."
- **rewrite-1**: prefer 42%, task 46%, original 58%. Constraint failures: 1. Judge: "Response B uses more vivid and consistent metaphors, creating a more distinctive and engaging rewrite while still adhering to the original message."
- **naming-1**: prefer 67%, task 33%, original 67%. Constraint failures: 0. Judge: "Response B offers more relevant and creative names that align closely with the brief's focus on a Mac cleaning application."
- **character-1**: prefer 58%, task 50%, original 50%. Constraint failures: 0. Judge: "Response A offers a more developed and unusual protagonist with a clearer hook and story potential, while Response B is more abstract and less compelling."
- **short_story-1**: prefer 67%, task 50%, original 50%. Constraint failures: 0. Judge: "Response A feels more grounded and relatable, offering a satisfying arc of overcoming initial anxieties, while Response B leans into quirky, slightly surreal elements that are less universally appealing for a first-day-at-a-new-job story."
