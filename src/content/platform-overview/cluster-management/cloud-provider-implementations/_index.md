---
linkTitle: Cloud providers and implementations
title: Supported cloud providers and implementations
description: Providers for which we support cluster management, and the different generations.
last_review_date: 2023-07-03
weight: 30
aliases:
menu:
  main:
    parent: platform-overview-cluster-management
    identifier: cluster-management-generations
user_questions:
  - Which cloud providers are supported?
  - Which cluster management generation is the latest?
owner:
  - https://github.com/orgs/giantswarm/teams/area-kaas
  - https://github.com/orgs/giantswarm/teams/team-horizon
---

One of the main building blocks of the platform is the cluster management. Our cluster management implementations come in different generations which are designed to be compatible with each other and integrate well with our [app platform]({{< relref "/platform-overview/app-platform" >}}). Development focuses on the latest generation: cluster management based on the Kubernetes subproject [Cluster API (CAPI)]({{< relref "/platform-overview/architecture" >}}). We are planning and supporting the migration of customer clusters to this generation in the long term. The previous generation is called _Vintage_. Depending on the generation, we support certain cloud providers.

## Cluster API (CAPI) generation

This is the latest and recommended generation.

We run [Cluster API (CAPI)](https://github.com/kubernetes-sigs/cluster-api/) operators and their respective cloud provider-specific operators, such as [cluster-api-provider-aws (CAPA)](https://github.com/kubernetes-sigs/cluster-api-provider-aws/) for the AWS cloud, on our Management Clusters. Our [Cluster API architecture page]({{< relref "/platform-overview/architecture" >}}) explains more details about the architecture of the platform.

This generation has several benefits over the previous _Vintage_ generation:

- CAPI and its cloud provider-specific implementations (e.g. CAPA) are well-supported open source projects under the Kubernetes community's umbrella. They unify creation and management of Kubernetes clusters across many cloud providers. Using the CAPI types to represent infrastructure, for example the `Cluster` CR, means that vendor lock-in is avoided and the community evolves the project over time. There is much less Giant Swarm specific code involved.
- Highly flexible configuration for infrastructure. For example, network CIDRs can be customized, or clusters installed into existing networks.
- Support for private clusters
- Support for moving workload clusters across management clusters

For certain cloud providers, there are even different options available: for example with Amazon Web Services (AWS), we offer open source Kubernetes with the control plane running on EC2 instances, or use of AWS EKS for which AWS runs the Kubernetes control plane.

The open-source cloud infrastructure providers of CAPI are separate projects – named CAPA for the AWS cloud, CAPZ for Azure, etc. Since they provide a major part of the cluster management, we name our implementations after them. We offer the following cloud provider-specific implementations:

- **{{% impl_title "capa_ec2" %}}**
- **{{% impl_title "capa_eks" %}}**
- **{{% impl_title "capg_vms" %}}**
- **{{% impl_title "capv" %}}**
- **{{% impl_title "capvcd" %}}**
- **{{% impl_title "capz_vms" %}}**

## Vintage generation

This is the previous generation and is still in production with many of our customers. We still actively support this generation. However, the development focus is limited to main customer needs and supporting the migration to our CAPI-based implementations. For example, we introduced Cilium as the CNI (Kubernetes Container Network Interface) for both the CAPI-based and vintage generation in order to make the migration simple.

We offer the following cloud provider-specific implementations:

- **{{% impl_title "vintage_aws" %}}**
- **{{% impl_title "vintage_azure" %}}**
- **{{% impl_title "vintage_kvm" %}}** – _deprecated and being phased out_

## Choice of cloud provider and implementation

As a new customer, the decision is usually based on the desired cloud provider (e.g. AWS). You have an assigned account engineer at Giant Swarm who will help from the very beginning to compose the development platform to your needs. We will work with you to make the right choice of the implementation, and also clarify customizations, such as networking or other requirements.

Once the decision for a cloud provider and implementation was made, we can [get you started]({{< relref "/getting-started" >}}) quickly.

We also offer _proof of concept (PoC)_ projects in which we take 1-2 weeks to set up a reasonable and working prototype with you and present our platform capabilities. This also gives you a chance to witness our communication and [support model]({{< relref "/support" >}}) while we are in close contact, as we are with all existing customers.

If you want to follow the development of certain features or cloud provider-specific implementations, please have a look at our [roadmap GitHub project](https://github.com/orgs/giantswarm/projects/273/views/28).
