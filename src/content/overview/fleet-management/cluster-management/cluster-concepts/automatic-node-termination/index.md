---
linkTitle: Automatic node termination
title: Automatic termination of unhealthy nodes
description: Unhealthy cluster nodes can lead to impaired workload reliability and wasted cluster resources. Here we explain how you can activate automatic termination of such nodes.
weight: 60
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement-concepts
    identifier: overview-fleetmanagement-clustermanagement-concepts-node-termination
user_questions:
  - How are unhealthy worker nodes treated?
last_review_date: 2025-07-14
aliases:
  - /advanced/cluster-management/automatic-node-termination
  - /basics/automatic-termination-of-bad-nodes/
  - /guides/automatic-node-termination/
  - /advanced/automatic-node-termination/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

Degraded nodes in a Kubernetes cluster should be a rare issue, however when it occurs, it can have severe consequences for the workloads scheduled to the affected nodes. The goal should be to detect bad nodes early and remove them from the cluster, replacing them with healthy ones.

## Technical details

The node's health status is used to determine if a node needs to be terminated. A node reporting a `Ready` status is considered healthy. If a node reports an unhealthy status continuously for a given time threshold it will be recycled.

An unhealthy status means the `kubelet` on a given node has reported `NotReady` status on consecutive checks (approximately every 2-3 minutes)  over a certain time threshold (approximately 15 minutes).

### AWS

For tuning the behavior of automatic node termination on AWS, you can configure your cluster `App` with these values:

- `global.apps.awsNodeTerminationHandler`: (**App resource**, object) Configuration of a default app that is part of the cluster and is deployed as an App resource.
- `global.apps.awsNodeTerminationHandler.extraConfigs`: (**Extra config maps or secrets**, array) Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.
- `global.apps.awsNodeTerminationHandler.extraConfigs[*]`: (**Config map or secret**, object)
- `global.apps.awsNodeTerminationHandler.extraConfigs[*].kind`: (**Kind**, string) Specifies whether the resource is a config map or a secret.
- `global.apps.awsNodeTerminationHandler.extraConfigs[*].name`: (**Name**, string) Name of the config map or secret. The object must exist in the same namespace as the cluster App.
- `global.apps.awsNodeTerminationHandler.extraConfigs[*].priority`: (**Priority**, integer, default: `25`)
- `global.apps.awsNodeTerminationHandler.values`: (**Config map**, object) Helm Values to be passed to the app as user config.

### Azure

To enable automatic termination of unhealthy nodes, edit the [`Cluster`](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/cluster.x-k8s.io/Cluster/v1beta1) resource of your cluster using the Management API.

Make sure the resource has the `alpha.node.giantswarm.io/terminate-unhealthy` annotation. The value can be anything you like, as just the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:
    alpha.node.giantswarm.io/terminate-unhealthy: "true"
  name: fn7t8
  namespace: org-giantswarm
spec:
  ...
```

If you want to disable the feature you must remove the annotation from the [`Cluster`](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/cluster.x-k8s.io/Cluster/v1beta1) custom resource.
