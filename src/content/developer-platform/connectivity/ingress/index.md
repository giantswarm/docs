---
linkTitle: Ingress
title: nginx Ingress Controller
description: An overview of how and what Giant Swarm offers with the nginx Ingress Controller.
weight: 10
menu:
  main:
    parent: developer-platform-connectivity
user_questions:
  - How do I do Ingress?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2022-11-14
---

For ingress we offer a fully managed nginx ingress controller. You can use any other ingress controller within the platform but the nginx ingress controller comes managed with 24/7 support by Giant Swarm.

A few resources to learn more about the nginx ingress controller:

- [Installing an ingress controller]({{< relref "/getting-started/ingress-controller" >}})
- [Exposing pods and services to the outside]({{< relref "/getting-started/exposing-workloads" >}})
- [Advanced Ingress Configuration]({{< relref "/advanced/ingress" >}})
- [TLS Certificates for Ingress with cert-manager]({{< relref "/advanced/tls-certificates" >}})
- [The nginx-ingress-controller helm chart on Github](https://github.com/giantswarm/nginx-ingress-controller-app)
