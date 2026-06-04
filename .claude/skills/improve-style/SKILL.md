---
description: Apply style fixes and run Vale prose linting on modified or added pages
argument-hint: [file-path]
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

**IMPORTANT:** When making changes, do not alter the meaning of the content or remove any detail.
