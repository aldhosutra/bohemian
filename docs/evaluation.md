# Evaluation methodology

The question: does the same model, given the same task and settings, produce measurably more original and less algorithmic work with Bohemian than without it, **without losing coherence or task alignment**? And is it better than a one-line "be original" instruction, the cheapest alternative anyone could use?

Results are in [`benchmark-results.md`](benchmark-results.md). This page describes the design.

## Arms

All arms use the same generator model, temperature (1.0), `max_tokens` (4000), reasoning setting (off) and user message. Only the system prompt differs.

| Arm | System prompt |
|---|---|
| `baseline` | "You are a helpful assistant." |
| `oneliner` | "You are a helpful assistant. Be original: avoid cliches and look past the first, most obvious idea." |
| `bohemian` | `SKILL.md` + `references/techniques.md` + `cliches.md` + `modes.md`, as an agent would see them after reading the files the skill points to, plus one line saying scripts cannot run |
| `antialgorithm` | the same preamble + Antialgorithm's unmodified `SKILL.md` (`eval/competitors/antialgorithm/`, commit `a6392c0`). Run on the test split of v3 only, added afterwards |

The one-liner arm follows Ponytail's practice. If a one-line instruction matches the skill, the skill is not worth its tokens, and the benchmark should show that.

**User message wrapper (identical for every arm):** the task, then *"(Format: you have no hidden thinking space here. First plan in brief notes. Then put the finished piece, exactly as you would hand it to me, between `<final>` and `</final>`. I will only see what is inside `<final>`.)"* Only the `<final>` content is judged or measured.

Why the wrapper: both generator models think adaptively by default. With thinking on, DeepSeek sometimes spent the whole token budget on hidden reasoning and returned nothing, and reasoning tokens varied a lot by arm. With thinking off and no planning instruction, every arm, Bohemian included, skipped planning and wrote the piece directly, so the method in the skill never ran. Telling every arm to plan briefly gives all arms the same chance to think, and the skill is the only thing that changes *how*. In agents with extended thinking (Claude Code, Codex), the planning happens in thinking instead.

## Models

| Role | Models | Why |
|---|---|---|
| Generators (under test) | `deepseek/deepseek-v4.1-flash`, `anthropic/claude-haiku-5.5` | Two families, both cheap. Results are reported per model. |
| Judges | `google/gemini-2.5-flash-lite`, `openai/gpt-4o-mini` | Different families from both generators, to reduce self-preference. Non-reasoning, temperature 0. |
| "Obvious answer" anchors | same two judge-family models | So no arm is measured against its own outputs |
| Embeddings | `openai/text-embedding-3-small` | |

`qwen/qwen3-235b-a22b-2507` was the original second judge. It failed the self-test because its OpenRouter provider returned degenerate one-word-per-line text, so it was replaced before any real judging.

All calls go through OpenRouter. The total budget was capped at USD 3.00 by a ledger that refuses calls past the cap. Every request is cached by a hash of its full body, so reruns are free and exact.

## Benchmark

54 tasks in 12 categories (`eval/tasks.jsonl`): fiction, short stories, poetry, marketing copy, headlines, naming, brainstorming, story concepts, characters, analogies, rewriting, brand positioning. 42 tasks carry a hard constraint (word limit, line or item count, paragraph count, forbidden words) that is checked deterministically. 12 are open.

**Splits.** The first task of each category (12 tasks) is the **dev** split. Only dev outputs were read while revising the skill. The other 42 are the **test** split, and the headline numbers for revised versions come from test only.

**Samples.** 3 independent generations per (task, model, arm): 54 × 2 × 3 × 3 = 972 generations per run.

## Metrics

No single score is the evidence. The eight requested dimensions map to instruments as follows:

| Dimension | Judge-based | Judge-free |
|---|---|---|
| Originality | pairwise `original`; absolute `originality` | typicality: cosine similarity to the "obvious answer" anchor |
| Semantic diversity | | 1 − mean pairwise cosine between the 3 samples; mean 3-gram Jaccard between samples (Self-BLEU-like); similarity between the two models' outputs; similarity *between items* inside one list output |
| Distinctiveness | pairwise `distinctive`; absolute `distinctiveness` | |
| Specificity | absolute `specificity` | |
| Anti-cliché | | lexicon hits per 100 words, split into **shared** (the tell appears in the skill text) and **held-out** (it does not) |
| Coherence | absolute `coherence` | |
| Task alignment | pairwise `task`; absolute `task_alignment` | deterministic constraint pass rate |
| Creative risk | pairwise `unpredictable`; absolute `creative_risk` | |
| Would you use it | pairwise `prefer` | |

