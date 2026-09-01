---
name: assess-readability
description: Assess English readability of documentation pages (Flesch Reading Ease, Flesch-Kincaid grade, Gunning Fog, LIX), excluding generated content
argument-hint: '[path ...] [--top N] [--max-grade N]'
---

# Assess the readability of documentation pages

Measure how hard the prose is to read across (almost) the whole content tree, so
you can find the pages that most need simplifying — then point
[`/improve-style`](../improve-style/SKILL.md) at them.

A helper script does the measuring in code — don't eyeball files by hand.

## What it measures

For each page it strips frontmatter, code fences, shortcodes and markup, then
computes four widely-cited metrics over the remaining prose:

1. **Flesch Reading Ease** — higher is easier (0–100+). ~60–70 is "plain English".
2. **Flesch-Kincaid Grade** — approximate US school grade level needed to read it.
3. **Gunning Fog Index** — approximate years of formal education to read it.
4. **LIX** — a language-independent index (sentence length + share of long words).

Everything is computed with the Python standard library and a fixed
syllable-counting heuristic, so the assessment is **completely deterministic**:
the same input always yields the same scores. No network, no external libraries.

`_index.md` list/section pages are skipped by default — by convention they are
frontmatter-only and shouldn't carry body prose (use `--include-index` to score
them anyway). Pages with fewer than 50 words of prose (redirects, stubs) are also
skipped, since their scores would be meaningless.

## Steps

1. Sweep the whole tree and list the hardest pages (fast, pure Python):

   ```bash
   python3 .claude/skills/assess-readability/assess_readability.py --top 20
   ```

   By default it scans `src/content` and **excludes auto-generated sections**:
   - `src/content/changes` (changelogs)
   - `src/content/reference/platform-api/cluster-apps`
   - `src/content/reference/platform-api/crd`

   It prints the corpus average across all scored pages, then a table of the
   pages above the difficulty target, worst first.

2. For a detailed per-metric breakdown of one page, pass a single file:

   ```bash
   python3 .claude/skills/assess-readability/assess_readability.py \
     src/content/overview/security/platform-security/index.md
   ```

3. Useful flags:
   - `--top N` — only show the N hardest files.
   - `--max-grade N` — Flesch-Kincaid grade above which a page is flagged
     (default 12).
   - `--min-flesch N` — also flag pages below this Flesch Reading Ease score.
   - `path ...` — one or more files or directories to scan instead of the default.
   - `--exclude SUBSTR` — skip paths containing `SUBSTR` (repeatable).
   - `--no-default-excludes` — also scan the generated sections listed above.
   - `--include-index` — also score `_index.md` list pages (skipped by default).
   - `--json` — machine-readable output for further processing.

4. Report the ranked list to the user. The scores are heuristic indicators, not
   verdicts — treat high-grade pages as candidates to simplify. To actually
   improve a page, run `/improve-style <path>` on it.

## Example

```bash
# The 15 hardest tutorial pages
python3 .claude/skills/assess-readability/assess_readability.py --top 15 \
  src/content/tutorials
```

Output, worst first:

```text
Scored 94 page(s); 22 above Flesch-Kincaid grade 12.

Corpus average:
  Flesch Reading Ease    44.10   (Difficult (college))
  Flesch-Kincaid Grade    9.80   (High school)
  Gunning Fog Index      12.40
  LIX                    44.30   (Medium (non-fiction, newspapers))

Hardest page(s), worst first (top 15 of 22 flagged):

    FK  Flesch    Fog    LIX  Path
------------------------------------------------------------------------
  15.4    14.4   19.6   61.3  src/content/tutorials/.../index.md
  ...
```
