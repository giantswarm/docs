---
linkTitle: Secure access to clusters
title: Secure access to clusters - Users and Giant Swarm support
description: This documentation explains security measures for users and Giant Swarm support to access your infrastructure.
weight: 30
menu:
  main:
    parent: platform-overview-security-cluster
last_review_date: 2022-12-07
aliases:
  - /platform-overview/security/cluster-security/cluster-access
  - /security/cluster-access
  - /basics/secured-access-to-clusters/
user_questions:
  - How does Giant Swarm access my cloud provider account?
  - How is admin access safeguarded?
  - What is admin access to a cluster?
  - What is Teleport?
  - What is the difference between user access and admin access to clusters?
  - What is user access to a cluster?
  - Which APIs enable user access to the clusters?
  - How do I get access my clusters?
  - Who has access to my clusters?
  - Why do Giant Swarm personnel need access to my clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
  - https://github.com/orgs/giantswarm/teams/team-rocket
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

It goes without saying that our customers will have secure access to their own workload clusters. In order to provide the best service possible, Giant Swarm staff also needs access to them.

In this document we will explain the nature of this access and the security measures in place to ensure management of your clusters is conducted privately and responsibly.

## Intro

Access to Giant Swarm clusters can be split into two parts.

1. User Access - designated for Giant Swarm customers to interact with the offered services.

2. Admin Access - designated for Giant Swarm staff for management/development/support purposes.

If you would like to know more about the different parts of the Giant Swarm infrastructure, please see our [operational layers article]({{< relref "/overview/architecture/operational-layers" >}})

## User access

The Kubernetes API of each workload cluster is exposed to customers. Authorized users of the cluster can be managed by connecting an external identity provider to the Kubernetes API.

## Admin access via Teleport

### What is Teleport?

[Teleport](https://goteleport.com/) is an open-source solution for managing secure access to infrastructure using identity-aware reverse proxy and short-lived certificates instead of passwords or long-lived keys. This helps strengthen security and simplifies compliance with regulations and network topology.

Some advantages of Teleport:

- Simplify VPN architecture
- Support more network layouts and overcome CIDR range limitations
- Increase security
- Audit logging
- Access to audit logs for customers

### Teleport at Giant Swarm

We use Teleport as a standard solution to maintain access to managed infrastructure for operational needs. Teleport offers us with robust audit and access logs which we lacked in our previous access management solution. Teleport's identity-aware reverse proxy with TLS routing simplifies and secures network access requirements, as VPN is no longer needed nor any additional ports needs to be open at customer network, as such, Teleport works seamlessly behind corporate firewalls, where only outbound HTTPS traffic to Giant Swarm hosted Teleport cluster needs to be allowed.

### Teleport secured access points

- **SSH** - SSH access is secured with Teleport (Node Agent).

- **Kubernetes API** - Usage of the Kubernetes API on the management/workload cluster is also secured with Teleport (Kube Agent).

The following diagram shows our Teleport architecture in more detail:

![Teleport Architecture](teleport.png)

Teleport cluster access is based on GitHub SSO with MFA. Only users in the GitHub Giant Swarm Organization are allowed to authenticate.

We run a highly resilient and available Teleport cluster with robust access and audit logs for each user session.

## Admin access via VPN (deprecated)

Admin access is restricted to a VPN that is managed via certificates (public/private keys).

Certificate management is backed by Hashicorp Vault, using the Giant Swarm GitHub organization for user authentication. Each Giant Swarm staff member uses their own individual keypair, the public key of which must be additionally signed by Vault after authorizing the user for each session.

### VPN secured access points

- **SSH** - SSH access is based on GitHub SSO. Only users in the GitHub Giant Swarm Organization are allowed to authenticate. The following diagram describes our SSH authentication in more detail:

![SSH access process diagram](ssh_access_process.svg)

Customer workload clusters are accessible only via SSH access to the Giant Swarm management cluster. The management cluster contains Giant Swarm's cluster automation and operations platform, and controls our access to the underlying workload clusters for diagnostic and "Day 2" operational reasons.

- **Management API** - Usage of the Kubernetes API on the management cluster is also secured with SSH.

### General VPN connection schema

The following schema illustrates what the VPN connection looks like in practice.

![VPN diagram](site-to-site-vpn.png)

A cluster can be accessed by connecting to a Giant Swarm VPN server which establishes a secure connection with the jump host of the cluster.

We use two different VPN providers to provide highly resilient and available support to our customers.

### Cloud provider access

Currently, Giant Swarm operators - which are responsible for managing cluster lifecycle - are granted admin rights by the customer to the given cloud provider. This is necessary to create, configure, and clean up the underlying resources (machines, networks, security groups, etc.) used by the cluster.

The operator secret used for authentication with the cloud provider is stored in etcd.
Access to etcd or the Kubernetes API is secured based on certificates signed by Vault, to which only personnel in the Giant Swarm GitHub organization have access.

## Further reading

- [GitHub Vault authentication](https://www.vaultproject.io/docs/auth/github)
- [Vault SSH certificate](https://www.vaultproject.io/docs/secrets/ssh/signed-ssh-certificates)
- [Giant Swarm Operational Layers]({{< relref "/overview/architecture/operational-layers" >}})
- [Giant Swarm User Space]({{< relref "/overview/architecture/operational-layers#userspace" >}})
