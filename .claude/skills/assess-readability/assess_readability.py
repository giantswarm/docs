#!/usr/bin/env python3
"""Assess the English readability of documentation pages.

Computes four widely-cited readability metrics over the prose of each Markdown
page (frontmatter, code fences, shortcodes and markup stripped):

  - Flesch Reading Ease      higher = easier (0-100+, ~60-70 is "plain English")
  - Flesch-Kincaid Grade     approximate US school grade level
  - Gunning Fog Index        approximate years of formal education to read
  - LIX (Laesbarhetsindex)   language-independent index (words/sentence + long words)

Everything is computed with the Python standard library and a fixed
syllable-counting heuristic, so the assessment is **completely deterministic**:
the same input always yields the same scores. No network, no external libraries.

Usage:
  python3 assess_readability.py [PATH ...]          # ranked sweep + corpus average
  python3 assess_readability.py page.md             # detailed single-file report
  python3 assess_readability.py --top 20            # only the 20 hardest pages
  python3 assess_readability.py --json              # machine-readable output

PATH defaults to src/content. A PATH may be a file or a directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass

# Strip helpers, shared with .claude/skills/find-style-issues/find_style_issues.py
# so the two tools see prose the same way.
RE_SHORTCODE = re.compile(r"\{\{[<%].*?[%>]\}\}", re.DOTALL)
RE_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")          # [text](url) -> text
RE_IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")        # ![alt](url) -> alt
RE_HTML_TAG = re.compile(r"<[^>]+>")
RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_EMPHASIS = re.compile(r"(\*\*|__|\*|_)")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
RE_ANCHOR = re.compile(r"\{#[^}]*\}\s*$")
RE_FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
RE_LIST = re.compile(r"^\s*([-*+]|\d+[.)])\s+")

# Sentences end at .!? — and also at line breaks, because list items, headings
# and table-free hub pages put one sentence-like unit per line without terminal
# punctuation (paragraphs in this repo are single, non-wrapped lines).
RE_SENTENCE_SPLIT = re.compile(r"[.!?\n]+")
RE_WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")

VOWELS = set("aeiouy")

# Pages with very little prose (frontmatter-only hub pages, redirects, pure
# reference tables) produce meaningless scores; skip them from analysis.
MIN_WORDS = 50

# Auto-generated or non-prose sections that aren't worth readability review.
# Kept in sync with find_style_issues.py:DEFAULT_EXCLUDES.
DEFAULT_EXCLUDES = [
    "src/content/changes",
    "src/content/reference/platform-api/cluster-apps",
    "src/content/reference/platform-api/crd",
]


def strip_markup(text: str) -> str:
    """Resolve a line of Markdown to its visible prose text."""
    text = RE_SHORTCODE.sub("", text)
    text = RE_IMAGE.sub(r"\1", text)
    text = RE_LINK.sub(r"\1", text)
    text = RE_INLINE_CODE.sub(lambda m: m.group(0).strip("`"), text)
    text = RE_HTML_TAG.sub("", text)
    text = RE_EMPHASIS.sub("", text)
    return text


def extract_prose(path: str) -> str:
    """Return the readable prose of a Markdown file.

    Skips YAML frontmatter and fenced code blocks entirely, drops heading
    markers, list markers, table rows, blockquotes and shortcode blocks, and
    resolves the remaining lines to their visible text.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
    except (OSError, UnicodeDecodeError):
        return ""

    in_frontmatter = False
    in_fence = False
    fence_marker = ""

    out: list[str] = []
    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        stripped = line.strip()

        # Frontmatter (leading --- ... ---)
        if idx == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue

        # Code fences — drop the whole block.
        fence_match = RE_FENCE.match(line)
        if fence_match and not in_fence:
            in_fence = True
            fence_marker = fence_match.group(2)[0] * 3
            continue
        if in_fence:
            if fence_match and fence_match.group(2)[0] * 3 == fence_marker and not fence_match.group(3).strip():
                in_fence = False
            continue

        # Headings — keep the words, drop the marker and any trailing {#anchor}.
        head = RE_HEADING.match(line)
        if head:
            out.append(strip_markup(RE_ANCHOR.sub("", head.group(2))))
            continue

        # Skip non-prose block starters (tables, blockquotes, raw HTML/shortcodes).
        if (
            stripped == ""
            or stripped.startswith("|")
            or stripped.startswith(">")
            or stripped.startswith("<")
            or stripped.startswith("{{")
        ):
            continue

        # List items — keep the text, drop the bullet/number marker.
        list_match = RE_LIST.match(line)
        if list_match:
            line = line[list_match.end():]

        out.append(strip_markup(line))

    return "\n".join(out)


