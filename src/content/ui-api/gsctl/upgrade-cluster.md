---
linkTitle: upgrade cluster
title: "'gsctl upgrade cluster' command reference"
description: Detailed documentation on how to upgrade a cluster using the 'upgrade cluster' command in gsctl.
weight: 260
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/upgrade-cluster/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - How can I upgrade a workload cluster using gsctl?
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

A message will be output showing the version to be upgraded, and a list of changelogs for the components that will be upgraded. Before confirming this action ensure you know the [upgrade process]({{< relref "/general/cluster-upgrades" >}})] and the impact it entails.

To prevent the interactive confirmation, you can use the `--force` flag. This will simplify the use in a non-interactive scenario. Example:

```nohighlight
gsctl upgrade cluster f01r4 --force
```

If you want to upgrade to a specific version, you can use the `--release` flag:

```nohighlight
gsctl upgrade cluster f01r4 --release 13.0.0
```

You can list available workload cluster releases with `gsctl list releases`.

## Related

- [Upgrade cluster general documentation]({{< relref "/general/cluster-upgrades" >}})
- [`gsctl create cluster`]({{< relref "/ui-api/gsctl/create-cluster" >}}): Reference for creating a cluster
- [`gsctl delete cluster`]({{< relref "/ui-api/gsctl/delete-cluster" >}}): Reference for deleting a cluster
- [`gsctl list releases`]({{< relref "/ui-api/gsctl/list-releases" >}}): Reference for listing available workload cluster releases
- [API: Upgrade cluster](/api/#operation/upgradeCluster)
