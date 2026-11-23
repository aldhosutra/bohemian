"""OpenRouter client for the Bohemian benchmark.

Stdlib only. Every call is cached on disk by a hash of the request, so reruns
never pay twice, and every paid call is appended to a ledger. Once the ledger
total reaches the budget, calls raise BudgetExceeded instead of spending.
"""
import hashlib
import json
import os
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parents[1]
CACHE_DIR = Path(os.environ.get("BOHEMIAN_CACHE", EVAL_DIR / ".cache"))
LEDGER = Path(os.environ.get("BOHEMIAN_LEDGER", EVAL_DIR / "results" / "ledger.jsonl"))
BUDGET_USD = float(os.environ.get("BOHEMIAN_BUDGET_USD", "3.00"))
API = "https://openrouter.ai/api/v1"

_lock = threading.Lock()


class BudgetExceeded(RuntimeError):
    pass


def spent():
    if not LEDGER.exists():
        return 0.0
    total = 0.0
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if line.strip():
            total += json.loads(line).get("cost", 0.0)
    return total


def _key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")
    return key


def _post(path, body, timeout=180):
    req = urllib.request.Request(
        API + path,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {_key()}",
            "Content-Type": "application/json",
            "X-Title": "bohemian-benchmark",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def _cached(kind, body, fetch, tag):
    digest = hashlib.sha256(json.dumps([kind, body], sort_keys=True).encode()).hexdigest()
    path = CACHE_DIR / kind / digest[:2] / f"{digest}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    with _lock:
        if spent() >= BUDGET_USD:
            raise BudgetExceeded(f"ledger at ${spent():.4f} >= budget ${BUDGET_USD:.2f}")
    last = None
    for attempt in range(5):
        try:
            data = fetch(body)
            break
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError, KeyError) as e:
            last = e
            time.sleep(2 * (attempt + 1))
    else:
        raise RuntimeError(f"{kind} call failed after retries: {last}")
    cost = (data.get("usage") or {}).get("cost", 0.0) or 0.0
    with _lock:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"t": time.time(), "kind": kind, "model": body.get("model"), "tag": tag, "cost": cost}) + "\n")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")
    return data


def chat(model, system, user, temperature=1.0, max_tokens=1200, seed_index=0, tag="", reasoning=False):
    """One chat completion. seed_index separates independent samples of the same prompt in the cache."""
    body = {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}],
    }
    if not reasoning:
        body["reasoning"] = {"enabled": False}

    def fetch(b):
        data = _post("/chat/completions", b)
        if "choices" not in data:
            raise ValueError(f"bad response: {str(data)[:300]}")
        return data

    data = _cached("chat", {**body, "_sample": seed_index}, lambda b: fetch(body), tag)
    msg = data["choices"][0]["message"]
    return msg.get("content") or "", data.get("usage") or {}


def embed(texts, model="openai/text-embedding-3-small", tag="embed"):
    out = []
    for i in range(0, len(texts), 64):
        batch = texts[i : i + 64]
        body = {"model": model, "input": batch}
        data = _cached("embed", body, lambda b: _post("/embeddings", b), tag)
        out.extend(d["embedding"] for d in sorted(data["data"], key=lambda d: d["index"]))
    return out
