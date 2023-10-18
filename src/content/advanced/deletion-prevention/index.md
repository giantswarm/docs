---
linkTitle: Prevent deletion of resources
title: Prevent accidental deletion of resources
description: Learn how to prevent accidental deletion of resources by introducing a label.
weight: 110
menu:
  main:
    parent: advanced
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
last_review_date: 2023-10-10
user_questions:
  - How can I prevent the accidental deletion of resources?
  - How can I protect resources from accidental deletion?
  - How can I safeguard resources?
  - How can I protect clusters from accidental deletion?
  - How can I safeguard clusters?
---


In Kubernetes environments, it can be quite easy to accidentally delete an important object with `kubectl delete`.
To mitigate such risks, Giant Swarm introduces a mechanism: the `giantswarm.io/prevent-deletion` label.
When applied, this label, in conjunction with our Kyverno policy, acts as a safeguard against accidental deletions.

## Usage

To use this mechanism you have to do two things:

1. Ensure that the resource type of the object you want to protect is in the [list of targeted resources](https://github.com/giantswarm/kyverno-policies-ux/blob/main/helm/kyverno-policies-ux/values.yaml).
   For more information about configuring the targeted resources look at the [Configure Target Resources]({{< relref "advanced/deletion-prevention#targeted-resource-configuration" >}}) section.
2. Add the `giantswarm.io/prevent-deletion` label to the object with any value.

### Example

The following `kubectl` commands show you how to apply the label to a cluster.
{{< tabs >}}

{{< tab id="capi" for-impl="capi_any">}}

```sh
kubectl label app -n org-ORGANIZATION CLUSTER_NAME-default-apps \
  giantswarm.io/prevent-deletion=true

kubectl label app -n org-ORGANIZATION CLUSTER_NAME \
  giantswarm.io/prevent-deletion=true

kubectl label configmap -n org-ORGANIZATION CLUSTER_NAME-default-apps-userconfig \
  giantswarm.io/prevent-deletion=true

kubectl label configmap -n org-ORGANIZATION CLUSTER_NAME-userconfig \
  giantswarm.io/prevent-deletion=true
```

{{< /tab >}}
{{< tab id="vintage" for-impl="vintage_any">}}

```sh
kubectl label cluster \
  -n org-ORGANIZATION \
  CLUSTER_NAME \
  giantswarm.io/prevent-deletion=true
```

{{< /tab >}}
{{< tab id="app" title="Managed app">}}

You can use the `--prevent-deletion` parameter or alternatively set the label manually.

```sh
kubectl gs template app \
  --cluster-name=your-workload-cluster \
  --catalog=giantswarm \
  --name=nginx-ingress-controller-app \
  --version=3.0.1 \
  --target-namespace=kube-system \
  --prevent-deletion
```

{{< /tab >}}
{{< /tabs >}}

You can find more details about labelling clusters in the [Labelling workload clusters]({{< relref "advanced/labelling-workload-clusters" >}}) article.

__Warning__: Only resources with the assigned label are protected against
deletion. Resources indirectly linked to the protected resource are not
protected. For instance, node pools within a protected cluster can be deleted
directly unless they too bear the label.

## Configure Targeted Resources {#targeted-resource-configuration}

If the [list of targeted resources](https://github.com/giantswarm/kyverno-policies-ux/blob/main/helm/kyverno-policies-ux/values.yaml)
does not cover all resources that you want to protect, it is possible to configure them through the user config values of the `kyverno-policies-ux` app.
[Here]({{< relref "getting-started/app-platform/app-configuration" >}}) you can learn more about how to configure an app.
