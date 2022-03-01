---
linkTitle: Releases
title: Workload cluster release versions
description: Details on the workload cluster release offered by Giant Swarm and ways to look up even more details.
last_review_date: 2022-03-01
weight: 30
menu:
  main:
    parent: general
user_questions:
  - What is a workload cluster release?
  - Where can I find details about workload cluster releases?
  - What is a major workload cluster release?
  - What is a minor workload cluster release?
  - What is a patch workload cluster release?
  - What is a pre-release?
  - How long are workload cluster releases supported?
  - What does it mean when a workload cluster release is deprecated?
  - How soon does Giant Swarm provide new Kubernetes versions?
  - How are workload cluster releases announced?
aliases:
  - /reference/release-versions/
  - /reference/tenant-cluster-release-versions/
  - /reference/workload-cluster-release-versions/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

# Workload Cluster release versions

Our workload cluster (formerly: _tenant cluster_) releases define the capabilities of the clusters you create in your installations. Here we explain the semantics of our versioning and give details on workload cluster release on certain providers.

## Introduction

Throughout the lifecycle of a cluster, you first have the option to select a workload cluster release when creating the cluster. Later you are likely to upgrade the cluster from release to release. Understanding the differences of Major, Minor and Patch releases and their impact is crucial. We sometimes give you access to pre-releases, so understanding their impact and their value will help you decide whether to try them or not.

Each workload cluster release bundles a stack of components with their specific versions. The workload cluster release itself is distinguished by the provider it is made for (AWS, Azure, or KVM) and the version number, which follows the [Semver](https://semver.org/) standard.

We test workload cluster releases as a whole. To upgrade a component to a newer version, the entire cluster is upgrade to a new workload cluster release. This is our best way to ensure that all components in the cluster interoperate well.

## Conventions around workload cluster release versioning {#versioning-conventions}

The Semver standard specifies version numbers in the form of `Major.Minor.Patch`.

Each new workload cluster release defines a set of changes with regard to exactly one previous workload cluster release. The nature or impact of the changes influence the version number of the new release.

### Major version {#major}

The Kubernetes project provides the most important component of our workload clusters. So we align our workload cluster release versioning with the Kubernetes releases.

**Convention**: For each new _minor_ Kubernetes release we provide a new _major_ workload cluster release version.

The following table shows which of our major releases contain which Kubernetes release.

| Workload cluster release version | Kubernetes version | Availability |
|:---------------------------:|:------------------:|:------------:|
| **12.x.x**                  | 1.17.x             | Available    |
| **13.x.x**                  | 1.18.x             | Available    |
| **14.x.x**                  | 1.19.x             | Available    |
| **15.x.x**                  | 1.20.x             | Available    |
| **16.x.x**                  | 1.21.x             | Available    |

We test every new major workload cluster release, bringing a new Kubernetes minor release, against the CNCF [conformance test suite](https://github.com/cncf/k8s-conformance).
Every workload cluster release, from patch to major, also undergoes automated integration testing.

A major workload cluster release may contain more important changes, apart from a new Kubernetes release. Check the [Details about releases and features](#release-details) section for more information.

### Minor version {#minor}

We increase (bump) the minor version number when a workload cluster release adds new functionality, while maintaining the functionality of the stack as it was in the previous version. This can include minor upgrades of third party components, except for Kubernetes.

### Patch version {#patch}

We use patch releases to publish bug fixes, security fixes, or to make changes to the observability while maintaining the given functionality of the stack. This can include any sort of patch upgrades of third party components.

### Lifecycle {#lifecycle}

For every provider, we maintain **two different major versions** of workload cluster releases at the same time, which means that you have two different Kubernetes minor versions to chose from.

With our development of **new functionality** we focus on our latest major version. The older major version is mostly maintained to fix security issues and stability problems.

Old workload cluster release get [deprecated](#deprecation) when replaced by newer ones. After deprecation, and once no longer in use by any customer, a workload cluster release gets archived, which means that it is no longer accessible to you.

### Deprecation {#deprecation}

Once we provide a new workload cluster release, be it major, minor, or patch, we usually deprecate an older version.

- When we release a new major version, we deprecate all remaining workload cluster release in the oldest major version (to have only two major versions maintained).
- When releasing a new minor or patch version, we deprecate the previous version. For example, when v12.1.0 comes out, the previous version v12.0.1 gets deprecated.

Once deprecated, you can still continue to use the workload cluster release with existing clusters. In addition, as long as you have at least one cluster in your installation running the deprecated release, you can also create new clusters using that release. This allows you to create test clusters to test an upgrade from that release.

### Pre-release

Apart from the stable releases described above, we sometimes offer pre-releases. The goal of pre-releases is to give you the option to test new features or use new functionality before the feature is released in a major version. At the same time it helps us evaluate the impact of new features we are planning to release. This hinges on your trying out these versions and coming back to us with feedback and bug reports. This utimately leads to a more robust release. You will have the freeedom to break things, but _should_ not use this release in production, for reasons of stability and an uncertain upgrade path.

Pre-releases can be alpha, beta, or RC depending on the testing needs of the team wanting to test their feature.

#### Use Cases for Pre-Releases:

- New feature with unclear impact is done and the team wants to test and evaluate its impact before deciding the scope of the release. This is an __alpha__ release. Customers get early access to the functionaliy and see if it satisfies their requirements. Customers report back with bugs and additional commentary. This allows the functionality to be evaluated in a less controlled way and to fix bugs that we may have not found. It also may bring about reconsidering the feature/solution in general.

- New high impact feature is done, but needs to wait for the next major release. This is a __beta__ release. Customers get early access to the functionaliy and see that it sits well with their set-up. Customers report back with bugs . This allows us to make fixes to bugs that we may have not found.

- New high impact feature is done and is urgently needed by a customer. This is a __release candidate (rc)__ release. The customer can get a pre-release to test and roll out ASAP. This release is complete and stable. It may not meet the quality bars of a general availaibility (ga) release.


### Inspecting workload cluster releases {#inspecting}

You have several options to inspect workload cluster release details:

- We announce new workload cluster releases in your Slack support channel. In each announcement, you will find a link to the corresponding release notes in our [changes and releases]({{< relref "/changes" >}}) section here on the docs site, where you also find comprehensive release notes.

- In the [web UI]({{< relref "/ui-api/web/" >}}), the cluster overview and the cluster details page show the release version number of the workload cluster. In the cluster details page you can click the release version number to get more information about a workload cluster release. Additionally, the web UI will soon provide more ways to browse workload cluster releases and inspect changes between versions.

- In `gsctl`, our command line interface, commands like [`gsctl list clusters`]({{< relref "/ui-api/gsctl/list-clusters" >}}) and [`gsctl show cluster`]({{< relref "/ui-api/gsctl/show-cluster" >}}) reveal the release version number of an existing cluster. To get information on all available releases, use the [`gsctl list releases`]({{< relref "/ui-api/gsctl/list-releases" >}}) command. The command `gsctl show release` gives you more details on a specific workload cluster release.

- The [Giant Swarm REST API]({{< relref "/ui-api/rest-api" >}}) provides an endpoint to list all workload cluster releases with their details.


## Further reading

- [Cluster upgrades]({{< relref "/general/cluster-upgrades" >}}) explains how upgrades work and suggests some best practices to keep a cluster ready to upgrade.
