---
linkTitle: update cluster 
title: "'kubectl gs update cluster' command reference"
description: Reference documentation on how to update update a Cluster using 'kubectl gs'.
weight: 100
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/update-cluster/
last_review_date: 2021-12-13
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I update a cluster from the command line?
---

# `kubectl gs update cluster`

Updating clusters can be done in two ways. A cluster can be immediately updated or a cluster update can be scheduled in the future.

## Usage

### Update a cluster immediately

```nohighlight
kgs update cluster --name a1b2c --namespace org --release-version 16.1.0 --provider aws
```

### Schedule a cluster update

```nohighlight
kgs update cluster --name a1b2c --namespace org --release-version 16.1.0 --scheduled-time "2022-01-01 02:00" --provider aws
```

Supported flags:

- `--name` - ID of the cluster.
- `--namespace` - Namespace of the cluster.
- `--release-version` - Version of the release the cluster should be upgraded to.
- `--scheduled-time` - Optionally: Scheduled time when cluster should be updated, time format 'YYYY-MM-DD HH:MM'.
- `--provider` - The infrastructure provider, either `aws` or `azure`.

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
- [`cluster-upgrades`]({{< relref "/general/cluster-upgrades" >}}) - Cluster upgrades.
