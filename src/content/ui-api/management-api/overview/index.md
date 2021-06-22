---
linkTitle: Overview
title: Management API overview
description: Introduction to the Giant Swarm Management API, the Kubernetes API of the management cluster in your Giant Swarm installation.
weight: 10
menu:
  main:
    identifier: uiapi-managementapi-overview
    parent: uiapi-managementapi
user_questions:
  - What is the Management API?
  - In what development stage is the Management API?
last_review_date: 2021-05-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-biscuit
---

# The Management API (preview)

## What it is

In a Giant Swarm installation, the [management cluster]({{< relref "/general/management-clusters/index.md" >}}) is a Kubernetes cluster that runs all the operational and monitoring workloads which are needed to create and manage the _workload clusters_ (formerly called _tenant clusters_). These are the clusters you create to run your actual workloads.

Your workload clusters and other associated resources are represented in the management cluster as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). To access these, you can use the Kubernetes API of the management cluster, or in short, the Management API.

## How to gain access

Access to the Giant Swarm Control Plane API is secured using OIDC. Our [authentication]({{< relref "/ui-api/management-api/authentication" >}}) section provides additional information both for admins and end users. Please contact your Account Engineer to sort out the details.

Currently we provide read-only access by default. As we are currently working on a fine-grained way to control permissions to resources, and validation and defaulting are not implemented to the extend we want to, having write access right now means fully unrestricted access and should only be granted to select individuals.

## How to use

Currently (as of May 2021) we are in the process of enabling our [web user interface]({{< relref "/ui-api/web" >}}) to interact with the Management API.

For now we recommend using `kubectl` to interact with the Management API. To facilitate this we provide a kubectl plug-in called [`kubectl gs`]({{< relref "/ui-api/kubectl-gs" >}}).

Besides general Kubernetes know-how this will require only a bit of structural knowledge:

### How we organize resources in namespaces

We are working towards making [organization namespaces]({{< relref "/general/organizations/index.md" >}}) the default location for all resources associated with one organization. However, so far we haven't reached this goal yet. Please check [this dedicated section]({{< relref "/general/organizations/index.md" >}}#namespace-use) regarding the current state on various providers.

### Which custom resources are used for what purpose

Following are some resources that should help you:

- The guide [Creating workload clusters via the Management API]({{< relref "/ui-api/management-api/creating-workload-clusters" >}}) explains step by step how you can create a cluster and node pools via the Management API. Here you learn about all the custom resources a cluster comprises.
- The [App Platform]({{< relref "/app-platform" >}}) introduction outlines the several custom resources involved when managing app catalogs and apps.
- Our [custom resource definitions (CRD) documentation]({{< relref "/ui-api/management-api/crd" >}}) provides details on all the custom resources (CR) we use with the various providers and their versions and schema.

## Feedback is welcome

We are keen to learn from you about your experience with using the Management API, with navigating the custom resources via the API, with our reference documentation and the user guides we provide. This helps us provide more and better material and improve to make the journey more seamless, more satisfactory for you.

So please, don't hesitate to give your feedback in your Slack channel.
