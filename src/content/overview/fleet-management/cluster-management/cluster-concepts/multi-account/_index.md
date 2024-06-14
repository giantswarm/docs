---
title: Multi-account clusters
description: Learn the advantages of using multi-account clusters in the Giant Swarm platform.
weight: 10
menu:
  principal:
    parent: overview-fleet-management-cluster-concepts
    identifier: overview-fleet-management-cluster-concepts-multi-account
last_review_date: 2024-06-14
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - Why should I use multi-account clusters in the Giant Swarm platform?
---

The Giant Swarm architecture distinguishes between the management cluster and workload clusters. The management cluster enables the creation and operation of workload clusters and the workload cluster(s) run your Kubernetes workloads.

{{< platform_support_table aws="ga" azure="ga" >}}

## How does multi-account support help? {#benefits}

NEEDS TO BE REWRITTEN

Both on AWS and Azure, workload cluster resources usually exist in an account (or in Azure terms: a subscription) separate from the one hosting the management cluster resources. We configure a default account to use for all workload clusters in an installation. Both accounts, the one for the management cluster and the default one for workload clusters, are under the customer's jurisdiction.

**Note:** Some customers use the same account/subscription for both management cluster and workload clusters. This choice does not affect the capabilities described below.

With multi-account support you can have more fine-grained control over the accounts used by workload clusters. Each Giant Swarm organization in an installation can have an individual configuration of which cloud provider account to use.

The following two schemas illustrate the difference:

![same-account](same-account.png)

![same-account](separate-accounts.png)

This enables use cases such as

- Several teams, business units, or profit centers sharing an installation, where many or all of them run workload clusters in their own cloud provider account, separate from each other.

- An ISV, being the Giant Swarm customer, creating and giving access to workload clusters in the name of a third party, in the third party's cloud provider account. The third party in this scenario has no relationship with Giant Swarm and needs no access to the Giant Swarm REST API or management cluster.

In both cases, customers benefit from simpler usage and cost allocation, plus a higher level of security through isolation. It can also help to make use of credits available in certain accounts.

## Provider-specific mechanisms {#provider-specific}

Details of the implementation differ between AWS and Azure.

- On AWS, Giant Swarms uses two separate IAM roles in order to act in the workload cluster account: one for use by automation, one for technical support staff. Details on the exact permissions required can be found in our guide on [preparing an AWS account to run Giant Swarm workload clusters]({{< relref "/vintage/getting-started/cloud-provider-accounts/vintage/aws" >}}).

- On Azure, one service principal is configured for Giant Swarm, used by automation and technical support staff. Details can be found in our guide on [preparing an Azure subscription to run Giant Swarm workload clusters]({{< relref "/vintage/getting-started/cloud-provider-accounts/vintage/azure" >}}).

## Additional information {#details}

- Cloud provider account/subscription credentials are specified on the (Giant Swarm) **organization level**.

- Cloud provider credentials are **immutable**. Once specified on an organization, cloud provider credentials cannot be modified or deleted. In order to switch to new cloud provider credentials you'll have to create a new organization and migrate to new clusters owned by that organization.

- If an organization does not yet have provider credentials configured but already has workload clusters, these clusters are run in the default workload cluster account. Setting credentials for this organization does not affect the workload clusters created already.

## Get started

To create clusters in a new cloud provider account, you first need to provide the credentials to the organization you'd like to use for this purpose. You are free to create a new organization for this purpose if you like. Organizations can be created in the Giant Swarm web UI, or via the [Giant Swarm REST API](/api/#operation/addOrganization).

To prepare your credentials, either as AWS account roles or as an Azure service principle, please follow our specific guides:

- [Prepare an AWS account to run Giant Swarm workload clusters]({{< relref "/vintage/getting-started/cloud-provider-accounts/vintage/aws" >}})
- [Prepare an Azure subscription to run Giant Swarm workload clusters]({{< relref "/vintage/getting-started/cloud-provider-accounts/vintage/azure" >}})

You can then assign the credentials to your organization in several ways:

- In the Giant Swarm web UI via the organization details page
- In `gsctl` using the [`update organization set-credentials`]({{< relref "/vintage/use-the-api/gsctl/update-org-set-credentials" >}}) command
- Via the [Giant Swarm REST API](/api/#operation/addCredentials)

All workload clusters created for that organization will then use the credentials provided to the organization and will reside in the account/subscription associated with them.

When inspecting details of such a cluster, or using the [`gsctl show cluster`]({{< relref "/vintage/use-the-api/gsctl/show-cluster" >}}) command, we display cloud provider details in the case the workload cluster does not reside in the default account.
