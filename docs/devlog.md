# Development log

Decisions and experimental results, in order. Costs are actual OpenRouter charges from `eval/results/ledger.jsonl`.

## 2026-11-23

### Phase 1: research
- Identified Ponytail as `DietrichGebert/ponytail` (the original; many forks and ports exist). Cloned both repositories and read their skill text, scripts, manifests, benchmarks and licenses (both MIT). Notes: [`research.md`](research.md).
- The main takeaways for the evaluation: Ponytail's cheap competitor arm, its judge self-tests, and its per-task statistics. Antialgorithm's showcase compares an unfiltered baseline batch with a *picked* treatment batch, which Bohemian must not repeat.

### Phase 2: architecture
- Format: Agent Skill (`skills/bohemian/SKILL.md` + `references/` + optional stdlib `scripts/`), plus a Claude Code plugin manifest. No hooks. Creative help is request-scoped, and hooks would need per-agent code.
- The method has six steps. The new elements compared with Antialgorithm are per-layer defaults (premise, shape, material, voice), technique *families* with named cheap versions, voice preservation as a hard constraint, intensity defined by *what may move*, and five modes.
- All skill text was written from scratch. Concepts are credited.

### Phase 3: MVP
- `SKILL.md`, `references/{techniques,cliches,modes}.md`, `scripts/{seed,moves,lint,state}.py`. Smoke-tested every script. `claude plugin validate .` passes.

### Phase 4: benchmark and harness
- Budget: the user capped total spend at **USD 3**. Chose cheap models: DeepSeek V4.1 Flash and Claude Haiku 5.5 as generators, Gemini 2.5 Flash Lite and GPT-4o-mini as judges. Wrote a ledger that refuses calls past the cap, plus a request cache.
- 54 tasks in 12 categories, 42 with deterministic constraints, and a 12-task dev split (first task of each category).
- **Finding: adaptive thinking breaks controlled comparison.** In the first smoke test, DeepSeek spent its whole 3,000-token budget on hidden reasoning on 3 of 6 cells and returned nothing. Decision: reasoning off for every arm.
- **Finding: without thinking, nobody plans.** With reasoning off, all arms (Bohemian included) went straight to the final piece. The skill's method never ran. Decision: the user wrapper tells *every* arm to "plan in brief notes" before `<final>`. Planning is equal across arms, and only the skill changes how.
- Wrote an independent cliché lexicon (162 entries). Entries are automatically split into 61 *shared* with the skill text and 101 *held out*. A first version counted substrings ("ember" inside "remember") as shared; fixed with word boundaries.
- **Judge self-test.** Qwen3-235B as judge returned degenerate one-word-per-line text through its OpenRouter provider and was replaced by GPT-4o-mini. Gemini and GPT-4o-mini each pass 23 of 24 checks. Their misses (a tie on an off-brief poem; lenient absolute task alignment for nonsense names in the right format) mean pairwise `task` and the deterministic checks carry the alignment evidence.
- Smoke tests and self-tests cost $0.056.

### Phase 5: v1 run
- 972 generations, all with a well-formed `<final>` block, cost $0.41.
- **Finding: Haiku skips the method.** Haiku wrote no planning notes in 110 of 162 Bohemian outputs (DeepSeek: 18 of 162). Likely cause: `SKILL.md` says "Work through these steps privately. The user sees the finished work, not the steps," which Haiku reads as "do not write the steps". In an environment without hidden thinking, that turns the method off.
- **Finding: provider ignores reasoning=off.** 4 of 972 cells (all DeepSeek, all Bohemian arm) came back empty. The OpenRouter provider Novita ignored `reasoning: {enabled: false}` and spent all 4,000 tokens reasoning. v1 keeps them as scored losses for Bohemian. From v2 on, an arm-agnostic rule resamples outputs that came back empty because hidden reasoning used the budget (up to 3 retries, recorded per cell).
- v1 judging: 2,592 judgments. Test-split headline: vs baseline prefer 64% [58–71], distinctive 72%, task 51% (neutral). **vs one-liner prefer 26% [21–32]: the skill lost to one sentence.** Judge-free metrics disagreed with the judges: Bohemian was further from the obvious answer, more diverse and less convergent than the one-liner.
- Constraint pass: baseline 94%, Bohemian 89%, one-liner 87%. Bohemian's misses are mostly word limits.
- Strong position bias in the cheap judges (treatment wins 76% as A vs 48% as B). Balanced by hash, so it cancels in expectation.

