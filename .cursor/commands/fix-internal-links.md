# Fix broken links

The purpose of this command is to find broken links in content and fix them.

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
		-t 4 \
		--no-status \
		--file-output text/linkcheck-report.txt \
		--ignore-url="^https://docs\.giantswarm\.io/.*" \
		--ignore-url="^http://server:8080/changes/.*"
   ```

5. When done, read the rport file `linkcheck-report.txt`. Each report starts with the term `URL` and ends with a double line break.

6. Fix each broken link. Also update links that are permanent redirects (status 301) to point to actual target.

7. Quit the server container: `docker kill server`.

8. Report the results to the user.

IMPORTANT: Always use the `relref` shortcode for internal links. When modifying an internal link that was not using relref, change it to relref syntax.
