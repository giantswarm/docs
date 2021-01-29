---
linkTitle: update nodepool
title: "'gsctl update nodepool' command reference"
description: The 'gsctl update nodepool' command allows renaming and scaling of a node pool.
weight: 240
menu:
  main:
    parent: uiapi-gsctl
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl update nodepool`

The `gsctl update nodepool` allows modifying a [node pool]({{< relref "/advanced/node-pools" >}}), such as editing the scaling range and the name.

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

* Autoscaling enabled (AWS and Azure {{% first_azure_autoscaling_version %}} or newer)

```nohighlight
gsctl update nodepool f01r4/op1dl --nodes-min 3 --nodes-max 20
```

* No Autoscaling

```nohighlight
gsctl update nodepool f01r4/op1dl --nodes-min 6 --nodes-max 6
```

## Related

* [`gsctl create nodepool`]({{< relref "/ui-api/gsctl/create-nodepool" >}}) - Add a node pool to a cluster
* [`gsctl list nodepools`]({{< relref "/ui-api/gsctl/list-nodepools" >}}) - List all node pools of a cluster
* [`gsctl update nodepool`]({{< relref "/ui-api/gsctl/update-nodepool" >}}) - Modify a node pool
* [`gsctl delete nodepool`]({{< relref "/ui-api/gsctl/delete-nodepool" >}}) - Delete a node pool
