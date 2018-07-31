+++
title = "gsctl command Reference: delete cluster"
description = "Detailed documentation on how to delete a cluster using the 'delete cluster' command in gsctl."
date = "2017-04-04"
type = "page"
weight = 50
+++

# Delete a Cluster using `gsctl`

Deleting a cluster means that all workloads running on the cluster are terminated. Both master and worker nodes are deprovisioned. All data stored on the nodes will be deleted.

__Caution:__ There is no way to undo the deletion of a cluster. All data stored on the nodes will be lost.

## Command Usage

To delete a cluster, issue a command like below, applying the ID of the cluster you want to delete:

```nohighlight
$ gsctl delete cluster --cluster=<cluster-id>
```

You will be asked for confirmation that you really want to delete the cluster.

To prevent the interactive confirmation, you can use the `--force` flag. This will simplify the use in a non-interactive scenario. Example:

```nohighlight
$ gsctl delete cluster --force --cluster=<cluster-id>
```

## Related

- [`gsctl scale cluster`](../scale-cluster/)
- [`gsctl` reference overview](../)
- [API: Delete cluster](/api/#operation/deleteCluster)
