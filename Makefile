PROJECT=docs
COMPANY=giantswarm
REGISTRY=gsoci.azurecr.io
SHELL=bash
MARKDOWNLINT_IMAGE=ghcr.io/igorshubovych/markdownlint-cli:v0.35.0@sha256:22cf4699a448a7bbc311a940e0600019423d7671cbedae9c35cd32b51f560350
APPLICATION=docs-app
RUNNING_IN_CI ?= false

include Makefile.*.mk

default: docker-build

# Export CSV on article metadata
export-csv:
	docker run --rm \
	  --volume=${PWD}:/workdir \
	  -w /workdir \
	  $(REGISTRY)/$(COMPANY)/docs-scriptrunner:latest \
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
	  $(REGISTRY)/$(COMPANY)/docs-scriptrunner:latest \
	  /workdir/script.py /workdir/config.yaml /output /data

changes-test:
	docker run --rm \
	  --volume=${PWD}/scripts/aggregate-changelogs:/workdir:ro \
	  -w /workdir \
	  $(REGISTRY)/$(COMPANY)/docs-scriptrunner:latest \
	  /workdir/test_script.py foo bar baz

# Generate the reference documentation for the cluster apps.
update-cluster-app-reference:
	scripts/update-helm-chart-reference/main.sh

# Generate the reference documentation for the custom resource
# definitions (CRD) used in the Management API.
update-crd-reference:
	scripts/update-crd-reference/main.sh

lint:
	@docker pull $(MARKDOWNLINT_IMAGE) > /dev/null
	@docker run \
	  -v ${PWD}:/workdir \
	  -w /workdir \
	  $(MARKDOWNLINT_IMAGE) \
	  --config .markdownlint.yaml \
	  --ignore README.md \
	  --ignore ./src/content/changes \
	  --ignore ./src/content/vintage/use-the-api/management-api/crd \
	  $$(if [ "$(RUNNING_IN_CI)" = "true" ]; then echo "--output markdownlint.out"; fi) \
	  ./src

# Validate front matter in all pages.
validate-front-matter:
	docker run --rm \
	  --volume=${PWD}:/workdir:ro \
	  -w /workdir \
	  $(REGISTRY)/$(COMPANY)/docs-scriptrunner:latest \
	  /workdir/scripts/validate-front-matter/script.py

# Print a report of pages with a last_review_date that's
# too long ago.
validate-last-reviewed:
	docker run --rm \
	  --volume=${PWD}:/workdir:ro \
	  -w /workdir \
	  $(REGISTRY)/$(COMPANY)/docs-scriptrunner:latest \
	  /workdir/scripts/validate-front-matter/script.py --validation last-reviewed

docker-build:
	docker build -t $(REGISTRY)/$(COMPANY)/$(PROJECT):latest .

docker-run:
	docker run --rm -ti -p 8080:8080 $(REGISTRY)/$(COMPANY)/$(PROJECT):latest

dev:
	hugo server -s src

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
