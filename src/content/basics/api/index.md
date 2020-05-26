---
title: API Access to Giant Swarm Resources
description: An overview of the APIs that provide you with programmatic access to
  resources like your tenant cluster in a Giant Swarm installation. Namely the Rest
  API and the Control Plane Kubernetes API.
date: 2020-05-26
weight: 75
type: page
categories: ["basics"]
last-review-date:
---

# API Access to Giant Swarm Resources

For integrating Giant Swarm with your automation, we provide programmatic access via two different APIs:

- [The Rest API](#rest-api): stable and recommended for production use.

- [The Control Plane Kubernetes API](#cp-k8s-api): our next generation API, currently in a preview phase.

In the following sections we explain the differences and specific benefits and provide some guidance on how to get started.

## The Rest API {#rest-api}

The Rest API is an abstraction over the many resources that reside in the Control Plane of a Giant Swarm installation. It is used by our dedicated user interfaces, the web User Interface and gsctl.

Browse our [API documentation](/api/) for a complete overview into the provided functionality.

The Rest API was originally designed to provide a simpler, easier access to the relevant resources for managing clusters, key pairs, etc. while keeping the internals under the hood. However at Giant Swarm we learnt that there are always more use cases emerging on your side than we could anticipate in our API design. We realized that the best we can do for you to provide full insight into the state and spec of your infrastructure is by opening up the underlying system itself.

With this realization, we made the decision to phase out the development of the Rest API in favor of providing access to the [Control Plane Kubernetes API](#cp-k8s-api) instead.

As of now, there is no termination date for the Rest API. As it might provide the much simpler and more accessible starting point, feel free to explore the [documentation](/api/), knowing that one day you may have to switch to the Control Plane Kubernetes API.

## The Control Plane Kubernetes API (CP-K8s-API) {#cp-k8s-api}

## What it is

At Giant Swarm, when we say "control plane", we talk about the Kubernetes Cluster that runs all the operational and monitoring workloads which are needed to create and manage the "tenant clusters". These are the clusters you create to run your actual workloads. This is not to be confused with how the Kubernetes project uses the same term. In that case, it simply refers to the master nodes of a Kubernetes cluster.

The control plane is a Kubernetes cluster. Your tenant clusters and other associated resources are represented in that cluster as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). To access these, you can use the Kubernetes API of the cluster that forms the control plane, or in short, the Control Plane Kubernetes API.

### How to gain access

Access to the Giant Swarm Control Plane API is secured using OIDC. Please contact your Solution Engineer (SE) to sort out the details.

Currently we provide read-only access by default. As we are currently working on a fine-grained way to control permissions to resources, and validation and defaulting are not implemented to the extend we want to, having write access right now means fully unrestricted access and should only be granted to select individuals.

### How to use

We recommend using `kubectl` to navigate the resources present on the Control Plane Kubernetes API. Besides general Kubernetes know-how this will require only a bit of structural knowledge:

#### How we organize resources in namespaces

We create one namespace for each tenant cluster, where the namespace name is equal to the tenant cluster ID. All cluster specific resources reside in the namespace of that tenant cluster.

### Which custom resources are used for what purpose

Following are some resources that should help you:

- The guide [Creating tenant clusters via the Control Plane Kubernetes API](/guides/creating-clusters-via-crs-on-aws/) explains step by step how you can create a cluster and node pools via the Control Plane Kubernetes API. Here you learn about all the custom resources a cluster comprises.
- The [App Platform](/basics/app-platform/) introduction outlines the several custom resources involved when managing app catalogs and apps.
- Our [Control Plane Kubernetes API Reference](https://docs.giantswarm.io/reference/cp-k8s-api/) provides detailed documentation on all the custom resources we use with the various providers and their versions and schema.

### Feedback is welcome

We are keen to learn from you about your experience with accessing the Control Plane Kubernetes API, with navigating the custom resources via the API, with our reference documentation and the user guides we provide. This helps us provide more and better material and improve to make the journey more seamless, more satisfactory for you.

So please, don't hesitate to give your feedback in your Slack channel.
