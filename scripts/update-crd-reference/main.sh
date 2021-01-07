#!/bin/bash

CRD_DOCS_GENERATOR_VERSION=0.2.0

DESTINATION=src/content/reference/management-cluster-api

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs rm

# Generate new content
docker run \
    -v ${PWD}/${DESTINATION}:/opt/crd-docs-generator/output \
    -v ${PWD}/scripts/update-crd-reference:/opt/crd-docs-generator/config \
    quay.io/giantswarm/crd-docs-generator:${CRD_DOCS_GENERATOR_VERSION} \
        --config /opt/crd-docs-generator/config/config.yaml
