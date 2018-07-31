+++
title = "gsctl Command Reference: scale cluster"
description = "The 'gsctl scale cluster' command allows to add or remove worker nodes to reach a desired number."
date = "2018-03-28"
type = "page"
weight = 53
+++

# `gsctl scale cluster`

The `gsctl scale cluster` command allows you to scale a cluster, i.e. to add or remove worker nodes to/from a cluster.

When using the command, you define how many worker nodes (short: workers) you intend to have (desired state). The according number of workers is then added or removed.

When **scaling up** (increasing the number of workers), the new workers will be configured in the same way as the existing workers.

When **scaling down** (reducing the number of workers), the decision on which workers get removed is left to the AWS Auto Scaling Groups logic. We use the [default termination policy](http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-termination.html#default-termination-policy). In brief, this policy will remove the oldest workers first. If all workers have the same age, the workers to be removed will be selected at random.

## Command Usage {#usage}

To scale a cluster, use this command syntax:

```nohighlight
$ gsctl scale cluster <cluster-id> -w <desired-number-of-workers>
```

If `<desired-number-of-workers>` is a number smaller than the current number of workers in the cluster, you will have to confirm the scaling in an **interactive prompt**. This is to prevent you from scaling down accidentally.

When adding worker nodes, no confirmation is required.

After the command execution is finished, it can take a couple of minutes until the new workers are available in your Kubernetes clusters.

## Full Argument Reference {#arguments}

- `-w`, `--num-workers` (required): The desired amount of worker nodes after scaling.
- `--force`: If set, no confirmation is required when reducing the number of workers. You should only use this argument in automations when you are sure that reducing the number of workers is desired.
- `--memory-gb`: Currently not functional. Once scaling is supported on KVM, which argument will allow to configure the amount of RAM of the worker node(s) to be added.
- `--storage-gb`: Currently not functional. Once scaling is supported on KVM, which argument will allow to configure the amount of local storage of the worker node(s) to be added.
- `--num-cpus`: Currently not functional. Once scaling is supported on KVM, which argument will allow to configure the number of CPU cores (threads) of the worker node(s) to be added.

Use `gsctl scale cluster --help` for a additional (global) arguments.

## Related

- [`gsctl` reference overview](../)
