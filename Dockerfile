FROM golang:1.3

MAINTAINER Matthias Luebken <matthias@giantswarm.io>
MAINTAINER Marian Steinbach <marian@giantswarm.io>

ENV DEBIAN_FRONTEND noninteractive

COPY requirements.txt /requirements.txt

# install software
RUN set -x \
    && apt-get update -q \
    && apt-get install -y -q --no-install-recommends \
        wget \
        curl \
        ca-certificates \
        python2.7 \
        python-pip \
        python-dev \
    && cd /go/src \
    && wget -q https://github.com/spf13/hugo/archive/v0.12.tar.gz \
    && tar xzf v0.12.tar.gz \
    && cd /go/src/hugo-0.12 \
    && go get \
    && go build main.go \
    && mv main /usr/bin/hugo \
    && pip install -r /requirements.txt \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false \
        python-dev python-pip wget curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ADD . /docs

WORKDIR /docs

ENTRYPOINT ["/docs/run.sh"]

EXPOSE  80
