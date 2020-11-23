#!/bin/bash

CRD_DOCS_GENERATOR_VERSION=0.1.2

docker run \
    -v ${PWD}/src/content/reference/cp-k8s-api:/opt/crd-docs-generator/output \
    -v ${PWD}/scripts/update-crd-reference:/opt/crd-docs-generator/config \
    quay.io/giantswarm/crd-docs-generator:${CRD_DOCS_GENERATOR_VERSION} \
        --config /opt/crd-docs-generator/config/config.yaml
