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

The Giant Swarm API is a customer facing API that is usually whitelisted for only a certain IP range within the customer's network. This layer covers the API itself, but also its easy to use client manifestations in form of the Happa Web UI and `gsctl` CLI.

On this layer there's two types of access:

1. Giant Swarm API admin - access to all orgs and clusters in an installation
2. Giant Swarm API user - access to all clusters in the orgs they belong to

### User space

Kubernetes

1. Kubernetes users (either certs created by 3 or OIDC role mapping also by 3) - access limited based on RBAC