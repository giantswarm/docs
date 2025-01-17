---
linkTitle: Multi-account
title: Multi-account support
description: By default, all your workload clusters run in the same cloud provider account. With multi-account support for AWS and Azure, you can define a specific cloud provider account to use per organization.
weight: 170
menu:
  main:
    parent: advanced-infrastructure-management
user_questions:
- What use cases are supported by the multi-account functionality?
- How do I setup multi-account functionality?
- How can I run workload clusters in different cloud provider accounts?
last_review_date: 2023-11-07
aliases:
  - /advanced/infrastructure-management/multi-account
  - /basics/multi-account/
  - /advanced/multi-account
  - /guides/multi-account
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

The Giant Swarm architecture distinguishes between the management cluster and workload clusters. The management cluster enables the creation and operation of workload clusters and the workload cluster(s) run your Kubernetes workloads.

{{< platform_support_table aws="ga" azure="ga" >}}

## How does multi-account support help? {#benefits}

Both on AWS and Azure, workload cluster resources usually exist in an account (or in Azure terms: a subscription) separate from the one hosting the management cluster resources. We configure a default account to use for all workload clusters in an installation. Both accounts, the one for the management cluster and the default one for workload clusters, are under the customer's jurisdiction.

**Note:** Some customers use the same account/subscription for both management cluster and workload clusters. This choice does not affect the capabilities described below.

With multi-account support you can have more fine-grained control over the accounts used by workload clusters. Each Giant Swarm organization in an installation can have an individual configuration of which cloud provider account to use.

The following two schemas illustrate the difference:

![same-account](same-account.png)

![same-account](separate-accounts.png)

This enables use cases such as

- Several teams, business units, or profit centers sharing an installation, where many or all of them run workload clusters in their own cloud provider account, separate from each other.

- An ISV, being the Giant Swarm customer, creating and giving access to workload clusters in the name of a third party, in the third party's cloud provider account. The third party in this scenario has no relationship with Giant Swarm and needs no access to the Giant Swarm management cluster.

In both cases, customers benefit from simpler usage and cost allocation, plus a higher level of security through isolation. It can also help to make use of credits available in certain accounts.

## Provider-specific mechanisms {#provider-specific}

Details of the implementation differ between AWS and Azure.

- On AWS, Giant Swarms uses two separate IAM roles in order to act in the workload cluster account: one for use by automation, one for technical support staff.

- On Azure, one service principal is configured for Giant Swarm, used by automation and technical support staff.

## Additional information {#details}

- Cloud provider account/subscription credentials are specified on the (Giant Swarm) **organization level**.

- Cloud provider credentials are **immutable**. Once specified on an organization, cloud provider credentials cannot be modified or deleted. In order to switch to new cloud provider credentials you'll have to create a new organization and migrate to new clusters owned by that organization.

- If an organization does not yet have provider credentials configured but already has workload clusters, these clusters are run in the default workload cluster account. Setting credentials for this organization does not affect the workload clusters created already.

## Further reading

- [The Giant Swarm AWS Architecture]({{< relref "/vintage/platform-overview/cluster-management/vintage/aws" >}}) explains the setup of Giant Swarm on AWS, in more detail.
- [The Giant Swarm Azure Architecture]({{< relref "/vintage/platform-overview/cluster-management/vintage/azure" >}}) explains the setup of Giant Swarm on Azure, in more detail.
