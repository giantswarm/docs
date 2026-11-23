import unittest

import support  # noqa: F401 - sets up the import path
from anchors import PageAnchors, slugify, split_attributes, visible_text
from sections import _blocks, parse_frontmatter


def ids_for(headings):
    page = PageAnchors()
    return [page.next_id(h) for h in headings]


class TestRenderedPages(unittest.TestCase):
    """Compare with ids Hugo rendered for real pages of this repo."""

    def test_every_heading_id_matches_hugo(self):
        pages = support.load_fixture("rendered_pages.json")["pages"]
        for name, expected in pages.items():
            with self.subTest(page=name):
                _, body = parse_frontmatter(support.read_page(name))
                headings = [h for level, h, _ in _blocks(body) if level and level >= 2]
                got = [i for i in ids_for(headings) if i]
                self.assertEqual(got, expected["ids"])


class TestScratchPages(unittest.TestCase):
    """Compare with ids Hugo rendered for scratch pages.

    No page in src/content repeats a heading in the same scope, so the
    duplicate numbering rules can only be checked on a page written for it.
    """

    def test_sequences_match_hugo(self):
        for name, entries in support.load_fixture("synthetic_headings.json")["sequences"].items():
            with self.subTest(page=name):
                self.assertEqual(ids_for([e["heading"] for e in entries]), [e["id"] for e in entries])


class TestSlugify(unittest.TestCase):
    def test_lowercases_and_joins_with_hyphens(self):
        self.assertEqual(slugify("Install the App"), "install-the-app")

    def test_drops_punctuation_but_keeps_hyphen_and_underscore(self):
        self.assertEqual(slugify("Hello, World! (v1.2) a-b c_d"), "hello-world-v12-a-b-c_d")

    def test_each_space_is_a_hyphen_and_edges_are_kept(self):
        self.assertEqual(slugify("a   b"), "a---b")
        self.assertEqual(slugify("- a -"), "--a--")

    def test_keeps_unicode_letters_and_decimal_digits(self):
        self.assertEqual(slugify("Müller Straße ٣"), "müller-straße-٣")

    def test_drops_marks_symbols_and_other_numbers(self):
        self.assertEqual(slugify("café x² ① 🚀"), "cafe-x--")

    def test_lowercases_one_code_point_at_a_time(self):
        self.assertEqual(slugify("İstanbul"), "istanbul")


class TestVisibleText(unittest.TestCase):
    def test_link_and_image_text_count_but_not_destinations(self):
        self.assertEqual(visible_text("A [link](https://x.io/a_(b)) and ![alt](i.png)"), "A link and alt")

    def test_code_span_content_is_kept_verbatim(self):
        self.assertEqual(visible_text("Use `a_b *c* -- d` now"), "Use a_b *c* -- d now")

    def test_raw_html_and_autolinks_add_no_text(self):
        self.assertEqual(visible_text("<b>bold</b> <https://x.io> <!-- c -->end"), "bold  end")

    def test_named_entities_are_decoded_and_numeric_ones_are_not(self):
        self.assertEqual(visible_text("a &amp; b &#65;"), "a & b &#65;")

    def test_typographer_dashes_vanish_from_the_id(self):
        self.assertEqual(slugify(visible_text("foo -- bar")), "foo--bar")
        self.assertEqual(slugify(visible_text("foo--bar")), "foobar")
        self.assertEqual(slugify(visible_text("a---b----c")), "ab-c")

    def test_underscore_emphasis_is_removed_but_snake_case_stays(self):
        self.assertEqual(visible_text("_em_ and snake_case and _open"), "em and snake_case and _open")

    def test_backslash_escape_keeps_the_character(self):
        self.assertEqual(slugify(visible_text(r"a \_ b")), "a-_-b")


class TestAttributes(unittest.TestCase):
    def test_trailing_id_attribute(self):
        self.assertEqual(split_attributes("Title {#my-id .cls}"), ("Title", "my-id"))

    def test_class_only_attribute_leaves_no_id(self):
        self.assertEqual(split_attributes("Title {.cls}"), ("Title", None))

    def test_braces_inside_the_text_are_not_attributes(self):
        self.assertEqual(split_attributes("A {#x} b"), ("A {#x} b", None))

    def test_invalid_id_leaves_the_block_in_the_text(self):
        text, ident = split_attributes("VCD settings {#vcd-(settings)}")
        self.assertIsNone(ident)
        self.assertEqual(slugify(visible_text(text)), "vcd-settings-vcd-settings")


class TestPageAnchors(unittest.TestCase):
    def test_duplicates_take_the_first_free_number(self):
        self.assertEqual(ids_for(["A", "A", "A 1", "A", "A-1"]), ["a", "a-1", "a-1-1", "a-2", "a-1-2"])

    def test_explicit_ids_are_taken_but_never_renumbered(self):
        self.assertEqual(ids_for(["A {#x}", "X", "B {#x}"]), ["x", "x-1", "x"])

    def test_empty_heading_gets_no_id_and_empty_slug_gets_heading(self):
        self.assertEqual(ids_for(["", "!!!", "???"]), [None, "heading", "heading-1"])


if __name__ == "__main__":
    unittest.main()
