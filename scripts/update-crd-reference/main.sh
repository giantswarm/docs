#!/bin/bash

set -e

# renovate: datasource=docker depName=gsoci.azurecr.io/giantswarm/crd-docs-generator versioning=semver
CRD_DOCS_GENERATOR_VERSION=0.12.38

DESTINATION=src/content/container-platform/reference/platform-api/crd
PRODUCTS=scripts/update-crd-reference/products.txt

# Clear output folders
find ${DESTINATION} src/content/*/reference/crd -type f -not -name "_index.md" | xargs -I '{}' rm '{}'

# Generate new content
docker run --rm \
    -v ${PWD}/${DESTINATION}:/opt/crd-docs-generator/output \
    -v ${PWD}/scripts/update-crd-reference:/opt/crd-docs-generator/config \
    gsoci.azurecr.io/giantswarm/crd-docs-generator:${CRD_DOCS_GENERATOR_VERSION} \
        --config /opt/crd-docs-generator/config/config.yaml

# Move pages that belong to another product, keeping their Container Platform URL as an alias
while read -r crd product; do
    source=${DESTINATION}/${crd}.md
    if [ ! -f "${source}" ]; then
        echo "Error: ${crd} is listed in ${PRODUCTS} but no page was generated for it" >&2
        exit 1
    fi
    awk -v alias="  - /container-platform/reference/platform-api/crd/${crd}/" \
        '{ print } /^aliases:$/ && !done { print alias; done = 1 }' \
        "${source}" > "src/content/${product}/reference/crd/${crd}.md"
    rm "${source}"
done < <(grep -vE '^(#|$)' ${PRODUCTS})
