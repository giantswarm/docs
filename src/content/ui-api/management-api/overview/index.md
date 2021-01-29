---
linkTitle: Overview
title: Management API overview
description: Introduction to the Giant Swarm Management API, the Kubernetes API of the management cluster in your Giant Swarm installation.
weight: 10
---

# The Management API (preview)

## What it is

In a Giant Swarm installation, the management cluster is a Kubernetes cluster that runs all the operational and monitoring workloads which are needed to create and manage the _workload clusters_ (formerly called _tenant clusters_). These are the clusters you create to run your actual workloads.

Your workload clusters and other associated resources are represented in the management cluster as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). To access these, you can use the Kubernetes API of the management cluster, or in short, the Management API.

## How to gain access

Access to the Giant Swarm Control Plane API is secured using OIDC. Please contact your Solution Engineer (SE) to sort out the details.

Currently we provide read-only access by default. As we are currently working on a fine-grained way to control permissions to resources, and validation and defaulting are not implemented to the extend we want to, having write access right now means fully unrestricted access and should only be granted to select individuals.

## How to use

We recommend using `kubectl` to navigate the resources present on the Management API.

To facilitate this we provide a kubectl plugin called [`kubectl gs`](/reference/kubectl-gs/).
Our goal is to have the same great user experience you've become accustomed from `gsctl` and `happa`.

Besides general Kubernetes know-how this will require only a bit of structural knowledge:

### How we organize resources in namespaces

We create one namespace for each workload cluster, where the namespace name is equal to the workload cluster ID. All cluster specific resources reside in the namespace of that workload cluster.

### Which custom resources are used for what purpose

Following are some resources that should help you:

- The guide [Creating workload clusters via the Management API](/guides/creating-clusters-via-crs/) explains step by step how you can create a cluster and node pools via the Management API. Here you learn about all the custom resources a cluster comprises.
- The [App Platform](/basics/app-platform/) introduction outlines the several custom resources involved when managing app catalogs and apps.
- Our [Management API reference](/reference/management-api/) provides detailed documentation on all the custom resources we use with the various providers and their versions and schema.

## Feedback is welcome

We are keen to learn from you about your experience with using the Management API, with navigating the custom resources via the API, with our reference documentation and the user guides we provide. This helps us provide more and better material and improve to make the journey more seamless, more satisfactory for you.

So please, don't hesitate to give your feedback in your Slack channel.
