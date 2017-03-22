PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io
SHELL=bash

default: docker-build

build-css:
	sass src/static/css/base.sass src/static/css/base.css

vendor:


docker-build: build-css
	#
	# clean
	rm -rf build

	# create build directory
	mkdir build

	# copy src to build directory
	cp -r src/ build/
	#
	# copy content from docs-content repo
	cp -r vendor/docs-content/content build/
	cp -r vendor/docs-content/img build/static/
	#
	# Cache breaker
	echo -n `md5 -q ./build/static/css/base.css|head -c 9` > build/layouts/partials/cachebreaker_css.html
	echo -n `md5 -q ./build/static/js/base.js|head -c 9` > build/layouts/partials/cachebreaker_js.html
	#
	# Latest gsctl version
	mkdir -p build/layouts/shortcodes
	curl -s https://downloads.giantswarm.io/gsctl/VERSION > build/layouts/shortcodes/gsctl_version.html

	#
	# tie in recipes frome external repositories
	./build-external-repositories.sh
	# build docker image
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

docker-run:
	docker run --rm -ti -p 80:80 \
		-e BASE_URL="http://docker.dev" \
		$(registry)/$(COMPANY)/$(PROJECT)

clean:
	rm -rf build
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(COMPANY)/$(PROJECT)

linkcheck:
	linklint -http -host docker.dev -limit 1000 -doc linklinttest /@
