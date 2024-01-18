---
linkTitle: Provider credentials
title: Handling cloud provider credentials
description: Where to configure the cloud provider account/subscription to be used, and how to deposit credentials via the Management API.
weight: 30
menu:
  main:
    parent: uiapi-managementapi
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
last_review_date: 2024-01-18
aliases:
  - /ui-api/management-api/credentials/
user_questions:
  - How can I provide AWS identity details to use with my workload clusters?
  - How can I provide Azure identity details to use with my workload clusters?
  - How can I set cloud provider credentials via the Management API?
---

### Notice: This document describes how to configure cloud provider credentials for _vintage_ Giant Swarm Clusters. For _CAPI_ Clusters, upstream documentation is available for [CAPA](https://cluster-api-aws.sigs.k8s.io/topics/multitenancy) and [CAPZ](https://capz.sigs.k8s.io/topics/multitenancy/)

In order to manage workload clusters in your cloud provider accounts/subscriptions, the Giant Swarm controllers require some configuration so they are able to act on your behalf.

In this article we explain how to provide this configuration via the Management API.

## Terminology

As we are dealing with two cloud providers here which use different vocabulary in their own worlds, let's first establish some terminology for this article.

- **Account** (AWS) or **Subscription** (Azure): we use the term _account_ here for both.
- **Credentials**: a set of details which enable a controller or a Giant Swarm staff member to work with your cloud provider account on your behalf. This article is mostly about providing these credentials in the right place and format.

## Credential secrets explained

Credentials are stored in the management cluster in the form of a `Secret` resource.

In the `metadata`, credential secrets _must_ provide the `giantswarm.io/managed-by: credentiald` and `app: credentiald` labels. We also _recommend_ to choose a resource name starting with `credential-`.

The `data` part contains the cloud provider credentials that should be used. The format here differs slightly between cloud providers.

{{< tabs >}}
{{< tab title="AWS" >}}

Here is an example for AWS:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: credential-example
  namespace: my-namespace
  labels:
    app: credentiald
    giantswarm.io/managed-by: credentiald
data:
  aws.admin.arn: YXJuOmF3czppYW06OjEyMzQ1Njc4OTA6cm9sZS9HaWFudFN3YXJtQWRtaW4=
  aws.awsoperator.arn: YXJuOmF3czppYW06OjEyMzQ1Njc4OTA6cm9sZS9HaWFudFN3YXJtQVdTT3BlcmF0b3I=
```

In above AWS example, these are two fields which both indicate AWS IAM role identifiers (ARNs). As typical with opaque secrets, the value is encoded in base64. Here is how the two example strings would look like when decoded:

| Key                   | Example value (decoded)                              |
|-----------------------|------------------------------------------------------|
| `aws.admin.arn`       | `arn:aws:iam::1234567890:role/GiantSwarmAdmin`       |
| `aws.awsoperator.arn` | `arn:aws:iam::1234567890:role/GiantSwarmAWSOperator` |

The first of the two identifies the IAM role to be assumed by Giant Swarm staff for operations tasks. The second one is used by `aws-operator`, which is the software in charge of automatic cluster management. Easily visible, they include the numeric AWS account ID and also the IAM role name to be assumed.

We provide [detailed documentation]({{< relref "/getting-started/cloud-provider-accounts/vintage/aws" >}}) regarding how to configure these roles in your AWS account.

{{< /tab >}}
{{< tab title="Azure" >}}

Here is an example for a credential secret on Azure:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: credential-example
  namespace: my-namespace
  labels:
    app: credentiald
    giantswarm.io/managed-by: credentiald
data:
data:
  azure.azureoperator.clientid: MTIzNGFiY2QtYWIxMi0xMmFiLWNkMzQtYWJjZDEyMzRhYmNkCg==
  azure.azureoperator.subscriptionid: NTY3OGFiY2QtYWI1Ni01NmFiLWNkNTYtYWJjZDU2NzhhYmNkCg==
  azure.azureoperator.tenantid: MTIzNGRlZmctZGUxMi0xMmRlLWRlMzQtZGVmZzEyMzRkZWZnCg==
  azure.azureoperator.clientsecret: YWJjZC1lZmdoaWprbG1uTE9QUTEyMzQ1Njd+ODlSU3R1dnd4Cg==
```

Here the `data` part contains four fields which specify the IDs of `Client`, `Subscription` and `Tenant` as well as the `Client Secret`.

Decoded example:

| Key                                  | Example value (decoded)                |
|--------------------------------------|----------------------------------------|
| `azure.azureoperator.clientid`       | `1234abcd-ab12-12ab-cd34-abcd1234abcd` |
| `azure.azureoperator.subscriptionid` | `5678abcd-ab56-56ab-cd56-abcd5678abcd` |
| `azure.azureoperator.tenantid`       | `1234defg-de12-12de-de34-defg1234defg` |
| `azure.azureoperator.clientsecret`   | `abcd-efghijklmnLOPQ1234567~89RStuvwx` |

