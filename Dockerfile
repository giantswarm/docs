FROM nginx-unprivileged:1.16-alpine

EXPOSE  8080

WORKDIR /
ADD vendor/hugo/hugo /usr/bin/hugo
RUN chmod u+x /usr/bin/hugo
WORKDIR /docs/build
ADD ./build /docs/build
RUN /usr/bin/hugo version
RUN /usr/bin/hugo --destination /usr/share/nginx/html
