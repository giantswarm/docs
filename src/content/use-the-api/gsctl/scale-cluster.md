---
linkTitle: scale cluster
title: "'gsctl scale cluster' command reference"
description: The 'gsctl scale cluster' command allows to add or remove worker nodes to an on-premises cluster (KVM).
weight: 180
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/scale-cluster/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I scale an on-premises (KVM) cluster using gsctl?
last_review_date: 2022-12-07
---

{{% gsctl_deprecation_disclaimer %}}

The `gsctl scale cluster` command allows to specify the number of worker nodes for an on-premises (KVM) cluster.

For clusters on AWS and Azure, instead of scaling an entire cluster, please see [`gsctl update nodepool`]({{< relref "/use-the-api/gsctl/update-nodepool" >}}) regarding how to scale a node pool.

## Notes on worker node removal {#node-removal}

When reducing the worker node count, you have no influence in which exact order worker nodes are removed. Your workloads have to be configured in a way that single pods can be removed any time. See our article on [recommendations and best practices]({{< relref "/getting-started/best-practices" >}}) for details on how to achieve that.

## Command usage {#usage}

To scale a cluster to a **specific number** of nodes, e. g. 5, use this syntax:

```nohighlight
gsctl scale cluster f0r14 --num-workers 5
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl scale cluster "Cluster name" --num-workers 5
```

After the command has been executed, it can take a few minutes until the worker node count has adapted to the new settings.

## Confirmation

When reducing the number of worker nodes, you will have to confirm the command execution in an interactive prompt.
This prompt can be suppressed using the `--force` flag.

When adding worker nodes, no such confirmation is required.

## Full argument reference {#arguments}

- `-w`, `--num-workers`: The intended number of worker nodes.
- `--force`: If set, no confirmation is required when reducing the number of workers. You should only use this argument in automations when you are sure that reducing the number of workers is desired.

Use `gsctl scale cluster --help` for a additional (global) arguments.

## Related

- [`gsctl update nodepool`]({{< relref "/use-the-api/gsctl/update-nodepool" >}}): Among others, allows to scale a node pool
- [`gsctl delete cluster`]({{< relref "/use-the-api/gsctl/delete-cluster" >}}): Delete a cluster
- [Basics: Cluster Size and Autoscaling]({{< relref "/getting-started/cluster-size-autoscaling" >}})
- [API: Modify cluster](/api/#operation/modifyCluster)
