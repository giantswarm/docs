---
title: Authentication
description: Authentication and authorization mechanisms in the Giant Swarm platform.
weight: 20
menu:
  principal:
    parent: overview-architecture
    identifier: overview-architecture-authentication
user_questions:
  - What are the authentication and authorization mechanisms in the Giant Swarm platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
last_review_date: 2024-06-26
---

During the management cluster installation, Giant Swarm sets up authentication and authorization mechanisms to secure access to the platform. These mechanisms ensure that only authorized users can interact with the platform and its resources.

## Platform API

### Authentication

The platform API is a Kubernetes API that operates on the management cluster. To allow access to the platform API, Giant Swarm sets up a [dex](https://github.com/giantswarm/dex-app) instance in the management cluster, configured with some default connectors that grant our staff access and additional connectors that can be configured by the customer.

Dex acts as a portal to other identity providers (idP) through "connectors". The supported connectors are [listed in the official dex documentation](https://dexidp.io/docs/connectors/) and we can walk you through the setup of any of them.

### Authorization

We utilize Kubernetes-native RBAC to control access to resources in the platform API. Resources are segregated into organizations, each represented by a dedicated namespace, enabling improved access control. This approach allows for fine-grained permissions at both the organization and namespace levels. For more detailed information on this topic, you can refer to our comprehensive [multi-tenancy documentation](https://docs.giantswarm.io/vintage/platform-overview/multi-tenancy/).

## Workload Cluster

### Authentication

For workload cluster - where you run your applications - we do not enforce any specific OpenID Connect (OIDC) tool to enable single sign-on (SSO). However, if you wish to implement SSO for accessing your workload cluster, we provide a detailed guide on how to configure Dex for this purpose, you can follow our comprehensive guide: [Configure OIDC using Dex to access your clusters](https://docs.giantswarm.io/vintage/advanced/access-management/configure-dex-in-your-cluster/).

### Authorization

We provide managed apps and tools designed to simplify and automate RBAC configuration for your workload cluster.

One of the key tools we offer is the [rbac-bootstrap-app](https://github.com/giantswarm/rbac-bootstrap-app). This app allows you to create role bindings on workload cluster directly from the management cluster. This centralized approach simplifies RBAC management across multiple clusters.

When implementing authorization for your workload cluster, consider the following best practices:
- Implement the principle of least privilege: Assign the minimum necessary permissions to users and groups.
- Regularly review and audit permissions to ensure they remain appropriate.
- Use group-based access control where possible for easier management.
- Leverage OIDC integration for enhanced security and simplified user management.

By utilizing these tools and following best practices, you can create a secure, manageable, and flexible authorization system for your workload cluster that meets your organization's specific needs and security requirements.

## We are here to help

At Giant Swarm, we understand that configuring authentication and authorization can be complex, especially when dealing with multiple clusters, diverse organizational structures, and varying security requirements. Don't hesitate to reach out to our support channels. Our goal is to ensure you have a secure, well-configured environment that meets your specific requirements while adhering to best practices in cloud-native security.
