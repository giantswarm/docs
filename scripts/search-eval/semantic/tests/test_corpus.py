import os
import tempfile
import unittest

import support  # noqa: F401 - sets up the import path
from corpus import Page, build_page, load_pages, page_url, parse_frontmatter
from embed import Embedder

PAGE = """---
title: Provision a cluster
description: Create your first workload cluster.
weight: 10
menu:
  principal:
    parent: getting-started
owner:
  - https://github.com/orgs/giantswarm/teams/team-a
user_questions:
  - How do I provision my first workload cluster?
  - "What is a \\"workload cluster\\"?"
  - 'What''s the first step?'
last_review_date: 2026-01-01
---

## Heading that is not read

Body text.
"""


class TestParseFrontmatter(unittest.TestCase):
    def test_reads_scalars_and_lists_at_the_top_level(self):
        fields = parse_frontmatter(PAGE)
        self.assertEqual(fields["title"], "Provision a cluster")
        self.assertEqual(fields["weight"], "10")
        self.assertEqual(fields["owner"], ["https://github.com/orgs/giantswarm/teams/team-a"])
        self.assertEqual(fields["last_review_date"], "2026-01-01")

    def test_unquotes_double_and_single_quoted_items(self):
        self.assertEqual(parse_frontmatter(PAGE)["user_questions"], [
            "How do I provision my first workload cluster?",
            'What is a "workload cluster"?',
            "What's the first step?"])

    def test_nested_mappings_do_not_leak_into_the_parent_key(self):
        fields = parse_frontmatter(PAGE)
        self.assertEqual(fields["menu"], "")
        self.assertNotIn("parent", fields)

    def test_block_scalars_are_joined_on_one_line(self):
        fields = parse_frontmatter("---\ndescription: |\n  First line.\n  Second line.\nweight: 1\n---\nBody")
        self.assertEqual(fields["description"], "First line. Second line.")
        self.assertEqual(fields["weight"], "1")

    def test_folded_scalar_with_chomping_indicator(self):
        fields = parse_frontmatter("---\ndescription: >-\n  One\n  two\n---\n")
        self.assertEqual(fields["description"], "One two")

    def test_quoted_title_keeps_inner_quotes(self):
        self.assertEqual(parse_frontmatter("---\ntitle: \"'kubectl gs' reference\"\n---\n")["title"], "'kubectl gs' reference")

    def test_no_front_matter(self):
        self.assertEqual(parse_frontmatter("# Just a body\n"), {})


class TestBuildPage(unittest.TestCase):
    def test_page_with_questions(self):
        page = build_page(PAGE, "/getting-started/provision/")
        self.assertEqual(page.title, "Provision a cluster")
        self.assertEqual(page.description, "Create your first workload cluster.")
        self.assertEqual(len(page.questions), 3)
        self.assertEqual((page.url, page.type), ("/getting-started/provision/", "Documentation"))

    def test_page_without_questions_has_title_and_description_only(self):
        page = build_page("---\ntitle: Section\ndescription: A list page.\n---\n", "/s/")
        self.assertEqual(page.questions, [])
        self.assertEqual(Embedder("tei", "http://x").document_text(page), "Section\nA list page.")

    def test_empty_questions_key_gives_no_questions(self):
        page = build_page("---\ntitle: T\ndescription: D.\nuser_questions:\n---\n", "/t/")
        self.assertEqual(page.questions, [])

    def test_page_without_a_title_is_skipped(self):
        self.assertIsNone(build_page("---\ndescription: x\n---\n", "/x/"))

    def test_assembled_text_is_title_description_then_questions(self):
        page = build_page(PAGE, "/p/")
        self.assertEqual(
            Embedder("tei", "http://x").document_text(page),
            'Provision a cluster\nCreate your first workload cluster.\n'
            'How do I provision my first workload cluster? What is a "workload cluster"? What\'s the first step?')

    def test_body_is_not_part_of_the_record(self):
        page = build_page(PAGE, "/p/")
        self.assertNotIn("Body text", " ".join([page.title, page.description, page.text]))

    def test_page_fields_map_onto_the_embedding_template_names(self):
        page = Page("T", "D.", ["Q1?", "Q2?"], "/t/", "Documentation")
        self.assertEqual((page.heading, page.text), ("D.", "Q1? Q2?"))


class TestLoadPages(unittest.TestCase):
    def test_skips_changes_includes_list_pages_and_sorts_by_url(self):
        files = {
            "changes/app/v1.md": "---\ntitle: v1\ndescription: Release.\n---\n",
            "tutorials/b/index.md": PAGE,
            "tutorials/a/index.md": "---\ntitle: A\ndescription: Page a.\nuser_questions:\n  - Q?\n---\nBody",
            "tutorials/_index.md": "---\ntitle: Tutorials\ndescription: List of tutorials.\n---\n",
            "reference/faq.md": "---\ntitle: FAQ\ndescription: Questions.\n---\nBody",
        }
        with tempfile.TemporaryDirectory() as root:
            for rel, raw in files.items():
                path = os.path.join(root, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(raw)
            pages = load_pages(root)
        self.assertEqual([p.url for p in pages],
                         ["/reference/faq/", "/tutorials/", "/tutorials/a/", "/tutorials/b/"])
        self.assertEqual([bool(p.questions) for p in pages], [False, False, True, True])


class TestPageUrl(unittest.TestCase):
    def test_page_url(self):
        self.assertEqual(page_url("tutorials/a/b/index.md"), "/tutorials/a/b/")
        self.assertEqual(page_url("overview/_index.md"), "/overview/")
        self.assertEqual(page_url("reference/kubectl-gs/faq.md"), "/reference/kubectl-gs/faq/")


if __name__ == "__main__":
    unittest.main()
