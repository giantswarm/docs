---
linkTitle: update cluster
title: "'kubectl gs update cluster' command reference"
description: Reference documentation on how to upgrade a workload cluster using kubectl-gs.
weight: 130
menu:
  main:
    parent: uiapi-kubectlgs
    identifier: uiapi-kubectlgs-updatecluster
aliases:
  - /use-the-api/kubectl-gs
  - /reference/kubectl-gs/update-cluster/
  - /ui-api/kubectl-gs/update-cluster/
last_review_date: 2023-04-04
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I upgrade a workload cluster from the command line?
  - How can I schedule a workload cluster upgrade from the command line?
---

This command's purpose is to modify details of a workload cluster. Currently it allows to upgrade a workload cluster to a newer [release]({{< relref "/vintage/platform-overview/cluster-management/releases" >}}).

## Usage

### Upgrading a workload cluster {#cluster-upgrade}

Upgrades can either be triggered immediately, or the upgrade can be scheduled to happen at a specific date and time.

The following example shows how to upgrade a workload cluster to the release specified via the `--release-version` flag.

```nohighlight
kubectl gs update cluster \
  --provider aws \
  --namespace org-acme \
  --name a1b2c \
  --release-version 16.1.0
```

Note that all flags are mandatory. As a result of the command execution, the cluster resource's version label (`release.giantswarm.io/version`) will be updated, which in turn triggers the cluster upgrade.

To schedule a workload cluster upgrade in the future, the `--scheduled-time` flag is used, like in the example below:

```nohighlight
kubectl gs update cluster \
  --provider aws \
  --namespace org-acme \
  --name a1b2c \
  --release-version 16.1.0 \
  --scheduled-time "2022-01-01 02:00"
```

This adds annotations to the cluster resource, triggering the upgrade to the specified version at the scheduled time.

## Flags

- `--provider` - The infrastructure provider of the installation, either `aws` or `azure`.
- `--name` - Name of the cluster.
- `--namespace` - Namespace of the cluster resource.
- `--release-version` - Version of the release the cluster should be upgraded to.
- `--scheduled-time` (optional): Scheduled time when the cluster should be updated, in the format `YYYY-MM-DD HH:MM`. Timezone UTC is assumed. If not given, the upgrade happens as soon as possible.

## Related

- [`kubectl gs login`]({{< relref "/vintage/use-the-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
- [`cluster-upgrades`]({{< relref "/vintage/platform-overview/cluster-management/cluster-upgrades" >}}) - Cluster upgrades.
