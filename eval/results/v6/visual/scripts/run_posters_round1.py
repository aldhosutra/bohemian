import json, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "eval")
from generate import skill_prompt, BASELINE, WRAPPER, MODELS, extract, ANTIALGORITHM
from lib.llm import chat, spent
S = Path(sys.argv[1])
anti = skill_prompt(ANTIALGORITHM) + "\n\n=== visuals.md ===\n" + (S/"upstream/visuals.md").read_text()
arms = {"baseline": BASELINE, "antialgorithm": anti,
        "bohemian_v4b": skill_prompt(Path("eval/results/v4/skill_snapshot_v4b")),
        "bohemian_v5": skill_prompt(Path("skills/bohemian"))}
FMT = " Deliver it as one self-contained SVG with viewBox=\"0 0 600 900\": no external images, fonts or links (use font-family stacks the viewer's system will have)."
briefs = {
 "library": "Design a poster for Friday Late Nights at Eastgate Public Library: the library stays open every Friday from 7 pm to midnight, free, all ages." + FMT,
 "jazz": "Design a poster for a jazz concert: Trio Nadir, live at The Cellar, Saturday 14 March, 9 pm, tickets $15." + FMT,
}
jobs = [(b, m, a, s) for b in briefs for m in MODELS for a in arms for s in range(2)]
print(len(jobs), "calls; spent", round(spent(), 4))
def work(j):
    b, m, a, s = j
    raw, u = chat(m, arms[a], briefs[b] + WRAPPER, temperature=1.0, max_tokens=12000, seed_index=s, tag=f"demo:poster:{a}")
    final, ok = extract(raw)
    mm = re.search(r"<svg.*</svg>", final, re.S | re.I)
    return {"brief": b, "prompt": briefs[b], "model": m, "arm": a, "sample": s, "svg": mm.group(0) if mm else "", "raw": raw, "wrapped": ok, "out_tokens": u.get("completion_tokens")}
with ThreadPoolExecutor(8) as ex:
    rows = list(ex.map(work, jobs))
(S/"out.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))
print("missing svg:", sum(1 for r in rows if not r["svg"]), "; spent", round(spent(), 4))
