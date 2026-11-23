# Stronger-judge audit: openai/gpt-5.4-mini, run `v3`, test split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| baseline | 40 | openai/gpt-5.4-mini | 90% | 98% | 100% | 92% | 61% |
| baseline | 40 | google/gemini-2.5-flash-lite | 76% | 89% | 86% | 86% | 65% |
| baseline | 40 | openai/gpt-4o-mini | 61% | 69% | 64% | 61% | 44% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (baseline): 92% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (baseline): 68% of 40 pairs

| oneliner | 40 | openai/gpt-5.4-mini | 49% | 38% | 48% | 55% | 56% |
| oneliner | 40 | google/gemini-2.5-flash-lite | 32% | 32% | 35% | 32% | 39% |
| oneliner | 40 | openai/gpt-4o-mini | 42% | 32% | 30% | 29% | 34% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (oneliner): 38% of 40 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (oneliner): 48% of 40 pairs

