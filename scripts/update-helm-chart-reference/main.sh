#!/bin/bash

# renovate: datasource=docker depName=gsoci.azurecr.io/giantswarm/helm-chart-docs-generator versioning=loose
HELM_CHART_DOCS_GENERATOR_VERSION=0.2.0

DESTINATION=src/content/reference/platform-api/cluster-apps

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs -I '{}' rm '{}'

# Generate new content
docker run --rm \
    -v ${PWD}/${DESTINATION}:/opt/helm-chart-docs-generator/output \
    -v ${PWD}/scripts/update-helm-chart-reference:/opt/helm-chart-docs-generator/config \
    gsoci.azurecr.io/giantswarm/helm-chart-docs-generator:${HELM_CHART_DOCS_GENERATOR_VERSION} \
        --config /opt/helm-chart-docs-generator/config/config.yaml

for file in ${DESTINATION}/*.md; do
  # Remove empty lines
  awk 'NF > 0 || NR == 1 {blank=0} NF == 0 {blank++} blank < 2 {print}' $file > $file
  # Remove trailing whitespace
  sed -i 's/[ \t]*$//' $file
  # quote storage * expressions (hack to fix https://github.com/giantswarm/docs/actions/runs/8155151741)
  sed -i 's/\/dev\/disk\/by-\*/"&"/g' $file
done
