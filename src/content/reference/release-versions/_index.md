---
title: Release Versions
description: Here you find our reference regarding our release versions
date: 2020-05-14
layout: subsection
weight: 500
---

# Giant Swarm Release Versions

When you create a tenant cluster at Giant Swarm you also get to choose which
release version you would like the cluster to have.

The release version of a cluster helps you identify additional information like
what Kubernetes version the cluster will have.

Besides Kubernetes, other components come into play as well, for example Calico,
Flannel, Docker, and our own services and operators.

Together, all these components define the capabilities of a tenant cluster.

When a new version of a component gets released (to fix a bug or introduce a new feature),
we create a new release version so that you can upgrade your existing tenant clusters
and create new clusters with the added or fixed functionality.

## Conventions around release versioning

We've had to break these conventions in some cases, but we're trying to re-align
things as time goes on and customers no longer use older versions.

### Major versions increment on Kubernetes releases
We generally try to increment our Major version only when there is a new Kubernetes release.


||||
|-----------|------------|-|
|**v9.0.x** | Kubernetes 1.15.x ||
|**v11.x.x** | Kubernetes 1.16.x ||
|**v12.x.x** | Kubernetes 1.17.x | not yet available|
|**v13.x.x** | Kubernetes 1.18.x | not yet available|


#### Exceptions

On AWS, **v9.2.0** and up contains **Kubernetes 1.16.x**

## Versions that support node pools

Currently only AWS **v11.x.x** and up support nodepools.

While it is still a work in progress, on Azure, **v12.1.0** and above will
be the releases that support nodepools.

## Versions with an optional ingress controller

As of **v11.0.0** on AWS installations, the ingress controller has been
made optional. That means it is not installed by default when you create your
cluster.

On Azure and KVM the ingress controller is still automatically installed, though
a release is planned for Azure that will make the ingress controller optional
Most likely that will be **v11.4.0**

## Versions with Flatcar Container Linux

Generally all active releases are available with Flatcar Container Linux as
the operating system.

Look for the latest patch version.

**AWS**
||||
|-----------|------------|-|
|**v9.3.0** | Kubernetes 1.16.x | Flatcar Container Linux|
|**v11.3.0** | Kubernetes 1.16.x | Flatcar Container Linux with Nodepools|

**KVM**
||||
|-----------|------------|-|
|**v9.0.3** | Kubernetes 1.15.x | Flatcar Container Linux|
|**v11.3.x** | Kubernetes 1.16.x | Flatcar Container Linux|

**Azure**
||||
|-----------|------------|-|
|**v11.3.x** | Kubernetes 1.16.x | Flatcar Container Linux|
