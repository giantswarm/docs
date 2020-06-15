---
title: High availability Kubernetes masters
description: A general description of node pools as a concept, it's benefits, and some details you should be aware of.
date: 2020-05-16
weight: 120
type: page
categories: ["basics"]
---

# High availability Kubernetes masters

Intro:
- since version v11.4.0 on AWS it's the default
- HA means three

## Benefits

- Less/short downtimes during upgrades and updates/changes
- Resilience in case of datacenter outages
- Load balancing of K8s API requests (except for writes) should lead to lower latency
- Clusters can be created with only 1 master, later converted to high availability

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

## Limitations

- API downtimes possible
  - switch from 1 to 3
  - rolling master nodes, e. g. to switch the instance type
  - etcd leader change (to be confirmed)
- Conversion from high availability (3 masters) to a single master node is not possible.
