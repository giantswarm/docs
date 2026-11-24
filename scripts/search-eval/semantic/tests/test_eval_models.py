import json
import os
import unittest
from unittest import mock

import support  # noqa: F401 - sets up the import path
import eval_models
from eval_models import format_comparison, format_report, index_name, rrf


class TestRrf(unittest.TestCase):
    def test_ids_in_both_lists_beat_ids_in_one(self):
        self.assertEqual(rrf([["a", "b", "c"], ["c", "d"]], k=60)[:1], ["c"])

    def test_scores_are_one_over_k_plus_rank(self):
        fused = rrf([["a"], ["b", "a"]], k=1)
        # a: 1/2 + 1/3, b: 1/2
        self.assertEqual(fused, ["a", "b"])

    def test_ties_keep_first_appearance(self):
        self.assertEqual(rrf([["a", "b"], ["b", "a"]]), ["a", "b"])

    def test_empty_input(self):
        self.assertEqual(rrf([[], []]), [])


class TestShapes(unittest.TestCase):
    def test_index_name_is_prefixed_and_safe(self):
        self.assertEqual(index_name("EmbeddingGemma 300m/512"), "docs-pages-eval-embeddinggemma-300m-512")

    def test_refuses_production_hosts(self):
        with self.assertRaises(SystemExit):
            eval_models.refuse_production("docs.giantswarm.io")
        eval_models.refuse_production("localhost")

    def test_query_clauses(self):
        self.assertEqual(eval_models.vector_clause([0.5], 10), {"knn": {"embedding": {"vector": [0.5], "k": 10}}})
        self.assertIn("questions^2", eval_models.keyword_clause("x")["multi_match"]["fields"])

    def test_models_json_is_valid_for_the_embedder(self):
        with open(os.path.join(support.HERE, "..", "models.json"), encoding="utf-8") as f:
            models = json.load(f)["models"]
        names = [m["name"] for m in models]
        self.assertEqual(len(names), len(set(names)))
        for m in models:
            eval_models.Embedder.from_config(m)


class FakeEmbedder:
    def embed_query(self, query):
        return [1.0, 0.0]


class TestKeywordLeg(unittest.TestCase):
    def test_normalize_url_reduces_gateway_urls_to_index_paths(self):
        n = eval_models.normalize_url
        self.assertEqual(n("https://docs.giantswarm.io/a/b/#sec"), "/a/b/")
        self.assertEqual(n("/a/b"), "/a/b/")
        self.assertEqual(n("/a/b/?q=x"), "/a/b/")

    def test_gateway_keyword_uses_the_phase_1_client_for_docs_and_blog(self):
        calls = []

        def fake_fetch(endpoint, query, type_, size, timeout):
            calls.append((endpoint, query, type_, size, timeout))
            hits = [{"url": "https://docs.giantswarm.io/x/y#z"}] if type_ == "Documentation" else [{"url": "/blog/b/"}]
            return hits, 12.0

        with mock.patch.object(eval_models.run, "fetch", side_effect=fake_fetch):
            docs, blog, ms = eval_models.keyword_gateway("https://gw/", 7.0, 4)("login", 50)
        self.assertEqual((docs, blog, ms), (["/x/y/"], ["/blog/b/"], 12.0))
        self.assertEqual(calls, [("https://gw/", "login", "Documentation", 50, 7.0),
                                 ("https://gw/", "login", "Blog", 4, 7.0)])

    def test_score_query_counts_blog_for_keyword_and_hybrid_but_not_vector(self):
        keyword = lambda query, size: (["/a/", "/b/"], ["/blog/post/"], 5.0)  # noqa: E731
        with mock.patch.object(eval_models, "search", return_value=["/c/", "/a/"]):
            result, _ = eval_models.score_query(None, "idx", FakeEmbedder(), keyword, "q", ["/blog/"], 5, 50, 60)
        self.assertEqual([result[m][0] for m in eval_models.METHODS], [True, False, True])

    def test_score_query_fuses_gateway_and_vector_rankings(self):
        keyword = lambda query, size: (["/a/", "/b/"], [], 5.0)  # noqa: E731
        with mock.patch.object(eval_models, "search", return_value=["/c/", "/b/"]):
            result, _ = eval_models.score_query(None, "idx", FakeEmbedder(), keyword, "q", ["/c/"], 1, 50, 60)
        self.assertEqual(result["keyword"][:2], (False, "/a/"))
        self.assertEqual(result["vector"][:2], (True, "/c/"))
        self.assertEqual(result["hybrid"][1], "/b/")  # in both lists, so it leads the fusion
        self.assertEqual(result["hybrid"][2], 5.0 + result["vector"][2])


class TestReport(unittest.TestCase):
    def result(self):
        return {"name": "m", "keyword_label": eval_models.KEYWORD_LABELS["gateway"], "dimension": 512, "embed_seconds": 12.0, "total": 2,
                "rows": [("login", {"keyword": True, "vector": False, "hybrid": True}, "/a/"),
                         ("bad", None, "ERROR: boom")],
                "hits": {"keyword": 1, "vector": 0, "hybrid": 1},
                "p95": {"keyword": 20.0, "vector": 350.0, "hybrid": 370.0}, "embed_p95": 300.0}

    def test_report_has_table_and_summary(self):
        report = format_report(self.result(), 303, 5, 300)
        self.assertIn("| login | hit | miss | hit | /a/ |", report)
        self.assertIn("| bad | ERROR | ERROR | ERROR | ERROR: boom |", report)
        self.assertIn("Keyword column: keyword (live /searchapi)", report)
        self.assertIn("- keyword (live /searchapi) top-5 hit rate: **50%** (1/2), p95 latency **20 ms**", report)
        self.assertIn("- vector top-5 hit rate: **0%** (0/2), p95 latency **350 ms** (over budget)", report)
        self.assertIn("512-dimension vectors, 303 pages", report)

    def test_local_keyword_is_labelled_as_not_the_baseline(self):
        result = dict(self.result(), keyword_label=eval_models.KEYWORD_LABELS["local"])
        self.assertIn("NOT the baseline", format_report(result, 303, 5, 300))
        self.assertIn("NOT the baseline", format_comparison([result], 5))

    def test_comparison_has_one_row_per_model(self):
        table = format_comparison([self.result()], 5)
        self.assertIn("| m | 512 | 1/2 (50%) | 0/2 (0%) | 1/2 (50%) | 350 | 370 |", table)


if __name__ == "__main__":
    unittest.main()
