---
linkTitle: FluxCD
title: What is FluxCD
description: An explanation of the GitOps principles and a guide to managing Giant Swarm platform resources with FluxCD.
weight: 30
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-flux
user_questions:
  - What is FluxCD?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-07
---

The [`FluxCD`](https://fluxcd.io) project, called often just `Flux`, is a set of continuous and progressive delivery solutions for `Kubernetes` that are open and extensible.

From a developer perspective is a set of operators and custom resources designed to implement GitOps in a `Kubernetes` environment. The operators watch `Git` repositories, `Helm` repositories, or even `S3` buckets, reconciling the contents with the state of the cluster to make sure they both match.

To get started with `Flux`, you need to bootstrap `Flux` in your cluster and create at least one of each of the following:

1. A `source.toolkit.fluxcd.io` resource. It's a custom resource that defines where `Flux` should look for the manifests to apply. It can be a `Git` repository, a `Helm` repository, or an `S3` bucket.
2. A `helm.toolkit.fluxcd.io` or `kustomize.toolkit.fluxcd.io` resource. It's a custom resource that defines how `Flux` should apply the manifests. It can be a `Helm` chart or a `Kustomize` overlay.

Luckily, `Flux` is bootstrapped and running in Giant Swarm management clusters, so you can start using it immediately. Browse the [template configuration]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters" >}}) to understand how to set up your environment.

If want to learn more about `Flux` and its capabilities, here are some useful links to read:

- [`Flux` documentation homepage](https://fluxcd.io/docs/).
- [Get started with `Flux`](https://fluxcd.io/docs/get-started/) is a great way to get familiar with `Flux` on a test cluster or even a [`Kind`](https://kind.sigs.k8s.io/) cluster.
- [GitOps toolkit components](https://fluxcd.io/docs/components/) is where you can browse `Flux` custom resources and their use cases.

Learn [`what's a base template`]({{< relref "/tutorials/continuous-deployment/bases/"}}).
