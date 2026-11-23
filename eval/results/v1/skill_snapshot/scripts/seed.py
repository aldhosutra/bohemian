#!/usr/bin/env python3
import argparse
import random
import sys

import state

rng = random.SystemRandom()

POOLS = {
    "text": {
        "lens": [
            "the person who cleans up afterwards", "someone who arrived too late", "a child who misread it",
            "the one who was against it", "someone doing it for the hundredth time", "a stranger overhearing",
            "the person who pays for it", "someone who used to believe in it", "a beginner on day one",
            "the person it was built to replace", "someone keeping it secret", "a translator between two sides",
        ],
        "entry": [
            "a sound", "a mistake", "a rule someone breaks", "the ending", "a smell", "an object that is missing",
            "a complaint", "a habit", "a misunderstanding", "a bill or receipt", "a body feeling", "a promise",
            "something being repaired", "a question nobody answers", "a joke that falls flat",
        ],
        "shape": [
            "one long sentence", "short sections with gaps between", "a conversation", "instructions",
            "a sequence told backwards", "two voices alternating", "a single scene in real time",
            "a list that turns into a story", "a plain report", "a letter that is never sent",
        ],
        "register": ["plain", "dry", "warm", "blunt", "careful", "playful", "nervous", "formal", "tender", "impatient"],
    },
    "idea": {
        "verb": [
            "repair", "borrow", "queue", "share", "sort", "measure", "return", "wait", "swap", "trust", "forget",
            "translate", "inherit", "rent", "split", "pack", "hide", "teach", "deliver", "inspect",
        ],
        "constraint": [
            "it must work offline", "the user cannot read well", "it only works in one building",
            "it costs nothing to the end user", "it is used once a year", "two people must agree",
            "it must be done in under a minute", "the user is not the buyer", "it has to work in silence",
            "nobody may know they use it", "it gets better with more strangers", "it must survive bad weather",
        ],
        "who": [
            "night-shift workers", "people caring for a parent", "small landlords", "teenagers with a first job",
            "rural clinics", "people who just moved country", "retired tradespeople", "school janitors",
            "long-haul drivers", "people with a chronic illness", "volunteer organizers", "street vendors",
        ],
        "pressure": ["a deadline", "a debt", "a rumor", "a rule that changes", "noise", "fatigue",
                     "a rival", "running out of space", "a guest who will not leave", "weather"],
    },
    "name": {
        "source": [
            "a verb from a trade", "a sound the product makes or prevents", "a place where the problem shows up",
            "an old unit of measure", "a gesture people make", "a word from the user's own complaint",
            "a tool from a different craft", "a household phrase", "a misheard word", "a person's job title",
        ],
        "form": [
            "one plain real word", "two words with a gap", "a short phrase", "a verb in the imperative",
            "a nickname", "a word with one letter changed", "a number with meaning", "a word from another language the users speak",
        ],
        "feel": ["dry", "friendly", "serious", "small", "strange but sayable", "old", "physical", "quiet"],
    },
}

ANCHORS = [
    "ladder", "glove", "bread", "hinge", "fog", "thread", "lamp", "sponge", "ice", "radio", "key", "brick",
    "coin", "button", "wire", "bell", "window", "kite", "honey", "nail", "tent", "elevator", "umbrella",
    "cassette", "spoon", "lock", "stairs", "battery", "laundry", "ticket", "alarm clock", "cable", "knot",
    "pump", "tire", "zip", "comb", "chair", "puddle", "rice", "bus", "receipt", "parking meter", "kettle",
    "bucket", "doorbell", "lanyard", "staple", "lunchbox", "headlamp", "measuring tape", "spare key",
]


def recent(n=10):
    seen = {}
    for row in reversed(state.load("seed")[-n:]):
        for axis, value in row.get("seed", {}).items():
            seen.setdefault(axis, set()).add(value)
    return seen


def pick(axis, items, avoid):
    fresh = [i for i in items if i not in avoid.get(axis, set())]
    return rng.choice(fresh or items)


def roll(kind, keep, avoid):
    out = {axis: pick(axis, items, avoid) for axis, items in POOLS[kind].items()}
    out["anchor"] = pick("anchor", ANCHORS, avoid)
    out.update(keep)
    return out


def main():
    ap = argparse.ArgumentParser(description="Roll a creative starting point that does not come from the model's own taste.")
    ap.add_argument("kind", nargs="?", default="text", choices=sorted(POOLS))
    ap.add_argument("--keep", action="append", default=[], help='hold an axis fixed, e.g. --keep "register=dry"')
    ap.add_argument("--no-log", action="store_true", help="do not save this seed to history")
    args = ap.parse_args()
    keep = {}
    for item in args.keep:
        k, sep, v = item.partition("=")
        if not sep:
            sys.exit(f"--keep needs axis=value, got '{item}'")
        keep[k.strip()] = v.strip()
    seed = roll(args.kind, keep, recent())
    for k, v in seed.items():
        print(f"{k}: {v}")
    print("Tie each axis to the subject with a reason, or drop it. A seed pasted on top of a default piece is still a default piece.")
    if not args.no_log:
        state.add({"type": "seed", "kind": args.kind, "seed": seed})


if __name__ == "__main__":
    main()
