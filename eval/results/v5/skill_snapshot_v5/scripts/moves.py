#!/usr/bin/env python3
import argparse
import collections
import json
import os
import sys

import state

FAMILIES = ["lens", "material", "form", "premise", "subtraction", "chance"]


def show(last):
    rows = state.load("move")[-last:]
    if not rows:
        print("No moves recorded yet. Any family is fine.")
        return
    counts = collections.Counter(r.get("family", "?") for r in rows)
    print(f"Last {len(rows)} moves (newest last):")
    for r in rows:
        print(f"  [{r.get('family', '?')}] {r.get('move', '')}")
    print("Family use: " + ", ".join(f"{f}={counts.get(f, 0)}" for f in FAMILIES))
    least = min(counts.get(f, 0) for f in FAMILIES if f != "chance")
    fresh = [f for f in FAMILIES if f != "chance" and counts.get(f, 0) == least]
    print("Least used: " + ", ".join(fresh))
    last_family = rows[-1].get("family")
    streak = 0
    for r in reversed(rows):
        if r.get("family") != last_family:
            break
        streak += 1
    if streak >= 2:
        print(f"Warning: the last {streak} moves were all '{last_family}'. Pick another family unless this brief needs it.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Log of the main creative move behind each piece, so the escape does not become a habit.")
    ap.add_argument("action", nargs="?", default="show", choices=["show", "add", "clear"])
    ap.add_argument("family", nargs="?", help="technique family: " + ", ".join(FAMILIES))
    ap.add_argument("move", nargs="*", help="the move in a few plain words, never the user's content")
    ap.add_argument("--last", type=int, default=12)
    args = ap.parse_args()
    if args.action == "show":
        show(args.last)
    elif args.action == "add":
        if args.family not in FAMILIES:
            sys.exit(f"family must be one of: {', '.join(FAMILIES)}")
        text = " ".join(args.move).strip()
        if not text:
            sys.exit('add needs a move, e.g. moves.py add lens "story told by the person who cleans up"')
        state.add({"type": "move", "family": args.family, "move": text})
        print(f"saved [{args.family}] {text}")
    else:
        kept = [r for r in state.load() if r.get("type") != "move"]
        path = state.history_path()
        if os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                for r in kept:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("move log cleared")


if __name__ == "__main__":
    main()
