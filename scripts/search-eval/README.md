# Docs search relevance gate

The decision point for phase 1 of the self-hosted docs search. It measures how
often keyword search over the `/searchapi` gateway returns a correct page, and
compares that with Inkeep. Phase 1 is enough, and the plan stops, when keyword
search hits at least as often as Inkeep with p95 latency under the budget. Only
if it falls short does phase 2 (semantic search) get built.

## Run it

```sh
python3 run.py --queries queries.json
```

No dependencies beyond the Python standard library. It queries the production
`/searchapi` the way the widget does (a `Documentation` query plus a smaller
`Blog` query) and prints a Markdown report: a per-query table, the top-k hit
rate, the p95 latency, and, once Inkeep results are filled in, a verdict.

## The query set

`queries.json` holds the queries. Each entry is:

```json
{"q": "how do I resize a cluster", "expect": ["/cluster-management"], "inkeep_hit": null}
```

- `q` is a real query. Use about 30 from real search behaviour, not invented ones.
- `expect` lists URL fragments. A result counts as a hit when any fragment is a
  substring of the result's URL, so keep them specific enough to mean the right
  page but not so exact they miss a valid anchor.
- `inkeep_hit` records how Inkeep did, filled in by hand (see below). `null`
  until judged.

Top of the file, `top_k` sets how many docs results count as the visible top
(the blog group is always included), and `latency_budget_ms` sets the p95 budget.

## Judging Inkeep

Inkeep is still live on the production docs site, so compare against it there.
For each query, open the Inkeep search on <https://docs.giantswarm.io/>, run the
query, and set `inkeep_hit` to `true` if a correct page is in its top 5, `false`
if not. Re-run `run.py` and it prints the comparison and the verdict.

The query set and this script stay in the repo so the gate can be re-run after
any tuning or a model change.