### Phase 6: failure analysis (dev split only)
- Judge reasons when the one-liner won: "more evocative", "more engaging", "fully realized". Bohemian fiction was "less fully realized", "like a vignette".
- Read side by side. One Bohemian/DeepSeek positioning piece followed the method exactly and produced the sharpest line in the set ("Take the long way. You've got the legs for it now."), yet lost to "Ride like the tide". Part of the gap is cheap-judge taste for ornament.
- But real problems too: the "displaced witness" technique (first in the list) appeared in 12 of 44 dev plans; Haiku delivered 3 taglines and a recommendation when asked for one; rewrites overran length because the model never switched into rewrite mode.
- **v2** (see `benchmark-results.md` for the full list). On dev: prefer vs baseline 53% → 65%, vs one-liner 27% → 26%, constraint pass got worse (94% → 86%, all `rewrite-1` overruns). Added mode inference ("v2b"): constraint 92%, vs baseline 67%, vs one-liner 31%.
- **Ablation:** SKILL.md without the reference files did not beat the one-liner either (24%), so the long lists of tells are not why it loses.
- Haiku still planned in only 4 of 36 dev outputs with v2's wording. With thinking off, Haiku treats the skill as a prompt only, whatever the wording.

### Phase 7: v2 on all tasks
- Test split: vs baseline prefer 70% [62–77], vs one-liner 31% [25–38], constraint 88.4%.
- **Stronger-judge audit** (`gpt-5.4-mini`, 60 test pairs per reference): vs baseline prefer 82%, task 70%; vs one-liner prefer 38%. The one-liner gap is partly cheap-judge taste, mostly real.
- Strong judge's reasons on dev one-liner pairs: Bohemian "smart but internally literary", "a premise sketch", "polished but conventional"; the one-liner "more vivid", "a stronger, more unusual premise". One Bohemian output leaked notes into the piece. Diagnosis: the anchor rule plus "never ask what would be interesting" plus plain-words guidance produced grounded, low-hook work.
- **v3:** anchor as a launch point; first interesting idea named and passed; strongest hook; restraint not a house style; fully realized; no leaked notes. Dev: strong judge vs one-liner prefer 39% → 50%, task 56%; cheap judges flat; constraint 100%.

### v3 on all tasks (final)
- Test split, cheap judges: vs baseline prefer **73% [65–80]**, distinctive 80%, unpredictable 82%, task 53% (neutral). vs one-liner prefer **37% [31–43]**.
- Audit (40 pairs per reference): vs baseline prefer 92%; vs one-liner prefer **55%**, task 56%.
- Judge-free metrics: v3 slightly less divergent than v2 (semantic diversity 0.276 vs 0.301, held-out clichés 0.171 vs 0.137), still better than baseline everywhere and than the one-liner on typicality and cross-model similarity.
- **Length bias found:** Bohemian more than 10% longer than baseline → 81% prefer; length-matched → 70%; shorter → 54%. v3 is 20% longer than baseline. Length-matched vs one-liner: 33%.
- Fiction remains the weakest category (42% prefer vs baseline).
- Stopped iterating at USD 2.39 of the 3.00 cap. Another round on the one-liner gap would need human ratings to tell judge taste from quality, and would risk tuning to the judges.

