---
name: mermaid-diagrams
description: Use when adding or editing mermaid diagrams
argument-hint: '[file-path]'
---

# Mermaid diagrams

Add or edit a Mermaid diagram on a docs page, and verify it's readable once rendered.

If a file path is provided (`$ARGUMENTS`), work on the diagrams in that page. Otherwise, ask the user which page and diagram to work on.

## How diagrams render

Mermaid source is rendered to SVG in the reader's browser, not at build time. The pieces:

- `src/layouts/shortcodes/mermaid.html` wraps the diagram source in `<div class="mermaid">`.
- `src/layouts/_default/single.html` includes `src/layouts/partials/mermaid.html`, which loads Mermaid from jsDelivr, only on pages whose frontmatter sets `mermaid: true`. The partial also gives every diagram shrunk below 90% of its natural width an **Expand** button that shows it in a full-window dialog, fitted to the window but with text no smaller than 12 px. That's a fallback for diagrams that can't be made narrow enough, not a substitute for step 3.
- `params.mermaid` in `src/config.yaml` sets the theme, alignment, and font (Roboto, to match the body text); `src/assets/styles/_mermaid.sass` centers the diagram and sets the label weight.

Mermaid measures each label in the browser to size its box, so site CSS that changes the text's size or weight after measuring crops the text. If labels are cut off, look for a site rule that matches a Mermaid class (such as Bootstrap's `.label`) and neutralize it in `_mermaid.sass`.

There's no render hook for fenced code blocks, so a ```` ```mermaid ```` block shows up as code, not as a diagram.

## Steps

1. **Enable Mermaid on the page** by adding `mermaid: true` to its frontmatter. Without it, the page shows the raw diagram source as text.

2. **Wrap the diagram** in the shortcode, fenced by Vale directives:

   ```markdown
   <!-- vale off -->
   {{< mermaid >}}
   flowchart TB
     client["MCP client"]
     edge["Edge Gateway<br/>TLS termination"]

     client -- "HTTPS" --> edge
   {{< /mermaid >}}
   <!-- vale on -->
   ```

   `.vale.ini` only ignores fenced code blocks, so without the directives Vale lints node IDs and labels as prose.

3. **Fit the diagram to the content column.** The column is at most about 650 px wide, whatever the screen width, and narrower on small screens. Mermaid shrinks the whole SVG to fit the column, so a flowchart that's naturally 1,000 px wide renders its 12 px labels at under 8 px. Keep the natural width to about 700 px for a flowchart, or about 950 px for a sequence diagram, whose text starts at 16 px:
   - Use `flowchart TB` for a chain of more than three nodes. A left-to-right chain grows with every node; a top-to-bottom one only grows downward.
   - Use `flowchart LR` only for short chains or fan-outs with a few targets.
   - Keep labels to a name plus a short line or two. Split lines with `<br/>`, and move lists (of servers, components, and so on) into the surrounding prose.
   - Keep `sequenceDiagram` participants few and aliases short; every participant adds a column.

4. **Explain the diagram in prose.** Put the key point in the text before or after the diagram, so readers who can't see the SVG still get it.

5. **Measure the rendered diagram** (see [Measure the effective font size](#measure-the-effective-font-size)). The effective label size should be at least 11 px at desktop width. If it isn't, go back to step 3.

## Measure the effective font size

Start the local preview with `make dev`, then open the page under the URL it prints (`Web Server is available at …`) in a browser 1440 px wide or wider. With the Chrome DevTools MCP, run this with `evaluate_script`; without it, paste the function body into the browser's DevTools console:

```js
() => [...document.querySelectorAll('div.mermaid')].map((div, i) => {
  const svg = div.querySelector('svg');
  if (!svg) return { diagram: i, rendered: false };
  const label = svg.querySelector('.nodeLabel') || svg.querySelector('.messageText') || svg.querySelector('text');
  const fontPx = parseFloat(getComputedStyle(label).fontSize);
  const scale = svg.getBoundingClientRect().width / svg.viewBox.baseVal.width;
  return {
    diagram: i,
    naturalWidthPx: Math.round(svg.viewBox.baseVal.width),
    columnWidthPx: Math.round(div.getBoundingClientRect().width),
    scale: +scale.toFixed(2),
    effectiveFontPx: +(fontPx * scale).toFixed(1),
  };
})
```

`effectiveFontPx` is the label size a reader sees. A `scale` well below 1 means the diagram is too wide for the column. Repeat at a phone-sized width to see the worst case.
