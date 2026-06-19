---
name: export-csv
description: Export a CSV inventory of all documentation pages (title, navigation path levels, and public URL) from the frontmatter of every Markdown file under src/content
user-invocable: true
---

# Export a CSV inventory of all documentation pages

Generate a flat CSV listing every documentation page, so the content can be
reviewed, filtered, or analyzed in a spreadsheet.

A helper script does the work in code — don't assemble the inventory by hand.

## What it produces

A CSV file (`export.csv` by default) with one row per page and these columns:

- `title` — from the page's frontmatter
- `path_l1` through `path_l6` — the first six URL path segments, i.e. the
  navigation hierarchy
- `url` — the public docs URL (`https://docs.giantswarm.io/<relpath>`)

The script walks all `.md` files under `src/content`, reads each file's YAML
frontmatter, and derives the path levels and URL from the file location.

By default it **excludes the `/changes/` section** (changelogs, `path_l1=changes`),
which otherwise dominates the output. Adjust `EXCLUDED_SECTIONS` in the script to
change which top-level sections are skipped.

## Steps

1. Run the script (pure Python plus PyYAML, no Docker needed):

   ```bash
   python3 .claude/skills/export-csv/export_csv.py
   ```

   It writes `export.csv` to the current working directory and covers all
   pages under `src/content`.

2. Report the result to the user — the output path and how many rows were
   written. Offer to open or summarize the CSV if useful.

## Notes

- The same script also backs the `make export-csv` target, which runs it inside
  the `docs-scriptrunner` Docker image (no local Python required).
- Pages with empty content or missing frontmatter are skipped.
