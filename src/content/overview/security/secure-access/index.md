---
title: Secure access to clusters
description: Our team needs access to your clusters for management purposes. Here's how we make sure this access is secure and responsible.
weight: 30
menu:
  principal:
    parent: overview-security
last_review_date: 2025-05-15
aliases:
  - /vintage/platform-overview/security/cluster-security/cluster-access/
user_questions:
  - How do you access my infrastructure provider account?
  - How do you safeguard admin access to my clusters?
  - What is Teleport and how does it improve security?
  - What's the difference between user access and admin access?
  - How can I control access to my clusters?
  - Which APIs let me access my clusters?
  - How do I get access to my clusters?
  - Who can access my clusters?
  - Why does the Giant Swarm team need access to my clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

You get secure access to your workload clusters by default. Our team at Giant Swarm also needs access to these clusters in order to provide you with the best support.

This guide walks you through how this access works and the security measures implemented to ensure your clusters are managed securely and responsibly.

## Intro

Let's talk about the two types of access to your Giant Swarm clusters:

1. User access - this is for you and your team to interact with your services.

2. Admin access - this is for our team to help with management, development, and support.

Want to learn more about how our infrastructure works? Check out our [operational layers article]({{< relref "/overview/architecture/operational-layers" >}})

## User access

We expose the Kubernetes API of each workload cluster to you. You can [manage who gets access by connecting your external identity provider]({{< relref "/overview/architecture/authentication" >}}) to the Kubernetes API.

## Admin access via Teleport

### What is Teleport?

[Teleport](https://goteleport.com/) is an open-source tool that helps us manage secure access to your infrastructure. It uses an identity-aware reverse proxy and short-lived certificates instead of passwords or long-lived keys. This makes your clusters more secure and helps us follow regulations and work with different network setups.

Teleport is awesome because it:

- Requires no open ports, publicly accessible machines, or privileged bastion hosts
- Works flexibly with our range of different customer network layouts
- Requires only outbound HTTPS traffic
- Uses short-lived, tightly scoped credentials
- Provides detailed audit logging to us and to our customers

### Teleport secured access points

We use Teleport to securely access:

- **SSH** - Node access is exposed through Teleport, which authenticates the user and records the session without requiring personal SSH keys on customer machines.
- **Kubernetes API** - Management cluster and workload cluster Kubernetes API server access is auditable and can be fully private.
- **Apps** - User interfaces for Giant Swarm apps are also exposed and protected by Teleport, minimizing the number of components that require public endpoints.

Here's a diagram that shows how our Teleport setup works:

![Teleport Architecture](teleport.png)

We secure Teleport access with GitHub Single Sign-On (SSO) and multi-factor authentication. Only people in our GitHub organization can log in.

We've built our Teleport cluster to be super reliable, and we keep detailed access and audit logs for every session.

### Infrastructure provider access

You'll also need to grant our operators admin rights to your infrastructure provider so that we can manage your cluster's lifecycle - creating, configuring, and cleaning up resources like machines, networks, and security groups.

