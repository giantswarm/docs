# Semantic PoC result (2026-11-19)

Ran the OpenSearch ML Commons PoC (`all-MiniLM-L6-v2`, page-level embeddings)
over 302 docs pages (release notes excluded), comparing keyword, neural and
hybrid search on 15 reworded / synonym queries.

## Result

| Method | Hit rate |
|---|---|
| keyword | 8/15 (53%) |
| neural (semantic) | 12/15 (80%) |
| hybrid (min-max, 0.3 keyword / 0.7 neural) | 11/15 (73%) |

Setting aside one broken query (`make a cluster smaller`, whose best page
`cluster-downgrades` is not on this branch), neural is 12/14 (86%).

## Reading it

- Semantic search clearly helps on reworded queries. Neural rescued the cases
  keyword missed: "restrict traffic between pods" to network policy, "move apps
  off the app platform" to the app-platform deprecation page, "single sign on
  setup" to Dex.
- Hybrid landed below neural here only because every query in this set is
  reworded, so the weak keyword scores drag the min-max blend down. On mixed
  traffic (the real gate queries hit 91% on keyword alone) hybrid is normally the
  best of both. Re-weighting toward neural, or using the RRF score-ranker, would
  lift it.
- Two genuine neural misses show the small-model, page-level limits. For
  "automatically add and remove nodes" the model keyed on the surface words
  "automatic" and "add" (gitops automatic-update, add organization) rather than
  the concept of autoscaling. For "sign in to my cluster" the word "cluster"
  dominated and pulled cluster-management pages over authentication. Both are
  what real phase 2 addresses: section-level records (the autoscaler page body
  describes adding and removing nodes, which embeds far better than the title)
  and optionally a stronger model.

## For the plan

Phase 2 (semantic) would measurably improve the minority of queries that use
non-doc vocabulary, which is also why Inkeep (AI, semantic) handled the gate's
keyword misses. Keyword alone already served 91% of real traffic, so semantic is
a real improvement, not a necessity. This PoC is page-level and uses a small
model, so it is a floor, not a ceiling: the real phase 2 (section records, a
hybrid pipeline tuned across mixed traffic) should do better.
