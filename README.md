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

One file, [`skills/bohemian/SKILL.md`](skills/bohemian/SKILL.md), about 1,100 words. Before writing, the model makes a five-line plan, in its thinking or in hidden notes:

1. **Fixed:** format, facts, audience, voice, and the target length as a number.
2. **Default:** the obvious premise, shape and stock material for this brief.
3. **Directions:** three that differ in kind, each from a different technique *family* (premise, material, form, subtraction, lens) and each grown from a specific fact of the brief.
4. **Pick:** the strongest hook that still serves the purpose. Not the strangest, not the most restrained.
5. **Reason:** one sentence, from the brief, for why it belongs here.

Each family names **how it goes cheap**, because every escape eventually becomes a default. The writing rules cover concrete detail, names taken from the world of the piece rather than stock names, numbers only when the reader needs them, endings that stop, and never running longer than the brief asks. A final check asks whether the piece could be pasted into another brief, whether it pays off as fully as the obvious version would, and whether it does exactly what was asked.

Optional stdlib scripts add an external seed for thin briefs (`seed.py`), a cross-session log of moves by family so the skill doesn't repeat itself (`moves.py`), and a tell linter (`lint.py`). Details: [methodology](docs/methodology.md) · [architecture](docs/architecture.md).

**Intensity** is defined by what may move: `mild` (material and wording), `bold`, the default (adds premise, angle and shape), `wild` (anything the brief doesn't fix, still coherent).

**Modes:** `create`, `brainstorm`, `rewrite`, `critique`, `compare`. When no mode is named, it's inferred from the request.

## Evidence

Benchmark: 54 creative tasks, two generator models (DeepSeek V4.1 Flash, Claude Haiku 5.5), 3 samples each, blinded LLM judges from other model families, judge-free metrics, per-task bootstrap CIs. Headline numbers come from 42 test tasks never looked at during tuning. Full report: **[docs/benchmark-results.md](docs/benchmark-results.md)**.

The current skill is **v4b**, a lean rewrite of the earlier v3 (about 4,400 words with its reference files). On the test split:

| | no skill | one-line prompt | [Antialgorithm](https://github.com/mankidev/antialgorithm) | Bohemian v3 | **Bohemian v4b** |
|---|---|---|---|---|---|
| Input tokens per call (DeepSeek / Haiku) | ~80 / 120 | ~100 / 140 | 2,422 / 3,236 | ~6,100 / 8,800 | **1,624 / 2,318** |
| Output length (words) | 169 | 194 | 169 | 203 | **173** |
| Hard limits passed | 94.0% | 87.0% | 88.4% | 89.8% | **94.9%** |
| Clichés per 100 words | 0.44 | 0.28 | **0.03** | 0.21 | 0.18 |
| Similarity to an "obvious answer" anchor (lower = more original) | 0.737 | 0.626 | **0.549** | 0.605 | 0.582 |
| Diversity across repeated samples | 0.187 | 0.267 | **0.323** | 0.276 | 0.319 |

Blinded judgments, Bohemian v4b's win rate [95% CI]:

| against | cheap judges: preferred | cheap judges: task fit | stronger judge (GPT-5.4-mini, 40 pairs): preferred |
|---|---|---|---|
| no skill | **68%** [60–76] | 45% [40–50] | 85% |
| one-line prompt ("Be original: avoid cliches and look past the first, most obvious idea") | 33% [28–38] | 39% [35–44] | 48% |
| Antialgorithm | 57% [52–62] | 50% [46–55] | 48% |

What this shows:

- **Against no skill, Bohemian clearly wins**: judges prefer it, it is less clichéd (−89% on held-out clichés), further from the obvious answer (−21%) and more varied (+71%), at the same length and with the best hard-limit pass rate of any arm.
- **Against the one-line prompt, it has not been shown to be better.** The cheap judges prefer the one-liner. The stronger judge calls it even. Judge-free, Bohemian is slightly further from the obvious answer, more varied, and keeps limits far better (94.9% vs 87.0%).
- **Against Antialgorithm, LLM judges call it a tie, and it is cheaper.** About 30% fewer input tokens. Cheap judges lean Bohemian, the stronger judge calls it even, and Antialgorithm is still a little further from the obvious answer and much lower on clichés. In one person's blind picks (below) Bohemian won clearly.

**Costs and caveats:**

- Cheap judges rate v4b's task fit below baseline (45%). The stronger judge rates it above (65%).
- Fiction, character sketches and short poems are its weakest categories (40%, 39% and 52% preferred vs baseline).
- **Human evaluation is small:** one rater's blind picks on posters and Shorts (below). The 40-pair text review kit has not been run.

## Blind picks by a person

LLM judges disagreed with each other and with people, so we also ran visual tests that a person can judge at a glance. Each arm made SVG posters (8 briefs) and playable 30-second HTML Shorts aimed at virality (2 topics), on the same two models with two samples each. Antialgorithm got its own visual guide (`visuals.md`); Bohemian has no visual guidance. One rater (the project owner) looked at each set unlabelled, in shuffled order, and picked the one they would put up or post.

| Test | Sets | Bohemian v4b | Antialgorithm | No skill | Other Bohemian versions |
|---|---|---|---|---|---|
| Posters, round 1 | 4 | 2 | 1 | 0 | v5: 1 |
| Posters, round 2 | 12 | **7** | 3 | 2 | v6: 0 |
| Playable Shorts | 4 | **3** | 1 | — | — |
| **Total** | 20 | **12** | 5 | 2 | 1 |

The picks were crafted, warm pieces built around one image or one twist tied to the subject: a river drawn as the run's map, a sheet-music choir poster, "Don't count sheep. Count to ninety." Later versions that pushed harder for surprise (v5) or for loudness (v6) lost. A vision judge (Gemini 3.1 Flash Lite) matched the rater's first choice no more often than chance, so these picks are the only quality evidence here that comes from a person. It is one rater, two cheap models and short briefs. Data and scripts: [`eval/results/v6/visual/`](eval/results/v6/visual/).

## Examples

From the v3 benchmark run. Picked by a fixed rule (first test task per category, sample 0), not for quality. More in [docs/examples.md](docs/examples.md), including the worst case.

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

**Any chat model:** paste `SKILL.md` into the system prompt. That is how the benchmark runs it.

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

- **Not better than a strong one-line instruction** on the evidence so far (see above), and not more original than Antialgorithm by the judge-free measures.
- **Almost no human ratings.** Apart from one rater's blind picks on posters and Shorts, all quality evidence comes from LLM judges, which here favored longer and more ornamental text and showed position bias.
- **Cheap generators only.** Results are for two small, fast models with thinking off. Larger models and agents with extended thinking are untested.
- **The method depends on planning.** With thinking off, Haiku wrote its plan in 92 of 162 v4b outputs. DeepSeek always planned.
- **Fiction and character work** are the weakest categories.
- **The escape becomes the default.** Outputs still slip into some second-order tells (a clock time to look concrete, a stock first name).
- **Memory** is best-effort. Nothing forces the model to log its moves, and the log is per machine, not per project.

## Credits

Bohemian's ideas build on two MIT-licensed projects. No code or instruction text from either is in the skill. The benchmark includes an unmodified copy of Antialgorithm's `SKILL.md`, with its license, in `eval/competitors/antialgorithm/` so it can be run as a comparison arm.

- [Antialgorithm](https://github.com/mankidev/antialgorithm) by mankidev: naming the default before moving away from it, case-specific reasons for each choice, external seeds, a log of moves, and the idea that the escape becomes a default.
- [Ponytail](https://github.com/DietrichGebert/ponytail) by Dietrich Gebert: intensity levels, an ordered method with hard floors, and benchmarking practice (a cheap competitor arm, self-tested judges, per-task statistics, publishing the runs you lose).

Research notes: [docs/research.md](docs/research.md). Development log: [docs/devlog.md](docs/devlog.md). Contributing: [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
