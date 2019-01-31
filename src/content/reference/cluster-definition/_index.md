+++
title = "Cluster Definition YAML Reference"
description = "Complete documentation of the Giant Swarm cluster definition YAML format"
date = "2019-01-31"
layout = "subsection"
weight = 100
+++

# Cluster Definition YAML Reference

The [`gsctl create cluster`](../gsctl/create-cluster/) command can consume YAML files conforming to this specification to create new clusters.

The YAML format corresponds directly with the Giant Swarm API v4 request body spec for [creating clusters](/api/#operation/addCluster).


## General notes on YAML

Chances are that you already work with YAML in various places. If not, here are some hints:

- In YAML, whitespace is important. Indentation must be made using blanks (space), not tabs.

- If in doubt, check your YAML in a linter. There are plenty online, e. g. [yamllint.com](http://www.yamllint.com/).

- JSON is valid YAML. If you prefer JSON's notation, just use valid JSON.

- You can add comments to YAML files by starting a line with the character `#`.

## Examples

The following example defines a cluster with three worker nodes:

```yaml
name: Example Cluster
owner: myorg
scaling:
  min: 3
  max: 3
workers:
  - memory:
      size_gb: 16
    cpu:
      cores: 8
    storage:
      size_gb: 100
```

As you can possibly see, the definition is quite sparse. Not all worker nodes need to have specifications for storage, CPU, and memory. Where details aren't specified, Giant Swarm will make use of defaults when creating the cluster.

**Note:** To learn about our current default values, available Kubernetes version, and valid ranges for the specifications for clusters, please contact us at support@giantswarm.io. We plan to offer simpler ways to inform you about current default values in the future.

In contrast to the example above, for AWS EC2 based clusters, worker nodes have to be specified by selecting an instance type. The following example shows how to select instance types for worker nodes instead. The keys `cpu`, `memory`, and `storage` are not applicable here.

```yaml
name: Example AWS Cluster
owner: myorg
scaling:
  min: 3
  max: 3
workers:
  - aws:
      instance_type: m3.large
```

**Note:** As of now, in AWS based clusters all worker nodes must be of the same instance type. Based on your installation, only certain instance types may be available. Please contact the support team to learn which instance types are supported on your installation.

## Definition Keys {#keys}

### Root level keys {#root-keys}

- `owner`: Name of the owner organization.
- `name`: Friendly name of the cluster. If not specified, a name will be generated.
- `workers`: Array of node definition objects describing each worker node. See below for possible keys. If not specified, the default number of worker nodes with default settings will be created.
- `release`: Allows to select a specific release version. The value must be the semver version number of an active relaese. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command.

### Node definition keys {#node-keys}

- `memory`: The sub-key `size_gb` allows to specify the amount of RAM to provide in a node using an integer or float value. Only usable on KVM (on-premises/bare metal) installations.
- `cpu`: The sub-key `cores` allows to require a number of CPU cores as integer. Only usable on KVM (on-premises/bare metal) installations.
- `storage`: The sub-key `size_gb` is used to specify the amount of local node storage in GB as an integer or decimal number. Only usable on KVM (on-premises/bare metal) installations.
- `aws`: Settings specific to AWS based clusters
- `aws.instance_type`: The AWS EC2 instance type to use for worker nodes, e. g. `m5.large`.
- `azure`: Settings specific to Azure based clusters
- `azure.vm_size`: The Azure VM size to use for worker nodes

## Related

- Learn how to create a cluster based on a definition file using [`gsctl create cluster`](/reference/gsctl/create-cluster/)
- Giant Swarm API v4: [creating clusters](/api/#operation/addCluster).
- Listing available releases using [`gstl list releases`](/reference/gsctl/list-releases/)
