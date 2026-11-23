# Creative methodology

## Why AI writing drifts toward the generic

A language model picks likely continuations. Averaged over everything it has read, the likely continuation of "write a story about a lonely astronaut" is the story most often written: a figure at a window, Earth small and blue, a realization about connection, a hopeful last image. That isn't a bug in any one model. It's what "likely" means. The result has three visible symptoms:

- **Convergent ideas.** Different models, and different runs of one model, land on the same premise. In this project's benchmark, baseline outputs from two unrelated model families had a mean embedding similarity of 0.75 for the same task, and the coffee-roastery names from every arm and both models started with "Ember".
- **Stock material.** The same metaphors, words and structures recur: "tapestry", "a testament to", the benefit triad, the mirrored slogan, the closing moral.
- **Second-order defaults.** Told to "be creative", models reach for a second, smaller set of moves just as reliably: the object narrates, the story is a log or a letter, exact times are sprinkled in to look concrete, the piece ends on one short line. A naive anti-cliché instruction mostly swaps the first set for the second.

## What Bohemian does about it

Bohemian doesn't ask for strangeness. It asks the model to find the obvious answer, keep it in view as a reference point, and justify every departure with a fact of this brief.

### 1. Read the brief

Separate what is **fixed** (length, format, facts, required words, audience, point of view, voice) from what is **open**. Only open parts are available for divergence. If a draft or voice sample exists, record its voice markers: sentence length, register, vocabulary, humor, what it never does.

### 2. Name the default, by layer

| Layer | Question | Example (lonely astronaut) |
|---|---|---|
| Premise / angle | What would most people make this about? | Isolation far from Earth; a realization about connection |
| Shape | What structure, opening and ending? | Opens on the view; linear; ends on a hopeful image |
| Material | What images, examples, words? | The blue marble, silence, the vast dark, a photo of family |
| Voice | What register would a generic assistant use? | Earnest, lyrical third person |

Naming the default by layer lets a piece keep a default where the brief needs it (a press release keeps its shape) while moving others.

### 3. Diverge for a reason

Every direction must be:

- **anchored** in a specific fact of the brief, with a one-sentence reason;
- **anchored, not literal:** the fact is a launch point, and the leap can be large;
- **different in kind** from the other directions: if one sentence summarizes two directions, they are one;
- **not the famous opposite** ("dark instead of light" is the second most common answer).

Directions come from six technique families. The family matters more than the technique, because two techniques from one family produce the same kind of surprise:

| Family | What moves | Examples |
|---|---|---|
| premise | what it is about | assumption reversal, contradiction held, stakes relocation, genre transposition |
| material | what it is made of | specificity injection, source-domain transfer, the true odd fact |
| form | what shape it takes | borrowed vessel, constraint manipulation, structural displacement |
| subtraction | what is left out | remove the expected center, cut the explanation |
| lens | who sees it | displaced witness, inverted stake, wrong expert |
| chance | where the start comes from | an external seed (`seed.py`) |

Each technique in `references/techniques.md` comes with **how it goes cheap**. Perspective inversion decays into "the object narrates", and source-domain transfer decays into "life is like jazz". The benchmark showed why this matters: in v1, the first technique on the list (the displaced witness) appeared in 12 of 44 dev plans. The skill's escape had become its own default, so v2 says outright that the list order is not a ranking.

### 4. Choose

Pick what serves the user's purpose, then, among the directions that fit, the one with the strongest hook and the most life on the page. Not the strangest one, and not the most restrained one either.

### 5. Make it

Concrete over general, precise words over impressive ones, feeling shown through detail. Fixed parts kept, limits counted. Specific doesn't mean small or quiet: a fresh premise can be big, funny or lush. The piece has to be fully realized, because a sketch of a clever idea isn't the piece.

### 6. Critique, then refine once

| Test | Question |
|---|---|
| Swap | Could this be pasted into a different brief with small changes? |
| Default | Is the premise, shape or main image the one from step 2? Is there a reason? |
| Reason | Can each main choice be justified with a fact of the brief? |
| Tells | Do stock phrases or second-order moves remain? (`lint.py` gives a first pass) |
| Payoff | Does it deliver what the form is for (pull, desire, memorability, an image that lands) as fully as the default would? |
| Brief | Exact length, format, audience and voice? Would the user actually use it? |

One refinement pass, for real problems only. Over-polishing drifts back toward the average.

## Intensity

Intensity is defined by **what may move**, not by how odd the result is:

| | mild | bold (default) | wild |
|---|---|---|---|
| may move | material, wording | + premise, angle, shape | anything the brief does not fix |
| directions weighed | 2 | 3 | 4, one high-risk |
| guardrail | the author recognizes their piece | the novelty never reads as a trick | strange allowed, arbitrary not; still readable and on-brief |

## Voice

There is no Bohemian house style. A minimalist stays minimal. A brand stays usable by that brand. Originality is supposed to come from choices (what to notice, where to start, what to leave out, what to compare it to), not from ornament. The benchmark exposed this risk in v1, which had drifted into a house style of understated literary minimalism ("smart but internally literary", one judge wrote). v3 responded by stating that restraint is a choice for particular briefs.

## Modes

| Mode | Output contract |
|---|---|
| create | one piece, in the asked length and format, no options or notes |
| brainstorm | N directions from at least three families, each with a "Why here:" line, clones replaced, one recommendation |
| rewrite | the author's voice and every fact kept; mild changes material only, bold may change angle or shape, wild may change form; placeholders instead of invented facts |
| critique | what works, the default it leans on, numbered findings (quote, why it is predictable *for this purpose*, a direction tied to the piece), the biggest opportunity |
| compare | 2–3 directions from different families, developed far enough to judge, then one pick with a reason |

When no mode is named, it is inferred: a draft to improve means rewrite, a request for ideas means brainstorm, a request for feedback means critique.

## Anti-repetition

Any move that works becomes the next default. Bohemian tracks moves by family:

- **Persistent:** `moves.py` logs `[family] move` to `~/.local/state/bohemian/history.jsonl`, shows counts and the least-used families, and warns after two moves in a row from the same family. `seed.py` avoids values used in the last ten seeds.
- **Session-only fallback:** without scripts, the model is told not to reuse an earlier piece's main move in the same conversation without a reason.

Limits: nothing forces the model to log. The log mixes all projects on a machine. Neither kind of memory knows what other users got, which is why seeds come from system randomness.

## What this methodology does not do

- It cannot verify facts. It is told not to invent facts that could pass as real.
- It does not know what is fresh *to a particular reader*: a move that is new to the model's average may be familiar in a niche.
- Its gains over a strong one-line instruction are unproven (see [`benchmark-results.md`](benchmark-results.md)).
