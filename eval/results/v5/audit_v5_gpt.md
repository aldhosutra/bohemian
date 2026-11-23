# Stronger-judge audit: openai/gpt-5.4-mini, run `v5`, test split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| antialgorithm | 120 | openai/gpt-5.4-mini | 52% | 53% | 47% | 46% | 45% |
| antialgorithm | 120 | google/gemini-2.5-flash-lite | 48% | 45% | 45% | 44% | 48% |
| antialgorithm | 120 | openai/gpt-4o-mini | 49% | 59% | 57% | 59% | 50% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (antialgorithm): 60% of 120 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (antialgorithm): 58% of 120 pairs

