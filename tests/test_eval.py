import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "eval" / "human"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "eval"))

import analyze  # noqa: E402
import judge  # noqa: E402
import lexicon  # noqa: E402
import metrics  # noqa: E402
from generate import extract, load_tasks  # noqa: E402
from score import fleiss  # noqa: E402


class Tasks(unittest.TestCase):
    def test_benchmark_shape(self):
        tasks = load_tasks()
        self.assertGreaterEqual(len(tasks), 50)
        self.assertEqual(len({t["id"] for t in tasks}), len(tasks))
        self.assertGreaterEqual(len({t["category"] for t in tasks}), 12)
        self.assertTrue(any(t["constrained"] for t in tasks) and any(not t["constrained"] for t in tasks))
        self.assertEqual(len(load_tasks("dev")), 12)


class Extraction(unittest.TestCase):
    def test_extract(self):
        self.assertEqual(extract("notes\n<final>\nHello\n</final>"), ("Hello", True))
        self.assertEqual(extract("notes <final>cut off"), ("cut off", False))
        self.assertEqual(extract("no tags"), ("no tags", False))
        self.assertEqual(extract("<final>draft</final> more <final>last</final>")[0], "last")


class Checks(unittest.TestCase):
    def test_constraints(self):
        t = {"checks": {"max_words": 5}}
        self.assertTrue(metrics.check(t, "one two three")[0])
        self.assertFalse(metrics.check(t, "one two three four five six")[0])
        self.assertTrue(metrics.check({"checks": {"n_lines": 3}}, "a\n\nb\nc\n")[0])
        self.assertFalse(metrics.check({"checks": {"n_lines": 3}}, "a\nb")[0])
        self.assertTrue(metrics.check({"checks": {"n_items": 2}}, "1. x\ntext\n2. y")[0])
        self.assertTrue(metrics.check({"checks": {"n_items": 2}}, "**1.** x\n**2.** y")[0])
        self.assertFalse(metrics.check({"checks": {"forbid": ["time"]}}, "Time passes")[0])
        self.assertTrue(metrics.check({"checks": {"forbid": ["age"]}}, "a page of cabbage")[0])
        self.assertTrue(metrics.check({"checks": {"paragraphs": 2}}, "p1\n\n\np2")[0])
        self.assertEqual(metrics.check({"checks": {}}, "x"), (None, {}))

    def test_items_and_jaccard(self):
        self.assertEqual(metrics.items("1. a\n2. b\nnote"), ["1. a", "2. b"])
        self.assertEqual(metrics.jaccard(metrics.ngrams("a b c d"), metrics.ngrams("a b c d")), 1.0)


class Lexicon(unittest.TestCase):
    def test_shared_and_heldout(self):
        # Use a fixed text so the test does not depend on the current skill wording.
        original = lexicon.skill_text
        lexicon.skill_text = lambda: "avoid a rich tapestry. remember the brief."
        try:
            shared = lexicon.shared_keys()
        finally:
            lexicon.skill_text = original
        self.assertIn("tapestry", shared)
        self.assertNotIn("ember", shared, "substring of 'remember' must not count as shared")
        real = lexicon.shared_keys()
        self.assertGreater(len(lexicon.ENTRIES) - len(real), len(real), "most entries should be held out")

    def test_case_sensitivity(self):
        self.assertIn("aria", lexicon.scan("Aria waited."))
        self.assertNotIn("aria", lexicon.scan("she sang an aria"))
        self.assertIn("delve", lexicon.scan("Let us DELVE in"))
        r = lexicon.rates("plain words only here")
        self.assertEqual(r["cliche_per100"], 0)


class Stats(unittest.TestCase):
    def test_sign_test(self):
        self.assertEqual(analyze.sign_test([1, 1, 1, -1, 0])[:2], (3, 1))
        self.assertAlmostEqual(analyze.sign_test([1] * 10)[2], 2 / 1024)
        self.assertEqual(analyze.sign_test([0, 0])[2], 1.0)

    def test_kappa(self):
        self.assertAlmostEqual(analyze.kappa(list("aabb"), list("aabb"), "ab"), 1.0)
        self.assertLess(analyze.kappa(list("abab"), list("baba"), "ab"), 0)

    def test_boot_contains_mean(self):
        m, lo, hi = analyze.boot([1, 2, 3, 4, 5])
        self.assertTrue(lo <= m <= hi)

    def test_spearman(self):
        self.assertAlmostEqual(analyze.spearman([1, 2, 3, 4], [10, 20, 30, 40]), 1.0)

    def test_fleiss_perfect(self):
        self.assertAlmostEqual(fleiss([{"treat": 3}, {"ref": 3}, {"treat": 3}]), 1.0)


class Judge(unittest.TestCase):
    def test_parse_and_balance(self):
        self.assertEqual(judge.parse_json('```json\n{"a": 1}\n```'), {"a": 1})
        self.assertIsNone(judge.parse_json("no json"))
        flips = [judge.flip(f"t{i}", "m", s, "bohemian", "baseline") for i in range(100) for s in range(3)]
        self.assertTrue(100 < sum(flips) < 200, "A/B assignment should be roughly balanced")


if __name__ == "__main__":
    unittest.main()
