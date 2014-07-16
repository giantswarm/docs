PROJECT=docs
registry=registry.giantswarm.io

default: run

build:
	docker build -t $(registry)/$(PROJECT) .

run: build
	docker run  -i -t -p 8000:8000 $(registry)/$(PROJECT)

release: build
	docker push $(registry)/$(PROJECT)
	swarm create swarmdocs.json
	swarm start swarmdocs