**Why distance is never treated as originality on its own.** Typicality and diversity reward any departure, including nonsense. They count as evidence only next to coherence, task alignment and preference. The judge self-test (below) checks that the judges do not reward random weirdness.

**Held-out clichés.** The lexicon (`eval/lexicon.py`, 162 entries) was written separately from the skill. 61 entries also appear somewhere in the skill's text, and the rest are held out. If Bohemian only reduced shared tells, it would be teaching to the test. The held-out rate shows whether the reduction generalizes.

## Judging protocol

- **Blind.** Judges see the brief and the final text only: no arm names, no planning notes.
- **Pairwise:** treatment vs each reference arm, for the same (task, model, sample index). A/B position comes from a hash, so it is random, reproducible and balanced. Five questions: original, unpredictable, distinctive, prefer, task. Answers are A, B or tie. Both judges judge every pair.
- **Absolute:** each output scored alone, 1–5 on six anchored dimensions. The primary judge (Gemini) scores every output. The second judge scores sample 0 of each cell to measure agreement.
- **Self-test before trusting a judge** (`eval/judge_selftest.py`). Three hand-written triples (clichéd, distinctive, off-brief-but-weird) for a naming task, a poem and an ad, each pairwise check run in both A/B orders. A judge must rank distinctive above clichéd on originality, rank clichéd above off-brief on task fit, prefer distinctive over off-brief, and give the off-brief text lower absolute task alignment. Results:
  - Gemini: 23/24 checks. It called the off-brief surreal poem a tie with the clichéd poem on task fit in one order.
  - GPT-4o-mini: 23/24 checks. It gave nonsense names 5/5 absolute task alignment because the format was right.
  - Consequence: pairwise `task` and the deterministic constraint checks are the primary alignment evidence. Absolute task alignment is reported but treated as lenient.

## Statistics

- The **task** is the unit of analysis. Each metric is averaged over models and samples within a task, then compared with paired per-task differences.
- 95% intervals are percentile bootstraps over tasks (10,000 resamples, fixed seed).
- "Better on X of Y tasks" uses an exact two-sided sign test.
- Pairwise win rate = (wins + ½ ties) / judgments, averaged per task. 50% means no difference.
- Judge agreement: percent identical verdicts and Cohen's κ (pairwise). Spearman ρ (absolute, on the overlap subset).
- Position bias: treatment win rate shown separately for A and B placement.

## Stronger-judge audit

The two pairwise judges are small models. `eval/audit.py` re-judges a random, task-stratified sample of test-split pairs (40–60 per reference) with `openai/gpt-5.4-mini`, using the same blind prompt. It reports that judge's win rates next to the cheap judges' verdicts on the *same* pairs, plus `prefer` agreement. It checks judge taste. It does not replace the main judges.

## Development protocol

1. v1 was run on all 54 tasks exactly as first written.
2. Failures were analysed on the **dev split only** (outputs, planning notes, judge reasons, a strong-judge audit of dev pairs, and one ablation).
3. Each revision was evaluated on dev first, then run on all tasks. Headline numbers come from the 42-task **test split**, whose outputs were never read while revising.
4. From v2 on, an arm-agnostic rule resamples outputs that came back empty because the provider spent the whole budget on hidden reasoning. v1 had 4 such cells (all Bohemian/DeepSeek), which were kept and scored as losses.

## Human evaluation

`eval/human/build.py` builds a self-contained `review.html`: one brief and two responses per page, randomized sides, the five questions, answers saved in the browser and downloadable as JSON. The key mapping sides to arms is written to a separate `key.json`, which reviewers never see. `eval/human/score.py` scores any number of answer files against the key: preference rate per question, W/T/L, sign test, and Fleiss' κ across reviewers.

**Status: the human study has not been run.** The kit is built and tested, but no human ratings exist yet. See the results page.

## Reproducing

```bash
export OPENROUTER_API_KEY=...
python3 eval/judge_selftest.py                       # validate judges
python3 eval/generate.py  --run v1                   # 972 generations
python3 eval/judge.py     --run v1                   # pairwise + absolute
python3 eval/metrics.py   --run v1                   # judge-free metrics
python3 eval/analyze.py   --run v1 --split all       # report_*.md + summary_*.json
python3 eval/audit.py     --run v1 --per-ref 40       # stronger-judge audit
python3 eval/compare.py   --runs v1,v2,v3 --split test
```

With the request cache (`eval/.cache/`) present, every command above reproduces the published numbers with no API spend. The cache is 213 MB and is not committed. Without it, `analyze.py` and `compare.py` still reproduce every table from the saved results, while regenerating outputs means paying again and, at temperature 1.0, getting similar rather than identical numbers.
