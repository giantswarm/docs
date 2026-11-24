"""A small client for HTTP embedding services.

The embedding model runs outside the search engine, in a CPU service the
gateway calls at search time. This module hides which service and which model
sit behind it, so scoring a different model is a change to models.json and not
to code. Two request shapes are supported:

- `ollama`: POST /api/embed with {"model", "input": [...]}, answered with
  {"embeddings": [[...]]}.
- `tei` (Text Embeddings Inference): POST /embed with {"inputs": [...]},
  answered with [[...]]. The model is fixed when the server starts, so `model`
  is ignored.

Standard library only. A model that needs a Python package can get its own
class with the same `embed_query` and `embed_pages` methods, and nothing
else in this directory changes.
"""
import json
import math
import urllib.error
import urllib.request

DEFAULT_QUERY_TEMPLATE = "{text}"
DEFAULT_DOCUMENT_TEMPLATE = "{title}\n{heading}\n{text}"
DEFAULT_BATCH_SIZE = 16
DEFAULT_MAX_CHARS = 3000


def truncate_and_normalize(vector, dimensions):
    """Cut a Matryoshka (MRL) embedding to its first `dimensions` values and rescale.

    MRL models put the most information in the leading values, so a prefix is a
    valid smaller embedding once it has unit length again. With dimensions None
    the vector is only rescaled.
    """
    if dimensions:
        if dimensions > len(vector):
            raise ValueError("cannot truncate a %d-dimension vector to %d" % (len(vector), dimensions))
        vector = vector[:dimensions]
    norm = math.sqrt(sum(v * v for v in vector))
    return [v / norm for v in vector] if norm else list(vector)


def _ollama(model, texts):
    return "/api/embed", {"model": model, "input": texts}, lambda data: data["embeddings"]


def _tei(model, texts):
    # truncate: a page longer than the model's window is cut, not rejected.
    return "/embed", {"inputs": texts, "normalize": True, "truncate": True}, lambda data: data


SHAPES = {"ollama": _ollama, "tei": _tei}


def post_json(url, body, timeout):
    """POST body as JSON and return the decoded response. A function so tests can replace it."""
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("POST %s -> %d: %s" % (url, e.code, e.read().decode("utf-8")[:500]))


class Embedder:
    """Embeds queries and pages through one HTTP endpoint.

    query_template and document_template wrap the text before it is sent.
    Models differ here: some expect an instruction before the query, some a
    "title: ... | text: ..." layout for documents. Documents may use {title},
    {heading} and {text}. Queries use {text}.
    """

    def __init__(self, shape, endpoint, model=None, dimensions=None,
                 query_template=DEFAULT_QUERY_TEMPLATE, document_template=DEFAULT_DOCUMENT_TEMPLATE,
                 batch_size=DEFAULT_BATCH_SIZE, max_chars=DEFAULT_MAX_CHARS, timeout=120.0):
        if shape not in SHAPES:
            raise ValueError("unknown shape %r, use one of %s" % (shape, ", ".join(sorted(SHAPES))))
        self.shape = shape
        self.endpoint = endpoint.rstrip("/")
        self.model = model
        self.dimensions = dimensions
        self.query_template = query_template
        self.document_template = document_template
        self.batch_size = batch_size
        self.max_chars = max_chars
        self.timeout = timeout

    @classmethod
    def from_config(cls, cfg):
        """Build an Embedder from one entry of models.json."""
        known = ("shape", "endpoint", "model", "dimensions", "query_template",
                 "document_template", "batch_size", "max_chars", "timeout")
        return cls(**{k: cfg[k] for k in known if cfg.get(k) is not None})

    def embed(self, texts):
        """Return one vector per text, truncated and normalised."""
        path, body, parse = SHAPES[self.shape](self.model, texts)
        vectors = parse(post_json(self.endpoint + path, body, self.timeout))
        if len(vectors) != len(texts):
            raise RuntimeError("sent %d texts, got %d vectors" % (len(texts), len(vectors)))
        return [truncate_and_normalize(v, self.dimensions) for v in vectors]

    def embed_query(self, query):
        return self.embed([self.query_template.format(text=query)])[0]

    def embed_pages(self, pages, progress=None):
        """Embed Page records in batches, in order."""
        texts = [self.document_text(p) for p in pages]
        vectors = []
        for i in range(0, len(texts), self.batch_size):
            vectors.extend(self.embed(texts[i:i + self.batch_size]))
            if progress:
                progress(len(vectors), len(texts))
        return vectors

    def document_text(self, page):
        text = self.document_template.format(title=page.title, heading=page.heading,
                                             text=page.text[:self.max_chars])
        # A list page has no questions, and some have no description, which would leave an empty line.
        return "\n".join(line for line in text.split("\n") if line.strip())
