# Inspired by https://github.com/dotcloud/docker/blob/master/docs/Dockerfile

FROM 		ubuntu:14.04
MAINTAINER	Matthias Luebken <matthias@giantswarm.io>



RUN 	apt-get update && apt-get install -yq python-pip gettext
RUN		pip install mkdocs==0.9

WORKDIR	/docs
EXPOSE	8000
ADD 	. /docs

CMD 	["mkdocs", "serve"]
