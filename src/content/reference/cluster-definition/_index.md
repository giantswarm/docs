---
title: Cluster Definition Reference
description: Complete documentation of the Giant Swarm cluster definition YAML format, compatible with API v4 and v5.
date: 2019-10-28
layout: subsection
weight: 100
---

# Cluster Definition Reference

<div class="well disclaimer">
This page mentions <a href="/basics/nodepools/">Node pools</a> which are a new concept to be introduced soon to Giant Swarm customers on AWS.
</div>

Giant Swarm's cluster definition allows to define the detailed specs for a cluster in a YAML
format, which is then passed to [`gsctl create cluster`](/reference/gsctl/create-cluster/) in order to
create that cluster.

The cluster definition schema corresponds to a high degree with the Giant Swarm API schema for cluster
creation. As it's the case within the API, the YAML definition comes in two different versions:

- [**v4**](#v4): For a long time, this has been the only version around. As of now, this version is required
to create clusters on **Azure** and on bare metal (**KVM**). It is also needed for cluster creation on
AWS using a release prior to {{% first_aws_nodepools_version %}}, basically to create a cluster without
support for node pools.

- [**v5**](#v5): This version has been introduced in October 2019 to support clusters with
[node pools](/basics/nodepools/). The feature is available on AWS starting with release
{{% first_aws_nodepools_version %}}.

As it's the case with the Giant Swarm API, cluster creation using the YAML definition only requires you
to specify the details you need to deviate from defaults. For every setting not contained in the
definition, defaults will apply as explained below. For any missing information regarding defaults,
please contact your Giant Swarm support team via Slack or at support@giantswarm.io.

## v4 Definition {#v4}

### Examples

The following example defines a bare metal/KVM cluster with three worker nodes:

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

**Note:** AWS clusters defined using a v4 definition (and consequently not using node pools) restrict you to all worker nodes being of the same instance type. With v5 and node pools, you gain the flexibility to create several node pools using different instance types.

### Schema {#v4-schema}

#### Root level keys {#root-keys}

- `owner`: Name of the owner organization.
- `name`: Friendly name of the cluster. If not specified, a name will be generated.
- `workers`: Array of node definition objects describing each worker node. See below for possible keys. If not specified, the default number of worker nodes with default settings will be created.
- `release_version`: Allows to select a specific release version. The value must be the semver version number of an active release. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command.

#### Node definition keys {#node-keys}

- `memory`: The sub-key `size_gb` allows to specify the amount of RAM to provide in a node using an integer or float value. Only usable on KVM (on-premises/bare metal) installations.
- `cpu`: The sub-key `cores` allows to require a number of CPU cores as integer. Only usable on KVM (on-premises/bare metal) installations.
- `storage`: The sub-key `size_gb` is used to specify the amount of local node storage in GB as an integer or decimal number. Only usable on KVM (on-premises/bare metal) installations.
- `aws`: Settings specific to AWS based clusters
- `aws.instance_type`: The AWS EC2 instance type to use for worker nodes, e. g. `m5.large`.
- `azure`: Settings specific to Azure based clusters
- `azure.vm_size`: The Azure VM size to use for worker nodes

## v5 Definition {#v5}

Let's start with an example:

```yaml
api_version: "v5"
release_version: "11.0.0"
name: "Test cluster with two node pools"
master:
  availability_zone: "eu-central-1a"
nodepools:
- name: "Node pool with 2 random AZs using defaults"
  availability_zones:
    number: 2
- name: "Node pool with 3 specific AZs A, B, C, m5.xlarge"
  availability_zones:
    zones:
    - "eu-central-1a"
    - "eu-central-1b"
    - "eu-central-1c"
  scaling:
    min: 3
    max: 10
  node_spec:
    aws:
      instance_type: "m5.xlarge"
```

Coming from v4, you might want to understand how v5 is different from v4:

- in v5, the key `api_version` is mandatory and the value must be `v5`.
- Several settings that were specified on the cluster level in v4 (root level of the definition) have been moved to the node pool level.
- The key `master` has been added to allow influencing in which availability zone the master node will be placed.

### Schema {#v5-schema}

#### Root level keys

- `api_version`: Mandatory and must have the string value `v5`.
- `owner`: Name of the owner organization.
- `name`: Friendly name of the cluster. If not specified, a name will be generated.
- `release_version`: Allows to select a specific release version. The value must be the semver version number of an active release. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command.
- `master`:
  - `availability_zone`: Name of the availability zone to use for the master node. If not set, one will be assigned randomly.
- `nodepools`: Here you can list your node pool definitions as explained below. Note that this is not mandatory and you can also add node pools to a cluster after it has been created.

#### Node pool definition keys

- `name`: User-friendly name of the node pool, ideally indicating the purpose. Maximum of 100 characters allowed, must not contain control characters such as newline. If not set, a generic name will be assigned that can be changed later.
- `availability_zones`: Allows to influence the availability zone placement of the worker nodes. Either use `zones` to select specific ones or `number` to set the number of zones to use, if you are fine with random selection. If neither is specified, all worker nodes of this pool will be in the same availability zone, selected randomly. Setting both `zones` and `number` will cause an error.
  - `zones`: Array of availability zone names.
  - `number`: Number of availability zones to use.
- `node_spec`: Worker node specification details.
  - `aws`: AWS specific details
    - `instance_type`: EC2 instance type to use for all worker nodes in this pool.
- `scaling`: Scaling or size range for the node pool. Setting `min` and `max` to the same value effectively disables autoscaling.
  - `min`: Minimum number of worker nodes in the pool. In other words, the lower limit for the autoscaler. Default: 3.
  - `max`: Maximum number of worker nodes in the pool or upper limit for the autoscaler. Default: 3.

## General notes on YAML

Chances are that you already work with YAML in various places. If not, here are some hints:

- In YAML, whitespace is important. Indentation must be made using blanks (space), not tabs.
- If in doubt, check your YAML in a linter. There are plenty online, e. g. [yamllint.com](http://www.yamllint.com/).
- JSON is valid YAML. If you prefer JSON's notation, just use valid JSON.
- You can add comments to YAML files by starting a line with the character `#`.


## Related

- [`gsctl create cluster`](/reference/gsctl/create-cluster/): Create a cluster based on flags or a definition file
- [`gsctl create nodepool`](/reference/gsctl/create-nodepool/)
- [`gsctl list releases`](/reference/gsctl/list-releases/): Listing available releases
- [API: Create cluster (v4)](/api/#operation/addCluster)
- [API: Create cluster (v5)](/api/#operation/addClusterV5)
- [API: Create node pool](/api/#operation/addNodePool)
