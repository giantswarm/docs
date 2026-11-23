"""Heading anchors, the way Hugo renders them.

Hugo turns every Markdown heading into an `id` with goldmark's auto heading id
(the `github` style). A search result that links to a section has to use the
same id, or the link lands at the top of the page. Python-Markdown slugs
differ (punctuation, Unicode, duplicates), so this module reimplements Hugo's
rules. It is checked against pages rendered by Hugo 0.163 in
tests/test_anchors.py. docs-indexer needs the same logic.

The rules, as observed on rendered pages:

- The id comes from the visible text of the heading, not the Markdown source.
  Link text and image alt text count. Code span content counts. Raw HTML tags
  and autolinks do not. Named entities (`&amp;`) are decoded, numeric ones
  (`&#65;`) are not.
- The typographer runs first: `--` becomes an en dash and `---` an em dash,
  and both are then dropped.
- Lowercase the text. Keep letters, decimal digits, `_` and `-`. Turn each
  space into `-`. Drop everything else, including combining marks, other
  whitespace and symbols such as `²` or emoji. Leading and trailing hyphens
  stay.
- An empty slug becomes `heading`. A heading with no text gets no id at all.
- A trailing `{#my-id .class}` sets the id explicitly. Explicit ids are used
  as written, even when they repeat.
- Every generated id must be unique on the page, and explicit ids count as
  taken. A clash appends `-1`, `-2` and so on to the base id, using the first
  number that is free. Headings of every level share one namespace.
"""
import html.entities
import re
import unicodedata

ASCII_PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# A trailing attribute block such as {#my-id .class key=value}. Goldmark only
# accepts it when every token is valid, so an id with parentheses, for example,
# leaves the whole block in the heading text.
ATTRIBUTE = r"""(?:#[\w:.-]+|\.[\w:.-]+|[\w:-]+=(?:"[^"]*"|'[^']*'|[^\s"'=<>`}]+))"""
ATTRIBUTES = re.compile(r"[ \t]*\{[ \t]*(%s(?:[ \t]+%s)*)[ \t]*\}[ \t]*$" % (ATTRIBUTE, ATTRIBUTE))
ATTRIBUTE_ID = re.compile(r"(?:^|\s)#([^\s}]+)")

# Raw inline HTML (tags, comments) and autolinks. Neither adds text to the id.
INLINE_HTML = re.compile(
    r"<!--.*?-->"
    r"|</?[A-Za-z][A-Za-z0-9-]*(?:\s+[^<>]*?)?/?>"
    r"|<[A-Za-z][A-Za-z0-9+.-]{1,31}:[^\s<>]*>"
    r"|<[^\s<>@]+@[^\s<>]+>",
    re.S,
)
NAMED_ENTITY = re.compile(r"&([A-Za-z][A-Za-z0-9]*);")


def split_attributes(heading):
    """Return (text, explicit_id) for the content of a heading line.

    explicit_id is None unless the heading ends in a `{#id}` attribute.
    """
    m = ATTRIBUTES.search(heading)
    if not m:
        return heading.strip(), None
    ident = ATTRIBUTE_ID.search(m.group(1))
    return heading[:m.start()].strip(), ident.group(1) if ident else None


def visible_text(markdown):
    """Return the text of inline Markdown the way goldmark collects it for an id."""
    chars = []  # (character, literal). Literal characters can't be emphasis markers.
    _scan(markdown, chars)
    chars = _typographer(chars)
    chars = _drop_underscore_emphasis(chars)
    return "".join(c for c, _ in chars)


def slugify(text):
    """Return the base id for already-visible heading text."""
    out = []
    for c in text.strip(" \t"):
        if c == " ":
            out.append("-")
        elif c in "-_":
            out.append(c)
        else:
            category = unicodedata.category(c)
            if category[0] == "L" or category == "Nd":
                # One code point in, one out, like Go's unicode.ToLower. Python's
                # str.lower() expands a few characters (the dotted capital I).
                out.append(c.lower()[0])
    return "".join(out)


class PageAnchors:
    """Hands out ids for the headings of one page, in document order."""

    def __init__(self):
        self.taken = set()

    def next_id(self, heading):
        """Return the id Hugo renders for the next heading, or None for no id.

        heading is the text after the `#` marks, with any closing `#` marks
        removed and any `{#id}` attribute still attached.
        """
        text, explicit = split_attributes(heading)
        if explicit:
            self.taken.add(explicit)
            return explicit
        if not text:
            return None
        base = slugify(visible_text(text)) or "heading"
        ident = base
        n = 0
        while ident in self.taken:
            n += 1
            ident = "%s-%d" % (base, n)
        self.taken.add(ident)
        return ident