In order for `azure-operator` to manage workload clusters using these credentials, it will need access to your `Subscription` using a `Service Principal`.

We provide a [detailed guide]({{< relref "/getting-started/cloud-provider-accounts/vintage/azure" >}}) prepare and obtain this data.

{{< /tab >}}
{{< /tabs >}}

## Referencing credentials in the cluster resource {#explicit}

When creating a workload cluster, depending on the cloud provider, there will be an [`AWSCluster`]({{< relref "/use-the-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) or [`AzureCluster`]({{< relref "/use-the-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) resource created, containing the provider-specific configuration of your workload cluster.

If you create your cluster manifest manually or via the [`kubectl gs template cluster`]({{< relref "/use-the-api/kubectl-gs/template-cluster" >}}) command, you are free to adapt the provider cluster resource to match your exact requirements before submitting the manifest to the API (e. g. via `kubectl apply`).

In **AWS**, it is possible to reference your credential secret directly. The custom resource definition (CRD) provides an attribute [`.spec.provider.credentialSecret`]({{< relref "/use-the-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md#v1alpha3-.spec.provider.credentialSecret" >}}). The two sub-attributes `name` has to match the credential secret's resource name. The `namespace` sub-attribute accordingly must match the secret's namespace.

Note that this attribute has to be set _before_ submitting the manifest to the Management API. Otherwise, if the `AWSCluster` resource gets submitted without any `.spec.provider.credentialSecret` in place, our admission controllers will fill in default values. Read on to understand the defaulting logic.

On **Azure**, the `AzureCluster` field  [`.spec.identityRef`]({{< relref "/use-the-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md#v1alpha4-.spec.identityRef" >}}) is set by the `azure-operator`. It references credential secrets indirectly by creating an `org-credential` based on the organization your workload cluster is created in.

## Defaulting

If the cluster resource does not reference a provider credential secret to use (as explained above), our admission controller fills in some defaults, in this logical order

1. An organization's credential secret is used, if it exists
2. Otherwise the installation's default secret is used

Both options are explained in further detail below.

### Organization default credentials {#organization-default}

Any workload cluster in Giant Swarm belongs to an [organization]({{< relref "/platform-overview/multi-tenancy" >}}) as encoded in the `giantswarm.io/organization` label of the cluster's [`Cluster`]({{< relref "/use-the-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) resource.

For each organization you can also deposit a credential secret which will be used automatically for any new workload cluster that does not specify credentials explicitly (as explained [above](#explicit)). To be looked up as the organization's default credentials, your `Secret` resource must match the following requirements:

- The label `giantswarm.io/organization` must be present, with the value matching the organization name
- There must not be any other credential secret matching the same `giantswarm.io/organization` label value.

This partial example shows the required metadata:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: credential-example
  namespace: org-example
  labels:
    app: credentiald
    giantswarm.io/managed-by: credentiald
    giantswarm.io/organization: acme
data:
  ...
```

### Installation default credentials {#installation-default}

As a last resort, if credentials are not referenced [explicitly](#explicit) and no [organization default credentials](#organization-default) are found, our defaulting will use the installation default credentials.

The installation default credentials are typically configured for you by Giant Swarm, using credentials that you provide. They are placed in the namespace `giantswarm` and thus normally not accessible to customers directly.

The idea of the default credentials is to enable every organization to create clusters, even if they don't have specific credentials configured. This can be a viable use case if all tenants are trusted and should be allowed to use the same cloud provider account.

## Choosing the right method for you

The defaulting options as well as the option to reference credentials explicitly per workload cluster should offer the right method for each use case. To sum up the different methods and reasons to use them:

- If you want to run all workload clusters in the same cloud provider account, use the **installation default credentials**. As a result you won't have to worry about this detail during cluster creation at all.

- If you plan to run each organization's clusters in a different cloud provider account, use the **organization default credentials** mechanism. Just make sure to set up the organization's credentials as early as possible, to prevent any cluster running via the installation default credentials.

- On AWS, you can **set the cloud provider credentials explicitly** for more flexibility. Whether you want to rely on organization level or installation level defaults as a fall back is up to you.

## Further reading

- [aws-admission-controller](https://github.com/giantswarm/aws-admission-controller/): Explore the source code of the component that does the defaulting of AWS credentials on cluster creation.
- [azure-operator](https://github.com/giantswarm/azure-admission-controller/): Explore the source code of the component that takes care of the indirect reference of Azure credentials on cluster creation.
