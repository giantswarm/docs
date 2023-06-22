---
title: Our product
description: Overview of the Giant Swarm cluster management product, the different generations and cloud provider implementations.
last_review_date: 2023-06-20
weight: 10
aliases:
menu:
  main:
    parent: platform-overview-cluster-management
    identifier: cluster-management-products
user_questions:
  - Which different products does Giant Swarm offer?
  - Which cloud providers are supported?
owner:
  - https://github.com/orgs/giantswarm/teams/area-kaas
---

## The Giant Swarm cluster management product

We offer _one_ cluster management product. It comes in different generations which are designed to be compatible with each other and integrate well with our [app platform]({{< relref "/platform-overview/app-platform" >}}). Our development focuses on the latest generation: cluster management based on the Kubernetes subproject [Cluster API (CAPI)]({{< relref "/platform-overview/cluster-management/cluster-api" >}}). We are planning and supporting the migration of customer clusters to this generation in the long term. The previous generation is called _Vintage_.

## Development state

Below, the provider-specific implementations are described in one of these states:

- **GA (General Availability)** – Stable and fully supported 24/7. Chance of breaking changes is very low and we maintain working upgrade paths between release versions.
- **Beta** – Working and supported, but we may still require more testing with live workloads. Breaking changes are still probable.
- **Alpha** – Mostly working and supported, but with missing features or major breaking changes outstanding.
- **In development** – Early phase development and not working yet. No 24/7 support.
- **Deprecated** – We are actively moving customers off this old implementation.

## Cluster API (CAPI) generation

This is the latest and recommended generation of our product.

The open-source cloud infrastructure providers of CAPI are separate projects (named CAPA for AWS cloud, CAPZ for Azure cloud, etc.). Since they mostly provide the cluster management logic and specification, we name our implementations after them.

For certain cloud providers, there are even different options available: for example with Amazon Web Services (AWS), we offer open source Kubernetes with the control plane running on EC2 instances, or use of AWS EKS for which the provider manages the control plane availability.

We offer the following cloud provider implementations:

- **CAPA (AWS EC2)** – _GA (general availability) expected soon (around 2023Q3)_
- **CAPA (AWS EKS)** – _in development_
- **CAPG (GCP VMs)** – _alpha_
- **CAPV (VMware vSphere)** – _alpha_
- **CAPVCD (VMware Cloud Director)** – _beta_
- **CAPZ (Azure VMs)** – _beta_

## Vintage generation

This is the previous generation of our product and is still in production with many of our customers. We still actively support this generation. However, the development focus is limited to main customer needs and supporting the migration to our CAPI-based implementations. For example, we introduced Cilium as the CNI (Kubernetes Container Network Interface) for both the CAPI-based and vintage generation in order to make the migration simple.

We offer the following cloud provider implementations:

- **Vintage (AWS)** – _GA (general availability)_
- **Vintage (Azure)** – _GA (general availability)_
- **Vintage (KVM)** – _deprecated and being phased out in 2023_

## How to choose the cloud provider and implementation

As new customer, the decision is usually based on the desired cloud provider (e.g. AWS) and development state of the implementation. Your contact and the team at Giant Swarm will work with you to make the right choice. We also clarify any potential customization with customers, such as specific network requirements or other requirements.

Once the decision for a cloud provider and implementation was made, we can [get you started]({{< relref "/getting-started" >}}) quickly.

Note that we also offer _proof of concept (PoC)_ projects in which we take 1-2 weeks to set up a reasonable and working prototype with you and present our platform capabilities. This also gives you a chance to witness our communication and [support model]({{< relref "/support" >}}) while we are in close contact, as we are with all existing customers.

Please use this per-provider overview for the implementation choice:

- **Cloud provider: AWS (Amazon Web Services)**

  Since we are close to GA state for our _CAPA (AWS EC2)_ implementation, we recommend starting with it instead of using _Vintage (AWS)_. This avoids a migration later on. We also support [private clusters]({{< relref "/advanced/private-clusters" >}}) with this implementation.

  If you prefer to switch to AWS EKS as control plane later, our platform is designed with high consistency in mind so that a migration would become easy.

- **Cloud provider: GCP (Google Cloud Platform)**

  The _CAPG (GCP VMs)_ implementation is the right one. It is currently not yet in GA state.

- **Cloud provider: Azure (Microsoft)**

  The _Vintage (Azure)_ implementation is the most stable at the moment.

  For new projects, we however recommend starting with _CAPZ (Azure VMs)_ since our focus is shifting to CAPI-based offerings. We also support [private clusters]({{< relref "/advanced/private-clusters" >}}) with this implementation.

  We may support Azure AKS in the future as well.

- **Cloud provider: VMware**

  VMware offers _vSphere_ and _Cloud Director_. Depending on which of their platforms you are using, our implementation is _CAPV (VMware vSphere)_ or _CAPVCD (VMware Cloud Director)_, respectively.
