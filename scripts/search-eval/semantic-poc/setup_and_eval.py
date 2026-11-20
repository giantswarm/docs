#!/usr/bin/env python3
"""Semantic search PoC against OpenSearch (sitesearch), the phase 2 shape.

Stands up a vector index next to the existing keyword index, registers the
small embedding model the plan picks (all-MiniLM-L6-v2) in ML Commons, indexes
a sample of docs pages with their embeddings, and compares keyword, neural
(pure vector) and hybrid (keyword + vector) search on a set of reworded /
synonym queries. The point is to see whether semantic search finds the right
page where keyword search struggles.

The embedding model runs inside OpenSearch, so this script is only HTTP calls.
No Python dependencies beyond the standard library.

Typical run (with a port-forward to sitesearch on localhost:9200):

    python3 setup_and_eval.py all --host localhost --port 9200

Subcommands: setup, eval, cleanup, all. State (the model id) is kept in
poc-state.json next to this script so eval and cleanup can find it.

This is a throwaway PoC. It creates an index, two pipelines and a deployed
model, all named *-poc; `cleanup` removes them. It does not touch the existing
docs/blog/intranet indices (it only reads the source index during reindex).
"""
import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request

MODEL_NAME = "huggingface/sentence-transformers/all-MiniLM-L6-v2"
MODEL_VERSION = "1.0.1"
MODEL_FORMAT = "TORCH_SCRIPT"
DIMENSION = 384  # all-MiniLM-L6-v2 output size

INDEX = "docs-hybrid-poc"
INGEST_PIPELINE = "docs-embed-poc"
SEARCH_PIPELINE = "docs-hybrid-poc"
MODEL_GROUP = "docs-search-poc"

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poc-state.json")
SYNONYMS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synonyms.json")

# Fields pulled from the source keyword index and embedded. The source index may
# name its body field "body" or "text"; both are tried, missing ones render empty.
SOURCE_FIELDS = ["title", "description", "body", "text", "url", "type", "breadcrumb"]
MATCH_FIELDS = ["title^3", "description", "body", "text"]


