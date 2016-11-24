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
	git clone --depth 1 -b more-structure git@github.com:giantswarm/docs-content.git
	cp -r docs-content/content swarmdocs/
	cp -r docs-content/img swarmdocs/static/
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
