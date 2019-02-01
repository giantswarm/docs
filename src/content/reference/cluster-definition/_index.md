+++
title = "Cluster Definition YAML Reference"
description = "Complete documentation of the Giant Swarm cluster definition YAML format"
date = "2017-06-21"
layout = "subsection"
weight = 100
+++

# Cluster Definition YAML Reference

The [`gsctl create cluster`](../gsctl/create-cluster/) command can consume YAML files conforming to this specification to create new clusters.

## General notes on YAML

Chances are that you already work with YAML in various places. If not, here are some hints:

- In YAML, whitespace is important. Indentation must be made using blanks (space), not tabs.

- If in doubt, check your YAML in a linter. There are plenty online, e. g. [yamllint.com](http://www.yamllint.com/).

- JSON is valid YAML. If you prefer JSON's notation, just use valid JSON.

- You can add comments to YAML files by starting a line with the character `#`.

## Examples

The following example defines a cluster with three worker nodes, where each has different characteristics:

```yaml
name: Example Cluster
owner: myorg
workers:
  - memory:
      size_gb: 16
    labels:
      nodetype: big memory
  - cpu:
      cores: 8
    labels:
      nodetype: big cpu
  - storage:
      size_gb: 100
    labels:
      nodetype: big storage
```

As you can possibly see, the definition is quite sparse. Not all worker nodes need to have specifications for storage, CPU, and memory. Where details aren't specified, Giant Swarm will make use of defaults when creating the cluster.

**Note:** To learn about our current default values, available Kubernetes version, and valid ranges for the specifications for clusters, please contact us at support@giantswarm.io. We plan to offer simpler ways to inform you about current default values in the future.

In contrast to the example above, for AWS EC2 based clusters, worker nodes have to be specified by selecting an instance type. The following example shows how to select instance types for worker nodes instead. The keys `cpu`, `memory`, and `storage` are not applicable here.

```yaml
name: Example AWS Cluster
owner: myorg
workers:
  - aws:
      instance_type: m3.large
  - aws:
      instance_type: m3.large
  - aws:
      instance_type: m3.large
```

**Note:** As of now, in AWS based clusters all worker nodes must be of the same instance type. Based on your installation, only certain instance types may be available. Please contact the support team to learn which instance types are supported on your installation.

## Definition keys {#keys}

### Root level keys {#root-keys}

- `owner`: Name of the owner organization.
- `name`: Friendly name of the cluster. If not specified, a name will be generated.
- `kubernetes_version`: Kubernetes version to use, as a string, e. g. `1.4.6`.
- `workers`: Array of node definition objects describing each worker node. See below for possible keys. If not specified, the default number of worker nodes with default settings will be created.

### Node definition keys {#node-keys}

- `memory`: The sub-key `size_gb` allows to specify the amount of RAM to provide in a node using an integer or float value.
- `cpu`: The sub-key `cores` allows to require a number of CPU cores as integer.
- `storage`: The sub-key `size_gb` is used to specify the amount of local node storage in GB as an integer or decimal number.
- `labels`: Here, you can pass arbitrary key-value-pairs to be added as Kubernetes node labels. Values have to be of type string.
- `aws`: Settings specific to AWS based clusters
- `aws.instance_type`: The AWS EC2 instance type to use for a cluster, e. g. `m3.medium`.

## Related

- Learn how to create a cluster based on a definition file using [`gsctl create cluster`](../gsctl/create-cluster/)
