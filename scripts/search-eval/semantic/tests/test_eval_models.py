import json
import os
import unittest

import support  # noqa: F401 - sets up the import path
import eval_models
from eval_models import format_comparison, format_report, index_name, rrf, top_pages
from sections import Section


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


class TestTopPages(unittest.TestCase):
    def test_collapses_sections_of_one_page_and_stops_at_top_k(self):
        hits = [{"url": u} for u in ["/a/", "/a/", "/b/", "/a/", "/c/", "/d/"]]
        self.assertEqual(top_pages(hits, 3), ["/a/", "/b/", "/c/"])


class TestShapes(unittest.TestCase):
    def test_index_name_is_prefixed_and_safe(self):
        self.assertEqual(index_name("EmbeddingGemma 300m/512"), "docs-sections-eval-embeddinggemma-300m-512")

    def test_refuses_production_hosts(self):
        with self.assertRaises(SystemExit):
            eval_models.refuse_production("docs.giantswarm.io")
        eval_models.refuse_production("localhost")

    def test_query_clauses(self):
        self.assertEqual(eval_models.vector_clause([0.5], 10), {"knn": {"embedding": {"vector": [0.5], "k": 10}}})
        self.assertIn("heading^3", eval_models.keyword_clause("x")["multi_match"]["fields"])

    def test_models_json_is_valid_for_the_embedder(self):
        with open(os.path.join(support.HERE, "..", "models.json"), encoding="utf-8") as f:
            models = json.load(f)["models"]
        names = [m["name"] for m in models]
        self.assertEqual(len(names), len(set(names)))
        for m in models:
            eval_models.Embedder.from_config(m)


class TestReport(unittest.TestCase):
    def result(self):
        return {"name": "m", "dimension": 512, "embed_seconds": 12.0, "total": 2,
                "rows": [("login", {"keyword": True, "vector": False, "hybrid": True}, "/a/"),
                         ("bad", None, "ERROR: boom")],
                "hits": {"keyword": 1, "vector": 0, "hybrid": 1},
                "p95": {"keyword": 20.0, "vector": 350.0, "hybrid": 370.0}, "embed_p95": 300.0}

    def test_report_has_table_and_summary(self):
        sections = [Section("T", "H", "h", "/a/", "Documentation", 2, "x")]
        report = format_report(self.result(), sections, 5, 300)
        self.assertIn("| login | hit | miss | hit | /a/ |", report)
        self.assertIn("| bad | ERROR | ERROR | ERROR | ERROR: boom |", report)
        self.assertIn("- keyword top-5 hit rate: **50%** (1/2), p95 latency **20 ms**", report)
        self.assertIn("- vector top-5 hit rate: **0%** (0/2), p95 latency **350 ms** (over budget)", report)
        self.assertIn("1 sections from 1 pages", report)

    def test_comparison_has_one_row_per_model(self):
        table = format_comparison([self.result()], 5)
        self.assertIn("| m | 512 | 1/2 (50%) | 0/2 (0%) | 1/2 (50%) | 350 | 370 |", table)


if __name__ == "__main__":
    unittest.main()
