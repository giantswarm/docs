# Write observability documentation

Create or edit a page in the observability section of the Giant Swarm docs.

If a file path or topic is provided as an argument (`$ARGUMENTS`), use that as the target. Otherwise, ask the user what page they want to create or edit.

## Steps

1. **Consult reference resources** before writing. Read relevant sections from:
   - [Giant Swarm Public Docs](https://docs.giantswarm.io/) — existing observability pages for context and consistency
   - [Giant Swarm Intranet](https://intranet.giantswarm.io/docs/) — internal context where needed
   - [Grafana Documentation](https://grafana.com/docs/) — for Grafana-specific features

2. **Determine the page type**:
   - **Conceptual** — explains what something is, its purpose, and how it fits into the platform
   - **Tutorial** — step-by-step instructions for performing a specific task

3. **Place the page correctly** in the documentation hierarchy (see AGENTS.md for the full structure). Determine the correct path under `src/content/overview/observability/` or `src/content/getting-started/`.

4. **Write the page** following these rules:
   - Start with a brief introduction explaining relevance and what the reader will learn
   - Use clear, descriptive headings to break content into sections
   - Include practical examples and step-by-step instructions where applicable
   - Use bullet points and numbered lists for clarity
   - Format and explain all code snippets
   - Keep prose minimal; link to other docs or external resources rather than repeating content
   - Conclude with a summary or next steps

5. **Add required frontmatter** at the top of the file:

   ```yaml
   ---
   title: "Clear, concise title"
   description: "Brief description of the page's content and purpose."
   user_questions:
     - A question users might have that this page answers
   owner:
     - https://github.com/orgs/giantswarm/teams/team-atlas
   last_review_date: YYYY-MM-DD
   ---
   ```

6. **If moving or renaming an existing page**:
   - Add or update the `aliases` field with the old path so existing links redirect correctly
   - Update all internal links pointing to the old path
   - Verify the `menu` field reflects the correct hierarchy

7. **Run style checks** using `/improve-style` on the finished page.

Follow the Giant Swarm style guide defined in AGENTS.md: conversational tone, American English, sentence case headings, Oxford comma, contractions, and active voice.