### Comparison with Antialgorithm (after v3)
- The user asked whether Bohemian beats Antialgorithm and said to adopt it if it does. Added Antialgorithm's unmodified `SKILL.md` (commit `a6392c0`) as a fourth arm on the 42 test tasks. Decision rule fixed before judging: switch if the cheap judges prefer it head-to-head with the CI above 50%, the stronger judge agrees, and task fit and constraint pass are not worse.
- Head-to-head: cheap judges prefer Bohemian 59% [52–65], partly length (Bohemian is 20% longer; length-matched 61%). Stronger judge: 52%, even.
- Against the references, judges rate Antialgorithm lower than Bohemian (vs baseline 61% prefer with task 43%; vs one-liner 27%; stronger judge vs one-liner 38%).
- Judge-free, Antialgorithm wins every originality measure: clichés 0.026 vs 0.205 per 100 words, typicality 0.549 vs 0.605, diversity 0.323 vs 0.276. It avoids stock character names that Bohemian still uses.
- Outcome: rule not met, Bohemian stays. Recorded as a trade-off, not a win. A natural next step is to borrow what makes Antialgorithm diverge (its handling of names, seeds and regions) and test it, which needs budget beyond the remaining USD 0.16.
- Cost USD 0.45. Total USD 2.84.

### v4 "lean" experiment (uncommitted)
- Goal from the user: make Bohemian cheaper than Antialgorithm and more creative. v4 is one 1,072-word `SKILL.md` (v3: ~4,400 words with references; Antialgorithm: 1,882). It keeps the steps that won judges (fixed parts, strongest hook, payoff and brief checks, mode inference), folds techniques into a five-family table, replaces the cliché catalog with a short list of moves, adds three rules learned from Antialgorithm's results (names from the world's own naming, numbers only when needed, endings that stop) and a strict length rule, and plans in five lines.
- Success criteria, fixed before running: on the test split, (1) input tokens below Antialgorithm's; (2) the stronger judge prefers v4 over Antialgorithm head-to-head; (3) the judge-free gap to Antialgorithm narrows on clichés and typicality; (4) task fit vs baseline at least 50%; (5) constraint pass at least Antialgorithm's (0.884). Tuning on dev only. Budget raised to USD 4.00 by the user.
- Paused mid-run at the user's request (another session needed the OpenRouter credit), with `STATUS.md` as the resume tracker. Resumed later.
- Dev, v4: input tokens 1,599 / 2,288 per call (Antialgorithm 2,421 / 3,232). Prefer vs baseline 63%, vs Antialgorithm 61%. Constraint pass dropped to 89%: three rewrites ran to 120–150 words against a 55-word original, because the plan recorded "short paragraph" instead of a number.
- v4b: the plan's first line now asks for the target length as a number of words, lines or items. Dev constraint pass 97%, typicality 0.553 (v4 0.570). Stopped revising after this one round.
- Test, v4b: prefer vs baseline 68% [60–76], vs one-liner 33% [28–38], vs Antialgorithm 56.6% [51.9–61.5]; task fit vs baseline 45.1% [40.1–49.9]. Stronger judge (n=40 each): vs Antialgorithm 48%, vs baseline 85% (task 65%), vs one-liner 48%. Judge-free: length equal to baseline, constraint pass 0.949 (best of all arms), held-out clichés −89% vs baseline, typicality 0.582 (Antialgorithm 0.549, v3 0.605), diversity 0.319 (Antialgorithm 0.323).
- Criteria: tokens pass, judge-free gap pass, constraint pass pass; stronger-judge head-to-head fail (even); task fit mixed (cheap judges 45%, stronger judge 65%).
- Spend so far USD 3.55.

