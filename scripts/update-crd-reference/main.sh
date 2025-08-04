#!/bin/bash

set -e

# renovate: datasource=docker depName=gsoci.azurecr.io/giantswarm/crd-docs-generator versioning=loose
CRD_DOCS_GENERATOR_VERSION=0.11.4

DESTINATION=src/content/reference/platform-api/crd

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs -I '{}' rm '{}'

# Generate new content
docker run --rm \
    -v ${PWD}/${DESTINATION}:/opt/crd-docs-generator/output \
    -v ${PWD}/scripts/update-crd-reference:/opt/crd-docs-generator/config \
    gsoci.azurecr.io/giantswarm/crd-docs-generator:${CRD_DOCS_GENERATOR_VERSION} \
        --config /opt/crd-docs-generator/config/config.yaml
