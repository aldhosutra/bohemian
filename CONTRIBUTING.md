# Contributing

Issues and pull requests are welcome.

## The skill text is the behavior

`skills/bohemian/SKILL.md` and `references/*.md` are read by the model, so wording changes behavior. Keep sentences short and plain. Don't name other tools, people or projects in skill text, and keep examples general.

`SKILL.md` loads on every creative request, so keep it short. Put detail in `references/` and point to it from the step that needs it.

## Changing the skill: prove it

A change to skill text must be measured, not argued for. One good output proves nothing.

1. Tune on the **dev split only** (12 tasks, one per category). Never look at test-split outputs while iterating.
2. Run the dev split with the old and new text, then judge and analyze:
   ```
   python3 eval/generate.py --run mychange --split dev --skill-dir path/to/new/skill --arm-label bohemian_new
   python3 eval/judge.py --run mychange --pairs bohemian_new:baseline,bohemian_new:oneliner
   python3 eval/metrics.py --run mychange
   python3 eval/analyze.py --run mychange --treat bohemian_new --split dev
   ```
3. If it helps on dev, run the full benchmark and report the **test split** numbers, including metrics that got worse.
4. Read a sample of outputs side by side. If a batch shares one look or one move, the skill has found a new default: add it to the second-order tells.

The benchmark caps spending with `BOHEMIAN_BUDGET_USD` (default 3.00) and caches every call, so a rerun with unchanged prompts costs nothing.

## New techniques

Add a technique to `references/techniques.md` only with: its family, what it does, when it fits, and **how it goes cheap**. A technique without a named failure mode is not ready.

## New tells

Add tells to `references/cliches.md` with a short example of output that made you want them. If a tell is also added to `eval/lexicon.py`, it becomes a *shared* entry and stops counting toward the held-out cliché rate. That is intended: the held-out rate only means something if the skill never sees those entries.

## Scripts

Python 3 standard library only. They must run on Linux, macOS and Windows: use `os.path`, and open files with `encoding="utf-8"`. Run the tests before opening a PR:

```
python3 -m unittest discover -s tests
```

## License

By contributing you agree that your work is released under the MIT license.
