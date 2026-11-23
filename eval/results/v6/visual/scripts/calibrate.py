import json, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, sys.argv[1]); from vjudge import judge
from lib.llm import spent
S = Path(sys.argv[1]); rows = json.loads((S/"out.json").read_text())
USER = {("library","anthropic/claude-haiku-5.5"): "antialgorithm:1", ("library","deepseek/deepseek-v4.1-flash"): "bohemian_v4b:0",
        ("jazz","anthropic/claude-haiku-5.5"): "bohemian_v4b:1", ("jazz","deepseek/deepseek-v4.1-flash"): "bohemian_v5:0"}
JUDGES = sys.argv[2].split(",")
jobs = []
for (b, m), pick in USER.items():
    items = [(f"{r['arm']}:{r['sample']}", r["svg"]) for r in rows if r["brief"] == b and r["model"] == m]
    brief = next(r["prompt"] for r in rows if r["brief"] == b).split(" Deliver it as")[0]
    for j in JUDGES:
        for seed in range(3): jobs.append((b, m, pick, j, seed, brief, items))
def work(x):
    b, m, pick, j, seed, brief, items = x
    ranked, raw = judge(j, brief, items, seed)
    return {"wall": f"{b}/{m.split('/')[1]}", "user": pick, "judge": j, "seed": seed, "ranked": ranked, "raw": raw}
with ThreadPoolExecutor(8) as ex: res = list(ex.map(work, jobs))
(S/"calibration.json").write_text(json.dumps(res, indent=1))
for j in JUDGES:
    rs = [r for r in res if r["judge"] == j]
    top1 = sum(r["ranked"][:1] == [r["user"]] for r in rs); top3 = sum(r["user"] in r["ranked"] for r in rs)
    print(f"{j}: top1 {top1}/{len(rs)} (chance 1/8), in top3 {top3}/{len(rs)} (chance 3/8)")
    for r in rs: print("   ", r["wall"], "user", r["user"], "| judge", r["ranked"])
print("spent", round(spent(), 4))
