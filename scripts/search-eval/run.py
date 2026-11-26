#!/usr/bin/env python3
"""Relevance gate for docs search.

Runs a fixed query set against the public /searchapi gateway the way the search
widget does (a Documentation query plus a smaller Changes query for release
notes) and reports, per query, whether an expected page appears in the top
results, plus the overall top-k hit rate and p95 latency. Where the query set
also records how Inkeep did (filled in by hand, see the README), it compares the
two and prints a verdict.

Phase 1 passes, and the plan stops, when keyword search hits at least as often
as Inkeep with p95 latency under the budget. Only then is phase 2 considered.

No dependencies beyond the standard library. Run it from anywhere:

    python3 run.py --queries queries.json
"""
import argparse
import json
import time
import urllib.parse
import urllib.request

DEFAULT_ENDPOINT = "https://docs.giantswarm.io/searchapi/"
DEFAULT_DOCS_SIZE = 10
DEFAULT_CHANGES_SIZE = 5
DEFAULT_TOP_K = 5
DEFAULT_LATENCY_BUDGET_MS = 300


def fetch(endpoint, query, type_, size, timeout, breadcrumb=None):
    """Return (hits, elapsed_ms). hits is a list of _source dicts.

    breadcrumb narrows the query to one section, for example "changes".
    """
    params = {"q": query, "type": type_, "size": size}
    if breadcrumb:
        params["breadcrumb"] = breadcrumb
    params = urllib.parse.urlencode(params)
    req = urllib.request.Request(endpoint + "?" + params, headers={"Accept": "application/json"})
    start = time.monotonic()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read()
    elapsed_ms = (time.monotonic() - start) * 1000
    data = json.loads(body)
    hits = [h.get("_source", {}) for h in data.get("hits", {}).get("hits", [])]
    return hits, elapsed_ms


def changes_size(spec):
    """The size of the Changes query. An older query set names it blog_size."""
    return spec.get("changes_size", spec.get("blog_size", DEFAULT_CHANGES_SIZE))


def matches(url, expected):
    """True when any expected fragment is a substring of the result URL."""
    return any(fragment and fragment in url for fragment in expected)


def percentile(values, p):
    if not values:
        return 0.0
    ordered = sorted(values)
    # Nearest-rank percentile: the smallest value at or above p% of the data.
    rank = max(1, -(-len(ordered) * p // 100))  # ceil(len*p/100), at least 1
    return ordered[int(rank) - 1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", default="queries.json", help="path to the query set JSON")
    ap.add_argument("--timeout", type=float, default=10.0, help="per-request timeout in seconds")
    args = ap.parse_args()

    with open(args.queries, encoding="utf-8") as f:
        spec = json.load(f)

    endpoint = spec.get("endpoint", DEFAULT_ENDPOINT)
    docs_size = spec.get("docs_size", DEFAULT_DOCS_SIZE)
    changes = changes_size(spec)
    top_k = spec.get("top_k", DEFAULT_TOP_K)
    budget = spec.get("latency_budget_ms", DEFAULT_LATENCY_BUDGET_MS)
    queries = spec.get("queries", [])

    rows = []
    latencies = []
    searchapi_hits = 0
    inkeep_hits = 0
    inkeep_judged = 0

    for entry in queries:
        q = entry["q"]
        expected = entry.get("expect", [])
        inkeep_hit = entry.get("inkeep_hit", None)
        try:
            docs, latency = fetch(endpoint, q, "Documentation", docs_size, args.timeout)
            release_notes, _ = fetch(endpoint, q, "Documentation", changes, args.timeout, breadcrumb="changes")
        except Exception as e:  # noqa: BLE001 - report the failure in the row
            rows.append((q, None, "ERROR: %s" % e, inkeep_hit))
            continue

        # What the widget shows first: the top-k docs and the Changes group.
        shown = [d.get("url", "") for d in docs[:top_k]] + [c.get("url", "") for c in release_notes]
        hit = any(matches(url, expected) for url in shown)
        top_title = docs[0].get("title", "") if docs else "(no results)"

        latencies.append(latency)
        if hit:
            searchapi_hits += 1
        if inkeep_hit is not None:
            inkeep_judged += 1
            if inkeep_hit:
                inkeep_hits += 1
        rows.append((q, hit, top_title, inkeep_hit))

    total = len([r for r in rows if r[1] is not None])
    print("# Docs search relevance gate\n")
    print("Endpoint: `%s`  |  top-k: %d  |  latency budget: %d ms\n" % (endpoint, top_k, budget))
    print("| Query | /searchapi top-%d | Inkeep top-5 | Top result |" % top_k)
    print("|---|---|---|---|")
    for q, hit, top_title, inkeep_hit in rows:
        sa = "ERROR" if hit is None else ("hit" if hit else "miss")
        ink = "-" if inkeep_hit is None else ("hit" if inkeep_hit else "miss")
        note = "" if hit is None else top_title
        print("| %s | %s | %s | %s |" % (q, sa, ink, note))

    print("\n## Summary\n")
    if total:
        sa_rate = 100.0 * searchapi_hits / total
        p95 = percentile(latencies, 95)
        print("- /searchapi top-%d hit rate: **%.0f%%** (%d/%d)" % (top_k, sa_rate, searchapi_hits, total))
        print("- /searchapi p95 latency: **%.0f ms** (budget %d ms)" % (p95, budget))
        print("  (round-trip from this client, each request opening a new connection, so it overstates per-query server latency; confirm the budget from gateway logs or a client close to the cluster)")
        if inkeep_judged:
            ink_rate = 100.0 * inkeep_hits / inkeep_judged
            print("- Inkeep top-5 hit rate: **%.0f%%** (%d/%d judged)" % (ink_rate, inkeep_hits, inkeep_judged))
            passes = sa_rate >= ink_rate and p95 < budget
            print("\n**Verdict: %s** (hit rate %s Inkeep, p95 %s budget)" % (
                "PASS, phase 1 is enough" if passes else "phase 2 is warranted",
                ">=" if sa_rate >= ink_rate else "<",
                "<" if p95 < budget else ">=",
            ))
        else:
            print("- Inkeep: not judged yet (fill `inkeep_hit` in the query set, see README)")
    else:
        print("- No successful queries.")


if __name__ == "__main__":
    main()
