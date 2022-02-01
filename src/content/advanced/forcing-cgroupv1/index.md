---
linkTitle: force nodes cgroup v1
title: Forcing nodes to use legacy Control Groups v1
description: This article describes how to force nodes to use legacy Control Groups v1 instead the default v2.
weight: 60
menu:
  main:
    parent: advanced
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---
# Forcing cgroups v1
{{< platform_support_table aws="beta=v17.0.0" azure="beta=v17.0.0" >}}

# Introduction
Flatcar version `3033.2.0` and above is by default using a Control Groups v2 which means all nodes using this version of Flatcar will be by default using cgroups v2 for all kubernetes containers. 

To ensure smooth transition and to give more time for migration, We introduced a configration, that will allow downgrading to legacy cgroup v1 for a specific node pool.


## Configure node pool with cgroup v1

### AWS

To enable it, you have to edit the [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/ui-api/management-api/" >}}).

Make sure the resource has the `node.giantswarm.io/cgroupv1` annotation. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: MachineDeployment
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io/
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

If you want to disable the feature you must remove the annotation from the [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) custom resource.

### Azure

To enable it, you have to edit the [`MachinePool`]({{< relref "/ui-api/management-api/crd/machinepools.exp.cluster.x-k8s.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/ui-api/management-api/" >}}).

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

If you want to disable the feature you must remove the annotation from the [`MachinePool`]({{< relref "/ui-api/management-api/crd/machinepools.exp.cluster.x-k8s.io.md" >}}) custom resource.
