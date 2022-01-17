---
linkTitle: Overview
title: Introduction to the Giant Swarm offering
description: A broad overview of everything you get from Giant Swarm, including links to detailed documentation on specific topics.
weight: 10
menu:
  main:
    identifier: general-overview
    parent: general
last_review_date: 2021-12-26
user_questions:
  - What's included with Kubernetes run by Giant Swarm?
  - What's not included with Kubernetes run by Giant Swarm?
aliases:
  - /basics/kubernetes-on-giant-swarm/
owner:
  - https://github.com/orgs/giantswarm/teams/team-horizon
---

# Running Kubernetes on Giant Swarm

At Giant Swarm we enable platform teams to move from administartion to innovation. We achieve this by providing you with fully-managed Kubernetes clusters, which you can then use to deploy your containers as you see fit. You have full admin rights to your clusters through their API, so you can change anything that is accessible through the Kubernetes API. Changes that require configuration of the Kubernetes components themselves (e.g. starting the API server or kubelets with specific arguments) need to be set by the Giant Swarm Ops team. If you have specific needs or feedback, don't hesitate to [get in touch](mailto:support@giantswarm.io).

This model aligns with the value we see in providing Open-Source-as-a-Service. Our goal is to encourage experimentation in a safe environment. In this environmenet you can innovate while we provide advice, guardrails and connections to upstream. You reap the benefits of going cloud native easily and quickly by side stepping some of the work of introducing or scaling Kubernetes in your organization.



## What is included

We provide support for [AWS]({{< relref "/general/architecture/aws" >}}), [Azure]({{< relref "/general/architecture/azure" >}}) and [on-premises]({{< relref "/general/architecture/on-premises" >}}) clusters. With the adoption of [Cluster API](https://www.giantswarm.io/blog/its-cluster-api-time-are-you-ready-giant-swarm), our customers will benefit from a growing number of supported clouds.

Your Giant Swarm installation comes out-of-the-box as follows:

- A [management cluster]({{< relref "/general/management-clusters" >}}) in a specific cloud region or data center which will manage the workload clusters in the same region.
- Any number of workload clusters according to your needs. (Capacity restrictions apply regarding availability of IPv4 addresses, (virtual) machine availability in the data center.)
- Workload clusters with [high-availability Kubernetes control planes]({{< relref "/advanced/high-availability/control-plane" >}}) with clustered etcd (available on AWS only currently) or single node control plane with resilient etcd.
- Full end-to-end encryption between Kubernetes components with regular rolling of keys/certificates.
- CNI networking (native plug-ins on AWS and Azure) installed and Calico for network policy enforcement. TODO: which providers is this true for?
- CoreDNS installed
- All resources and feature gates (incl. alpha) enabled
- [NGINX Ingress Controller]({{< relref "/getting-started/ingress-controller" >}}) - running inside your cluster (optional app)
- Monitoring
- [Storage]({{< relref "/advanced/storage" >}})

As a user of Giant Swarm you can utilize any of our four front ends: [API]({{< relref "/ui-api/management-api/overview" >}}), [CLI]({{< relref "/ui-api/kubectl-gs" >}}), [Web UI]({{< relref "/ui-api/web/overview" >}}) and [GitOps]({{< relref "/advanced/gitops" >}})

## Management and support

Rooted in the DevOps way of thinking, we run what we build. Thus, you get a managed service with 24/7 support. What does this actually mean for you?

It can be broken down into a three step process:

1. We develop the platform
We provide upgrades, security patches (CVEs) for all components involved. BUT we also build a platform to manage multiple clusters. Upgrades are fully automated. The platform is resilient due to the operator pattern we are using. The platform scales automatically. And we constantly add new cluster orchestration features, new managed apps and app deployment/management features in the app platform.
2. We operate the platform
We take the pager on the infrastructure. This includes the cloud resources as well as the kubernetes stack and the managed apps on top. So if something goes wrong we automatically get notified and start acting. We provide RCAs and do post mortems to prevent the same problem from happening again. Customers also alert us, when they discover issues. 
3. We consult on how to use the platform
Weekly calls with an Account Engineer. Easy access to knowledge via the shared slack channel. We share experience from other customers and how they solved their problems. We have a lot of experience building a cloud-native stack for enterprises. We speak the language of different departments of an organization (e.g. security, infrastructure and operations, DevOps). We bring experience of building setups over multiple locations.

## What is not included

There are some things not included in the cluster managed by us:

- Additional user-space services like dashboards, logging, container registry, etc. are not installed (getting them running is [really easy]({{< relref "/app-platform/overview" >}}), though).

