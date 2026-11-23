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
        "bohemian_v6": skill_prompt(Path("eval/results/v6/skill_snapshot_v6"))}
FMT = " Deliver it as one self-contained SVG with viewBox=\"0 0 600 900\": no external images, fonts or links (use font-family stacks the viewer's system will have)."
briefs = {
 "market": "Design a poster for a farmers' market that runs every Sunday, 8 am to 1 pm, in the Lot 4 car park on Mill Road.",
 "cat": "Design a lost-cat poster: Biscuit, a grey tabby, missing since Tuesday from Alder Street. Call 555-0142.",
 "bees": "Design a poster for a science museum's new exhibition about bees, called The Hive Mind, opening 3 May.",
 "run": "Design a poster for a 10 km charity fun run along the river, Sunday 8 June, registration $20, all proceeds to the city food bank.",
 "choir": "Design a poster recruiting singers for a community choir: no auditions, Tuesdays at 7 pm, St Brendan's Hall.",
 "horror": "Design a cinema poster for a horror film called The Quiet Floor, in cinemas this October.",
}
jobs = [(b, m, a, s) for b in briefs for m in MODELS for a in arms for s in range(2)]
print(len(jobs), "calls; spent", round(spent(), 4))
def work(j):
    b, m, a, s = j
    for retry in range(3):
        raw, u = chat(m, arms[a], briefs[b] + FMT + WRAPPER, temperature=1.0, max_tokens=12000, seed_index=s + 1000 * retry, tag=f"demo:poster6:{a}")
        final, ok = extract(raw); mm = re.search(r"<svg.*</svg>", final, re.S | re.I)
        if mm: break
    return {"brief": b, "prompt": briefs[b], "model": m, "arm": a, "sample": s, "svg": mm.group(0) if mm else "", "wrapped": ok, "retries": retry, "out_tokens": u.get("completion_tokens"), "raw": raw}
with ThreadPoolExecutor(8) as ex: rows = list(ex.map(work, jobs))
(S/"v6/out.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))
print("missing svg:", sum(1 for r in rows if not r["svg"]), "; spent", round(spent(), 4))