### v5 "tail pick" (not shipped)
- Approved by the user, with the cap raised to USD 5.00. Changes from v4b (1,162 words, snapshot `eval/results/v5/skill_snapshot_v5/`): a seed step (`seed.py`, or a self-written random string when scripts can't run, after String Seed of Thought); five candidates with an estimated chance that a typical model would write each, striking any above 10% (after Verbalized Sampling); the first three names that come to mind are written down and not used; no named stock nouns in the skill text.
- 20 new tasks added (`split: fresh`, `fresh-1` to `fresh-20`) before any v5 output existed. Never used for tuning.
- Bar for "clearly better than Antialgorithm", fixed before v5 judging: on the test split, (1) `gpt-5.4-mini` prefers v5 ≥ 60% with the 95% CI above 50%, on ≥ 120 pairs; (2) `mistral-large-2512` (after passing the judge self-test) agrees, ≥ 55%; (3) typicality, semantic diversity and all-cliché rate at least as good as Antialgorithm's; (4) task fit vs Antialgorithm ≥ 50% (cheap judges); (5) input tokens below Antialgorithm's. Then (6): the same direction on the fresh split for (1), (3) and (4).
- User approved USD 1.30 more (cap 4.85). Judge self-test: `gpt-5.4-mini` 22/24 (misses only lenient task fit on nonsense), `mistral-large-2512` 20/24 and **rejected** (preferred nonsense names over distinctive ones in one order), `gemini-3.5-flash-lite` unusable (reasoning cannot be turned off), `gemini-3.1-flash-lite` 22/24, used as the second strong judge instead.
- Dev, v5: typicality 0.520 (Antialgorithm 0.514), diversity 0.360 (0.365), prefer vs Antialgorithm 62%, task 56%. DeepSeek ran the plan in 32/36 outputs (probability estimates in 27); Haiku in 18/36 (9). No revision.
- Test, v5 (cheap judges): vs Antialgorithm prefer 58.5% [53.4–63.5], original 55.9% [51.0–60.5], task 54.0%; vs baseline prefer 66.8%, task 46.7%; vs one-liner prefer 34.5%. Judge-free vs Antialgorithm: diversity 0.335 vs 0.323 and cross-model similarity 0.619 vs 0.618 (ties), typicality 0.571 vs 0.549 (Antialgorithm better), all-cliché 0.190 vs 0.026 (Antialgorithm better), constraint pass 0.926 vs 0.884 (v5 better). Input tokens 1,719 / 2,437 (Antialgorithm 2,422 / 3,236).
- Strong-judge audit vs Antialgorithm, 120 pairs each: `gpt-5.4-mini` prefer **46%**, `gemini-3.1-flash-lite` **40%**. Both lowest on character (22%), fiction (27–36%) and positioning (25–38%); judges' reasons: v5 "more playful and distinctive but awkward or off-brief".
- **Bar not met** (criteria 1, 2 and 3 fail; 4 and 5 pass). Fresh-split run not done: it was to confirm a win, and there is none. Spend USD 4.18.

### Visual tests and v6 "great first, then stands out" (not shipped)
- Text side-by-sides of YouTube Short scripts were hard to judge by eye, so the user suggested posters. Each arm wrote SVG posters (600×900, self-contained) for 2 briefs, then 6 new ones. Antialgorithm got its `visuals.md` (1,450 words), as its users would. Generators, settings and wrapper as in the benchmark. The artifacts and scripts are in the session scratchpad, not the repo.
- Round 1 (library late nights, jazz concert; 32 posters): the user's blind picks were Bohemian 3 (v4b twice, v5 once), Antialgorithm 1, baseline 0. Their picks were bold, high-impact pieces. My picks (clever, concept-heavy ones) and the user's agreed on none of the 4 walls.
- The user's direction: being original is pointless if the result isn't great. They want work that is great and different, so it stands out.
- Vision judges were calibrated on the user's 4 picks (8 posters per wall, top-3 ranking, 3 shuffles each). `gemini-3.1-flash-lite` put the user's pick first 4/12 times (chance 1.5) and in its top 3 6/12 times. `gpt-5.4-mini` put it first 2/12 times. Both lean toward the plain baseline.
- v6 (1,360 words, snapshot `eval/results/v6/skill_snapshot_v6/`), built from v4b, not v5:
  - "Great first, then different" replaces "original and good".
  - The plan names "the wall": where the piece is met and what the others there look like.
  - Each direction is scored on Great (would the best in the field ship it; does it land at once) and Stands out (would someone stop on it, next to the others). A direction that fails Great is never picked.
  - "Make it great" adds impact first and full commitment.
  - A new section on visual work: one hero element, readable at a distance, a look chosen on purpose, text that fits with a margin.
  - Facts: invent nothing, in words or pictures, and on posters include every fact the brief gives.
- Round 2 (6 new briefs, 96 posters: baseline, Antialgorithm, v4b, v6):
  - Gemini vision judge, first place across 36 rankings: baseline 26, v6 4, v4b 3, Antialgorithm 3. Given its calibration, this is weak evidence.
  - Text running off the canvas (render-based check): v6 2/24, Antialgorithm 2/23, baseline 3/24, v4b 3/24.
  - One Antialgorithm poster was invalid SVG.
  - My read: every skill arm drifts to a dark, monospace, technical-diagram look; v6 is the boldest of them.
  - The user's blind picks (12 walls, `eval/results/v6/user_picks_round2.json`): **v4b 7, Antialgorithm 3, baseline 2, v6 0.**
  - Across both rounds the user picked v4b 9/16, Antialgorithm 4, baseline 2, v5 1, v6 0/12.
  - The user's picks are crafted, warm and illustrated: one drawn image tied to the subject (a river as a map, a sheet-music choir poster, a taped flyer, a race bib), clear hierarchy, often a light paper ground. v6's "full scale, full contrast, commit" made posters loud and blocky, with heavy type and two clipped titles. My reading of round 1 as a taste for "bold impact" was wrong.
  - Gemini agreed with the user's first choice in 5 of 36 rankings (chance 4.5). It is not a usable proxy for the user's taste.
  - Outcome: v6 not shipped. The best poster arm by the user's eye is the shipped v4b, which has no visual guidance at all.
- Playable Shorts (v4b vs Antialgorithm with `visuals.md`): each arm built 30-second 9:16 HTML Shorts with captions, for 2 topics (why onions make you cry; a "90-second rule" for falling back asleep) × 2 models × 2 samples, with a brief that asks for virality. Cost USD 0.05. The user's blind picks (`eval/results/v6/user_picks_shorts.json`): **v4b 3, Antialgorithm 1.** Their picks open with a plain hook that carries a twist ("it isn't the smell", "Don't count sheep. Count to ninety.", "Awake at 3 a.m.?"), and they passed over the most experimental pieces.
- Decision: v4b restored as the shipped skill; v5 and v6 kept as snapshots.
- Across the three blind tests the user chose v4b 12 times, Antialgorithm 5, baseline 2, v5 1 and v6 0 (20 sets; one rater, two models, small briefs).
- Text, dev split (12 tasks):
  - Cheap judges: v6 vs Antialgorithm prefer 58.3%, task 55.9%; vs baseline prefer 60.4%, task 46.9%. v5 on dev: 61.8% and 67.4%.
  - Typicality 0.556 (v4b 0.553, v5 0.520, Antialgorithm 0.514). Constraint pass 0.972.
  - Strong judges vs Antialgorithm (72 dev pairs): `gpt-5.4-mini` 44%, `gemini-3.1-flash-lite` 43%; for comparison, v5 on the same dev pairs with Gemini scored 56%. No text gain over v4b or v5.
- Note: `metrics.py --run v5` was rerun with the v6 text in place, so the shared and held-out cliché columns in `eval/results/v5/metrics.json` now split by v6's text. The all-cliché rate is unaffected.
- Cost of this phase USD 0.56 including the Shorts. Total USD 4.74 of the 4.85 cap.

### Phase 8: docs and packaging
- README, methodology, architecture, evaluation, results and examples written. The examples are selected by a fixed rule (first test task in six categories, sample 0), not by quality, and include the worst-scoring task.
- Human review kit built from v3 (40 pairs) and checked with a synthetic rater. **No human ratings collected.**
