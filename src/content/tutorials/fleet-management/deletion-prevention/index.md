---
linkTitle: Prevent deletion of resources
title: Prevent accidental deletion of resources
diataxis_content_type: how-to-guide
description: Avoid accidental deletion of clusters, apps or other resources in Giant Swarm platform.
weight: 110
menu:
  principal:
    identifier: tutorials-fleet-management-deletion-prevention
    parent: tutorials-fleet-management
user_questions:
  - How can I prevent the accidental deletion of resources?
  - How can I protect resources from accidental deletion?
  - How can I safeguard resources?
  - How can I protect clusters from accidental deletion?
  - How can I safeguard clusters?
  - How can I delete a cluster that has deletion prevention?
last_review_date: 2026-11-19
aliases:
  - /advanced/app-platform/deletion-prevention
  - /guides/deletion-prevention/
  - /advanced/deletion-prevention/
  - /vintage/advanced/app-platform/deletion-prevention
  - /tutorials/fleet-management/cluster-management/deletion-prevention
owner:
  - https://github.com/orgs/giantswarm/teams/team-tenet
---


In Kubernetes environments, it can be easy to unintentionally delete an important object with `kubectl delete`. To mitigate such risks, Giant Swarm clusters have Kyverno policy which safeguards against deletions of resources with the `giantswarm.io/prevent-deletion` label.

## How the label works

To use this mechanism you have to do two things:

