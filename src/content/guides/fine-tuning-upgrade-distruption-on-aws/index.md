---
title: "Fine-tuning upgrade distruption on AWS"
description: "How configure and tune tenant clusters upgrade granuality."
date: "2020-11-5"
type: page
weight: 130
tags: ["recipe"]
---

# Fine-tuning upgrade distruption on AWS

Giant Swarm release `12.7.0` allows a configuration of [AWS CloudFormation UpdatePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html) parameters to have better control over the updates of a tenant cluster. This feature is currently in an `alpha` state.

The configuration is done via annotations on `AWSCluster` or `AWSMachineDeployment`. They can be added either at creation time or they can be added on already created CRs.

## Max Batch Size

The property `MaxBatchSize` specifies the maximum number of instances that AWS CloudFormation updates.

This value can be set via annotation `alpha.aws.giantswarm.io/update-max-batch-size` on `AWSCluster` CR or `AWSMachineDeploymentCR`. The value set on `AWSCluster` will be used for a whole cluster. The value set on `AWSMachineDeploymentCR` will be only used for that specific NodePool and will override the value from `AWSCluster` in case it is defined.

There are two valid formats for the `MaxBatchSize`:

* An integer number bigger than zero, which specifies the static amount of nodes, e.g "5"
* A decimal number in a range `0 < x <= 1.0` which defines a percentage of nodes that can be rolled in a single batch, e. g. "0.25" which represents 25% of all nodes

The default value is `0.3` which implies 30% of instances will be rolled in each batch.

### MaxBatchSize examples

Set value to static value `10` to roll maximum 10 instances per single batch.

```yaml

apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  annotations:
    alpha.aws.giantswarm.io/update-max-batch-size: "10"
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.7.0
  name: jni9x
  namespace: default
spec:
 ....

```

Set value to `0.10` to roll maximum of 10% of nodes per single batch.

```yaml

apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  annotations:
    alpha.aws.giantswarm.io/update-max-batch-size: "0.10"
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.7.0
  name: jni9x
  namespace: default
spec:
 ....

```

## Pause Time

The amount of time that AWS CloudFormation pauses after making a change to a batch of instances to give those instances time to start software applications.

This value can be set via annotation `alpha.aws.giantswarm.io/update-pause-time` on `AWSCluster` CR or `AWSMachineDeploymentCR`. Value set on `AWSCluster` will be used for a whole cluster. Value set on `AWSMachineDeploymentCR` will be only used for that specific NodePool and will override  value from `AWSCluster` (if set).

`PauseTime` needs to be in ISO 8601 duration format, e. g. "PT10M" for 10 minutes or "PT15S" for 15 seconds.

The default value is `PT15M` (15 minutes).

### PauseTime examples

Set value to `PT1M30S` to pause for 1 minute and 30 seconds between each batch.

```yaml

apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  annotations:
    alpha.aws.giantswarm.io/update-pause-time: "PT1M30S"
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.7.0
  name: jni9x
  namespace: default
spec:
 ....

```

Set value to `PT5M` on `AWSMachineDeployment` to pause for 5 minutes between each batch only for this NodePool.

```yaml

apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSMachineDeployment
metadata:
  annotations:
    alpha.aws.giantswarm.io/update-pause-time: "PT5M"
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/machine-deployment: 2suw9
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.7.0
  name: 2suw9
  namespace: default
  uid: 17c33685-2c03-4520-9109-9b6ff0b07b70
spec:
 ...

```
