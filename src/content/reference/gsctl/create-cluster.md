+++
title = "gsctl Command Reference: create cluster"
description = "Detailed documentation on how to create a new cluster using the 'create cluster' command in gsctl."
date = "2019-10-30"
type = "page"
weight = 20
+++

# `gsctl create cluster`

<div class="well disclaimer">
This page reflects the future-proof way to use the `gsctl create cluster` command, which applies to releases both before and after v0.18.0. Versions before v0.18.0 support additional command line flags to specify cluster details without using a definition file. Please check `gsctl create cluster --help` in your version to find out more.
</div>

The command `gsctl create cluster` allows to create new Kubernetes clusters.

You can use the command with very simple syntax to create a cluster using default values. Note that several cluster specification details cannot be changed after creation.

In order to configure all details of the cluster according to your requirements, you'll create a [cluster definition](/reference/cluster-definition/) first and pass it to the command.

## Command line examples

The first and rather trivial example shows how to create a cluster for organization `myorg` and specifying the cluster name, while leaving all other settings to defaults:

```nohighlight
$ gsctl create cluster --owner myorg --name "Test cluster"
```

The second example shows how to create a cluster where most or even all configurable details are specified, using a definition file:

```nohighlight
$ gsctl create cluster --file prod_cluster_definition.yaml
```

Note that command line flags take precedence over values in the definition. This way you can, for example, define a default cluster name in the definition, but set a specific one via the `--name` flag when applying the same definition several times.

## Full argument reference {#arguments}

- `--file`, `-f`: Definition file path. See [cluster definition reference](../../cluster-definition/) for details. The value `-` means that the definition will be read from standard input.
- `--owner`, `-o`: Name of the owner organization. Overwrites a name given per definition file.
- `--name`: Name of the cluster. Overwrites name given in definition file.
- `--release`, `-r`: Specific release version number to use. Defaults to the latest active release. See [list releases](/reference/gsctl/list-releases/) for details on releases.

## Passing the cluster definition via standard input {#stdin}

The `--file` (short `-f`) flag accepts the special value `-` to read a definition from standard input. Depending on your shell you can make use of that in various ways.

For example, you can use a pipe like this:

```nohighlight
cat my-cluster.yaml | gsctl create cluster -f -
```

At least in bash, this syntax allows to include the entire definition in the command:

```bash
gsctl create cluster --file - <<EOF
owner: acme
name: Dev cluster
release: 7.1.1
EOF
```

## Related

- [Cluster definition reference](/reference/cluster-definition/)
- [`gsctl list releases`](/reference/gsctl/list-releases/) - List all available releases
- [`gsctl create kubeconfig`](/reference/gsctl/create-kubeconfig/) - Getting a key pair and enabling `kubctl` to access a cluster
- [`gsctl delete cluster`](/reference/gsctl/delete-cluster/) - Deleting a cluster
- [Basics: Cluster Size and Autoscaling](/basics/cluster-size-autoscaling/)
- [API: Create cluster (v4)](/api/#operation/addCluster)
- [API: Create cluster (v5)](/api/#operation/addClusterV5)
