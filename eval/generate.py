#!/usr/bin/env python3
"""Generate outputs for every (task, model, arm, sample).

Arms differ ONLY in the system prompt. Model, temperature, max_tokens, the user
message and the output wrapper are identical across arms.

  python3 eval/generate.py --run v1 [--split all|dev|test] [--arms baseline,oneliner,bohemian]
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.llm import BudgetExceeded, chat, spent  # noqa: E402

EVAL = Path(__file__).resolve().parent
ROOT = EVAL.parent
SKILL = ROOT / "skills" / "bohemian"
ANTIALGORITHM = EVAL / "competitors" / "antialgorithm"  # unmodified upstream SKILL.md, see SOURCE.md

MODELS = ["deepseek/deepseek-v4.1-flash", "anthropic/claude-haiku-5.5"]
TEMPERATURE = 1.0
MAX_TOKENS = 4000
SAMPLES = 3
RETRIES = 3

WRAPPER = ("\n\n(Format: you have no hidden thinking space here. First plan in brief notes. "
           "Then put the finished piece, exactly as you would hand it to me, between <final> and </final>. "
           "I will only see what is inside <final>.)")


BASELINE = "You are a helpful assistant."
ONELINER = "You are a helpful assistant. Be original: avoid cliches and look past the first, most obvious idea."


def skill_prompt(skill_dir=SKILL):
    """The skill as an agent would see it after reading SKILL.md and the references it points to.
    Scripts cannot run in a single API call, which the preamble states, matching the skill's own fallback."""
    parts = [
        "You are a helpful assistant with the following skill active for this request. "
        "You cannot run scripts in this environment; follow the skill's no-script fallbacks.",
        "=== SKILL.md ===\n" + (skill_dir / "SKILL.md").read_text(encoding="utf-8"),
    ]
    for ref in ["techniques.md", "cliches.md", "modes.md"]:
        if (skill_dir / "references" / ref).exists():
            parts.append(f"=== references/{ref} ===\n" + (skill_dir / "references" / ref).read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def arms(skill_dir=SKILL):
    return {"baseline": BASELINE, "oneliner": ONELINER, "bohemian": skill_prompt(skill_dir),
            "antialgorithm": skill_prompt(ANTIALGORITHM)}


def extract(raw):
    m = re.findall(r"<final>(.*?)</final>", raw, flags=re.S | re.I)
    if m:
        return m[-1].strip(), True
    m = re.search(r"<final>(.*)$", raw, flags=re.S | re.I)
    if m:
        return m.group(1).strip(), False
    return raw.strip(), False


def load_tasks(split="all"):
    tasks = [json.loads(l) for l in (EVAL / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    return [t for t in tasks if split == "all" or t["split"] == split]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--split", default="all")
    ap.add_argument("--arms", default="baseline,oneliner,bohemian")
    ap.add_argument("--skill-dir", default=str(SKILL), help="alternate skill folder (for ablations / versions)")
    ap.add_argument("--arm-label", default=None, help="label to store the bohemian arm under (e.g. bohemian_v2)")
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--samples", type=int, default=SAMPLES)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--retry-empty", action=argparse.BooleanOptionalAction, default=True,
                    help="resample outputs that came back empty because hidden reasoning used the whole budget (all arms)")
    args = ap.parse_args()

    prompts = arms(Path(args.skill_dir))
    tasks = load_tasks(args.split)
    if args.limit:
        tasks = tasks[: args.limit]
    out_dir = EVAL / "results" / args.run
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "generations.jsonl"
    done = set()
    if out.exists():
        for l in out.read_text(encoding="utf-8").splitlines():
            r = json.loads(l)
            done.add((r["task_id"], r["model"], r["arm"], r["sample"]))

    jobs = []
    for t in tasks:
        for model in args.models.split(","):
            for arm in args.arms.split(","):
                label = args.arm_label if (arm == "bohemian" and args.arm_label) else arm
                for s in range(args.samples):
                    if (t["id"], model, label, s) not in done:
                        jobs.append((t, model, arm, label, s))
    print(f"{len(jobs)} generations to run; spent so far ${spent():.4f}")

    def work(job):
        t, model, arm, label, s = job
        retries = 0
        while True:
            # Technical-failure rule, identical for every arm (added after run v1): some providers ignore
            # reasoning=off and spend the whole budget on hidden reasoning, returning no text. Resample those.
            raw, usage = chat(model, prompts[arm], t["prompt"] + WRAPPER, temperature=TEMPERATURE,
                              max_tokens=MAX_TOKENS, seed_index=s + 1000 * retries, tag=f"gen:{label}")
            final, ok = extract(raw)
            hidden = (usage.get("completion_tokens_details") or {}).get("reasoning_tokens") or 0
            if final.strip() or hidden < 0.9 * MAX_TOKENS or retries >= RETRIES or not args.retry_empty:
                break
            retries += 1
        return {"task_id": t["id"], "model": model, "arm": label, "sample": s, "final": final,
                "wrapped": ok, "raw": raw, "completion_tokens": usage.get("completion_tokens"),
                "cost": usage.get("cost"), "retries": retries}

    n = 0
    with ThreadPoolExecutor(args.workers) as ex, out.open("a", encoding="utf-8") as f:
        futs = [ex.submit(work, j) for j in jobs]
        for fut in as_completed(futs):
            try:
                r = fut.result()
            except BudgetExceeded as e:
                print("BUDGET STOP:", e)
                ex.shutdown(cancel_futures=True)
                break
            except Exception as e:  # keep going; a missing cell is reported by the analysis
                print("error:", e)
                continue
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
            n += 1
            if n % 50 == 0:
                print(f"  {n}/{len(jobs)}  spent ${spent():.4f}")
    print(f"done: {n} written; spent ${spent():.4f}")


if __name__ == "__main__":
    main()
