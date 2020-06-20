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
  the nodes get updated one at a time. The API can only become unreachable in the event
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

We recommend that all production clusters on AWS are run with high
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

- With **three or more AZs** in the region, each master node is assigned to a different
  AZ, selected randomly.
- With **two AZs** in the region (as is the case in `cn-north-1`), both AZs get used.
  Two master nodes will share the same AZ.

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

### Via the web UI {#web-ui}

The web UI presents information on the master node in the cluster details page.
Next to these details you find a button _Switch to high availability…_, unless
the cluster is currently undergoing an upgrade. Click this button and follow
the instructions in the web UI.

### Via the CLI (`gsctl`) {#gsctl}

The `gsctl` CLI as of v0.23.1 provides the
[gsctl update cluster](/reference/gsctl/update-cluster/) to change cluster details.
Check the reference for the `--master-ha` flag.

### Via the Rest API {#rest-api}

Check the [v5 cluster modification API reference](/api/#operation/modifyClusterV5)
to find out how to convert a cluster programmatically using the Rest API.

### Via the Control Plane K8s API {#cp-k8s-api}

In order to convert a single master cluster to high availability, the cluster's
[`G8sControlPlane`](/reference/cp-k8s-api/g8scontrolplanes.infrastructure.giantswarm.io/)
has to be modified. First you have to find the resource for your cluster ID. The
following command helps with that:

```nohighlight
kubectl get g8scontrolplanes.infrastructure.giantswarm.io \
  -l giantswarm.io/cluster=<CLUSTER_ID>
```

As a result, you should find one `G8sControlPlane` with the name showing in the
first output column. Use that name in the `kubectl edit` command, or a
`kubectl patch` command alternatively. For interactive editing:

```nohighlight
kubectl edit g8scontrolplanes.infrastructure.giantswarm.io <NAME>
```

The `.spec.replicas` attribute, which specifies the number of master nodes to
run, must be changed from 1 to 3.

For non-interactive patching:

```nohighlight
kubectl patch g8scontrolplanes.infrastructure.giantswarm.io <NAME> \
  --type merge -p '{"spec": {"replicas": 3}}
```

Once that is done, the operators will reconcile the desired state and create the
additional master nodes.

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
