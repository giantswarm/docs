PROJECT=docs
COMPANY=giantswarm
REGISTRY=quay.io
SHELL=bash
MARKDOWNLINT_IMAGE=06kellyjac/markdownlint-cli:0.23.0-alpine
CRD_DOCS_GENERATOR_VERSION=0.1.2

default: docker-build


vendor:
	# Vendor other external repositories as defined in 'external-repositories.txt'
	./vendorize-external-repositories.sh

# Aggregate changelog entries from various repositories into our Changes section.
changes:
	@if [ -z "${GITHUB_TOKEN}" ]; then echo "Please set the GITHUB_TOKEN environment variable"; exit 1; fi

	docker build scripts/aggregate-changelogs -t aggregate-changelogs
	docker run --rm \
	  --volume=${PWD}/scripts/aggregate-changelogs:/workdir:ro \
	  --volume=${PWD}/src/content/changes:/output:rw \
	  -w /workdir \
	  --env GITHUB_TOKEN \
	  aggregate-changelogs \
	  /workdir/script.py /workdir/config.yaml /output

build: vendor changes
	# check dependencies
	which jq || (echo "jq not found" && exit 1)
	which curl || (echo "curl not found" && exit 1)

	# Clean
	rm -rf build

	# Create build directory
	mkdir build

	# Copy src to build directory
	cp -r src/. build/

	# Latest gsctl version
	mkdir -p build/layouts/shortcodes
	curl -s https://api.github.com/repos/giantswarm/gsctl/releases/latest | jq -j .tag_name > build/layouts/shortcodes/gsctl_version.html

	# Tie in content from external repositories
	./build-external-repositories.sh

	# Generate the Control Plane K8s API reference documentation.
	docker run \
		-v ${PWD}/build/content/reference/cp-k8s-api:/opt/crd-docs-generator/output \
		-v ${PWD}:/opt/crd-docs-generator/config \
		quay.io/giantswarm/crd-docs-generator:$(CRD_DOCS_GENERATOR_VERSION) \
		  --config /opt/crd-docs-generator/config/crd-docs-generator-config.yaml

lint:
	@docker pull $(MARKDOWNLINT_IMAGE) > /dev/null
	@docker run \
	  -v ${PWD}:/workdir \
	  -w /workdir \
	  $(MARKDOWNLINT_IMAGE) \
	    --config .markdownlint.yaml \
	    --ignore README.md \
		./src

docker-build: build
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
