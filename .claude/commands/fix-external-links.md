# Fix broken external links

Find and fix all broken external links in the docs site.

## Steps

1. Fetch the latest release tag for the docs container image:

   ```bash
   az acr repository show-tags \
     --name gsoci \
     --repository giantswarm/docs \
     --orderby time_desc \
     --output tsv | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | head -1
   ```

2. Store the tag as the `TAG` environment variable.

3. Start the docs server:

   ```bash
   docker run -d --rm --name server -p 8080:8080 -P gsoci.azurecr.io/giantswarm/docs:$TAG
   ```

4. Run linkchecker with external link checking enabled:

   ```bash
   docker run --rm --name linkchecker \
     -v $PWD:/workdir \
     -w /workdir \
     --link server:server \
     ghcr.io/linkchecker/linkchecker:latest \
     http://server:8080 \
     -t 3 \
     --no-status \
     --check-extern \
     --file-output text/linkcheck-report.txt \
     --ignore-url="^https://docs\.giantswarm\.io/.*" \
     --ignore-url="^http://server:8080/changes/.*" \
     --ignore-url="^https://.*example\.com/.*" \
     --ignore-url=".*gigantic\.io.*" \
     --ignore-url="^https://my-org\.github\.com/.*" \
     --ignore-url="^https://github\.com/giantswarm/giantswarm/.*"
   ```

5. Read `linkcheck-report.txt`. Each link report starts with the term `URL` and ends with a double line break.

6. Analyse each reported link. **Skip** any:
   - Internal links
   - Non-permanent redirects (HTTP 302) within the same domain
   - Links to `example.com`
   - Server errors (HTTP 5xx)
   - Timeout errors

7. Fix permanent redirects (HTTP 301) — update the URL in the markdown source to point directly to the real target URL ("Real URL" in the report).

8. For 404 not found errors — search the web for an adequate replacement page. If found, update the link. If not found, leave the link unchanged and note it.

9. Stop the server:

   ```bash
   docker kill server
   ```

10. Report results to the user as Markdown suitable for a GitHub pull request description, in this order:
    1. List of redirects fixed
    2. List of 404 errors fixed
    3. List of 404 errors not fixed (no replacement found)
    4. List of links skipped
    5. Statistical summary (warnings/errors reported, links modified, links unmodified)
