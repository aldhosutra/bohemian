# Bohemian

**Make the unexpected the default.**

Bohemian is an open-source agent skill for creative work: stories, poems, copy, headlines, names, brand positioning, brainstorming, characters, rewriting and critique. It makes the model find the obvious answer first, keep it in view, and move past it for a reason taken from the brief, while keeping the user's goal, constraints and voice.

> The first idea is usually the most obvious. Don't stop there.

Bohemian is not about making everything weird. A surprising choice with no reason is as empty as a safe one.

## Why AI writing sounds generic

A language model picks likely continuations, and the likely story about a lonely astronaut is the one most often written: a window, a small blue Earth, a lesson about connection. Three symptoms follow:

- **Convergence.** Different models land on the same idea. In this repo's benchmark, two unrelated model families produced baseline outputs with 0.75 mean embedding similarity for the same task.
- **Stock material.** "Tapestry", "a testament to", "say goodbye to", the benefit triad, the moral at the end.
- **Second-order defaults.** Told to "be creative", models reach for a second set of moves just as reliably: the object narrates, the story is a diary, exact times are sprinkled in to look concrete.

## How Bohemian works

A six-step method in [`skills/bohemian/SKILL.md`](skills/bohemian/SKILL.md):

1. **Read the brief.** Separate what is fixed (length, format, facts, audience, voice) from what is open.
2. **Name the default** for each layer: premise, shape, material, voice.
3. **Diverge for a reason.** Build directions from different technique *families* (premise, material, form, subtraction, lens, chance). Each must be anchored in a fact of this brief, different in kind from the others, and not just the famous opposite.
4. **Choose** what serves the purpose and has the strongest hook. Not the strangest option.
5. **Make it** concrete and fully realized, in the user's voice, inside every limit.
6. **Critique and refine once:** swap test, default test, reason test, tells, payoff test, brief test.

Each technique in [`references/techniques.md`](skills/bohemian/references/techniques.md) names **how it goes cheap**, because every escape eventually becomes a default. Optional stdlib scripts add an external seed for thin briefs (`seed.py`), a cross-session log of moves by family so the skill doesn't repeat itself (`moves.py`), and a tell linter (`lint.py`). Details: [methodology](docs/methodology.md) · [architecture](docs/architecture.md).

