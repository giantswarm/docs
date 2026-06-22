"""Generate Miro layout DSL from a CSV inventory of pages.

Reads a CSV with a title column, a url column, and any number of `path_l*`
columns (e.g. the output of the `export-csv` skill) and emits Miro layout DSL
laying out one "box" per row in a grid. Each box is composed of THREE
independent items:

  1. a SHAPE  — the bordered rectangle (the box itself; no text)
  2. a TEXT   — the page title, larger font, as a clickable link to the URL
  3. a TEXT   — the navigation path (path_l* joined by "/"), smaller, gray

Two text items are used because a single Miro shape/text item supports only
ONE font size — inline `font-size` styles are silently stripped. Overlaying a
large title TEXT and a small path TEXT on a border SHAPE is the only way to get
two sizes per box.

The three items are NOT grouped: the Miro MCP exposes no grouping tool, and a
FRAME (the only container that moves children together) adds a visible label
and awkward click-to-move behavior. Group the items manually in Miro if needed.

The DSL is meant to be fed to the Miro MCP `layout_create` tool, split into
chunk files because a single call has a ~50k-char DSL limit.

IMPORTANT detail this script encodes (learned the hard way):
links MUST use SINGLE-quoted hrefs (`<a href='...'>`). Miro shape/text content
silently strips anchors whose href uses double quotes, because they collide
with the double-quoted DSL content string.

Usage:
    python3 generate_miro_dsl.py INPUT.csv [options]

Run with -h for the full option list.
"""

import argparse
import csv
import html
import math
import sys


def esc(s):
    """HTML-escape a value for safe inclusion in item content."""
    return html.escape((s or "").strip(), quote=True)


def main():
    ap = argparse.ArgumentParser(description="Generate Miro layout DSL from a CSV.")
    ap.add_argument("csv_path")
    ap.add_argument("--out-prefix", default="/tmp/miro_dsl_chunk")
    # Grid
    ap.add_argument("--cols", type=int, default=8)
    ap.add_argument("--gap-x", type=int, default=460, help="spacing between box centers, x")
    ap.add_argument("--gap-y", type=int, default=170, help="spacing between box centers, y")
    ap.add_argument("--x0", type=float, default=None, help="x center of first column (default: centered on 0)")
    ap.add_argument("--y0", type=float, default=-2000.0, help="y center of first row")
    # Box geometry (Option B)
    ap.add_argument("--box-width", type=int, default=420)
    ap.add_argument("--box-height", type=int, default=120)
    ap.add_argument("--border", default="#4A6FF3")
    ap.add_argument("--text-pad", type=int, default=40, help="box_width - text_width")
    # Title text
    ap.add_argument("--title-size", type=int, default=16)
    ap.add_argument("--title-dy", type=int, default=-28, help="title center offset from box center, y")
    # Path text
    ap.add_argument("--path-size", type=int, default=11)
    ap.add_argument("--path-dy", type=int, default=32, help="path center offset from box center, y")
    ap.add_argument("--path-color", default="#6B7280")
    # Plumbing
    ap.add_argument("--max-chars", type=int, default=44000)
    ap.add_argument("--title-col", default="title")
    ap.add_argument("--url-col", default="url")
    args = ap.parse_args()

    with open(args.csv_path, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    for required in (args.title_col, args.url_col):
        if required not in fieldnames:
            sys.exit(f"error: column '{required}' not found in {args.csv_path}. "
                     f"Columns present: {', '.join(fieldnames)}")

    path_cols = sorted(
        (c for c in fieldnames if c.startswith("path_l") and c[len("path_l"):].isdigit()),
        key=lambda c: int(c[len("path_l"):]),
    )

    n = len(rows)
    if n == 0:
        sys.exit("error: CSV has no data rows.")

    cols = max(1, args.cols)
    x0 = args.x0 if args.x0 is not None else -(cols - 1) * args.gap_x / 2
    text_w = args.box_width - args.text_pad

    lines = []
    for i, r in enumerate(rows):
        cx = int(round(x0 + (i % cols) * args.gap_x))
        cy = int(round(args.y0 + (i // cols) * args.gap_y))

        title = esc(r.get(args.title_col, ""))
        url = (r.get(args.url_col, "") or "").strip()
        path = esc("/".join(p for p in (r.get(c, "") for c in path_cols) if p and p.strip()))

        # Single-quoted href is REQUIRED — double quotes would clash with the
        # double-quoted DSL content string and Miro would strip the link.
        lines.append(
            f"b{i}box SHAPE x={cx} y={cy} w={args.box_width} h={args.box_height} "
            f"type=rectangle fill=#FFFFFF border_color={args.border} "
            f'size=12 valign=middle align=left ""'
        )
        lines.append(
            f"b{i}t TEXT x={cx} y={cy + args.title_dy} w={text_w} align=left "
            f'size={args.title_size} "<p><a href=\'{url}\'>{title}</a></p>"'
        )
        lines.append(
            f"b{i}p TEXT x={cx} y={cy + args.path_dy} w={text_w} align=left "
            f'size={args.path_size} color={args.path_color} "<p>{path}</p>"'
        )

    # Pack lines into chunks under the size limit. Items are independent
    # (no cross-line aliases), so chunk boundaries can fall anywhere.
    chunks = []
    cur, cur_len = [], 0
    for ln in lines:
        if cur and cur_len + len(ln) + 1 > args.max_chars:
            chunks.append(cur)
            cur, cur_len = [], 0
        cur.append(ln)
        cur_len += len(ln) + 1
    if cur:
        chunks.append(cur)

    n_rows = math.ceil(n / cols)
    out = []
    for idx, c in enumerate(chunks):
        path = f"{args.out_prefix}_{idx}.dsl"
        with open(path, "w") as fh:
            fh.write("\n".join(c))
        out.append((path, len(c), sum(len(l) + 1 for l in c)))

    print(f"rows={n} grid={cols}x{n_rows} items={len(lines)} (3/box) chunks={len(chunks)}")
    for path, count, size in out:
        print(f"  {path}  ({count} items, {size} chars)")


if __name__ == "__main__":
    main()
