FROM golang:1.3

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

# install HUGO
WORKDIR	/go/src
RUN wget -q https://github.com/spf13/hugo/archive/v0.12.tar.gz && tar xzf v0.12.tar.gz
WORKDIR /go/src/hugo-0.12
RUN go get && go build main.go && mv main /usr/bin/hugo

# install everything needed for docs indexing
ADD requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]

ADD . /docs

WORKDIR /docs

ENTRYPOINT ["/docs/run.sh"]

EXPOSE	80
