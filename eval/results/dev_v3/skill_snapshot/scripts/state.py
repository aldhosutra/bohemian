import json
import os
import time


def state_dir():
    custom = os.environ.get("BOHEMIAN_HOME")
    if custom:
        return custom
    base = os.environ.get("XDG_STATE_HOME") or os.path.join(os.path.expanduser("~"), ".local", "state")
    return os.path.join(base, "bohemian")


def history_path():
    return os.path.join(state_dir(), "history.jsonl")


def load(kind=None):
    path = history_path()
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if kind is None or row.get("type") == kind:
                rows.append(row)
    return rows


def add(row, keep=500):
    os.makedirs(state_dir(), exist_ok=True)
    rows = load()
    rows.append({"t": int(time.time()), **row})
    rows = rows[-keep:]
    with open(history_path(), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
