PROJECT=docs
COMPANY=giantswarm
REGISTRY=quay.io
SHELL=bash
MARKDOWNLINT_IMAGE=06kellyjac/markdownlint-cli:0.23.0-alpine

default: docker-build

# Update content from external repositories that gets copied in here.
update-external-repos:
	./scripts/update-external-repos/main.sh

# Aggregate changelog entries from various repositories into our Changes section.
changes:
	@if [ -z "${GITHUB_TOKEN}" ]; then echo "Please set the GITHUB_TOKEN environment variable"; exit 1; fi

	docker build scripts/aggregate-changelogs -t aggregate-changelogs
	docker run --rm \
	  --volume=${PWD}/scripts/aggregate-changelogs:/workdir:ro \
	  --volume=${PWD}/src/content/changes:/output:rw \
	  --volume=${PWD}/src/data:/data:rw \
	  -w /workdir \
	  --env GITHUB_TOKEN \
	  aggregate-changelogs \
	  /workdir/script.py /workdir/config.yaml /output /data

changes-test:
	docker run --rm \
	  --volume=${PWD}/scripts/aggregate-changelogs:/workdir:ro \
	  -w /workdir \
	  aggregate-changelogs \
	  /workdir/test_script.py foo bar baz

# Generate the reference documentation for the custom resource
# definitions (CRD) used in the management cluster API.
update-crd-reference:
	scripts/update-crd-reference/main.sh

# Ensure that the CLI version mention in docs is actually the latest
update-latest-versions:
	which jq || (echo "jq not found" && exit 1)
	which curl || (echo "curl not found" && exit 1)
	curl -s https://api.github.com/repos/giantswarm/gsctl/releases/latest | jq -j .tag_name > src/layouts/shortcodes/gsctl_version.html

lint:
	@docker pull $(MARKDOWNLINT_IMAGE) > /dev/null
	@docker run \
	  -v ${PWD}:/workdir \
	  -w /workdir \
	  $(MARKDOWNLINT_IMAGE) \
	    --config .markdownlint.yaml \
	    --ignore README.md \
		--ignore ./src/content/changes \
		--ignore ./src/content/reference/cp-k8s-api \
		./src

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
linkcheck-external:
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

grab-main-site-header-footer:
	curl -s https://www.giantswarm.io/why-giant-swarm | sed -n '/^<!-- BEGIN SITE_HEADER -->/,/^<!-- END SITE_HEADER -->/p;/^<!-- END SITE_HEADER -->/q' | sed '1d;$d' > src/layouts/partials/gs_header.html
	curl -s https://www.giantswarm.io/why-giant-swarm | sed -n '/^<!-- BEGIN SITE_FOOTER -->/,/^<!-- END SITE_FOOTER -->/p;/^<!-- END SITE_FOOTER -->/q' | sed '1d;$d' > src/layouts/partials/gs_footer.html

# Verify internal and external links
linkcheck:
	@echo "Checking all links\n"
	docker run -d --rm --name server -p 8080:8080 -P $(REGISTRY)/$(COMPANY)/$(PROJECT):latest
	sleep 2

	docker run --rm -ti --name linkchecker \
		--link server:server \
		linkchecker/linkchecker \
		http://server:8080 \
		-t 2 \
		--check-extern \
		--no-status \
		--ignore-url="^https://docs.giantswarm.io/.*" \
		--ignore-url=/api/ \
		--ignore-url="^https://.+.example.com/.*" \
		--ignore-url=".*gigantic\.io.*" \
		--ignore-url="^https://my-org\.github\.com/.*" \
		--ignore-url="^https://github\.com/giantswarm/giantswarm/.*"

	docker kill server
	docker kill linkchecker
