# Fix broken external links

The purpose of this command is to find broken external links in content and fix them.

1. Fetch the latest release tag for container image `gsoci.azurecr.io/giantswarm/docs`. A release tag has the format `[0-9]+\.[0-9]+\.[0-9]+`. Use this command:

   ```
   az acr repository show-tags \
     --name gsoci \
	 --repository giantswarm/docs \
	 --orderby time_desc \
	 --output tsv | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | head -1
   ```

2. Store that found tag as TAG environment variable.

3. Start `docker run -d --rm --name server -p 8080:8080 -P gsoci.azurecr.io/giantswarm/docs:$TAG`

4. Run the linkchecker against the container using this command to check internal links:

   ```
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
        --ignore-url="^https://.*example.com/.*" \
		--ignore-url=".*gigantic\.io.*" \
		--ignore-url="^https://my-org\.github\.com/.*" \
		--ignore-url="^https://github\.com/giantswarm/giantswarm/.*"
   ```

5. When done, read the report file `linkcheck-report.txt`. 

6. Analyse each link reported. Each link report starts with the term `URL` and ends with a double line break. Skip any
   - internal links
   - non-permanent redirects (HTTP status 302) within the same domain
   - Links to targets that include the domain example.com
   - Server errors (HTTP status 5xx)
   - Timeout errors

6. Fix all permanent redirects (status 301) so that the URL target in the markdown source in this repository points to the actual target URL ("Real URL" in the report).

7. Attempt to fix not found errors (404) by searching the web for an adequate replacement page. If found, modify the link to point to the new target URL. If no adequate page can be found, don't change the link.

8. Report the results to the user in the following order, as Markdown code to be copied into a GitHub pull request description:
   1. List of redirects adapted
   2. List of not found errors adapted
   3. List of not found errors not adapted
   4. List of links skipped
   5. Statistical summary (number of warnings and errors reported, number of links modified, number of links unmodified)

7. Quit the server container: `docker kill server`.
