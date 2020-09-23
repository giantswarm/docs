FROM cimg/base:stable-18.04 as build

USER 0

WORKDIR /docs

COPY vendor/hugo/hugo /usr/bin/hugo

COPY build .

RUN hugo --verbose --gc --minify --cleanDestinationDir --destination /public

FROM nginxinc/nginx-unprivileged:1.18-alpine

EXPOSE 8080

COPY --from=build --chown=101 /public /usr/share/nginx/html
