# Stronger-judge audit: openai/gpt-5.4-mini, run `v3`, test split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| antialgorithm | 40 | openai/gpt-5.4-mini | 49% | 46% | 50% | 52% | 54% |
| antialgorithm | 40 | google/gemini-2.5-flash-lite | 45% | 45% | 48% | 50% | 51% |
| antialgorithm | 40 | openai/gpt-4o-mini | 44% | 64% | 54% | 61% | 56% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (antialgorithm): 68% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (antialgorithm): 72% of 40 pairs

