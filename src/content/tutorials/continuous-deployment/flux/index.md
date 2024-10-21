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
aliases:
  - /advanced/gitops/flux
  - /advanced/fluxcd/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-10-21
---

The [FluxCD](https://fluxcd.io), called just `Flux` too, website states:
> Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible.

What it's from a developer perspective is a set of operators and custom resources designed to apply GitOps in a Kubernetes environment. The operators, configured with the custom resources, will be watching Git repositories, Helm repositories, or even S3 buckets and reconciling their contents with the state of the cluster to make sure they both match.

To get started with `Flux`, you will need to bootstrap `Flux` to your cluster of choice and create at least one of each of the following:

1. `source.toolkit.fluxcd.io` resources - they tell the `source-controller` where to look for the manifests
2. `helmrelease.helm.toolkit.fluxcd.io` or `kustomization.kustomize.toolkit.fluxcd.io` resources - they're meant for `helm-controller` and `kustomize-controller` respectively and govern how the manifests found in sources will be applied

Luckily, `Flux` is bootstrapped and running in Giant Swarm management clusters, so you can start using it immediately.

If want to learn more about `Flux` and its capabilities, here are a couple of useful links:

- [`Flux` documentation homepage](https://fluxcd.io/docs/).
- [Get Started with `Flux`](https://fluxcd.io/docs/get-started/) is a great way to get familiar with Flux on a test cluster or even a [Kind](https://kind.sigs.k8s.io/) cluster.
- [GitOps Toolkit components](https://fluxcd.io/docs/components/) is where you can browse Flux Custom Resources and their use cases.
