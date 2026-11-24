# Semantic search model scoring

Phase 2 of the docs search adds semantic search. This directory scores
candidate embedding models on the real query set, so the model is chosen by
measurement. It replaces [`../semantic-poc`](../semantic-poc/README.md), which
ran the model inside OpenSearch (ML Commons). That design is dropped. The
embedding model now runs in a small separate CPU service, the gateway embeds
the query at search time and sends a plain `knn` clause. There is no ML
Commons, no neural clause and no stored search template.

The proof of concept stays as the record of the 87% neural and hybrid against
53% keyword result. It is a separate directory because that result came from a
different architecture, and this harness would overwrite its scripts and
findings.

## One record per page

Each page is embedded as one record, built from its front matter only: the
title, the description and the `user_questions`, on three lines. The body is
not read.

Section-level records were tried first and dropped. Most headings in these
docs are scaffolding (`Prerequisites`, `Usage`, `Flags`), so they would give
near-identical vectors on hundreds of pages. The pages also already carry
hand-written text shaped like a search query. 268 of the 303 pages outside
`/changes` have a `user_questions` list, for example "How do I configure and
provision my first workload cluster?". Embedding those compares a query with
a query, which is an easier problem than comparing a query with body text.

The other 35 pages are list pages with front matter only. They get the title
and the description. `/changes` release notes are left out, and a result links
to the page, as in phase 1.

## Run it

> Use a throwaway OpenSearch. This creates and deletes indices named
> `docs-pages-eval-*`. Production sitesearch has no authentication and holds
> the confidential `intranet` index on the same node, so never point the
> OpenSearch client at it. The script refuses hosts under `giantswarm.io`.
>
> The only production call is the keyword leg, a read-only GET to
> `/searchapi` that is the same request the search widget and `run.py` send.
> It creates and changes nothing.

Start a disposable OpenSearch and an embedding service. For OpenSearch, see the
Docker command in the [proof of concept README](../semantic-poc/README.md). For
the embedding service, run Ollama (`ollama pull embeddinggemma`) or a Text
Embeddings Inference container, and set its URL in `models.json`.

```sh
python3 eval_models.py corpus                   # build the page records, print counts, needs no services
python3 eval_models.py eval                     # score every model in models.json, keyword from the live gateway
python3 eval_models.py eval --keyword local     # offline: BM25 over front matter, not the baseline
python3 eval_models.py eval --only bge-m3       # score one model
```

No dependencies beyond the Python standard library. `eval` prints a Markdown
report per model and a comparison table. Run the unit tests with:

```sh
python3 -m unittest discover -s tests
```

## What it does

1. `corpus.py` reads the front matter of every page under `src/content` and
   builds one record per page. The questions are joined with a space, since
   each ends in a question mark.
2. `embed.py` sends the records to the model's HTTP endpoint in batches. It
   supports the Ollama (`/api/embed`) and Text Embeddings Inference (`/embed`)
   request shapes, and can cut a Matryoshka embedding to fewer dimensions and
   renormalise it, for example to 512.
3. `eval_models.py` loads the vectors into a local OpenSearch index as
   `knn_vector`, then runs each query in `../queries.json` three ways:
   - keyword: the live `/searchapi` gateway, using `run.py`'s own client.
     This is the real phase 1 system over full page bodies, the system that
     scored 29 of 32. It is the baseline.
   - vector: a plain `knn` clause on the local index.
   - hybrid: the two rankings fused with reciprocal rank fusion (k=60), in
     the client.
4. It reports the top-k hit rate and p95 latency with the rules of
   [`../run.py`](../run.py), which it imports. A hit means an expected URL
   fragment appears in the top k pages. Like `run.py` and the widget, keyword
   and hybrid also count the blog results the gateway returns. Vector does not,
   since no blog is embedded.

The local index holds only front matter, so a keyword search over it would
compare front matter with front matter and flatter the vector leg. That is why
the keyword column comes from the gateway. `--keyword local` runs BM25 over the
local index for offline work. The report labels it "NOT the baseline", and it
must not be read as one.

## Reading the results

Several queries in `queries.json` are single words (`gpu`, `zot`, `dex`,
`karp`). They are keyword-shaped, not question-shaped, so expect the vector leg
to help little on them. Hybrid is what protects them, because the gateway's
keyword ranking stays in the fusion. `karp` is now served by prefix matching
that shipped in giantswarm/docs-proxy#347 and giantswarm/docs-indexer#638, so
it no longer separates the legs the way it did when the 29 of 32 was measured.

## Changing the model list

`models.json` lists one entry per model and size. A model is swapped by
editing this file, not code. Each entry sets:

- `shape`: `ollama` or `tei`.
- `endpoint` and `model`. A TEI server fixes its model at start, so `model` is
  ignored there.
- `dimensions`: the size to index. Leave it out for the full vector.
- `query_template` and `document_template`: the text wrapped around queries
  and pages. Models differ here, for example EmbeddingGemma wants a task
  prefix. The templates keep the names `{title}`, `{heading}` and `{text}`.
  For a page, `{heading}` is the description and `{text}` is the questions.

A model that needs a Python package gets its own class with the same
`embed_query` and `embed_pages` methods. Keep the package import inside
that class so the rest stays dependency-free.

## What is simplified

- The gateway's keyword latency is a round trip to the public site, so it
  overstates what the gateway sees. The gateway returns a limited number of
  results per query, which may be fewer than `--candidates`, and then RRF fuses
  a shorter keyword list. Gateway URLs are reduced to their path (no host, no
  fragment, trailing slash) to line up with the local index.
- Hybrid uses client-side RRF over the gateway's docs ranking and the vector ranking. Production may use OpenSearch's score ranker
  instead, which gives the same ranking idea but is not the same code.
- Latency is a client round trip, one request after the other, like `run.py`.
  Hybrid is the sum of the keyword search, the query embedding and the vector
  search.
- The front matter parser reads the flat keys this repo uses (plain, quoted
  and block scalars, and `- item` lists). It is not a general YAML parser.