def count_syllables_en(word: str) -> int:
    """Deterministic English syllable count based on vowel groups.

    Lowercases, keeps letters only, counts runs of vowels (a e i o u y),
    drops a trailing silent 'e' (but keeps a 'le' ending after a consonant),
    and floors the result at 1.
    """
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0

    count = 0
    prev_vowel = False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel

    # Silent trailing 'e' (e.g. "make"), unless it's a consonant + "le" ("table").
    if word.endswith("e") and not (len(word) >= 3 and word.endswith("le") and word[-3] not in VOWELS):
        count -= 1

    return max(1, count)


def extract_sentences(text: str) -> list[str]:
    return [s for s in (s.strip() for s in RE_SENTENCE_SPLIT.split(text)) if s]


def extract_words(text: str) -> list[str]:
    return RE_WORD.findall(text)


@dataclass
class Stats:
    words: int
    sentences: int
    syllables: int
    complex_words: int   # words with >= 3 syllables
    long_words: int      # words with > 6 letters

    @property
    def words_per_sentence(self) -> float:
        return self.words / self.sentences

    @property
    def syllables_per_word(self) -> float:
        return self.syllables / self.words


def compute_stats(text: str) -> Stats | None:
    words = extract_words(text)
    sentences = extract_sentences(text)
    if not words or not sentences:
        return None
    syllables = 0
    complex_words = 0
    long_words = 0
    for w in words:
        s = count_syllables_en(w)
        syllables += s
        if s >= 3:
            complex_words += 1
        if len(w) > 6:
            long_words += 1
    return Stats(
        words=len(words),
        sentences=len(sentences),
        syllables=syllables,
        complex_words=complex_words,
        long_words=long_words,
    )


def flesch_reading_ease(st: Stats) -> float:
    return 206.835 - 1.015 * st.words_per_sentence - 84.6 * st.syllables_per_word


def flesch_kincaid_grade(st: Stats) -> float:
    return 0.39 * st.words_per_sentence + 11.8 * st.syllables_per_word - 15.59


def gunning_fog(st: Stats) -> float:
    return 0.4 * (st.words_per_sentence + 100 * (st.complex_words / st.words))


def lix(st: Stats) -> float:
    return st.words_per_sentence + (st.long_words * 100 / st.words)


def interpret_flesch(score: float) -> str:
    if score >= 90:
        return "Very easy (5th grade)"
    if score >= 80:
        return "Easy (6th grade)"
    if score >= 70:
        return "Fairly easy (7th grade)"
    if score >= 60:
        return "Plain English (8th-9th grade)"
    if score >= 50:
        return "Fairly difficult (10th-12th grade)"
    if score >= 30:
        return "Difficult (college)"
    return "Very difficult (college graduate)"


def interpret_grade(grade: float) -> str:
    if grade < 6:
        return "Elementary"
    if grade < 9:
        return "Middle school"
    if grade < 13:
        return "High school"
    if grade < 17:
        return "College"
    return "Graduate"


def interpret_lix(score: float) -> str:
    if score < 25:
        return "Very easy (children's literature)"
    if score < 35:
        return "Easy (fiction)"
    if score < 45:
        return "Medium (non-fiction, newspapers)"
    if score < 55:
        return "Difficult (technical texts)"
    return "Very difficult (academic texts)"


@dataclass
class FileReport:
    path: str
    stats: Stats
    flesch: float
    fk_grade: float
    fog: float
    lix: float
    flagged: bool = False


def analyze_file(path: str) -> FileReport | None:
    text = extract_prose(path)
    st = compute_stats(text)
    if st is None or st.words < MIN_WORDS:
        return None
    return FileReport(
        path=os.path.normpath(path),
        stats=st,
        flesch=round(flesch_reading_ease(st), 2),
        fk_grade=round(flesch_kincaid_grade(st), 2),
        fog=round(gunning_fog(st), 2),
        lix=round(lix(st), 2),
    )


def collect_markdown(paths: list[str], excludes: list[str], include_index: bool = False) -> list[str]:
    def excluded(path: str) -> bool:
        return any(ex in os.path.normpath(path) for ex in excludes)

    files: list[str] = []
    for p in paths:
        # An explicitly named file is always honored (even an _index.md).
        if os.path.isfile(p) and p.endswith(".md"):
            if not excluded(p):
                files.append(p)
        elif os.path.isdir(p):
            for root, _, names in os.walk(p):
                for n in names:
                    if not n.endswith(".md"):
                        continue
                    # List/section pages are frontmatter-only by convention.
                    if n == "_index.md" and not include_index:
                        continue
                    full = os.path.join(root, n)
                    if not excluded(full):
                        files.append(full)
    return sorted(set(files))


