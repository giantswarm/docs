---
linkTitle: Organizations
title: Organizations
description: Explaining the organization concept in the Giant Swarm Management API, how to use organizations currently, and our future plans to make use of them.
last_review_date: 2021-05-07
weight: 40
menu:
  main:
    parent: general
user_questions:
  - What is an organization?
  - Do I have to use organizations?
  - What's the benefit of using organizations?
owner:
  - https://github.com/orgs/giantswarm/teams/biscuit
---

# Organizations

<div class="well disclaimer">

<i class="fa fa-warning"></i> This article covers organizations as defined in the [Management API]({{< relref "/ui-api/management-api/_index.md" >}}). These are replacing the organizations as used with the [REST API]({{< relref "/ui-api/rest-api/index.md">}}). Please make sure you read the details about this transition carefully, especially the [roadmap](#roadmap) section, to understand the ramifications for you and your end users.

<!-- TODO: link article about changes and migration -->

</div>

## Introduction

Organizations are a way to manage resources like clusters and apps in a way that different entities are isolated from each other. You can use organizations to separate projects, business units, teams etc.

Clusters are _owned_ by organizations. So in order to be able to manage a cluster (on the Management API level, not on the individual cluster level), access to the organization owning the cluster is required.

The organization concept makes use of some well-known building blocks of Kubernetes in the [management cluster]({{< relref "/general/management-clusters/index.md" >}}), such as:

- Namespaces
- Role based access control (RBAC)
- Specific custom resources (CRs) that tie things together and make organizations easy to manage
- Operators which automate some management tasks

Typical use cases for organizations are:

- Separating clusters for development, experimentation, and testing from clusters used for staging and for production purposes.

- Isolating teams, business units, or even legal entities.

At Giant Swarm, for example, we run several shared installations where we allow different customers access to a single organization only, usually before they get their own installation. This way we can ensure that each customer, while using the same management cluster, can only access their own clusters and other resources.

### Visual overview {#intro-visual}

[![Organizations in the Management API, visualized](organizations-management-api.svg)](organizations-management-api.svg)

<!-- Source for above image: -->

## Current state and roadmap {#roadmap}

Organizations are transitioning from being managed completely by microservices behind our REST API to becoming entities you can manage fully via the Management API. In this section we disect where we are coming from, where we are heading, and what the current situation is on the different providers.

### 2016 to present: REST API

- Our REST API provides [functions to manage organizations](https://docs.giantswarm.io/api/#tag/organizations).
- Each workload cluster is owned by an organization.
- Customers assign users with proprietary Giant Swarm user accounts to organizations as members, in which they have full permissions.

### 2019: introduction of the Management API

- In order to give customers full access to management clusters, workload cluster and app resources, we provide experimental access to the Kubernetes API of management clusters, which we now call the Management API. (We used to call it the _Control Plane API_ back then.)
- For authentication we introduce OpenID Connect (OIDC), using the customer's own identity provider. We decide to abandon the proprietary Giant Swarm user account, used for the REST API, in the long run.
- In the beginning, the concept of the organization does not exist in the Management API.
- Cluster resources carry an annotation `giantswarm.io/organization` to indicate which organization they are assigned to via the REST API.

### 2020: introduction of the organization concept in the Management API

- With the [Organization CRD]({{< relref "/ui-api/management-api/crd/organizations.security.giantswarm.io.md" >}}) we introduce an entity in the Management API to represent an organization.
- Operators ensure that a namespace exists for each organization in the management cluster.
- Starting with workload cluster release v13.0.0 for Azure, cluster resources are created in the owner organization's namespace.

### Further plans

- We are migrating our [web user interface]({{< relref "/ui-api/web" >}}) from using the REST API to the Management API. This also brings a switch from proprietary Giant Swarm user accounts to single sign-on (SSO). Once this switch is effective for you, you will be using the same identity provider and identities for authentication in the web UI that you use with the Management API. With the web user interface no longer relying on the REST API, the REST API will be decommissioned.
- All resources related to workload clusters and apps should reside in the owner organization's namespace. See [roadmap#103](https://github.com/giantswarm/roadmap/issues/103) for details. As a next step, this will be implemented for AWS workload clusters. On-premises/KVM will follow. For details regarding the state on the different providers, see [namespace use in different providers](#namespace-use) further down.
- Once the web user interface only relies on the Management API as a backend, we will start supporting a variety of different user permissions. For example, based on RBAC it will be possible to admit users who have read permissions only. The web user interface will adapt to these restricted permissions and provide a good user experience, regardless of the permissions a user has. This will allow you to permit more users access to the web UI, using identities (user groups and individuals) from your own identity provider, authenticating via single-sign-on.

## Organization CRD and CRs {#organization-crd-cr}

If the concept of custom resources (CR) and custom resource definitions (CRD) is new to you: Kubernetes allows to define [arbitrary objects](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to be handled via the Kubernetes API. The schema of such an object is specified by a custom resource definition. The actual objects are called the custom resources.

Giant Swarm management clusters provide a CRD named `Organization` (long form: `organizations.security.giantswarm.io`). An organization is defined simply by a custom resource using that CRD, which we'll call an "organization CR" here for brevity.

> An organization is defined by an organization CR.

Our CRD schema documentation provides details about the [Organization CRD]({{< relref "/ui-api/management-api/crd/organizations.security.giantswarm.io.md" >}}). But before you raise your eyebrows in disappointment, be warned: there isn't much to document. The single most important aspect of an organization CR is it's name. But there is more to it, of course.

Once an organization CR is created, our operator ([organization-operator](https://github.com/giantswarm/organization-operator), to be precise) ensures that a namespace exists for the organization. More about that [in a minute](#namespace).

## Naming conventions {#naming-conventions}

Organization names (technically: organization CR names) must follow these rules:

- Must be unique within the management cluster
- Must contain at most 59 characters.
- Has to conform the same convention as Kubernetes namespaces additionally (i. e. the [DNS label names convention](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names)), which means:
    - contain only lowercase alphanumeric characters or '-'
    - start with an alphanumeric character
    - end with an alphanumeric character

Since there will be a namespace created for each org, prefixed with `org-`, we recommend against using that same prefix in the organization name, to avoid confusion.

## Organization namespace {#namespace}

For each organization there is a namespace in the management cluster. The namespace is named after the organization CR name, prefixed with `org-`.

For example, for an organization `acme`, there is the defining organization CR named `acme`. In addition, organization-operator ensures the existence of the namespace `org-acme` in the management cluster.

We recommend to place all resources belonging to an organization into the organization's namespace. Our user interfaces will work towards supporting this as a default.

### Namespace use in different providers {#namespace-use}

Giant Swarm is currently working towards making the organization's namespace the default namespace for all resources owned by the organization: clusters, node pools, apps, and more. We have (as of May 2021) reached different stages on different providers.

#### Azure {#namespace-use-azure}

With the latest workload cluster releases for Azure (as of April 2021 that is v14.1.x), all cluster and node pool resources are placed in the organization namespace by default.

Resources belonging to apps deployed to workload clusters are not yet placed in the organization namespace.

#### AWS {#namespace-use-aws}

With the latest AWS releases (as of April 2021 that's v14.1.x), the organization namespace is not yet used by default.

#### On-premises (KVM) {#namespace-use-onprem}

With the latest KVM releases (as of April 2021 that's v13.1.x), the organization namespace is not yet used by default.

## Managing organizations

Organizations can be managed in several ways.

- The [web user interface]({{< relref "/ui-api/web/_index.md" >}}) allows to create and delete organizations interactively. The web user interface leverages the [Management API]({{< relref "/ui-api/management-api/_index.md" >}}).
- The [Management API]({{< relref "/ui-api/management-api/_index.md" >}}) provides full, native support for managing all organization-related resources.

In addition, we plan to enhance the `kubectl` user experience for organization management via our [`gs`]({{< relref "/ui-api/kubectl-gs/_index.md" >}}) plug-in.

<!-- TODO: set links to more organization-specific sub sections once they are published -->

## Migrating from the REST API {#migration-from-rest-api}

Giant Swarm migrates all organizations from the REST API era into the Management API to ensure a smooth transition for customers.

In some cases, renaming an organization is necessary, where the original organization used characters that are not supported any more (uppercase letters and underscores). In this case, Giant Swarm Account Engineers will reach out to their customer contacts to agree on the new organization names.

More information will follow once this migration starts.

<!-- TODO: link specific page "Migration of organizations from REST API to MAPI" once published -->
