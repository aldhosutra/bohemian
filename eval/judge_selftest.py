#!/usr/bin/env python3
"""Validate the judges before trusting them.

Each case has three hand-written responses to one brief:
  generic     - the cliched default
  distinctive - specific, unexpected, on-brief
  offtask     - novel and strange, but ignores the brief (random weirdness)

A judge passes a case when, in BOTH A/B orders:
  pairwise: distinctive beats generic on `original`, and offtask loses to generic on `task`
            and to distinctive on `prefer`;
  absolute: distinctive scores higher than generic on originality, and offtask scores lower
            than distinctive on task_alignment.
This checks that the judge rewards originality and does not reward mere distance from the default.

  python3 eval/judge_selftest.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge import JUDGES, absolute, pairwise  # noqa: E402

CASES = [
    {
        "prompt": "Create a memorable name for a Mac cleaning application. Give 5 options, one per line, nothing else.",
        "generic": "CleanMyMac Pro\nMacSweep\nSwiftClean\nPureMac\nTidyMac",
        "distinctive": "Lint Trap\nAttic Hours\nLast Tuesday\nDustjacket\nWhat Stayed",
        "offtask": "Velvet Thunder Goat\nNebula Spoon\nQuantum Pickle Empire\nGrandma's Jetpack\nSeventeen Moons Laughing",
    },
    {
        "prompt": "Write a poem about the ocean.",
        "generic": "The ocean waves crash on the shore,\nA symphony forever more.\nThe endless sea of azure blue\nWhispers secrets old and new.\nIts vast expanse, its timeless song,\nReminds us where we all belong.",
        "distinctive": "My uncle sold the boat in March\nbut kept the tide table on the fridge,\nand every morning, coffee in hand,\nhe reads me when the water is leaving,\nas if I'd asked,\nas if it were news from a town\nwhere he still owes someone money.",
        "offtask": "Accountants of the violet staircase\nmarch through my telephone,\nseventeen pianos dissolve in a teaspoon,\nthe moon files its taxes in Portuguese,\nand my left shoe remembers Tuesday.",
    },
    {
        "prompt": "Write an advertisement for an ordinary household object.",
        "generic": "Say goodbye to messy kitchens! Introducing the SuperSponge, the game-changer your home deserves. Absorbent, durable and easy to use, it makes cleaning effortless. Experience the difference today!",
        "distinctive": "The wooden spoon has no settings. It doesn't need charging, it has never once asked for your email, and the burn mark on the handle is from the night you learned to make caramel. Fourteen dollars. It will outlive the pan.",
        "offtask": "Behold the cathedral of whispering pineapples, where time itself wears slippers made of thunder. Purple is a feeling. The owls have voted. Join the migration of forgotten umbrellas tonight.",
    },
]


def run_case(judge, case):
    task = {"prompt": case["prompt"]}
    fails = []
    for order in (0, 1):
        def pw(x_name, y_name):
            a, b = (x_name, y_name) if order == 0 else (y_name, x_name)
            r = pairwise(judge, task, case[a], case[b])
            if r is None:
                return None
            return {q: ("tie" if v == "tie" else (a if v == "A" else b)) for q, v in r.items() if q != "why"}
        r1 = pw("distinctive", "generic")
        r2 = pw("generic", "offtask")
        r3 = pw("distinctive", "offtask")
        if not r1 or r1["original"] != "distinctive":
            fails.append(f"order{order}: distinctive did not win original vs generic ({r1 and r1['original']})")
        if not r2 or r2["task"] != "generic":
            fails.append(f"order{order}: offtask was not beaten by generic on task ({r2 and r2['task']})")
        if not r3 or r3["prefer"] != "distinctive":
            fails.append(f"order{order}: offtask was not beaten by distinctive on prefer ({r3 and r3['prefer']})")
    s = {k: absolute(judge, task, case[k]) for k in ("generic", "distinctive", "offtask")}
    if not all(s.values()):
        fails.append("absolute: unparseable")
    else:
        if not s["distinctive"]["originality"] > s["generic"]["originality"]:
            fails.append(f"absolute: originality distinctive {s['distinctive']['originality']} <= generic {s['generic']['originality']}")
        if not s["offtask"]["task_alignment"] < s["distinctive"]["task_alignment"]:
            fails.append(f"absolute: task_alignment offtask {s['offtask']['task_alignment']} >= distinctive {s['distinctive']['task_alignment']}")
    return fails, s


def main():
    ok_all = True
    report = {}
    for judge in JUDGES:
        report[judge] = []
        for i, case in enumerate(CASES):
            fails, scores = run_case(judge, case)
            report[judge].append({"case": i, "fails": fails, "absolute": scores})
            status = "PASS" if not fails else "FAIL"
            ok_all &= not fails
            print(f"{judge} case {i}: {status}")
            for f in fails:
                print("   ", f)
    out = Path(__file__).resolve().parent / "results" / "judge_selftest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1), encoding="utf-8")
    print("ALL JUDGES PASS" if ok_all else "SOME CHECKS FAILED: see results/judge_selftest.json")
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
