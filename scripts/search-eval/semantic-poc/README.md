# Semantic search PoC

> Superseded by [`../semantic`](../semantic/README.md). That harness scores
> embedding models under the chosen architecture, with the model in an external
> service and section-level records. This directory stays as the record of the
> ML Commons proof of concept.

Checks whether semantic (vector) search finds the right page where keyword
search struggles, especially for reworded or synonym queries. This is the
phase 2 shape from the plan: the small embedding model (`all-MiniLM-L6-v2`)
runs inside OpenSearch (ML Commons), a vector index sits next to the keyword
index, and search can be keyword, neural (pure vector) or hybrid (both).

`setup_and_eval.py` is only HTTP calls to OpenSearch, so it needs no Python
packages and runs on any Python 3. The model runs in the cluster, not locally.

## Run it against a throwaway OpenSearch, not production sitesearch

> This registers and loads a model, changes `plugins.ml_commons` cluster
> settings, and creates an index and pipelines. Production sitesearch has no
> authentication and holds the confidential `intranet` index on the same node,
> so do not run this there. Use a disposable OpenSearch (a local container or a
> dev cluster) with a copy or a sample of the docs content.

A quick local OpenSearch for the PoC:

```sh
docker run -d --name os-poc -p 9200:9200 \
  -e discovery.type=single-node \
  -e DISABLE_SECURITY_PLUGIN=true \
  opensearchproject/opensearch:2.19.0
```

`DISABLE_SECURITY_PLUGIN=true` turns off authentication and TLS, so the PoC
reaches it over plain HTTP on `localhost:9200` with no credentials, which is
what `setup_and_eval.py` expects. If the model step runs out of memory, give
Docker more, or add `-e OPENSEARCH_JAVA_OPTS="-Xms2g -Xmx2g"`.

The cluster needs outbound internet to download the pretrained model from the
OpenSearch model repository the first time. Production would host a pinned copy
instead (see the plan's phase 2 notes).

## Steps

```sh
# 1. Load the docs content into a 'docs' index in the PoC cluster
#    (reads this repo's src/content, ~4500 pages):
python3 load_corpus.py --host localhost --port 9200

# 2. Register + deploy the model, build the vector index, index a sample,
#    then compare keyword / neural / hybrid on the synonym set:
python3 setup_and_eval.py all --host localhost --port 9200 --sample 1000

#    Or run the phases separately:
python3 setup_and_eval.py setup --sample 1000
python3 setup_and_eval.py eval

# 3. Remove everything the PoC created (the model, index and pipelines):
python3 setup_and_eval.py cleanup
```

`load_corpus.py` derives each page's URL from its file path, which approximates
the real site well enough to judge relevance. If you already have an OpenSearch
with the docs content indexed, skip step 1 and point `--source-index` at it.

`setup` saves the model id to `poc-state.json`, which `eval` and `cleanup` read.

## Reading the result

`eval` prints a per-query table and a summary with the hit rate for each of
keyword, neural and hybrid over the reworded queries in `synonyms.json`. The
signal to look for:

- **hybrid clearly above keyword** means semantic search helps on synonyms, so
  phase 2 would be worth building.
- **hybrid close to keyword** means the reworded queries already work on
  keywords, so phase 2 buys little.

Compare this with the keyword gate in the parent directory, which ran the real
top queries and reached 91% on keyword alone.

## What this PoC simplifies

- It embeds one vector per page (title + description + body), not one per
  section split at H2/H3 as the real phase 2 would. Section records usually
  help precision, so this is a floor, not a ceiling.
- It combines scores with min-max normalization. The plan also considers the
  RRF `score-ranker-processor` (OpenSearch 2.19+); swap the search pipeline to
  compare.
- It runs the model on data nodes and samples a subset of pages. Production
  sizing and a dedicated setup are separate questions in the plan.

The query set in `synonyms.json` is reworded on purpose so the wording differs
from the page it should find. Edit it to add your own cases.
