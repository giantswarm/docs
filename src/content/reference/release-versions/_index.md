---
title: Tenant Cluster Release Versions
description: Details on the tenant cluster release offered by Giant Swarm and ways to look up even more details.
date: 2020-11-18
last_review_date: 2020-10-30
layout: subsection
weight: 500
user_questions:
  - What is a tenant cluster release?
  - Where can I find details about tenant cluster releases?
  - What is a major tenant cluster release?
  - What is a minor tenant cluster release?
  - What is a patch tenant cluster release?
  - How long are tenant cluster releases supported?
  - What does it mean when a tenant cluster release is deprecated?
  - How soon does Giant Swarm provide new Kubernetes versions?
alias:
  - /reference/release-versions/
---

# Tenant Cluster Releases

Our tenant cluster releases define the capabilities of the clusters you create in your installations. Here we explain the semantics of our versioning and give details on tenant cluster release on certain providers.

## Introduction

Throughout the lifecycle of a cluster, you first have the option to select a tenant cluster release when creating the cluster. Later you are likely to upgrade the cluster from release to release. Understanding the differences of Major, Minor and Patch releases and their impact is crucial.

Each tenant cluster release bundles a stack of components with their specific versions. The tenant cluster release itself is distinguished by the provider it is made for (AWS, Azure, or KVM) and the version number, which follows the [Semver](https://semver.org/) standard.

We test tenant cluster releases as a whole. To upgrade a component to a newer version, the entire cluster is upgrade to a new tenant cluster release. This is our best way to ensure that all components in the cluster interoperate well.

## Conventions around tenant cluster release versioning {#versioning-conventions}

The Semver standard specifies version numbers in the form of `Major.Minor.Patch`.

Each new tenant cluster release defines a set of changes with regard to exactly one previous tenant cluster release. The nature or impact of the changes influence the version number of the new release.

### Major version {#major}

The Kubernetes project provides the most important component of our tenant clusters. So we align our tenant cluster release versioning with the Kubernetes releases.

**Convention**: For each new _minor_ Kubernetes release we provide a new _major_ tenant cluster release version.

The following table shows which of our major releases contain which Kubernetes release.

| Tenant cluster release version | Kubernetes version | Availability |
|:---------------------------:|:------------------:|:------------:|
| **9.x.x**                   | 1.15.x\*           | Available    |
| **11.x.x**                  | 1.16.x             | Available    |
| **12.x.x**                  | 1.17.x             | Available    |
| **13.x.x**                  | 1.18.x             | ETA November 2020 |
| **14.x.x**                  | 1.19.x             | ETA December 2020 |

\*) As an exception from the convention, on AWS, tenant cluster releases v9.2.0 and v9.3.x include Kubernetes v1.16.x.

We test every new major tenant cluster release, bringing a new Kubernetes minor release, against the CNCF [conformance test suite](https://github.com/cncf/k8s-conformance).
Every tenant cluster release, from patch to major, also undergoes automated integration testing.

A major tenant cluster release may contain more important changes, apart from a new Kubernetes release. Check the [Details about releases and features](#release-details) section for more information.

### Minor version {#minor}

We increase (bump) the minor version number when a tenant cluster release adds new functionality, while maintaining the functionality of the stack as it was in the previous version. This can include minor upgrades of third party components, except for Kubernetes.

### Patch version {#patch}

We use patch releases to publish bug fixes, security fixes, or to make changes to the observability while maintaining the given functionality of the stack. This can include any sort of patch upgrades of third party components.

### Lifecycle {#lifecycle}

For every provider, we maintain **two different major versions** of tenant cluster releases at the same time, which means that you have two different Kubernetes minor versions to chose from.

Whenever a new Kubernetes minor version is released by the Kubernetes project, we aim to make that version available in a new major tenant cluster release within 30 days.

With our development of **new functionality** we focus on our latest major version. The older major version is mostly maintained to fix security issues and stability problems.

Old tenant cluster release get [deprecated](#deprecation) when replaced by newer ones. After deprecation, and once no longer in use by any customer, a tenant cluster release gets archived, which means that it is no longer accessible to you.

### Deprecation {#deprecation}

Once we provide a new tenant cluster release, be it major, minor, or patch, we usually deprecate an older version.

- When we release a new major version, we deprecate all remaining tenant cluster release in the oldest major version (to have only two major versions maintained).
- When releasing a new minor or patch version, we deprecate the previous version. For example, when v12.1.0 comes out, the previous version v12.0.1 gets deprecated.

Once deprecated, you can still continue to use the tenant cluster release with existing clusters. In addition, as long as you have at least one cluster in your installation running the deprecated release, you can also create new clusters using that release. This allows you to create test clusters to test an upgrade from that release.

### Inspecting tenant cluster releases {#inspecting}

You have several options to inspect tenant cluster release details:

- All tenant cluster releases are defined in code in the [giantswarm/releases](https://github.com/giantswarm/releases) GitHub repository. Here you also find comprehensive release notes.

- In the [web UI](/reference/web-interface/), the cluster overview and the cluster details page show the release version number of the tenant cluster. In the cluster details page you can click the release version number to get more information about a tenant cluster release. Additionally, the web UI will soon provide more ways to browse tenant cluster releases and inspect changes between versions.

- In `gsctl`, our command line interface, commands like [`gsctl list clusters`](/reference/gsctl/list-clusters/) and [`gsctl show cluster`](/reference/gsctl/show-cluster/) reveal the release version number of an existing cluster. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command. The command `gsctl show release` gives you more details on a specific tenant cluster release.

- The [Rest API](/basics/api/#rest-api) provides an endpoint to list all tenant cluster releases with their details.

## Details about tenant cluster releases and features {#release-details}

### Node pools {#nodepools}

[Node pools](/basics/nodepools/) were introduced by the following tenant cluster releases:

- AWS: **{{% first_aws_nodepools_version %}}**.

- Azure: **{{% first_azure_nodepools_version %}}**.

### Optional ingress controller {#optional-ic}

As of **v11.0.0** on AWS installations, **v12.0.0** on Azure, and **12.2.0** on KVM the ingress controller has been
made optional. That means it is not installed by default when you create your
cluster.

### Flatcar Container Linux {#flatcar}

Generally all active tenant cluster releases are available with Flatcar Container Linux as
the operating system.

This table shows which tenant cluster releases first introduced Flatcar Container Linux on various providers and with which Kubernetes minor version:

| Provider | Tenant cluster release | Kubernetes version |
|:-:|:-:|:-:|
| AWS | **v9.3.0** | 1.16.x |
| AWS | **v11.3.0** | 1.16.x |
| Azure | **v11.3.x** | 1.16.x |
| KVM | **v9.0.3**  | 1.15.x  |
| KVM | **v11.3.x** | 1.16.x  |

## Further reading

- [Cluster Upgrades with Giant Swarm](/reference/cluster-upgrades/) explains how upgrades work and suggests some best practices to keep a cluster ready to upgrade.
