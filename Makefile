PROJECT=docs
COMPANY=giantswarm
registry=registry.giantswarm.io

default: ;

build:
	docker build -t $(registry)/$(COMPANY)/$(PROJECT) .

run:
	docker run --name=$(PROJECT) --rm -p 8000:8000 \
		-e SITESEARCH_PORT_9200_TCP_ADDR=$(SITESEARCH_PORT_9200_TCP_ADDR) \
		-e SITESEARCH_PORT_9200_TCP_PORT=$(SITESEARCH_PORT_9200_TCP_PORT) \
		$(registry)/$(COMPANY)/$(PROJECT)

delete:
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(COMPANY)/$(PROJECT)

deploy:
	swarm --api-endpoint="https://cluster-01.giantswarm.io/v1/" stop swarmdocs
	swarm --api-endpoint="https://cluster-01.giantswarm.io/v1/" delete swarmdocs
	swarm --api-endpoint="https://cluster-01.giantswarm.io/v1/" create swarmdocs.json
	swarm --api-endpoint="https://cluster-01.giantswarm.io/v1/" create swarm.json
	swarm --api-endpoint="https://cluster-01.giantswarm.io/v1/" swarm start swarmdocs
