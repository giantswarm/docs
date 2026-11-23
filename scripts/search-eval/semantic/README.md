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
different architecture and page-level vectors, and this harness would
overwrite its scripts and findings.

## Run it

> Use a throwaway OpenSearch. This creates and deletes indices named
> `docs-sections-eval-*`. Production sitesearch has no authentication and holds
> the confidential `intranet` index on the same node, so never point this at
> it. The script refuses hosts under `giantswarm.io`.

Start a disposable OpenSearch and an embedding service. For OpenSearch, see the
Docker command in the [proof of concept README](../semantic-poc/README.md). For
the embedding service, run Ollama (`ollama pull embeddinggemma`) or a Text
Embeddings Inference container, and set its URL in `models.json`.

```sh
python3 eval_models.py sections                 # split the docs, print counts, needs no services
python3 eval_models.py eval                     # score every model in models.json
python3 eval_models.py eval --only bge-m3       # score one model
```

No dependencies beyond the Python standard library. `eval` prints a Markdown
report per model and a comparison table. Run the unit tests with:

```sh
python3 -m unittest discover -s tests
```

## What it does

1. `sections.py` splits each page under `src/content` at H2 and H3. Every
   record carries title, heading, anchor, URL, type and text. `/changes` is
   skipped.
2. `embed.py` sends the sections to the model's HTTP endpoint in batches. It
   supports the Ollama (`/api/embed`) and Text Embeddings Inference (`/embed`)
   request shapes, and can cut a Matryoshka embedding to fewer dimensions and
   renormalise it, for example to 512.
3. `eval_models.py` loads the vectors into an OpenSearch index as
   `knn_vector`, then runs each query in `../queries.json` three ways: keyword
   (BM25), pure vector (`knn`) and hybrid (both rankings fused with reciprocal
   rank fusion, in the client).
4. It reports the top-k hit rate and p95 latency with the rules of
   [`../run.py`](../run.py), which it imports. A hit means an expected URL
   fragment appears in the top k distinct pages. Sections of one page count
   once, so the numbers compare with the keyword gate's 29 of 32.

## Changing the model list

`models.json` lists one entry per model and size. A model is swapped by
editing this file, not code. Each entry sets:

- `shape`: `ollama` or `tei`.
- `endpoint` and `model`. A TEI server fixes its model at start, so `model` is
  ignored there.
- `dimensions`: the size to index. Leave it out for the full vector.
- `query_template` and `document_template`: the text wrapped around queries
  and sections. Models differ here, for example EmbeddingGemma wants a task
  prefix. Documents can use `{title}`, `{heading}` and `{text}`.

A model that needs a Python package gets its own class with the same
`embed_query` and `embed_sections` methods. Keep the package import inside
that class so the rest stays dependency-free.

## Anchors

`anchors.py` reproduces the heading ids that Hugo renders, so a result can
link to `/page/#anchor`. The rules are in the module docstring, and
`tests/test_anchors.py` checks them against ids that Hugo 0.163 rendered for
real pages in this repo. docs-indexer needs the same logic and can port or
call this module.

Known gaps in the anchors and the splitter:

- Setext headings (underlined with `===`) are not recognised. No page uses them.
- A heading with nested square brackets inside a link, such as
  `[a [b] c](url)`, gets a different id in Hugo than here.
- Headings inside `details` and `tab` shortcodes are ignored. Hugo renders
  their inner Markdown on its own, so their ids can repeat across the page.
- Headings that a layout generates (the CRD reference pages) are not in the
  Markdown, so they are not split.

## What is simplified

- Keyword search here is BM25 over sections with the standard analyzer. The
  production gateway searches pages, so its 91% is the reference and not an
  exact baseline for this column.
- Hybrid uses client-side RRF. Production may use OpenSearch's score ranker
  instead, which gives the same ranking idea but is not the same code.
- Latency is a client round trip, one request after the other, like `run.py`.
  Hybrid is the sum of the keyword search, the query embedding and the vector
  search.
- The text is plain text made from the Markdown by regexes, not rendered HTML.
