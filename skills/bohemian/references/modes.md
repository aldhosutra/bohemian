# Modes

All modes use the method in `SKILL.md`. These are the differences.

## brainstorm

Return several directions that differ **in kind**. The user asked how many? Give that many. Otherwise give five at `mild`/`bold`, seven at `wild`.

- Take the directions from at least three technique families.
- Before writing the list, write the obvious three ideas to yourself and leave them out, unless you keep one as the labelled safe option.
- Each item: a short name, two or three sentences on the idea, and one line beginning "Why here:" with the fact from the brief it stands on.
- Check the list for clones: if two items share a mechanism, a target user or a premise, replace one.
- End with one recommendation and the reason for it. Do not leave the user with a neutral menu.

## rewrite

The user gave a draft. They own it.

- First, note the draft's voice (sentence length, register, vocabulary, humor) and its fixed content (facts, claims, names, calls to action, length). Both survive.
- Then name what makes it generic: the default premise, the stock material, the tells.
- At `mild`: keep the structure and the argument; replace stock material with specifics and remove tells. The author should recognize every paragraph.
- At `bold`: you may change the angle or the shape, but keep every fact and the purpose.
- At `wild`: you may change the form entirely, but the piece must still do the original job for the original audience.
- Do not add facts the draft does not contain. If a specific would help and you do not have it, use a clearly marked placeholder like `[the street your shop is on]` rather than inventing one.
- Return the rewrite only, unless asked to explain. Keep roughly the original length unless asked otherwise.

## critique

Report; do not rewrite. Write for the author, in plain words.

1. **What it does well**, in one or two sentences. Be specific; no flattery.
2. **The default it leans on**: name the premise, shape and material a reader would predict, and point to where the piece takes them.
3. **Findings**, numbered, most important first. Each finding has:
   - the quoted passage,
   - what is predictable or generic about it, and why that matters for this piece's purpose,
   - one concrete direction to fix it (a direction, not a finished rewrite), tied to a fact of the piece.
4. **The biggest opportunity**: the one change that would make the piece most its own.

Do not count something as a finding just because it is common. A convention that serves the purpose is fine; say so if it comes up. Keep findings to what would change a reader's experience. If the scripts can run, `python3 scripts/lint.py <file>` gives a first pass of surface tells; never stop at it.

## compare

Develop two or three directions far enough to judge them (a paragraph, an opening, a sample of five names, a tagline with its first line of body copy).

- Directions come from different technique families.
- For each: the family, the one-line idea, the sample, what it gains, what it risks.
- Then pick one and say why, using the user's purpose and audience. If combining two is better, show the combination.
