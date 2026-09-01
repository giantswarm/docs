---
name: find-style-issues
description: Find documentation pages that need style improvements (long paragraphs, non-sentence-case headings, over-long shell code lines, and Vale findings)
argument-hint: '[path ...] [--vale] [--top N]'
---

# Find articles that need style improvements

Scan the documentation and rank pages by the number of style problems they
contain, so you know where to point [`/improve-style`](../improve-style/SKILL.md) next.

A helper script does the finding in code — don't eyeball files by hand.

## What it detects

1. **Long paragraphs** — prose paragraphs whose *reading length* (markup, link
   URLs and shortcodes stripped) exceeds **600 characters**.
2. **Headings that aren't sentence case** — a heuristic pre-filter. Brand names,
   acronyms, code identifiers and camelCase field names are allowed; Vale's
   `Microsoft.Headings` rule remains the authoritative check.
3. **Over-long shell code lines** — lines longer than **65 characters** inside
   `sh` / `bash` / `shell` / `console` fenced code blocks.
4. **Vale findings** — error / warning / suggestion counts per file (opt-in,
   needs Docker).

## Steps

1. Run the structural scan (fast, pure Python, covers all 5000+ pages):

   ```bash
   python3 .claude/skills/find-style-issues/find_style_issues.py
   ```

   By default it scans `src/content` and **excludes auto-generated sections**
   that aren't worth manual style review:
   - `src/content/changes` (changelogs)
   - `src/content/reference/platform-api/cluster-apps`
   - `src/content/reference/platform-api/crd`

2. To include Vale findings, add `--vale`. This runs the same Docker image as
   the `improve-style` skill, so it's slower — scope it to a directory or a few
   files rather than the whole tree:

   ```bash
   python3 .claude/skills/find-style-issues/find_style_issues.py --vale \
     src/content/tutorials/observability
   ```

3. Useful flags:
   - `--top N` — only show the N worst files (results are ranked by Vale errors,
     then total issue count).
   - `path ...` — one or more files or directories to scan instead of the default.
   - `--exclude SUBSTR` — skip paths containing `SUBSTR` (repeatable).
   - `--no-default-excludes` — also scan the generated sections listed above.
   - `--max-paragraph N` / `--max-code-line N` — override the thresholds.
   - `--json` — machine-readable output for further processing.

4. Report the ranked list to the user. The heading check is heuristic, so treat
   its hits as candidates to review, not certain defects. To actually fix a
   page, run `/improve-style <path>` on it.

## Example

```bash
# Worst 15 pages in the tutorials section, including Vale
python3 .claude/skills/find-style-issues/find_style_issues.py --vale --top 15 \
  src/content/tutorials
```

Output is grouped per file, e.g.:

```text
src/content/overview/security/platform-security/index.md
  long-paragraph : 2 (longest 1137 chars) — L55 (762), L180 (1137)
  heading-case   : L53 — word 'Operator' is capitalized mid-heading: "Trivy Operator"
  long-code-line : 16 (longest 158 chars) — L81 (158), L82 (158), ...
  vale           : 23 (6 error, 0 warning, 17 suggestion)
```
