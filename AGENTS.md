# Giant Swarm Docs – Agent Instructions

This file provides detailed guidance for Claude agents working in this repository. The docs site is built with Hugo and published at <https://docs.giantswarm.io/>.

## Project structure

- `src/content/` — all documentation pages in Markdown
- `src/` — Hugo site root (layouts, static assets, config)
- `Makefile` — common tasks: `make lint`, `make lint-prose`, `make lint-markdown`

---

## Style guide

> Writing isn't a test. Even if you ignore all these guidelines, that's okay — that's what good editing is all about. Write how you feel, and SIG Content + SIG Docs will be there to support and shape your ideas.

### Voice

We sound like behind-the-scenes experts (sherpas) helping the reader climb the mountain. Key principles:

- **Be conversational** — write how you speak, encourage a two-way conversation
- **Be concise** — get to the point, make it digestible in word choice and formatting
- **Show personality** — if you have fun writing it, the reader will have fun reading it
- **Be generous with knowledge** — include helpful links, add TL;DRs
- **Be nice** — write how you'd like to be written to

Start sentences with verbs to keep things punchy:

> ✔️ Write punchy content by keeping sentences short.
> ❌ The way to write punchy content is by keeping sentences short.

Never be condescending or snobby. Don't write like a robot.

### Language and grammar

- Use contractions: `it's` not `it is`, `you're` not `you are`, `we're` not `we are`
- Use the Oxford comma in lists of three or more items
- Use **American English**: `center` not `centre`, `optimize` not `optimise`
- Spell out numbers one to ten; use numerals for 11 and above
- Don't use ellipses (`…`) for drama — only to indicate trailing off or omission in quotes

### Capitalization

Use **sentence case** everywhere (blog, website, docs, social media). Only capitalize the first word of a sentence, plus proper nouns and brand names.

- Don't use internal capitalization: ❌ `e-Commerce`
- When spelling out acronyms, only capitalize if it's a proper noun
- When using a slash (e.g., `On/Off`), match the case: `lowercase/lowercase` or `Uppercase/Uppercase`

### Words to avoid

| Avoid | Use instead |
|---|---|
| `utilize`, `leverage` | `use` |
| `Kubeception` | — |
| `Hyperconvergence` | — |
| `guru`, `ninja`, `rockstar` | — |
| `ideation` | `brainstorming` |
| `Draughtsman` (deprecated GS term) | — |
| `Giantnetes` (deprecated GS term) | — |

### Bias-free language

| Avoid | Use |
|---|---|
| chairman | chair, moderator |
| mankind | humanity, people, humankind |
| mans | operates, staffs |
| salesman | sales representative |
| manmade | manufactured, synthetic |
| manpower | workforce, staff, personnel |
| sane (defaults) | sensible (defaults) |
| guys | folks / folx |
| he/she, him/her | they / theirs |

### Technical writing fundamentals

- Use terms consistently
- Avoid ambiguous pronouns
- Prefer active voice over passive voice
- Pick specific verbs over vague ones
- Focus each sentence on a single idea
- Convert long sentences to lists where appropriate
- Eliminate unneeded words
- Use numbered lists when order matters, bulleted lists when it doesn't
- Keep list items parallel
- Start numbered list items with imperative verbs
- Introduce lists and tables with a sentence
- Create opening sentences that establish a paragraph's central point
- Focus each paragraph on a single topic

---

## Content rules (all `src/content/**/*.md`)

### URL to path mapping

- `src/` is the Hugo site root, published at `https://docs.giantswarm.io/`
- URL path → file path:
  - `https://docs.giantswarm.io/overview/security/platform-security/` → `src/content/overview/security/_index.md`
  - `https://docs.giantswarm.io/overview/observability/alert-management/alert-routing/` → `src/content/overview/observability/alert-management/alert-routing/index.md`

### Markdown

- Leave a blank line between a heading and the following paragraph
- The page title comes from the `title` frontmatter field — do **not** add an H1 in the body
- Run markdown lint after editing

