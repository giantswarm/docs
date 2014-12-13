# docs - User documentation for Giant Swarm

Simple markdown based documentation based on [MkDocs](http://www.mkdocs.org/). Setup inspired by [Docker docs](https://github.com/dotcloud/docker/tree/master/docs).

## How to document

Currently we have 3 sections:
  * Welcome: for a general introduction
  * Installation: on how to get started
  * Guides: howto types for typical user scenarios
  * Reference: detailed description of options / commands etc.

## Local install

### Running via Docker

Prerequisites:
 * `docker`

1. Build local docker image

    `make build`

2. Run docker container

    `make run`

3. Open [http://192.168.59.103:8000/](http://192.168.59.103:8000/)

### Running in a local Python environment

Prerequisites:
 * `virtualenv`

1. Create the virtual environment

    `virtualenv venv`

2. Activate it

    `source venv/bin/activate`

3. Install requirements

    `pip install -r requirements.txt`

4. Run mkdocs

    `mkdocs serve`

5. Open [http://localhost:8000/](http://localhost:8000/)

Currently there is only one master version. 

There is more information available in the [Wiki](https://git.giantswarm.io/giantswarm/docs/wikis/home).

