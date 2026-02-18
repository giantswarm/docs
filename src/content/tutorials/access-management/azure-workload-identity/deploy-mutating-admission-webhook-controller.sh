#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

export MANAGEMENT_CLUSTER_CONTEXT="mc-context"
export ORGANIZATION_NAME="your-org"
export CLUSTER_NAME="your-workload-cluster"
export AZURE_TENANT_ID=$(az account show --query tenantId -o tsv)

cat <<EOF | kubectl --context ${MANAGEMENT_CLUSTER_CONTEXT} apply -f -
---
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: OCIRepository
metadata:
  name: azure-workload-identity-webhook
  namespace: org-${ORGANIZATION_NAME}
spec:
  url: oci://gsoci.azurecr.io/charts/giantswarm/azure-workload-identity-webhook
  ref:
    tag: 1.0.3
  interval: 60m
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: ${CLUSTER_NAME}-azure-workload-identity-webhook
  namespace: org-${ORGANIZATION_NAME}
spec:
  chartRef:
    apiVersion: source.toolkit.fluxcd.io/v1beta2
    kind: OCIRepository
    name: azure-workload-identity-webhook
    namespace: org-${ORGANIZATION_NAME}
  interval: 60m
  kubeConfig:
    secretRef:
      name: ${CLUSTER_NAME}-kubeconfig
  releaseName: azure-workload-identity-webhook
  storageNamespace: giantswarm
  targetNamespace: giantswarm
  values:
    azureTenantID: ${AZURE_TENANT_ID}
EOF
