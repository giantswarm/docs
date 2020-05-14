---
title: "gsctl Command Reference: update cluster"
description: The 'gsctl update cluster' command allows the modification of the name of a cluster and its labels.
date: 2020-05-14
type: page
weight: 44
---

# `gsctl update cluster`

The `gsctl update cluster` command allows the modification of some cluster attributes, depending on the release version and the provider.

Changing the cluster name is possible on all providers and in all release versions.

Cluster labelling is only available for clusters with release version v{{% first_aws_nodepools_version %}} and above on AWS. High availability of master nodes is available on AWS starting at release v{{% first_aws_ha_masters_version %}}.

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

### Switching to high availability of master nodes {#ex-master-high-availability}

Starting with release v{{% first_aws_ha_masters_version %}}, a single master node cluster can be converted into using multiple master nodes in multiple availability zones using a command like the following:

```nohighlight
gsctl update cluster vxvc7 \
  --master-high-availability=true
```

Note that it is not possible to change from multiple master nodes to a single master.

## Full argument reference {#arguments}

- `--name` or `-n`: The new cluster name.
- `--label`: Specify a single label update.
Allowed multiple times.
Available on AWS starting at release {{% first_aws_nodepools_version %}}.
To remove a label, set its key to an empty string (`labeltodelete=`).
- `--master-high-availability`: When set to `true`, the cluster should be modified to use multiple master nodes. Available on AWS starting at release v{{% first_aws_ha_masters_version %}}.

## Related

- [`gsctl create cluster`](/reference/gsctl/create-cluster/) - Add a node pool to a cluster
- [`gsctl list clusters`](/reference/gsctl/list-clusters/) - List all node pools of a cluster
- [API: Modify cluster (v4)](/api/#operation/modifyCluster)
- [API: Modify cluster (v5)](/api/#operation/modifyClusterV5)
- [API: Update cluster labels](/api/#operation/setClusterLabels)
- [Labelling tennant clusters](/guides/tenant-cluster-labelling/)
