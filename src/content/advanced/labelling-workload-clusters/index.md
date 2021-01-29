---
title: Labelling workload clusters
description: Introduction to labelling workload clusters
weight: 110
menu:
  main:
    parent: advanced
aliases:
  - /guides/tenant-cluster-labelling/
owner:
  - https://github.com/orgs/giantswarm/teams/team-ludacris
---

# Labelling workload clusters

{{< platform_support_table aws="ga=v10.0.0" azure="ga=v13.0.0" >}}

## Introduction

It is possible to assign *key value labels* to Giant Swarm workload clusters with workload cluster release v{{% first_aws_nodepools_version %}} and above on AWS.

Labels are a mechanism to assign short pieces of additional information to your Giant Swarm workload clusters.
Under the hood, workload cluster labels are Kubernetes labels attached to [`Cluster`](/reference/management-api/clusters.cluster.x-k8s.io/) (`clusters.cluster.x-k8s.io`) resources.
Therefore, all means of listing workload cluster labels will return all Kubernetes labels attached to [`Cluster`](/reference/management-api/clusters.cluster.x-k8s.io/) resources requested.
Label keys and values are freely modifiable except labels with keys containing `giantswarm.io`.

Working with workload cluster labels works likewise as working with Kubernetes labels.
More information about Kubernetes Labels can be found in the [Kubernetes Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and our [cluster labels API documentation](/api/#tag/cluster-labels).

Note: You can also [manage cluster labels directly through `happa`](/reference/web-interface/workload-cluster-labelling/), our web user interface.

## Working with workload cluster labels using `gsctl`

With `gsctl`, our [CLI](https://github.com/giantswarm/gsctl), cluster labels can be modified by executing [`gsctl update cluster`]({{< relref "/ui-api/gsctl/update-cluster" >}}) by setting label changes using one or multiple `--label` flag.

Deleting a label can be accomplished by setting its value to an empty string. `--label labeltodelete=`.

```nohighlight
$ gsctl update cluster 7g4di --label my-org/team=upstate --label my-org/environment=testing
Cluster '7g4di' has been modified.
New cluster labels:
my-org/environment=testing
my-org/team=upstate
```

Once clusters are labelled, the output of [`gsctl list clusters`]({{< relref "/ui-api/gsctl/list-clusters" >}}) can be augmented by setting flag `--selector` (or `-l`)
It takes a [Kubernetes Label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) to specify requirements on cluster labels to select.

The output of [`gsctl show cluster`]({{< relref "/ui-api/gsctl/show-cluster" >}}) will contain all labels currently attached to the selected cluster.

## Working with workload cluster labels using the Giant Swarm API

Workload cluster labels of clusters with workload cluster release v{{% first_aws_nodepools_version %}} and above for AWS are returned by executing a [getClusters](/api/#operation/getClusters) request.
The field `labels` of suitable workload clusters contains the labels currently attached to the cluster.
Labels of a single workload cluster can be retrieved using the [getClusterLabels](/api/#operation/getClusterLabels) endpoint.

Selecting workload clusters based on a set of labels can be achieved through the [getV5ClustersByLabel](/api/#operation/getV5ClustersByLabel) operation.
The operation accepts label selectors in the same way that `kubectl get -l` does ([Kubernetes Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)) for listing clusters based on their labels.

The labels of a workload cluster can be modified by issuing a [setClusterLabels](/api/#operation/setClusterLabels) request to the API.
Keys and labels should adhere to [Kubernetes labels syntax and character set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
Label changes should be written as a [JSON Merge Patch, RFC 7386](https://tools.ietf.org/html/rfc7386).
Changes to labels with keys containing `giantswarm.io` is forbidden, changes to label `release.giantswarm.io/version` will be validated against available workload cluster releases.

Differing from `gsctl`, listing workload cluster labels with the API will show management labels required for operation.
These usually contain `giantswarm.io` in its label keys and cannot be changed.

### Example

Let's play through a simple workflow of assigning labels to a newly created workload cluster and selecting it based on the given label.

For brevity authentication and unrelated parts of requests and responses are left out.

After creation, a workload cluster will already have some labels containing information about the workload cluster release and operator version.

```json
GET /v5/clusters/7g4di
{
  "api_endpoint": "...",
  "create_date": "...",
  "id": "7g4di",
  "master": {...},
  "name": "...",
  "owner": "my-org",
  "release_version": "11.2.0",
  "conditions": [...],
  "labels": {
    "cluster-operator.giantswarm.io/version": "2.1.9",
    "giantswarm.io/cluster": "7g4di",
    "giantswarm.io/organization": "my-org",
    "release.giantswarm.io/version": "11.2.0"
  }
}
```

In our example, the cluster `7g4di` already has four labels (`cluster-operator.giantswarm.io/version`, `giantswarm.io/cluster`, `giantswarm.io/organization`, `release.giantswarm.io/version`).

The newly created cluster will be managed by your team in your upstate office and is planned to be used for testing purposes.

You've decided on using label keys `my-org/team` and `my-org/environment` to specify the clusters designation.

```json
PUT /v5/clusters/7g4di/labels/
{
  "labels": {
    "my-org/team": "upstate",
    "my-org/environment": "testing"
  }
}
```

Another cluster from earlier is also managed by your team in the upstate office but is being used for production.

```json
PUT /v5/clusters/g8s2o/labels/
{
  "labels": {
    "my-org/team": "upstate",
    "my-org/environment": "production"
  }
}
```

From this point on it is possible to select the clusters by label values or label key existence.

```json
POST /v5/clusters/by_label/
{
  "labels": "my-org/team=upstate"
}
```

will return all clusters managed by the upstate office team regardless of other label values.

The full documentation about label selectors can be found on the [Kubernetes Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) page.

## Working with workload cluster labels using `kubectl`

With access to the management cluster, you are able to use `kubectl` to manage workload cluster labels.
The underlying resource to operate on is [`clusters.cluster.x-k8s.io`](/reference/management-api/clusters.cluster.x-k8s.io/) from the upstream [cluster-api](https://cluster-api.sigs.k8s.io/) project.

Detailed documentation and examples of `kubectl label` and other commands used here can be found in the [Kubectl Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands).

### Modify workload cluster labels

All means of modifying cluster resources can be used to modify labels of a `clusters.cluster.x-k8s.io` resource.

Interactively, cluster labels can be modified using `kubectl edit`. Just edit the `metadata.labels` property.

```nohighlight
kubectl edit clusters.cluster.x-k8s.io/7g4di
```

It is also possible to modify workload cluster labels with `kubectl patch`.
More information about `kubectl patch` is available on the [Update API Objects in Place Using kubectl patch](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/) page.

```nohighlight
kubectl patch clusters.cluster.x-k8s.io/7g4di --type merge -p '{"metadata":{"labels":{"my-org/team":"upstate"}}}'
```

Additionally, [`kubectl label`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label) can be used to modify workload cluster labels.

```nohighlight
kubectl label clusters.cluster.x-k8s.io/7g4di my-org/team=upstate
```

### Show workload cluster labels

Differing from `gsctl`, listing workload cluster labels with `kubectl` will show management labels required for operation. These usually contain `giantswarm.io` in its label keys and cannot be changed.

Labels of all workload clusters:

```nohighlight
$ kubectl labels --list --all clusters.cluster.x-k8s.io
Listing labels for Cluster.cluster.x-k8s.io/7g4di:
 giantswarm.io/cluster=7g4di
 giantswarm.io/organization=my-org
 release.giantswarm.io/version=11.2.0
 cluster-operator.giantswarm.io/version=2.1.9
 my-org/team=upstate
 my-org/environment=testing
Listing labels for Cluster.cluster.x-k8s.io/zv86a:
 cluster-operator.giantswarm.io/version=2.1.9
 giantswarm.io/cluster=q84ct
 giantswarm.io/organization=my-org
 release.giantswarm.io/version=11.3.0
 my-org/team=upstate
 my-org/environment=production
```

Labels of a single workload cluster:

```nohighlight
$ kubectl labels --list clusters.cluster.x-k8s.io/7g4di
giantswarm.io/cluster=7g4di
giantswarm.io/organization=my-org
release.giantswarm.io/version=11.2.0
cluster-operator.giantswarm.io/version=2.1.9
my-org/team=upstate
my-org/environment=testing
```

### Select workload clusters by label selector

Many `kubectl` commands support the `-l, --selector` flag, which allows to limit the selected resources based on given [Kubernetes Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors).

```nohighlight
kubectl get clusters.cluster.x-k8s.io -l 'my-org/team=upstate'
```
