+++
title = "Giant Swarm Operational Layers"
description = "Here you learn how the operational layers of Giant Swarm are defined and what the intended operational model is."
date = "2018-10-12"
type = "page"
weight = 30
categories = ["basics"]
+++

# Giant Swarm Operational Layers

A Giant Swarm installation has several operational layers, which depict a separation of concerns both on an operational level as well as on a security level. In the following we will define the layers and explain the intended operational model.

## Operational Layers

We will go through the operational layers one by one from the bottom (infrastructre) to the top (user space). The layers are:

1. Infrastructure
2. Giant Swarm Control Plane
3. Giant Swarm API
4. User Space

### Infrastructure

The infrastructre layer covers the area of actual (or virtual) machines, networking, etc., which is managed by Giant Swarm SREs usually accessed through VPN and bastion hosts.

This layer does not include the actual hardware and maintenance of the Data Center. This is either covered by the (internal or external) Data Center provider or by the Cloud provider.

Giant Swarm SREs on this layer have root level SSH access to everything that pertains to a Giant Swarm installation. This is facilitated by a Single Sign On (SSO) mechanism including MFA.

### Giant Swarm Control Plane

The Giant Swarm Control Plane consists mainly of Services running inside the Control Plane Kubernetes cluster.

Just like the former layer, this layer is accessed through VPN and bastion hosts. Giant Swarm SREs and Operations personel have cluster admin access to the Control Plane Kubernetes API through a tunnel, which is again facilitated by SSO with MFA.

### Giant Swarm API

The Giant Swarm API (GS API) is a customer facing API that is usually whitelisted for only a certain IP range within the customer's network. This layer covers the API itself, but also its easy to use client manifestations in form of the Happa Web UI and `gsctl` CLI.

On this layer there's two types of access:

1. Giant Swarm API admin

This access level is reserved for Giant Swarm Operations and Support personel and like the above layers facilitated by SSO with MFA.

Such admin users have access to all organizations and all clusters in the Giant Swarm installation.

2. Giant Swarm API user

This is the standard type of GS API user that is given out to DevOps/Operations personel on the customer side.

Such users have access to all clusters in the organizations they belong to. They can be considered multi-cluster admins.

### User Space

The User Space layer is defined as the layer pertaining to a single Tenant Cluster Kubernetes API.

Users on this level are either created by a Giant Swarm API user (in form of key pairs) or managed in an external Identity Provider (IdP), like [Azure AD](https://docs.giantswarm.io/guides/authenticating-with-microsoft-azure-active-directory/) or any other OIDC compliant IdP.

However, a user with access to the Kubernetes API does not by default also gain any permissions, as the clusters are locked down by RBAC. Thus, a cluster admin first needs to create roles and bindings for the users. These roles can be defined as narrow as needed or as broad as being on cluster admin level for the specfic Tenant Kubernetes cluster. They can be bound to either single users or groups thereof. This enables the customer to individually set up their user management according to the needs of their organization.

## Further Reading

- [Securing your Cluster with RBAC and PSP](https://docs.giantswarm.io/guides/securing-with-rbac-and-psp/)
- [Creating a kubeconfig with gsctl](https://docs.giantswarm.io/reference/gsctl/create-kubeconfig/)
- [Creating a key pair with gsctl](https://docs.giantswarm.io/reference/gsctl/create-keypair/)