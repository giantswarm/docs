FROM debian:jessie

MAINTAINER Matthias Luebken <matthias@giantswarm.io>
MAINTAINER Marian Steinbach <marian@giantswarm.io>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR	/

# install basics
RUN apt-get update -qq && \
	apt-get install -y -q --no-install-recommends \
  wget \
  curl \
  ca-certificates \
  python2.7 \
  python-pip \
  python-dev


# install everything needed for docs indexing
COPY requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]


# install HUGO
RUN set -x \
	&& wget https://github.com/spf13/hugo/releases/download/v0.13/hugo_0.13_linux_amd64.tar.gz \
	&& tar xzf hugo_0.13_linux_amd64.tar.gz \
	&& mv hugo_0.13_linux_amd64/hugo_0.13_linux_amd64 /usr/bin/hugo \
	&& rm -r hugo_0.13_linux_amd64


ADD . /docs

WORKDIR /docs

ENTRYPOINT ["/docs/run.sh"]

EXPOSE	80
