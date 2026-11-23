import json, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "eval")
from generate import skill_prompt, WRAPPER, MODELS, extract, ANTIALGORITHM
from lib.llm import chat, spent
S = Path(sys.argv[1]); topics = sys.argv[2].split(",")
anti = skill_prompt(ANTIALGORITHM) + "\n\n=== visuals.md ===\n" + (S/"posters/upstream/visuals.md").read_text()
arms = {"antialgorithm": anti, "bohemian_v4b": skill_prompt(Path("eval/results/v4/skill_snapshot_v4b"))}
FMT = (" Deliver the finished Short as one self-contained HTML file that plays it: a 9:16 frame (fit it to the window), "
       "30 seconds, starts on its own and loops, animated with CSS and/or JavaScript. Most viewers watch muted, so put "
       "every spoken line on screen as captions. No external files, fonts, images, audio or network requests.")
BRIEFS = {
 "onion": "Make a 30-second YouTube Short for an everyday-science channel: why cutting onions makes you cry. The goal is virality: people should watch to the end, rewatch and share it.",
 "sleep": "Make a 30-second YouTube Short for a productivity channel about the 90-second rule for falling back asleep. The goal is virality: people should watch to the end, rewatch and share it.",
}
jobs = [(t, m, a, s) for t in topics for m in MODELS for a in arms for s in range(2)]
print(len(jobs), "calls; spent", round(spent(), 4))
def work(j):
    t, m, a, s = j
    for retry in range(2):
        raw, u = chat(m, arms[a], BRIEFS[t] + FMT + WRAPPER, temperature=1.0, max_tokens=12000, seed_index=s + 1000 * retry, tag=f"demo:short:{a}")
        final, ok = extract(raw); mm = re.search(r"<!doctype html.*</html>|<html.*</html>", final, re.S | re.I)
        if mm: break
    return {"topic": t, "brief": BRIEFS[t], "model": m, "arm": a, "sample": s, "html": mm.group(0) if mm else "", "out_tokens": u.get("completion_tokens"), "cost": u.get("cost")}
with ThreadPoolExecutor(8) as ex: rows = list(ex.map(work, jobs))
out = S/"viral/out.json"; old = json.loads(out.read_text()) if out.exists() else []
out.write_text(json.dumps(old + rows, ensure_ascii=False, indent=1))
print("missing html:", sum(1 for r in rows if not r["html"]), "; tokens", [r["out_tokens"] for r in rows], "; spent", round(spent(), 4))
