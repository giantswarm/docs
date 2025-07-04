---
linkTitle: Operational layers
title: Giant Swarm operational layers
description: Here you learn how the operational layers of Giant Swarm are defined and what the intended operational model is.
weight: 10
menu:
  principal:
    parent: overview-architecture
    identifier: overview-architecture-operational-layers
last_review_date: 2024-12-04
user_questions:
  - What are the Giant Swarm operational layers?
  - Why does Giant Swarm use several operational layers?
  - What is the Giant Swarm infrastructure layer?
  - Who has access to the infrastructure layer?
  - What is the Giant Swarm management cluster?
  - Who has access to the Giant Swarm management cluster?
  - What is the Giant Swarm user space?
  - Who has access to the Giant Swarm user space?
  - How is the Giant Swarm infrastructure layer accessed?
  - What are the security safeguards around access to the Giant Swarm infrastructure layer?
  - What are the security safeguards around access to the Giant Swarm management cluster?
  - How is access to the management cluster authorized?
  - How do users access workload clusters?
aliases:
  - /platform-overview/security/operational-layers
  - /security/operational-layers
  - /basics/giant-swarm-operational-layers/
owner:
  - https://github.com/orgs/giantswarm/teams/team-planeteers
---

A Giant Swarm installation has several operational layers. At Giant Swarm we use the term operational layers in order to indicate the different layers of the system that may require access by different users for different activities. Operational layers in this context are in effect a representation of a separation of concerns both on an operational and on a security level. In this document we will define the layers and explain the operational model.

## Operational layers

We will go through the operational layers one by one from the bottom (infrastructure) to the top (user space) and explain the intended operational model by defining (typical) users and permission levels. The layers are:

1. [Infrastructure](#infrastructure)
2. [Giant Swarm management cluster and Platform API](#management-cluster)
3. [User Space](#userspace)

### Infrastructure {#infrastructure}

The infrastructure layer covers the area on top of actual (or virtual) machines, networking, etc., which is managed by Giant Swarm SREs (Site Reliability Engineers). It is usually accessed through VPN and bastion hosts as well as through the cloud provider APIs if applicable. In most installations there's also ssh access through [Teleport]({{< relref "/overview/security/secure-access/#admin-access-via-teleport" >}}).

This layer does not include the actual hardware and maintenance of the data center. This is either covered by the (internal or external) data center provider or by the cloud provider.

On this layer, Giant Swarm SREs have root level SSH access to everything that pertains to a Giant Swarm installation. This is facilitated by a Single Sign On (SSO) mechanism including MFA (multi-factor authentication) - in most cases using through Teleport, which keeps access auditable. On the cloud they additionally have access to the cloud account/subscription through a role to set up and manage the cloud resources.

### Giant Swarm management cluster {#management-cluster}

The Giant Swarm management cluster consists mainly of services running inside the management cluster.

Network access to the Platform API is allowed only through the respective customer network or VPN as well as Teleport or the Giant Swarm VPN.

Giant Swarm SREs and operations personnel have cluster admin access to the Platform API through a VPN or Teleport tunnel. Authentication is facilitated by SSO with MFA, as described above.

A customer has *tenant admin* and *view* access via OpenID Connect (OIDC), integrated with the respective customer identity provider and bound to respective user groups there.

#### Platform API access for Customers

The Platform API is basically the Kubernetes API on every management cluster. It has [dex](https://github.com/dexidp/dex) installed as an OIDC issuer. Dex is configured with an identity provider chosen by the customer. A list of supported providers can be found in the [dex GitHub repository](https://github.com/dexidp/dex/tree/master/connector).

##### Authorization

With a valid *JWT* token, received from your chosen identity provider, customers can have two levels of access:

- *view*
    - *get*/*list*/*watch* access to all resources in the management cluster, except for `configmaps` and `secrets`.
    - *get*/*list*/*watch* access to all resources (including `configmaps` and `secrets`) in workload cluster namespaces.
- *admin*
    - full access, to the `cluster`, `node pool`, `appcatalogs` and `apps` resources of the management cluster.
    - includes *view* level access.

There's a possibility for admins to create sub-roles to give other users within their organization access to Platform API features. As the API is a Kubernetes API, this is facilitated with standard RBAC role definitions.

This enables use cases where the central platform team can give limited access to sub-teams like and observability team, but also go as far as to give end user developers access to certain resources and use the Platform API as the API to their own Developer Platform.

Additionally, the Platform API includes a concept called organizations, which are special namespaces that can hold clusters and their apps, and are used to create a level of multi-tenancy within the Platform API. Tenant admins can create such organizations and bind users and user groups to them, so that action of these users are limited to the resources in the organizations they are part of.

### User space {#userspace}

The user space layer is defined as the layer pertaining to a single workload cluster Kubernetes API. Workload clusters are the Kubernetes clusters that run your workloads.

Tenant admins can manage access to workload clusters through different mechanisms:

They can create certificate-based access using the kubectl gs CLI. Using this access should be time-limited to set up RBAC roles and bindings for Service Accounts and OIDC users.

End users on this level are then created by a Tenant admin either as Service Accounts inside the workload cluster or managed in an [external identity provider (IdP)]({{< relref "/overview/architecture/authentication" >}}), like Azure Active Directory or any other OIDC-compliant IdP.

However, a user with access to the Kubernetes API does not gain any permissions by default, as the clusters are locked down using RBAC. To provide access, a cluster admin needs to create roles and bindings for the users. These roles can be defined as narrow or broad as needed for the specific cluster. They can be bound to either single users or groups of them.

This enables the customer to individually set up their user management according to the needs of their organization. The configuration for this can be kept in version control and needs to be done by an initial cluster admin user.

## Further reading

- [Securing your Cluster with RBAC and PSP]({{< relref "/tutorials/security/rbac" >}})
- [Creating a client certificate for workload cluster access]({{< relref "/reference/kubectl-gs/login/#workload-cluster-client-certificate" >}})
