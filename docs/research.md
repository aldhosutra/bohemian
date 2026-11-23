# Phase 1: research notes on Ponytail and Antialgorithm

Studied on 2026-11-23 from the source of each repository (shallow clones of the default branch).

| | Ponytail | Antialgorithm |
|---|---|---|
| Repository | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | [mankidev/antialgorithm](https://github.com/mankidev/antialgorithm) |
| License | MIT (c) 2026 DietrichGebert | MIT (c) 2026 mankidev |
| Domain | Code generation | Creative choices (names, copy, visuals, UI) |
| Core file | `skills/ponytail/SKILL.md` (~1k words) | `SKILL.md` (~1.8k words) + `visuals.md` |
| Runtime | Node hooks (SessionStart, UserPromptSubmit, SubagentStart), many per-agent manifests | Python stdlib scripts (`seed.py`, `moves.py`, `history.py`), optional `check.py`/`rough.py` for SVG |

## How Ponytail improves generated code

- **A decision ladder.** Before writing, the model walks an ordered list and takes the first option that fully works: does it need to exist, is it already in the codebase, the standard library, an installed dependency, a one-liner, then the minimum new code. The order is the behavior.
- **Hard floors.** A short "never cut" list (validation at trust boundaries, data-loss handling, security, accessibility) stops laziness from becoming negligence.
- **Levels.** `lite | full | ultra`, switched with an argument, each a one-line change in behavior.
- **Always-on activation.** Hooks re-inject the rules every session and into subagents, so the mode survives context compaction.
- **Separate review skill** with a strict output contract: every finding needs a concrete failure case, "no case, no finding".
- **Benchmarking culture, which matters most here.** The agentic benchmark (`benchmarks/agentic/`) runs headless sessions per arm, includes a deliberately cheap competitor arm ("Follow YAGNI principles.") so the benchmark can show that a one-liner matches the skill, validates its LLM judges with `--selftest` reference pairs before trusting them, reports per-task ratios with geometric means, bootstrap intervals and sign tests, and publishes runs it loses.

## How Antialgorithm identifies conventional choices

- **Name the default.** Before answering, the model states the obvious pick to itself in one line ("the default here is X") and does not use it unless the context asks for it.
- **The reason must come from the case.** A choice has to have a one-sentence reason drawn from this project. A choice that could belong to any project is a default.
- **No famous opposites.** "Dark instead of bright" is called out as the second most common answer.
- **Lists of tells.** Concrete marks of default AI text (closing offers, bold labels, triads, mirrored slogans, a summing-up last line, even rhythm).
- **The escape becomes a default.** A list of the skill's *own* habits (the analog look, cream backgrounds, exact times, borrowed frames such as forms and schedules) and an instruction to treat a repeated escape as a new default.

## How Antialgorithm encourages divergence

- **Seeds from outside the model's taste.** `seed.py` draws from system randomness over pools (visual: method, color, layout, type, verb, scale, setting, region, anchor; text: voice, entry, register; idea: verb, constraint, scale, pressure). The rationale: the model cannot see what other users got, so a starting point chosen by the model's own sense of "interesting" lands everyone in the same place.
- **Anti-repetition across sessions.** Seeds are logged to `~/.local/state/antialgorithm/history.jsonl`, and the picker avoids values from the last dozen seeds. `moves.py` logs the main move of each off-default answer, and the model reads the log before showing new work.
- **Region as historical or cultural context.** The seed's region shapes setting details, with an explicit rule to use what a resident knows from a normal week rather than what an outsider lists first.
- **Validation is informal.** CONTRIBUTING asks for running the same prompt several times with old and new text and comparing sets. The README's showcase compares an unfiltered baseline batch with a *picked* treatment batch, so it is illustrative rather than evidence.

## What Bohemian reuses conceptually

| Idea | From | How Bohemian uses it |
|---|---|---|
| Name the default before diverging | Antialgorithm | Step 2, broken into four layers (premise, shape, material, voice) so a piece can keep a default shape while changing its premise |
| One-sentence reason from the brief | Antialgorithm | The "anchored" rule and the reason test in step 6 |
| No famous opposites | Antialgorithm | Stated in step 3 and in each technique's "goes cheap" note |
| The escape becomes a default | Antialgorithm | Second-order tells named in each technique family's "goes cheap" column; the move log |
| External seeds, history-aware | Antialgorithm | `scripts/seed.py`, with pools designed for writing and ideation (lens, entry, shape, register; verb, constraint, who, pressure; naming source, form, feel) |
| Levels via argument | Ponytail | `mild / bold / wild`, defined by *what may move*, not by how strange the result is |
| Ordered steps, hard floors | Ponytail | The six-step method; fixed parts of the brief are never traded for novelty |
| Strict output contract for review | Ponytail | The `critique` mode: quoted passage, why it is predictable for *this* purpose, a direction tied to the piece |
| Cheap competitor arm, validated judges, per-task stats, publish losses | Ponytail | The whole evaluation design (`docs/evaluation.md`) |

## What needed redesigning for creative writing

- **Writing has layers that can move independently.** Antialgorithm treats "the default" as one thing. In writing, a piece can rightly keep a conventional structure while its premise is fresh, or the reverse. Bohemian names the default per layer and intensity decides which layers may move.
- **Techniques need families.** Anti-repetition by exact move ("x-ray poster") does not stop the model from making the same *kind* of move. Bohemian groups techniques into six families (lens, material, form, premise, subtraction, chance), and `moves.py` warns when the same family repeats.
- **Each technique ships with its cheap version.** "Perspective inversion" decays into "the object narrates". Each technique entry names the decayed form so the model can recognize it in its own draft.
- **Voice preservation is a first-class constraint.** Antialgorithm optimizes the choice, while writing often comes with a voice to keep (a draft, a brand). Bohemian extracts voice markers in step 1 and checks them in step 6.
- **Modes.** Creative work needs create, brainstorm, rewrite, critique and compare, and each needs a different output contract.
- **Visual tooling is out of scope.** Antialgorithm's SVG scripts (`check.py`, `rough.py`) do not apply. Bohemian's deterministic aid is a text linter (`lint.py`).
- **No hooks.** Ponytail's always-on hooks suit a mode that should govern every coding turn. Creative help is request-scoped, so Bohemian is a model-invoked skill with a description that triggers on creative requests, which keeps the runtime to Markdown plus optional stdlib scripts.

## Licensing

Both projects are MIT. Bohemian copies no code or instruction text from either; all skill text and scripts were written for this project. The concepts above are credited in the README and here.

## Research for v5: what could make Bohemian clearly better than Antialgorithm

Done after v4b (2026-11-23). Where v4b stands against Antialgorithm on the test split: cheap judges prefer v4b (57%) and the stronger judge calls it even (48%, n=40). Antialgorithm is still a little further from the obvious answer (typicality 0.549 vs 0.582) and has fewer raw cliché hits (20 vs 32), and judges rate it more original on fiction (v4b 42%), rewrites (39%) and short stories (44%). v4b's remaining hits are mostly stock names ("Mara" 6, "Vance" 5) and clock times (8).

| Finding | Source | What it suggests for Bohemian |
|---|---|---|
| Asking the model for several candidates *with their probabilities* (Verbalized Sampling) raised creative-writing diversity 1.6–2.1× over direct prompting, with better human ratings. Mode collapse is traced to typicality bias in preference data. | [Zhang et al., 2025, arXiv 2510.01171](https://arxiv.org/abs/2510.01171) | In the plan, list candidate directions with a rough "how likely would a typical model write this" estimate and pick from the low-probability tail that still passes the brief. Antialgorithm has no such step. |
| Models repeat themselves and converge with each other on open-ended prompts (the "Artificial Hivemind"). A later critique argues the evidence is weaker than claimed, and that prompting reliably raises diversity. | [Jiang et al., 2025, arXiv 2510.22954](https://arxiv.org/abs/2510.22954); [Schaeffer et al., arXiv 2609.33936](https://arxiv.org/pdf/2609.33936) | Cross-model similarity is the right metric to watch. |
| Having the model first write a random string and derive its answer from it (String Seed of Thought) raised NoveltyBench diversity without hurting quality. Prepending unrelated random words also raises diversity. | [Misaki & Akiba, arXiv 2510.21150](https://arxiv.org/abs/2510.21150); [Agrawal & Goyal, arXiv 2601.18053](https://arxiv.org/abs/2601.18053) | A script-free seed: when `seed.py` can't run, the plan starts from a self-generated random string, used to choose among tail candidates and for names and setting. |
| Inference-time methods tend to trade quality for originality. | [Beyond Memorization, arXiv 2504.09389](https://arxiv.org/abs/2504.09389) | Keep v4b's payoff and brief checks, since they are where Bohemian beats Antialgorithm. |
| Simple "think outside the box" prompts beat complex creativity frameworks (TRIZ, SCAMPER) for novelty. | [IDEAFix, arXiv 2606.00875](https://arxiv.org/pdf/2606.00875) | Consistent with the one-liner's strength. Keep the skill short; don't add frameworks. |
| Slop phrases are best found by over-representation against human text, and suppressed at decoding time; prompt-level bans are weaker. | [Paech et al., Antislop, arXiv 2510.15061](https://arxiv.org/abs/2510.15061) | Naming clichés in the prompt can plant them. Prefer naming the *kind* of move. Leave word lists to `lint.py` after drafting. |
