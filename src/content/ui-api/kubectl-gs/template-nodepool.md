---
linkTitle: template nodepool
title: "'kubectl gs template nodepool' command reference"
description: Reference documentation on how to create a manifest for a node pool using 'kubectl gs'.
weight: 80
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-nodepool/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - How can I create a node pool manifest for the Management API?
---

# `kubectl gs template nodepool`

{{% kgs_alias_assumption %}}

Node pools are groups of worker nodes sharing common configuration. In terms of custom resources they consist of custom resources of type

The outcome depends on the provider, set via the `--provider` flag:

For AWS (`--provider aws`):

- [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1alpha2`)
- [`AWSMachineDeployment`]({{< relref "/ui-api/management-api/crd/awsmachinedeployments.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha2`)

For Azure (`--provider azure`):

- [`MachinePool`]({{< relref "/ui-api/management-api/crd/machinepools.exp.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1alpha3`)
- [`AzureMachinePool`]({{< relref "/ui-api/management-api/crd/azuremachinepools.exp.infrastructure.cluster.x-k8s.io.md" >}}) (API version `exp.infrastructure.cluster.x-k8s.io/v1alpha3`)
- [`Spark`]({{< relref "/ui-api/management-api/crd/sparks.core.giantswarm.io.md" >}}) (API version `core.giantswarm.io/v1alpha1`)

## Usage

To create the manifests for a new node pool, use this command:

```nohighlight
kgs template nodepool
```

Here are the supported flags:

- `--provider` - The infrastructure provider, either `aws` or `azure`.
- `--availability-zones` - list of availability zones to use, instead of setting a number. Use comma to separate values. (e. g. `eu-central-1a,eu-central-1b`)
- `--cluster-id` - ID of the cluster the node pool should be added to.
- `--nodepool-name` - node pool name or purpose description of the node pool. (default *Unnamed node pool*)
- `--nodes-max` - maximum number of worker nodes for the node pool. (default 10)
- `--nodes-min` - minimum number of worker nodes for the node pool. (default 3)
- `--num-availability-zones` - number of availability zones to use. (default 1)
- `--owner` - organization, owning workload cluster. Must be configured with existing organization in installation.

### AWS specific

- `--aws-instance-type`- EC2 instance type to use for workers, e. g. *m5.2xlarge*. (default *m5.xlarge*)

### Azure specific

- `--azure-vm-size` - Azure VM size to use for workers (e.g. *Standard_D4s_v3*).

## Example

```nohighlight
kgs template nodepool \
  --provider aws \
  --cluster-id a1b2c \
  --nodepool-name "General purpose" \
  --availability-zones eu-central-1a \
  --owner acme \
  --aws-instance-type m5.4xlarge \
```

## Output

The above example command would generate the following output:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: MachineDeployment
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: o4omf
    giantswarm.io/machine-deployment: fo2xh
    giantswarm.io/organization: giantswarm
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
    giantswarm.io/cluster: o4omf
    giantswarm.io/machine-deployment: fo2xh
    giantswarm.io/organization: giantswarm
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
