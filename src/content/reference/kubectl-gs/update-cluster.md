---
linkTitle: update cluster
title: "'kubectl gs update cluster' command reference (cluster upgrades)"
description: Reference documentation on how to upgrade a workload cluster using kubectl-gs.
weight: 130
menu:
  principal:
    parent: reference-kubectlgs
    identifier: reference-kubectlgs-updatecluster
last_review_date: 2024-11-28
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I upgrade a workload cluster from the command line?
  - How can I schedule a workload cluster upgrade from the command line?
aliases:
  - /vintage/use-the-api/kubectl-gs/update-cluster/
---

This command's purpose is to modify details of a workload cluster. Currently it allows to upgrade a workload cluster to a newer [release]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/releases" >}}).

## Usage

### Upgrading a workload cluster {#cluster-upgrade} for CAPI cluster

**Note:** This feature is currently only working when the cluster configuration is **not stored** via GitOps.

Upgrades can either be triggered immediately, or the upgrade can be scheduled to happen at a specific date and time.

The following example shows how to upgrade a workload cluster to the release specified via the `--release-version` flag.

```nohighlight
kubectl gs update cluster \
  --provider capa \
  --namespace org-acme \
  --name a1b2c \
  --release-version 26.2.0
```

To schedule a workload cluster upgrade in the future, the `--scheduled-time` flag is used, like in the example below:

```nohighlight
kubectl-gs update cluster \
  --provider capa \
  --name a1b2c \
  --namespace org-acme \
  --release-version 29.0.0
  --scheduled-time "2024-08-28 12:10"
```

This adds annotations to the cluster resource, triggering the upgrade to the specified version at the scheduled time.

### Upgrading a workload cluster {#cluster-upgrade} for Vintage cluster

To upgrade a workload cluster immediately, use the following command:

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

## Flags

- `--provider` - The infrastructure provider of the installation, `aws` or `azure` for Vintage cluster, `capa`, `capz`, `vsphere` or `cloud-director` for CAPI cluster.
- `--name` - Name of the cluster.
- `--namespace` - Namespace of the cluster resource.
- `--release-version` - Version of the release the cluster should be upgraded to.
- `--scheduled-time` (optional): Scheduled time when the cluster should be updated, in the format `YYYY-MM-DD HH:MM`. Timezone UTC is assumed. If not given, the upgrade happens as soon as possible.

## Related

- [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
- [`cluster-upgrades`]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/cluster-upgrades" >}}) - Cluster upgrades.
