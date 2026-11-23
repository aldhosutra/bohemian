#!/usr/bin/env python3
"""Deterministic and embedding metrics (no judge involved).

Per output:
  words, constraint_pass, cliche rates (total / shared-with-skill / held-out),
  typicality      cosine similarity to the task's "obvious answer" anchor (lower = further from the default)
  intra_list_sim  for list tasks, mean pairwise cosine between the items in one output (lower = items differ in kind)
Per (task, model, arm), across the independent samples:
  semantic_diversity  1 - mean pairwise cosine between samples
  ngram_overlap       mean pairwise Jaccard of word 3-grams between samples (Self-BLEU-like; lower = less repetition)
Per (task, arm, sample), across the two generator models:
  cross_model_sim     cosine between the two models' outputs (lower = the models did not converge on the same answer)

Anchors: for each task, two judge-family models are asked for the most predictable, conventional response. Their
centroid is the "default" the typicality metric measures distance from. Anchors come from models that are NOT the
generators, so no arm is measured against its own outputs.

  python3 eval/metrics.py --run v1
"""
import argparse
import itertools
import json
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lexicon import rates  # noqa: E402
from lib.llm import chat, embed  # noqa: E402

EVAL = Path(__file__).resolve().parent
ANCHOR_MODELS = ["google/gemini-2.5-flash-lite", "openai/gpt-4o-mini"]
ANCHOR_SYSTEM = ("Write the most predictable, conventional response to the brief: the version most writers or assistants "
                 "would produce first, with the most common ideas, structure and phrasing. Do not parody it or exaggerate it; "
                 "make it a typical competent answer. Respond with the piece only.")


def words(text):
    return len(re.findall(r"\b[\w'-]+\b", text))


def items(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    numbered = [l for l in lines if re.match(r"^(\d+[.)]|[-*•])\s+", l)]
    return numbered if len(numbered) >= 2 else lines


def check(task, text):
    """Return (passed, details) for the task's deterministic constraints, or (None, {}) if unconstrained."""
    c = task.get("checks") or {}
    if not c:
        return None, {}
    res = {}
    w = words(text)
    lines = [l for l in text.splitlines() if l.strip()]
    if "max_words" in c:
        res["max_words"] = w <= c["max_words"]
    if "min_words" in c:
        res["min_words"] = w >= c["min_words"]
    if "max_lines" in c:
        res["max_lines"] = len(lines) <= c["max_lines"]
    if "n_lines" in c:
        res["n_lines"] = len(lines) == c["n_lines"]
    if "n_items" in c:
        res["n_items"] = len([l for l in lines if re.match(r"^\s*(\*\*)?\d+[.)]", l)]) == c["n_items"]
    if "paragraphs" in c:
        paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
        res["paragraphs"] = len(paras) == c["paragraphs"]
    if "forbid" in c:
        res["forbid"] = not any(re.search(rf"\b{re.escape(f)}\b", text, re.I) for f in c["forbid"])
    return all(res.values()), res


def cos(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


def ngrams(text, n=3):
    t = re.findall(r"\b[\w']+\b", text.lower())
    return {tuple(t[i:i + n]) for i in range(len(t) - n + 1)}


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def anchors(tasks):
    out = {}
    for t in tasks.values():
        texts = []
        for m in ANCHOR_MODELS:
            raw, _ = chat(m, ANCHOR_SYSTEM, t["prompt"], temperature=0.7, max_tokens=900, tag="anchor")
            texts.append(raw.strip())
        out[t["id"]] = texts
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = EVAL / "results" / args.run
    gens = [json.loads(l) for l in (run_dir / "generations.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    tasks = {json.loads(l)["id"]: json.loads(l) for l in (EVAL / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    gens = [g for g in gens if g["task_id"] in tasks]

    anc = anchors({k: v for k, v in tasks.items() if any(g["task_id"] == k for g in gens)})
    anc_ids = list(anc)
    anc_vecs = embed([x for tid in anc_ids for x in anc[tid]])
    centroid = {tid: np.mean(anc_vecs[2 * i: 2 * i + 2], axis=0) for i, tid in enumerate(anc_ids)}

    vecs = embed([g["final"] or " " for g in gens])
    list_tasks = {tid for tid, t in tasks.items() if {"n_lines", "n_items"} & set(t.get("checks", {}))}

    per_output = []
    for g, v in zip(gens, vecs):
        t = tasks[g["task_id"]]
        passed, detail = check(t, g["final"])
        r = rates(g["final"])
        row = {k: g[k] for k in ("task_id", "model", "arm", "sample")}
        row.update({
            "words": words(g["final"]), "wrapped": g["wrapped"], "constraint_pass": passed, "constraint_detail": detail,
            "cliche_per100": r["cliche_per100"], "cliche_shared_per100": r["cliche_shared_per100"],
            "cliche_heldout_per100": r["cliche_heldout_per100"], "cliche_hits": r["cliche_hits"],
            "typicality": cos(v, centroid[g["task_id"]]),
        })
        if g["task_id"] in list_tasks:
            its = items(g["final"])[:10]
            if len(its) >= 2:
                iv = embed(its, tag="embed:items")
                row["intra_list_sim"] = float(np.mean([cos(a, b) for a, b in itertools.combinations(iv, 2)]))
        per_output.append(row)

    vec_of = {(g["task_id"], g["model"], g["arm"], g["sample"]): v for g, v in zip(gens, vecs)}
    text_of = {(g["task_id"], g["model"], g["arm"], g["sample"]): g["final"] for g in gens}
    groups = {}
    for (tid, m, arm, s) in vec_of:
        groups.setdefault((tid, m, arm), []).append(s)
    per_group = []
    for (tid, m, arm), ss in groups.items():
        if len(ss) < 2:
            continue
        pairs = list(itertools.combinations(sorted(ss), 2))
        per_group.append({
            "task_id": tid, "model": m, "arm": arm,
            "semantic_diversity": 1 - float(np.mean([cos(vec_of[(tid, m, arm, a)], vec_of[(tid, m, arm, b)]) for a, b in pairs])),
            "ngram_overlap": float(np.mean([jaccard(ngrams(text_of[(tid, m, arm, a)]), ngrams(text_of[(tid, m, arm, b)])) for a, b in pairs])),
        })
    models = sorted({g["model"] for g in gens})
    cross = []
    if len(models) == 2:
        for (tid, m, arm, s), v in vec_of.items():
            if m == models[0] and (tid, models[1], arm, s) in vec_of:
                cross.append({"task_id": tid, "arm": arm, "sample": s, "cross_model_sim": cos(v, vec_of[(tid, models[1], arm, s)])})

    (run_dir / "metrics.json").write_text(json.dumps({"per_output": per_output, "per_group": per_group, "cross_model": cross,
                                                      "anchors": anc}, ensure_ascii=False), encoding="utf-8")
    print(f"metrics: {len(per_output)} outputs, {len(per_group)} groups, {len(cross)} cross-model pairs")


if __name__ == "__main__":
    main()
