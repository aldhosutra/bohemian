### Pairwise win rate of Bohemian, all split (both cheap judges; 95% CI over tasks)


**vs baseline**

| question | v1 | v2 | v3 |
|---|---|---|---|
| original | 58% [53–64] | 61% [55–68] | 62% [55–68] |
| unpredictable | 74% [69–79] | 78% [73–83] | 80% [75–85] |
| distinctive | 70% [65–75] | 75% [69–80] | 78% [72–83] |
| prefer | 62% [56–68] | 67% [61–73] | 70% [63–76] |
| task | 48% [44–52] | 50% [46–55] | 50% [46–54] |

**vs oneliner**

| question | v1 | v2 | v3 |
|---|---|---|---|
| original | 40% [35–44] | 42% [37–47] | 43% [39–48] |
| unpredictable | 25% [21–30] | 29% [24–33] | 34% [29–39] |
| distinctive | 26% [22–30] | 27% [23–32] | 35% [30–41] |
| prefer | 27% [22–31] | 31% [26–36] | 34% [29–40] |
| task | 37% [33–41] | 40% [36–44] | 41% [36–45] |

**Judge-free metrics (Bohemian arm; baseline / one-liner for reference)**

| metric | baseline | oneliner | v1 | v2 | v3 |
|---|---|---|---|---|---|
| constraint pass | 0.948 | 0.881 | 0.901 | 0.889 | 0.913 |
| held-out clichés /100w | 1.116 | 0.183 | 0.120 | 0.107 | 0.139 |
| typicality | 0.731 | 0.616 | 0.590 | 0.590 | 0.598 |
| semantic diversity | 0.190 | 0.271 | 0.312 | 0.302 | 0.280 |
| cross-model sim | 0.745 | 0.680 | 0.627 | 0.638 | 0.648 |
| words | 185 | 212 | 199 | 206 | 216 |

**Stronger-judge audit (openai/gpt-5.4-mini) on a random test-split subset**

| run | reference | original | unpredictable | distinctive | prefer | task |
|---|---|---|---|---|---|---|
| v2 | baseline | 88% | 97% | 95% | 82% | 70% |
| v2 | oneliner | 42% | 42% | 42% | 38% | 41% |
| v3 | baseline | 90% | 98% | 100% | 92% | 61% |
| v3 | oneliner | 49% | 38% | 48% | 55% | 56% |
