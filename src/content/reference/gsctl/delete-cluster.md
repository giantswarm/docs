---
title: "gsctl command Reference: delete cluster"
description: "Detailed documentation on how to delete a cluster using the 'delete cluster' command in gsctl."
date: "2020-03-11"
type: page
weight: 50
---

# Delete a Cluster using `gsctl`

Deleting a cluster means that all workloads running on the cluster are terminated. Both master and worker nodes are deprovisioned. All data stored on the nodes will be deleted.

__Caution:__ There is no way to undo the deletion of a cluster. All data stored on the nodes will be lost.

## Command usage

To delete a cluster, issue a command like below, applying the ID of the cluster you want to delete:

```nohighlight
gsctl delete cluster --cluster f01r4
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl delete cluster --cluster "Cluster name"
```

You will be asked for confirmation that you really want to delete the cluster.

To prevent the interactive confirmation, you can use the `--force` flag. This will simplify the use in a non-interactive scenario. Example:

```nohighlight
gsctl delete cluster --force --cluster f01r4
```

## Argument reference {#arguments}

- `--force`: Disable any confirmations.
- `--output`: By specifying this flag with value `json`, the output can be printed in JSON format. Disables any confirmations. This is convenient for use in automation. See [JSON output](#json-output) for examples.

## JSON output {#json-output}

Passing flag `--output` with value `json` to `gsctl create kubeconfig` changes the printed output to be formatted as a JSON object.

**Example success output:**
```nohighlight
{
  "result": "deletion scheduled",
  "id": "f01r4"
}
```

**Example error output:**
```nohighlight
{
  "result": "error",
  "id": "",
  "error": {
    "kind": "CouldNotDeleteClusterError",
    "annotation": "Unauthorized",
    "stack": [
      {
        "file": "/go/src/giantswarm/gsctl/commands/delete/cluster/command.go",
        "line": 295
      }
    ]
  }
}
```

## Related

- [`gsctl scale cluster`](../scale-cluster/)
- [`gsctl` reference overview](../)
- [API: Delete cluster](/api/#operation/deleteCluster)
