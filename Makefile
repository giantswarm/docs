PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io
SHELL=bash

default: docker-build

build-css:
	sass swarmdocs/static/css/base.scss swarmdocs/static/css/base.css

docker-build:
	#
	# clean
	rm -rf swarmdocs/public/*
	#
	# copy content from content repo (which needs to be in the neighbor folder)
	rm -rf swarmdocs/content
	rm -rf swarmdocs/static/img
	rm -rf docs-content
	git clone --depth 1 git@github.com:giantswarm/docs-content.git
	cp -r docs-content/content swarmdocs/
	cp -r docs-content/img swarmdocs/static/
	#
	# cache date
	echo -n `date +"%Y%m%d%H%M"` > swarmdocs/layouts/partials/cache_datestamp.html
	#
	# update download links
	curl -s https://downloads.giantswarm.io/swarm/clients/VERSION > swarmdocs/layouts/partials/cli_latest_version.html
	mkdir -p swarmdocs/layouts/shortcodes
	cp swarmdocs/layouts/partials/cli_latest_version.html swarmdocs/layouts/shortcodes/cli_latest_version.html
	#
	# build
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

docker-run:
	docker run --name=$(PROJECT) --rm -ti -p 80:80 \
		-v $(shell pwd)/swarmdocs/:/docs/swarmdocs/ \
		-e BASE_URL="http://docker.dev" \
		$(registry)/$(COMPANY)/$(PROJECT)

swarm-update:
	SWARM_CLUSTER_ID=leaseweb-alpha-private.giantswarm.io swarm --env="giantswarm/production" update docs/content-master
	sleep 120
	SWARM_CLUSTER_ID=leaseweb-alpha-private.giantswarm.io swarm --env="giantswarm/production" update docs/content-slave

clean:
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(COMPANY)/$(PROJECT)

linkcheck:
	linklint -http -host docker.dev -limit 1000 -doc linklinttest /@
