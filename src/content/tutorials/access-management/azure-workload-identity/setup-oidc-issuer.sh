#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Resource group that contains the workload cluster.
# By default, it is the same name as the cluster.
export RESOURCE_GROUP="${CLUSTER_NAME}"
export LOCATION="westeurope"
# Randomly generate a storage account name.
# Be sure to manually set the name if you need to re-run the script.
export AZURE_STORAGE_ACCOUNT="oidcissuer$(openssl rand -hex 4)"
# A special container that is always publicly accessible,
# even when the storage account is private.
export AZURE_STORAGE_CONTAINER="\$web"

echo "Deploying Azure Storage Account..."

az storage account create --resource-group $RESOURCE_GROUP --name $AZURE_STORAGE_ACCOUNT
az storage container create --name $AZURE_STORAGE_CONTAINER
az storage blob service-properties update --account-name $AZURE_STORAGE_ACCOUNT --static-website

AZURE_WEB_ENDPOINT=$(az storage account show --query "primaryEndpoints.web" --output tsv --name $AZURE_STORAGE_ACCOUNT)

echo "Generating and publishing the OIDC discovery document..."

cat <<EOF > openid-configuration.json
{
    "issuer": "${AZURE_WEB_ENDPOINT}",
    "jwks_uri": "${AZURE_WEB_ENDPOINT}openid/v1/jwks",
    "response_types_supported": [
        "id_token"
    ],
        "subject_types_supported": [
        "public"
    ],
    "id_token_signing_alg_values_supported": [
        "RS256"
    ]
}
EOF

az storage blob upload \
  --container-name "${AZURE_STORAGE_CONTAINER}" \
  --file openid-configuration.json \
  --name .well-known/openid-configuration

echo "Generating and publishing the OIDC JWKS document..."

azwi jwks --public-keys sa.pub --output-file jwks.json

az storage blob upload \
  --container-name "${AZURE_STORAGE_CONTAINER}" \
  --file jwks.json \
  --name openid/v1/jwks

echo "Done! Your OIDC Issuer is located at:"
echo "${AZURE_WEB_ENDPOINT}"
