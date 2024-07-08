---
title: Authentication
description: Authentication and authorization mechanisms in the Giant Swarm platform.
weight: 20
menu:
  principal:
    parent: overview-architecture
    identifier: overview-architecture-authentication
user_questions:
  - What are the authentication mechanisms in the Giant Swarm platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
last_review_date: 2024-06-26
---

During the management cluster installation, Giant Swarm sets up authentication and authorization mechanisms to secure access to the platform. These mechanisms ensure that only authorized users can interact with the platform and its resources.

## Platform API

The platform API is a Kubernetes API that operates on the management cluster. To allow access to the platform API, Giant Swarm sets up a [dex](https://github.com/giantswarm/dex-app) instance in the management cluster, configured with some default connectors that grant our staff access and additional connectors that can be configured by the customer.

Dex acts as a portal to other identity providers (idP) through "connectors". The supported connectors are [listed in the official dex documentation](https://dexidp.io/docs/connectors/) and we can walk you through the setup of any of them.

As mentioned before, we automatically configure Dex in management cluster, allowing you to authenticate using your own identity providers. For workload clusters, we do not enforce any specific OpenID Connect (OIDC) tool to enable single single-on (SSO).  If you want to configure OIDC using Dex to acesss your workload cluster, you can [follow our guide here](https://docs.giantswarm.io/vintage/advanced/access-management/configure-dex-in-your-cluster/).
