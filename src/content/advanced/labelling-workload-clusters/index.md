---
linkTitle: Labelling clusters
title: Labelling workload clusters
description: Guide on using labels with workload clusters for the purpose of grouping, categorization and selection.
weight: 110
menu:
  main:
    parent: advanced
user_questions:
  - How can I assign metadata to cluster?
aliases:
  - /guides/tenant-cluster-labelling/
  - /guides/workload-cluster-labelling/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2022-05-24
---

{{< platform_support_table aws="ga=v10.0.0" azure="ga=v13.0.0" >}}

## Introduction

Workload clusters, like any other Kubernetes resource, can be enriched with [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). Labels are key-value-pairs, where each key can be used only once per object (here: per workload cluster).

Workload clusters are defined by a main Cluster resource ([`clusters.cluster.x-k8s.io`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}})). Accordingly, the labels we refer to in this article are those on that resource type only.

## Special purpose labels

Some of the controllers we use to manage clusters rely on the presence of certain labels. Hence we ask you be careful not to override or delete labels you find on the cluster resources. (For an exception to this rule, see [the service priority label](#service-priority).)

For your own labelling purposes, we strongly recommend to introduce a unique prefix, ideally based on a domain name. Example:

```yaml
example.tld/my-label: my-value
```

### Service priority {#service-priority}

Giant Swarm recommends to assign a _service priority_ to a cluster, using the following label:

```nohighlight
giantswarm.io/service-priority
```

Service priority is a relative ranking of the importance of clusters. It helps Giant Swarm staff and potentially, if your organization decides so, also your stakeholders to vet the priority of clusters in case of problems in several clusters. The possible label values are:

- `highest`: Clusters with this label value are considered the most important ones. We expect customers to use this class for clusters serving user-facing applications, production traffic, etc.
- `lowest`: The lowest priority class. We recommend this value for clusters that are not relied on, or which can be replaced easily and quickly. A typical case would be a cluster created for temporary testing purposes.
- `medium`: Clusters carrying this label value are considered less important than those with `highest`, but more important than clusters classified as `lowest`. Typical use cases would be staging clusters, clusters handling batch workloads, or development clusters that cannot be replaced easily by creating a new cluster.

If a cluster resource does not carry the `giantswarm.io/service-priority` label, we consider it's service priority to be `highest`.

Other values than the three mentioned above are not permitted and will be rejected by the Management API's admission controller. Also note that the label is only meant to be used on the main cluster resource. It will be ignored on other resource types, and we may also prevent setting it on other resource types in the future.

## Setting labels when creating a cluster

Depending on the method you use to create a cluster, you can specify labels when creating your cluster.

If you use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) to create a cluster manifest, you can apply the `--label` flag with your initial command, as often as required. You are also free to modify the created manifest before applying it. Example:

```nohighlight
kubectl gs template cluster \
  --label giantswarm.io/service-priority lowest \
  --label example.tld/environment testing \
  ...
```

## Modifying cluster labels

To modify labels on a cluster, several methods are supported:

- Our [web UI]({{< relref "/ui-api/web/workload-cluster-labelling" >}}) allows adding, modifying, and deleting labels interactively.
- The `kubectl label` command can be used with the cluster resource. See below for details.
- The deprecated [Rest API](https://docs.giantswarm.io/api/#tag/cluster-labels) and our CLI for it, [`gsctl`]({{< relref "/ui-api/gsctl/update-cluster">}}), allow modifying labels.

## Working with workload cluster labels using `kubectl`

With access to the management cluster, you are able to use `kubectl` to manage workload cluster labels.
The underlying resource to operate on is [`clusters.cluster.x-k8s.io`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) from the upstream [cluster-api](https://cluster-api.sigs.k8s.io/) project.

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
