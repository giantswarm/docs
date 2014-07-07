default: build run
build:
	docker build -t docs .
run:
	docker run  -i -t -p 8000:8000 docs
