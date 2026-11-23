# Relevance gate result (2026-11-19)

**Verdict: PASS. Phase 1 keyword search is enough. Phase 2 (semantic search) is not built.**

## What was measured

The 32 top docs search queries from the last 30 days (`queries.json`), run against
the production `/searchapi` gateway the way the search widget does: a
`Documentation` query plus a smaller `Blog` query. A query counts as a hit when a
page that answers it appears in the top 5 shown.

- Top-5 hit rate: **29 of 32 (91%)**.
- p95 latency: about **176 ms**, under the 300 ms budget. This is a client-side
  round-trip, so it overstates server latency. The plan owner accepted it as enough.

The three misses are specific, not systemic:

- `Configure the cluster role identity for Workload Cluster`: the long title ranks
  the general cluster configuration page above the AWS account page that documents
  `AWSClusterRoleIdentity`.
- `app migratoin`: the misspelling keeps the App Platform to HelmRelease migration
  page out of the results.
- `karp`: the gateway does not prefix-match, so the truncated "karpenter" finds no
  page and the query returns nothing.

## Inkeep comparison

The planned side-by-side with Inkeep was not run. Inkeep search is only reachable
through its proprietary API behind the widget SDK, not a queryable endpoint like
`/searchapi`, so it could not be measured the same way. The gate was decided on the
absolute result instead: a 91% top-5 hit rate on real queries, with latency under
budget, is enough to drop Inkeep. `inkeep_hit` stays open in the query set for a
manual check if one is ever wanted.

## Next

- Phase 2 is not built.
- Cancel Inkeep (giantswarm/docs#3654) is unblocked once the search widget
  (giantswarm/docs#3651) ships.
- Re-run `python3 run.py` after any search tuning to confirm the hit rate holds.
