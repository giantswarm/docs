---
linkTitle: Operational layers
title: Giant Swarm operational layers
description: Here you learn how the operational layers of Giant Swarm are defined and what the intended operational model is.
weight: 20
menu:
  main:
    parent: security
last_review_date: 2020-11-22
user_questions:
  - What are the Giant Swarm operational layers?
  - Why does Giant Swarm use several operational layers?
  - What is the Giant Swarm infrastructure layer?
  - Who has access to the infrastructure layer?
  - What is the Giant Swarm management cluster?
  - Who has access to the Giant Swarm management cluster?
  - What is the Giant Swarm API?
  - Who has access to the Giant Swarm API?
  - What is the Giant Swarm user space?
  - Who has access to the Giant Swarm user space?
  - How is the Giant Swarm infrastructure layer accessed?
  - What are the security safegaurds around access to the Giant Swarm infrastructure layer?
  - What are the security safegaurds around access to the Giant Swarm management cluster?
  - How is access to the management cluster authorized?
  - How do users access workload clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-horizon
---

# Giant Swarm operational layers

A Giant Swarm installation has several operational layers. At Giant Swarm we use the term operational layeres in order to indicate the different layers of code that may require access by different users for different activities. Operational layers in this context are in effect a representation of a separation of concerns both on an operational and on a security level. In this document we will define the layers and explain the operational model.

## Operational layers

We will go through the operational layers one by one from the bottom (infrastructure) to the top (user space) and explain the intended operational model by defining (typical) users and permission levels. The layers are:

1. [Infrastructure](#infrastructure)
2. [Giant Swarm management cluster](#management-cluster)
3. [Giant Swarm API](#giant-swarm-api)
4. [User Space](#userspace)

### Infrastructure {#infrastructure}

The infrastructure layer covers the area on top of actual (or virtual) machines, networking, etc., which is managed by Giant Swarm SREs (Site Reliability Engineers). It is usually accessed through VPN and bastion hosts as well as through the cloud provider APIs if applicable.

This layer does not include the actual hardware and maintenance of the data center. This is either covered by the (internal or external) data center provider or by the cloud provider.

On this layer, Giant Swarm SREs have root level SSH access to everything that pertains to a Giant Swarm installation. This is facilitated by a Single Sign On (SSO) mechanism including MFA (multi-factor authentication). On the cloud they additionally have access to the cloud account/subscription through a role to set up and manage the cloud resources.

### Giant Swarm management cluster {#management-cluster}

The Giant Swarm management cluster consists mainly of services running inside the management cluster.

Network access to the Management API is allowed only through Giant Swarm VPN and customer VPN.

Giant Swarm SREs and operations personnel have cluster admin access to the Management API through a tunnel. It is facilitated by SSO with MFA, as described above.

A customer has *tenant admin* and *view* access via OpenID Connect (OIDC), configured towards the supported identity provider.

#### Management API access for Customers

The Kubernetes API on every management cluster has [dex](https://github.com/dexidp/dex) installed as an OIDC issuer. Dex is configured with an identity provider chosen by the customer. A list of supported providers can be found in the [dex github repository](https://github.com/dexidp/dex/tree/master/connector).
[dex-k8s-authenticator](https://github.com/mintel/dex-k8s-authenticator) is also installed, it is a web app that helps in JWT token retrieval and kubectl configuration

##### Authorization

With a valid *jwt* token, received from your chosen identity provider, customers can have two levels of access:

- *view*
    - *get*/*list*/*watch* access to all resources in the management cluster, except for `configmaps` and `secrets`.
    - *get*/*list*/*watch* access to all resources (including `configmaps` and `secrets`) in workload cluster namespaces.
- *admin*
    - full access, to the `cluster`, `node pool`, `appcatalogs` and `apps` resources of management cluster Kubernetes.
    - includes *view* level access.
  
### Giant Swarm Rest API {#giant-swarm-api}

The [Giant Swarm API](/api/) is a customer facing API that is usually whitelisted for only a certain IP range within the customer's network. This layer covers the API itself, and its client manifestations in the form of the Giant Swarm Web UI and `gsctl` CLI.

On this layer there are two levels of access:

#### 1. Giant Swarm API admin

This access level is reserved for Giant Swarm operations and support personnel and like the above layers is facilitated by SSO with MFA.

Admin users have access to all organizations and all clusters in the Giant Swarm installation.

#### 2. Giant Swarm API user

This is the standard type of Giant Swarm API user that is given out to DevOps/Operations personnel on the customer side. Usually that covers only few users that are tasked with cluster creation and management.

Such users have access to all clusters in the organizations they belong to. They can create new clusters and organizations as well as manage or delete cluster and organization that they are part of. They can be considered multi-cluster admins.

### User space {#userspace}

The user space layer is defined as the layer pertaining to a single workload cluster Kubernetes API. Workload clusters are the Kubernetes clusters that run your workloads.

Users on this level are either created by a Giant Swarm API user (in form of key pairs) or managed in an external identity provider (IdP), like [Azure Active Directory](/guides/authenticating-with-microsoft-azure-active-directory/) or any other OIDC-compliant IdP.

However, a user with access to the Kubernetes API does not gain any permisssions by default, as the clusters are locked down by RBAC. To provide access, a cluster admin first needs to create roles and bindings for the users. These roles can be defined as narrowly or broadly as needed for the specific Tenant Kubernetes Cluster. They can be bound to either single users or groups of them.

This enables the customer to individually set up their user management according to the needs of their organization. The configuration for this can be kept in version control and needs to be done by an initial cluster admin user, which can be created by the Giant Swarm API user mentioned above.

Giant Swarm operational layers are the means which we use to keep a separation of concerns between different users of the Giant Swarm platform. This reduces burden from an operational perspective as well as enhancing security.

## Further reading

- [Securing your Cluster with RBAC and PSP](/guides/securing-with-rbac-and-psp/)
- [Creating a kubeconfig with gsctl]({{< relref "/ui-api/gsctl/create-kubeconfig" >}})
- [Creating a key pair with gsctl]({{< relref "/ui-api/gsctl/create-keypair" >}})