**Intensity** is defined by what may move: `mild` (material and wording), `bold`, the default (adds premise, angle and shape), `wild` (anything the brief doesn't fix, still coherent).

**Modes:** `create`, `brainstorm`, `rewrite`, `critique`, `compare`. When no mode is named, it's inferred from the request.

## Evidence

Benchmark: 54 creative tasks, two generator models (DeepSeek V4.1 Flash, Claude Haiku 5.5), 3 samples each, blinded LLM judges from other model families, judge-free metrics, per-task bootstrap CIs. Headline numbers come from 42 test tasks never looked at during tuning. Full report: **[docs/benchmark-results.md](docs/benchmark-results.md)**.

**Against the same model with no skill**, Bohemian v3 (current):

| | result [95% CI] |
|---|---|
| Judges preferred the Bohemian output | **73%** [65–80] of pairs |
| More distinctive / less predictable | 80% / 82% |
| Task fit | 53% [48–57], no measurable change |
| Clichés per 100 words, held-out lexicon the skill never sees | −50% |
| Similarity to an "obvious answer" anchor | −18% |
| Diversity across repeated samples | +48% |
| Stronger-judge audit (GPT-5.4-mini, 40 pairs) | 92% preferred |

**Against a one-line prompt** ("Be original: avoid cliches and look past the first, most obvious idea"), **Bohemian has not been shown to be better.** The two cheap judges preferred the one-liner (Bohemian 37% [31–43]). The stronger judge called it roughly even (55%, n=40). On judge-free measures, Bohemian is slightly further from the obvious answer (−3%) and the two models converge less (−5%). Otherwise the arms are statistically tied.

**Against [Antialgorithm](https://github.com/mankidev/antialgorithm)**, the skill Bohemian builds on, there is **no clear winner**. Head-to-head, the cheap judges preferred Bohemian 59% [52–65], partly because it writes longer, and the stronger judge called it even (52%). Judges rated Bohemian higher against the shared references. Antialgorithm wins every judge-free originality measure: about 8× fewer clichés, further from the obvious answer, more varied, 20% shorter. [Details](docs/benchmark-results.md#bohemian-vs-antialgorithm).

**Costs and caveats:**

- Bohemian misses hard length limits more often than baseline (89.8% vs 94.0% pass).
- Its outputs are 20% longer, and judges favor longer outputs. In length-matched pairs it wins 70% against baseline.
- Flash fiction is its weakest category (42% vs baseline).
- **No human evaluation has been run.** A blind review kit is included.

## Examples

Picked by a fixed rule (first test task per category, sample 0), not for quality. More in [docs/examples.md](docs/examples.md), including the worst case.

*"Write 5 headlines for a news story about a town that banned cars from its center."* (DeepSeek)

| Baseline | One-liner | Bohemian |
|---|---|---|
| Town Bans Cars From Center in Bid to Reclaim Streets for People | No Engines, No Problem: This Town Bet Its Downtown on Foot Traffic — and Won | Town Council Votes to Close Center to Cars, Starting Monday |
| Car-Free Comeback: Town Center Shuts Out Vehicles | The Quietest Revolution: How One Town Traded Parking Spots for Park Benches | Delivery Vans Get Two Hours. Everyone Else Walks. |
| No Cars Allowed: Town's Bold Move to Transform Its Center | They Erased Every Parking Meter in the Center. Local Shops Are Thriving. | The Main Street Experiment: Shops Watch, Traffic Counters Click |
| Town Pulls the Plug on Traffic in Downtown Car Ban | What Happens When a Town Says 'Walk, Don't Drive'? Nothing Anyone Expected | She Drove the Same Route for 22 Years. Next Week She Takes the Bus. |
| From Parking Lots to People: Town Center Goes Car-Free | Zero Cars, Full Cafes: The Unlikely Blueprint From a Town That Ripped Out Its Roads | What the Town Center Sounds Like Without Engines |

Both judges preferred Bohemian over baseline here, and the one-liner over Bohemian.

*"Write a 60-word product description for a stainless steel water bottle."* (DeepSeek)

> **Baseline:** Stay hydrated in style with this premium stainless steel water bottle. Double-wall vacuum insulation keeps drinks cold for 24 hours or hot for 12. Durable, leak-proof, and BPA-free… your perfect companion for gym, office, or adventure.
>
> **Bohemian:** This bottle has no opinions. It holds water, or coffee, or last night's tea. Stainless steel, so it dents instead of shattering, and clanks against a car door the way things do when they've been dropped a few times. No app, no reminder, no personality. Fill it. Cap it. Forget it on a desk and find it Tuesday. It'll still be cold.

The same task with Haiku produced Bohemian copy that is barely different from baseline. And the DeepSeek piece above still uses two moves the skill lists as tells: a named weekday used to look concrete, and a habitual triad.

## Install

The skill lives in `skills/bohemian/`. Replace `OWNER` with the GitHub account hosting this repo.

**Any agent that reads Agent Skills** (Claude Code, Codex, Cursor, OpenCode, Gemini CLI, GitHub Copilot and others), via the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add OWNER/bohemian
```

**Claude Code plugin:**

```
/plugin marketplace add OWNER/bohemian
/plugin install bohemian@bohemian
```

**Manual:** copy or clone `skills/bohemian/` into your agent's skills folder, for example `~/.claude/skills/bohemian` for Claude Code. To update, pull or re-run the install command. Your move log in `~/.local/state/bohemian/` is untouched by updates.

**Any chat model:** paste `SKILL.md` (and optionally the three reference files) into the system prompt. That is how the benchmark runs it.

The scripts are optional and need only Python 3.

## Use

In Claude Code, a skill installed in `~/.claude/skills` is invoked as `/bohemian`, and a plugin install as `/bohemian:bohemian`. Agents also load it on their own for creative requests, or when you say "too generic", "cliché", "make it less AI".

```
/bohemian write a story about a lonely astronaut
/bohemian brainstorm wild 7 names for a night-shift childcare service
/bohemian rewrite mild <paste your draft>
/bohemian critique <paste a piece>
/bohemian compare taglines for a secondhand furniture shop
```

Ask for "the standard version" and Bohemian steps aside.

Scripts, run from the skill folder:

```bash
python3 scripts/seed.py text          # or: idea | name; --keep "register=dry"; --no-log
python3 scripts/moves.py              # recent moves and least-used technique families
python3 scripts/moves.py add premise "e-bike sold as giving the commute back"
python3 scripts/lint.py draft.txt     # surface tells, first pass only
```

Set `BOHEMIAN_HOME` to keep the move log somewhere else.

## Run the benchmark

```bash
export OPENROUTER_API_KEY=...
python3 eval/judge_selftest.py                 # validate judges first
python3 eval/generate.py --run mine            # 972 generations (~USD 0.40)
python3 eval/judge.py    --run mine            # 2,592 blind judgments (~USD 0.40)
python3 eval/metrics.py  --run mine            # judge-free metrics
python3 eval/analyze.py  --run mine --split test
```

Spending is capped by `BOHEMIAN_BUDGET_USD` (default 3.00), and every request is cached. Method: [docs/evaluation.md](docs/evaluation.md). Blind human review: `python3 eval/human/build.py --run v3`, then `python3 eval/human/score.py answers-*.json`.

Tests: `python3 -m unittest discover -s tests`.

## Known limitations

- **Not better than a strong one-line instruction** on the evidence so far (see above).
- **No human ratings.** All quality evidence comes from LLM judges, which here favored longer and more ornamental text and showed position bias.
- **Cheap generators only.** Results are for two small, fast models with thinking off. Larger models and agents with extended thinking are untested.
- **The method depends on planning.** With thinking off, Haiku skipped the planning steps in most outputs even when told to plan. DeepSeek always planned.
- **Length limits** are missed more often than with plain prompting.
- **Fiction** (short scenes) is the weakest category.
- **The escape becomes the default.** Even with the second-order tells listed, outputs still slip into some of them (a named weekday, a reflex triad, "Ember" in coffee names).
- **Memory** is best-effort. Nothing forces the model to log its moves, and the log is per machine, not per project.

## Credits

Bohemian's ideas build on two MIT-licensed projects. No code or instruction text from either is in the skill. The benchmark includes an unmodified copy of Antialgorithm's `SKILL.md`, with its license, in `eval/competitors/antialgorithm/` so it can be run as a comparison arm.

- [Antialgorithm](https://github.com/mankidev/antialgorithm) by mankidev: naming the default before moving away from it, case-specific reasons for each choice, external seeds, a log of moves, and the idea that the escape becomes a default.
- [Ponytail](https://github.com/DietrichGebert/ponytail) by Dietrich Gebert: intensity levels, an ordered method with hard floors, and benchmarking practice (a cheap competitor arm, self-tested judges, per-task statistics, publishing the runs you lose).

Research notes: [docs/research.md](docs/research.md). Development log: [docs/devlog.md](docs/devlog.md). Contributing: [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
