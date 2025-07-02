---
title: Multi-tenancy
description: The Organization concept in the Giant Swarm Management API helps keep resources for different tenants separate.
last_review_date: 2023-08-02
aliases:
  - /platform-overview/multi-tenancy
  - /platform-overview/organizations/
weight: 50
menu:
  main:
    parent: platform-overview
user_questions:
  - What is an organization?
  - Do I have to use organizations?
  - What's the benefit of using organizations?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

## Introduction

_Organizations_ are a means to organize resources like clusters and apps in a way that different entities are isolated from each other. You can use organizations to separate resources for different projects, business units, teams, etc., within the same Giant Swarm management cluster.

The organization concept makes use of some well-known building blocks of Kubernetes in the Management API, such as:

- Namespaces
- Role based access control (RBAC)
- Specific custom resources (CRs) that tie things together and make organizations easy to manage
- Operators which automate some management tasks

Typical use cases for organizations are:

- Separating clusters for development, experimentation, and testing from clusters used for staging and for production purposes.

- Isolating teams, business units, or even legal entities.

At Giant Swarm, for example, we run several shared installations where we allow different customers access to a single organization only, usually before they get their own installation. This way we can ensure that each customer, while using the same management cluster, can only access their own workload clusters and resources.

### Visual overview {#intro-visual}

[![Organizations in the Management API, visualized](organizations-management-api.svg)](organizations-management-api.svg)

<!-- Source for above image: https://docs.google.com/drawings/d/1PDve3HoE7br_6npe0RSCw8ddt-H7pFztPlSDiQbNabs/edit -->

## Organization CRD and CRs {#organization-crd-cr}

If the concept of custom resources (CR) and custom resource definitions (CRD) is new to you: Kubernetes allows to define [arbitrary objects](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to be handled via the Kubernetes API. The schema of such an object is specified by a custom resource definition. The actual objects are called the custom resources.

Giant Swarm management clusters provide a CRD named `Organization` (long form: `organizations.security.giantswarm.io`, [schema documentation]({{< relref "/reference/platform-api/crd/organizations.security.giantswarm.io.md" >}})). An organization is defined simply by a custom resource using that CRD, which we'll call an "organization CR" here for brevity.

The single most important aspect of an organization CR is its name. Therefore the CR looks as simple as this:

```text
$ kubectl gs template organization --name ecommerce
apiVersion: security.giantswarm.io/v1alpha1
kind: Organization
metadata:
  name: ecommerce
# [...]
```

Once an organization CR is created, our automation ([organization-operator](https://github.com/giantswarm/organization-operator), to be precise) ensures that a namespace `org-<name of organization>` exists for the organization.

## Naming conventions {#naming-conventions}

Organization names (technically: organization CR names) must follow these rules:

- Must be unique within the management cluster
- Must contain at most 59 characters.
- Has to conform the same convention as Kubernetes namespaces additionally (i. e. the [DNS label names convention](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names)), which means:
    - contain only lowercase alphanumeric characters or '-'
    - start with an alphanumeric character
    - end with an alphanumeric character

Since there will be a namespace created for each organization, prefixed with `org-`, we recommend against using that same prefix in the organization name, to avoid confusion.

## Organization namespace {#namespace}

For each organization there is a namespace created in the management cluster. The namespace is named after the organization CR name, prefixed with `org-`.

For example, for an organization `acme`, there is the defining organization CR named `acme`. In addition, organization-operator ensures the existence of the namespace `org-acme` in the management cluster.

We recommend to place all resources belonging to an organization into the organization's namespace. Our user interfaces and admission controllers are moving towards supporting this as a default.

### Namespace utilization in different providers {#namespace-use}

We default to storing all resources of an organization in its organization `org-*` namespace: clusters, node pools, apps, and more.

Vintage implementations still have a historical difference: resources belonging to apps deployed to workload clusters are not yet placed in the organization namespace. Instead they are placed in a namespace named after the workload cluster ID. For example, if a workload cluster is named `ve5v6`, the namespace `ve5v6` would contain the `App` CRs for that cluster. Resources are not automatically moved to the organization namespace.

## Managing organizations

Organizations can be managed in several ways.

- The [web user interface]({{< relref "/vintage/platform-overview/web-interface/organizations/_index.md" >}}) allows creating and deleting organizations interactively.

- The [Management API]({{< relref "/vintage/use-the-api/management-api/_index.md" >}}) provides full, native support for managing all organization-related resources.

In addition, we plan to enhance the `kubectl` user experience for organization management via our [`gs`]({{< relref "/reference/kubectl-gs/_index.md" >}}) plug-in.

<!-- TODO: set links to more organization-specific sub sections once they are published -->
