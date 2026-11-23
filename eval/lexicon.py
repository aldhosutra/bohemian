"""Cliche / AI-tell lexicon for the benchmark.

Built separately from the skill and deliberately broader. Each entry is
(key, regex). `key` is a plain phrase; an entry counts as SHARED if its key
appears anywhere in the skill's text, otherwise HELD-OUT. Reporting the
held-out rate separately shows whether the skill reduces cliches in general
or only the exact ones it names (teaching to the test).
"""
import re
from functools import lru_cache
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1] / "skills" / "bohemian"

ENTRIES = [
    # openers / framing
    ("in a world where", r"\bin a world where\b"),
    ("imagine a", r"\bimagine a\b"),
    ("have you ever", r"\bhave you ever\b"),
    ("in today's", r"\bin today'?s\b"),
    ("picture this", r"\bpicture this\b"),
    ("once upon a time", r"\bonce upon a time\b"),
    ("little did", r"\blittle did (she|he|they|i|we) know\b"),
    ("it was a dark", r"\bit was a dark\b"),
    ("let's dive", r"\blet'?s dive\b"),
    ("ever wondered", r"\bever wondered\b"),
    ("look no further", r"\blook no further\b"),
    # inflated vocabulary
    ("tapestry", r"\btapestr(y|ies)\b"),
    ("testament", r"\btestament\b"),
    ("delve", r"\bdelv(e|es|ed|ing)\b"),
    ("realm", r"\brealms?\b"),
    ("embark", r"\bembark"),
    ("unlock", r"\bunlock"),
    ("elevate", r"\belevat(e|es|ed|ing)\b"),
    ("seamless", r"\bseamless"),
    ("vibrant", r"\bvibrant\b"),
    ("bustling", r"\bbustling\b"),
    ("intricate", r"\bintricate"),
    ("beacon", r"\bbeacons?\b"),
    ("symphony", r"\bsymphon(y|ies)\b"),
    ("labyrinth", r"\blabyrinth"),
    ("enigmatic", r"\benigmatic\b"),
    ("ethereal", r"\bethereal\b"),
    ("kaleidoscope", r"\bkaleidoscop"),
    ("myriad", r"\bmyriad\b"),
    ("plethora", r"\bplethora\b"),
    ("nestled", r"\bnestled\b"),
    ("palpable", r"\bpalpable\b"),
    ("profound", r"\bprofound(ly)?\b"),
    ("resonate", r"\bresonat(e|es|ed|ing)\b"),
    ("navigate the", r"\bnavigat(e|ing) the\b"),
    ("landscape of", r"\b(ever-?changing |digital )?landscape of\b"),
    ("foster", r"\bfoster(s|ed|ing)?\b"),
    ("holistic", r"\bholistic\b"),
    ("synergy", r"\bsynerg"),
    ("cutting-edge", r"\bcutting[- ]edge\b"),
    ("state-of-the-art", r"\bstate[- ]of[- ]the[- ]art\b"),
    ("innovative", r"\binnovative\b"),
    ("empower", r"\bempower"),
    ("journey", r"\bjourney\b"),
    ("whimsical", r"\bwhimsical\b"),
    ("cacophony", r"\bcacophony\b"),
    ("indelible", r"\bindelible\b"),
    ("unwavering", r"\bunwavering\b"),
    ("meticulous", r"\bmeticulous"),
    ("tireless", r"\btireless"),
    # stock phrases / filler
    ("more than ever", r"\bmore than ever\b"),
    ("at the end of the day", r"\bat the end of the day\b"),
    ("the power of", r"\bthe power of\b"),
    ("world of possibilities", r"\bworld of possibilit"),
    ("a sense of", r"\ba sense of\b"),
    ("in the heart of", r"\bin the heart of\b"),
    ("stands as", r"\bstands as\b"),
    ("serves as a reminder", r"\bserves? as a (reminder|testament)\b"),
    ("plays a crucial role", r"\bplays? a (crucial|vital|pivotal) role\b"),
    ("ever-evolving", r"\bever[- ]evolving\b"),
    ("not just", r"\b(is|are|it'?s|was) not (just|only|merely)\b"),
    ("more than just", r"\bmore than just\b"),
    ("whether you're", r"\bwhether you'?re\b"),
    ("best version of yourself", r"\bbest version of (yourself|you)\b"),
    ("journey not destination", r"\bjourney,? not (a|the) destination\b"),
    ("time stood still", r"\btime stood still\b"),
    ("heart pounding", r"\bheart (was )?(pounding|racing|hammering)\b"),
    ("breath caught", r"\bbreath (caught|hitched)\b"),
    ("let out a breath", r"\blet out a breath\b"),
    ("a mix of", r"\ba mix(ture)? of\b"),
    ("couldn't help but", r"\bcouldn'?t help but\b"),
    ("eyes sparkled", r"\beyes (sparkl|twinkl|glisten)"),
    ("smile tugged", r"\bsmile tug"),
    ("wave of", r"\b(wave|surge|pang|rush) of (sadness|relief|nostalgia|emotion|grief|joy|warmth|fear)\b"),
    ("felt a", r"\b(she|he|they|i) felt (a|an) (deep|sudden|strange|overwhelming)\b"),
    ("tears streamed", r"\btears (stream|roll|ran)"),
    ("lump in throat", r"\blump in (her|his|my|their) throat\b"),
    ("silence was deafening", r"\bsilence was deafening\b"),
    ("weight of the world", r"\bweight of the world\b"),
    ("vast emptiness", r"\bvast (emptiness|expanse|void|darkness)\b"),
    ("pale blue dot", r"\bpale blue dot\b"),
    ("blue marble", r"\bblue marble\b"),
    ("stars like diamonds", r"\bstars? like (diamonds|jewels)\b"),
    # nature/poetry stock images
    ("whispering wind", r"\bwhisper(ing|s|ed)? (wind|breeze|leaves|trees)\b"),
    ("dancing leaves", r"\bdancing (leaves|flames|shadows|light)\b"),
    ("golden sun", r"\bgolden (sun|hues?|light|rays)\b"),
    ("silver moon", r"\bsilver(y)? moon\b"),
    ("gentle rain", r"\bgentle (rain|breeze)\b"),
    ("crimson", r"\bcrimson\b"),
    ("azure", r"\bazure\b"),
    ("endless sea", r"\bendless (sea|ocean|sky|night)\b"),
    ("waves crash", r"\bwaves? crash"),
    ("tapestry of stars", r"\bblanket of stars\b"),
    ("city that never sleeps", r"\bcity that never sleeps\b"),
    ("neon lights", r"\bneon (lights|glow|signs)\b"),
    ("heart soul", r"\bheart and soul\b"),
    # marketing
    ("say goodbye to", r"\bsay goodbye to\b"),
    ("meet the new", r"\bmeet (the new|your new)\b"),
    ("your new favorite", r"\byour new favou?rite\b"),
    ("experience the difference", r"\bexperience the\b"),
    ("designed with you in mind", r"\bwith you in mind\b"),
    ("game-changer", r"\bgame[- ]chang"),
    ("revolutionize", r"\brevolutioni[sz]"),
    ("next level", r"\bnext[- ]level\b"),
    ("peace of mind", r"\bpeace of mind\b"),
    ("take it to", r"\btake (it|your \w+) to the next\b"),
    ("elevate your", r"\belevate your\b"),
    ("unleash", r"\bunleash"),
    ("hassle-free", r"\bhassle[- ]free\b"),
    ("effortless", r"\beffortless"),
    ("one-stop", r"\bone[- ]stop\b"),
    ("join thousands", r"\bjoin (thousands|millions)\b"),
    ("don't miss out", r"\bdon'?t miss( out)?\b"),
    ("what are you waiting for", r"\bwhat are you waiting for\b"),
    ("treat yourself", r"\btreat yourself\b"),
    ("crafted with", r"\b(lovingly |carefully )?crafted with\b"),
    ("passion for", r"\b(our )?passion (for|is)\b"),
    ("leading provider", r"\bleading provider\b"),
    ("commitment to excellence", r"\bcommitment to (excellence|quality)\b"),
    ("unforgettable", r"\bunforgettable\b"),
    ("like never before", r"\blike never before\b"),
    ("the future of", r"\bthe future of\b"),
    ("smarter faster", r"\b(smarter|faster|easier), (smarter|faster|easier),? and (smarter|faster|easier)\b"),
    # stock names
    ("elara", r"\bElara\b"), ("kael", r"\bKael\b"), ("lyra", r"\bLyra\b"), ("seraphina", r"\bSeraphina\b"),
    ("thorne", r"\bThorne\b"), ("silas", r"\bSilas\b"), ("aria", r"\bAria\b"), ("juniper", r"\bJuniper\b"),
    ("elias", r"\bElias\b"), ("mara", r"\bMara\b"), ("eleanor", r"\bEleanor\b"), ("evelyn", r"\bEvelyn\b"),
    ("arthur", r"\bArthur\b"), ("maya", r"\bMaya\b"), ("leo", r"\bLeo\b"), ("chen", r"\bChen\b"),
    ("vance", r"\bVance\b"), ("finch", r"\bFinch\b"), ("orion", r"\bOrion\b"), ("nova", r"\bNova\b"),
    ("lumina", r"\bLumina\b"), ("zenith", r"\bZenith\b"), ("nexus", r"\bNexus\b"), ("aether", r"\bAether\b"),
    ("apex", r"\bApex\b"), ("atlas", r"\bAtlas\b"), ("phoenix", r"\bPhoenix\b"), ("haven", r"\bHaven\b"),
    ("ember", r"\bEmber\b"), ("hearth", r"\bHearth\b"), ("bloom", r"\bBloom\b"), ("sprout", r"\bSprout\b"),
    # naming patterns
    ("-ify suffix", r"\b[A-Z]\w{2,}ify\b"),
    ("clean/sweep compound", r"\b(Clean|Sweep|Swift|Pure|Fresh|Tidy)[A-Z]\w+\b"),
    ("flow compound", r"\b[A-Z]\w+(Flow|Hub|Wise|Verse|Sphere|Genie|Mate|Pal|Buddy)\b"),
    # second-order creative tells
    ("exact time", r"\b\d{1,2}:\d{2}\s?(a\.?m\.?|p\.?m\.?)?\b"),
    ("captain's log", r"\b(captain'?s|personal|mission) log\b"),
    ("dear diary", r"\bdear (diary|future)\b"),
    ("error message", r"\berror( code)? \d+"),
]

