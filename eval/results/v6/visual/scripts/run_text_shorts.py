import json, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "eval")
from generate import skill_prompt, BASELINE, WRAPPER, MODELS, extract, ANTIALGORITHM
from lib.llm import chat, spent
ROOT = Path(".")
arms = {"baseline": BASELINE,
        "antialgorithm": skill_prompt(ANTIALGORITHM),
        "bohemian_v4b": skill_prompt(ROOT/"eval/results/v4/skill_snapshot_v4b"),
        "bohemian_v5": skill_prompt(ROOT/"skills/bohemian")}
briefs = {
 "finance": "Write the hook and full script for a 45-second YouTube Short for a personal-finance channel, about why everyone needs an emergency fund. Include on-screen text cues.",
 "rice": "Write the opening hook (first 3 seconds) and a 30-second voiceover script for a YouTube Short in which a home cook shows how to make fluffy rice.",
}
jobs = [(b, m, a, s) for b in briefs for m in MODELS for a in arms for s in range(2)]
print(len(jobs), "calls; spent", round(spent(), 4))
def work(j):
    b, m, a, s = j
    raw, u = chat(m, arms[a], briefs[b] + WRAPPER, temperature=1.0, max_tokens=4000, seed_index=s, tag=f"demo:shorts:{a}")
    final, ok = extract(raw)
    return {"brief": b, "prompt": briefs[b], "model": m, "arm": a, "sample": s, "final": final, "raw": raw, "wrapped": ok}
with ThreadPoolExecutor(8) as ex:
    rows = list(ex.map(work, jobs))
Path(sys.argv[1]).write_text(json.dumps(rows, ensure_ascii=False, indent=1))
print("done; spent", round(spent(), 4))
