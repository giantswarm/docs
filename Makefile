PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io
SHELL=bash

default: docker-build

build-css:
	sass swarmdocs/static/css/base.sass swarmdocs/static/css/base.css

docker-build: build-css
	#
	# clean
	rm -rf swarmdocs/public/*
	#
	# copy content from docs-content repo
	rm -rf swarmdocs/content
	rm -rf swarmdocs/static/img
	rm -rf docs-content
	git clone --depth 1 git@github.com:giantswarm/docs-content.git
	cp -r docs-content/content swarmdocs/
	cp -r docs-content/img swarmdocs/static/
	#
	# Cache breaker
	echo -n `date +"%Y%m%d%H%M%S"|md5|head -c 8` > swarmdocs/layouts/partials/cachebreaker.html
	#
	# Latest gsctl version
	curl -s https://downloads.giantswarm.io/gsctl/VERSION > swarmdocs/layouts/partials/gsctl_version.html
	mkdir -p swarmdocs/layouts/shortcodes
	cp swarmdocs/layouts/partials/gsctl_version.html swarmdocs/layouts/shortcodes/gsctl_version.html
	#
	rm -rf build
	# tie in recipes frome external repositories
	./build-recipes.sh
	# build docker image
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

docker-run:
	docker run --rm -ti -p 80:80 \
		-e BASE_URL="http://docker.dev" \
		$(registry)/$(COMPANY)/$(PROJECT)

clean:
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(COMPANY)/$(PROJECT)

linkcheck:
	linklint -http -host docker.dev -limit 1000 -doc linklinttest /@
