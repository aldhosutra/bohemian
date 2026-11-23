# Stronger-judge audit: openai/gpt-5.4-mini, run `dev_v2`, dev split

Win rate of the treatment on the same pairs, by judge. Ties count half.

| reference | n | judge | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|---|
| oneliner | 36 | openai/gpt-5.4-mini | 36% | 25% | 33% | 39% | 38% |
| oneliner | 36 | google/gemini-2.5-flash-lite | 42% | 25% | 25% | 33% | 39% |
| oneliner | 36 | openai/gpt-4o-mini | 47% | 25% | 22% | 31% | 42% |

- `prefer` agreement, audit judge vs google/gemini-2.5-flash-lite (oneliner): 56% of 36 pairs

- `prefer` agreement, audit judge vs openai/gpt-4o-mini (oneliner): 58% of 36 pairs

