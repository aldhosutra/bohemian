---
name: bohemian
description: >
  Creative intelligence for writing and ideation: finds the obvious answer first,
  then moves past it on purpose, for a reason taken from the brief, while keeping
  the user's goal, constraints and voice. Use for stories, poems, essays, copy,
  headlines, slogans, names, brand positioning, brainstorming, characters, plots,
  worldbuilding, rewriting a flat draft, or critiquing a piece for cliches. Also
  use when the user says "bohemian", "make it less generic", "too AI", "boring",
  "cliche", "predictable", "seen it before". Not for code, docs whose form is
  fixed (README, changelog, legal text), or when the user asks for the standard version.
argument-hint: "[create|brainstorm|rewrite|critique|compare] [mild|bold|wild] [brief or text]"
license: MIT
---

# Bohemian

The first idea that arrives is the one most writers would have. It feels right because it is familiar. Bohemian makes you notice that idea, put it to one side, and look for the one that belongs to this brief and no other.

Unexpected is not the goal. A surprising choice with no reason is as empty as a safe one. The goal is work that does what the user asked, in their voice, and could not have been written for a different brief.

Original and good, never original instead of good. The piece must deliver what its form exists to deliver (a story that pulls you through and changes something, an ad that makes you want the thing, a name people can say and remember, a poem with an image that stays) at least as fully as the default would.

The user's own rules (CLAUDE.md, AGENTS.md, a style guide, a voice sample, an explicit request) always win. Bohemian only works on what the user left open.

## Arguments

- **Mode** (default `create`): `create` makes the piece. `brainstorm` returns several directions that differ in kind. `rewrite` transforms a given draft. `critique` reports what is predictable and how to fix it, without rewriting. `compare` develops two or three directions side by side and recommends one. For brainstorm, rewrite, critique and compare, read `references/modes.md`.
- **Intensity** (default `bold`): `mild`, `bold` or `wild`. See the table below.
- If no mode is named, infer it from the request: a draft to improve means `rewrite` (keep roughly its length), a request for ideas or options means `brainstorm`, a request for feedback means `critique`. Otherwise `create`.
- If the user just says "bohemian" with a brief, use `create` at `bold`.

## The method

The steps are short, but they are not optional: do not jump straight to the piece. Do them in your thinking if you have a thinking space. If you do not, and your environment gives you a place for notes the user will not see, write them there in a few lines each. The user sees the finished work, not the steps, unless the mode is critique or compare, or they ask.

### 1. Read the brief

Note, in a line each: what is being made, who it is for, what it is for, the tone, and the **fixed** parts (length, format, facts, names, required words, point of view, audience). Fixed parts are never traded for novelty. If a voice sample or draft is given, note its voice: sentence length, register, vocabulary, humor, what it never does. Your piece keeps that voice.

If the brief is thin and the piece is short, do not stall with questions: make one stated assumption about the context and write. If the piece is long or costly, ask one short question first. If the user wants it now, roll a seed (step 3).

### 2. Name the default

Write down the obvious version in one line for each layer that applies:

- **Premise / angle**: what most people would make this about.
- **Shape**: the usual structure, opening move and ending move.
- **Material**: the stock images, examples, metaphors and words this subject attracts.
- **Voice**: the register a generic assistant would use.

For names and slogans, list the three names or lines that would come to anyone first. Then read `references/cliches.md` once for the tells of this kind of piece, including the second-order ones (the moves models make when told to "be creative").

The default is a reference point, not a ban. Keep a default layer when the brief really asks for it, and say to yourself why.

### 3. Diverge for a reason

Build directions away from the default. Each direction must be:

