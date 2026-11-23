# Divergence techniques

Each technique belongs to a **family**. Families matter more than techniques: two techniques from the same family tend to produce the same kind of surprise. When weighing directions, take them from different families, and prefer a family you have not used recently (`python3 scripts/moves.py` shows the counts).

Every entry says what it does, when it fits, and how it goes cheap. If you can see the cheap version in your draft, you have not used the technique, you have used its cliche.

---

## Family: lens (who sees it)

**Displaced witness.** Tell it through someone at the edge of the event who has a real stake in it: the person who cleans up afterwards, the one who sold the ticket, the neighbor who hears it through the wall.
Fits: stories, essays, ads where the obvious narrator is the hero or the brand.
Goes cheap: the narrator is an object, an animal or "the house itself". That move is now a default of its own.

**Inverted stake.** Find who loses if the obvious story goes well, or who would argue against the product, and let their logic in.
Fits: positioning, persuasive copy, conflict in fiction.
Goes cheap: a strawman objection set up to be knocked down.

**Wrong expert.** Describe the subject through the vocabulary of someone who knows a lot about something adjacent (a plumber on grief, an accountant on a love affair) where the transfer reveals something true.
Fits: essays, poems, character voice, analogies.
Goes cheap: the jargon is a joke and reveals nothing.

## Family: material (what it is made of)

**Specificity injection.** Replace each general noun with the particular one this situation would have. Not "food" but what is actually on the plate, not "a city" but the thing on its pavement.
Fits: everything; it is the safest technique and the core of `mild`.
Goes cheap: exact times, counts and brand names added only to look concrete. A detail must do work: reveal, contrast or move the piece.

**Source-domain transfer.** Explain or frame the subject through a field with the same underlying structure but no surface resemblance. Find the structure first ("both are about things that only work when nobody notices them"), then the domain.
Fits: analogies, headlines, naming, conceptual essays.
Goes cheap: the domain is picked for being exotic (jazz, chess, cooking, gardening, oceans are the overused ones), not for sharing the structure.

**The true odd fact.** Build on a real, checkable detail of the subject that most people do not know or forget.
Fits: copy, articles, brand stories, poems about familiar things.
Goes cheap: an invented fact presented as real. Never do that for non-fiction or claims.

## Family: form (what shape it takes)

**Borrowed vessel.** Pour the piece into a form that real people use for something else, when that form carries meaning for this subject (a returns policy for a breakup, a recipe written by someone who cannot cook for an ad about a meal kit).
Fits: short fiction, poems, campaigns.
Goes cheap: the form is a gimmick and the content would be the same in plain prose. Overused vessels: diary/log entries, letters to the future, lists of rules, error messages, chat transcripts.

**Constraint manipulation.** Add a constraint the brief does not need but the subject rewards (one sentence, no adjectives, only questions, the word count of something meaningful), or remove one everybody assumes (the product never appears, the hero never speaks).
Fits: poems, slogans, flash fiction, naming.
Goes cheap: the constraint is visible but changes nothing about what is said.

**Structural displacement.** Move the center of gravity: start at the consequence, spend the piece on the moment before the usual climax, give the ending first, or let the important event happen off-page.
Fits: stories, essays, case studies.
Goes cheap: nonlinear order for its own sake; the "twist" ending a reader saw coming.

## Family: premise (what it is about)

**Assumption reversal.** List the assumptions the default makes (the astronaut is lonely because she is far away; the cleaner app is about speed) and flip or question one that is actually doubtful.
Fits: concepts, startup ideas, positioning, plots.
Goes cheap: flipping to the famous opposite. Flip the assumption that is quietly wrong, not the one that is loudly obvious.

**Contradiction held.** Find two true things about the subject that pull against each other and do not resolve them.
Fits: characters, essays, poems, brand tension.
Goes cheap: a contradiction that resolves neatly in the last line.

**Stakes relocation.** Keep the situation, change what is actually at risk: smaller, more private, more practical, or owned by a different person.
Fits: fiction, ads, concepts.
Goes cheap: inflating the stakes (the world will end) instead of moving them.

**Genre transposition.** Keep the subject, apply the expectations of a genre that is not its usual one, when the genre's machinery shows something new (a heist structure for a family dinner, a nature documentary voice for an office).
Fits: fiction, campaign concepts, comic copy.
Goes cheap: parody that stays on the surface of the genre.

## Family: subtraction (what is left out)

**Remove the expected center.** Write it without the element everyone puts in the middle: the love story without the confession, the product ad without the product benefit, the ghost story without the ghost.
Fits: poems, short fiction, high-end brand copy.
Goes cheap: the absence is announced instead of felt.

**Cut the explanation.** Trust the reader with the connection. Delete the line that tells them what the image meant.
Fits: everything, especially endings.
Goes cheap: obscurity; the reader cannot rebuild the connection.

## Family: chance (where the start comes from)

**Seed.** Roll `python3 scripts/seed.py [text|idea|name]` and tie the result to the subject with a reason. Use it when the brief is thin, or when every direction you weigh comes from the same family.
Fits: open briefs, brainstorming.
Goes cheap: the seed is pasted on top of a default piece instead of changing it.

---

## Choosing between directions

For each direction, write: family, one-line summary, the fact from the brief it grows from, the main risk. Then ask:

1. Which serves the user's purpose best?
2. Which is truest to their voice and audience?
3. Which could only belong to this brief?

Two directions that share a family or a summary are one direction; replace one.
