---
linkTitle: create nodepool
title: "'gsctl create nodepool' command reference"
description: The 'gsctl create nodepool' command allows to create a new pool of worker nodes in cluster.
weight: 70
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/create-nodepool/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl create nodepool`

The `gsctl create nodepool` command allows to create a new [node pool]({{< relref "/advanced/node-pools" >}}) in a cluster.

## Usage

Execute the command giving the cluster ID as a positional argument. Further options can be given as command line flags.

Example:

```nohighlight
$ gsctl create nodepool f01r4 \
    --name "General purpose m4.2xlarge 3AZ autoscaling" \
    --aws-instance-type m4.2xlarge \
    --num-availability-zones 3 \
    --nodes-min 3 \
    --nodes-max 20
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
$ gsctl create nodepool "Cluster name" \
    --name "General purpose m4.2xlarge 3AZ autoscaling" \
    --aws-instance-type m4.2xlarge \
    --num-availability-zones 3 \
    --nodes-min 3 \
    --nodes-max 20
```

### Spot instances

#### AWS

To request spot instances in your node pool on AWS, you have to set the percentage of worker nodes to be using spot instances via the `--aws-spot-percentage` flag. Optionally you can also define a number of workers that will be guaranteed to use on-demand instances, using the flag `--aws-on-demand-base-capacity`. Here is an example with 3 on-demand instances as a base capacity and 50 percent spot instances above that:

```nohighlight
$ gsctl create nodepool "Cluster name" \
    --name "General purpose m4.2xlarge 3AZ spot" \
    --aws-instance-type m4.2xlarge \
    --num-availability-zones 3 \
    --aws-on-demand-base-capacity 3 \
    --aws-spot-percentage 50
```

#### Azure

In order to use spot instances, specify the flag, like this:

```nohighlight
$ gsctl create nodepool f01r4 \
    --name "Production" \
    --azure-spot-instances
```

Here is how you can set a maximum hourly price in USD that a single node pool VM instance can reach before it is deallocated:

```nohighlight
$ gsctl create nodepool f01r4 \
    --name "Production" \
    --azure-spot-instances \
    --azure-spot-instances-max-price 0.00315
```

By setting the `--azure-spot-instances-max-price` flag to '0', the maximum price will be set to the on-demand price of the instance.

### Options

- `-n, --name`: Name or purpose description of the node pool. Defaults to "Unnamed node pool".
- `--num-availability-zones`: Number of availability zones to use. Default is `1`. Use this option if you don't care about the specific zones to use.
- `--availability-zones`: Comma-separated list of availability zones to use, instead of setting a number. Use this option if you care about the exact zones to use.
- `--aws-instance-type`: EC2 instance type to use for workers, e. g. `m5.2xlarge`.
- `--aws-on-demand-base-capacity`: Number of on-demand instances that this node pool needs to have until spot instances are used. Defaults to `0`.
- `--aws-spot-percentage`: Percentage of spot instances used once the on-demand base capacity is fulfilled. A number of 40 would mean that 60% will be on-demand and 40% will be spot instances. Defaults to `0`.
- `--aws-use-alike-instance-types`: Use similar instance type in your node pool. This list is maintained by Giant Swarm at the moment. Eg if you select m5.xlarge then the node pool can fall back on m4.xlarge too.
- `--azure-spot-instances`: Whether the node pool must use spot instances or on-demand.
- `--azure-spot-instances-max-price`: Max bid hourly price (in USD) for a single instance. `0` means on-demand price.
- `--azure-vm-size`: VM Size to use for workers, e.g. `Standard_D4s_v3`.
- `--nodes-min`: Minimum number of worker nodes for the node pool. Defaults to `3`.
- `--nodes-max`: Maximum number of worker nodes for the node pool. Defaults to `10`.

## Related

- [`gsctl list nodepools`]({{< relref "/ui-api/gsctl/list-nodepools" >}}) - List all node pools of a cluster
- [`gsctl show nodepool`]({{< relref "/ui-api/gsctl/show-nodepool" >}}) - Show details for a node pool
- [`gsctl update nodepool`]({{< relref "/ui-api/gsctl/update-nodepool" >}}) - Modify a node pool
- [`gsctl delete nodepool`]({{< relref "/ui-api/gsctl/delete-nodepool" >}}) - Delete a node pool
