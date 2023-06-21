---
title: Our products
description: Overview of Giant Swarm cluster management products.
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

## Product families

We have two _product families_: _Cluster API (CAPI)_ based and _vintage_ products.

## Development state

Below, products are described in one of these states:

- **GA (General Availability)** – Stable and fully supported 24/7. Chance of breaking changes is low.
- **Beta** – Working and supported, but we may still require more testing with live workloads. Breaking changes are still probable.
- **Alpha** – Mostly working and supported, but with missing features or major breaking changes outstanding.
- **In development** – Early phase development and not working yet. No 24/7 support.

## Cluster API (CAPI) products

We started development of cluster management based on the Kubernetes subproject [Cluster API (CAPI)](https://github.com/kubernetes-sigs/cluster-api) in 2021 and support multiple cloud providers by now. We are planning to migrate customer clusters to these products in the long term.

Cloud infrastructure providers for CAPI are separate open source projects (named CAPA for AWS cloud, CAPZ for Azure cloud, etc.). Since they mostly provide the cluster management logic and specification, we call our products after them.

For certain cloud providers, there are even different options available: for example with Amazon Web Services (AWS), we offer open source Kubernetes with the control plane running on EC2 instances, or use of AWS EKS for which the provider manages the control plane availability.

- **CAPA (AWS EC2)** – _GA (general availability) i.e. stable state expected soon (around 2023Q3)_
- **CAPA (AWS EKS)** – _in development_
- **CAPG (GCP VMs)** – _alpha_
- **CAPZ (Azure VMs)** – _beta_

## Vintage products

These products are live with most of our customers, and we still actively support them. The development focus is on main customer needs and migration to our CAPI-based products. For example, we introduced Cilium as the CNI for both product families such that the migration becomes easier.

- **Vintage (AWS)** – _GA (general availability)_
- **Vintage (Azure)** – _GA (general availability)_
- **Vintage (KVM)** – _GA (general availability)_

## How to choose

As new customer, you should take the decision based on the cloud provider, development state (stability) of our offered product and how soon you want to go live with your workloads (business applications).

- **Cloud provider: AWS (Amazon Web Services)**

  Since we are close to GA state for our _CAPA (AWS EC2)_ product, we recommend starting with it instead of using _Vintage (AWS)_. This avoids a migration later on.

  If you prefer to switch to AWS EKS as control plane later, our platform is designed with high consistency in mind so that a migration would become easy.

- **Cloud provider: GCP (Google Cloud Platform)**

  The _CAPG (GCP VMs)_ product is the right one. It is currently not yet in GA state.

- **Cloud provider: Azure (Microsoft)**

  The _Vintage (Azure)_ product is the most stable at the moment.

  For new projects, we however recommend starting with _CAPZ (Azure VMs)_ since our focus is shifting to CAPI-based offerings.

  We may support Azure AKS in the future as well.

- **On-premises (own datacenter)**

  The _Vintage (KVM)_ product is the right one.

We also offer _proof of concepts (PoC)_ in which we take 1-2 weeks to start a reasonable and working prototype with you. This also gives you a chance to witness our communication and support model while we are in close contact with you, as we are with all existing customers.
