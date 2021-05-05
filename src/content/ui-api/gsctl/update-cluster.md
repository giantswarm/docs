---
linkTitle: update cluster
title: "'gsctl update cluster' command reference"
description: The 'gsctl update cluster' command allows the modification of the cluster name, its labels, and converting it to provide high-availability Kubernetes masters.
weight: 230
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/update-cluster/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - How can I modify a cluster using gsctl?
---

# `gsctl update cluster`

The `gsctl update cluster` command allows the modification of some cluster attributes, depending on the workload cluster release version and the provider.

Changing the cluster name is possible on all providers and in all workload cluster release versions.

Cluster labelling is only available for clusters with workload cluster release v{{% first_aws_nodepools_version %}} and above for AWS, or v{{% first_azure_nodepools_version %}} and above for Azure. High availability of master nodes is available on AWS starting at workload cluster release v{{% first_aws_ha_masters_version %}}.

## Usage

The command is called with the cluster ID or name as a positional argument.
The desired new name can be specified with the `--name` or `-n` flag.
The `--label` flag is used to modify a single label change.
It can be specified multiple times in order to change multiple labels at once.

## Examples

### Modifying the cluster name {#ex-name}

```nohighlight
gsctl update cluster f01r4 \
  --name "Precious Production Cluster"
```

### Modifying cluster labels {#ex-label}

```nohighlight
gsctl update cluster vxvc7 \
  --label environment=testing \
  --label locked=
```

will update the labels of cluster `vxvc7`. It will add (or update depending on prior existence) label `environment=testing` and delete the label with key `locked`.

### Switching to high-availability of master nodes {#ex-master-ha}

Starting with workload cluster release v{{% first_aws_ha_masters_version %}} for AWS, a single master node cluster can be converted into using multiple master nodes in multiple availability zones using a command like the following:

```nohighlight
gsctl update cluster vxvc7 \
  --master-ha=true
```

Note that it is not possible to change from multiple master nodes to a single master.

## Full argument reference {#arguments}

- `--name` or `-n`: The new cluster name.
- `--label`: Specify a single label update.
Allowed multiple times.
Available on AWS starting at workload cluster release v{{% first_aws_nodepools_version %}}.
To remove a label, set its key to an empty string (`labeltodelete=`).
- `--master-ha`: When set to `true`, the cluster should be modified to use multiple master nodes. Available on AWS starting at workload cluster release v{{% first_aws_ha_masters_version %}}.

## Related

- [`gsctl create cluster`]({{< relref "/ui-api/gsctl/create-cluster" >}}) - Add a node pool to a cluster
- [`gsctl list clusters`]({{< relref "/ui-api/gsctl/list-clusters" >}}) - List all node pools of a cluster
- [API: Modify cluster (v4)](/api/#operation/modifyCluster)
- [API: Modify cluster (v5)](/api/#operation/modifyClusterV5)
- [API: Update cluster labels](/api/#operation/setClusterLabels)
- [Labelling workload clusters]({{< relref "/advanced/labelling-workload-clusters" >}})
