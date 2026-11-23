import json, sys
from collections import defaultdict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
S = Path(sys.argv[1]); sys.path.insert(0, str(S))
from vjudge import judge
from overflow import overflow_px
from lib.llm import spent
rows = json.loads((S/"v6/out.json").read_text())
for r in rows: r["overflow"] = overflow_px(r["svg"]) if r["svg"] else None
JUDGE = "google/gemini-3.1-flash-lite"
walls = sorted({(r["brief"], r["model"]) for r in rows})
jobs = [(b, m, seed) for b, m in walls for seed in range(3)]
def work(x):
    b, m, seed = x
    items = [(f"{r['arm']}:{r['sample']}", r["svg"]) for r in rows if r["brief"] == b and r["model"] == m and r["svg"]]
    ranked, raw = judge(JUDGE, next(r["prompt"] for r in rows if r["brief"] == b), items, 100 + seed)
    return {"brief": b, "model": m, "seed": seed, "ranked": ranked, "raw": raw}
with ThreadPoolExecutor(8) as ex: res = list(ex.map(work, jobs))
(S/"v6/judged.json").write_text(json.dumps({"rows": [{k: v for k, v in r.items() if k != "raw"} for r in rows], "judge": res}, indent=1))
arms = ["baseline", "antialgorithm", "bohemian_v4b", "bohemian_v6"]
top1 = defaultdict(int); borda = defaultdict(int); per_model = defaultdict(lambda: defaultdict(int))
for r in res:
    for i, id_ in enumerate(r["ranked"]):
        a = id_.split(":")[0]; borda[a] += 3 - i; per_model[r["model"]][a] += 3 - i
        if i == 0: top1[a] += 1
n = len(res)
print(f"vision judge {JUDGE}, {n} walls x shuffles; chance top1 = {n/4:.1f} per arm")
print(f"{'arm':16} top1  borda  overflow(>50px)  " + "  ".join(m.split('/')[1][:8] for m in sorted(per_model)))
for a in arms:
    ov = [r["overflow"] for r in rows if r["arm"] == a and r["overflow"] is not None]
    print(f"{a:16} {top1[a]:4}  {borda[a]:5}  {sum(o > 50 for o in ov):2}/{len(ov)}            " + "  ".join(f"{per_model[m][a]:8}" for m in sorted(per_model)))
print("spent", round(spent(), 4))
