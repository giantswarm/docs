---
linkTitle: Ingress
title: Ingress NGINX Controller
description: An overview of how and what Giant Swarm offers with the Ingress NGINX Controller.
weight: 10
menu:
  main:
    parent: platform-overview-connectivity
aliases:
  - /developer-platform/connectivity/ingress
user_questions:
  - How do I do Ingress?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2022-11-14
---

For ingress we offer a fully managed Ingress NGINX Controller. You can use any other ingress controller within the platform but the Ingress NGINX Controller comes managed with 24/7 support by Giant Swarm.

A few resources to learn more about the Ingress NGINX Controller:

- [Installing an ingress controller]({{< relref "/getting-started/ingress-controller" >}})
- [Exposing pods and services to the outside]({{< relref "/getting-started/exposing-workloads" >}})
- [Advanced Ingress Configuration]({{< relref "/advanced/ingress" >}})
- [TLS Certificates for Ingress with cert-manager]({{< relref "/advanced/tls-certificates" >}})
- [The Ingress NGINX Controller Helm chart on Github](https://github.com/giantswarm/ingress-nginx-app)