# Patterns that contain capitals (names, CamelCase compounds) are case-sensitive; the rest are not.
COMPILED = [(k, re.compile(rx, 0 if re.search(r"[A-Z]", rx) else re.IGNORECASE)) for k, rx in ENTRIES]


@lru_cache(maxsize=1)
def skill_text():
    return " ".join(p.read_text(encoding="utf-8").lower() for p in SKILL_DIR.rglob("*") if p.suffix in {".md", ".py"})


def shared_keys():
    text = skill_text()
    return {k for k, _ in ENTRIES if re.search(r"(?<![a-z])" + re.escape(k.lower()) + r"s?(?![a-z])", text)}


def scan(text):
    """Return list of matched keys (with repeats)."""
    hits = []
    for key, rx in COMPILED:
        hits.extend(key for _ in rx.finditer(text))
    return hits


def rates(text):
    words = max(1, len(text.split()))
    hits = scan(text)
    shared = shared_keys()
    s = sum(1 for h in hits if h in shared)
    return {
        "cliche_per100": 100 * len(hits) / words,
        "cliche_shared_per100": 100 * s / words,
        "cliche_heldout_per100": 100 * (len(hits) - s) / words,
        "cliche_hits": hits,
    }


if __name__ == "__main__":
    sh = shared_keys()
    print(f"{len(ENTRIES)} entries, {len(sh)} shared with skill text, {len(ENTRIES) - len(sh)} held out")
    print("shared:", sorted(sh))
