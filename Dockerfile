# Inspired by https://github.com/dotcloud/docker/blob/master/docs/Dockerfile

FROM 		debian:jessie
MAINTAINER	Matthias Luebken <matthias@giantswarm.io>

RUN 	apt-get update && apt-get install -yq make python-pip python-setuptools vim-tiny git gettext
RUN		pip install mkdocs

ADD 	. /docs
WORKDIR	/docs

EXPOSE	8000
CMD 	["mkdocs", "serve"]