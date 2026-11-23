# Stronger-judge audit: openai/gpt-5.4-mini, run `v4`, test split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| antialgorithm | 40 | openai/gpt-5.4-mini | 41% | 42% | 40% | 48% | 52% |
| antialgorithm | 40 | google/gemini-2.5-flash-lite | 57% | 42% | 45% | 52% | 46% |
| antialgorithm | 40 | openai/gpt-4o-mini | 49% | 69% | 59% | 60% | 50% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (antialgorithm): 55% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (antialgorithm): 62% of 40 pairs

| baseline | 40 | openai/gpt-5.4-mini | 88% | 95% | 95% | 85% | 65% |
| baseline | 40 | google/gemini-2.5-flash-lite | 60% | 82% | 82% | 80% | 56% |
| baseline | 40 | openai/gpt-4o-mini | 55% | 62% | 55% | 40% | 41% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (baseline): 80% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (baseline): 50% of 40 pairs

| oneliner | 40 | openai/gpt-5.4-mini | 48% | 45% | 48% | 48% | 48% |
| oneliner | 40 | google/gemini-2.5-flash-lite | 57% | 55% | 60% | 60% | 49% |
| oneliner | 40 | openai/gpt-4o-mini | 55% | 28% | 30% | 22% | 46% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (oneliner): 52% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (oneliner): 50% of 40 pairs

