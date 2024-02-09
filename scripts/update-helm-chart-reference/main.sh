#!/bin/bash

set -e

HELM_CHART_DOCS_GENERATOR_VERSION=0.0.1
DESTINATION=src/content/use-the-api/management-api/cluster-apps

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs -I '{}' rm '{}'

# Generate new content
docker run --rm \
    -v ${PWD}/${DESTINATION}:/opt/helm-chart-docs-generator/output \
    -v ${PWD}/scripts/update-helm-chart-reference:/opt/helm-chart-docs-generator/config \
    gsoci.azurecr.io/giantswarm/helm-chart-docs-generator:${HELM_CHART_DOCS_GENERATOR_VERSION} \
        --config /opt/helm-chart-docs-generator/config/config.yaml
