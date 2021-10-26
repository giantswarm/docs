---
linkTitle: Provider credentials
title: Handling cloud provider credentials
description: Where to configure the cloud provider account/subscription to be used, and how to deposit credentials via the Management API.
weight: 30
menu:
  main:
    parent: uiapi-managementapi
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
last_review_date: 2021-10-26
user_questions:
  - How can I provide AWS identity details to use with my workload clusters?
  - How can I set cloud provider credentials via the Management API?
---

# Handling cloud provider credentials via the Management API

Our operators which manage workload clusters in your cloud provider accounts/subscriptions require some configuration so they are able to act on your behalf. In this article we explain how to provide this configuration via the Management API.

**Note:** This article covers AWS only initially. An update for Azure is planned.

## Terminology

As we are dealing with two cloud providers here which use different vocabulary in their own worlds, let's first establish some terminology for this article.

- **Account** (AWS) or **Subscription** (Azure): we use the term _account_ here for both.
- **Credentials**: a set of details which enable an operator (either human or software) to work with your cloud provider account on your behalf. This article is mostly about providing these credentials in the right place and format.

## Credentials lookup order

On AWS, credentials are looked up in this order:

1. Find credentials assigned to the organization that owns the cluster.
2. If not found, find default credentials.

Let's take a closer look, starting with the default credentials.

### Default credentials

The default credentials are typically configured for you by Giant Swarm, using IAM role ARNs that you provide. They are placed in the namespace `giantswarm` and thus normally accessible to customers.

The idea of the default credentials is to enable every organization to create clusters, even if they don't have specific credentials configured. This can be a viable use case if all tenants are trusted and should be allowed to use the same cloud provider account.

### Organization credentials

Any workload cluster in Giant Swarm belongs to an [organization]({{< relref "/general/organizations" >}}) as encoded in the `giantswarm.io/organization` label of the cluster's [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) resource.

Credentials are stored in the management cluster in the form of a `Secret` resource. Here is an example:

```yaml
kind: Secret
apiVersion: v1
type: Opaque
metadata:
  name: credential-acme
  namespace: org-acme
  labels:
    app: credentiald
    giantswarm.io/managed-by: credentiald
    giantswarm.io/organization: acme
    giantswarm.io/service-type: system
data:
  aws.admin.arn: YXJuOmF3czppYW06OjEyMzQ1Njc4OTA6cm9sZS9HaWFudFN3YXJtQWRtaW4=
  aws.awsoperator.arn: YXJuOmF3czppYW06OjEyMzQ1Njc4OTA6cm9sZS9HaWFudFN3YXJtQVdTT3BlcmF0b3I=
```

In the `metadata`, just like in the `Cluster` resource, here we find again the name of the organization owning both the cluster and the secret (note: `acme` is an example organization name). And accordingly the secret is placed in the organization's namespace. In fact, this namespace placement is not required, as the credentials would be found in other namespaces, too.

The `data` part contains two fields which both indicate AWS IAM role identifiers (ARNs). As typical with opaque secrets, the value is encoded in base64. Here is how the two example strings would look like when decoded:

| Key                   | Example value (decoded)                              |
|-----------------------|------------------------------------------------------|
| `aws.admin.arn`       | `arn:aws:iam::1234567890:role/GiantSwarmAdmin`       |
| `aws.awsoperator.arn` | `arn:aws:iam::1234567890:role/GiantSwarmAWSOperator` |

The first of the two identifies the IAM role to be assumed by Giant Swarm staff for operations tasks. The second one is used by `aws-operator`, which is the software in charge of automatic cluster management. Easily visible, they include the numeric AWS account ID and also the IAM role name to be assumed.

We provide [detailed documentation]({{< relref "/getting-started/cloud-provider-accounts/aws" >}}) regarding how to configure these roles in your AWS account.

## Important notes

- An organization's credentials have to be in place before the first cluster of that organization is created. Otherwise the default credentials will be used. Adding organization specific credentials later will result in `aws-operator` attempting from then on to use the organization's credentials to manage the cluster. This would only work if the credentials were identical (same AWS account and roles).
- Do not delete the credentials of an organization as long as the organization still has workload clusters. The consequence would be a loss of capabilities to manage and delete the cluster's resources in your account.
- There must not be more than one credential secret assigned to the same organization (by the `giantswarm.io/organization` label). Otherwise it would not be possible to predict which would be used when.
