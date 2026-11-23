# Stronger-judge audit: google/gemini-3.1-flash-lite, run `v5`, dev split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| antialgorithm | 72 | google/gemini-3.1-flash-lite | 54% | 53% | 54% | 56% | 47% |
| antialgorithm | 72 | google/gemini-2.5-flash-lite | 53% | 47% | 51% | 51% | 50% |
| antialgorithm | 72 | openai/gpt-4o-mini | 54% | 69% | 68% | 65% | 62% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (antialgorithm): 46% of 72 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (antialgorithm): 54% of 72 pairs

