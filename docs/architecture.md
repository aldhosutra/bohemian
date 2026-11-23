# Architecture

Bohemian is an [Agent Skill](https://agentskills.io): a folder with a `SKILL.md` whose frontmatter tells the agent when to load it. Everything else is optional and loaded on demand.

```
skills/bohemian/
  SKILL.md                 always loaded when the skill triggers (~1.9k words): intent, method, intensity, voice, memory, output
  references/
    techniques.md          read during step 3: six technique families, each technique with its "goes cheap" failure
    cliches.md             read during step 2: tells by kind of piece, plus second-order "creative mode" tells
    modes.md               read only for brainstorm / rewrite / critique / compare
  scripts/                 optional, Python 3 stdlib only
    seed.py                external starting point for thin briefs (text | idea | name), avoids recent values
    moves.py               log of main moves by technique family; warns on streaks
    lint.py                surface-tell scanner for drafts (first pass only)
    state.py               shared history file (~/.local/state/bohemian/history.jsonl or $BOHEMIAN_HOME)
.claude-plugin/            Claude Code plugin + marketplace manifests
eval/                      benchmark, judges, metrics, statistics, human review kit (not needed at runtime)
tests/                     unittest suite for scripts and evaluation logic
```

## Runtime flow

```
user request
   │
   ▼
[1 Read the brief] ── fixed parts, purpose, audience, voice markers
   │
   ▼
[2 Name the default] ── per layer: premise · shape · material · voice      ◄── references/cliches.md
   │
   ▼
[3 Diverge for a reason] ── directions from different families,            ◄── references/techniques.md
   │                         each anchored to a fact of the brief            ◄── scripts/moves.py (family use)
   │                                                                         ◄── scripts/seed.py (thin brief)
   ▼
[4 Choose] ── best for the user's purpose, not the strangest
   │
   ▼
[5 Make it] ── concrete, plain, voice kept, fixed parts kept
   │
   ▼
[6 Critique, refine once] ── swap test · default test · reason test         ◄── scripts/lint.py
   │                         tells · brief test
   ▼
deliver ──► scripts/moves.py add <family> "<move>"
```

Steps 1–4 and 6 are private. In agents with extended thinking they happen there. In a plain chat without thinking, the model has to plan in visible text or skip the steps. The benchmark measured this and made planning equal across all arms (see `docs/evaluation.md`).

## Design decisions

**Progressive disclosure.** `SKILL.md` holds the method. The longer references load only at the step that needs them, and `modes.md` loads only for non-default modes. This keeps the always-loaded cost down while letting the method point to detail.

**Scripts are optional.** Every script-backed step has a no-script fallback written into the skill (session-only move discipline, a seed-free start from the brief's own facts, a manual tell scan). The benchmark ran with no scripts at all.

**Intensity defined by what may move.** `mild` lets material and wording move, `bold` adds premise, angle and shape, and `wild` allows anything the brief does not fix. Defining levels by *scope* rather than by "how weird" keeps wild coherent: it gets more freedom, not a mandate for strangeness.

**Families, not just moves, for anti-repetition.** The log stores a family and a short description. Streaks within a family trigger a warning, since two techniques from one family produce the same kind of surprise.

**No hooks, no always-on mode.** Creative help is request-scoped, and the skill description triggers on creative requests and on complaint words ("too generic", "cliché"). That avoids per-agent hook code (Ponytail ships about ten variants) and keeps the skill portable.

## Memory: session vs persistent

| | Session-only | Persistent (`moves.py`, `seed.py`) |
|---|---|---|
| What is remembered | moves made earlier in the same conversation | the last 500 rows: main move + family, recent seed values |
| Survives a new conversation | no | yes, until the file is deleted |
| Survives context compaction | only if the summary keeps it | yes |
| Shared across agents on the same machine | no | yes (one file under `~/.local/state/bohemian/`) |
| Requires | nothing | Python 3, permission to run scripts |
| Privacy | stays in the conversation | stores move descriptions only, never the user's content (the skill instructs this; it is not enforced) |
| Limits | forgets everything at the end | the model must remember to run it; nothing forces a log entry; a single shared file mixes all projects |

Neither kind of memory gives Bohemian knowledge of what *other users* got. That is why seeds come from system randomness rather than from the model's sense of what would be interesting.

## Portability

- **Claude Code:** plugin (`/plugin install`) or a plain skill folder in `~/.claude/skills/`.
- **Codex, Cursor, OpenCode, Gemini CLI, GitHub Copilot and others that read Agent Skills:** `npx skills add <repo>` copies `skills/bohemian/` to the right folder.
- **Any chat model:** paste `SKILL.md` (and optionally the references) into a system prompt. This is exactly what the benchmark does.
