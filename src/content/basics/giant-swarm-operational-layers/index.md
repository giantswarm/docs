---
title: Giant Swarm Operational Layers
description: Here you learn how the operational layers of Giant Swarm are defined and what the intended operational model is.
date: 2020-05-18
type: page
weight: 80
categories: ["basics"]
---

# Giant Swarm Operational Layers

A Giant Swarm installation has several operational layers. This represents a separation of concerns both on an operational as well as on a security level. In this document we will define the layers and explain the operational model.

## Operational layers

We will go through the operational layers one by one from the bottom (infrastructure) to the top (user space) and explain the intended operational model by defining (typical) users and permission levels. The layers are:

1. [Infrastructure](#infrastructure)
2. [Giant Swarm Control Plane](#controlplane)
3. [Giant Swarm API](#giant-swarm-api)
4. [User Space](#userspace)

### Infrastructure {#infrastructure}

The infrastructure layer covers the area on top of actual (or virtual) machines, networking, etc., which is managed by Giant Swarm SREs (Site Reliability Engineers). It is usually accessed through VPN and bastion hosts as well as through the cloud provider APIs if applicable.

This layer does not include the actual hardware and maintenance of the data center. This is either covered by the (internal or external) data center provider or by the cloud provider.

On this layer, Giant Swarm SREs have root level SSH access to everything that pertains to a Giant Swarm installation. This is facilitated by a Single Sign On (SSO) mechanism including MFA (multi-factor authentication). On the cloud they additionally have access to the cloud account/subscription through a role to set up and manage the cloud resources.

### Giant Swarm control plane {#controlplane}

The Giant Swarm Control Plane consists mainly of services running inside the Control Plane Kubernetes cluster.

Control Plane Kubernetes API network access is allowed only through Giant Swarm VPN and customer VPN.

Giant Swarm SREs and operations personnel have cluster admin access to the Control Plane Kubernetes API through a tunnel. It is facilitated by SSO with MFA, as described above.

A customer has *tenant admin* and *view* access via OpenID Connect (OIDC), configured towards the supported Identity Provider.

#### Control Plane Kubernetes API Access for Customers

The kubernetes API on every Control has [dex](https://github.com/dexidp/dex) installed as an OIDC issuer. Dex is configured with an Identity Provider chosen by the customer. A list of supported providers can be found in the [dex github repository](https://github.com/dexidp/dex/tree/master/connector).
[dex-k8s-authenticator](https://github.com/mintel/dex-k8s-authenticator) is also installed, it is a web app that helps in JWT token retrieval and kubectl configuration

##### Authorization

With a valid *jwt* token, received from your chosen Identity Provider, customers can have two levels of access:

- *view*
    - *get*/*list*/*watch* access to all resources in the Control Plane, except for `configmaps` and `secrets`.
    - *get*/*list*/*watch* access to all resources (including `configmaps` and `secrets`) in tenant cluster namespaces.
- *admin*
    - full access, to the `cluster`, `node pool`, `appcatalogs` and `apps` resources of Control Plane Kubernetes.
    - includes *view* level access.
  
### Giant Swarm API {#giant-swarm-api}

The [Giant Swarm API](https://docs.giantswarm.io/api/) is a customer facing API that is usually whitelisted for only a certain IP range within the customer's network. This layer covers the API itself, and its client manifestations in the form of the Giant Swarm Web UI and `gsctl` CLI.

On this layer there are two levels of access:

#### 1. Giant Swarm API admin

This access level is reserved for Giant Swarm operations and support personnel and like the above layers is facilitated by SSO with MFA.

Admin users have access to all organizations and all clusters in the Giant Swarm installation.

#### 2. Giant Swarm API user

This is the standard type of Giant Swarm API user that is given out to DevOps/Operations personnel on the customer side. Usually that covers only few users that are tasked with cluster creation and management.

Such users have access to all clusters in the organizations they belong to. They can create new clusters and organizations as well as manage or delete cluster and organization that they are part of. They can be considered multi-cluster admins.

### User space {#userspace}

The user space layer is defined as the layer pertaining to a single Tenant Cluster Kubernetes API. Tenant Cluster are the Kubernetes clusters that run your workloads.

Users on this level are either created by a Giant Swarm API user (in form of key pairs) or managed in an external Identity Provider (IdP), like [Azure AD](https://docs.giantswarm.io/guides/authenticating-with-microsoft-azure-active-directory/) or any other OIDC compliant IdP.

However, a user with access to the Kubernetes API does not gain any permisssions by default, as the clusters are locked down by RBAC. To provide access, a cluster admin first needs to create roles and bindings for the users. These roles can be defined as narrowly or broadly as needed for the specific Tenant Kubernetes cluster. They can be bound to either single users or groups of them.

This enables the customer to individually set up their user management according to the needs of their organization. The configuration for this can be kept in version control and needs to be done by an initial cluster admin user, which can be created by the Giant Swarm API user mentioned above.

## Further reading

- [Securing your Cluster with RBAC and PSP](https://docs.giantswarm.io/guides/securing-with-rbac-and-psp/)
- [Creating a kubeconfig with gsctl](https://docs.giantswarm.io/reference/gsctl/create-kubeconfig/)
- [Creating a key pair with gsctl](https://docs.giantswarm.io/reference/gsctl/create-keypair/)
