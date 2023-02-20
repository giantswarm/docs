---
linkTitle: High-availability control plane
title: High-availability Kubernetes control plane
description: For production clusters with high availability requirements, Giant Swarm on AWS enables control planes with three control plane nodes and three etcd replicas spread over multiple availability zones.
weight: 10
last_review_date: 2021-06-07
menu:
  main:
    parent: advanced-highavailability
user_questions:
  - How can I maximize the availability of my cluster's API server?
  - Is there support for high-availability control planes on AWS?
  - Can I switch from a high-availability control plane to a single node control plane?
  - How can I switch a cluster to use a high-availability control plane?
aliases:
  - /basics/ha-masters/
  - /advanced/high-availability/masters/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

{{< platform_support_table aws="ga=v11.4.0" azure="roadmap=https://github.com/giantswarm/roadmap/issues/4" >}}

## Synopsis

Kubernetes control plane nodes are the nodes that run the Kubernetes API of a workload cluster,
as well as some other important components. In the case of Giant Swarm, the control plane nodes
also host the [etcd](https://etcd.io/) database that keeps all the states that configure
the cluster, the workloads, and other resources.

Clusters can run in a fully functional way with one control plane node. However this renders the
Kubernetes API unavailable in certain cases like a cluster upgrade or even an outage of
the underlying infrastructure.

As of workload cluster release v{{% first_aws_ha_controlplane_version %}} for AWS, new workload clusters are launched with three control plane nodes by default, spread over multiple availability zones. This results in much higher availability of the API during upgrades or other changes to the cluster configuration, plus enhanced resilience against any data center or hardware failures.

## Benefits

Having multiple control plane nodes in different availability zones has several benefits:

- **API downtimes during upgrades are reduced to a minimum**. With a single control plane node,
  upgrading the cluster requires only the control plane node to be terminated and rebooted with a new
  configuration. This results in several minutes of downtime. With multiple control plane nodes,
  the nodes get updated one at a time. The API can only become unreachable in the event
  that a new etcd leader has to be elected. This usually takes only a few seconds.
- **Resilience in case of infrastructure outages**. In the case of a failure of a single
  control plane node's EC2 instance, the two remaining control plane nodes take over and a replacement
  control plane node will be launched automatically. Running multiple control plane nodes of a cluster
  in different availability zones (AZ) also protects against
  the risk of losing control of the cluster in case of a single AZ downtime. Refer to
  [below](#use-of-az) for details.
- **Load balancing of API requests.** Read-only requests to the Kubernetes API are distributed over
  all three control plane nodes, so that latencies stay low in comparison to a single control plane
  node which can suffer from high loads temporarily.

We recommend that all production clusters on AWS are run with high-availability
control planes. As a result, this is the default setting starting with
workload cluster release v{{% first_aws_ha_controlplane_version %}}.

Since these benefits come at the cost of additional EC2 instances and
additional network traffic across availability zones, it is still possible to
create clusters with a single control plane node. This setting is viable for test
purposes or clusters which don't need high availability and resilience.

## Use of availability zones {#use-of-az}

When high-availability control plane is activated for a cluster, the three
control plane nodes are spread over different availability zones (AZ). Depending on
the number of AZs in the region, the logic is:

- In case of **three or more AZs** in the region, each control plane node is assigned to a different
  AZ, selected randomly.
- In case of **two AZs** in the region (as is the case in `cn-north-1`), both AZs get used.
  Two of the control plane nodes will share the same AZ.

When [converting a cluster with a single control plane node to high availability](#conversion-to-ha),
the AZ used by the control plane node before is re-used. Additional AZs are assigned
by applying the logic described above. Here, the AZ assignment of existing
worker [node pools]({{< relref "/advanced/node-pools" >}}) is taken into account.

## Upgrades from previous releases {#upgrades}

When upgrading a cluster to workload cluster release v11.4.0 or later, the cluster will still
only have one control plane node after the upgrade. The API unavailability during the
upgrade that is expected for a single control plane node will apply for this upgrade.

A conversion to high availability can be triggered after the upgrade is
complete.

## Conversion from a single control plane node to high availability {#conversion-to-ha}

Clusters using workload cluster release v{{% first_aws_ha_controlplane_version %}} or
above on AWS with a single control plane node can be converted via our user interfaces and APIs to run high-availability control planes.

### Via the web UI {#web-ui}

The web UI presents information on the control plane node in the cluster details page.
Next to these details you will find a button _Switch to high availability…_, unless
the cluster is currently undergoing an upgrade. Click this button and follow
the instructions in the web UI.

### Via `gsctl` {#gsctl}

The `gsctl` CLI as of v0.23.1 provides the
[gsctl update cluster]({{< relref "/use-the-api/gsctl/update-cluster" >}}) to change cluster details.
Check the reference for the `--master-ha` flag.

### Via the REST API {#rest-api}

Check the [v5 cluster modification API reference](/api/#operation/modifyClusterV5)
to find out how to convert a cluster programmatically using the Giant Swarm REST API.

### Via the Management API {#management-api}

In order to convert a single node control plane to high availability, the cluster's
[`G8sControlPlane`]({{< relref "/use-the-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io.md" >}})
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

The `.spec.replicas` attribute, which specifies the number of control plane nodes to
run, must be changed from 1 to 3.

For non-interactive patching:

```nohighlight
kubectl patch g8scontrolplanes.infrastructure.giantswarm.io <NAME> \
  --type merge -p '{"spec": {"replicas": 3}}
```

Once that is done, the operators will reconcile the desired state and create the
additional control plane nodes.

## Technical details

### Why three control plane nodes

At Giant Swarm we operate "stacked" clusters where etcd replicas run on the same machines
as the Kubernetes control plane nodes. Each control plane node runs control plane components and a member of
an etcd cluster.

In order to achieve high availability in an etcd cluster, a quorum (majority of members) is
needed. With three members, one member is allowed to become dysfunctional at any time, e. g.
through a machine failure or availability zone outage.

The number of three control plane nodes running three etcd members is a good balance between resilience
and cost. While it would be technically possible to run five or more control plane nodes, this
is not currently supported with Giant Swarm workload clusters.

## Limitations

- Currently only supported AWS. Not supported on Azure and KVM.
- Short API downtimes are still possible during cluster modifications, especially when the leader of the
  etcd cluster (the member that handles write requests) changes. This happens when the node that
  hosts the etcd leader has to be modified. Typical cases for this would be an upgrade to a newer
  workload cluster release or the conversion from a single to multiple control plane nodes. These downtimes are expected to
  last only a few seconds.
- Conversion of a cluster from high availability (three control plane nodes) to a single
  control plane node is not possible.
