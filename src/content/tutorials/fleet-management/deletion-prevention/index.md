---
linkTitle: Prevent deletion of resources
title: Prevent accidental deletion of resources
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
last_review_date: 2024-12-05
aliases:
  - /advanced/app-platform/deletion-prevention
  - /guides/deletion-prevention/
  - /advanced/deletion-prevention/
  - /vintage/advanced/app-platform/deletion-prevention
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

In the `kubectl gs template cluster` command of the [Create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster/" >}}) guide, add the parameter `--prevent-deletion`.

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

## Creating a managed app with deletion prevention

Like for cluster apps, you can use the `--prevent-deletion` parameter also with the command `kubectl gs template app`.

```sh
kubectl gs template app \
  --cluster-name=mycluster \
  --organization=myorg \
  --catalog=giantswarm \
  --app-name=mycluster-ingress-nginx \
  --name=ingress-nginx \
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
