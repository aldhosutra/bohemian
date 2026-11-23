### Pairwise win rate of Bohemian, test split (both cheap judges; 95% CI over tasks)


**vs baseline**

| question | v1 | v2 | v3 |
|---|---|---|---|
| original | 61% [55–68] | 64% [57–71] | 65% [58–72] |
| unpredictable | 77% [71–82] | 79% [73–85] | 82% [76–88] |
| distinctive | 72% [66–77] | 75% [69–82] | 80% [73–86] |
| prefer | 64% [58–71] | 70% [62–77] | 73% [65–80] |
| task | 51% [46–55] | 53% [48–58] | 53% [48–57] |

**vs oneliner**

| question | v1 | v2 | v3 |
|---|---|---|---|
| original | 39% [34–45] | 39% [34–45] | 44% [38–49] |
| unpredictable | 25% [20–30] | 29% [24–34] | 35% [29–41] |
| distinctive | 26% [21–31] | 28% [22–34] | 38% [31–44] |
| prefer | 26% [21–32] | 31% [25–38] | 37% [31–43] |
| task | 37% [32–42] | 40% [35–45] | 42% [36–47] |

**Judge-free metrics (Bohemian arm; baseline / one-liner for reference)**

| metric | baseline | oneliner | v1 | v2 | v3 |
|---|---|---|---|---|---|
| constraint pass | 0.940 | 0.870 | 0.894 | 0.884 | 0.898 |
| held-out clichés /100w | 0.342 | 0.225 | 0.149 | 0.137 | 0.171 |
| typicality | 0.737 | 0.626 | 0.603 | 0.596 | 0.605 |
| semantic diversity | 0.187 | 0.267 | 0.303 | 0.301 | 0.276 |
| cross-model sim | 0.749 | 0.680 | 0.635 | 0.642 | 0.648 |
| words | 169 | 194 | 185 | 191 | 203 |

**Stronger-judge audit (openai/gpt-5.4-mini) on a random test-split subset**

| run | reference | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|
| v2 | baseline | 88% | 97% | 95% | 82% | 70% |
| v2 | oneliner | 42% | 42% | 42% | 38% | 41% |
| v3 | baseline | 90% | 98% | 100% | 92% | 61% |
| v3 | oneliner | 49% | 38% | 48% | 55% | 56% |
