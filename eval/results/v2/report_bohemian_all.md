# Benchmark report: run `v2`, split `all`, treatment `bohemian`

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
| original | 61.0% [54.6, 67.5] | 395 / 1 / 252 | 29 / 17 | 0.1 |
| unpredictable | 78.3% [72.8, 83.4] | 507 / 1 / 140 | 44 / 3 | 2.5e-10 |
| distinctive | 74.9% [69.4, 80.5] | 485 / 1 / 162 | 46 / 6 | 1e-08 |
| prefer | 66.9% [60.6, 73.1] | 433 / 1 / 214 | 37 / 11 | 0.00022 |
| task | 50.4% [45.8, 54.9] | 252 / 149 / 247 | 26 / 23 | 0.78 |

- google/gemini-2.5-flash-lite: original 67%, unpredictable 90%, distinctive 89%, prefer 81%, task 63%

- openai/gpt-4o-mini: original 55%, unpredictable 67%, distinctive 61%, prefer 52%, task 38%
- Position check (prefer): treatment win rate 77% when shown as A (n=326), 56% when shown as B (n=322).

### bohemian vs oneliner

| question | win rate [95% CI] | W / T / L (all judgments) | tasks above / below 50% | sign-test p |
|---|---|---|---|---|
| original | 42.0% [37.3, 46.5] | 271 / 2 / 375 | 16 / 28 | 0.096 |
| unpredictable | 28.6% [24.4, 32.9] | 185 / 1 / 462 | 2 / 45 | 1.6e-11 |
| distinctive | 27.4% [22.8, 32.3] | 177 / 1 / 470 | 5 / 43 | 1.4e-08 |
| prefer | 30.9% [25.8, 36.2] | 200 / 1 / 447 | 6 / 41 | 1.8e-07 |
| task | 40.3% [36.0, 44.4] | 188 / 146 / 314 | 10 / 35 | 0.00025 |

- google/gemini-2.5-flash-lite: original 43%, unpredictable 32%, distinctive 33%, prefer 35%, task 39%

- openai/gpt-4o-mini: original 41%, unpredictable 25%, distinctive 22%, prefer 27%, task 42%
- Position check (prefer): treatment win rate 48% when shown as A (n=314), 15% when shown as B (n=334).

### Judge agreement

| question | % same verdict | Cohen's kappa |
|---|---|---|
| original | 85% | 0.69 |
| unpredictable | 70% | 0.41 |
| distinctive | 71% | 0.43 |
| prefer | 69% | 0.40 |
| task | 41% | 0.18 |

## 2. Blinded absolute scores (1-5)

Judge: google/gemini-2.5-flash-lite, every output scored alone. Δ = treatment minus reference, per-task paired.

| dimension | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| originality | 3.23 | 4.19 | 4.01 | +0.77 [+0.65, +0.89] (52↑/0↓) | -0.19 [-0.27, -0.10] (10↑/33↓) |
| specificity | 3.93 | 4.56 | 4.47 | +0.54 [+0.40, +0.69] (45↑/3↓) | -0.10 [-0.18, -0.02] (13↑/21↓) |
| distinctiveness | 3.31 | 4.23 | 4.09 | +0.77 [+0.65, +0.90] (50↑/1↓) | -0.14 [-0.20, -0.07] (9↑/28↓) |
| coherence | 5.00 | 5.00 | 5.00 | +0.00 [+0.00, +0.00] (0↑/0↓) | +0.00 [+0.00, +0.00] (0↑/0↓) |
| task_alignment | 5.00 | 5.00 | 4.99 | -0.01 [-0.02, +0.00] (0↑/2↓) | -0.01 [-0.02, +0.00] (0↑/2↓) |
| creative_risk | 2.37 | 3.41 | 3.21 | +0.84 [+0.68, +1.00] (49↑/3↓) | -0.20 [-0.30, -0.10] (10↑/32↓) |

Second judge (openai/gpt-4o-mini) on 324 outputs: Spearman ρ with the primary judge: originality 0.60, specificity 0.66, distinctiveness 0.65, coherence n/a, task_alignment n/a, creative_risk 0.73

Second judge's own means on that subset: baseline: origi 4.19, coher 5.00, task_ 5.00; oneliner: origi 4.73, coher 5.00, task_ 5.00; bohemian: origi 4.51, coher 5.00, task_ 5.00

## 3. Judge-free metrics

Lower is better for cliché rates, typicality, n-gram overlap, cross-model similarity and intra-list similarity; higher is better for semantic diversity and constraint pass rate.

