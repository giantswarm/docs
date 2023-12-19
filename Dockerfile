FROM gsoci.azurecr.io/giantswarm/hugo:v0.121.0-full AS build

RUN apk --update --no-cache add findutils gzip

WORKDIR /docs

COPY . /docs

# Expose the release version in content
ENV HUGO_DOCS_VERSION $CIRCLE_TAG

RUN hugo \
      --verbose \
      --gc \
      --minify \
      --source src \
      --printPathWarnings \
      --printUnusedTemplates \
      --destination /public \
      --cleanDestinationDir

# Compress static files above 512 bytes using gzip
RUN find /public \
  -type f -regextype posix-extended \
  -size +512c \
  -iregex '.*\.(css|csv|html?|js|svg|txt|xml|json|webmanifest|ttf)' \
  -exec gzip -9 -k '{}' \;

FROM gsoci.azurecr.io/giantswarm/nginx:1.23-alpine

COPY nginx.conf /etc/nginx/nginx.conf

RUN rm /docker-entrypoint.d/* && \
  sed -i \
    -e 's|listen       80;|listen 8080;|' \
    -e 's|listen  [::]:80;||' \
    /etc/nginx/conf.d/default.conf

RUN nginx -t -c /etc/nginx/nginx.conf && \
    rm -rf /tmp/nginx.pid

EXPOSE 8080

COPY --from=build --chown=101 /public /usr/share/nginx/html
