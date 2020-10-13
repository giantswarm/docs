---
title: "gsctl Command Reference: upgrade cluster"
description: Detailed documentation on how to upgrade a cluster using the 'upgrade cluster' command in gsctl.
date: 2020-03-11
type: page
weight: 30
---

# `gsctl upgrade cluster`

In order to upgrade a cluster to the next suitable version, use this command:

```nohighlight
gsctl upgrade cluster f01r4
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl upgrade cluster "Cluster name"
```

A message will be output showing the version to be upgraded, and a list of changelogs for the components that will be upgraded. Before confirming this action ensure you know the [upgrade process](/reference/cluster-upgrades/)] and the impact it entails.

To prevent the interactive confirmation, you can use the `--force` flag. This will simplify the use in a non-interactive scenario. Example:

```nohighlight
gsctl upgrade cluster f01r4 --force
```

## Related

- [Upgrade cluster general documentation](/reference/cluster-upgrades/)
- [`gsctl create cluster`](/reference/gsctl/create-cluster/): Reference for creating a cluster
- [`gsctl delete cluster`](/reference/gsctl/delete-cluster/): Reference for deleting a cluster
- [API: Upgrade cluster](/api/#operation/upgradeCluster)
