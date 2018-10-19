FROM nginx:1.14.0-alpine

EXPOSE  80
WORKDIR /
ADD vendor/hugo/hugo /usr/bin/hugo
RUN chmod u+x /usr/bin/hugo
WORKDIR /docs/build
ADD ./build /docs/build
RUN hugo --destination /usr/share/nginx/html
