import os
import tempfile
import unittest

import support  # noqa: F401 - sets up the import path
from sections import load_sections, page_url, parse_frontmatter, plain_text, split_page

URL = "/tutorials/example/"


def split(body, title="Example"):
    return split_page("---\ntitle: %s\n---\n%s" % (title, body), URL)


class TestSplitPage(unittest.TestCase):
    def test_splits_at_h2_and_h3_with_title_heading_anchor_url_and_type(self):
        sections = split("Intro text.\n\n## Install\n\nRun it.\n\n### Verify the result\n\nCheck it.\n")
        self.assertEqual([(s.heading, s.anchor, s.level) for s in sections],
                         [("", "", 1), ("Install", "install", 2), ("Verify the result", "verify-the-result", 3)])
        self.assertEqual([s.text for s in sections], ["Intro text.", "Run it.", "Check it."])
        self.assertEqual({(s.title, s.url, s.type) for s in sections}, {("Example", URL, "Documentation")})

    def test_fenced_code_lines_that_look_like_headings_do_not_split(self):
        body = "## Real\n\n```bash\n## not a heading\n# comment\n```\n\n~~~\n## nor this\n~~~\n\n## Next\n"
        sections = split(body)
        self.assertEqual([s.heading for s in sections], ["Real", "Next"])
        self.assertIn("not a heading", sections[0].text)

    def test_a_longer_fence_is_not_closed_by_a_shorter_one(self):
        body = "## A\n\n````md\n```\n## inside\n```\n````\n\n## B\n"
        self.assertEqual([s.heading for s in split(body)], ["A", "B"])

    def test_html_comments_are_skipped(self):
        body = "## A\n\n<!--\n## hidden\n-->\n\n## B\n"
        self.assertEqual([s.heading for s in split(body)], ["A", "B"])

    def test_headings_inside_details_and_tab_shortcodes_do_not_split(self):
        body = ('## A\n\n{{% details "More" %}}\n### Inner\n\ntext\n{{% /details %}}\n\n'
                '{{< tabs >}}\n{{< tab title="x" id="x" >}}\n### Tabbed\n{{< /tab >}}\n{{< /tabs >}}\n\n## B\n')
        self.assertEqual([s.heading for s in split(body)], ["A", "B"])

    def test_notice_and_steps_do_not_hide_headings(self):
        body = "{{% notice warning %}}\n## Inside notice\n{{% /notice %}}\n"
        self.assertEqual([s.heading for s in split(body)], ["Inside notice"])

    def test_step_shortcode_is_an_h3_heading(self):
        body = ('## Flow\n\n{{% steps %}}\n\n{{% step title="Claude Code → Muster" %}}\n\nDo it.\n\n'
                '{{% /step %}}\n\n{{% /steps %}}\n')
        sections = split(body)
        self.assertEqual([(s.heading, s.anchor, s.level) for s in sections],
                         [("Flow", "flow", 2), ("Claude Code → Muster", "claude-code--muster", 3)])
        self.assertEqual(sections[1].text, "Do it.")

    def test_deeper_headings_use_ids_but_do_not_split(self):
        sections = split("## A\n\n#### A\n\ndeep text\n\n## A\n")
        self.assertEqual([(s.heading, s.anchor) for s in sections], [("A", "a"), ("A", "a-2")])
        self.assertIn("deep text", sections[0].text)

    def test_explicit_id_and_attributes_are_not_part_of_the_heading(self):
        sections = split("## Options {#flags}\n\ntext\n")
        self.assertEqual((sections[0].heading, sections[0].anchor), ("Options", "flags"))

    def test_closing_hashes_and_markup_are_dropped_from_the_heading(self):
        sections = split("## The `kubectl gs` [tool](/x/) ##\n\ntext\n")
        self.assertEqual((sections[0].heading, sections[0].anchor), ("The kubectl gs tool", "the-kubectl-gs-tool"))

    def test_page_without_title_or_text_gives_no_records(self):
        self.assertEqual(split_page("---\ndescription: x\n---\n## A\n", URL), [])
        self.assertEqual(split(""), [])

    def test_empty_section_with_a_heading_is_kept(self):
        self.assertEqual([(s.heading, s.text) for s in split("## A\n\n## B\n\ntext\n")], [("A", ""), ("B", "text")])


class TestRenderedPages(unittest.TestCase):
    def test_h2_and_h3_anchors_are_ids_in_the_page_hugo_rendered(self):
        pages = support.load_fixture("rendered_pages.json")["pages"]
        for name, expected in pages.items():
            with self.subTest(page=name):
                sections = split_page(support.read_page(name), expected["url"])
                self.assertTrue(sections)
                anchors = [s.anchor for s in sections if s.heading]
                self.assertTrue(all(anchors))
                self.assertTrue(set(anchors) <= set(expected["ids"]))
                self.assertEqual(anchors, [i for i in expected["ids"] if i in anchors])

    def test_step_page_has_a_record_for_each_step(self):
        name = "tutorials__observability__network-monitoring__index.md"
        sections = split_page(support.read_page(name), "/x/")
        self.assertIn("identify-high-cross-az-namespaces", [s.anchor for s in sections])


class TestPlainText(unittest.TestCase):
    def test_removes_shortcodes_comments_html_and_link_syntax(self):
        md = 'See [the docs]({{< relref "/x/" >}}) <b>now</b> ok\n{{< mermaid >}}\n<!-- c -->\n- item **bold**'
        self.assertEqual(plain_text(md), "See the docs now ok item bold")

    def test_keeps_code_and_snake_case(self):
        self.assertEqual(plain_text("```yaml\ncluster_name: my_cluster\n```"), "cluster_name: my_cluster")


class TestPagesAndFiles(unittest.TestCase):
    def test_page_url(self):
        self.assertEqual(page_url("tutorials/a/b/index.md"), "/tutorials/a/b/")
        self.assertEqual(page_url("overview/_index.md"), "/overview/")
        self.assertEqual(page_url("reference/kubectl-gs/faq.md"), "/reference/kubectl-gs/faq/")

    def test_frontmatter_fields_are_unquoted(self):
        fields, body = parse_frontmatter('---\ntitle: "A title"\nweight: 3\n---\nBody\n')
        self.assertEqual((fields["title"], fields["weight"], body), ("A title", "3", "Body\n"))

    def test_load_sections_skips_changes_and_keeps_order(self):
        with tempfile.TemporaryDirectory() as root:
            for rel, body in [("changes/app/v1.md", "## Fixed\n\nbug\n"), ("tutorials/b/index.md", "## B\n\nb\n"),
                              ("tutorials/a/index.md", "## A\n\na\n"), ("tutorials/_index.md", "")]:
                path = os.path.join(root, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write("---\ntitle: T\n---\n" + body)
            sections = load_sections(root)
        self.assertEqual([(s.url, s.heading) for s in sections],
                         [("/tutorials/a/", "A"), ("/tutorials/b/", "B")])


if __name__ == "__main__":
    unittest.main()
