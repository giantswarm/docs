---
title: kubectl gs template nodepool
description: Reference documentation on how to create a manifest for a node pool using 'kubectl gs'.
date: 2020-10-02
type: page
weight: 10
---

# `kubectl gs template nodepool`

{{% kgs_alias_assumption %}}

Node pools are groups of worker nodes sharing common configuration. In terms of custom resources they consist of custom resources of type

The outcome depends on the provider, set via the `--provider` flag:

For AWS (`--provider aws`):

- [`MachineDeployment`](/reference/cp-k8s-api/machinedeployments.cluster.x-k8s.io/) (API version `cluster.x-k8s.io/v1alpha2`)
- [`AWSMachineDeployment`](/reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io/) (API version `infrastructure.giantswarm.io/v1alpha2`)

For Azure (`--provider azure`):

- [`MachinePool`](/reference/cp-k8s-api/machinepools.exp.cluster.x-k8s.io/) (API version `cluster.x-k8s.io/v1alpha3`)
- [`AzureMachinePool`](/reference/cp-k8s-api/azuremachinepools.exp.infrastructure.cluster.x-k8s.io/) (API version `exp.infrastructure.cluster.x-k8s.io/v1alpha3`)
- [`Spark`](/reference/cp-k8s-api/sparks.core.giantswarm.io/) (API version `core.giantswarm.io/v1alpha1`)

## Usage

To create the manifests for a new node pool, use this command:

```nohighlight
kubectl gs template nodepool
```

Here are the supported flags:

- `--provider` - The infrastructure provider, either `aws` or `azure`.
- `--availability-zones` - list of availability zones to use, instead of setting a number. Use comma to separate values. (e. g. `eu-central-1a,eu-central-1b`)
- `--cluster-id` - ID of the cluster the node pool should be added to.
- `--nodepool-name` - node pool name or purpose description of the node pool. (default *Unnamed node pool*)
- `--nodex-max` - maximum number of worker nodes for the node pool. (default 10)
- `--nodex-min` - minimum number of worker nodes for the node pool. (default 3)
- `--num-availability-zones` - number of availability zones to use. (default 1)
- `--owner` - organization, owning tenant cluster. Must be configured with existing organization in installation.
- `--release` - valid release version.
Can be retrieved with `gsctl list releases` for your installation. Only versions *10.x.x*+ support cluster CRs.
- `--release-branch` (optional) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the release set via the `--release` flag (default: `master`).

### AWS specific

- `--aws-instance-type`- EC2 instance type to use for workers, e. g. *m5.2xlarge*. (default *m5.xlarge*)
- `--region` - tenant cluster AWS region. Must be configured with installation region.

### Azure specific

- `--azure-vm-size` - Azure VM size to use for workers (e.g. *Standard_D4s_v3*).

## Example

```nohighlight
kgs template nodepool \
  --provider aws \
  --cluster-id a1b2c \
  --nodepool-name "General purpose" \
  --region eu-central1 \
  --availability-zones eu-central-1b \
  --owner acme \
  --aws-instance-type m5.4xlarge \
  --release 11.2.1
```

## Output

The above example command would generate the following output:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: MachineDeployment
metadata:
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: 2.1.10
    giantswarm.io/cluster: o4omf
    giantswarm.io/machine-deployment: fo2xh
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.2.1
  name: fo2xh
  namespace: default
spec:
  selector: {}
  template:
    metadata: {}
    spec:
      bootstrap: {}
      infrastructureRef:
        apiVersion: infrastructure.giantswarm.io/v1alpha2
        kind: AWSMachineDeployment
        name: fo2xh
        namespace: default
      metadata: {}
status: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSMachineDeployment
metadata:
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: 8.4.0
    giantswarm.io/cluster: o4omf
    giantswarm.io/machine-deployment: fo2xh
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.2.1
  name: fo2xh
  namespace: default
spec:
  nodePool:
    description: Unnamed node pool
    machine:
      dockerVolumeSizeGB: 100
      kubeletVolumeSizeGB: 100
    scaling:
      max: 10
      min: 3
  provider:
    availabilityZones:
    - eu-central-1a
    worker:
      instanceType: m5.xlarge
```
