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

### Section and list pages

- An `_index.md` is a section's list page — it renders an auto-generated index of its child pages (their titles and `description`s). Keep it to frontmatter only; don't add a body
- Put general or introductory content about a section on a dedicated overview or introduction page inside the section, sorted to the top of the menu with the lowest `weight` (use `linkTitle: Introduction` so the menu entry stays short). See `src/content/overview/developer-portal/` for the pattern
- The list page's frontmatter `description` is what appears as the section summary, so make it a good standalone description

### Required frontmatter

Article pages (an `index.md`, or any page that isn't an `_index.md` list page) must carry these fields. CI enforces them via the frontmatter validator:

- `title` — the page title (don't also add an H1 in the body)
- `description` — a single standalone sentence, 50–300 characters, ending in a full stop
- `owner` — one or more GitHub team URLs (`https://github.com/orgs/giantswarm/teams/<team>`)
- `user_questions` — questions the page answers, each ending in a question mark
- `last_review_date` — `YYYY-MM-DD`
- `diataxis_content_type` — the page's Diátaxis type (see [Page types](#page-types--the-diátaxis-model))
- `weight` — when the page has a `menu` entry

`_index.md` list pages are exempt from `user_questions` and `diataxis_content_type`. Some sections (changes, support, meta) are relaxed by config; see `scripts/frontmatter-validator/config-default.yaml`.

### Markdown

- Leave a blank line between a heading and the following paragraph
- The page title comes from the `title` frontmatter field — do **not** add an H1 in the body
- Run markdown lint after editing

### Linking

- Use the `relref` shortcode for all internal links (links to other pages on `docs.giantswarm.io`)
- The relref parameter always starts with a forward slash
- Example: `{{< relref "/overview/security/platform-security/" >}}`

### Page structure

A typical article:

- Opens with a brief introduction explaining relevance and what the reader will learn
- Uses clear, descriptive headings to break content into sections
- Includes practical examples and step-by-step instructions where applicable
- Uses bullet points and numbered lists for clarity
- Formats and explains all code snippets
- Keeps prose minimal; links to other docs or external resources rather than repeating content
- Concludes with a summary or next steps

### Moving or renaming pages

- Add or update the `aliases` field with the old path so existing links redirect
- Update all internal links pointing to the old path
- Verify the `menu` field reflects the correct hierarchy

---

## Page types — the Diátaxis model

These rules apply to **every** topic — there's one page-type model for the whole docs site.

Each article belongs to exactly one [Diátaxis](https://diataxis.fr/) type, recorded in the `diataxis_content_type` frontmatter field. The four types serve four different reader needs. Keep each page in a single type and deliberately leave the other modes out — that's where the value is.

| `diataxis_content_type` | Orientation | What it is |
|---|---|---|
| `tutorial` | Learning | A lesson that takes a beginner through steps to build confidence and familiarity. No options, no "why" digressions. |
| `how-to-guide` | Task | A recipe that solves a specific real-world problem for someone who already knows the basics. Goal-focused; assumes competence; may offer choices. |
| `reference` | Information | A dry, accurate description of the machinery — CLI flags, CRD/chart fields, config keys. Describes; doesn't teach or explain. |
| `explanation` | Understanding | A discussion of concepts, architecture, trade-offs, and the "why". Read away from the keyboard. |

Use `none` only for pages outside the framework (for example support or meta pages).

**Don't classify by folder.** The folder a page lives in doesn't determine its type — many pages under `tutorials/`, for instance, are really how-to guides or explanations. Judge by the page's actual purpose and writing style. When in doubt, run `/classify-diataxis` (see Skills).

A page should serve a single type. If you find yourself mixing modes — a how-to that stops to explain concepts, a reference padded with tutorials — split the extra material into its own page of the right type and link to it.

---

## Skills

These are available as Claude slash commands, defined as skills in `.claude/skills/`.

### `/fix-internal-links`

Finds and fixes broken internal links by running the linkchecker Docker image against a local copy of the published docs site. Updates permanent redirects (301) to point directly to the target URL. Always converts updated internal links to use the `relref` shortcode.

### `/fix-external-links`

Finds and fixes broken external links by running the linkchecker Docker image with `--check-extern`. Fixes permanent redirects (301) to point to the real URL. Attempts web search to find replacement pages for 404 errors. Skips: non-permanent redirects within the same domain, `example.com` links, server errors (5xx), and timeouts.

### `/improve-style`

Applies style fixes and runs Vale prose linting on modified/added pages (or a specified file path). Fixes grammar issues, then resolves Vale errors → warnings → suggestions in order. Does not modify the meaning of the content or remove any detail.

Vale image: see Makefile (VALE_IMAGE)

### `/classify-diataxis`

Classifies a page (or a glob of pages, or the current diff) into its Diátaxis type and proposes the `diataxis_content_type` value, flagging pages that mix modes. Holds the shared classification rubric — the single source of truth for deciding a page's type.

### `/write-observability-docs`

Guided workflow for creating or editing a page in the observability section. Consults reference resources, determines the page's Diátaxis type (deferring to the `/classify-diataxis` rubric) and its placement, writes the page with the required frontmatter (including `diataxis_content_type`), and handles page moves/renames (aliases, internal link updates, menu). Ends by running `/improve-style` on the result.

### `/publish-crd-reference`

Explains how the generated CRD reference pages under `/reference/platform-api/crd/` are produced from `scripts/update-crd-reference/config.yaml`, and helps register a new CRD source repo or make sure a published CRD's page shows an example CR — including the exact rule the generator uses to find an example file (`{cr_path}/{group}_{version}_{singular}.yaml`). Use when a CRD page is missing or renders without an example.
