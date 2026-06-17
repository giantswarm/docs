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

2. Fix obvious grammar problems. When in doubt, explain the issue to the user and let them decide.

3. Run Vale linting on the target file(s):

   ```bash
   VALE_IMAGE=gsoci.azurecr.io/giantswarm/vale:v3.11.2@sha256:27aab968708850a6cc7369dc1325f1812e2c3de0741327fa0aed832e328357d7

   docker run --rm \
     -v $PWD:/workdir \
     -w /workdir \
     $VALE_IMAGE \
     --config=/workdir/.vale.ini \
     --no-wrap \
     <relative-path-to-markdown-file>
   ```

4. Resolve Vale findings in order of severity: **errors first**, then **warnings**, then **suggestions**.

5. Make sure longer paragraphs provide some anchors for the eye, by emphasizing a few key words or key phrases.

   Example (before)

   > Network traffic, particularly cross-availability zone (cross-AZ) and egress traffic, is often a hidden but significant cost driver in cloud environments. Cloud providers typically charge for data transfer between availability zones. For example, AWS charges approximately $0.01/GB for cross-AZ traffic, and these costs can add up quickly in distributed systems.

   Exmaple (after)

   > Network traffic, particularly cross-availability zone (cross-AZ) and egress traffic, is often a **hidden but significant cost driver** in cloud environments. Cloud providers typically charge for data transfer between availability zones. For example, AWS charges approximately $0.01/GB for cross-AZ traffic, and these costs can **add up quickly** in distributed systems.

6. Break overly long shell command lines.

   Shell commands should ideally not have lines longer than 65 characters. If you find a shell command in a fenced code block that has longer lines, try breaking it into multiple lines, adding a backslash before each line break, and indenting subsequent lines.

**IMPORTANT:** When making changes, do not alter the meaning of the content or remove any detail.
