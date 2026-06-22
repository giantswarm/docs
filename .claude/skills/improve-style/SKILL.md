---
name: improve-style
description: Apply style fixes and run Vale prose linting on modified or added pages
argument-hint: '[file-path]'
---

# Improve writing style and formatting

Apply style fixes and run Vale prose linting on modified or added pages.

## Steps

1. Determine which files to process:
   - If a file path was passed as an argument (`$ARGUMENTS`), use that file
   - Otherwise, check git to find pages that were added or modified compared to the base branch

2. Run Vale linting on the target file(s). For this, read the `VALE_IMAGE` from `Makefile` first. Then:

   ```bash
   docker run --rm \
     -v $PWD:/workdir \
     -w /workdir \
     $VALE_IMAGE \
     --config=/workdir/.vale.ini \
     --no-wrap \
     <relative-path-to-markdown-file>
   ```

3. Resolve Vale findings in order of severity: **errors first**, then **warnings**, then **suggestions**.

4. Fix obvious grammar problems. When in doubt, explain the issue to the user and let them decide.

5. Make sure longer paragraphs provide some anchors for the eye, by emphasizing a few key words or key phrases.

   Example (before)

   > Network traffic, particularly cross-availability zone (cross-AZ) and egress traffic, is often a hidden but significant cost driver in cloud environments. Cloud providers typically charge for data transfer between availability zones. For example, AWS charges approximately $0.01/GB for cross-AZ traffic, and these costs can add up quickly in distributed systems.

   Exmaple (after)

   > Network traffic, particularly cross-availability zone (cross-AZ) and egress traffic, is often a **hidden but significant cost driver** in cloud environments. Cloud providers typically charge for data transfer between availability zones. For example, AWS charges approximately $0.01/GB for cross-AZ traffic, and these costs can **add up quickly** in distributed systems.

6. Assess readability — **only after** the Vale findings above are resolved.

   Vale's suggestions (sentence length, passive voice, wordiness, complex words)
   overlap with what the readability metrics measure, so fixing them first often
   moves the scores on its own. Re-measure on the already-improved text:

   ```bash
   python3 .claude/skills/assess-readability/assess_readability.py <relative-path-to-markdown-file>
   ```

   This prints the page's Flesch Reading Ease, Flesch-Kincaid grade, Gunning Fog
   and LIX (see [`/assess-readability`](../assess-readability/SKILL.md)). Treat the
   page as needing readability work when **Flesch-Kincaid grade > 12** *or*
   **Flesch Reading Ease < 40** (the same default target the assessment flags on).

   If it's over the threshold, reduce the difficulty without changing meaning or
   dropping detail:
   - Split long, multi-clause sentences into shorter ones (sentence length drives
     every one of these metrics).
   - Prefer a plainer word where one exists (e.g. "use" over "utilize"), but keep
     necessary technical terms — product names and Kubernetes vocabulary will
     legitimately keep the syllable counts high, so don't chase the numbers past
     the point of clarity.
   - Re-run the command to confirm the scores improved, and report the before/after
     values to the user.

   The metrics are heuristic indicators, not hard gates: a page that stays above
   the threshold purely because of unavoidable technical vocabulary is fine.

7. Break overly long shell command lines.

   Shell commands should ideally not have lines longer than 65 characters. If you find a shell command in a fenced code block that has longer lines, try breaking it into multiple lines, adding a backslash before each line break, and indenting subsequent lines.

**IMPORTANT:** When making changes, do not alter the meaning of the content or remove any detail.
