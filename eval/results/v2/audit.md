# Stronger-judge audit: openai/gpt-5.4-mini, run `v2`, test split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| baseline | 60 | openai/gpt-5.4-mini | 88% | 97% | 95% | 82% | 70% |
| baseline | 60 | google/gemini-2.5-flash-lite | 63% | 85% | 85% | 82% | 62% |
| baseline | 60 | openai/gpt-4o-mini | 57% | 66% | 61% | 52% | 42% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (baseline): 77% of 60 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (baseline): 57% of 60 pairs

| oneliner | 60 | openai/gpt-5.4-mini | 42% | 42% | 42% | 38% | 41% |
| oneliner | 60 | google/gemini-2.5-flash-lite | 33% | 28% | 27% | 28% | 32% |
| oneliner | 60 | openai/gpt-4o-mini | 37% | 20% | 23% | 28% | 32% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (oneliner): 57% of 60 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (oneliner): 67% of 60 pairs

