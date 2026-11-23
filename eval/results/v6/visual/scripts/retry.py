import json, sys, re
from pathlib import Path
sys.path.insert(0, "eval")
from generate import skill_prompt, WRAPPER, extract, ANTIALGORITHM
from lib.llm import chat, spent
S = Path(sys.argv[1]); rows = json.loads((S/"out.json").read_text())
anti = skill_prompt(ANTIALGORITHM) + "\n\n=== visuals.md ===\n" + (S/"upstream/visuals.md").read_text()
for r in rows:
    if r["svg"]: continue
    print("first try tail:", repr(r["raw"][-200:]), "len", len(r["raw"]))
    raw, u = chat(r["model"], anti, r["prompt"] + WRAPPER, temperature=1.0, max_tokens=12000, seed_index=r["sample"] + 1000, tag="demo:poster:antialgorithm")
    final, ok = extract(raw); m = re.search(r"<svg.*</svg>", final, re.S | re.I)
    r.update(svg=m.group(0) if m else "", raw=raw, wrapped=ok, out_tokens=u.get("completion_tokens"), retries=1)
    print("retry ok:", bool(r["svg"]), u.get("completion_tokens"))
(S/"out.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1)); print("spent", round(spent(),4))
