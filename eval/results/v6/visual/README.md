# Visual tests (posters and playable Shorts)

These were run during the v6 work, from a scratch folder. The scripts in `scripts/` read `upstream/visuals.md` and write `out.json` there. To rerun them, point those paths at `eval/competitors/antialgorithm/visuals.md` and this folder. Generators, settings and wrapper are the same as in the text benchmark. Antialgorithm's arm adds its `visuals.md` to its SKILL.md.

| File | What it is |
|---|---|
| `scripts_text_shorts.json` | YouTube Short scripts as text (2 briefs, 4 arms), the first comparison |
| `posters_round1.json` | 32 SVG posters: library late nights and a jazz concert; baseline, Antialgorithm, v4b, v5 |
| `posters_round2.json` | 96 SVG posters on 6 new briefs; baseline, Antialgorithm, v4b, v6 |
| `shorts_html.json` | 16 playable 30-second HTML Shorts aimed at virality; Antialgorithm vs v4b |
| `user_picks_round1.json`, `user_picks_round2.json`, `user_picks_shorts.json` | the user's blind picks, decoded |
| `poster_codes.json`, `shorts_codes.json` | the blind codes shown on the review pages, mapped to arms |
| `judge_calibration_round1.json` | vision judges ranking the round-1 walls, compared with the user's picks |
| `judged_round2.json` | Gemini vision rankings of round 2, and text-overflow pixel counts |

`scripts/overflow.py` renders only the text of an SVG on a padded canvas and counts ink outside the 600×900 poster. `scripts/vjudge.py` shows a judge a numbered grid of posters and asks for its top three.
