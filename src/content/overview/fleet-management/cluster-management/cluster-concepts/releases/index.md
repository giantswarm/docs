---
title: Workload cluster releases
description: Details on the workload cluster release offered by Giant Swarm and ways to look up even more details.
weight: 30
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement-concepts
    identifier: overview-fleetmanagement-clustermanagement-concepts-releases
user_questions:
  - What is a workload cluster release?
  - Where can I find details about workload cluster releases?
  - What is a major workload cluster release?
  - What is a minor workload cluster release?
  - What is a patch workload cluster release?
  - How long are workload cluster releases supported?
  - What does it mean when a workload cluster release is deprecated?
  - How soon does Giant Swarm provide new Kubernetes versions?
  - How are workload cluster releases announced?
  - What is a pre-release?
  - What is an alpha release?
  - What is a beta release?
  - What is a release candidate?
aliases:
  - /platform-overview/cluster-management/releases
  - /reference/workload-cluster-release-versions/
last_review_date: 2025-07-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-tenet
---

Our workload cluster releases define the capabilities of the clusters you create in your installations. Here we explain the semantics of our versioning and give details on workload cluster release on certain providers.

## Introduction

Throughout the lifecycle of a cluster, you first have the option to select a workload cluster release when creating the cluster. Later you are likely to upgrade the cluster from release to release. Understanding the differences of Major, Minor and Patch releases and their impact is crucial.

Each workload cluster release bundles a stack of components with their specific versions. The workload cluster release itself is distinguished by the provider it is made for (AWS, Azure, or KVM) and the version number, which follows the [Semver](https://semver.org/) standard.

We test workload cluster releases as a whole. To upgrade a component to a newer version, the entire cluster is upgrade to a new workload cluster release. This is our best way to ensure that all components in the cluster interoperate well.

## Conventions around release versioning {#versioning-conventions}

The Semver standard specifies version numbers in the form of `Major.Minor.Patch`.

Each new workload cluster release defines a set of changes with regard to exactly one previous workload cluster release. The nature or impact of the changes influence the version number of the new release.

### Major version {#major}

The Kubernetes project provides the most important component of our workload clusters. So we align our workload cluster release versioning with the Kubernetes releases.

**Convention**: For each new _minor_ Kubernetes release we provide a new _major_ workload cluster release version.

The following table shows which of our major releases contain which Kubernetes release.

| Release version | Kubernetes version | Availability |
|:---------------------------:|:------------------:|:------------:|
| **28.x.x**                  | 1.28.x             | Available    |
| **29.x.x**                  | 1.29.x             | Available    |
| **30.x.x**                  | 1.30.x             | Available    |
| **31.x.x**                  | 1.31.x             | Available    |
| **32.x.x**                  | 1.32.x             | Available    |

We test every new major workload cluster release, bringing a new Kubernetes minor release, against the CNCF [conformance test suite](https://github.com/cncf/k8s-conformance).
Every workload cluster release, from patch to major, also undergoes automated integration testing.

A major workload cluster release may contain other important changes, apart from a new Kubernetes release. Check the [Details about releases and features](#release-details) section for more information.

### Minor version {#minor}

We increase (bump) the minor version number when a workload cluster release adds new functionality, while maintaining the functionality of the stack as it was in the previous version. This can include minor upgrades of third party components, except for Kubernetes.

### Patch version {#patch}

We use patch releases to publish bug fixes, security fixes, or to make changes to the observability while maintaining the given functionality of the stack. This can include any sort of patch upgrades of third party components.

### Lifecycle {#lifecycle}

For every provider, we maintain **two major versions** of workload cluster releases at the same time, which means that you have two different Kubernetes minor versions to chose from.

With our development of **new functionality** we focus on our latest major version. The older major version is mostly maintained to fix security issues and stability problems.

Old workload cluster releases get [deprecated](#deprecation) when replaced by newer ones. After deprecation, and once no longer in use by any customer, a workload cluster release gets archived, which means that it is no longer accessible to you.

### Deprecation {#deprecation}

Once we provide a new workload cluster release, be it major, minor, or patch, we usually deprecate an older version.

- When we release a new major version, we deprecate all remaining workload cluster release in the oldest major version (to have only two major versions maintained).
- When releasing a new minor or patch version, we deprecate the previous version. For example, when 28.1.0 comes out, the previous version 28.0.1 gets deprecated.

Once deprecated, you can still continue to use the workload cluster release with existing clusters. In addition, as long as you have at least one cluster in your installation running the deprecated release, you can also create new clusters using that release. This allows you to create test clusters to test an upgrade from that release.

### Pre-releases

Pre-releases (when available) give you the option to test new features or use new functionality before the feature is released. At the same time helps us release new features and test them in a realworld scenario with your help. When you test out a pre-release it helps find bugs or evaluate the impact of new functionality on the system.

Currently not all Giant Swarm releases become available as pre-releases. We communicate pre-releases, when they are available for customer testing.

Pre-releases can be alpha, beta, or release candidates (RC). This depends on the needs of the team wanting to test their feature.

Use Cases for Pre-Releases:

- A new feature with unclear impact is done and the team wants to test and evaluate its impact before deciding the scope of the release (alpha). Customers get early access to the functionality and see if it satisfies their requirements. Customers report back with bugs and additional commentary. This allows the functionality to be evaluated in a less controlled way than in our testing environments. It also identifies bugs that we may have not found, allowing us to fix them early. It also may bring about reconsidering the feature/solution in general.

- A new high impact feature is done, but needs to wait for the next major release (beta). Customers get early access to the functionality and see that it sits well with their set-up. Customers report back with bugs as necessary. This allows us to make fixes to bugs that we may have not found.

- A new high impact feature is done and is urgently needed by a customer (release candidate (rc)). The customer can get a pre-release to test and roll out ASAP. This release is complete and stable. It may not meet the quality bars of a general availaibility (GA) release.

### Inspecting workload cluster releases {#inspecting}

You have several options to inspect workload cluster release details:

- We announce new workload cluster releases in your Slack support channel. In each announcement, you will find a link to the corresponding release notes in our [changes and releases]({{< relref "/changes" >}}) section here on the docs site, where you can also find comprehensive release notes.

- Using the [`kubectl gs get release`]({{< relref "/vintage/platform-overview/web-interface/" >}}) command, you can get more information about the workload cluster releases available in your installation. This command lists all available workload cluster releases, their versions, and the Kubernetes version they contain.

### Default applications {#apps}

TBD

## Further reading

- [Cluster upgrades]({{< relref "/tutorials/fleet-management/cluster-management/cluster-upgrades" >}}) explains how upgrades work and suggests some best practices to keep a cluster ready to upgrade.
