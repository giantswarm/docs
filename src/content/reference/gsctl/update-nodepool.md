---
title: "gsctl Command Reference: update nodepool"
description: The 'gsctl update nodepool' command allows renaming and scaling of a node pool.
date: 2020-08-25
type: page
weight: 44
---

# `gsctl update nodepool`

The `gsctl update nodepool` allows modifying a [node pool](/basics/nodepools/), such as editing the scaling range and the name.

## Usage

The command is called with the cluster and node pool ID as a positional argument,
separated by a slash. The `--name` flag is used to set a new name.

Example for renaming a node pool:

```nohighlight
gsctl update nodepool f01r4/op1dl --name "New node pool name"
```

Here, `f01r4` is the cluster ID and `op1dl` is the node pool ID.

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl update nodepool "Cluster name"/opdl --name "New node pool name"
```

Example for adjusting the scaling limits:

* Autoscaling enabled (AWS only)

```nohighlight
gsctl update nodepool f01r4/op1dl --nodes-min 3 --nodes-max 20
```

* No Autoscaling

```nohighlight
gsctl update nodepool f01r4/op1dl --nodes-min 6 --nodes-max 6
```

## Related

* [`gsctl create nodepool`](/reference/gsctl/create-nodepool/) - Add a node pool to a cluster
* [`gsctl list nodepools`](/reference/gsctl/list-nodepools/) - List all node pools of a cluster
* [`gsctl update nodepool`](/reference/gsctl/update-nodepool/) - Modify a node pool
* [`gsctl delete nodepool`](/reference/gsctl/delete-nodepool/) - Delete a node pool
