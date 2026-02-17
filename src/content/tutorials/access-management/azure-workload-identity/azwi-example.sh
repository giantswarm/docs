#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# The name of your workload cluster.
export CLUSTER_NAME="your-workload-cluster"
# Azure location of your workload cluster resources.
export LOCATION="westeurope"
# HTTPS URL to the OIDC issuer that was created in the previous section.
export SERVICE_ACCOUNT_ISSUER=""
# The name of the resource group that contains the workload cluster.
export RESOURCE_GROUP="${CLUSTER_NAME}"

export KEYVAULT_NAME="azwi-kv-${CLUSTER_NAME}"
export KEYVAULT_SECRET_NAME="my-secret"

export USER_ASSIGNED_IDENTITY_NAME="${CLUSTER_NAME}-msal"
export SERVICE_ACCOUNT_NAMESPACE="default"
export SERVICE_ACCOUNT_NAME="workload-identity-msal"

echo "Creating the Azure Key Vault and Secret..."

VAULT_ID=$(az keyvault create --resource-group "$RESOURCE_GROUP" \
   --location "$LOCATION" \
   --name "$KEYVAULT_NAME" \
   --query id -o tsv )

# Assign the logged-in user permissions to manage secrets in the Key Vault.
ASSIGNEE_OBJECT_ID=$(az ad signed-in-user show --query id -o tsv)
az role assignment create \
  --assignee-object-id $ASSIGNEE_OBJECT_ID \
  --assignee-principal-type User \
  --role "Key Vault Secrets Officer" \
  --scope $VAULT_ID

echo "Waiting for Azure Key Vault RBAC permissions to apply..."
sleep 60

az keyvault secret set --vault-name "$KEYVAULT_NAME" \
   --name "$KEYVAULT_SECRET_NAME" \
   --value "Hello\!"

echo "Creating user-assigned managed identity..."
USER_ASSIGNED_IDENTITY_CLIENT_ID=$(az identity create \
    --name "$USER_ASSIGNED_IDENTITY_NAME" \
    --resource-group "$RESOURCE_GROUP" \
    --query clientId -o tsv)

USER_ASSIGNED_IDENTITY_OBJECT_ID=$(az identity show \
    --name $USER_ASSIGNED_IDENTITY_NAME \
    --resource-group $RESOURCE_GROUP \
    --query principalId -o tsv)

az role assignment create \
  --assignee-object-id $USER_ASSIGNED_IDENTITY_OBJECT_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Key Vault Secrets User" \
  --scope $VAULT_ID

echo "Creating federated credential..."
az identity federated-credential create \
  --name "workload-identity-fc" \
  --identity-name $USER_ASSIGNED_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --issuer $SERVICE_ACCOUNT_ISSUER \
  --subject system:serviceaccount:${SERVICE_ACCOUNT_NAMESPACE}:${SERVICE_ACCOUNT_NAME}

echo "Creating example workload..."

KEYVAULT_URL=$(az keyvault show \
    --resource-group $RESOURCE_GROUP \
    --name $KEYVAULT_NAME \
    --query properties.vaultUri -o tsv)

cat <<EOF | kubectl apply -f -
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ${SERVICE_ACCOUNT_NAME}
  namespace: ${SERVICE_ACCOUNT_NAMESPACE}
  annotations:
    azure.workload.identity/client-id: ${USER_ASSIGNED_IDENTITY_CLIENT_ID}
---
apiVersion: v1
kind: Pod
metadata:
  name: quick-start
  namespace: ${SERVICE_ACCOUNT_NAMESPACE}
  labels:
    azure.workload.identity/use: "true"
spec:
  serviceAccountName: ${SERVICE_ACCOUNT_NAME}
  containers:
    - image: ghcr.io/azure/azure-workload-identity/msal-go
      name: oidc
      env:
        - name: KEYVAULT_URL
          value: ${KEYVAULT_URL}
        - name: SECRET_NAME
          value: ${KEYVAULT_SECRET_NAME}
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  nodeSelector:
    kubernetes.io/os: linux
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
EOF
