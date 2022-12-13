PROJECT=docs
COMPANY=giantswarm
REGISTRY=quay.io
SHELL=bash
MARKDOWNLINT_IMAGE=06kellyjac/markdownlint-cli:0.23.0-alpine
APPLICATION=docs-app

include Makefile.*.mk

default: docker-build

# Export CSV on article metadata
export-csv:
	docker run --rm \
	  --volume=${PWD}:/workdir \
	  -w /workdir \
	  quay.io/giantswarm/docs-scriptrunner:latest \
	  /workdir/scripts/export-csv/script.py

# Update content from external repositories that gets copied in here.
update-external-repos:
	./scripts/update-external-repos/main.sh

# Aggregate changelog entries from various repositories into our Changes section.
changes:
	@if [ -z "${GITHUB_TOKEN}" ]; then echo "Please set the GITHUB_TOKEN environment variable"; exit 1; fi

	docker run --rm \
	  --volume=${PWD}/scripts/aggregate-changelogs:/workdir:ro \
	  --volume=${PWD}/src/content/changes:/output:rw \
	  --volume=${PWD}/src/data:/data:rw \
	  -w /workdir \
	  --env GITHUB_TOKEN \
	  quay.io/giantswarm/docs-scriptrunner:latest \
	  /workdir/script.py /workdir/config.yaml /output /data

changes-test:
	docker run --rm \
	  --volume=${PWD}/scripts/aggregate-changelogs:/workdir:ro \
	  -w /workdir \
	  quay.io/giantswarm/docs-scriptrunner:latest \
	  /workdir/test_script.py foo bar baz

# Generate the reference documentation for the custom resource
# definitions (CRD) used in the Management API.
update-crd-reference:
	scripts/update-crd-reference/main.sh

# Ensure that the CLI version mention in docs is actually the latest
update-latest-versions:
	scripts/update-latest-versions/main.sh

lint:
	@docker pull $(MARKDOWNLINT_IMAGE) > /dev/null
	@docker run \
	  -v ${PWD}:/workdir \
	  -w /workdir \
	  $(MARKDOWNLINT_IMAGE) \
	    --config .markdownlint.yaml \
	    --ignore README.md \
		--ignore ./src/content/changes \
		--ignore ./src/content/use-the-api/management-api/crd \
		./src

# Validate front matter in all pages.
validate-front-matter:
	docker run --rm \
	  --volume=${PWD}:/workdir:ro \
	  -w /workdir \
	  quay.io/giantswarm/docs-scriptrunner:latest \
	  /workdir/scripts/validate-front-matter/script.py

# Print a report of pages with a last_review_date that's
# too long ago.
validate-last-reviewed:
	docker run --rm \
	  --volume=${PWD}:/workdir:ro \
	  -w /workdir \
	  quay.io/giantswarm/docs-scriptrunner:latest \
	  /workdir/scripts/validate-front-matter/script.py --validation last-reviewed

docker-build: update-latest-versions
	docker build -t $(REGISTRY)/$(COMPANY)/$(PROJECT):latest .

docker-run:
	docker run --rm -ti -p 8080:8080 $(REGISTRY)/$(COMPANY)/$(PROJECT):latest

dev:
	docker build -t $(REGISTRY)/$(COMPANY)/$(PROJECT):dev --target=build .
	docker run --rm -ti \
	-p 1313:1313 \
	-v ${PWD}/build:/docs:z \
	$(REGISTRY)/$(COMPANY)/$(PROJECT):dev serve --bind 0.0.0.0 -w -s /docs

clean:
	rm -rf build
	rm -rf vendor
	rm -rf .sass-cache

# Verify internal links
linkcheck-internal:
	@echo "Checking internal links only\n"
	docker run -d --rm --name server -p 8080:8080 -P $(REGISTRY)/$(COMPANY)/$(PROJECT):latest
	sleep 2

	# We ignore https://docs.giantswarm.io/.* because otherwise we could never add new pages,
	# as checks for the "canonical" link would fail.
	docker run --rm -ti --name linkchecker \
		--link server:server \
		linkchecker/linkchecker \
		http://server:8080 \
		-t 5 \
		--no-status \
		--ignore-url="^https://docs\.giantswarm\.io/.*" \
		--ignore-url=/api/
	docker kill server
	docker kill linkchecker

update-website-content:
	cd ./scripts/update-website-content && \
		npm ci && \
		npm start

# Verify internal and external links
# based on the currently deployed docs website.
linkcheck:
	@echo "Checking all links\n"

	docker run --rm -ti --name linkchecker \
		-v ${PWD}/volumes/linkchecker:/workdir:rw \
		-w /workdir \
		ghcr.io/linkchecker/linkchecker \
		https://docs.giantswarm.io \
		-t 1 \
		--file-output csv/linkcheck.csv \
		--check-extern \
		--verbose \
		--ignore-url=/api/ \
		--ignore-url="^https://.+.example.com/.*" \
		--ignore-url=".*gigantic\.io.*" \
		--ignore-url="^https://my-org\.github\.com/.*" \
		--ignore-url="^https://github\.com/giantswarm/giantswarm/.*"