### Linking

- Use the `relref` shortcode for all internal links (links to other pages on `docs.giantswarm.io`)
- The relref parameter always starts with a forward slash
- Example: `{{< relref "/overview/security/platform-security/" >}}`

---

## Observability documentation (`src/content/**/observability/**/*.md`)

Additional rules apply when writing or editing observability documentation.

### Role

You are a technical writer for Giant Swarm, writing documentation for the observability section. Content should be clear, concise, and helpful for users with varying levels of expertise.

### Structure

The observability documentation hierarchy:

```
Overview
└── Observability
    ├── Data Management
    │   ├── Data Exploration
    │   │   ├── Advanced LogQL Tutorial
    │   │   └── Advanced PromQL Tutorial
    │   ├── Data Ingestion
    │   ├── Data Transformation
    │   └── Data Export (Observability Platform API)
    ├── Dashboard Management
    │   ├── Dashboard Exploration
    │   └── Dashboard Creation
    ├── Alert Management
    │   ├── Alert Rules
    │   ├── Alert Routing
    │   └── Silences
    └── Configuration
        ├── Initial Platform Setup
        └── Multi-Tenancy
            └── Creating Grafana Organisations
Getting Started
└── Observe your clusters and apps  (/getting-started/observe-your-clusters-and-apps/)
```

### Page types

1. **Conceptual pages** — overview of a topic: its purpose, how it fits into the platform, relevance to users
2. **Tutorial pages** — step-by-step instructions to perform specific tasks

### Page structure

Every observability page should:

- Open with a brief introduction explaining relevance and what the reader will learn
- Use clear, descriptive headings to break content into sections
- Include practical examples and step-by-step instructions where applicable
- Use bullet points and numbered lists for clarity
- Format and explain all code snippets
- Keep prose minimal; link to other docs or external resources
- Conclude with a summary or next steps

### Required frontmatter

Every observability page must include:

```yaml
title: "Clear, concise title"
description: "Brief description of the page's content and purpose."
user_questions:
  - Question users might have that this page answers
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: YYYY-MM-DD
```

### Moving or renaming pages

When moving or renaming an observability page:

- Add or update the `aliases` field with the old path to redirect existing links
- Update all existing internal links pointing to the old path
- Verify the `menu` field reflects the correct hierarchy

### Reference resources

Before writing observability documentation, consult:

- [Giant Swarm Public Docs](https://docs.giantswarm.io/)
- [Giant Swarm Intranet](https://intranet.giantswarm.io/docs/)
- [Giant Swarm GitHub](https://github.com/giantswarm)
- [Grafana Documentation](https://grafana.com/docs/)

---

## Skills

These are available as Claude slash commands, defined as skills in `.claude/skills/`.

### `/fix-internal-links`

Finds and fixes broken internal links by running the linkchecker Docker image against a local copy of the published docs site. Updates permanent redirects (301) to point directly to the target URL. Always converts updated internal links to use the `relref` shortcode.

### `/fix-external-links`

Finds and fixes broken external links by running the linkchecker Docker image with `--check-extern`. Fixes permanent redirects (301) to point to the real URL. Attempts web search to find replacement pages for 404 errors. Skips: non-permanent redirects within the same domain, `example.com` links, server errors (5xx), and timeouts.

### `/improve-style`

Applies style fixes and runs Vale prose linting on modified/added pages (or a specified file path). Fixes grammar issues, then resolves Vale errors → warnings → suggestions in order. Does not modify the meaning of the content or remove any detail.

Vale image: `gsoci.azurecr.io/giantswarm/vale:v3.11.2@sha256:27aab968708850a6cc7369dc1325f1812e2c3de0741327fa0aed832e328357d7`

### `/write-observability-docs`

Guided workflow for creating or editing a page in the observability section. Consults reference resources, determines the correct page type (conceptual or tutorial) and placement in the hierarchy, writes the page with required frontmatter, and handles page moves/renames (aliases, internal link updates, menu). Ends by running `/improve-style` on the result.
