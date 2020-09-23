PROJECT=docs
COMPANY=giantswarm
REGISTRY=quay.io
SHELL=bash
MARKDOWNLINT_IMAGE=06kellyjac/markdownlint-cli:0.21.0
CRD_DOCS_GENERATOR_VERSION=0.1.1

default: docker-build

build-css:
	docker run -it \
		-v ${PWD}/src/static/css:/sass \
		ellerbrock/alpine-sass /sass/base.sass /sass/base.css -m auto


vendor:
	# Vendor hugo
	mkdir -p vendor
	mkdir -p vendor/hugo
	cd vendor/hugo && \
		wget -O hugo.tar.gz -q https://github.com/gohugoio/hugo/releases/download/v0.75.1/hugo_extended_0.75.1_Linux-64bit.tar.gz && \
		tar -xvf hugo.tar.gz && \
		rm hugo.tar.gz

	# Vendor other external repositories as defined in 'external-repositories.txt'
	./vendorize-external-repositories.sh


build: vendor build-css
	# check dependencies
	which jq || (echo "jq not found" && exit 1)
	which curl || (echo "curl not found" && exit 1)

	# Clean
	rm -rf build

	# Create build directory
	mkdir build

	# Copy src to build directory
	cp -r src/. build/

	# Cache breaker
	echo -n `git hash-object ./build/static/css/base.css|head -c 9` > build/layouts/partials/cachebreaker_css.html
	echo -n `git hash-object ./build/static/js/base.js|head -c 9` > build/layouts/partials/cachebreaker_js.html

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
	docker run --rm -ti \
	-p 8080:8080 \
	-v ${PWD}/src:/docs/build:z \
	$(REGISTRY)/$(COMPANY)/$(PROJECT):latest /bin/sh -c "nginx; hugo -w --destination /usr/share/nginx/html"

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
