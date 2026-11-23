#!/usr/bin/env python3
import argparse
import re
import sys

TELLS = [
    ("opener", r"\bin a world where\b", "warm-up opener"),
    ("opener", r"\bimagine a (world|place|life)\b", "warm-up opener"),
    ("opener", r"\bhave you ever (wondered|felt|thought)\b", "hype question opener"),
    ("opener", r"\bin today'?s (fast-paced|digital|modern|busy)\b", "stock opener"),
    ("opener", r"\bpicture this\b", "warm-up opener"),
    ("inflated", r"\btapestry\b", "inflated word"),
    ("inflated", r"\btestament to\b", "inflated phrase"),
    ("inflated", r"\bdelv(e|es|ed|ing)\b", "inflated word"),
    ("inflated", r"\brealm of\b", "inflated phrase"),
    ("inflated", r"\bembark(s|ed|ing)? on\b", "inflated phrase"),
    ("inflated", r"\bunlock(s|ing)? (the|your)\b", "inflated phrase"),
    ("inflated", r"\belevate(s|d)? your\b", "inflated phrase"),
    ("inflated", r"\bseamless(ly)?\b", "inflated word"),
    ("inflated", r"\bvibrant\b", "inflated word"),
    ("inflated", r"\bbustling\b", "inflated word"),
    ("inflated", r"\bintricate\b", "inflated word"),
    ("inflated", r"\bbeacon of\b", "inflated phrase"),
    ("inflated", r"\bsymphony of\b", "inflated phrase"),
    ("inflated", r"\bdance of\b", "inflated phrase"),
    ("structure", r"\b(it'?s|this is|is) not (just|only|merely) (a |an )?[\w\s'-]{1,30}[,;.—-]+\s*(it'?s|but)\b", "not-just-X-but-Y contrast"),
    ("filler", r"\bmore than ever\b", "filler"),
    ("filler", r"\bat the end of the day\b", "filler"),
    ("filler", r"\bthe power of\b", "filler"),
    ("filler", r"\ba world of possibilit", "filler"),
    ("emotion", r"\b(felt|feel|feels|feeling) a (wave|surge|pang|rush) of\b", "named emotion"),
    ("emotion", r"\ba wave of (sadness|relief|nostalgia|emotion)\b", "named emotion"),
    ("copy", r"\bsay goodbye to\b", "stock copy"),
    ("copy", r"\bmeet the new\b", "stock copy"),
    ("copy", r"\byour new favorite\b", "stock copy"),
    ("copy", r"\bexperience the difference\b", "stock copy"),
    ("copy", r"\bdesigned with you in mind\b", "stock copy"),
    ("copy", r"\bgame[- ]changer\b", "stock copy"),
    ("copy", r"\brevolutioniz", "stock copy"),
    ("copy", r"\bnext level\b", "stock copy"),
    ("copy", r"\bpeace of mind\b", "promised feeling"),
    ("poetry", r"\bwhisper(ing|s)? winds?\b", "stock image"),
    ("poetry", r"\bdancing leaves\b", "stock image"),
    ("poetry", r"\bgolden sun\b", "stock image"),
    ("poetry", r"\bsilver moon\b", "stock image"),
    ("poetry", r"\bgentle rain\b", "stock image"),
    ("names", r"\b(Elara|Kael|Lyra|Seraphina|Thorne|Aria|Silas|Juniper)\b", "stock character name"),
    ("names", r"\b(Lumina|Zenith|Nexus|Aether|Veritas)\b", "stock brand name"),
    ("second-order", r"\b(at|around) \d{1,2}:\d{2}\s?(a\.?m\.?|p\.?m\.?)", "exact time used to look concrete"),
]

COMPILED = [(cat, re.compile(rx, re.IGNORECASE), note) for cat, rx, note in TELLS]


def lint(text):
    hits = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for cat, rx, note in COMPILED:
            for m in rx.finditer(line):
                hits.append((line_no, cat, m.group(0), note))
    triples = len(re.findall(r"\b\w+, \w+,? and \w+\b", text))
    exclaims = text.count("!")
    return hits, triples, exclaims


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="List surface tells in a draft. A first pass only: it cannot see a default premise or structure.")
    ap.add_argument("file", nargs="?", help="file to check; reads stdin if omitted")
    args = ap.parse_args()
    text = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    hits, triples, exclaims = lint(text)
    words = max(1, len(text.split()))
    for line_no, cat, found, note in hits:
        print(f"line {line_no}: [{cat}] \"{found}\" ({note})")
    if triples:
        print(f"{triples} list(s) of three; check they are not there by habit")
    if exclaims:
        print(f"{exclaims} exclamation mark(s)")
    print(f"{len(hits)} tell(s) in {words} words. Surface tells only; the default premise, shape and material need the method's own checks.")


if __name__ == "__main__":
    main()
