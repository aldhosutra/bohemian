import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "skills" / "bohemian" / "scripts"


def run(*args, home):
    env = {**os.environ, "BOHEMIAN_HOME": home}
    return subprocess.run([sys.executable, str(SCRIPTS / args[0]), *args[1:]], capture_output=True, text=True, env=env)


class SkillScripts(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def test_seed_kinds_and_keep(self):
        for kind in ("text", "idea", "name"):
            r = run("seed.py", kind, "--no-log", home=self.home)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("anchor:", r.stdout)
        r = run("seed.py", "text", "--no-log", "--keep", "register=dry", home=self.home)
        self.assertIn("register: dry", r.stdout)
        self.assertFalse(os.path.exists(os.path.join(self.home, "history.jsonl")))

    def test_seed_avoids_recent_values(self):
        seen = set()
        for _ in range(6):
            out = run("seed.py", "text", home=self.home).stdout
            seen.add([l for l in out.splitlines() if l.startswith("register:")][0])
        self.assertGreaterEqual(len(seen), 5, "recent registers should not repeat quickly")

    def test_moves_log_and_streak_warning(self):
        self.assertIn("No moves", run("moves.py", home=self.home).stdout)
        run("moves.py", "add", "lens", "cleaner tells it", home=self.home)
        run("moves.py", "add", "lens", "ticket seller tells it", home=self.home)
        out = run("moves.py", home=self.home).stdout
        self.assertIn("lens=2", out)
        self.assertIn("Warning", out)
        self.assertNotEqual(run("moves.py", "add", "nonsense", "x", home=self.home).returncode, 0)
        run("moves.py", "clear", home=self.home)
        self.assertIn("No moves", run("moves.py", home=self.home).stdout)

    def test_lint_finds_tells_and_passes_clean_text(self):
        env = {**os.environ}
        dirty = "In a world where clutter rules, say goodbye to mess. It's not just an app, it's a lifestyle!"
        r = subprocess.run([sys.executable, str(SCRIPTS / "lint.py")], input=dirty, capture_output=True, text=True, env=env)
        self.assertIn("warm-up opener", r.stdout)
        self.assertIn("stock copy", r.stdout)
        self.assertIn("not-just-X-but-Y", r.stdout)
        clean = "The kettle clicks off. Nobody gets up."
        r = subprocess.run([sys.executable, str(SCRIPTS / "lint.py")], input=clean, capture_output=True, text=True, env=env)
        self.assertIn("0 tell(s)", r.stdout)


if __name__ == "__main__":
    unittest.main()
