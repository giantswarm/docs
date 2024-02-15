#!/bin/bash

HELM_CHART_DOCS_GENERATOR_VERSION=0.0.1
DESTINATION=src/content/use-the-api/management-api/cluster-apps

# Clear output folder
find ${DESTINATION} -type f -not -name "_index.md" | xargs -I '{}' rm '{}'

# Generate new content
# docker run --rm \
#     -v ${PWD}/${DESTINATION}:/opt/helm-chart-docs-generator/output \
#     -v ${PWD}/scripts/update-helm-chart-reference:/opt/helm-chart-docs-generator/config \
#     gsoci.azurecr.io/giantswarm/helm-chart-docs-generator:${HELM_CHART_DOCS_GENERATOR_VERSION} \
#         --config /opt/helm-chart-docs-generator/config/config.yaml

docker run --rm -v $PWD/src/content/use-the-api/management-api/cluster-apps:/opt/helm-chart-docs-generator/output -v $PWD/scripts/update-helm-chart-reference:/opt/helm-chart-docs-generator/config giantswarm/helm-chart-docs-generator:0.0.1 --config /opt/helm-chart-docs-generator/config/config.yaml

for file in ${DESTINATION}/*.md; do
  if grep -q '\--&gt;' $file; then
    sed -i.bak 's/\&lt;.*\&gt;//g' $file
    if [ $? -ne 0 ]; then
      echo "An error occurred removing HTML comment lines from $file"
    fi
  fi
done

rm ${DESTINATION}/*.bak
