---
linkTitle: Azure Workload Identity
title: Azure Workload Identity
description: This article describes how to configure a Giant Swarm cluster to support Azure Workload Identity.
weight: 70
menu:
  principal:
    parent: tutorials-access-management
    identifier: tutorials-access-management-azwi
user_questions:
  - How can I use Azure Workload Identity?
last_review_date: 2026-02-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

This tutorial is adapted from [Azure's documentation](https://azure.github.io/azure-workload-identity/docs/introduction.html).

Azure Workload Identity is a mechanism for configuring a Kubernetes cluster to use Azure Entra ID as a federated credential provider through the OpenID Connect (OIDC) protocol.
It is the successor of Azure AD Pod Identity offering broader support, better scaling, and simpler usage.

Configuring a workload cluster to enable Azure Workload Identity is not yet automated in the Giant Swarm platform.
However, customers that require it can configure their clusters manually.
These manual actions only need to be taken once for the lifecycle of each workload cluster, and do not require maintenance.

## How it works

The Kubernetes cluster issues tokens to Service Accounts.
These service account tokens are configured to be trusted on user-assigned managed identities.
Cluster workloads exchange a service account token projected to its volume for an Entra ID access token using the Azure Identity SDKs or the Microsoft Authentication Library (MSAL).

![Diagram showing the OIDC flow as it applies to Azure Workload Identity](how-it-works-diagram.png "How it works")

## Enabling Azure Workload Identity

### Prerequisites

* Azure workload cluster
* [Kubernetes CLI (`kubectl`)](https://kubernetes.io/docs/tasks/tools/#kubectl)
* [Azure CLI (`az`)](https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest)
* [Azure AD Workload CLI (`azwi`)](https://azure.github.io/azure-workload-identity/docs/installation/azwi.html)

Make sure that your Azure CLI is logged in and configured to use the subscription that your workload cluster is running in.

### Retrieve service account public key

The Kubernetes API server issues tokens for service accounts.
The public part of the API server's key pair must be published in the OIDC JSON Web Key Sets (JWKS) document.
This public key must be retrieved so that we can generate the JWKS document in the next step.

Make sure that your `kubectl` context is set to your management cluster.
Then run the following command:

```bash
export MANAGEMENT_CLUSTER_CONTEXT="mc-context"
export ORGANIZATION_NAME="your-org"
export CLUSTER_NAME="your-workload-cluster"

kubectl --context ${MANAGEMENT_CLUSTER_CONTEXT} \
    --namespace org-${ORGANIZATION_NAME} \
    get secrets ${CLUSTER_NAME}-sa -o jsonpath="{.data.tls\.crt}" \
    | base64 --decode > sa.pub
```

The following section assumes that the public key is available in the `sa.pub` file.

### Setup OpenID Connect issuer

We first need a way to host the discovery and JWKS documents required by OpenID Connect.
These documents do not contain sensitive information, and must be hosted on a publicly accessible endpoint.
For this we will use an Azure Storage Account.

Download [`setup-oidc-issuer.sh`](./setup-oidc-issuer.sh) and review the variables at the beginning of the script.
The script will:

  1. Deploy an Azure Storage Account.
  2. Generate and publish the OIDC discovery document.
  3. Generate and publish the OIDC JWKS document.

Be sure to copy the URL of your OIDC issuer shown at the end of the script output.
You will need it in the next steps.

### Configure workload cluster

Once the OIDC Issuer is created, you must configure it as a service account issuer in your workload cluster.
You can do so by adding the following workload cluster configuration:

```yaml
cluster:
  providerIntegration:
    controlPlane:
      kubeadmConfig:
        clusterConfiguration:
          apiServer:
            serviceAccountIssuers:
              # Fill in your own OIDC Issuer here.
              # Example: https://oidcissuera67fb168.z6.web.core.windows.net
              - url: 
              # Make sure to include this entry, leaving it at this value.
              - url: https://kubernetes.default.svc.cluster.local
```

Applying this configuration will roll the control plane.
After the configuration is done, applications in your cluster can use Azure Workload Identity.

### Deploy mutating admission webhook controller

The Azure Workload Identity webhook mutates Pods to include the necessary configuration for Azure Workload Identity.

You can deploy it using [`deploy-mutating-admission-webhook-controller.sh`](./deploy-mutating-admission-webhook-controller.sh).

Once the webhook has finished installing, your workload cluster supports Azure Workload Identity.

## Example usage

This section is based on [Azure's quick start guide](https://azure.github.io/azure-workload-identity/docs/quick-start.html).

You can run the [example script](./azwi-example.sh) to test your setup.

Running the script will:

* Deploy an Azure Key Vault
* Create a user-assigned managed identity
* Grant permission to the identity to read secrets from the Key Vault
* Deploy an example application to your workload cluster to read a secret

Please make sure that you review the variables at the beginning of the script and make the necessary changes.

If the test is successful, the `quick-start` Pod should periodically log something like this:

```console
I0210 15:46:04.114179       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:47:04.274439       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:48:04.404953       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:49:04.696782       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:50:04.816333       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:51:05.003743       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:52:05.120376       1 main.go:63] "successfully got secret" secret="Hello\\!"
I0210 15:53:05.285953       1 main.go:63] "successfully got secret" secret="Hello\\!"
```
