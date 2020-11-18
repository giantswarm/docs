---
title: Cluster Definition Reference
description: Complete documentation of the Giant Swarm cluster definition YAML format, compatible with API v4 and v5.
date: 2020-11-18
layout: subsection
weight: 100
user_questions:
  - What are additional fields I need to fill out for node pool clusters
  - What are node definition keys I need to specify for a non-node pool cluster definition?
  - What are root level keys I need to specify for a node pool cluster definition?
  - What are root level keys I need to specify for a non-node pool cluster definition?
  - What are the node pool definition keys I need to specify for a cluster definition? 
  - What goes into the 'masters' key of a cluster definition?
  - Will my cluster definition change if I use node pools?
---

# Cluster Definition Reference

Giant Swarm's cluster definition allows to define the detailed specs for a cluster in a YAML
format, which is then passed to [`gsctl create cluster`](/reference/gsctl/create-cluster/) in order to
create that cluster.

The cluster definition schema corresponds to a high degree with the Giant Swarm API schema for cluster
creation. As it's the case within the API, the YAML definition comes in two different versions:

- [**v4**](#v4): For a long time, this has been the only version around. As of now, this version is required
to create clusters on bare metal (**KVM**). It is also needed for cluster creation on
AWS using a tenant cluster release prior to v{{% first_aws_nodepools_version %}}, or on Azure using a tenant cluster release prior to v{{% first_azure_nodepools_version %}}, basically to create a cluster without
support for node pools.
- [**v5**](#v5): This version has been introduced in October 2019 to support clusters with
[node pools](/basics/nodepools/). The feature is available on AWS starting with tenant cluster release
v{{% first_aws_nodepools_version %}}, or on Azure starting with tenant cluster release v{{% first_azure_nodepools_version %}};

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
Also, we use the `availability_zones` field to spread the worker nodes over two availability zones.

```yaml
name: Example AWS Cluster
owner: myorg
scaling:
  min: 3
  max: 3
availability_zones: 2
workers:
  - aws:
      instance_type: m4.xlarge
```

**Note:** AWS clusters defined using a v4 definition (and consequently not using node pools) restrict you to all worker nodes being of the same instance type. With v5 and node pools, you gain the flexibility to create several node pools using different instance types.

### v4 Schema {#v4-schema}

#### v4 root level keys {#root-keys}

- `owner`: Name of the owner organization.
- `name`: Friendly name of the cluster. If not specified, a name will be generated.
- `release_version`: Allows to select a specific release version. The value must be the semantic version number (SemVer) of an active release. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command.
- `availability_zones`: Number of availability zones to use for worker nodes (on AWS and Azure only). Both the default value and the maximum can be obtained via the [Info endpoint](/api/#operation/getInfo) of the Giant Swarm API.
- `workers`: Array of node definition objects describing each worker node. See below for possible keys. If not specified, the default number of worker nodes with default settings will be created.

#### Node definition keys {#node-keys}

- `memory`: The sub-key `size_gb` allows to specify the amount of RAM to provide in a node using an integer or float value. Only usable on KVM (on-premises/bare metal) installations.
- `cpu`: The sub-key `cores` allows to require a number of CPU cores as integer. Only usable on KVM (on-premises/bare metal) installations.
- `storage`: The sub-key `size_gb` is used to specify the amount of local node storage in GB as an integer or decimal number. Only usable on KVM (on-premises/bare metal) installations.
- `aws`: Settings specific to AWS based clusters
- `aws.instance_type`: The AWS EC2 instance type to use for worker nodes, e.g. `m5.2xlarge`.
- `azure`: Settings specific to Azure based clusters
- `azure.vm_size`: The Azure VM size to use for worker nodes

## v5 Definition {#v5}

Let's start with an AWS example:

```yaml
api_version: v5
owner: myorg
release_version: 11.0.0
name: Test cluster with two node pools
master_nodes:
  high_availability: true
labels:
  locked: "false"
  environment: "testing"
nodepools:
- name: Node pool with 2 random AZs using defaults
  availability_zones:
    number: 2
- name: Node pool with 3 specific AZs A, B, C, m5.xlarge spot
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
      instance_distribution:
        on_demand_base_capacity: 3
        on_demand_percentage_above_base_capacity: 0
      instance_type: m5.xlarge
      use_alike_instance_types: true
```

Or an Azure example:

```yaml
api_version: v5
owner: myorg
release_version: 13.0.0
name: Test cluster with two node pools
master_nodes:
  high_availability: false
nodepools:
- name: Node pool with 2 random AZs using defaults
  availability_zones:
    number: 2
- name: Node pool with 3 specific AZs 1, 2, 3, Standard_E8a_v4
  availability_zones:
    zones:
    - 1
    - 2
    - 3
  scaling:
    min: 3
    max: 10
  node_spec:
    azure:
      vm_size: Standard_E8a_v4
```

Coming from v4, you might want to understand how v5 is different from v4:

- in v5, the key `api_version` is mandatory, and the value must be `v5`.
- Several settings that were specified on the cluster level in v4 (root level of the definition) have been moved to the node pool level.
- The key `master_nodes` has been added to allow influencing master nodes.

### v5 Schema {#v5-schema}

#### v5 root level keys {#v5-root-keys}

- `api_version`: Mandatory and must have the string value `v5`.
- `owner`: Name of the owner organization.
- `name`: Friendly name of the cluster. If not specified, a name will be generated.
- `release_version`: Allows to select a specific release version. The value must be the semver version number of an active release. To get information on all available releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command.
- `master_nodes`: Settings regarding the Kubernetes master nodes.
    - `high_availability`: Where supported, this is `true` by default, which means that the cluster will have three master nodes. Supported on AWS since release v{{% first_aws_ha_masters_version %}}. Set this to `false` to have only one master node in the cluster (recommended only for test clusters).
- `nodepools`: Here you can list your node pool definitions as explained below. Note that this is not mandatory, and you can also add node pools to a cluster after it has been created.
- `master` (deprecated):
    - `availability_zone`: Name of the availability zone to use for the master node. If not set, one will be assigned randomly.
- `labels`: Labels to be attached to this cluster.

**Note:** The `master_nodes` and `master` attribute must not be used in the same request/command, otherwise an HTTP error with status code 400 will be triggered.

#### Node pool definition keys {#v5-nodepool-keys}

- `name`: User-friendly name of the node pool, ideally indicating the purpose. Maximum of 100 characters allowed, must not contain control characters such as newline. If not set, a generic name will be assigned that can be changed later.
- `availability_zones`: Allows to influence the availability zone placement of the worker nodes. Either use `zones` to select specific ones or `number` to set the number of zones to use, if you are fine with random selection. If neither is specified, all worker nodes of this pool will be in the same availability zone, selected randomly. Setting both `zones` and `number` will cause an error.
    - `zones`: Array of availability zone names.
    - `number`: Number of availability zones to use.
- `node_spec`: Worker node specification details.
    - `aws`: AWS specific details.
        - `instance_distribution`: Attributes defining the instance distribution in the node pool being created. Added with AWS release v{{% first_aws_spotinstances_version %}}.
            - `on_demand_base_capacity`: Base capacity of on-demand EC2 instances to use for worker nodes in this pool. When this is larger than 0, this value defines a number of worker nodes that will be created using on-demand EC2 instances, regardless of the value configured as `on_demand_percentage_above_base_capacity`.
            - `on_demand_percentage_above_base_capacity`: Percentage of on-demand EC2 instances to use for worker nodes, instead of spot instances, for instances exceeding `on_demand_base_capacity`. For example, to have half of the worker nodes use spot instances and half use on-demand, set this value to 50.
        - `instance_type`: EC2 instance type to use for all worker nodes in this pool.
        - `use_alike_instance_types`: Boolean defining whether similar instance types can be used. See [our node pools documentation](/basics/nodepools/#similar-instance-types) for details.
    - `azure`: Azure specific details.
        - `vm_size`:  The Azure VM size to use for all worker nodes in this pool.
- `scaling`: Scaling or size range for the node pool. Setting `min` and `max` to the same value effectively disables autoscaling.
    - `min`: Minimum number of worker nodes in the pool. In other words, the lower limit for the autoscaler. Default: 3.
    - `max`: Maximum number of worker nodes in the pool or upper limit for the autoscaler. Default: 3.

## General notes on YAML

Chances are that you already work with YAML in various places. If not, here are some hints:

- In YAML, whitespace is important. Indentation must be made using blanks (space), not tabs.
- If in doubt, check your YAML in a linter. There are plenty online, e.g. [yamllint.com](http://www.yamllint.com/).
- JSON is valid YAML. If you prefer JSON's notation, just use valid JSON.
- You can add comments to YAML files by starting a line with the character `#`.

## Related

- [`gsctl create cluster`](/reference/gsctl/create-cluster/): Create a cluster based on flags, or a definition file
- [`gsctl create nodepool`](/reference/gsctl/create-nodepool/)
- [`gsctl list releases`](/reference/gsctl/list-releases/): Listing available releases
- [API: Create cluster (v4)](/api/#operation/addCluster)
- [API: Create cluster (v5)](/api/#operation/addClusterV5)
- [API: Create node pool](/api/#operation/addNodePool)
