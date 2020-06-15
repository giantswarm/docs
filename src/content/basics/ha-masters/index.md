---
title: High availability Kubernetes masters
description: A general description of node pools as a concept, it's benefits, and some details you should be aware of.
date: 2020-05-16
weight: 120
type: page
categories: ["basics"]
---

# High availability Kubernetes masters

## Synopsis

Kubernetes master nodes are the nodes that run the Kubernetes API of a tenant cluster,
as well as some other important components. In the case of Giant Swarm, the master nodes
also host the [etcd](https://etcd.io/) database that keeps all the state that configures
the cluster, the workloads and other resources.

Clusters can run in a fully functional way with one master node, however this renders the
Kubernetes API unavailable in certain cases like a cluster upgrade or even an outage of
the underlying infrastructure.

With AWS release v{{% first_aws_ha_masters_version %}} new tenant clusters are launched
with three master nodes in different availability zones by default, increasing the API
availability during upgrades and cluster changes drastically and making the cluster more
resilient against data center failure.

## Benefits

Multiple master nodes in different availability zones has several benefits:

- **API downtimes during upgrades are reduced to a minimum**. With a single master node,
  upgrading the cluster requires the only master to be terminated and rebooted with new configuration, resulting in several minutes of downtime. With multiple master nodes, the nodes get update one at a time. The API can only become unreachable in the event that a new etcd leader has to be elected. This usually takes only a few seconds.
- **Resilience in case of infrastructure outages**. In the case of a failure of a single
  master node's EC2 instance, the two remaining master nodes take over and a replacement
  master node will be launched automatically. Since multiple master nodes of a cluster are running in different availability zones (AZ), this setting also protects against the risk of losing control over the cluster in the case of a single AZ downtime.
- **Load balancing of API requests.** Read-only requests to the Kubernetes API are performed
  by all three master nodes, so that latencies stay lower overall compared to a single master
  node which can suffer from high loads temporarily.

We recommend that all productions clusters on AWS are run with high availability of master nodes, hence this is the default setting starting with release v{{% first_aws_ha_masters_version %}}.

Since these benefits come at the cost of additional EC2 instances and additional network traffic across availability zones, it is still possible to create clusters with a single master node. This setting is viable for test purposes or clusters which don't need the high availability and resilience.

## Use of availability zones

- Where available, each of the 3 master nodes uses a separate AZ
  - Regions with only 2 AZs (e. g. `cn-north-1`): One AZ gets two masters, the other one gets one master
- Where more than three AZs, selection is random.
- When switching from 1 to 3 masters, the previously used AZ of the existing master node is used. Two additional AZs are added randomly for the added master nodes.

## Upgrades from earlier releases

When upgrading a cluster to release v11.4.0, it will keep the single master node it had. A conversion to high availability can be triggered manually later.

## Conversion from single master to high availability

- Possible in happa, gsctl, and via the Rest API
- Happa how to
- [gsctl update cluster](/reference/gsctl/update-cluster/) with the `--master-ha` flag
- API link

## Technical details

- Why three master nodes?

At Giantswarm we operate stacked HA clusters where etcd is stacked on top of our master nodes. 
Each master node runs control-plane and a local etcd member. Enabling HA master needs to have a quorum 
(majority of nodes) meaning running at least 3 master nodes. By enabling HA a master node can be down 
in case of a failing instance or a AZ outage without affecting cluster operations.

## Limitations

- Currently not supported on Azure and KVM.
- API downtimes possible
  - switch from 1 to 3
  - rolling master nodes, e. g. to switch the instance type
  - etcd leader change (to be confirmed)
- Conversion from high availability (3 masters) to a single master node is not possible.
