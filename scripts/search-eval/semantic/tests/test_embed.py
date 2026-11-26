import math
import unittest
from unittest import mock

import support  # noqa: F401 - sets up the import path
import embed
from embed import Embedder, truncate_and_normalize
from corpus import Page


def norm(v):
    return math.sqrt(sum(x * x for x in v))


class TestTruncate(unittest.TestCase):
    def test_keeps_the_prefix_and_rescales_to_unit_length(self):
        out = truncate_and_normalize([3.0, 4.0, 12.0, 84.0], 2)
        self.assertEqual(len(out), 2)
        self.assertAlmostEqual(out[0], 0.6)
        self.assertAlmostEqual(out[1], 0.8)

    def test_without_dimensions_only_rescales(self):
        out = truncate_and_normalize([3.0, 4.0], None)
        self.assertAlmostEqual(norm(out), 1.0)

    def test_zero_vector_is_returned_as_is(self):
        self.assertEqual(truncate_and_normalize([0.0, 0.0, 0.0], 2), [0.0, 0.0])

    def test_cannot_grow_a_vector(self):
        with self.assertRaises(ValueError):
            truncate_and_normalize([1.0, 2.0], 4)


class TestEmbedder(unittest.TestCase):
    def page(self, description="Install it.", questions=("How?",)):
        return Page("Guide", description, list(questions), "/g/", "Documentation")

    def test_ollama_request_and_response_shape(self):
        e = Embedder("ollama", "http://host:11434/", model="m", dimensions=2)
        with mock.patch.object(embed, "post_json", return_value={"embeddings": [[3.0, 4.0, 9.0]]}) as post:
            vector = e.embed_query("hello")
        post.assert_called_once_with("http://host:11434/api/embed", {"model": "m", "input": ["hello"]}, 120.0)
        self.assertAlmostEqual(vector[0], 0.6)
        self.assertEqual(len(vector), 2)

    def test_tei_request_and_response_shape(self):
        e = Embedder("tei", "http://tei:8080", model="ignored")
        with mock.patch.object(embed, "post_json", return_value=[[1.0, 0.0]]) as post:
            vector = e.embed_query("hello")
        post.assert_called_once_with(
            "http://tei:8080/embed", {"inputs": ["hello"], "normalize": True, "truncate": True}, 120.0)
        self.assertEqual(vector, [1.0, 0.0])

    def test_query_template_wraps_the_query(self):
        e = Embedder("tei", "http://x", query_template="Query: {text}")
        with mock.patch.object(embed, "post_json", return_value=[[1.0]]) as post:
            e.embed_query("login")
        self.assertEqual(post.call_args[0][1]["inputs"], ["Query: login"])

    def test_pages_go_in_batches_and_keep_their_order(self):
        e = Embedder("tei", "http://x", batch_size=2, document_template="{title}|{heading}|{text}")
        pages = [self.page(description="", questions=[str(i)]) for i in range(5)]
        calls = []

        def fake(url, body, timeout):
            calls.append(body["inputs"])
            return [[float(t.rsplit("|", 1)[1]), 1.0] for t in body["inputs"]]

        seen = []
        with mock.patch.object(embed, "post_json", side_effect=fake):
            vectors = e.embed_pages(pages, progress=lambda done, total: seen.append((done, total)))
        self.assertEqual([len(c) for c in calls], [2, 2, 1])
        self.assertEqual(seen, [(2, 5), (4, 5), (5, 5)])
        self.assertEqual([round(v[0] / v[1]) for v in vectors], [0, 1, 2, 3, 4])

    def test_document_text_is_title_description_and_questions_on_three_lines(self):
        e = Embedder("tei", "http://x")
        page = self.page("Install it.", ["How do I install?", "Where is it?"])
        self.assertEqual(e.document_text(page), "Guide\nInstall it.\nHow do I install? Where is it?")

    def test_document_text_skips_an_empty_description_line_and_caps_the_text(self):
        e = Embedder("tei", "http://x", max_chars=4)
        self.assertEqual(e.document_text(self.page(description="", questions=["abcdefgh"])), "Guide\nabcd")

    def test_mismatched_vector_count_is_an_error(self):
        e = Embedder("tei", "http://x")
        with mock.patch.object(embed, "post_json", return_value=[[1.0]]):
            with self.assertRaises(RuntimeError):
                e.embed(["a", "b"])

    def test_unknown_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            Embedder("openai", "http://x")

    def test_from_config_reads_models_json_entries(self):
        e = Embedder.from_config({"name": "n", "shape": "ollama", "endpoint": "http://x", "model": "m",
                                  "dimensions": 512, "query_template": None})
        self.assertEqual((e.shape, e.model, e.dimensions, e.query_template), ("ollama", "m", 512, "{text}"))


if __name__ == "__main__":
    unittest.main()