def _scan(s, out):
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n and s[i + 1] in ASCII_PUNCTUATION:
            out.append((s[i + 1], True))
            i += 2
        elif c == "`":
            i = _code_span(s, i, out)
        elif c == "<":
            m = INLINE_HTML.match(s, i)
            if m:
                i = m.end()
            else:
                out.append((c, False))
                i += 1
        elif c == "&":
            m = NAMED_ENTITY.match(s, i)
            decoded = html.entities.html5.get(m.group(1) + ";") if m else None
            if decoded:
                out.extend((d, True) for d in decoded)
                i = m.end()
            else:
                out.append((c, False))
                i += 1
        elif c == "[" or (c == "!" and s[i + 1:i + 2] == "["):
            start = i + 1 if c == "!" else i
            link = _inline_link(s, start)
            if link:
                text, i = link
                _scan(text, out)
            else:
                out.append((c, False))
                i += 1
        else:
            out.append((c, False))
            i += 1
    return out


def _code_span(s, i, out):
    """Append the content of the code span at s[i] and return the next index."""
    n = len(s)
    j = i
    while j < n and s[j] == "`":
        j += 1
    ticks = s[i:j]
    k = j
    while True:
        k = s.find(ticks, k)
        if k < 0:
            out.extend((t, False) for t in ticks)  # no closing run: literal backticks
            return j
        end = k + len(ticks)
        if (k == 0 or s[k - 1] != "`") and (end == n or s[end] != "`"):
            break
        k = end
    content = s[j:k].replace("\n", " ")
    if len(content) > 1 and content[0] == " " and content[-1] == " " and content.strip(" "):
        content = content[1:-1]
    out.extend((ch, True) for ch in content)
    return end


def _inline_link(s, i):
    """Parse `[text](destination)` at s[i]. Return (text, end) or None."""
    n = len(s)
    depth = 0
    j = i
    while j < n:
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "[":
            depth += 1
        elif s[j] == "]":
            depth -= 1
            if depth == 0:
                break
        j += 1
    if j >= n or s[j + 1:j + 2] != "(":
        return None
    depth = 0
    k = j + 1
    while k < n:
        if s[k] == "\\":
            k += 2
            continue
        if s[k] == "(":
            depth += 1
        elif s[k] == ")":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], k + 1
        k += 1
    return None


def _typographer(chars):
    """Apply goldmark's `--` and `---` replacements, which are dropped later anyway."""
    out = []
    i = 0
    n = len(chars)
    while i < n:
        c, literal = chars[i]
        if c == "-" and not literal:
            run = 1
            while i + run < n and chars[i + run] == ("-", False):
                run += 1
            # Greedy, like goldmark: triples first, then a pair, then a lone hyphen.
            left = run % 3
            out.extend([("-", False)] * (1 if left == 1 else 0))
            i += run
        else:
            out.append((c, literal))
            i += 1
    return out


def _drop_underscore_emphasis(chars):
    """Remove `_` characters that CommonMark treats as emphasis delimiters.

    Other `_` stay in the id, as in snake_case or an unmatched `_lead`.
    """
    n = len(chars)
    runs = []  # [start, count, can_open, can_close]
    i = 0
    while i < n:
        if chars[i] == ("_", False):
            j = i
            while j < n and chars[j] == ("_", False):
                j += 1
            before = chars[i - 1][0] if i > 0 else " "
            after = chars[j][0] if j < n else " "
            before_space, after_space = before.isspace(), after.isspace()
            before_punct, after_punct = _is_punctuation(before), _is_punctuation(after)
            left = not after_space and (not after_punct or before_space or before_punct)
            right = not before_space and (not before_punct or after_space or after_punct)
            runs.append([i, j - i, left and (not right or before_punct), right and (not left or after_punct)])
            i = j
        else:
            i += 1

    removed = set()
    stack = []
    for run in runs:
        start, count, can_open, can_close = run
        used = 0  # delimiters of this run consumed from its left end as closers
        while can_close and used < count and stack:
            opener = stack[-1]
            if not opener[2] or opener[1] == 0:
                stack.pop()
                continue
            take = 2 if (opener[1] >= 2 and count - used >= 2) else 1
            # The opener gives up its rightmost delimiters, the closer its leftmost.
            removed.update(range(opener[0] + opener[1] - take, opener[0] + opener[1]))
            removed.update(range(start + used, start + used + take))
            opener[1] -= take
            used += take
            if opener[1] == 0:
                stack.pop()
        if can_open and count - used > 0:
            stack.append([start + used, count - used, True])
    return [ch for idx, ch in enumerate(chars) if idx not in removed]


def _is_punctuation(c):
    return c in ASCII_PUNCTUATION or unicodedata.category(c)[0] == "P"
