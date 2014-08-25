PROJECT=docs
registry=registry.giantswarm.io

default: run

build:
	docker build -t $(registry)/$(PROJECT) .

run: build
	docker run --rm -p 8000:8000 $(registry)/$(PROJECT)

push: build 
	docker push $(registry)/$(PROJECT)

deploy: push
	swarm create swarmdocs.json
	swarm start swarmdocs
