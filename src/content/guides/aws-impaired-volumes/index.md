+++
title = "Handling Impaired EBS Volumes"
description = "This guide will walk you through what happens to a node with impaired EBS volumes, and how to improve your workloads to handle them."
date = "2019-05-01"
type = "page"
weight = 100
tags = ["tutorial"]
+++
# Handling Impaired EBS Volumes
# What happens when EBS Volumes are impaired?

When an EBS Volume is stuck in an attaching state for more than 30 minutes,
the node is marked as unscheduable with the following taint:

```
- effect: "NoSchedule"
  key: "NodeWithImpairedVolumes"
  value: "true"
```

This stops Pods from being scheduled on the node, to reduce the impact of
EBS Volumes not being able to be attached.

Giant Swarm will take care to drain and terminate nodes with this taint.

# What if my workloads don't need EBS Volumes?

If your pods don't require EBS Volumes, it may be helpful to tolerate the above taint.
This can be helpful in the case where a node is tainted, but you still wish for
workloads to be scheduled onto that node.

Setting the following toleration:

```
- effect: "NoSchedule"
  key: "NodeWithImpairedVolumes"
  operator: "Exists"
```

## Further reading

- [Kubernetes Pull Request to add support for this taint](https://github.com/kubernetes/kubernetes/pull/55558/files)
