---
title: "Labelling tenant clusters"
description: "Introduction to labelling tenant clusters"
date: "2020-04-27"
type: page
weight: 130
tags: ["recipe"]
---

# Labelling tenant clusters

It is possible to assign *key value labels* to Giant Swarm tenant clusters on AWS with release version 10.0.0 and above.

Labels are a mechanism to assign short pieces of additional information to your Giant Swarm tenant clusters.
Under the hood, tenant cluster labels are Kubernetes labels attached to [`Cluster`](https://github.com/kubernetes-sigs/cluster-api/blob/master/config/crd/bases/cluster.x-k8s.io_clusters.yaml) (`clusters.cluster.x-k8s.io`) resources.
Therefore, all means of listing tenant cluster labels will return all Kubernetes labels attached to [`Cluster`](https://github.com/kubernetes-sigs/cluster-api/blob/master/config/crd/bases/cluster.x-k8s.io_clusters.yaml) resources requested.
Label keys and values are freely modifiable except labels with keys containing `giantswarm.io`.

Working with tenant cluster labels works likewise as working with Kubernetes labels.
More information about Kubernetes Labels can be found in the [Kubernetes Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[getClusters](/api/#operation/getClusters) documentation.

## Working with tenant cluster labels using the Giant Swarm API

Tenant cluster labels of clusters with release version 10.0.0 and above are returned by executing a [getClusters] request.
The field `labels` of suitable tenant clusters contains the labels currently attached to the cluster.

Selecting tenant clusters based on a set of labels can be achieved through the [getV5ClustersByLabel](/api/#operation/getV5ClustersByLabel) operation.
The operation accepts label selectors in the same way that `kubectl get -l` does ([Kubernetes Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)) for listing clusters based on their labels.

The labels of a tenant cluster can be modified by issuing a [setClusterLabels](/api/#operation/setClusterLabels) request to the API.
Keys and labels should adhere to [Kubernetes labels syntax and character set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
Label changes should be written as a [JSON Merge Patch, RFC 7386](https://tools.ietf.org/html/rfc7386).
Changes to labels with keys containing `giantswarm.io` is forbidden, changes to label `release.giantswarm.io/version` will be validated against available Giant Swarm releases.

### Example

Let's play through a simple workflow of assigning labels to a newly created tenant cluster and selecting it based on the given label.

For brevity authentication and unrelated parts of requests and responses are left out.

After creation, a tenant cluster will already have some labels containing information about release and operator.

```json
GET /v5/clusters/7g4di
{
  "api_endpoint": "...",
  "create_date": "...",
  "id": "7g4di",
  "master": {...},
  "name": "...",
  "owner": "your-org",
  "release_version": "11.2.0",
  "conditions": [...],
  "labels": {
    "cluster-operator.giantswarm.io/version": "2.1.9",
    "giantswarm.io/cluster": "7g4di",
    "giantswarm.io/organization": "your-org",
    "release.giantswarm.io/version": "11.2.0"
  }
}
```

In our example, the cluster `7g4di` already has four labels (`cluster-operator.giantswarm.io/version`, `giantswarm.io/cluster`, `giantswarm.io/organization`, `release.giantswarm.io/version`).

The newly created cluster will be managed by your team in your upstate office and is planned to be used for testing purposes.

You've decided on using label keys `your-org/team` and `your-org/environment` to specify the clusters designation.

```json
PUT /v5/clusters/7g4di/labels/
{
  "labels": {
    "your-org/team": "upstate",
    "your-org/environment": "testing"
  }
}
```

Another cluster from earlier is also managed by your team in the upstate office but is being used for production.

```json
PUT /v5/clusters/g8s2o/labels/
{
  "labels": {
    "your-org/team": "upstate",
    "your-org/environment": "production"
  }
}
```

From this point on it is possible to select the clusters by label values or label key existence.

```json
POST /v5/clusters/by_label/
{
  "labels": "your-org/team=upstate"
}
```

Will return all clusters managed by the upstate office team regardless of other label values.

The full documentation about label selectors can be found on the [Kubernetes Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[getClusters](/api/#operation/getClusters) page.

## Working with tenant cluster labels using `kubectl`

With access to the control plane, you are able to use `kubectl` to manage tenant cluster labels.
The underlying resource to operate on is `clusters.cluster.x-k8s.io` from the upstream [cluster-api](https://cluster-api.sigs.k8s.io/) project.

### Modify tenant cluster labels

All means of modifying cluster resouces can be used to modify labels of a `clusters.cluster.x-k8s.io` resource.

Interactively, cluster labels can be modifed using `kubectl edit`. Just edit the `metadata.labels` property.

```nohighlight
$ kubectl edit clusters.cluster.x-k8s.io/7g4di
```

It is also possible to modify tenant cluster labels with `kubectl patch`.
More information about `kubectl patch` is available on the [Update API Objects in Place Using kubectl patch](https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/) page.

```nohighlight
$ kubectl patch clusters.cluster.x-k8s.io/7g4di --type merge -p '{"metadata":{"labels":{"your-org/team":"upstate"}}}'
```

### Show tenant cluster labels

Labels of all tenant clusters:

```nohighlight
$ kubectl get --show-labels=true clusters.cluster.x-k8s.io
NAME    AGE   LABELS
7g4di   60m   cluster-operator.giantswarm.io/version=2.1.9,giantswarm.io/cluster=7g4di,giantswarm.io/organization=my-org,release.giantswarm.io/version=11.2.0,your-org/team=upstate,your-org/environment=testing
q84ct   63m   cluster-operator.giantswarm.io/version=2.1.9,giantswarm.io/cluster=q84ct,giantswarm.io/organization=my-org,release.giantswarm.io/version=11.3.0,your-org/team=upstate,your-org/environment=production
```

Labels of a single tenant cluster:

```nohighlight
$ kubectl get --show-labels=true clusters.cluster.x-k8s.io/7g4di
```

### Select tenant clusters by label selector

Many `kubectl` commands support the `-l, --selector` flag, which allows to limit the selected resources based on given [Kubernetes Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors).

```nohighlight
$ kubectl get clusters.cluster.x-k8s.io -l 'your-org/team=upstate'
```
