---
name: classify-diataxis
description: Classify documentation pages into their Diátaxis type and propose the diataxis_content_type frontmatter value, flagging pages that mix modes
user-invocable: true
argument-hint: "[file path, glob, or 'diff']"
---

# Classify pages by Diátaxis type

Decide which [Diátaxis](https://diataxis.fr/) type a page is, and propose its
`diataxis_content_type` frontmatter value. This skill is the **single source of truth**
for the rubric — other skills and reviewers defer to it.

## Target

From `$ARGUMENTS`:

- a **file path** → classify that page
- a **glob** (e.g. `src/content/tutorials/**`) → classify each matching article
- `diff` → classify the article pages changed in the current working tree / branch

If no argument is given, ask what to classify. Skip `_index.md` list pages — they don't
carry the field.

## The rubric

Diátaxis splits docs along two axes: **study vs. work** (is the reader learning or doing a
job?) and **action vs. cognition** (do they need steps or knowledge?). That yields four types:

- **`tutorial`** (study + action) — a learning-oriented **lesson**. Takes a beginner by the
  hand through steps to build confidence and familiarity; the learning experience matters
  more than the end result. No options, no digressions, no explaining-why.
- **`how-to-guide`** (work + action) — a task-oriented **recipe**. Steps to solve a specific
  real-world problem for someone who already knows the basics. Goal-focused, assumes
  competence, may offer choices. Titles often start with a verb ("Configure…", "Expose…",
  "Set up…", "Deploy…", "Migrate…").
- **`reference`** (work + cognition) — an information-oriented **description**. Dry, factual,
  structured: CLI flags, command usage, CRD/chart schemas, config keys, annotation/label
  lists, API fields. Describes the machinery; doesn't teach or explain why.
- **`explanation`** (study + cognition) — an understanding-oriented **discussion**. Concepts,
  architecture, background, the "why", trade-offs. Read away from the keyboard. Titles often
  "Introduction to…", "What is…", "How X works", "…concepts".

Use **`none`** only for pages outside the framework (support, meta).

### How to decide

1. Read the **full page**, not just the title or frontmatter.
2. Ask the two axis questions: is the reader **acquiring** skill (study) or **applying** it
   (work)? Does the page serve **action** (steps) or **cognition** (knowledge)?
   - study + action → `tutorial`
   - work + action → `how-to-guide`
   - work + cognition → `reference`
   - study + cognition → `explanation`
3. **Ignore the folder.** This repo's folders are mixed — the `tutorials/` folder holds many
   how-to guides, some explanations, and some reference; `overview/` is mostly explanation.
   Classify by the page's dominant purpose and writing style.
4. A page is **mixed** if it substantially serves more than one type — usually two, but
   sometimes three or four (e.g. a how-to that embeds a long conceptual section and a big
   reference table). Still pick the single best **primary** type for the field, and flag the
   page — noting the other types it carries — for a possible later split.

## Output

For each page report: `path`, proposed `diataxis_content_type`, confidence
(high / medium / low), whether it's `mixed` (and which other type(s) it carries), and a
one-line rationale. Then, unless told otherwise, set the `diataxis_content_type` field in the
frontmatter of each page, right after `title`.

This skill only touches frontmatter — there's no need to run `/improve-style`, and don't
change `last_review_date` when only setting the type (that's a mechanical change, not a
content review).
