---
name: export-to-miro
description: Create a box on a Miro board for every row in a CSV inventory of pages (e.g. the output of the export-csv skill) — each box shows the page title as a clickable link to its URL, with the navigation path as a subline
user-invocable: true
---

# Export a CSV of pages to boxes on a Miro board

Given a CSV with one row per page (a `title` column, a `url` column, and
`path_l1`…`path_lN` navigation columns — exactly what the `export-csv` skill
produces), create one box per row on a Miro board.

Each box is **three independent items**:

1. a `SHAPE` — the bordered rectangle (the box; no text). Its **border color encodes the
   page's Diátaxis type** when the CSV has a `diataxis_content_type` column (as the
   `export-csv` skill now produces)
2. a `TEXT` — the page **title**, larger font (size 16), as a link to the `url`
3. a `TEXT` — the **navigation path** (`path_l*` joined by `/`), smaller (size 11), gray

Border colors (matching the SIG Docs Diátaxis deck palette):

| Type | Border |
|---|---|
| `tutorial` | teal `#0D9488` |
| `how-to-guide` | blue `#2563EB` |
| `reference` | purple `#7C3AED` |
| `explanation` | amber `#D97706` |
| `none` / untagged / no column | default `--border` (`#4A6FF3`) |

Two text items are needed because a single Miro item supports only **one** font
size (see gotchas). A helper script generates the layout DSL deterministically —
don't hand-write the boxes. You then feed that DSL to the Miro MCP `layout_create`
tool.

## Prerequisites

- A CSV file to import (default assumption: `export.csv` in the working dir).
- The Miro MCP server connected, and the **target board URL** from the user
  (e.g. `https://miro.com/app/board/uXjVO2Dh15w=/`). Ask for it if not given.

## Steps

1. **Generate the DSL** from the CSV:

   ```bash
   python3 .claude/skills/export-to-miro/generate_miro_dsl.py export.csv
   ```

   This writes chunk files (`/tmp/miro_dsl_chunk_0.dsl`, `_1.dsl`, …) and prints
   the grid size, item count (3 per box), and chunk list. It splits into chunks
   because a single `layout_create` call has a ~50k-char DSL limit. Run with
   `-h` for layout options (columns, spacing, box size, fonts, colors). The
   defaults are the agreed design: box 420×120, title size 16, path size 11
   gray (`#6B7280`), 8 columns, and box borders colored by Diátaxis type (read
   from the `diataxis_content_type` column; `--type-col` to change it).

2. **Create the boxes — delegate to subagents.** Each chunk's `dsl` argument is
   large (tens of KB), and `layout_create` returns an even larger response. To
   keep that bulk out of the main agent's context, spawn **one subagent per
   chunk** and have each subagent do the work. Pass the subagent only the
   **chunk file path, the board URL, and the expected item count** — do NOT read
   the chunk file in the main agent (that would pull the big text back into the
   main context).

   Each subagent should:
   - `ToolSearch` for `mcp__claude_ai_Miro__layout_create`, then Read its chunk
     file, then call `layout_create` with `miro_url` = the board URL and `dsl` =
     the file's exact contents (the MCP tool takes a string, not a file path, so
     it must inline the text verbatim).
   - Treat a too-large/"saved to file" response as success; confirm
     `created_count` equals the expected item count (jq the saved file if
     needed). Report back only the count.

   Model/chunk-size trade-off (the subagent must reproduce the `dsl` verbatim,
   so fidelity drops as chunks grow):
   - **Sonnet** with the default ~44k chunks (≈3 chunks) — good fidelity, few agents.
   - **Haiku** with smaller chunks (`--max-chars 10000`, ≈9 chunks) — cheapest.

   The generator is deterministic, so if a chunk's count is off, just re-run the
   script and recreate that one chunk.

3. **Verify.** List the board's shapes/texts and confirm every box's title links
   correctly and nothing came through broken (see "Verifying"). Report the box
   count and board URL to the user.

## Critical gotchas (baked into the script — don't undo them)

- **One font size per item.** A `SHAPE` or `TEXT` renders all its text at a
  single size; inline `<p style='font-size:…'>` / `<span style='font-size:…'>`
  are **silently stripped**. That's why the title and path are separate `TEXT`
  items overlaid on a border `SHAPE`.

- **Single-quoted hrefs are mandatory.** Title content uses
  `<p><a href='https://…'>Title</a></p>`. With *double* quotes the anchor
  collides with the DSL's double-quoted content string and Miro **silently
  strips the link**, leaving plain text with a stray `>`. The generator always
  emits single quotes.

- **HTML-escape title and path.** The script escapes `&`, `<`, `>`, `'`, `"`.

- **No grouping.** The Miro MCP has no group tool. The only container that moves
  children together is a `FRAME`, but it adds a visible label and clicking a
  child moves only that child — not worth it. The three items per box are left
  ungrouped; group them manually in Miro if desired.

- **Boxes auto-nest into overlapping frames.** A box created at coordinates
  inside an existing frame becomes that frame's child. Usually fine. Use
  `--x0/--y0` to place the grid in empty space, or set `miro_url` to a specific
  frame (`…/?moveToWidget=<frame_id>`) to target it (children then use
  frame-relative coordinates).

- **The 200-item limit only affects frame-scoped *edits*, not creation.**
  `layout_create` happily creates hundreds of items. But once a frame holds
  more than 200 items, `layout_read`/`layout_update` *scoped to that frame* fail
  with `too many items (maximum 200)`. To edit an item in a large frame, scope
  the `layout_update` to the **individual item's** URL (`…/?moveToWidget=<id>`),
  which parses just that one item.

## Verifying

`board_list_items` for `item_type: text` returns a large JSON saved to a file.
Use `jq` on that file:

```bash
# count title items with a working docs link (expect = number of pages):
jq '[.data[] | select((.data.content // "") | test("href=.https"))] | length' <FILE>
# 0 means no link-stripped titles:
jq '[.data[] | select((.data.content // "") | test("&gt;"))] | length' <FILE>
```

## Editing or deleting individual items (gotchas)

`layout_update` does find/replace on an item's DSL. When matching content that
contains a link, two surprises:

- The canonical DSL **backslash-escapes** the link's inner quotes
  (`href=\"https://…\"`). Your `old_string` must include those backslashes —
  they are part of the DSL, not JSON artifacts.
- `layout_read` displays the link **without** the `rel="noopener noreferrer"`
  attribute, but the matcher includes it. To delete a whole item line, read it
  first, then match the full canonical line (with `rel` and escaped quotes).

To delete an item: item-scoped `layout_update` with `old_string` = the item's
exact canonical line and `new_string` = empty.

## Repairing (only if titles were created without working links)

If title items exist with stripped links (content stored as `&gt;Title…`), fix
each with an **item-scoped** `layout_update` (frame-scoped fails past 200 items):
`miro_url` = the item's `…/?moveToWidget=<id>`, `old_string` = the broken
content, `new_string` = `<p><a href='URL'>Title</a></p>`. There can be many, so
fan the repairs out across parallel subagents (Haiku is sufficient).
