---
linkTitle: Client certificates for clusters
title: Creating workload cluster client certificates via the Platform API
description: We recommend OIDC for authentication to the workload cluster Kubernetes API. However, in some scenarios, client certificates are a viable alternative. Here we explain how to create such certificates via the Platform API.
weight: 80
menu:
  main:
    parent: reference-platform-api
user_questions:
  - How to create workload cluster client certificates via the Platform API?
last_review_date: 2024-10-17
aliases:
  - /use-the-api/management-api/wc-key-pairs
  - /ui-api/management-api/wc-key-pairs/
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

As of `kubectl gs` v1.44.0, the [`login`]({{< relref "/vintage/use-the-api/kubectl-gs/login" >}}) command supports the creation of client certificates for workload clusters.

**Note**: We recommend the use of OIDC authentication over client certificates. Please see our related documentation:

- [Configure OpenID Connect (OIDC) with Dex to access your clusters]({{< relref "/vintage/advanced/access-management/configure-dex-in-your-cluster" >}})
- [Authenticating with Microsoft Azure Active Directory]({{< relref "/vintage/advanced/access-management/authentication-azure-ad" >}})
