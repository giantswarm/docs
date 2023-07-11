---
linkTitle: Use cgroups v1
title: Forcing nodes to use legacy control croups (cgroups) v1
description: This article describes how to force nodes to use legacy control groups (cgroups) v1 instead of the default v2.
weight: 60
menu:
  main:
    parent: advanced
user_questions:
 -  How can I enable cgroupsv1?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-04-04
---

{{< platform_support_table aws="beta=v17.0.0" azure="beta=v17.0.0" >}}

Flatcar version `3033.2.0` and above uses control groups (cgroups) v2 by default, which means all nodes will be using cgroups v2 for all containers in Kubernetes, as opposed to cgroups v1 used on previous versions.

To ensure a smooth transition, in case you need time to modify applications to make them compatible with cgroups v2, we provide a mechanism that will allow using cgroups v1 on specific node pools.

## Configure node pool with cgroup v1

### AWS

To enable cgroups v1, you have to edit the [`MachineDeployment`]({{< relref "/use-the-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/use-the-api/management-api/" >}}).

Make sure the resource has the `node.giantswarm.io/cgroupv1` annotation. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: MachineDeployment
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/machinedeployments.cluster.x-k8s.io/
    node.giantswarm.io/cgroupv1: ""
  labels:
    cluster.x-k8s.io/cluster-name: abcd1
    giantswarm.io/cluster: abcd1
    giantswarm.io/machine-deployment: u6gw3
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 17.0.0
  name: u6gw3
  namespace: org-giantswarm
spec:
  ...
```

Alternatively you can use `kubectl` command to annotate the CR like shown below:

```yaml
kubectl annotate machinedeployments.cluster.x-k8s.io u6gw3 node.giantswarm.io/cgroupv1=""
```

In order to apply the changes, rolling of the nodes in the modified node pool is required. Rolling of the nodes can be triggered either by an update or by manually by terminating each node.

We recommend to set the proper annotation on the node pool before upgrading to release `v17.0.0` or later.

If you want to disable the feature you must remove the annotation from the [`MachineDeployment`]({{< relref "/use-the-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) resource.

### Azure

To enable cgroups v1, you have to edit the [`MachinePool`]({{< relref "/use-the-api/management-api/crd/machinepools.exp.cluster.x-k8s.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/use-the-api/management-api/" >}}).

Make sure the resource has the `node.giantswarm.io/cgroupv1` annotation. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: exp.cluster.x-k8s.io/v1alpha3
kind: MachinePool
metadata:
  annotations:
    cluster.k8s.io/cluster-api-autoscaler-node-group-max-size: "2"
    cluster.k8s.io/cluster-api-autoscaler-node-group-min-size: "2"
    machine-pool.giantswarm.io/name: vaclav-cluster-xacl9-2
    node.giantswarm.io/cgroupv1: ""
  creationTimestamp: null
  labels:
    cluster.x-k8s.io/cluster-name: xacl9
    giantswarm.io/cluster: xacl9
    giantswarm.io/machine-pool: f8ak0
    giantswarm.io/organization: giantswarm
  name: f8ak0
  namespace: org-giantswarm
spec:
  ...
```

Or you can use the `kubectl` command to annotate the CR.

```yaml
kubectl annotate machinepools.exp.cluster.x-k8s.io f8ak0 node.giantswarm.io/cgroupv1=""
```

In order to apply the changes, rolling of the nodes in the modified node pool is required. Rolling of the nodes can be triggered either by an update or by manually by terminating each node.

We recommend to set the proper annotation on the node pool before updating to the release `17.0.0` or later.

If you want to disable the feature you must remove the annotation from the [`MachinePool`]({{< relref "/use-the-api/management-api/crd/machinepools.exp.cluster.x-k8s.io.md" >}}) custom resource.
