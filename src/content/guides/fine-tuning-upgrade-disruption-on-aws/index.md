---
title: Fine-tuning upgrade disruption on AWS
description: The level of disruption caused by cluster upgrades can be influenced per cluster. This article explains how to adjust the number of nodes that is updated simlutaneously, and the wait time between batches of nodes.
type: page
weight: 130
tags: ["recipe"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Fine-tuning upgrade disruption on AWS

{{< platform_support_table aws="alpha=v12.7.0" >}}

## Introduction

Cluster upgraded, described in detail in our [cluster upgrades reference](/reference/cluster-upgrades/)), can cause disruption on workloads, if the upgrade requires upgrading worker nodes.

We provide two ways of limiting the amount of disruption:

- **Maximum batch size**: the highest possible number of nodes to upgrade at the same time
- **Pause time**: the time to wait between batches of worker nodes

As worker [node pools](/basics/nodepools/) on AWS are based on Auto Scaling Groups built using CloudFormation, both settings directly affect configuration details of the CloudFormation stack's [update policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html).

Configurability of these details has been introduced with workload cluster release v12.7.0 for AWS. The feature is currently in an early stage and its behaviour may change in the near future.

Adjustments to these settings require using the [Management API](/basics/api/#cp-k8s-api) to edit the [`AWSCluster`](/reference/cp-k8s-api/awsclusters.infrastructure.giantswarm.io/) resource of the cluster (for cluster-wide settings) or the [`AWSMachineDeployment`](/reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io/) of an individual node pool.

## Maximum batch size {#maximum-batch-size}

When a worker node update is necessary, nodes are updated (terminated and replaced by new ones) in groups or batches. The maximum batch size configures how many nodes are updated at the same time.

The settings directly maps to the [`MaxBatchSize`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-rollingupdate-maxbatchsize) property of the AWS CloudFormation update policy.

The **default value** for this property is `0.3`, which means that each batch will contain at most 30% of the nodes.

In order to override the default for either the entire cluster or a spdcific node pool, the annotation

```nohighlight
alpha.aws.giantswarm.io/update-max-batch-size
```

must be set

- on the [`AWSCluster`](/reference/cp-k8s-api/awsclusters.infrastructure.giantswarm.io/) resource, to be applied as a default to **all node pools** of the cluster.
- on the [`AWSMachineDeployment`](/reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io/) resource, to be effective for only **one node pool**. A value here will override any value specified on the `AWSCluster` level.

You have two options to configure the maximum batch size:

- **Absolute**: using an integer number larger than zero, you'll specify the maximum number of nodes in absolute terms.
- **Relative**: using a decimal number between `0.0` and `1.0` you can define the group size as a percentage of the node pool size. As an example, the value `"0.25"` would mean that all worker nodes would be divided into four groups, each containing 25 percent of the worker nodes (roughly).

The smaller you configure the maximum batch size, the less disruptive the upgrade will be, and the longer it will take.

**Note:** As with any Kubernetes annotation, the value must be of type String. In YAML this requires wrapping the value in double quotes.

### Examples {#maximum-batch-size-examples}

In this first example we set the absolute value `10` to roll a maximum of ten worker nodes per batch.

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  name: jni9x
  annotations:
    alpha.aws.giantswarm.io/update-max-batch-size: "10"
 ...
```

In this second example, we set the value to `0.1` to roll a maximum of 10 percent of nodes of a node pool per single batch.

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  name: jni9x
  annotations:
    alpha.aws.giantswarm.io/update-max-batch-size: "0.1"
 ...
```

## Pause Time {#pause-time}

After updating a batch of worker nodes, a pause time is applied. This time effectively allows Kubernetes to schedule workloads on the new worker nodes.

This setting maps to the [`PauseTime`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-rollingupdate-pausetime) property of the AWS CloudFormation update policy.

**By default**, the pause time is set to 15 minutes.

This value can be influenced via the annotation

```nohighlight
alpha.aws.giantswarm.io/update-pause-time
```

Again, the setting can be defined on two levels:

- on the [`AWSCluster`](/reference/cp-k8s-api/awsclusters.infrastructure.giantswarm.io/) resource, to be applied as a default to **all node pools** of the cluster.
- on the [`AWSMachineDeployment`](/reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io/) resource, to be effective for only **one node pool**. A value here will override any value specified on the `AWSCluster` level.

The value must be a string in the ISO 8601 duration format. Value examples:

- `PT10M`: 10 minutes
- `PT15S`: 15 seconds
- `PT1M30S`: 1 minute and 30 seconds

The maximum pause time is one hour (`PT1H`).

### Examples {#pause-time-examples}

In the first example, we set the value to `PT1M30S` to pause for one and a half minute between each batch.

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  name: jni9x
  annotations:
    alpha.aws.giantswarm.io/update-pause-time: "PT1M30S"
 ...
```

In this second example, we set the value to `PT5M` on `AWSMachineDeployment` to pause for five minutes between each batch only for this node pool.

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSMachineDeployment
metadata:
  name: 2suw9
  annotations:
    alpha.aws.giantswarm.io/update-pause-time: "PT5M"
 ...
```

## Further reading

- [Cluster upgrades reference](/reference/cluster-upgrades/)
- [Node pools](/basics/nodepools/)
- [Management API](/basics/api/#cp-k8s-api)