1. Ensure that the resource type of the object you want to protect is in the [list of targeted resources](https://github.com/giantswarm/kyverno-policies-ux/blob/main/helm/kyverno-policies-ux/values.yaml). You can also show the preinstalled policy to see the list:

   ```nohighlight
   $ kubectl get ClusterPolicy/block-resource-deletion-if-has-prevent-deletion-label -o yaml
   [...]
     rules:
     - match:
         any:
         - resources:
             kinds:
             - Cluster
             - Cluster
             - Cluster
             - Cluster
             - Cluster
             - MachineDeployment
             - MachinePool
             - AWSCluster
             - App
             - Organization
             - Namespace
             - Secret
             - Secret
             - ConfigMap
             - KubeadmControlPlane
             selector:
               matchLabels:
                 giantswarm.io/prevent-deletion: '*'
   [...]
   ```

   If you want to extend this list of object types, please continue reading below about how to configure it.

2. Add the `giantswarm.io/prevent-deletion: "true"` label to the desired object (the `"true"` value does not matter). Below, we explain how to easily do this for clusters or managed apps.

## Creating a cluster with deletion prevention

Since kubectl-gs v7.0.0, `kubectl gs template cluster` and `kubectl gs gitops add base` protect new clusters by default, as described in their [template cluster]({{< relref "/reference/kubectl-gs/template-cluster" >}}) and [add base]({{< relref "/reference/kubectl-gs/gitops/add-base" >}}) references. They label the cluster's resources, and set `global.metadata.preventDeletion: true` in the cluster values, so that the chart labels the `Cluster` resource too. `kubectl gs template cluster` also labels the `<cluster-name>-userconfig` ConfigMap.

To create a cluster without deletion prevention, pass `--prevent-deletion=false`. Older kubectl-gs versions only protect the cluster when you pass `--prevent-deletion`.

## Adding deletion prevention to an existing cluster

Our Cluster API (CAPI) based cluster charts allow setting the option `global.metadata.preventDeletion=true`. It can be toggled in the values of the chart:

```yaml
---
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        availabilityZoneUsageLimit: 3
        network: {}
        topology: {}
      controlPlane: {}
      metadata:
        description: My test cluster
        name: mycluster
        organization: myorg

        ###############################################
        preventDeletion: false # <==== set this to true
        ###############################################
      nodePools:
        # [...]
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: mycluster
  name: mycluster-userconfig
  namespace: org-myorg
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: mycluster
  namespace: org-myorg
spec:
  # [...]
  name: cluster-aws
  namespace: org-myorg
  userConfig:
    configMap:
      name: mycluster-userconfig
      namespace: org-myorg
  version: ""
```

After applying the ConfigMap change on the management cluster, you should see the deletion prevention label on certain resources such as the `Cluster` object.

The value doesn't protect the resources that deploy the chart. Label them too, for example for a cluster deployed as a `HelmRelease`:

```sh
kubectl label -n org-myorg helmrelease/mycluster ocirepository/mycluster configmap/mycluster-userconfig giantswarm.io/prevent-deletion=true
```

For a cluster deployed as an `App`, label `app/mycluster` instead of the `HelmRelease` and the `OCIRepository`.

## Deleting a cluster with deletion prevention {#deleting-a-protected-cluster}

The management cluster refuses to delete a resource with the `giantswarm.io/prevent-deletion` label. To delete a protected cluster, remove the protection first:

1. Set `global.metadata.preventDeletion` to `false`, so that the chart removes the label from the `Cluster` resource. For a cluster deployed as a `HelmRelease`, set it in the `HelmRelease` values, which take precedence over the ConfigMaps in `valuesFrom`:

   ```sh
   kubectl patch -n org-myorg helmrelease mycluster --type merge \
     -p '{"spec":{"values":{"global":{"metadata":{"preventDeletion":false}}}}}'
   ```

   For a cluster deployed as an `App`, set it in the `<cluster-name>-userconfig` ConfigMap instead.

2. Wait until the chart upgrade has removed the label from the `Cluster` resource. The `PREVENT-DELETION` column has to be empty:

   ```sh
   kubectl get clusters.cluster.x-k8s.io -n org-myorg mycluster -L giantswarm.io/prevent-deletion
   ```

3. Remove the label from the resources that deploy the chart:

   ```sh
   kubectl label -n org-myorg helmrelease/mycluster ocirepository/mycluster configmap/mycluster-userconfig giantswarm.io/prevent-deletion-
   ```

   For a cluster deployed as an `App`, remove it from `app/mycluster` and `configmap/mycluster-userconfig`.

4. Delete the cluster as usual, for example as described in [Create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster#deleting-workload-cluster" >}}).

If Flux applies the cluster's resources from a GitOps repository, make these changes in the repository instead, or Flux restores the labels and values. The `gitops-template` [getting started guide](https://github.com/giantswarm/gitops-template/blob/main/docs/getting-started.md#6-delete-the-cluster-optional) shows how.

## Creating a managed app with deletion prevention

The `giantswarm.io/prevent-deletion=true` label works on both the legacy `App` custom resource and on Flux `HelmRelease` resources. For HelmRelease, set the label under `metadata.labels` in the rendered YAML.

Like for cluster apps, you can use the `--prevent-deletion` parameter also with the command `kubectl gs template app`.

```sh
kubectl gs template app \
  --cluster-name=mycluster \
  --organization=myorg \
  --catalog=giantswarm \
  --app-name=mycluster-envoy-gateway \
  --name=envoy-gateway \
  --version=3.9.1 \
  --target-namespace=kube-system \
  --prevent-deletion
```

## Protecting an existing object

In this example, the object `App/myapp` and its related user values ConfigMap receive deletion prevention:

```sh
kubectl label -n org-ORGANIZATION App myapp giantswarm.io/prevent-deletion=true
kubectl label -n org-ORGANIZATION ConfigMap myapp-userconfig giantswarm.io/prevent-deletion=true
```

Each label only protects a single object, not a hierarchy of objects such as seen with CAPI clusters (`Cluster`, `AWSCluster` and other children). For workload clusters and managed apps, please prefer the aforementioned instructions instead of this manual labeling.

## Configure targeted resources {#targeted-resource-configuration}

If the [list of targeted resources](https://github.com/giantswarm/kyverno-policies-ux/blob/main/helm/kyverno-policies-ux/values.yaml)
does not cover all resources that you want to protect, it is possible to configure them through the user configuration values of the `kyverno-policies-ux` app.
[Here]({{< relref "/tutorials/fleet-management/app-platform/app-configuration/" >}}) you can learn more about how to configure an app.
