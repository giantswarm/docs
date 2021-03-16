---
linkTitle: High-availability masters
title: High-availability Kubernetes masters
description: A general description of high availability of masters as a concept, it's benefits, and some details you should be aware of.
weight: 10
menu:
  main:
    parent: advanced-highavailability
aliases:
  - /basics/ha-masters/
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# High-availability Kubernetes masters

{{< platform_support_table aws="ga=v11.4.0" azure="roadmap=https://github.com/giantswarm/roadmap/issues/4" >}}

## Synopsis

Kubernetes master nodes are the nodes that run the Kubernetes API of a workload cluster,
as well as some other important components. In the case of Giant Swarm, the master nodes
also host the [etcd](https://etcd.io/) database that keeps all the states that configure
the cluster, the workloads and other resources.

Clusters can run in a fully functional way with one master node. However this renders the
Kubernetes API unavailable in certain cases like a cluster upgrade or even an outage of
the underlying infrastructure.

As of workload cluster release v{{% first_aws_ha_masters_version %}} for AWS, new workload clusters are launched with three master nodes by default, spread over multiple availability zones. This results in much higher availability of the API during upgrades or other changes to the cluster configuration, plus enhanced resilience against any data center or hardware failures.

## Benefits

Having multiple master nodes in different availability zones has several benefits:

- **API downtimes during upgrades are reduced to a minimum**. With a single master node,
  upgrading the cluster requires the only master to be terminated and rebooted with new
  configuration. This results in several minutes of downtime. With multiple master nodes,
  the nodes get updated one at a time. The API can only become unreachable in the event
  that a new etcd leader has to be elected. This usually takes only a few seconds.
- **Resilience in case of infrastructure outages**. In the case of a failure of a single
  master node's EC2 instance, the two remaining master nodes take over and a replacement
  master node will be launched automatically. Running multiple master nodes of a cluster
  in different availability zones (AZ), also protects against
  the risk of losing control of the cluster in case of a single AZ downtime. Refer to
  [below](#use-of-az) for details.
- **Load balancing of API requests.** Read-only requests to the Kubernetes API are performed
  by all three master nodes, so that latencies stay low in comparison to a single master
  node which can suffer from high loads temporarily.

We recommend that all production clusters on AWS are run with high
availability of master nodes. As a result, this is the default setting starting with
workload cluster release v{{% first_aws_ha_masters_version %}}.

Since these benefits come at the cost of additional EC2 instances and
additional network traffic across availability zones, it is still possible to
create clusters with a single master node. This setting is viable for test
purposes or clusters which don't need high availability and resilience.

## Use of availability zones {#use-of-az}

When high-availability master nodes is activated for a cluster, the three
master nodes are spread over different availability zones (AZ). Depending on
the number of AZs in the region, the logic is:

- In case of **three or more AZs** in the region, each master node is assigned to a different
  AZ, selected randomly.
- In case of **two AZs** in the region (as is the case in `cn-north-1`), both AZs get used.
  Two of the master nodes will share the same AZ.

When [converting a single master cluster to high availability](#conversion-to-ha),
the AZ used by the master node before is re-used. Additional AZs are assigned
by applying the logic described above. Here, the AZ assignment of existing
worker [node pools]({{< relref "/advanced/node-pools" >}}) is taken into account.

## Upgrades from previous releases {#upgrades}

When upgrading a cluster to workload cluster release v11.4.0, the cluster will remain a single
master cluster during and after the upgrade. The API unavailability during the
upgrade that is typical for single master clusters will apply for this upgrade.

A conversion to high availability can be triggered after the upgrade is
complete.

## Conversion from single master to high availability {#conversion-to-ha}

Single master clusters using workload cluster release v{{% first_aws_ha_masters_version %}} or
above on AWS can be converted to master node high availability in the user
interfaces and via the APIs.

### Via the web UI {#web-ui}

The web UI presents information on the master node in the cluster details page.
Next to these details you will find a button _Switch to high availability…_, unless
the cluster is currently undergoing an upgrade. Click this button and follow
the instructions in the web UI.

### Via the CLI (`gsctl`) {#gsctl}

The `gsctl` CLI as of v0.23.1 provides the
[gsctl update cluster]({{< relref "/ui-api/gsctl/update-cluster" >}}) to change cluster details.
Check the reference for the `--master-ha` flag.

### Via the REST API {#rest-api}

Check the [v5 cluster modification API reference](/api/#operation/modifyClusterV5)
to find out how to convert a cluster programmatically using the Giant Swarm REST API.

### Via the Management API {#management-api}

In order to convert a single master cluster to high availability, the cluster's
[`G8sControlPlane`]({{< relref "/ui-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io.md" >}})
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

At Giant Swarm we operate "stacked" clusters where etcd nodes run on the same machines
as the Kubernetes master nodes. Each master node runs control plane components and a member of
an etcd cluster.

In order to achieve high availability in an etcd cluster, a quorum (majority of members) is
needed. With three members, one member is allowed to become dysfunctional at any time, e. g.
through a machine failure or availability zone outage.

The number of three masters running three etcd members is a good balance between resilience
and cost. While it would be technically possible to run five or more master nodes, this
is not currently supported with Giant Swarm workload clusters.

## Limitations

- Currently only supported AWS. Not supported on Azure and KVM.
- Short API downtimes are still possible during cluster modifications, especially when the leader of the
  etcd cluster (the member that handles write requests) changes. This happens when the node that
  hosts the etcd leader has to be modified. Typical cases for this would be an upgrade to a newer
  workload cluster release or the conversion from a single to multiple master nodes. These downtimes are expected to
  last only a few seconds.
- Conversion of a cluster from high availability (three masters) to a single master node is not
  possible.