- **Anchored**: it grows from a specific fact of this brief (the audience, the product's real use, a constraint, a detail the user mentioned, an odd truth about the subject). Say the reason in one sentence. If the reason would fit any brief, the direction is decoration.
- **Different in kind**: two directions that can be summarized with the same sentence are one direction. Change the premise or the shape, not just the words.
- **Not the famous opposite**: "dark instead of light", "the villain is the hero", "the object tells the story" are the second most common answers, not escapes.

Pick techniques from `references/techniques.md`. The list order is not a ranking, and the technique that comes to mind first is a default like any other (telling it through a bystander or witness is the one models reach for most). Prefer a family you have not used recently (see Memory below). If the brief gives you nothing specific to stand on, run `python3 scripts/seed.py` (path relative to this skill's folder) and tie what it gives to the subject with a reason. Never choose a starting point by asking yourself "what would be most interesting": that question lands everyone in the same place.

### 4. Choose

Pick the direction that best serves the user's purpose, not the strangest one. You may combine directions if the result has one clear idea. If you can only say why it is surprising and not why it fits, choose again.

### 5. Make it

- Concrete beats general: a thing someone could see, hear, touch or do in this situation.
- Precise words beat impressive ones. A vivid image is welcome when it is specific to this piece and earns its place.
- Specific does not mean small or quiet. A fresh premise can be big, funny, lush, warm or loud. Match the energy the brief and its audience want; do not default to understatement.
- Let feeling come from detail; do not name the feeling.
- Vary sentence length the way a person does.
- Keep every fixed part from step 1: length, format, facts, point of view, required elements. If a word, line, item or paragraph limit is set, count before you show it and cut to fit.
- Do not invent facts that could pass as real and cause harm (prices, specs, claims, statistics, quotes). Fiction and poems need no disclaimer.

### 6. Critique, then refine once

Before showing, check:

1. **Swap test**: could this be pasted into a different brief with small changes? Then it is too general. Fix the parts that fail.
2. **Default test**: is the premise, shape or main image the one from step 2? If yes, is there a reason the brief needs it?
3. **Reason test**: can you say in one sentence, using a fact of the brief, why each main choice is here?
4. **Tells**: scan for phrases and moves in `references/cliches.md`. If the scripts are available, `python3 scripts/lint.py <file>` lists them. Remove a tell only if the replacement is better, not merely different.
5. **Payoff test**: does it deliver what this form is for, as fully as the default would? A story needs pull and a change; copy needs desire; a name needs to be sayable and memorable; a poem needs an image that lands; a concept needs a hook. If the original version is thinner or flatter than the obvious one, it has not succeeded yet.
6. **Brief test**: re-read the request. Does the piece do exactly what was asked, in the asked length and format, for the asked audience, in the user's voice? Would the user actually use it? A piece that is original but off-brief has failed.

Make one refinement pass for real problems. Do not polish into blandness.

## Intensity

| | mild | bold (default) | wild |
|---|---|---|---|
| What may move | material and wording; premise and shape stay | premise, angle or shape may change | anything not fixed by the brief, including genre and form |
| Directions to weigh | 2 | 3 | 4, at least one high-risk |
| Typical move | swap stock details for specific ones, cut tells | an unexpected but apt angle, a structure chosen for this brief | a premise or form the user would not have asked for but will recognize as right |
| Guardrail | the user should recognize their own piece | a reader should never feel the novelty is a trick | strange is allowed; arbitrary is not; it must still be readable and on-brief |

Wild never means incoherent. If a wild choice needs a paragraph of explanation, it is not working.

## Voice

Bohemian has no house style. A minimalist stays minimal, a corporate brand stays usable by that brand, a children's story stays for children. Originality should come from the choices (what to notice, what to leave out, where to start, what to compare it to), not from ornament. If your draft sounds like "a creative writer" instead of like the user, rewrite it toward the user.

## Memory: do not let the escape become a habit

Any move that works becomes the next default. Watch for repeating yourself across pieces: the same technique family, the same kind of twist, the same closing move, the same naming pattern.

- If scripts can run: before choosing techniques, run `python3 scripts/moves.py` to see the recent moves and the under-used technique families. After delivering, record the main move: `python3 scripts/moves.py add <family> "<move in a few plain words>"`. Record the move, never the user's content.
- If scripts cannot run, keep the same discipline within the conversation: do not reuse the main move of an earlier piece in this session without a reason.

Session memory forgets when the conversation ends. The move log lives on the user's machine (`~/.local/state/bohemian/`) and persists until deleted.

## Output

Deliver the piece in the length and format asked for. In `create` mode, deliver one piece: no alternative versions, no menu of options, no recommendation, unless the user asked for options. No preamble, no notes about how it was made, no offer to revise, unless the user asked for options or explanation. If you made one assumption about thin context, add one short line after the work naming it and the one fact that would make it better.

If the user asks for the plain, standard or conventional version, give it. Bohemian is for choices left open, not for overruling the user.
