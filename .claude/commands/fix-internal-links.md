# Fix broken internal links

Find and fix all broken internal links in the docs site.

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

4. Run linkchecker to find broken internal links:

   ```bash
   docker run --rm --name linkchecker \
     -v $PWD:/workdir \
     -w /workdir \
     --link server:server \
     ghcr.io/linkchecker/linkchecker:latest \
     http://server:8080 \
     -t 4 \
     --no-status \
     --file-output text/linkcheck-report.txt \
     --ignore-url="^https://docs\.giantswarm\.io/.*" \
     --ignore-url="^http://server:8080/changes/.*"
   ```

5. Read `linkcheck-report.txt`. Each link report starts with the term `URL` and ends with a double line break.

6. Fix each broken link:
   - Update permanent redirects (301) to point directly to the real target URL
   - Investigate and fix 404 not found errors

7. Stop the server:

   ```bash
   docker kill server
   ```

8. Report results to the user.

**IMPORTANT:** Always use the `relref` shortcode for internal links. When modifying an internal link that was not using `relref`, convert it to `relref` syntax.
