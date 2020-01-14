+++
title = "gsctl Command Reference: create nodepool"
description = "The 'gsctl create nodepool' command allows to create a new pool of worker nodes in cluster."
date = "2019-12-19"
type = "page"
weight = 44
+++

# `gsctl create nodepool`

The `gsctl create nodepool` command allows to create a new [node pool](/basics/nodepools/) in a cluster.

## Usage

Execute the command giving the cluster ID as a positional argument. Further options can be given as command line flags.

Example:

```nohighlight
gsctl create nodepool f01r4 \
    --name "General purpose m4.2xlarge 3AZ autoscaling" \
    --aws-instance-type m4.2xlarge \
    --num-availability-zones 3 \
    --nodes-min 3 \
    --nodes-max 20
```

### Options

- `-n, --name`: Name or purpose description of the node pool. Defaults to "Unnamed node pool".
- `--num-availability-zones`: Number of availability zones to use. Default is `1`. Use this option if you don't care about the specific zones to use.
- `--availability-zones`: Comma-separated list of availability zones to use, instead of setting a number. Use this option if you care about the exact zones to use.
- `--aws-instance-type`: EC2 instance type to use for workers, e. g. `m5.2xlarge`.
- `--nodes-min`: Minimum number of worker nodes for the node pool. Defaults to `10`.
- `--nodes-max`: Maximum number of worker nodes for the node pool. Defaults to `3`.

## Related

- [`gsctl list nodepools`](/reference/gsctl/list-nodepools/) - List all node pools of a cluster
- [`gsctl show nodepool`](/reference/gsctl/show-nodepool/) - Show details for a node pool
- [`gsctl update nodepool`](/reference/gsctl/update-nodepool/) - Modify a node pool
- [`gsctl delete nodepool`](/reference/gsctl/delete-nodepool/) - Delete a node pool
