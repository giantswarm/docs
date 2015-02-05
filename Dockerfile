FROM debian:wheezy

MAINTAINER Matthias Luebken <matthias@giantswarm.io>
MAINTAINER Marian Steinbach <marian@giantswarm.io>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR	/

# install basics
RUN apt-get update -qq && \
	apt-get install -y -q --no-install-recommends \
  wget \
  curl \
  build-essential \
  ca-certificates \
  git-core \
  mercurial \
  bzr \
  python2.7 \
  python-pip \
  python-dev

# install Go 1.3
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.3.1.linux-amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1
RUN mkdir /gopath && mkdir /gopath/src
ENV GOROOT /goroot
ENV GOPATH /gopath
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

# install HUGO
WORKDIR	/gopath/src
RUN wget -q https://github.com/spf13/hugo/archive/v0.12.tar.gz && tar xzf v0.12.tar.gz
WORKDIR /gopath/src/hugo-0.12
RUN go get && go build main.go && mv main /usr/bin/hugo
WORKDIR	/
RUN rm -rf /gopath/src/hugo-0.12

# install everything needed for docs indexing
ADD requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]

ADD . /docs

WORKDIR /docs

ENTRYPOINT ["/docs/run.sh"]

EXPOSE	80
