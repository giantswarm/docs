PROJECT=docs
registry=registry.giantswarm.io

default: ;

build:
	docker build -t $(registry)/$(PROJECT) .

run:
	docker run --name=$(PROJECT) --rm -p 8000:8000 \
		-e SITESEARCH_PORT_9200_TCP_ADDR=$(SITESEARCH_PORT_9200_TCP_ADDR) \
		-e SITESEARCH_PORT_9200_TCP_PORT=$(SITESEARCH_PORT_9200_TCP_PORT) \
		$(registry)/$(PROJECT)

delete:
	docker stop $(PROJECT)
	docker rm $(PROJECT)
	docker rmi $(registry)/$(PROJECT)

deploy: 
	swarm stop swarmdocs
	swarm delete swarmdocs
	swarm create swarmdocs.json
	swarm start swarmdocs
