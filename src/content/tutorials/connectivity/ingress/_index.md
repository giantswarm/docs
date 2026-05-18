---
title: Ingress connectivity (deprecated)
linkTitle: Ingress (deprecated)
description: Ingress Nginx is deprecated. Use Gateway API with Envoy Gateway instead.
weight: 40
aliases:
  - /getting-started/connectivity/ingress-controller
  - /vintage/getting-started/connectivity/ingress-controller
  - /advanced/connectivity/ingress
last_review_date: 2026-05-18
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I expose my workloads to the internet using an ingress?
---

{{% notice warning %}}
**Deprecated:** Giant Swarm no longer offers Ingress Nginx as a managed solution. It has been replaced by [Gateway API with Envoy Gateway]({{< relref "/tutorials/connectivity/gateway-api/" >}}). If you're still running ingress-nginx, follow the [migration guide]({{< relref "/tutorials/connectivity/gateway-api/ingress-nginx-migration/" >}}) to transition your workloads.
{{% /notice %}}

The pages in this section are kept for reference while you migrate existing workloads. They describe ingress-nginx features and configuration that are no longer actively supported.

## Archived pages

- [Exposing workloads]({{< relref "/tutorials/connectivity/ingress/exposing-workloads/" >}}): basic ingress setup and port forwarding
- [Advanced ingress configuration]({{< relref "/tutorials/connectivity/ingress/configuration/" >}}): annotations, TLS, auth, rate limiting, ModSecurity
- [Running multiple ingress-nginx controllers]({{< relref "/tutorials/connectivity/ingress/multi-nginx-ic/" >}}): separating internal and external traffic
- [Services of type LoadBalancer]({{< relref "/tutorials/connectivity/ingress/service-type-loadbalancer/" >}}): direct cloud load balancer exposure on AWS and Azure
