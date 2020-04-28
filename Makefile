PROJECT=docs
COMPANY=giantswarm
REGISTRY=quay.io
SHELL=bash

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
		wget -q https://github.com/gohugoio/hugo/releases/download/v0.49.2/hugo_0.49.2_Linux-64bit.tar.gz && \
		tar -xvf hugo_0.49.2_Linux-64bit.tar.gz && \
		rm hugo_0.49.2_Linux-64bit.tar.gz

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
		quay.io/giantswarm/crd-docs-generator:latest --apiextensions-commit-ref v0.3.3

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

# Verify links.
linkcheck:
	docker run -d --rm --name server -p 8080:8080 -P $(REGISTRY)/$(COMPANY)/$(PROJECT):latest
	sleep 2

	# We ignore https://docs.giantswarm.io/.* because otherwise we could never add new pages,
	# as checks for the "canonical" link would fail.
	docker run --rm -ti --name linkchecker \
		--link server:server \
		linkchecker/linkchecker \
		http://server:8080 \
		--check-extern -t 5 --ignore-url="^https://docs.giantswarm.io/.*" --ignore-url=/api/ --ignore-url="^https://.+.example.com/.*"
	docker ps --filter name=server && docker kill server
	docker ps --filter name=linkchecker && docker kill linkchecker
