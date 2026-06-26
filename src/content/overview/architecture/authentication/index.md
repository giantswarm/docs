---
title: Authentication
diataxis_content_type: explanation
description: Authentication and authorization mechanisms in the Giant Swarm platform.
weight: 20
menu:
  principal:
    parent: overview-architecture
    identifier: overview-architecture-authentication
user_questions:
  - What are the authentication and authorization mechanisms in the Giant Swarm platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
last_review_date: 2026-06-22
---

During the management cluster installation, Giant Swarm sets up authentication and authorization mechanisms to secure access to the platform. These mechanisms ensure that only authorized users can interact with the platform and its resources.

## Platform API

### Authentication: Platform API

The platform API is a Kubernetes API that operates on the management cluster. To grant access to it, Giant Swarm sets up a [dex](https://github.com/giantswarm/dex-app) instance in the management cluster. This instance comes with **default connectors** that grant our staff access, plus **additional connectors** that you can configure yourself.

Dex acts as a portal to other identity providers (idP) through connectors. The supported connectors are [listed in the official dex documentation](https://dexidp.io/docs/connectors/) and we can walk you through the setup of any of them.

### Authorization: Platform API

We use Kubernetes-native RBAC to control access to resources in the platform API. Resources are segregated into organizations, each represented by a dedicated namespace. This gives you **fine-grained permissions** at both the organization and namespace levels. For more detail, see our [multi-tenancy documentation]({{< relref "/overview/fleet-management/multi-tenancy" >}}).

### Observability

The platform API provides read access to the observability tools, like the Grafana instance running on the management cluster. This lets you browse the data collected in your managed clusters, plus any additional data you choose to push to the platform. For more detail, see our [Grafana organization documentation]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization" >}}).

## Workload cluster

### Authentication: Workload cluster

For the workload cluster—where you run your applications—we don't enforce any specific OpenID Connect (OIDC) tool to enable single sign-on (SSO). However, if you want to implement SSO for your workload cluster, we provide a detailed guide: [Configure OIDC using Dex to access your clusters]({{< relref "/tutorials/access-management/configure-dex-in-your-cluster/" >}}).

### Authorization: Workload cluster

We provide managed apps and tools designed to simplify and automate RBAC configuration for your workload cluster.

One of the key tools we offer is the [`rbac-bootstrap-app`](https://github.com/giantswarm/rbac-bootstrap-app). This app lets you create role bindings on the workload cluster directly from the management cluster. This centralized approach simplifies RBAC management across multiple clusters.

When implementing authorization for your workload cluster, consider the following best practices:

- Implement the principle of least privilege: Assign the minimum necessary permissions to users and groups.
- Frequently review and audit permissions to ensure they remain appropriate.
- Use group-based access control where possible for easier management.
- Use OIDC integration for enhanced security and simplified user management.

Using these tools and following these best practices, you can create a secure, manageable, and flexible authorization system for your workload cluster. It will meet your organization's specific needs and security requirements.

## We're here to help

At Giant Swarm, we understand that configuring authentication and authorization can be complex, especially when dealing with multiple clusters, diverse organizational structures, and varying security requirements. Don't hesitate to reach out to our support channels. We aim to ensure you have a secure, well-configured environment that meets your specific requirements while adhering to best practices in cloud-native security.
