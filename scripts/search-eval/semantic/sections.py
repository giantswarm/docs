"""Split Hugo pages into section records for the semantic index.

A record is one H2 or H3 section: the page title, the heading, the anchor Hugo
renders for it, the page URL, the type and the text under the heading. Text
before the first H2 or H3 becomes a record with an empty heading and anchor.

The split works on the raw Markdown, because the keyword indexer throws
headings away when it converts a page to text. Two things make a regex on
`^##` wrong:

- Fenced code blocks, HTML comments and some shortcodes hold lines that look
  like headings but aren't. Shortcodes whose inner Markdown Hugo renders on its
  own (`details`, `tab`) are skipped too, since their headings get ids in a
  separate namespace that a page-level anchor can't point at.
- Every heading consumes an id, not only H2 and H3. An H4 or a `step` heading
  changes the suffix of a later duplicate, so all of them go through
  PageAnchors even though only H2 and H3 start a record.

Setext headings (underlined with `===` or `---`) are not recognised. No page
under src/content uses one.

Release notes under /changes are skipped. Their headings ("Fixed", "Added")
would give thousands of near-identical records.
"""
import collections
import os
import re

from anchors import PageAnchors, split_attributes

TYPE_DOCUMENTATION = "Documentation"
SKIPPED_SECTIONS = ("changes",)
SPLIT_LEVELS = (2, 3)

Section = collections.namedtuple("Section", "title heading anchor url type level text")

FRONTMATTER = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*\n?(.*)$", re.S)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
ATX_HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
SHORTCODE = re.compile(r"\{\{[<%]\s*(/?)\s*([A-Za-z_][A-Za-z0-9_-]*)([^}]*?)[>%]\}\}")
STEP_TITLE = re.compile(r"""title\s*=\s*(?:"([^"]*)"|'([^']*)')""")

# Shortcodes whose inner Markdown is rendered separately or not at all.
OPAQUE_SHORTCODES = frozenset(["details", "tab", "tabs", "mermaid", "highlight"])


def parse_frontmatter(raw):
    """Return (fields, body). Only the flat `key: value` lines are read."""
    m = FRONTMATTER.match(raw)
    if not m:
        return {}, raw
    fields = {}
    for line in m.group(1).split("\n"):
        kv = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*?)[ \t]*$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip("\"'")
    return fields, m.group(2)


def page_url(relpath):
    """Map a path under src/content to its published URL path."""
    parts = relpath.replace(os.sep, "/")[:-len(".md")].split("/")
    if parts[-1] in ("index", "_index"):
        parts = parts[:-1]
    return "/" + "/".join(parts) + "/" if parts else "/"


def split_page(raw, url, title=None, type_=TYPE_DOCUMENTATION):
    """Split one page's raw Markdown into Section records.

    title defaults to the front matter title. A page without one gives no
    records, like the PoC loader.
    """
    fields, body = parse_frontmatter(raw)
    title = title or fields.get("title")
    if not title:
        return []

    anchors = PageAnchors()
    sections = []
    current = {"heading": "", "anchor": "", "level": 1, "lines": []}

    def close():
        text = plain_text("\n".join(current["lines"]))
        if text or current["heading"]:
            sections.append(Section(title, current["heading"], current["anchor"], url,
                                    type_, current["level"], text))

    for level, heading, line in _blocks(body):
        if level is None:
            current["lines"].append(line)
            continue
        anchor = anchors.next_id(heading)
        if level in SPLIT_LEVELS:
            close()
            current = {"heading": plain_text(split_attributes(heading)[0]), "anchor": anchor or "",
                       "level": level, "lines": []}
        else:
            current["lines"].append(heading)
    close()
    return sections


def load_sections(content_root, type_=TYPE_DOCUMENTATION):
    """Return the Section records of every page under content_root, sorted by URL."""
    sections = []
    for dirpath, dirnames, files in os.walk(content_root):
        dirnames.sort()
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), content_root)
            if rel.split(os.sep)[0] in SKIPPED_SECTIONS:
                continue
            with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                raw = f.read()
            sections.extend(split_page(raw, page_url(rel), type_=type_))
    return sections


def plain_text(markdown):
    """Reduce a block of Markdown to prose for embedding and keyword search.

    Code stays, since commands and resource names are what people search for.
    Shortcode tags, comments, HTML tags and Markdown syntax go.
    """
    text = re.sub(r"<!--.*?-->", " ", markdown, flags=re.S)
    text = SHORTCODE.sub(" ", text)
    text = re.sub(r"^ {0,3}(`{3,}|~{3,}).*$", " ", text, flags=re.M)
    text = re.sub(r"<[^>\n]+>", " ", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^[ \t]*(?:#{1,6}|>|[-*+]|\d+[.)])[ \t]+", "", text, flags=re.M)
    text = re.sub(r"[*`|]+|(?<!\w)_+|_+(?!\w)", " ", text)  # keep snake_case intact
    return re.sub(r"\s+", " ", text).strip()


def _blocks(body):
    """Yield (level, heading, line) per line of the body.

    level is None for an ordinary line, else the heading level, with heading
    holding the text after the `#` marks. Lines inside code, comments and
    opaque shortcodes are ordinary lines.
    """
    fence = None
    in_comment = False
    opaque = collections.Counter()
    for line in body.split("\n"):
        m = FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2).strip():
                fence = None
            yield None, "", line
            continue
        if m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
            fence = m.group(1)
            yield None, "", line
            continue

        if in_comment:
            in_comment = "-->" not in line
            yield None, "", line
            continue
        if line.lstrip().startswith("<!--") and "-->" not in line:
            in_comment = True
            yield None, "", line
            continue

        depth_before = sum(opaque.values())
        step = None
        for sc in SHORTCODE.finditer(line):
            closing, name = sc.group(1), sc.group(2)
            if name in OPAQUE_SHORTCODES:
                opaque[name] += -1 if closing else 1
                opaque[name] = max(opaque[name], 0)
            elif name == "step" and not closing:
                t = STEP_TITLE.search(sc.group(3))
                step = (t.group(1) if t.group(1) is not None else t.group(2)) if t else None
        if depth_before or sum(opaque.values()):
            yield None, "", line
            continue

        if step is not None:
            # The step shortcode emits "### <title>", a real heading with an id.
            yield 3, step, line
            continue

        h = ATX_HEADING.match(line)
        if h:
            text = h.group(2) or ""
            yield len(h.group(1)), "" if set(text) == {"#"} else text, line
            continue
        yield None, "", line
