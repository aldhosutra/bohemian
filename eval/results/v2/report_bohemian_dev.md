# Benchmark report: run `v2`, split `dev`, treatment `bohemian`

- Tasks: 12  
- Generator models: anthropic/claude-haiku-5.5, deepseek/deepseek-v4.1-flash  
- Arms: baseline, oneliner, bohemian  
- Generations analysed: 216  
- Pairwise judges: google/gemini-2.5-flash-lite, openai/gpt-4o-mini

- Outputs with a well-formed `<final>` block: 215/216

## 1. Blinded pairwise preference (treatment vs reference)

Win rate = (wins + ties/2) / comparisons, averaged per task, then over tasks. 50% = no difference. Interval: 95% bootstrap over tasks. Sign test: tasks where the treatment's mean win score was above vs below 50%.


### bohemian vs baseline

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 51.4% [41.0, 61.8] | 74 / 0 / 70 | 5 / 5 | 1 |
| unpredictable | 74.3% [63.2, 84.7] | 107 / 0 / 37 | 9 / 1 | 0.021 |
| distinctive | 72.9% [60.4, 84.0] | 105 / 0 / 39 | 10 / 2 | 0.039 |
| prefer | 57.6% [46.5, 68.8] | 83 / 0 / 61 | 7 / 4 | 0.55 |
| task | 42.0% [33.0, 51.4] | 46 / 29 / 69 | 5 / 7 | 0.77 |

- google/gemini-2.5-flash-lite: original 58%, unpredictable 82%, distinctive 82%, prefer 71%, task 53%

- openai/gpt-4o-mini: original 44%, unpredictable 67%, distinctive 64%, prefer 44%, task 31%
- Position check (prefer): treatment win rate 79% when shown as A (n=58), 43% when shown as B (n=86).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 50.7% [42.4, 59.0] | 73 / 0 / 71 | 5 / 4 | 1 |
| unpredictable | 28.5% [20.8, 38.2] | 41 / 0 / 103 | 1 / 10 | 0.012 |
| distinctive | 25.7% [18.7, 34.0] | 37 / 0 / 107 | 0 / 10 | 0.002 |
| prefer | 30.6% [22.9, 38.9] | 44 / 0 / 100 | 1 / 10 | 0.012 |
| task | 42.4% [35.4, 49.3] | 45 / 32 / 67 | 2 / 7 | 0.18 |

- google/gemini-2.5-flash-lite: original 54%, unpredictable 35%, distinctive 36%, prefer 38%, task 42%

- openai/gpt-4o-mini: original 47%, unpredictable 22%, distinctive 15%, prefer 24%, task 43%
- Position check (prefer): treatment win rate 45% when shown as A (n=78), 14% when shown as B (n=66).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 84% | 0.68 |
| unpredictable | 69% | 0.40 |
| distinctive | 71% | 0.44 |
| prefer | 66% | 0.34 |
| task | 46% | 0.21 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.35 | 4.44 | 4.12 | +0.78 [+0.51, +1.06] (12↑/0↓) | -0.32 [-0.44, -0.19] (0↑/10↓) |
| specificity | 4.04 | 4.57 | 4.43 | +0.39 [+0.08, +0.72] (10↑/2↓) | -0.14 [-0.33, +0.01] (2↑/5↓) |
| distinctiveness | 3.44 | 4.39 | 4.18 | +0.74 [+0.46, +1.03] (11↑/0↓) | -0.21 [-0.35, -0.08] (1↑/8↓) |
| coherence | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| creative_risk | 2.47 | 3.62 | 3.29 | +0.82 [+0.53, +1.14] (12↑/0↓) | -0.33 [-0.49, -0.18] (0↑/9↓) |

Second judge (openai/gpt-4o-mini) on 72 outputs: Spearman ρ with the primary judge: originality 0.63, specificity 0.62, distinctiveness 0.75, coherence n/a, task_alignment n/a, creative_risk 0.74

