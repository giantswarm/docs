# Semantic PoC result (2026-11-19)

Ran the OpenSearch ML Commons PoC (`all-MiniLM-L6-v2`, page-level embeddings)
over 302 docs pages (release notes excluded), comparing keyword, neural and
hybrid search on 15 reworded / synonym queries.

## Result

| Method | Hit rate |
|---|---|
| keyword | 8/15 (53%) |
| neural (semantic) | 13/15 (87%) |
| hybrid (min-max, 0.3 keyword / 0.7 neural) | 13/15 (87%) |

Semantic (neural) and hybrid both reach 87% against keyword's 53% on these
reworded queries.

## Reading it

- Semantic search clearly helps on reworded queries. Neural and hybrid rescued
  the cases keyword missed: "restrict traffic between pods" to network policy,
  "move apps off the app platform" to the app-platform deprecation page, "single
  sign on setup" to Dex, "automatically add and remove nodes" to the autoscaler,
  "make a cluster smaller" to scaling.
- Hybrid matched neural at 87% and even caught one query neural alone missed
  ("cache container images locally"), so on this set it is the best of both. On
  mixed real traffic (the gate queries hit 91% on keyword alone) hybrid is the
  production choice, combining keyword precision with semantic recall.
- One residual miss shows the small-model, page-level limit: for "sign in to my
  cluster" the word "cluster" dominates the embedding and pulls cluster-management
  pages over authentication. This is what real phase 2 addresses: section-level
  records embed the concept more precisely than a page title, and a stronger model
  would help further.

## For the plan

Phase 2 (semantic) would measurably improve the minority of queries that use
non-doc vocabulary, which is also why Inkeep (AI, semantic) handled the gate's
keyword misses. Keyword alone already served 91% of real traffic, so semantic is
a real improvement, not a necessity. This PoC is page-level and uses a small
model, so it is a floor, not a ceiling: the real phase 2 (section records, a
hybrid pipeline tuned across mixed traffic) should do better.
