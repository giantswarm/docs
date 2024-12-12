FROM gsoci.azurecr.io/giantswarm/hugo:v0.139.3-full AS build

WORKDIR /docs

COPY . /docs

# Expose the release version in content
ENV HUGO_DOCS_VERSION="$CIRCLE_TAG"

RUN hugo \
      --logLevel info \
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
  -iregex '.*\.(css|csv|html?|js|svg|txt|xml|json|webmanifest|ttf)'  | \
    xargs gzip -9 -k

# Remove uncompressed HTML files
# to reduce storage requirements and image size.
RUN find /public \
  -type f \
  -name 'index.html' \
  -delete

FROM gsoci.azurecr.io/giantswarm/nginx:1.25-alpine
EXPOSE 8080
USER 0

# Delete default config (which we have no control over)
RUN rm -r /etc/nginx/conf.d && rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Ensure tmp dir exists and has right ownership
RUN mkdir -p /tmp/nginx && chown -R 101 /tmp/nginx

RUN nginx -t -c /etc/nginx/nginx.conf && \
    rm -rf /tmp/nginx/nginx.pid

COPY --from=build --chown=101 /public /usr/share/nginx/html

USER 101