def print_detail(r: FileReport) -> None:
    st = r.stats
    print("=" * 72)
    print("READABILITY — English")
    print("=" * 72)
    print(f"\nFile: {r.path}\n")

    print("BASIC STATISTICS")
    print("-" * 72)
    print(f"Sentences:                {st.sentences}")
    print(f"Words:                    {st.words}")
    print(f"Avg. sentence length:     {st.words_per_sentence:.2f} words")
    print(f"Avg. syllables per word:  {st.syllables_per_word:.2f}")
    print(f"Complex words (3+ syll.): {st.complex_words} ({100 * st.complex_words / st.words:.1f}%)")
    print()

    print("METRICS")
    print("-" * 72)
    print(f"Flesch Reading Ease:      {r.flesch:>7.2f}   {interpret_flesch(r.flesch)}")
    print(f"Flesch-Kincaid Grade:     {r.fk_grade:>7.2f}   {interpret_grade(r.fk_grade)}")
    print(f"Gunning Fog Index:        {r.fog:>7.2f}   {interpret_grade(r.fog)}")
    print(f"LIX:                      {r.lix:>7.2f}   {interpret_lix(r.lix)}")
    print()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=["src/content"], help="Files or directories to scan (default: src/content)")
    parser.add_argument("--max-grade", type=float, default=12.0, help="Flag pages above this Flesch-Kincaid grade (default: 12)")
    parser.add_argument("--min-flesch", type=float, default=None, help="Also flag pages below this Flesch Reading Ease score")
    parser.add_argument("--top", type=int, default=0, help="Only show the N hardest files")
    parser.add_argument("--exclude", action="append", default=[], metavar="SUBSTR", help="Skip paths containing SUBSTR (repeatable)")
    parser.add_argument("--no-default-excludes", action="store_true", help=f"Don't apply default excludes ({', '.join(DEFAULT_EXCLUDES)})")
    parser.add_argument("--include-index", action="store_true", help="Also score _index.md list pages (skipped by default; meant to be frontmatter-only)")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args(argv)

    paths = args.paths or ["src/content"]
    excludes = list(args.exclude)
    if not args.no_default_excludes:
        excludes += DEFAULT_EXCLUDES
    files = collect_markdown(paths, excludes, include_index=args.include_index)
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    # Single-file detailed mode.
    if len(files) == 1 and os.path.isfile(paths[0]) and not args.json:
        r = analyze_file(files[0])
        if r is None:
            print(f"Not enough prose to analyze (< {MIN_WORDS} words): {files[0]}", file=sys.stderr)
            return 1
        print_detail(r)
        return 0

    reports: list[FileReport] = []
    for f in files:
        r = analyze_file(f)
        if r is None:
            continue
        if r.fk_grade > args.max_grade or (args.min_flesch is not None and r.flesch < args.min_flesch):
            r.flagged = True
        reports.append(r)

    if not reports:
        print(f"No pages with at least {MIN_WORDS} words of prose were found.", file=sys.stderr)
        return 1

    flagged = sorted((r for r in reports if r.flagged), key=lambda r: r.fk_grade, reverse=True)
    ranked = flagged
    if args.top:
        ranked = ranked[: args.top]

    n = len(reports)
    avg_flesch = sum(r.flesch for r in reports) / n
    avg_grade = sum(r.fk_grade for r in reports) / n
    avg_fog = sum(r.fog for r in reports) / n
    avg_lix = sum(r.lix for r in reports) / n

    if args.json:
        out = {
            "scored_files": n,
            "flagged_files": len(flagged),
            "max_grade": args.max_grade,
            "min_flesch": args.min_flesch,
            "corpus_average": {
                "flesch_reading_ease": round(avg_flesch, 2),
                "flesch_kincaid_grade": round(avg_grade, 2),
                "gunning_fog": round(avg_fog, 2),
                "lix": round(avg_lix, 2),
            },
            "files": [
                {
                    "path": r.path,
                    "flesch_reading_ease": r.flesch,
                    "flesch_kincaid_grade": r.fk_grade,
                    "gunning_fog": r.fog,
                    "lix": r.lix,
                    "words": r.stats.words,
                    "sentences": r.stats.sentences,
                }
                for r in ranked
            ],
        }
        print(json.dumps(out, indent=2))
        return 0

    print(f"Scored {n} page(s); {len(flagged)} above Flesch-Kincaid grade {args.max_grade:g}"
          + (f" or below Flesch {args.min_flesch:g}" if args.min_flesch is not None else "")
          + ".\n")
    print("Corpus average:")
    print(f"  Flesch Reading Ease  {avg_flesch:7.2f}   ({interpret_flesch(avg_flesch)})")
    print(f"  Flesch-Kincaid Grade {avg_grade:7.2f}   ({interpret_grade(avg_grade)})")
    print(f"  Gunning Fog Index    {avg_fog:7.2f}")
    print(f"  LIX                  {avg_lix:7.2f}   ({interpret_lix(avg_lix)})")
    print()

    if not ranked:
        print("No pages exceed the difficulty target. 🎉")
        return 0

    print(f"Hardest page(s), worst first ({'top ' + str(args.top) if args.top else len(flagged)} of {len(flagged)} flagged):\n")
    print(f"{'FK':>6} {'Flesch':>7} {'Fog':>6} {'LIX':>6}  Path")
    print("-" * 72)
    for r in ranked:
        print(f"{r.fk_grade:6.1f} {r.flesch:7.1f} {r.fog:6.1f} {r.lix:6.1f}  {r.path}")
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
