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


run-with-indexer:
	docker run --name=$(PROJECT) --rm -p 8000:8000 \
		-e SITESEARCH_PORT_9200_TCP_ADDR=$(SITESEARCH_PORT_9200_TCP_ADDR) \
		-e SITESEARCH_PORT_9200_TCP_PORT=$(SITESEARCH_PORT_9200_TCP_PORT) \
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
