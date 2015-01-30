PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io

default: ;

build:
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

run:
	docker run --name=$(PROJECT) --rm -ti -p 8000:8000 \
		-v $(shell pwd)/swarmdocs/:/docs/swarmdocs/ \
		$(registry)/$(COMPANY)/$(PROJECT)

run-nginx:
	docker run -d --name="docs-auth" -p 8080:80 \
		--link docs:mkdocsmaster \
		--link docs-sitesearch:sitesearch \
		-e MKDOCSSLAVE_PORT_8000_TCP_ADDR=0.0.0.0 \
		-e MKDOCSSLAVE_PORT_8000_TCP_PORT=8000 \
		registry.giantswarm.io/giantswarm/docs-auth

run-sitesearch:
	docker run -d --name="docs-sitesearch" -p 9200:9200 \
		$(registry)/$(COMPANY)/sitesearch

run-with-indexer:
	docker run --name=$(PROJECT) --rm -p 8000:8000 \
		--link docs-sitesearch:sitesearch \
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
	export SWARM_CLUSTER_ID=cluster-01.giantswarm.io && swarm stop swarmdocs
	swarm delete swarmdocs
	swarm create swarmdocs.json
	swarm create swarm.json
	swarm swarm start swarmdocs
	unset SWARM_CLUSTER_ID
