PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io


default: ;

build:
	#
	# clean
	rm -rf swarmdocs/public/*
	#
	# copy content from content repo (which needs to be in the neighbor folder)
	rm -rf swarmdocs/content
	rm -rf swarmdocs/static/img
	#rm -rf docs-content
	#git clone --depth 1 git@github.com:giantswarm/docs-content.git
	cp -r docs-content/content swarmdocs/
	cp -r docs-content/img swarmdocs/static/
	#
	# cache date
	echo `date +"%Y%m%d%H%M"` > swarmdocs/layouts/partials/cache_datestamp.html
	#
	# update download links
	curl -s http://downloads.giantswarm.io/swarm/clients/VERSION > swarmdocs/layouts/partials/cli_latest_version.html
	mkdir -p swarmdocs/layouts/shortcodes
	cp swarmdocs/layouts/partials/cli_latest_version.html swarmdocs/layouts/shortcodes/cli_latest_version.html
	#
	# build
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

run:
	docker run --name=$(PROJECT) --rm -ti -p 8000:80 \
		-v $(shell pwd)/swarmdocs/:/docs/swarmdocs/ \
		$(registry)/$(COMPANY)/$(PROJECT)

delete:
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(COMPANY)/$(PROJECT)

pull:
	docker pull $(registry)/$(COMPANY)/$(PROJECT)

highlight.js:
	rm -rf highlight.js
	git clone git@github.com:giantswarm/highlight.js.git

highlight.js-build: highlight.js
	rm -rf highlight.js/build
	cd highlight.js && npm install
	cd highlight.js && node tools/build.js -n bash dockerfile java javascript json php python ruby
	cp highlight.js/build/highlight.pack.js swarmdocs/themes/swarmdocs/static/js/
	cp highlight.js/src/styles/solarized_dark.css swarmdocs/themes/swarmdocs/static/css/

deploy:
	export SWARM_CLUSTER_ID=cluster-01.giantswarm.io
	swarm stop swarmdocs/content-master
	swarm start swarmdocs/content-master
	swarm stop swarmdocs/content-slave
	swarm start swarmdocs/content-slave
	unset SWARM_CLUSTER_ID

linkcheck:
	linklint -http -host localhost:1313 -limit 1000 -doc linklinttest /@
