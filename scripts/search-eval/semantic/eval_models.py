#!/usr/bin/env python3
"""Score candidate embedding models on the real docs query set.

This replaces ../semantic-poc, which ran the model inside OpenSearch (ML
Commons). Here the model runs in a separate HTTP service, the gateway embeds
the query and sends a plain `knn` clause, and the index holds one record per
H2/H3 section.

For each model in models.json the script splits the docs into sections,
embeds them through the model's endpoint, loads them into a throwaway
OpenSearch as `knn_vector`, then runs every query in ../queries.json three
ways: keyword (BM25), pure vector, and hybrid (the two rankings fused with
reciprocal rank fusion). It prints a Markdown report per model with the same
top-k hit rate and p95 latency rules as ../run.py.

A hit means an expected URL fragment appears in the URL of one of the top-k
distinct pages. Sections of the same page count once, so the numbers compare
with the page-level keyword gate.

Subcommands:

    python3 eval_models.py sections   # split the docs and print counts, needs nothing running
    python3 eval_models.py eval       # score the models in models.json

Standard library only. Never point this at the production sitesearch
OpenSearch, see the README.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from run import matches, percentile  # noqa: E402 - the phase 1 gate's scoring rules

from embed import Embedder  # noqa: E402
from sections import load_sections  # noqa: E402

DEFAULT_CONTENT = os.path.join(HERE, "..", "..", "..", "src", "content")
DEFAULT_QUERIES = os.path.join(HERE, "..", "queries.json")
DEFAULT_MODELS = os.path.join(HERE, "models.json")
DEFAULT_TOP_K = 5
DEFAULT_LATENCY_BUDGET_MS = 300
DEFAULT_CANDIDATES = 50
DEFAULT_RRF_K = 60
INDEX_PREFIX = "docs-sections-eval-"
SEARCH_FIELDS = ["title^2", "heading^3", "text"]
METHODS = ("keyword", "vector", "hybrid")


class OpenSearch:
    def __init__(self, scheme, host, port, timeout):
        self.base = "%s://%s:%d" % (scheme, host, port)
        self.timeout = timeout

    def req(self, method, path, body=None, ndjson=False):
        if ndjson:
            data, ctype = body.encode("utf-8"), "application/x-ndjson"
        else:
            data, ctype = (json.dumps(body).encode("utf-8") if body is not None else None), "application/json"
        r = urllib.request.Request(self.base + path, data=data, method=method, headers={"Content-Type": ctype})
        try:
            with urllib.request.urlopen(r, timeout=self.timeout) as resp:
                text = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            raise RuntimeError("%s %s -> %d: %s" % (method, path, e.code, e.read().decode("utf-8")[:500]))
        return json.loads(text) if text.strip() else {}


def refuse_production(host):
    """Production sitesearch has no authentication and holds the confidential intranet index."""
    if host.endswith("giantswarm.io"):
        sys.exit("refusing to run against %s, use a throwaway OpenSearch (see the README)" % host)


def index_name(model_name):
    return INDEX_PREFIX + "".join(c if c.isalnum() else "-" for c in model_name.lower())


def create_index(c, name, dimension):
    try:
        c.req("DELETE", "/" + name)  # so a re-run starts clean
    except RuntimeError:
        pass
    c.req("PUT", "/" + name, {
        "settings": {"index.knn": True, "number_of_shards": 1, "number_of_replicas": 0},
        "mappings": {"properties": {
            "embedding": {"type": "knn_vector", "dimension": dimension,
                          "method": {"name": "hnsw", "engine": "lucene", "space_type": "cosinesimil"}},
            "title": {"type": "text"}, "heading": {"type": "text"}, "text": {"type": "text"},
            "url": {"type": "keyword"}, "anchor": {"type": "keyword"}, "type": {"type": "keyword"},
        }},
    })


def bulk_index(c, name, sections, vectors, batch=200):
    for start in range(0, len(sections), batch):
        lines = []
        for i in range(start, min(start + batch, len(sections))):
            s = sections[i]
            lines.append(json.dumps({"index": {"_index": name, "_id": str(i)}}))
            lines.append(json.dumps({"title": s.title, "heading": s.heading, "text": s.text, "url": s.url,
                                     "anchor": s.anchor, "type": s.type, "embedding": vectors[i]}))
        res = c.req("POST", "/_bulk", "\n".join(lines) + "\n", ndjson=True)
        if res.get("errors"):
            failed = [it["index"]["error"] for it in res["items"] if it["index"].get("error")]
            raise RuntimeError("bulk index failed for %d records, first: %s" % (len(failed), failed[0]))
    c.req("POST", "/%s/_refresh" % name)


def search(c, name, query_clause, size):
    body = {"size": size, "_source": ["title", "heading", "url", "anchor"], "query": query_clause}
    resp = c.req("POST", "/%s/_search" % name, body)
    return [{"id": h["_id"], **h["_source"]} for h in resp.get("hits", {}).get("hits", [])]


def keyword_clause(query):
    return {"multi_match": {"query": query, "fields": SEARCH_FIELDS}}


def vector_clause(vector, k):
    return {"knn": {"embedding": {"vector": vector, "k": k}}}


def rrf(rankings, k=DEFAULT_RRF_K):
    """Fuse ranked id lists with reciprocal rank fusion. Return ids, best first.

    An id scores the sum of 1 / (k + rank) over the lists it appears in, with
    rank counted from 1. Ties keep the order of first appearance.
    """
    scores = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return sorted(scores, key=lambda d: -scores[d])


def top_pages(hits, top_k):
    """Return the URLs of the first top_k distinct pages in a list of section hits."""
    urls = []
    for h in hits:
        if h["url"] not in urls:
            urls.append(h["url"])
        if len(urls) == top_k:
            break
    return urls


def score_query(c, index, embedder, query, expected, top_k, candidates, rrf_k):
    """Run one query three ways. Return {method: (hit, top_url, latency_ms)} and the embed latency."""
    t0 = time.monotonic()
    kw = search(c, index, keyword_clause(query), candidates)
    kw_ms = (time.monotonic() - t0) * 1000

    t0 = time.monotonic()
    vector = embedder.embed_query(query)
    embed_ms = (time.monotonic() - t0) * 1000
    t0 = time.monotonic()
    vec = search(c, index, vector_clause(vector, candidates), candidates)
    vec_ms = embed_ms + (time.monotonic() - t0) * 1000

    # The hybrid cost is every step of it, run one after the other.
    by_id = {h["id"]: h for h in kw + vec}
    fused = [by_id[i] for i in rrf([[h["id"] for h in kw], [h["id"] for h in vec]], rrf_k)]
    hybrid_ms = kw_ms + vec_ms

    result = {}
    for method, hits, ms in (("keyword", kw, kw_ms), ("vector", vec, vec_ms), ("hybrid", fused, hybrid_ms)):
        pages = top_pages(hits, top_k)
        result[method] = (any(matches(u, expected) for u in pages), pages[0] if pages else "(no results)", ms)
    return result, embed_ms


def show_progress(done, total):
    if done == total or done % 400 == 0:
        print("  %d/%d" % (done, total), file=sys.stderr)


def score_model(c, cfg, sections, queries, top_k, candidates, rrf_k, keep_index):
    """Index the sections with one model and score every query. Return a result dict."""
    embedder = Embedder.from_config(cfg)
    name = index_name(cfg["name"])

    print("[%s] embedding %d sections..." % (cfg["name"], len(sections)), file=sys.stderr)
    t0 = time.monotonic()
    vectors = embedder.embed_sections(sections, progress=show_progress)
    embed_seconds = time.monotonic() - t0

    create_index(c, name, len(vectors[0]))
    bulk_index(c, name, sections, vectors)

    rows, latencies, embed_latencies = [], {m: [] for m in METHODS}, []
    hits = {m: 0 for m in METHODS}
    try:
        for entry in queries:
            try:
                result, embed_ms = score_query(c, name, embedder, entry["q"], entry.get("expect", []),
                                               top_k, candidates, rrf_k)
            except Exception as e:  # noqa: BLE001 - report the failure in the row
                rows.append((entry["q"], None, "ERROR: %s" % e))
                continue
            embed_latencies.append(embed_ms)
            for m in METHODS:
                hits[m] += 1 if result[m][0] else 0
                latencies[m].append(result[m][2])
            rows.append((entry["q"], {m: result[m][0] for m in METHODS}, result["hybrid"][1]))
    finally:
        if not keep_index:
            try:
                c.req("DELETE", "/" + name)
            except RuntimeError as e:
                print("could not delete %s: %s" % (name, e), file=sys.stderr)

    return {"name": cfg["name"], "dimension": len(vectors[0]),
            "rows": rows, "hits": hits, "total": len([r for r in rows if r[1] is not None]),
            "p95": {m: percentile(latencies[m], 95) for m in METHODS},
            "embed_p95": percentile(embed_latencies, 95), "embed_seconds": embed_seconds}


def format_report(result, sections, top_k, budget):
    """Return the Markdown report for one model."""
    pages = len({s.url for s in sections})
    lines = ["## %s\n" % result["name"],
             "%d-dimension vectors, %d sections from %d pages, embedded in %.0f s  |  top-k: %d  |  latency budget: %d ms\n"
             % (result["dimension"], len(sections), pages, result["embed_seconds"], top_k, budget),
             "| Query | keyword | vector | hybrid | Top hybrid page |", "|---|---|---|---|---|"]
    for q, hit, top in result["rows"]:
        if hit is None:
            lines.append("| %s | ERROR | ERROR | ERROR | %s |" % (q, top))
        else:
            lines.append("| %s | %s | %s | %s | %s |" % (
                q, *("hit" if hit[m] else "miss" for m in METHODS), top))
    total = result["total"]
    lines.append("\n### Summary\n")
    if not total:
        return "\n".join(lines + ["- No successful queries."])
    for m in METHODS:
        lines.append("- %s top-%d hit rate: **%.0f%%** (%d/%d), p95 latency **%.0f ms**%s" % (
            m, top_k, 100.0 * result["hits"][m] / total, result["hits"][m], total, result["p95"][m],
            "" if result["p95"][m] < budget else " (over budget)"))
    lines.append("- Query embedding p95: **%.0f ms** (included in vector and hybrid)" % result["embed_p95"])
    lines.append("  (round-trip from this client, requests one after the other, so hybrid is the sum of its parts)")
    return "\n".join(lines)


def format_comparison(results, top_k):
    """Return a Markdown table with one row per model."""
    lines = ["## Comparison\n",
             "| Model | Dimensions | keyword | vector | hybrid | p95 vector (ms) | p95 hybrid (ms) |",
             "|---|---|---|---|---|---|---|"]
    for r in results:
        t = r["total"] or 1
        lines.append("| %s | %d | %s | %s | %s | %.0f | %.0f |" % (
            r["name"], r["dimension"],
            *("%d/%d (%.0f%%)" % (r["hits"][m], r["total"], 100.0 * r["hits"][m] / t) for m in METHODS),
            r["p95"]["vector"], r["p95"]["hybrid"]))
    return "\n".join(lines)


def cmd_sections(args):
    sections = load_sections(args.content)
    pages = {s.url for s in sections}
    with_anchor = [s for s in sections if s.anchor]
    print("%d sections from %d pages (%d with an anchor)" % (len(sections), len(pages), len(with_anchor)))
    lengths = sorted(len(s.text) for s in sections)
    if lengths:
        print("text length in characters: median %d, p95 %d, max %d" % (
            lengths[len(lengths) // 2], percentile(lengths, 95), lengths[-1]))


def cmd_eval(args):
    refuse_production(args.host)
    with open(args.queries, encoding="utf-8") as f:
        spec = json.load(f)
    with open(args.models, encoding="utf-8") as f:
        models = json.load(f)["models"]
    if args.only:
        models = [m for m in models if m["name"] in args.only]
        if not models:
            sys.exit("no model in %s matches --only" % args.models)

    top_k = spec.get("top_k", DEFAULT_TOP_K)
    budget = spec.get("latency_budget_ms", DEFAULT_LATENCY_BUDGET_MS)
    sections = load_sections(args.content)
    c = OpenSearch(args.scheme, args.host, args.port, args.timeout)

    results = []
    print("# Semantic search model scoring\n")
    print("Queries: %d from `%s`\n" % (len(spec["queries"]), os.path.basename(args.queries)))
    for cfg in models:
        result = score_model(c, cfg, sections, spec["queries"], top_k, args.candidates, args.rrf_k, args.keep_index)
        results.append(result)
        print(format_report(result, sections, top_k, budget) + "\n")
    if len(results) > 1:
        print(format_comparison(results, top_k))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["sections", "eval"])
    ap.add_argument("--content", default=DEFAULT_CONTENT, help="path to src/content")
    ap.add_argument("--queries", default=DEFAULT_QUERIES, help="path to the query set JSON")
    ap.add_argument("--models", default=DEFAULT_MODELS, help="path to the model list JSON")
    ap.add_argument("--only", nargs="+", help="score only the models with these names")
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=9200)
    ap.add_argument("--scheme", default="http", choices=["http", "https"])
    ap.add_argument("--candidates", type=int, default=DEFAULT_CANDIDATES,
                    help="sections fetched per ranking before they are fused and grouped into pages")
    ap.add_argument("--rrf-k", type=int, default=DEFAULT_RRF_K, help="rank constant of reciprocal rank fusion")
    ap.add_argument("--keep-index", action="store_true", help="leave each model's index in place after scoring")
    ap.add_argument("--timeout", type=float, default=120.0)
    args = ap.parse_args()

    {"sections": cmd_sections, "eval": cmd_eval}[args.command](args)


if __name__ == "__main__":
    main()
