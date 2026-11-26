"""Build the page-level corpus for the semantic index.

One record per page, made from the front matter alone: the title, the
description and the `user_questions`. The body is not read.

Headings are not embedded. Most are scaffolding ("Prerequisites", "Usage",
"Flags") and would give near-identical vectors on hundreds of pages. The page
carries hand-written text shaped like a search query instead, the
`user_questions` list, such as "How do I configure and provision my first
workload cluster?". Embedding those compares a query with a query, which is an
easier problem than comparing a query with body text.

The 303 pages outside /changes all have a title and a description. 268 have
`user_questions`, which is every page with a body. The other 35 are list pages
with front matter only, and they get the title and description alone.

Release notes under /changes are skipped. There are thousands, and their
titles say little about their content.

A record is keyed on the page URL with no anchor, as in the phase 1 gate.
"""
import collections
import os
import re

TYPE_DOCUMENTATION = "Documentation"
SKIPPED_SECTIONS = ("changes",)

FRONTMATTER = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", re.S)
KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*?)[ \t]*$")
LIST_ITEM = re.compile(r"^ {0,2}-[ \t]+(.*?)[ \t]*$")
BLOCK_SCALAR = re.compile(r"^[|>][+-]?$")


class Page(collections.namedtuple("Page", "title description questions url type")):
    """One page. questions is a list of strings, empty when the page has none.

    embed.py's templates name the fields title, heading and text. For a page
    the description is the heading and the questions joined by a space are the
    text, so the default template yields the title, the description and the
    questions on three lines. Each question ends in a question mark, so a
    space is enough of a separator.
    """

    @property
    def heading(self):
        return self.description

    @property
    def text(self):
        return " ".join(self.questions)


def parse_frontmatter(raw):
    """Return the top-level front matter as a dict, or {} without front matter.

    A value is a string, or a list of strings for a `- item` list. Plain,
    quoted and block (`|` and `>`) scalars are read. Nested mappings are
    ignored, so a key that only has indented children gets an empty string.
    """
    m = FRONTMATTER.match(raw)
    if not m:
        return {}
    fields = {}
    key = None
    block = False  # inside the indented lines of a | or > scalar
    for line in m.group(1).split("\n"):
        kv = KEY.match(line)
        if kv:
            key, value = kv.group(1), kv.group(2)
            block = bool(BLOCK_SCALAR.match(value))
            fields[key] = "" if block else _scalar(value)
        elif key is None:
            continue
        elif block:
            fields[key] = (fields[key] + " " + line.strip()).strip()
        else:
            item = LIST_ITEM.match(line)
            if item:
                if not isinstance(fields[key], list):
                    fields[key] = []
                fields[key].append(_scalar(item.group(1)))
    return fields


def _scalar(value):
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return re.sub(r"\\(.)", r"\1", value[1:-1])
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def page_url(relpath):
    """Map a path under src/content to its published URL path."""
    parts = relpath.replace(os.sep, "/")[:-len(".md")].split("/")
    if parts[-1] in ("index", "_index"):
        parts = parts[:-1]
    return "/" + "/".join(parts) + "/" if parts else "/"


def build_page(raw, url, type_=TYPE_DOCUMENTATION):
    """Return the Page for one file's contents, or None when it has no title."""
    fields = parse_frontmatter(raw)
    title = _clean(fields.get("title"))
    if not title:
        return None
    questions = fields.get("user_questions")
    if not isinstance(questions, list):
        questions = []
    return Page(title, _clean(fields.get("description")), [q for q in map(_clean, questions) if q], url, type_)


def load_pages(content_root, type_=TYPE_DOCUMENTATION):
    """Return a Page for every page under content_root outside /changes, sorted by URL."""
    pages = []
    for dirpath, dirnames, files in os.walk(content_root):
        dirnames.sort()
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), content_root)
            if rel.split(os.sep)[0] in SKIPPED_SECTIONS:
                continue
            with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                page = build_page(f.read(), page_url(rel), type_)
            if page:
                pages.append(page)
    return pages


def _clean(value):
    return re.sub(r"\s+", " ", value).strip() if isinstance(value, str) else ""