| metric | baseline | oneliner | bohemian | Δ vs baseline [95% CI] | Δ vs oneliner [95% CI] |
|---|---|---|---|---|---|
| words | 185.0 | 212.3 | 205.7 | +20.704 [+10.722, +31.642] +11% | -6.537 [-18.694, +3.948] -3% |
| constraint pass rate | 0.948 | 0.881 | 0.889 | -0.060 [-0.107, -0.016] -6% | +0.008 [-0.036, +0.052] +1% |
| clichés /100 words (all) | 1.213 | 0.234 | 0.135 | -1.078 [-2.685, -0.205] -89% | -0.099 [-0.207, -0.023] -42% |
| clichés /100 words (shared with skill) | 0.097 | 0.050 | 0.028 | -0.069 [-0.126, -0.021] -71% | -0.022 [-0.050, +0.005] -44% |
| clichés /100 words (held-out) | 1.116 | 0.183 | 0.107 | -1.009 [-2.612, -0.147] -90% | -0.077 [-0.185, -0.009] -42% |
| typicality (cos to obvious answer) | 0.731 | 0.616 | 0.590 | -0.141 [-0.160, -0.123] -19% | -0.026 [-0.039, -0.013] -4% |
| intra-list similarity (list tasks) | 0.429 | 0.349 | 0.349 | -0.080 [-0.144, -0.024] -19% | +0.000 [-0.016, +0.019] +0% |
| semantic diversity across samples | 0.190 | 0.271 | 0.302 | +0.112 [+0.093, +0.131] +59% | +0.031 [+0.016, +0.045] +11% |
| 3-gram overlap across samples | 0.052 | 0.015 | 0.014 | -0.039 [-0.060, -0.022] -74% | -0.001 [-0.004, +0.002] -7% |
| cross-model similarity | 0.745 | 0.680 | 0.638 | -0.107 [-0.132, -0.084] -14% | -0.042 [-0.058, -0.025] -6% |

## 4. Per generator model (pairwise vs baseline, both judges)

| model | original | unpredictable | distinctive | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 62% | 74% | 70% | 64% | 51% | 90% / 91% |
| deepseek/deepseek-v4.1-flash | 60% | 83% | 80% | 69% | 50% | 87% / 98% |

## 5. Per category (pairwise vs baseline, both judges, both models)

| category | n tasks | original | prefer | task | constraint pass (treat / baseline) |
|---|---|---|---|---|---|
| analogy | 4 | 49% | 72% | 51% | 94% / 100% |
| brainstorm | 5 | 93% | 93% | 67% | 100% / 100% |
| character | 4 | 50% | 54% | 42% | 92% / 100% |
| fiction | 5 | 28% | 28% | 24% | 89% / 78% |
| headlines | 4 | 85% | 88% | 61% | 100% / 100% |
| marketing | 5 | 72% | 80% | 45% | 79% / 79% |
| naming | 5 | 70% | 70% | 46% | 100% / 100% |
| poetry | 5 | 70% | 60% | 57% | 75% / 100% |
| positioning | 4 | 67% | 79% | 60% | 83% / 100% |
| rewrite | 4 | 50% | 65% | 62% | 79% / 88% |
| short_story | 5 | 52% | 53% | 46% | 67% / 92% |
| story_concept | 4 | 42% | 65% | 48% | 88% / 100% |

## 6. Failure cases (lowest task-level `prefer` and `task` win rates vs baseline)

- **fiction-5**: prefer 8%, task 8%, original 17%. Constraint failures: 0. Judge: "Response A feels more complete as an opening paragraph, establishing setting, character, and a sense of melancholy, while Response B is more focused on a specific interaction that feels less like an opening."
- **fiction-2**: prefer 17%, task 17%, original 42%. Constraint failures: 1. Judge: "Response B feels more emotionally resonant and captures the subtle grief and shared history of the siblings more effectively, while still fulfilling the prompt's requirements."
- **fiction-1**: prefer 25%, task 25%, original 17%. Constraint failures: 0. Judge: "Response A presents a more emotionally resonant and character-driven narrative that aligns closely with the brief about a lonely astronaut."
- **character-1**: prefer 33%, task 17%, original 42%. Constraint failures: 0. Judge: "Response B offers a more unusual and compelling protagonist with a unique sensory ability and a built-in character flaw that directly impacts her investigative process, making for a more intriguing mystery."
- **poetry-1**: prefer 33%, task 33%, original 50%. Constraint failures: 0. Judge: "Response A uses more evocative imagery and a more traditional poetic structure, making it a stronger choice for a general poem about the ocean, while Response B is more experimental and less universally appealing."
- **rewrite-3**: prefer 25%, task 42%, original 50%. Constraint failures: 2. Judge: "Response A is more vivid and less predictable, using stronger imagery and more evocative language while still adhering to the original events and emotional tone."
- **analogy-1**: prefer 42%, task 33%, original 33%. Constraint failures: 0. Judge: "Response A is more comprehensive and better explains the core concepts of the internet using the postal analogy, while Response B is more poetic but less informative."
- **fiction-3**: prefer 42%, task 38%, original 33%. Constraint failures: 0. Judge: "Response A offers a unique perspective on lost items in an airport, while Response B captures a poignant human interaction that aligns closely with the brief's emotional tone."
