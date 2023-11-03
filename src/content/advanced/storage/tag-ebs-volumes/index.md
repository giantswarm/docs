---
linkTitle: Tag Persistent Volumes on AWS
title: Tag Persistent Volumes on AWS
description: This article describes how tag Persistent Volumes using a EBS Storage Class on AWS.
weight: 60
menu:
  main:
    parent: advanced-storage
user_questions:
 -  How can I tag persistent volumes on AWS?
last_review_date: 2023-11-03
aliases:
  - /guides/tag-ebs-volumes/
  - /advanced/tag-ebs-volumes/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

If your application needs additional storage, you usually create a `Persistent Volume Claim` (PVC) object and add this volume claim name to your `Deployment` or `Stateful Set`.

The `AWS-EBS-CSI-Driver`, which is installed by default in all workload clusters, is responsible for creating Elastic Block Storage (EBS) Volumes when creating EBS Persistent Volumes (PV) inside you cluster.

To tag your EBS volumes there are currently two ways:

1. Apply a new storage class with tag specifications
2. Install the optional `aws-ebs-volume-tagger` app in your cluster

### Create a new storage class

With `AWS-EBS-CSI-Driver` version >= 1.6.0 you can set additional tags on the storage class will tag EBS volumes when being created. It will only tag EBS volumes when you create a new EBS volume not on any updates like resizing.

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: example
provisioner: ebs.csi.aws.com
parameters:
  tagSpecification_1: "key1=value1"
  tagSpecification_2: "key2=hello world"
  tagSpecification_3: "key3=test"
  ...
```

Whenever you create a new PVC with this Storage Class it will set those tags on your EBS volumes.

### Use the `aws-ebs-volume-tagger` app

The `aws-ebs-volume-tagger` is a optional app which can be applied to your cluster. It runs as a cronjob periodically (every 15 minutes) and checks if there are any PVs which need to be tagged in AWS.

To tag all your PV's inside your cluster you need to add a `User level config` Yaml file with the following struct:

```yaml
extraVolumeTags:
  tag.provider.giantswarm.io/example: test
  tag.provider.giantswarm.io/example2: test2
  ...
```

Note that every key must start with `tag.provider.giantswarm.io` otherwise it will be ignored.

The config is the source of truth, the tagger will always ensure only the tags inside the config will be applied to the EBS volumes inside your cluster. If an additional tag starting with `tag.provider.giantswarm.io` is added manually on one of your EBS volumes, it will be reverted.

The tagger only considers EBS volumes from a PV in your cluster.