Second judge's own means on that subset: baseline: origi 4.29, coher 5.00, task_ 5.00; oneliner: origi 4.88, coher 5.00, task_ 5.00; bohemian: origi 4.54, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 240.5 | 275.7 | 258.6 | +18.097 [-7.139, +45.945] +8% | -17.139 [-51.417, +14.417] -6% |
| constraint pass rate | 1.000 | 0.944 | 0.917 | -0.083 [-0.194, +0.000] -8% | -0.028 [-0.083, +0.000] -3% |
| clichés /100 words (all) | 3.929 | 0.074 | 0.046 | -3.883 [-10.865, -0.170] -99% | -0.028 [-0.090, +0.032] -38% |
| clichés /100 words (shared with skill) | 0.105 | 0.038 | 0.046 | -0.060 [-0.122, -0.004] -56% | +0.008 [-0.037, +0.058] +22% |
| clichés /100 words (held-out) | 3.823 | 0.036 | 0.000 | -3.823 [-10.829, -0.137] -100% | -0.036 [-0.084, +0.000] -100% |
| typicality (cos to obvious answer) | 0.711 | 0.581 | 0.572 | -0.139 [-0.194, -0.095] -20% | -0.009 [-0.033, +0.015] -2% |
| intra-list similarity (list tasks) | 0.432 | 0.326 | 0.297 | -0.135 [-0.326, -0.025] -31% | -0.029 [-0.056, -0.009] -9% |
| semantic diversity across samples | 0.203 | 0.285 | 0.304 | +0.102 [+0.066, +0.134] +50% | +0.019 [-0.011, +0.051] +7% |
| 3-gram overlap across samples | 0.040 | 0.013 | 0.010 | -0.030 [-0.056, -0.010] -74% | -0.002 [-0.007, +0.002] -19% |
| cross-model similarity | 0.729 | 0.679 | 0.625 | -0.105 [-0.136, -0.073] -14% | -0.055 [-0.087, -0.016] -8% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 51% | 68% | 65% | 54% | 40% | 94% / 100% |
| deepseek/deepseek-v4.1-flash | 51% | 81% | 81% | 61% | 44% | 89% / 100% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 1 | 33% | 42% | 33% | n/a / n/a |
| brainstorm | 1 | 75% | 75% | 58% | 100% / 100% |
| character | 1 | 42% | 33% | 17% | n/a / n/a |
| fiction | 1 | 17% | 25% | 25% | n/a / n/a |
| headlines | 1 | 83% | 83% | 62% | 100% / 100% |
| marketing | 1 | 42% | 67% | 38% | n/a / n/a |
| naming | 1 | 50% | 67% | 21% | 100% / 100% |
| poetry | 1 | 50% | 33% | 33% | n/a / n/a |
| positioning | 1 | 75% | 83% | 62% | 100% / 100% |
| rewrite | 1 | 58% | 67% | 58% | 67% / 100% |
| short_story | 1 | 33% | 50% | 38% | n/a / n/a |
| story_concept | 1 | 58% | 67% | 58% | 83% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-1**: prefer 25%, task 25%, original 17%. Constraint failures: 0. Judge: "Response A presents a more emotionally resonant and character-driven narrative that aligns closely with the brief about a lonely astronaut."
- **character-1**: prefer 33%, task 17%, original 42%. Constraint failures: 0. Judge: "Response B offers a more unusual and compelling protagonist with a unique sensory ability and a built-in character flaw that directly impacts her investigative process, making for a more intriguing mystery."
- **poetry-1**: prefer 33%, task 33%, original 50%. Constraint failures: 0. Judge: "Response A uses more evocative imagery and a more traditional poetic structure, making it a stronger choice for a general poem about the ocean, while Response B is more experimental and less universally appealing."
- **analogy-1**: prefer 42%, task 33%, original 33%. Constraint failures: 0. Judge: "Response A is more comprehensive and better explains the core concepts of the internet using the postal analogy, while Response B is more poetic but less informative."
- **short_story-1**: prefer 50%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A provides a clearer narrative structure and aligns more closely with the brief, while Response B, though distinctive, is less straightforward and may confuse readers."
- **naming-1**: prefer 67%, task 21%, original 50%. Constraint failures: 0. Judge: "Response B offers more creative and relevant names that align well with the brief for a Mac cleaning application."
- **marketing-1**: prefer 67%, task 38%, original 42%. Constraint failures: 0. Judge: "Response A feels more polished and effectively highlights the enduring, simple utility of the wooden spoon, while Response B's focus on the ephemeral nature of the rubber band is more novel but less compelling as an advertisement."
- **story_concept-1**: prefer 67%, task 58%, original 58%. Constraint failures: 1. Judge: "Response A presents a more cohesive and imaginative concept that aligns closely with the brief's request for a fantasy novel pitch."
