FROM nginx:stable-alpine

EXPOSE  80
WORKDIR /
ADD hugo_0.16_linux-64bit/hugo /usr/bin/hugo
RUN chmod u+x /usr/bin/hugo
ADD . /docs
WORKDIR /docs/swarmdocs
RUN hugo --destination /usr/share/nginx/html
