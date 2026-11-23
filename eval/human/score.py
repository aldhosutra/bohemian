#!/usr/bin/env python3
"""Score human answers against the hidden key.

  python3 eval/human/score.py answers-R1.json answers-R2.json ...

Reports, per question: treatment preference rate (ties count half), W/T/L, an exact sign test,
and Fleiss' kappa across reviewers on pairs that every reviewer answered.
"""
import collections
import json
import math
import sys
from pathlib import Path

QS = ["original", "unpredictable", "distinctive", "prefer", "task"]


def fleiss(table):
    n_items = len(table)
    if n_items == 0:
        return float("nan")
    n = sum(table[0].values())
    cats = {c for row in table for c in row}
    p_j = {c: sum(row.get(c, 0) for row in table) / (n_items * n) for c in cats}
    P_i = [(sum(v * v for v in row.values()) - n) / (n * (n - 1)) for row in table]
    P_bar, P_e = sum(P_i) / n_items, sum(p * p for p in p_j.values())
    return (P_bar - P_e) / (1 - P_e) if P_e < 1 else float("nan")


def main(paths):
    key = json.loads((Path(__file__).resolve().parent / "key.json").read_text(encoding="utf-8"))
    raters = [json.loads(Path(p).read_text(encoding="utf-8")) for p in paths]
    print(f"{len(raters)} reviewer(s); {len(key)} pairs in key")
    for q in QS:
        votes = collections.defaultdict(list)
        for r in raters:
            for pid, a in r["answers"].items():
                if q in a and pid in key:
                    v = a[q]
                    votes[pid].append("tie" if v == "tie" else ("treat" if v == key[pid]["treat_side"] else "ref"))
        flat = [v for vs in votes.values() for v in vs]
        c = collections.Counter(flat)
        rate = (c["treat"] + c["tie"] / 2) / max(1, len(flat))
        n = c["treat"] + c["ref"]
        k = min(c["treat"], c["ref"])
        p = min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n) if n else 1.0
        full = [collections.Counter(vs) for vs in votes.values() if len(vs) == len(raters)]
        kap = fleiss(full) if len(raters) > 1 else float("nan")
        print(f"{q:14s} treatment rate {100*rate:5.1f}%  W/T/L {c['treat']}/{c['tie']}/{c['ref']}  sign p={p:.3g}  Fleiss kappa={kap:.2f}")


if __name__ == "__main__":
    main(sys.argv[1:])
