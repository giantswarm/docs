---
name: plan-diataxis-split
description: For one owner team, turn its mixed-Diátaxis pages (from issue giantswarm/giantswarm#37021) into a concrete single-purpose split plan — classify each page, pin its secondary content, and map every extraction to a target page that has been verified against the corpus as new-vs-existing. Produces the plan; does not edit pages.
user-invocable: true
argument-hint: "[owner team slug, e.g. team-atlas]"
---

# Plan a Diátaxis split for one team

Issue [`giantswarm/giantswarm#37021`](https://github.com/giantswarm/giantswarm/issues/37021)
lists ~59 docs pages that mix two or more [Diátaxis](https://diataxis.fr/) types, grouped by
`owner` team. This skill takes **one team** and produces an actionable plan to split its pages so
each serves a single type — where the secondary material goes, and which target pages already
exist versus need creating.

This skill **plans**; it does not edit article bodies. Hand the plan to the split work
(or to the per-page steps in #37021) afterwards.

## Input

From `$ARGUMENTS`: an `owner` team slug (e.g. `team-atlas`). If none is given, ask which team,
or list the teams in #37021.

## The rubric

Do **not** re-invent classification criteria. The `/classify-diataxis` skill
(`.claude/skills/classify-diataxis/`) is the single source of truth for the four types and the
two axes. Load it and apply it. One principle it's easy to get wrong, so keep it front of mind:

> A **tutorial** is something the reader does **to learn** (a lesson). A page that walks through
> steps **to accomplish a real goal** — even with a narrated worked example — is a
> **how-to-guide**, not a tutorial. Judge by the reader's intent, not the step-by-step style.

## Process

### 1. Scope the team's pages from the issue

Fetch #37021 and pull the rows under the team's heading:

```bash
gh issue view 37021 --repo giantswarm/giantswarm --json body --jq .body
```

Each row carries the page's current **primary** `diataxis_content_type` (the bracketed tag) and
its live docs URL. Note pages marked ⚡ (co-owned) — flag them, since another team may also touch
them.

### 2. Map each URL to its source file

`https://docs.giantswarm.io/<X>/` → `src/content/<X>/index.md`, or `src/content/<X>.md` for a
flat page. Confirm each file exists before analysing it.

### 3. Classify and dissect each page (fan out for scale)

For more than a handful of pages, spawn **parallel subagents**, and **group related pages into
the same agent** (e.g. all query-language pages together) so their classifications stay
consistent. Give each agent the rubric inline. For each page, require:

- **Primary type** + confidence, and whether it **disagrees** with the declared type. Always
  challenge the declared value — it is frequently wrong (a page titled "…tutorial" is often
  reference; a page in `tutorials/` is often a how-to).
- **Secondary content**: which type(s) the page *also* serves, citing the specific headings /
  passages that carry each secondary mode.
- **Extraction proposal**: for each secondary block, the destination page (path under
  `src/content/`), its Diátaxis type, and how the pages should cross-link.

### 4. Verify every target against the corpus — BEFORE proposing it as "new"

This is the step most easily skipped, and the most costly to skip: much of the "secondary"
content already has a home. **Do not propose creating a page without checking.** For team-atlas,
6 of 8 targets already existed.

```bash
# What already exists in the relevant section?
find src/content/<section> -name '*.md' | sort
# Read a section _index.md — its user_questions/body often already cover a "how to access X"
sed -n '1,120p' src/content/<section>/_index.md
# Does a concept / reference already live somewhere?
grep -rliE '<concept-or-term>' --include='*.md' src/content
# CRD / reference pages
ls src/content/reference/platform-api/crd/ | grep -i <name>
```

Tag each target **existing** (relref / extend it — never recreate) or **new** (must be authored).

### 5. Find consolidation opportunities

Look across the team's pages for the *same* reference or concept repeated on several pages
(schemas, endpoints, a routing model). These converge into one **shared target** — the split is
also a de-duplication. Record which pages feed each shared target (the fan-in).

### 6. Untangle dependencies

Separate work that can **start now** (independent, parallelisable) from work that is **blocked**
(e.g. duplicate pages that need a keep-vs-redirect decision first, or ⚡ co-owned pages needing
another team). Present ready-now items at equal priority — resist a false 1→N ordering.

## Output

The plan must contain:

1. A **summary table**: page · declared type · assessed primary type · secondary content.
2. **Per-page plans**: what stays, what's extracted, each extraction's target path + type +
   existing/new status, cross-linking, and any `aliases` needed.
3. **Shared targets**: each with type, existing/new, and its feeder pages.
4. **Suggested order**: ready-now vs blocked.

### Always render the plan as an Artifact

Produce a self-contained HTML **Artifact by default** — don't wait to be asked. (Load the
`artifact-design` skill first to calibrate the treatment; this is an information-dense internal
planning doc, not an editorial page.) It must include all four output sections above, plus a
**content-flow graph**, and it should encode the Diátaxis types as a consistent colour system
throughout. Concretely:

- **Header + summary stats**: team slug, page count, how many change their declared type, how
  many new pages vs. existing targets to reuse, count of shared consolidation targets.
- **A Diátaxis legend**: the four types as a 2×2 compass (study/work × action/cognition) in the
  colour system used everywhere else (one hue per type; reserve a separate "state" colour for
  pages whose declared type flips).
- **A content-flow graph** — the centrepiece. Every existing page, new page, and shared target
  is a node; every arrow is content moving out of a page into its new home. Requirements:
  - Lay it out in columns (e.g. existing pages → new pages → shared targets) so most edges read
    left-to-right and the fan-in onto shared targets is visible.
  - Colour each edge by its **destination type**; colour/stripe each node by its own type.
  - Mark nodes **new** vs **existing** distinctly (existing targets must not read as new work).
  - Make it interactive: hovering/tapping a node highlights just its edges and neighbours so a
    single page's fan-out (or a target's fan-in) is traceable in the dense middle.
  - Build it self-contained (hand-rolled SVG + positioned nodes) — the Artifact CSP blocks
    external libraries and font/CDN requests.
- **Per-page cards**, grouped by section, each showing `current → target` type, what stays, the
  extraction chips (dotted by destination type, marking shared targets), a live link to the docs
  page, and any flags (e.g. a duplicate to resolve, a bug spotted, invalid examples).
- **Shared-targets panel**: each target with its path, type, existing/new tag, and feeder pages.
- **Suggested order** as ready-now vs blocked lanes.
- **Theme-aware** (light/dark) and responsive; wide content scrolls inside its own container.

Redeploy to the **same** Artifact file/URL when iterating, rather than minting a new one.

### Also offer (don't do unprompted)

- A **sub-issue** of #37021 for the team, linking the Artifact (GitHub sub-issues API:
  `gh api --method POST repos/giantswarm/giantswarm/issues/37021/sub_issues -F sub_issue_id=<id>`).
  Note the Artifact is private by default — the user must share it for teammates to open.

## Mechanics the plan must respect (issue #37021, steps 4–6)

- Set `diataxis_content_type` correctly on **every** resulting page (original + new).
- Cross-link with the `relref` shortcode; give each hub page a "Next steps" / "See also".
- Any moved/renamed page → add an `aliases` entry for the old path and update inbound links.
- Changed pages get `/improve-style`; the `validate` CI check must stay green.
- On each PR, add the page's `owner` team as a reviewer.
- Do **not** bump `last_review_date` for a pure `diataxis_content_type` change (mechanical, not a
  content review).
