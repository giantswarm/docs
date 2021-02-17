#!/bin/bash

set -e

CRD_DOCS_GENERATOR_VERSION=0.4.0-ee74b086d228a80d7c560ffe5a90bf7480c98cd7
DESTINATION=src/content/ui-api/management-api/crd

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs rm

# Determine apiextensions version
VERSION=$(docker run --rm -ti --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner -c "curl --silent https://api.github.com/repos/giantswarm/apiextensions/releases/latest|jq -r .tag_name|tr -d '\n'")

echo "Version: ${VERSION}"

# Generate new content
docker run \
    -v ${PWD}/${DESTINATION}:/opt/crd-docs-generator/output \
    -v ${PWD}/scripts/update-crd-reference:/opt/crd-docs-generator/config \
    quay.io/giantswarm/crd-docs-generator:${CRD_DOCS_GENERATOR_VERSION} \
        --version ${VERSION} \
        --config /opt/crd-docs-generator/config/config.yaml \
        --template /opt/crd-docs-generator/config/crd.template
