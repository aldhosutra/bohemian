#!/usr/bin/env python3
"""Build a blind pairwise review page for human raters.

Writes two files:
  review.html  self-contained page: brief + Response A + Response B, five questions per pair.
               Nothing in it says which arm wrote which response.
  key.json     which side is the treatment for each pair id. Keep it away from reviewers.

  python3 eval/human/build.py --run v2 --treat bohemian --ref baseline --pairs 40 --seed 7
"""
import argparse
import html
import json
import random
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
QUESTIONS = [
    ("original", "Which response is more original?"),
    ("unpredictable", "Which response is less predictable?"),
    ("distinctive", "Which response is more distinctive (has a character of its own rather than generic AI writing)?"),
    ("prefer", "Which response would you actually prefer to use?"),
    ("task", "Which response better satisfies the brief?"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--treat", default="bohemian")
    ap.add_argument("--ref", default="baseline")
    ap.add_argument("--pairs", type=int, default=40)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--split", default="test")
    args = ap.parse_args()
    rng = random.Random(args.seed)
    tasks = {json.loads(l)["id"]: json.loads(l) for l in (EVAL / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    gens = [json.loads(l) for l in (EVAL / "results" / args.run / "generations.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    by = {(g["task_id"], g["model"], g["arm"], g["sample"]): g["final"] for g in gens}
    cands = [(t, m, s) for (t, m, a, s) in by if a == args.treat and (t, m, args.ref, s) in by
             and (args.split == "all" or tasks[t]["split"] == args.split)]
    rng.shuffle(cands)
    seen, chosen = set(), []
    for t, m, s in cands:
        if t not in seen:
            chosen.append((t, m, s))
            seen.add(t)
        if len(chosen) == args.pairs:
            break
    items, key = [], {}
    for i, (t, m, s) in enumerate(chosen):
        pid = f"p{i:03d}"
        treat_a = rng.random() < 0.5
        a, b = (by[(t, m, args.treat, s)], by[(t, m, args.ref, s)]) if treat_a else (by[(t, m, args.ref, s)], by[(t, m, args.treat, s)])
        items.append({"id": pid, "brief": tasks[t]["prompt"], "a": a, "b": b})
        key[pid] = {"task_id": t, "model": m, "sample": s, "treat_side": "A" if treat_a else "B", "treat": args.treat, "ref": args.ref}
    out = Path(__file__).resolve().parent
    (out / "key.json").write_text(json.dumps(key, indent=1), encoding="utf-8")
    page = TEMPLATE.replace("__ITEMS__", json.dumps(items).replace("</", "<\\/")).replace("__QUESTIONS__", json.dumps(QUESTIONS))
    (out / "review.html").write_text(page, encoding="utf-8")
    print(f"wrote {out/'review.html'} ({len(items)} pairs) and key.json (do not share the key with reviewers)")


TEMPLATE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Blind writing review</title>
<style>
:root{color-scheme:light dark;--bg:#fafaf7;--fg:#1d1d1b;--mut:#6b6b66;--line:#d9d8d2;--card:#fff;--acc:#2f5d50}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#ecebe6;--mut:#9a9992;--line:#34342f;--card:#1f1f1d;--acc:#8cc2b0}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px}
.brief{font-weight:600;margin:8px 0 16px;white-space:pre-wrap}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media(max-width:800px){.cols{grid-template-columns:1fr}}
.resp{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px;white-space:pre-wrap;max-height:60vh;overflow:auto}
.resp h3{margin:0 0 8px;font-size:14px;color:var(--mut)}
fieldset{border:0;padding:0;margin:14px 0}legend{font-weight:600;margin-bottom:6px}
label{margin-right:18px;cursor:pointer}button{font:inherit;padding:8px 16px;border-radius:6px;border:1px solid var(--line);background:var(--card);color:var(--fg);cursor:pointer}
button.primary{background:var(--acc);color:var(--bg);border-color:var(--acc)}.bar{display:flex;gap:10px;align-items:center;margin-top:16px;flex-wrap:wrap}
.mut{color:var(--mut)}input[type=text]{font:inherit;padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg)}
</style></head><body><main>
<h1>Blind writing review</h1>
<p class="mut">Each page shows one brief and two responses. They were produced in different ways; you are not told how. Read both, then answer each question. Answers save in this browser. When you finish, download your answers and send the file back.</p>
<p>Your reviewer name or initials: <input type="text" id="rater" placeholder="e.g. R1"></p>
<div id="app"></div>
<div class="bar"><button id="prev">Previous</button><button id="next" class="primary">Next</button><span id="pos" class="mut"></span><button id="dl">Download answers</button></div>
</main><script>
const ITEMS=__ITEMS__;const QS=__QUESTIONS__;const KEY="blind-review-v1";
let st=JSON.parse(localStorage.getItem(KEY)||'{"i":0,"ans":{},"rater":""}');
const app=document.getElementById('app'),rater=document.getElementById('rater');rater.value=st.rater||'';
rater.oninput=()=>{st.rater=rater.value;save()};
function save(){localStorage.setItem(KEY,JSON.stringify(st))}
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
function render(){const it=ITEMS[st.i];const a=st.ans[it.id]||{};
app.innerHTML=`<div class="brief">Brief: ${esc(it.brief)}</div><div class="cols"><div class="resp"><h3>Response A</h3>${esc(it.a)}</div><div class="resp"><h3>Response B</h3>${esc(it.b)}</div></div>`+
QS.map(([k,q])=>`<fieldset><legend>${q}</legend>${["A","B","tie"].map(v=>`<label><input type="radio" name="${k}" value="${v}" ${a[k]===v?'checked':''}> ${v==='tie'?'Cannot choose':v}</label>`).join('')}</fieldset>`).join('');
app.querySelectorAll('input[type=radio]').forEach(r=>r.onchange=()=>{st.ans[it.id]=Object.assign(st.ans[it.id]||{},{[r.name]:r.value});save();upd()});upd()}
function upd(){const done=Object.values(st.ans).filter(a=>QS.every(([k])=>a[k])).length;document.getElementById('pos').textContent=`Pair ${st.i+1} of ${ITEMS.length} · ${done} complete`}
document.getElementById('prev').onclick=()=>{if(st.i>0){st.i--;save();render();scrollTo(0,0)}};
document.getElementById('next').onclick=()=>{if(st.i<ITEMS.length-1){st.i++;save();render();scrollTo(0,0)}};
document.getElementById('dl').onclick=()=>{const b=new Blob([JSON.stringify({rater:st.rater,answers:st.ans},null,1)],{type:'application/json'});const u=URL.createObjectURL(b);const l=document.createElement('a');l.href=u;l.download=`answers-${st.rater||'anon'}.json`;l.click()};
render();
</script></body></html>"""

if __name__ == "__main__":
    main()
