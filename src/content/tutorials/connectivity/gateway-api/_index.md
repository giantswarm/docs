---
linkTitle: Gateway API
title: Gateway API
description: Learn how to use the Kubernetes Gateway API with Envoy Gateway in Giant Swarm workload clusters for advanced traffic management, load balancing, and API gateway functionality.
weight: 25
menu:
  principal:
    parent: tutorials-connectivity
    identifier: tutorials-connectivity-gateway-api
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I set up Gateway API in my Giant Swarm cluster?
  - What is the difference between Gateway API and Ingress?
  - How do I configure Envoy Gateway for my workloads?
  - What are the Gateway API components and how do they work together?
last_review_date: 2025-10-17
---

The Kubernetes Gateway API is the next-generation standard for managing ingress traffic in Kubernetes clusters. It provides a more expressive, extensible, and role-oriented approach to traffic management compared to traditional Ingress resources. Giant Swarm supports Gateway API through Envoy Gateway, providing advanced load balancing, traffic routing, and API gateway capabilities.

This guide explains how to set up and use Gateway API with Envoy Gateway in Giant Swarm workload clusters.

## Overview

Gateway API introduces several key concepts that provide more flexibility and control over traffic management:

### Gateway API vs. Ingress

| Feature | Ingress | Gateway API |
|---------|---------|-------------|
| **Role separation** | Single resource | Separate resources for infrastructure (Gateway) and routing (HTTPRoute) |
| **Protocol support** | HTTP/HTTPS only | HTTP/HTTPS, TCP, UDP, TLS |
| **Extensibility** | Limited | Highly extensible with custom resources |
| **Traffic policies** | Basic | Advanced (retries, timeouts, load balancing) |
| **Multi-tenancy** | Limited | Built-in role-based access control |

### Key Components

The Gateway API consists of three main components available in Giant Swarm:

1. **[Gateway API CRDs](https://github.com/giantswarm/gateway-api-crds-app)**: Core custom resource definitions for Gateway API
2. **[Envoy Gateway](https://github.com/giantswarm/envoy-gateway-app)**: The gateway implementation based on Envoy Proxy
3. **[Gateway API Config](https://github.com/giantswarm/gateway-api-config-app)**: Default configuration for quick setup

Those are bundle together in [Gateway API bundle](https://github.com/giantswarm/gateway-api-bundle/tree/main/helm/gateway-api-bundle) to help with the installation.

### Gateway API resources

- **GatewayClass**: Defines the type of gateway (managed by platform team)
- **Gateway**: Configures load balancer and listeners (managed by platform team)
- **HTTPRoute**: Defines HTTP routing rules (managed by application teams)
- **TCPRoute/UDPRoute**: Defines TCP/UDP routing rules
- **ReferenceGrant**: Enables cross-namespace references

## Next steps

Now that you understand the basics of Gateway API, you can:

- [Install Gateway API](installation/) in your Giant Swarm cluster
- [Learn how to use Gateway API](usage/) for routing and traffic management

## Limitations

- Gateway API is still evolving; some features may be experimental
- Not all Ingress controller features have direct Gateway API equivalents
- Some advanced Envoy features may require custom EnvoyProxy configuration

## Further reading

- [Kubernetes Gateway API documentation](https://gateway-api.sigs.k8s.io/)
- [Kubernetes Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/)
- [Envoy Gateway documentation](https://gateway.envoyproxy.io/)
- [Gateway API CRDs app repository](https://github.com/giantswarm/gateway-api-crds-app)
- [Envoy Gateway app repository](https://github.com/giantswarm/envoy-gateway-app)
- [Gateway API Config app repository](https://github.com/giantswarm/gateway-api-config-app)
