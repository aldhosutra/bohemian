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

### Phase 8: docs and packaging
- README, methodology, architecture, evaluation, results and examples written. The examples are selected by a fixed rule (first test task in six categories, sample 0), not by quality, and include the worst-scoring task.
- Human review kit built from v3 (40 pairs) and checked with a synthetic rater. **No human ratings collected.**
