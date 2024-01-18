FROM gsoci.azurecr.io/giantswarm/hugo:v0.121.0-full AS build

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

# Compress files using gzip
# (creates a copy and leaves the uncompressed version in place)
RUN find /public \
  -type f -regextype posix-extended \
  -iregex '.*\.(css|csv|html?|js|svg|txt|xml|json|webmanifest|ttf)' \
  -exec gzip -9 -k '{}' \;

# Remove uncompressed HTML files
# to reduce storage requirements and image size.
RUN find /public \
  -type f \
  -name 'index.html' \
  -delete

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