class Client:
    def __init__(self, scheme, host, port, timeout):
        self.base = "%s://%s:%d" % (scheme, host, port)
        self.timeout = timeout

    def req(self, method, path, body=None):
        url = self.base + path
        data = json.dumps(body).encode("utf-8") if body is not None else None
        r = urllib.request.Request(url, data=data, method=method,
                                   headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(r, timeout=self.timeout) as resp:
                text = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            raise RuntimeError("%s %s -> %d: %s" % (method, path, e.code, e.read().decode("utf-8")[:500]))
        return json.loads(text) if text.strip() else {}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def load_state():
    with open(STATE_FILE, encoding="utf-8") as f:
        return json.load(f)


def poll_task(c, task_id, what):
    for _ in range(120):  # up to ~4 minutes
        task = c.req("GET", "/_plugins/_ml/tasks/" + task_id)
        state = task.get("state")
        if state == "COMPLETED":
            return task
        if state in ("FAILED", "COMPLETED_WITH_ERROR"):
            raise RuntimeError("%s failed: %s" % (what, json.dumps(task)))
        print("  ...%s: %s" % (what, state))
        time.sleep(2)
    raise RuntimeError("%s timed out" % what)


def ensure_model_group(c):
    """Return the model group id, reusing an existing group with the same name."""
    try:
        mg = c.req("POST", "/_plugins/_ml/model_groups/_register",
                   {"name": MODEL_GROUP, "description": "Docs search semantic PoC"})
        return mg["model_group_id"]
    except RuntimeError as e:
        # A group with this name already exists; its id is in the error message.
        m = re.search(r"model group with ID:\s*([A-Za-z0-9_-]+)", str(e))
        if m:
            print("  reusing existing model group %s" % m.group(1))
            return m.group(1)
        raise


def setup(c, source_index, sample):
    print("Allowing ML to run on data nodes (PoC cluster settings)...")
    c.req("PUT", "/_cluster/settings", {"persistent": {
        "plugins.ml_commons.only_run_on_ml_node": False,
        "plugins.ml_commons.model_access_control_enabled": False,
        "plugins.ml_commons.native_memory_threshold": 99,
    }})

    # Reuse an already-deployed model from a previous run, so re-running setup
    # to rebuild the index does not re-download the model.
    model_id = None
    group_id = None
    if os.path.exists(STATE_FILE):
        prev = load_state()
        mid = prev.get("model_id")
        if mid:
            try:
                info = c.req("GET", "/_plugins/_ml/models/" + mid)
                if info.get("model_state") == "DEPLOYED":
                    model_id, group_id = mid, prev.get("model_group_id")
                    print("Reusing deployed model %s" % model_id)
            except Exception:
                pass

    if not model_id:
        print("Ensuring the model group...")
        group_id = ensure_model_group(c)

        print("Registering the embedding model (%s)..." % MODEL_NAME)
        reg = c.req("POST", "/_plugins/_ml/models/_register", {
            "name": MODEL_NAME, "version": MODEL_VERSION,
            "model_group_id": group_id, "model_format": MODEL_FORMAT,
        })
        task = poll_task(c, reg["task_id"], "model register")
        model_id = task["model_id"]
        print("  model_id: %s" % model_id)

        print("Deploying the model...")
        dep = c.req("POST", "/_plugins/_ml/models/%s/_deploy" % model_id)
        poll_task(c, dep["task_id"], "model deploy")

    print("Creating the ingest pipeline...")
    c.req("PUT", "/_ingest/pipeline/" + INGEST_PIPELINE, {
        "description": "Embed docs pages for the semantic PoC",
        "processors": [
            {"set": {"field": "embed_text",
                     "value": "{{{title}}} {{{description}}} {{{body}}} {{{text}}}"}},
            {"text_embedding": {"model_id": model_id,
                                "field_map": {"embed_text": "content_embedding"}}},
        ],
    })

    print("Creating the k-NN index...")
    try:
        c.req("DELETE", "/" + INDEX)  # so a re-run rebuilds the index cleanly
    except Exception:
        pass
    c.req("PUT", "/" + INDEX, {
        "settings": {"index.knn": True, "default_pipeline": INGEST_PIPELINE},
        "mappings": {"properties": {
            "content_embedding": {"type": "knn_vector", "dimension": DIMENSION,
                                  "method": {"name": "hnsw", "engine": "lucene",
                                             "space_type": "cosinesimil"}},
            "embed_text": {"type": "text"},
            "title": {"type": "text"}, "description": {"type": "text"},
            "body": {"type": "text"}, "text": {"type": "text"},
            "url": {"type": "keyword"}, "type": {"type": "keyword"},
        }},
    })

    print("Reindexing up to %d docs from '%s' (embeddings computed on ingest)..." % (sample, source_index))
    res = c.req("POST", "/_reindex?wait_for_completion=true&requests_per_second=-1", {
        "max_docs": sample,
        "source": {"index": source_index, "_source": SOURCE_FIELDS},
        "dest": {"index": INDEX},
    })
    print("  indexed: %s, failures: %s" % (res.get("created", "?"), len(res.get("failures", []))))
    c.req("POST", "/%s/_refresh" % INDEX)

    print("Creating the hybrid search pipeline (min-max normalization)...")
    c.req("PUT", "/_search/pipeline/" + SEARCH_PIPELINE, {
        "description": "Normalize and combine keyword and neural scores",
        "phase_results_processors": [{"normalization-processor": {
            "normalization": {"technique": "min_max"},
            "combination": {"technique": "arithmetic_mean",
                            "parameters": {"weights": [0.3, 0.7]}},
        }}],
    })

    save_state({"model_id": model_id, "model_group_id": group_id})
    print("Setup done. model_id saved to poc-state.json.")


def hits(resp, top_k):
    return [h.get("_source", {}).get("url", "") for h in resp.get("hits", {}).get("hits", [])[:top_k]]


def is_hit(urls, expect):
    return any(frag and frag in url for url in urls for frag in expect)


def eval_(c, top_k):
    model_id = load_state()["model_id"]
    with open(SYNONYMS_FILE, encoding="utf-8") as f:
        spec = json.load(f)
    top_k = spec.get("top_k", top_k)
    queries = spec["queries"]

    counts = {"keyword": 0, "neural": 0, "hybrid": 0}
    print("\n# Semantic search PoC: keyword vs neural vs hybrid (top-%d)\n" % top_k)
    print("| Query | keyword | neural | hybrid |")
    print("|---|---|---|---|")
    for entry in queries:
        q, expect = entry["q"], entry.get("expect", [])

        kw = c.req("POST", "/%s/_search" % INDEX, {
            "size": top_k, "_source": ["title", "url"],
            "query": {"multi_match": {"query": q, "fields": MATCH_FIELDS}},
        })
        ne = c.req("POST", "/%s/_search" % INDEX, {
            "size": top_k, "_source": ["title", "url"],
            "query": {"neural": {"content_embedding": {
                "query_text": q, "model_id": model_id, "k": top_k}}},
        })
        hy = c.req("POST", "/%s/_search?search_pipeline=%s" % (INDEX, SEARCH_PIPELINE), {
            "size": top_k, "_source": ["title", "url"],
            "query": {"hybrid": {"queries": [
                {"multi_match": {"query": q, "fields": MATCH_FIELDS}},
                {"neural": {"content_embedding": {
                    "query_text": q, "model_id": model_id, "k": top_k}}},
            ]}},
        })

        r = {"keyword": is_hit(hits(kw, top_k), expect),
             "neural": is_hit(hits(ne, top_k), expect),
             "hybrid": is_hit(hits(hy, top_k), expect)}
        for k, v in r.items():
            counts[k] += 1 if v else 0
        print("| %s | %s | %s | %s |" % (
            q, "hit" if r["keyword"] else "miss",
            "hit" if r["neural"] else "miss", "hit" if r["hybrid"] else "miss"))

    n = len(queries)
    print("\n## Summary (%d reworded queries)\n" % n)
    for k in ("keyword", "neural", "hybrid"):
        print("- %-8s hit rate: %d/%d (%.0f%%)" % (k, counts[k], n, 100.0 * counts[k] / n))


def inspect(c, query, top_k):
    """Print the top results of each method for one query, to debug a miss."""
    model_id = load_state()["model_id"]

    def show(name, body, suffix=""):
        resp = c.req("POST", "/%s/_search%s" % (INDEX, suffix), body)
        print("\n[%s]" % name)
        for h in resp.get("hits", {}).get("hits", [])[:top_k]:
            s = h.get("_source", {})
            print("  %-55s %s" % ((s.get("title", "") or "")[:55], s.get("url", "")))

    print("# inspect: %s" % query)
    show("keyword", {"size": top_k, "_source": ["title", "url"],
                     "query": {"multi_match": {"query": query, "fields": MATCH_FIELDS}}})
    show("neural", {"size": top_k, "_source": ["title", "url"],
                    "query": {"neural": {"content_embedding": {
                        "query_text": query, "model_id": model_id, "k": top_k}}}})
    show("hybrid", {"size": top_k, "_source": ["title", "url"],
                    "query": {"hybrid": {"queries": [
                        {"multi_match": {"query": query, "fields": MATCH_FIELDS}},
                        {"neural": {"content_embedding": {
                            "query_text": query, "model_id": model_id, "k": top_k}}}]}}},
         suffix="?search_pipeline=" + SEARCH_PIPELINE)


def cleanup(c):
    state = {}
    try:
        state = load_state()
    except Exception:
        pass
    for method, path in [("DELETE", "/" + INDEX),
                         ("DELETE", "/_ingest/pipeline/" + INGEST_PIPELINE),
                         ("DELETE", "/_search/pipeline/" + SEARCH_PIPELINE)]:
        try:
            c.req(method, path)
            print("deleted %s" % path)
        except Exception as e:
            print("skip %s (%s)" % (path, e))
    model_id = state.get("model_id")
    if model_id:
        for method, path in [("POST", "/_plugins/_ml/models/%s/_undeploy" % model_id),
                             ("DELETE", "/_plugins/_ml/models/" + model_id)]:
            try:
                c.req(method, path)
                print("%s %s" % (method, path))
            except Exception as e:
                print("skip %s (%s)" % (path, e))
    group_id = state.get("model_group_id")
    if group_id:
        try:
            c.req("DELETE", "/_plugins/_ml/model_groups/" + group_id)
            print("deleted model group %s" % group_id)
        except Exception as e:
            print("skip model group (%s)" % e)
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["setup", "eval", "inspect", "cleanup", "all"])
    ap.add_argument("--query", default="", help="query string for the inspect command")
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=9200)
    ap.add_argument("--scheme", default="http", choices=["http", "https"])
    ap.add_argument("--source-index", default="docs", help="existing keyword index to sample from")
    ap.add_argument("--sample", type=int, default=10000,
                    help="max docs to index for the PoC (default covers the whole corpus)")
    ap.add_argument("--top-k", type=int, default=5)
    ap.add_argument("--timeout", type=float, default=120.0)
    args = ap.parse_args()

    c = Client(args.scheme, args.host, args.port, args.timeout)
    if args.command in ("setup", "all"):
        setup(c, args.source_index, args.sample)
    if args.command in ("eval", "all"):
        eval_(c, args.top_k)
    if args.command == "inspect":
        inspect(c, args.query, args.top_k)
    if args.command == "cleanup":
        cleanup(c)


if __name__ == "__main__":
    main()
