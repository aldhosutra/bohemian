# Stronger-judge audit: openai/gpt-5.4-mini, run `dev_v3`, dev split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| oneliner | 36 | openai/gpt-5.4-mini | 47% | 44% | 44% | 50% | 56% |
| oneliner | 36 | google/gemini-2.5-flash-lite | 39% | 39% | 38% | 33% | 38% |
| oneliner | 36 | openai/gpt-4o-mini | 47% | 19% | 17% | 17% | 35% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (oneliner): 67% of 36 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (oneliner): 56% of 36 pairs

| baseline | 36 | openai/gpt-5.4-mini | 83% | 86% | 86% | 78% | 72% |
| baseline | 36 | google/gemini-2.5-flash-lite | 64% | 83% | 81% | 72% | 56% |
| baseline | 36 | openai/gpt-4o-mini | 53% | 64% | 50% | 44% | 29% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (baseline): 72% of 36 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (baseline): 56% of 36 pairs

