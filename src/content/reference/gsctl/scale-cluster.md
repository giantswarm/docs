+++
title = "gsctl Command Reference: scale cluster"
description = "The 'gsctl scale cluster' command allows to add or remove worker nodes to reach a desired number."
date = "2019-01-31"
type = "page"
weight = 53
+++

# `gsctl scale cluster`

The `gsctl scale cluster` command allows you to influence the cluster size, i. e. the number of worker nodes.
For an [autoscaling cluster](/basics/cluster-size-autoscaling/), the command allows to modify the scaling limits for the autoscaler.

As of now, all worker nodes in a cluster share the same configuraition.
So any nodes added to the cluster will be of the same kind as the existing ones.

## Notes on worker node removal {#node-removal}

When reducing the worker node count, either manually or via the autoscaler, you have no influence in which exact order worker nodes are removed. Your workloads have to be configured in a way that single pods can be removed any time. See our [Recommendations and Best Practices](/guides/recommendations-and-best-practices/) article for details on how to achieve that.

For AWS, the Auto Scaling Group's logic determines which workers are removed. We use the [default termination policy](http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-termination.html#default-termination-policy). In brief, this policy will remove the oldest workers first. If all workers have the same age, the workers to be removed will be selected at random.

On Azure, the virtual machine scale set (VMSS) behaviour is responsible for the termination order. Here, VMs with the highest IDs are removed first.

## Command Usage {#usage}

To scale a cluster to a **specific number** of nodes, e. g. 5, use this syntax:

```nohighlight
$ gsctl scale cluster <cluster-id> --workers-min 5 --workers-max 5
```

Where **autoscaling** is available, you can specify a range within which the autoscaler can scale the number of worker nodes. Example:

```nohighlight
$ gsctl scale cluster <cluster-id> --workers-min 5 --workers-max 20
```

Note that autoscaling is currently only available on AWS in release version 6.3.0 or newer.

After the command has been executed, it can take a couple of minutes until the worker node count has adapted to the new settings.

## Confirmation

If the command execution will result in the removal of worker nodes, you will have to confirm the scaling in an interactive prompt.
This prompt can be suppressed using the `--force` flag.

When adding worker nodes, no such confirmation is required.

## Full Argument Reference {#arguments}

- `-w`, `--num-workers` (required): The desired amount of worker nodes after scaling.
- `--force`: If set, no confirmation is required when reducing the number of workers. You should only use this argument in automations when you are sure that reducing the number of workers is desired.

Use `gsctl scale cluster --help` for a additional (global) arguments.

## Related

- [`gsctl delete cluster`](/reference/gsctl/delete-cluster/): Delete a cluster
- [Basics: Cluster Size and Autoscaling](/basics/cluster-size-autoscaling/)
- [API: Modify cluster](/api/#operation/modifyCluster)
