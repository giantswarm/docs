PROJECT=docs
COMPANY=giantswarm
REGISTRY=quay.io
SHELL=bash

default: docker-build

build-css:
	sass src/static/css/base.sass src/static/css/base.css

vendor:
	# Vendor hugo
	mkdir -p vendor
	mkdir -p vendor/hugo
	cd vendor/hugo && \
		wget -q https://github.com/spf13/hugo/releases/download/v0.16/hugo_0.16_linux-64bit.tgz && \
		tar -xvf hugo_0.16_linux-64bit.tgz && \
		rm hugo_0.16_linux-64bit.tgz

	# Vendor other external repositories as defined in docs-content repo 'external-repositories.txt'
	./vendorize-external-repositories.sh

build: vendor build-css
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
	curl -s https://downloads.giantswarm.io/gsctl/VERSION > build/layouts/shortcodes/gsctl_version.html

	# Tie in content from external repositories
	./build-external-repositories.sh

docker-build: build
	docker build -t $(REGISTRY)/$(COMPANY)/$(PROJECT):latest .

docker-run:
	docker run --rm -ti -p 8080:80 $(REGISTRY)/$(COMPANY)/$(PROJECT):latest

clean:
	rm -rf build
	rm -rf vendor
	rm -rf .sass-cache

# Verify links.
linkcheck:
	docker run -d --rm --name server -P $(REGISTRY)/$(COMPANY)/$(PROJECT):latest
	sleep 2
	docker run --rm -ti --name linkchecker \
		--link server:server \
		jare/linkchecker \
		http://server:80 \
		--check-extern -t 5 --ignore-url /api/
	docker kill server
