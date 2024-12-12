#!/bin/bash

# renovate: datasource=docker depName=gsoci.azurecr.io/giantswarm/helm-chart-docs-generator versioning=loose
HELM_CHART_DOCS_GENERATOR_VERSION=0.2.0

DESTINATION=src/content/vintage/use-the-api/management-api/cluster-apps

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs -I '{}' rm '{}'

# Generate new content
docker run --rm \
    -v ${PWD}/${DESTINATION}:/opt/helm-chart-docs-generator/output \
    -v ${PWD}/scripts/update-helm-chart-reference:/opt/helm-chart-docs-generator/config \
    gsoci.azurecr.io/giantswarm/helm-chart-docs-generator:${HELM_CHART_DOCS_GENERATOR_VERSION} \
        --config /opt/helm-chart-docs-generator/config/config.yaml

for file in ${DESTINATION}/*.md; do
  ## Remove all content before the docs line
  sed -i '/<!-- INTRO_END -->/,/<!-- DOCS_START -->/d' $file
  # Remove empty lines
  awk 'NF > 0 || NR == 1 {blank=0} NF == 0 {blank++} blank < 2 {print}'  $file > /tmp/_back.md && mv /tmp/_back.md $file
  # Remove trailing whitespace
  sed -i 's/[ \t]*$//' $file
  # quote storage * expressions (hack to fix https://github.com/giantswarm/docs/actions/runs/8155151741)
  sed -i 's/\/dev\/disk\/by-\*/"&"/g' $file
done
