---
title: Release Versions
description: Here you find our reference regarding our release versions
date: 2020-10-05
layout: subsection
weight: 500
---

# Giant Swarm Release Versions

When you create a tenant cluster at Giant Swarm you also get to choose which
release version you would like the cluster to have.

The release version of a cluster helps you identify additional information like
what Kubernetes version the cluster will have.

Besides Kubernetes, other components come into play as well, for example Calico, Docker, CoreDNS, and our own services and operators.

Together, all these components define the capabilities of a tenant cluster.

When a new version of a component gets released (to fix a bug or introduce a new feature),
we create a new release version so that you can upgrade your existing tenant clusters
and create new clusters with the added or fixed functionality.

## Conventions around release versioning

We've had to break these conventions in some cases, but we're re-aligning
things as time goes on and customers no longer use older versions.

### Major versions increment on Kubernetes releases

We generally try to increment our Major version only when there is a new Kubernetes release.

| Giant Swarm release version | Kubernetes version | Status |
|:-----------:|:------------:|:-----:|
| **9.x.x** | 1.15.x\* | Available |
| **11.x.x** | 1.16.x | Available |
| **12.x.x** | 1.17.x | Available |
| **13.x.x** | 1.18.x | Available soon |


\*) On AWS, **v9.2.0** and **v9.3.x** and up includes **Kubernetes 1.16.x**.

## Versions that support node pools

- AWS **{{% first_aws_nodepools_version %}}** and up.

- Azure **{{% first_azure_nodepools_version %}}** and up.

## Versions with an optional ingress controller

As of **v11.0.0** on AWS installations, **v12.0.0** on Azure, and **12.2.0** on KVM the ingress controller has been
made optional. That means it is not installed by default when you create your
cluster.

## Versions with Flatcar Container Linux

Generally all active releases are available with Flatcar Container Linux as
the operating system.

This table shows which releases first introduces Flatcar Container Linux on various providers and minor releases:

| Provider |Giant Swarm minor release | Kubernetes version |
|:-:|:-:|:-:|
| AWS | **v9.3.0** | 1.16.x |
| AWS | **v11.3.0** | 1.16.x |
| Azure | **v11.3.x** | 1.16.x |
| KVM | **v9.0.3**  | 1.15.x  |
| KVM | **v11.3.x** | 1.16.x  |

## Latest release information

Check the [giantswarm/releases](https://github.com/giantswarm/releases) GitHub repository for full information on all releases.
