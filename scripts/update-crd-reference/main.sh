#!/bin/bash

set -e

# TODO: set release version
CRD_DOCS_GENERATOR_VERSION=0.6.1-d98f2e890b9274ca2ed3a3dddbacfe7344942667
DESTINATION=src/content/ui-api/management-api/crd

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs rm

# Determine apiextensions version
#VERSION=$(docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner -c "curl --silent https://api.github.com/repos/giantswarm/apiextensions/releases/latest|jq -r .tag_name|tr -d '\n'")

# TODO: revert this
VERSION=add-docs-metadata

echo "Version: ${VERSION}"

# Generate new content
docker run --rm \
    -v ${PWD}/${DESTINATION}:/opt/crd-docs-generator/output \
    -v ${PWD}/scripts/update-crd-reference:/opt/crd-docs-generator/config \
    quay.io/giantswarm/crd-docs-generator:${CRD_DOCS_GENERATOR_VERSION} \
        --commit-reference ${VERSION} \
        --config /opt/crd-docs-generator/config/config.yaml
