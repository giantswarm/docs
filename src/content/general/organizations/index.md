---
linkTitle: Organizations
title: Organizations
description: Explaining the organization concept in the Giant Swarm management API
last_review_date: 2021-04-21
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

<i class="fa fa-warning"></i> This article covers organizations as defined in the [management API]({{< relref "/ui-api/management-api/_index.md" >}}). These are replacing the organizations as used with the [REST API]({{< relref "/ui-api/rest-api/index.md">}}). While the general concept is similar in both implementations, there are difference which we'll provide more detailed documentation for soon.

<!-- TODO: link article about changes and migration -->

</div>

## Introduction

Organizations are a way to manage resources like clusters and apps in a way that different entities are isolated from each other. You can use organizations to separate projects, business units, teams etc.

Clusters are _owned_ by organizations. So in order to be able to manage a cluster (on the management API level, not on the individual cluster level), access to the organization owning the cluster is required.

Technically, organizations make use of some well-known building blocks of Kubernetes in the [management cluster]({{< relref "/general/management-clusters/index.md" >}}):

- Namespaces
- Role based access control (RBAC)
- Specific custom resources (CRs) that tie things together and make them easier to manage
- Operators which automate some management tasks

Typical use cases for organizations are:

- Separating clusters for development, experimentation, and testing, form clusters used for staging and for production purposes.

- Isolating teams, business units, or even legal entities.

At Giant Swarm, for example, we run several shared installations where we allow different customers access to a single organization only, usually before they get their own installation. This way we can ensure that each customer, while using the same management cluster, can only access their own clusters and other resources.

## Visual overview

TODO: visualization

- Organization CR
- org-namespace per organization
- Cluster resources, app resources, configmaps, secrets, other resources
- User/group from IdP, or service account, being bound via role/clusterrole

## Organization CRD and CRs {#organization-crd-cr}

If the concept of custom resources (CR) and custom resource definitions (CRD) is new to you: Kubernetes allows to define [arbitrary objects](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to be handled via the Kubernetes API. The schema of such an object is specified by a custom resource definition. The actual objects are called the custom resources.

Giant Swarm management clusters provide a custom resource definition (CRD) named `Organization` (long form: `organizations.security.giantswarm.io`). An organization is defined simply by a custom resource using that CRD, which we'll call an "organization CR" here for brevity.

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

For example, for an organization `acme`, there is the defining organization CR named `acme`. In addition, cluster-operator ensures the existence of the namespace `org-acme` in the management cluster.

We recommend to place all resources to be owned by an organization into the organization's namespace. Our user interfaces will work towards supporting this as a default.

### Namespace use in different providers {#namespace-use}

Giant Swarm is currently working towards making the organization's namespace the default namespace for all resources owned by the organization: clusters, node pools, apps, and more. We have (as of April 2021) reached different stages on different providers.

#### Azure {#namespace-use-azure}

With the latest workload cluster releases for Azure (as of April 2021 that is v14.1.x), all cluster and node pool resources are placed in the organization namespace by default.

Resources belonging to apps deployed to workload clusters are not yet placed in the organization namespace.

#### AWS {#namespace-use-aws}

With the latest AWS releases (as of April 2021 that's v14.1.x), the organization namespace is not yet used by default.

#### On-premises (KVM) {#namespace-use-onprem}

With the latest KVM releases (as of April 2021 that's v13.1.x), the organization namespace is not yet used by default.

## Access control

The management API relies on single sign-on using each customer's own identity provider for authentication.

As the customer's admin for an installation, you decide which users should get access to an organization's resources. You do so associating the user or group identifiers from your own identity provider with permissions for resources in the organization's namespace. All of this is done using standard Kubernetes RBAC elements:

- `Role` and `ClusterRole` resources define the permissions to be granted (using verbs like `get`, `create`, `delete` etc.) for a set of resources. You can define these roles yourself, or get started with the default roles we provide.
- `RoleBindings` associate (cluster) roles with the organization's namespace and subjects like users, groups, and service accounts.

<!-- TODO: link to SSO documentation once it's published -->

Our web user interface provides support for interactively adding and revoking organization access to/from users, groups, and service accounts.

<!-- TODO: link to web user interface > organizations > access control -->

## Managing organizations

Organizations can be managed in several ways.

- The [web user interface]({{< relref "/ui-api/web/_index.md" >}}) allows to create organizations, delete organizations, and manage access interactively. The web user interface leverages the [management API]({{< relref "/ui-api/management-api/_index.md" >}}).
- The [management API]({{< relref "/ui-api/management-api/_index.md" >}}) provides full, native support for managing all organization-related resources.

In addition, we plan to enhance the `kubectl` user experience for organization management via our [`gs`]({{< relref "/ui-api/kubectl-gs/_index.md" >}}) plug-in.

<!-- TODO: set links to more organization-specific sub sections once they are published -->

## Migrating from the REST API {#migration-from-rest-api}

Giant Swarm migrates all organizations from the REST API era into the management API to ensure a smooth transition for customers.

In some cases, renaming an organization is necessary, where the original organization used characters that are not supported any more (uppercase letters and underscores). In this case, Giant Swarm Solution Engineers will reach out to their customer contacts to agree on the new organization names.

We will provide additional information regarding the technical changes caused by the migration soon.

<!-- TODO: link specific page "Migration of organizations from REST API to MAPI" once published -->
