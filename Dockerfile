# Inspired by https://github.com/dotcloud/docker/blob/master/docs/Dockerfile

FROM 		ubuntu:14.04
MAINTAINER	Matthias Luebken <matthias@giantswarm.io>

RUN 	apt-get update && apt-get install -yq python-pip gettext
RUN		pip install mkdocs

ADD 	. /docs
WORKDIR	/docs

EXPOSE	8000
CMD 	["mkdocs", "serve"]
