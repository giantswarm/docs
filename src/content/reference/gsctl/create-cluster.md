+++
title = "gsctl Command Reference: create cluster"
description = "Detailed documentation on how to create a new cluster using the 'create cluster' command in gsctl."
date = "2019-01-31"
type = "page"
weight = 20
+++

# `gsctl create cluster`

With Giant Swarm, an organization can own any number of clusters. `gsctl create cluster` allows for creating a new Kubernetes cluster.

You can make use of two different approaches:

- Using **command line arguments**, you can quickly define a cluster name, how many nodes you need and how big these nodes should be.

- For full control over every detail, you first create a **cluster definition file** describing your desired cluster in YAML, which you then submit using `gsctl`. You know this declarative approach well from Kubernetes, where you apply manifest files using `kubectl`. It is reproducible, self-documenting, and the definitions can be kept in version control repositories.

In fact, you can also mix the two approaches, as some command line arguments can be used to extend (or overwrite) the definition passed as a file.


## Command Line Examples

The shortest possible way to create a new cluster with default settings:

```nohighlight
$ gsctl create cluster --owner=myorg
```

Here, `--owner` (alternatively: `-o`) specifies the name of the organization that will own the cluster.
You have to be logged in as a member of that organization.

As a result, a cluster with three nodes and a rather minimal node configuration will be created.
The name will be auto-generated, so it might or might not make sense to you and your team mates.

**Note:** The default configuration for nodes (amount of memory, disk storage, and CPU cores) may depend on your installation. Please contact us at support@giantswarm.io if you are unsure.

To set a friendly name for your new cluster, pass the `--name` (or `-n`) argument with the `create cluster` command:

```nohighlight
$ gsctl create cluster -o myorg --name "Test Cluster"
```

To create a new cluster that auto-scales within a certain range, use the `--workers-min` and `--workers-max` argument:

```nohighlight
$ gsctl create cluster \
  --owner myorg \
  --name "Dev cluster" \
  --workers-min 6 --workers-max 10
```

You can use further command line arguments to specify additional parameters of the worker nodes. Still, all worker nodes will have an identical configuration. Example *for bare-metal installations*:

```nohighlight
$ gsctl create cluster \
  --owner myorg \
  --name "Dev cluster" \
  --workers-min 5 \
  --memory-gb 8 \
  --num-cpus 2 \
  --storage-gb 100
```



To create a cluster with a variety of different node specifications, submit a definition file instead:

```nohighlight
$ gsctl create cluster --file devcluster.yaml
```

Learn more about the expected file format in the [cluster defininition reference](../../cluster-definition/).

The next example shows how the owner organization and the cluster name can be given as command line arguments when using a definition file:

```nohighlight
$ gsctl create cluster \
  --file devcluster.yaml \
  --owner=myorg \
  --name="Another dev cluster" \
  --release="1.4.6"
```

In this case it doesn't matter if the definition file has an `owner`, `name`, or `release` attribute, as the command line arguments take precedence.


## Full Argument Reference {#arguments}

Some arguments are specific to the provider used in the installation
(KVM for bare metal clusters, or AWS as a cloud provider).

- `--owner`, `-o`: Name of the owner organization. Overwrites name given in definition file.
- `--file`, `-f`: Definition file path. See [cluster defininition reference](../../cluster-definition/) for details.
- `--name`: Name of the cluster. Overwrites name given in definition file.
- `--workers-min`, `--workers-max`: Minimum and maximum number of worker nodes. For autoscaling clusters (available on AWS since release 6.3.0) this specifies the range within the autoscaler can scale the number of worker nodes. For releases prior to 6.3.0, and to pin the number of worker nodes to a specific amount, and on non-AWS installations, both values must be set to the same number.
- `--num-workers` (*deprecated*): Shorthand to set both minimum and maximum number of worker nodes to the same value.
- `--release`, `-r`: Specific release version number to use. Defaults to the latest active release. See [list releases](../list-releases/#definition) for details on releases.
- `--dry-run`: Add this flag (no value expected) to simulate the cluster creation. This is especially useful in combination with the global `--verbose`/`-v` flag, which will display the resulting definition YAML based on any command line argument or definition file input.

#### KVM specific {#arguments-kvm}

- `--memory-gb`: Worker node memory size in GB. Cannot be combined with `--file`/`-f`.
- `--num-cpus`: Number of CPU cores per worker node. Cannot be combined with `--file`/`-f`.
Cannot be combined with `--file`/`-f`.
- `--storage-gb`: Local node storage per node in GB. Cannot be combined with `--file`/`-f`.

#### AWS specific {#arguments-aws}

- `--availability-zones`: Number of availability zones. Cannot be combined with `--file`/`-f`.
- `--aws-instance-type`: AWS EC2 instance type to use for all worker nodes, e. g. `m5.large`.
Note that not all instance types might be allowed in your installation. When in doubt, please
contact the Giant Swarm support team.

#### Azure specific {#arguments-azure}

- `--azure-vm-size`: VM size to use for all worker nodes, e. g. `Standard_D2s_v3`.
Note that not all VM sizes might be allowed in your installation.
You can find out which VM sizes are allows using the [`gsctl info`](/reference/gsctl/info/) command.

## Related

- [Cluster defininition reference](/reference/cluster-definition/)
- [Basics: Cluster Size and Autoscaling](/basics/cluster-size-autoscaling/)
- [`gsctl create kubeconfig`](/reference/gsctl/create-kubeconfig/): Obtaining a key pair and enabling `kubctl` to access a cluster
- [`gsctl delete cluster`](/reference/gsctl/delete-cluster/): Reference for deleting a cluster
- [API: Create cluster](/api/#operation/addCluster)
