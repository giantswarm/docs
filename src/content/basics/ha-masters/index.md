---
title: High availability Kubernetes masters
description: A general description of high availability of masters as a concept, it's benefits, and some details you should be aware of.
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
  upgrading the cluster requires the only master to be terminated and rebooted with new
  configuration, resulting in several minutes of downtime. With multiple master nodes,
  the nodes get update one at a time. The API can only become unreachable in the event
  that a new etcd leader has to be elected. This usually takes only a few seconds.
- **Resilience in case of infrastructure outages**. In the case of a failure of a single
  master node's EC2 instance, the two remaining master nodes take over and a replacement
  master node will be launched automatically. Since multiple master nodes of a cluster
  are running in different availability zones (AZ), this setting also protects against
  the risk of losing control over the cluster in the case of a single AZ downtime. Read
  [below](#use-of-az) for details.
- **Load balancing of API requests.** Read-only requests to the Kubernetes API are performed
  by all three master nodes, so that latencies stay lower overall compared to a single master
  node which can suffer from high loads temporarily.

We recommend that all productions clusters on AWS are run with high
availability of master nodes, hence this is the default setting starting with
release v{{% first_aws_ha_masters_version %}}.

Since these benefits come at the cost of additional EC2 instances and
additional network traffic across availability zones, it is still possible to
create clusters with a single master node. This setting is viable for test
purposes or clusters which don't need the high availability and resilience.

## Use of availability zones {#use-of-az}

When high availability master nodes is activated for a cluster, the three
master nodes are spread over different availability zones (AZ). Depending on
the number of AZ in the region, the logic is:

- With **three or more AZs** in the region, each master node is assigned to a different AZ, selected randomly.
- With **two AZs** in the region (as is the case in `cn-north-1`), both AZs get used. Two master nodes will share the same AZ.

When [converting a single master cluster to high availability](#conversion-to-ha),
the AZ used by the master node before is re-used. Additional AZs are assigned
by applying the logic described above. Here, the AZ assignment of existing
worker [node pools](/basic/nodepools/) is taken into account.

## Upgrades from previous releases {#upgrades}

When upgrading a cluster to release v11.4.0, the cluster will remain a single
master cluster during and after the upgrade. The API unavailability during the
upgrade that is typical for single master clusters will apply for this upgrade.

A conversion to high availability can be triggered after the upgrade is
finished.

## Conversion from single master to high availability {#conversion-to-ha}

Single master clusters using release v{{% first_aws_ha_masters_version %}} or
above on AWS can be converted to master node high availability in the user
interfaces and via the APIs.

## Via the web UI {#web-ui}

The web UI presents information on the master node in the cluster details page.
Next to these details you find a button _Switch to high availability…_, unless
the cluster is currently undergoing an upgrade. Click this button and follow
the instructions in the web UI.

## Via the CLI (`gsctl`) {#gsctl}

The `gsctl` CLI provides the [gsctl update cluster](/reference/gsctl/update-cluster/) to change cluster details. Check the reference for the `--master-ha` flag.

## Via the Rest API {#rest-api}

Check the [v5 cluster modification API reference](/api/#operation/modifyClusterV5) to find out how to convert a cluster programmatically using the Rest API.

## Via the Control Plane K8s API {#cp-k8s-api}

Two resources have to be changed in order to convert a single master cluster
to high availability.

1. `AWSControlPlane`
2. `G8sControlPlane`

### `AWSControlPlane`

The cluster's [`AWSControlPlane`](/reference/cp-k8s-api/awscontrolplanes.infrastructure.giantswarm.io/)
has a `.spec.availabilityZones` array which, in case of a single master
cluster, has only one item. This item is the availability zone assigned to the
only master node.

To convert the cluster to high availability, this array has to be extended
to have three items. Each item specifies the availability zone for one master
node after the conversion.

**CAUTION:** Order is important here. The first item must be left untouched. Or, in other words, what was the only array item before must be the first of three item after the change.

Example for a cluster in region `eu-central-1`:

The `AWSControlPlane` shows this spec (shortened):

```yaml
spec:
  availabilityZones:
  - eu-central-1c
```

The resource gets changed to this:

```yaml
spec:
  availabilityZones:
  - eu-central-1c
  - eu-central-1a
  - eu-central-1b
```

### `G8sControlPlane`

The [`G8sControlPlane`](/reference/cp-k8s-api/g8scontrolplanes.infrastructure.giantswarm.io/)
has a `.spec.replicas` attribute which indicates the number of master nodes to
run. This is `1` for a single master cluster and needs to be modified to `3`.

**Note:** Modifying the `G8sControlPlane` resource must happen _after_ the `AWSControlPlane`
modification in order to have full control over AZ usage. Otherwise the `AWSControlPlane` will
be modified automatically and AZs will be added by our automation. This may or may not
be your desired way.

## Technical details

### Why three master nodes

At Giant Swarm we operate "stacked" clusters where etcd nodes are running on the same machines
as the Kubernetes master nodes. Each master node runs control plane components and a member of
an etcd cluster.

In order to achieve high availability in an etcd cluster, a quorum (majority of members) is
needed. With three members, one member is allowed to become dysfunctional at any time, e. g.
through a machine failure or availability zone outage.

The number of three masters running three etcd members is a good balance between resilience
and cost. While it would be technically possible to run five or more master nodes, this
is not currently supported with Giant Swarm tenant clusters.

## Limitations

- Currently only supported AWS, not on Azure and KVM.
- Short API downtimes are still possible during cluster modifications, especially when the leader of the
  etcd cluster (the member that handles write requests) changes. This happens when the node that
  hosts the etcd leader has to be modified. Typical cases for this would be an upgrade to a newer
  release or the conversion from a single to multiple master nodes. These downtimes are expected to
  last only for a few seconds.
- Conversion of a cluster from high availability (three masters) to a single master node is not
  possible.
