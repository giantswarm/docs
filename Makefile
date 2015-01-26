PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io

default: ;

build:
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

run:
	docker run --name=$(PROJECT) --rm -p 8000:8000 \
		-v $(shell pwd)/sources/:/docs/sources/ \
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
		registry.giantswarm.io/giantswarm/sitesearch

run-with-indexer:
	docker run --name=$(PROJECT) --rm -p 8000:8000 \
		--link docs-sitesearch:sitesearch \
		-v $(shell pwd)/sources/:/docs/sources/ \
		$(registry)/$(COMPANY)/$(PROJECT)


delete:
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(COMPANY)/$(PROJECT)

pull:
	docker pull $(registry)/$(COMPANY)/$(PROJECT)

deploy:
	export SWARM_CLUSTER_ID=cluster-01.giantswarm.io && swarm stop swarmdocs
	swarm delete swarmdocs
	swarm create swarmdocs.json
	swarm create swarm.json
	swarm swarm start swarmdocs
	unset SWARM_CLUSTER_ID
