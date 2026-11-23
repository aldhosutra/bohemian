# Stronger-judge audit: openai/gpt-5.4-mini, run `v3`, test split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| baseline | 40 | openai/gpt-5.4-mini | 90% | 95% | 95% | 82% | 69% |
| baseline | 40 | google/gemini-2.5-flash-lite | 52% | 90% | 85% | 72% | 55% |
| baseline | 40 | openai/gpt-4o-mini | 40% | 82% | 68% | 45% | 28% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (baseline): 75% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (baseline): 52% of 40 pairs

| oneliner | 40 | openai/gpt-5.4-mini | 45% | 52% | 50% | 38% | 32% |
| oneliner | 40 | google/gemini-2.5-flash-lite | 48% | 42% | 45% | 40% | 42% |
| oneliner | 40 | openai/gpt-4o-mini | 49% | 19% | 25% | 30% | 41% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (oneliner): 68% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (oneliner): 78% of 40 pairs

