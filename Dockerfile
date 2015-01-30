FROM debian:wheezy

MAINTAINER	Matthias Luebken <matthias@giantswarm.io>, Marian Steinbach <marian@giantswarm.io>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR	/

# configure apt
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.7.9-1~wheezy

# install basics
RUN apt-get update -qq && \
	apt-get install -y -q --no-install-recommends wget curl build-essential ca-certificates git-core mercurial bzr nginx=${NGINX_VERSION}

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

# clean up stuff we only need for building, not for running
RUN apt-get remove -qy wget curl build-essential ca-certificates git-core mercurial && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# make nginx log to STDOUT/STDERR
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# TODO: install everything needed for docs indexing

ADD . /docs

WORKDIR /docs/swarmdocs

CMD ["hugo", "server", "-p", "8000"]

EXPOSE	8000
