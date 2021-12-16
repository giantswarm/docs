---
linkTitle: update cluster 
title: "'kubectl gs update cluster' command reference"
description: Reference documentation on how to upgrade a workload cluster using kubectl-gs.
weight: 100
menu:
  main:
    identifier: kubectl-gs-update-cluster
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/update-cluster/
last_review_date: 2021-12-13
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I upgrade a workload cluster from the command line?
  - How can I schedule a workload cluster upgrade from the command line?
---

# `kubectl gs update cluster`

This command allows to upgrade a workload cluster. Upgrades can either be triggered immediately, or the upgrade can be scheduled to happen at a specific date and time.

## Usage

### Upgrade a cluster immediately

```nohighlight
kubectl gs update cluster \
  --name a1b2c \
  --namespace org-acme \
  --release-version 16.1.0 \
  --provider aws
```

### Schedule a cluster upgrade

```nohighlight
kubectl gs update cluster \
  --name a1b2c \
  --namespace org-acme \
  --release-version 16.1.0 \
  --scheduled-time "2022-01-01 02:00" \
  --provider aws
```

Supported flags:

- `--name` - Name of the cluster.
- `--namespace` - Namespace of the cluster resource.
- `--release-version` - Version of the release the cluster should be upgraded to.
- `--scheduled-time` (optional): Scheduled time when cluster should be updated, in the format 'YYYY-MM-DD HH:MM'. Timezone UTC is assumed. If not given, the upgrade happens as soon as possible.
- `--provider` - The infrastructure provider, either `aws` or `azure`.

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
- [`cluster-upgrades`]({{< relref "/general/cluster-upgrades" >}}) - Cluster upgrades.
