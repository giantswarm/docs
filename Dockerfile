FROM quay.io/giantswarm/hugo:v0.75.1 AS build

WORKDIR /docs

COPY build .

RUN hugo --verbose --gc --minify --cleanDestinationDir --destination /public

FROM quay.io/giantswarm/nginx:1.18-alpine

EXPOSE 8080

COPY --from=build --chown=101 /public /usr/share/nginx/html
