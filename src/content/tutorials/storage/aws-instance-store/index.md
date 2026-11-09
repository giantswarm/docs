---
title: Fast ephemeral storage with AWS instance store
linkTitle: AWS instance store
diataxis_content_type: how-to-guide
description: Place pod emptyDir volumes and other ephemeral pod data on the local NVMe instance-store disks of AWS worker nodes.
weight: 30
menu:
  principal:
    parent: tutorials-storage
    identifier: tutorials-storage-aws-instance-store
last_review_date: 2026-11-09
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can pods use the local NVMe disks of AWS worker nodes?
  - How do I get faster emptyDir volumes on AWS?
  - How do I use the EC2 instance store in my workload cluster?
---

By default, the kubelet keeps pod [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volumes and other ephemeral pod data in `/var/lib/kubelet` on the EBS volume of the node. Many EC2 instance types also come with local NVMe disks, the [instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html). You can configure a node pool to mount these disks on `/var/lib/kubelet` instead. If an instance has several of these disks, they're combined into one volume.

Container images and the writable container layers stay on the EBS volume.

## When to use it

The instance store is a good fit for scratch data that pods write and read a lot, such as caches, downloaded AI models, build directories, or intermediate files of batch jobs:

- Local NVMe disks offer higher throughput and IOPS than EBS `gp3` volumes
- You don't pay for EBS capacity for scratch data
- The capacity grows with the instance size

It's not a fit for data that must outlive the node. The instance store is lost whenever a node is replaced. This happens during normal operation, for example:

- When a node pool rolls, for example during a cluster upgrade or after a change to the node pool configuration
- When the cluster autoscaler or Karpenter removes a node to scale down or consolidate

The data survives a reboot of the instance. Stopping and starting an instance [wipes the instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html). Giant Swarm clusters don't stop and start instances during normal operation. If someone does so manually, for example in the AWS console, the kubelet doesn't start again on that node, and you have to delete the node.

## Requirements

- An AWS (CAPA) workload cluster on release v35.2.0 or newer in the v35 series, or v36.1.0 or newer
- Instance types whose instance store is NVMe-attached SSD, such as the `c6id`, `m6id`, `r6id`, or `i4i` families. See [instance store volume limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html) for the instance store size of each type. The `d` families (`d3`, `d3en`) use HDDs and aren't supported.

Instance types with instance store usually cost more than their counterparts without, for example `m6id` compared to `m6i`. Not every family is offered in every region. To check a family in your region, run:

```sh
aws ec2 describe-instance-type-offerings \
  --region <REGION> \
  --location-type region \
  --filters 'Name=instance-type,Values=m6id.*' \
  --query 'InstanceTypeOfferings[].InstanceType' \
  --output text
```

## Configuration

Set `kubeletVolume: instanceStore` on the node pool in the cluster values. Enabling or disabling it replaces all nodes of that node pool.

For a node pool managed by the cluster autoscaler:

```yaml
global:
  nodePools:
    pool0:
      instanceType: m6id.xlarge
      kubeletVolume: instanceStore
      minSize: 3
      maxSize: 6
```

{{% notice warning %}}
For node pools managed by the cluster autoscaler, you must pick an instance type with an NVMe instance store yourself, also in `instanceTypeOverrides`. On an instance type without one, the node doesn't become ready.
{{% /notice %}}

For a node pool managed by [Karpenter]({{< relref "/tutorials/fleet-management/cluster-management/node-pools" >}}):

```yaml
global:
  nodePools:
    pool1:
      type: karpenter
      kubeletVolume: instanceStore
```

Karpenter then only launches instance types with an NVMe SSD instance store.

## Check the result

The `ephemeral-storage` capacity of a node now matches the size of its instance store instead of its EBS volume:

```sh
kubectl get nodes -o custom-columns='NAME:.metadata.name,TYPE:.metadata.labels.node\.kubernetes\.io/instance-type,EPHEMERAL:.status.capacity.ephemeral-storage'
```

## Sizing and eviction

The kubelet now measures the free space of the instance store as its node filesystem (`nodefs`). If its free space drops below 10%, the kubelet [evicts pods](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) from the node.

To make the scheduler aware of how much disk space a pod needs, set [`ephemeral-storage` requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage) on pods that use large `emptyDir` volumes. Also set `sizeLimit` on the `emptyDir` volume itself:

```yaml
spec:
  containers:
    - name: app
      resources:
        requests:
          ephemeral-storage: 50Gi
        limits:
          ephemeral-storage: 100Gi
      volumeMounts:
        - name: scratch
          mountPath: /scratch
  volumes:
    - name: scratch
      emptyDir:
        sizeLimit: 100Gi
```
