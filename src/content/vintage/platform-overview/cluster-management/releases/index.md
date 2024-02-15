---
linkTitle: Releases
title: Workload cluster release versions
description: Details on the workload cluster release offered by Giant Swarm and ways to look up even more details.
last_review_date: 2023-07-05
weight: 30
menu:
  main:
    parent: platform-overview-cluster-management
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
  - /general/releases
  - /reference/release-versions/
  - /reference/tenant-cluster-release-versions/
  - /reference/workload-cluster-release-versions/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Our workload cluster (formerly: _tenant cluster_) releases define the capabilities of the clusters you create in your installations. Here we explain the semantics of our versioning and give details on workload cluster release on certain providers.

## Introduction

Throughout the lifecycle of a cluster, you first have the option to select a workload cluster release when creating the cluster. Later you are likely to upgrade the cluster from release to release. Understanding the differences of Major, Minor and Patch releases and their impact is crucial.

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
- When releasing a new minor or patch version, we deprecate the previous version. For example, when v12.1.0 comes out, the previous version v12.0.1 gets deprecated.

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

- In the [web UI]({{< relref "/vintage/platform-overview/web-interface/" >}}), the cluster overview and the cluster details page show the release version number of the workload cluster. In the cluster details page you can click the release version number to get more information about a workload cluster release.

- In `gsctl`, our command line interface, commands like [`gsctl list clusters`]({{< relref "/vintage/use-the-api/gsctl/list-clusters" >}}) and [`gsctl show cluster`]({{< relref "/vintage/use-the-api/gsctl/show-cluster" >}}) reveal the release version number of an existing cluster. To get information on all available releases, use the [`gsctl list releases`]({{< relref "/vintage/use-the-api/gsctl/list-releases" >}}) command. The command `gsctl show release` gives you more details on a specific workload cluster release.

- The [Giant Swarm REST API]({{< relref "/vintage/use-the-api/rest-api" >}}) provides an endpoint to list all workload cluster releases with their details.

## Details about workload cluster releases and features {#release-details}

### Node pools {#nodepools}

[Node pools]({{< relref "/vintage/advanced/cluster-management/node-pools-vintage" >}}) were introduced by the following workload cluster releases:

- AWS: v{{% first_aws_nodepools_version %}}

- Azure: v{{% first_azure_nodepools_version %}}

### Preinstalled and optional Apps {#apps}

Depending on your provider (AWS, Azure, or KVM), the apps Ingress NGINX Controller, External DNS and Cert Manager may be preinstalled, optional, or not available (n/a).

Preinstalled apps are installed by default upon cluster creation. Optional apps can be installed from App Catalogs. In releases where they are not preinstalled, n/a apps (e.g. External DNS in certain releases) are currently not available to be installed as an optional app.

| Workload cluster release version | Ingress NGINX Controller | External DNS  | Cert Manager |
|:--------------------------------:|:------------------------:|:-------------:|:------------:|
| **AWS v10.x.x+**                 | optional                 | preinstalled  | preinstalled |
| **AWS legacy**                   | preinstalled             | n/a           | optional     |
| **Azure v12.x.x+**               | optional                 | preinstalled  | optional     |
| **Azure legacy**                 | preinstalled             | preinstalled  | optional     |
| **KVM 12.2.x+**                  | optional                 | n/a           | optional     |
| **KVM legacy**                   | preinstalled             | n/a           | optional     |

## Further reading

- [Cluster upgrades]({{< relref "/vintage/platform-overview/cluster-management/cluster-upgrades" >}}) explains how upgrades work and suggests some best practices to keep a cluster ready to upgrade.
