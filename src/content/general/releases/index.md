---
linkTitle: Releases
title: Workload cluster release versions
description: Details on the workload cluster release offered by Giant Swarm and ways to look up even more details.
last_review_date: 2020-10-30
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
  - How long are workload cluster releases supported?
  - What does it mean when a workload cluster release is deprecated?
  - How soon does Giant Swarm provide new Kubernetes versions?
aliases:
  - /reference/release-versions/
  - /reference/tenant-cluster-release-versions/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

# Workload Cluster release versions

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
| **9.x.x**                   | 1.15.x\*           | Available    |
| **11.x.x**                  | 1.16.x             | Available    |
| **12.x.x**                  | 1.17.x             | Available    |
| **13.x.x**                  | 1.18.x             | Available    |
| **14.x.x**                  | 1.19.x             | ETA January 2021|

\*) As an exception from the convention, on AWS, workload cluster releases v9.2.0 and v9.3.x include Kubernetes v1.16.x.

We test every new major workload cluster release, bringing a new Kubernetes minor release, against the CNCF [conformance test suite](https://github.com/cncf/k8s-conformance).
Every workload cluster release, from patch to major, also undergoes automated integration testing.

A major workload cluster release may contain more important changes, apart from a new Kubernetes release. Check the [Details about releases and features](#release-details) section for more information.

### Minor version {#minor}

We increase (bump) the minor version number when a workload cluster release adds new functionality, while maintaining the functionality of the stack as it was in the previous version. This can include minor upgrades of third party components, except for Kubernetes.

### Patch version {#patch}

We use patch releases to publish bug fixes, security fixes, or to make changes to the observability while maintaining the given functionality of the stack. This can include any sort of patch upgrades of third party components.

### Lifecycle {#lifecycle}

For every provider, we maintain **two different major versions** of workload cluster releases at the same time, which means that you have two different Kubernetes minor versions to chose from.

Whenever a new Kubernetes minor version is released by the Kubernetes project, we aim to make that version available in a new major workload cluster release within 30 days.

With our development of **new functionality** we focus on our latest major version. The older major version is mostly maintained to fix security issues and stability problems.

Old workload cluster release get [deprecated](#deprecation) when replaced by newer ones. After deprecation, and once no longer in use by any customer, a workload cluster release gets archived, which means that it is no longer accessible to you.

### Deprecation {#deprecation}

Once we provide a new workload cluster release, be it major, minor, or patch, we usually deprecate an older version.

- When we release a new major version, we deprecate all remaining workload cluster release in the oldest major version (to have only two major versions maintained).
- When releasing a new minor or patch version, we deprecate the previous version. For example, when v12.1.0 comes out, the previous version v12.0.1 gets deprecated.

Once deprecated, you can still continue to use the workload cluster release with existing clusters. In addition, as long as you have at least one cluster in your installation running the deprecated release, you can also create new clusters using that release. This allows you to create test clusters to test an upgrade from that release.

### Inspecting workload cluster releases {#inspecting}

You have several options to inspect workload cluster release details:

- All workload cluster releases are defined in code in the [giantswarm/releases](https://github.com/giantswarm/releases) GitHub repository. Here you also find comprehensive release notes.

- In the [web UI](/reference/web-interface/), the cluster overview and the cluster details page show the release version number of the workload cluster. In the cluster details page you can click the release version number to get more information about a workload cluster release. Additionally, the web UI will soon provide more ways to browse workload cluster releases and inspect changes between versions.

- In `gsctl`, our command line interface, commands like [`gsctl list clusters`](/reference/gsctl/list-clusters/) and [`gsctl show cluster`](/reference/gsctl/show-cluster/) reveal the release version number of an existing cluster. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command. The command `gsctl show release` gives you more details on a specific workload cluster release.

- The [Rest API]({{< relref "/ui-api/rest-api" >}}) provides an endpoint to list all workload cluster releases with their details.

## Details about workload cluster releases and features {#release-details}

### Node pools {#nodepools}

[Node pools](/basics/nodepools/) were introduced by the following workload cluster releases:

- AWS: **{{% first_aws_nodepools_version %}}**.

- Azure: **{{% first_azure_nodepools_version %}}**.

### Preinstalled and optional Apps {#apps}

Depending on your provider (AWS, Azure, or KVM), the apps NGINX IC, External DNS, and Cert Manager may be preinstalled, optional, or not available (n/a).

Preinstalled apps are installed by default upon cluster creation. Optional apps can be installed from App Catalogs. In releases where they are not preinstalled, n/a apps (e.g. External DNS in certain releases) are currently not available to be installed as an optional app.

| Workload cluster release version | NGINX IC      | External DNS  | Cert Manager |
|:------------------------------:|:-------------:|:-------------:|:------------:|
| **AWS v10.x.x+**               | optional      | preinstalled  | preinstalled |
| **AWS legacy**                 | preinstalled  | n/a           | optional     |
| **Azure v12.x.x+**             | optional      | preinstalled  | optional     |
| **Azure legacy**               | preinstalled  | preinstalled  | optional     |
| **KVM 12.2.x+**                | optional      | n/a           | optional     |
| **KVM legacy**                 | preinstalled  | n/a           | optional     |

### Flatcar Container Linux {#flatcar}

Generally all active workload cluster releases are available with Flatcar Container Linux as
the operating system.

This table shows which workload cluster releases first introduced Flatcar Container Linux on various providers and with which Kubernetes minor version:

| Provider | Workload cluster release | Kubernetes version |
|:-:|:-:|:-:|
| AWS | **v9.3.0** | 1.16.x |
| AWS | **v11.3.0** | 1.16.x |
| Azure | **v11.3.x** | 1.16.x |
| KVM | **v9.0.3**  | 1.15.x  |
| KVM | **v11.3.x** | 1.16.x  |

## Further reading

- [Cluster Upgrades with Giant Swarm](/reference/cluster-upgrades/) explains how upgrades work and suggests some best practices to keep a cluster ready to upgrade.
