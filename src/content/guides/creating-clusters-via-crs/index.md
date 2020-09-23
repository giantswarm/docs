---
title: Creating tenant clusters via Control Plane Kubernetes API
description: This guide will walk you through the process of tenant cluster creation via Control Plane Kubernetes.
date: 2020-06-19
type: page
weight: 100
tags: ["tutorial"]
---

# Creating tenant clusters via the Control Plane Kubernetes API

This guide will show you how to create tenant clusters by creating and applying custom resources (CRs) directly to the control plane.

Previously you might have used our Rest API to create clusters, however, Giant Swarm is replacing its own REST API for cluster management with the [Control Plane Kubernetes API](/api/#cp-k8s-api)  based on the upstream [Cluster API](https://cluster-api.sigs.k8s.io/).
[The Cluster API](https://cluster-api.sigs.k8s.io/) is a Kubernetes project to bring declarative, Kubernetes-style APIs to cluster creation, configuration, and management. It provides optional, additive functionality on top of core Kubernetes.

Following this strategy, the Giant Swarm Rest API is going to be deprecated at some point. Subscribe to our related [roadmap issue](https://github.com/giantswarm/roadmap/issues/90) to stay informed about the deprecation.

## How does cluster creation work now

- [On AWS](/guides/creating-clusters-via-crs/aws.md).
- [On Azure](/guides/creating-clusters-via-crs/azure.md).
