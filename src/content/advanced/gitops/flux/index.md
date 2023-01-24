---
linkTitle: What is FluxCD
title: What is FluxCD
description: An explanation of the GitOps principles and a guide to managing Giant Swarm platform resources with FluxCD.
weight: 30
menu:
  main:
    parent: advanced-gitops
    identifier: advanced-gitops-flux
user_questions:
  - What is FluxCD?
aliases:
  - /advanced/fluxcd/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2022-12-20
---

## What is FluxCD

The [FluxCD](https://fluxcd.io) website states:
> Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible.

What it is from a developer perspective is a set of operators and Custom Resources designed to apply GitOps in a Kubernetes environment. The operators, configured with the Custom Resources, will be watching Git repositories, Helm repositories, or even S3 buckets and reconciling their contents with the state of the cluster to make sure they both match.

To get started with FluxCD, you will need to bootstrap FluxCD to your cluster of choice and create at least one of each of the following:

1. `source.toolkit.fluxcd.io` resources - they tell the `source-controller` where to look for the manifests
2. `helmrelease.helm.toolkit.fluxcd.io` or `kustomization.kustomize.toolkit.fluxcd.io` resources - they are meant for `helm-controller` and `kustomize-controller` respectively and govern how the manifests found in sources will be applied

Luckily, FluxCD is bootstrapped and running in Giant Swarm management clusters, so you can start using it immediately.

If want to learn more about FluxCD and its capabilities, here are a couple of useful links:

- [FluxCD documentation homepage](https://fluxcd.io/docs/)
- [Get Started with Flux](https://fluxcd.io/docs/get-started/) is a great way to get familiar with Flux on a test cluster or even a [Kind](https://kind.sigs.k8s.io/) cluster
- [GitOps Toolkit components](https://fluxcd.io/docs/components/) is where you can browse Flux Custom Resources and their use cases.
