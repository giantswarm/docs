---
title: "gsctl Command Reference: update cluster"
description: The 'gsctl update cluster' command allows the modification of the name of a cluster and its labels.
date: 2020-05-04
type: page
weight: 44
---

# `gsctl update cluster`

The `gsctl update cluster` allows the modification of the name of a cluster and its labels.
Cluster labelling is only available for clusters with release version {{% first_aws_nodepools_version %}} and above on AWS.

## Usage

The command is called with the cluster ID or name as a positional argument.
The desired new name can be specified with the `--name` or `-n` flag.
The `--label` flag is used to modify a single label change.
It can be specified multiple times in order to change multiple labels at once.

### Name modification example

```nohighlight
$ gsctl update cluster f01r4 --name "Precious Production Cluster"
```

### Labels modification key=value example

```nohighlight
$ gsctl update cluster vxvc7 --label environment=testing --label locked=
```

will update the labels of cluster `vxvc7`. It will add (or update depending on prior existence) label `environment=testing` and delete the label with key `locked`.

## Full argument reference {#arguments}

- `--name` or `-n`: The new cluster name.
- `--label`: Specify a single label update.
Allowed multiple times.
To remove a label, set its key to an empty string (`labeltodelete=`).

## Related

- [`gsctl create cluster`](/reference/gsctl/create-cluster/) - Add a node pool to a cluster
- [`gsctl list clusters`](/reference/gsctl/list-clusters/) - List all node pools of a cluster
- [API: Modify cluster (v4)](/api/#operation/modifyCluster)
- [API: Modify cluster (v5)](/api/#operation/modifyClusterV5)
- [API: Update cluster labels](/api/#operation/setClusterLabels)
- [Labelling tennant clusters](/guides/tenant-cluster-labelling/)
