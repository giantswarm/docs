---
linkTitle: template nodepool
title: "'kubectl gs template nodepool' command reference"
description: Reference documentation on how to create a manifest for a node pool using 'kubectl gs'.
weight: 100
menu:
  principal:
    parent: reference-kubectlgs
user_questions:
  - How can I create a node pool manifest for the platform API?
last_review_date: 2024-11-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
aliases:
  - /vintage/use-the-api/kubectl-gs/template-nodepool/
---

The `template nodepool` command allows to create [node pools]({{< relref "/vintage/advanced/cluster-management/node-pools-vintage" >}}), which are groups of worker nodes in a cluster sharing common configuration. The command creates a manifest for the custom resources that define a node pool. These are then meant to be applied to the management cluster, e.g. via `kubectl apply`.

## Provider support

This command **does not support Cluster API** (CAPI) based workload clusters. It only supports AWS and Azure before CAPI. Adding a node pool to a CAPI workload cluster requires modification of the cluster app configuration values.

| Provider | `--provider` flag value |
|-|-|
| AWS | `aws` |
| Azure | `azure` |

## Resources generated

The resulting resources depend on the provider, set via the `--provider` flag.

{{< tabs >}}
{{< tab id="flags-aws" for-impl="vintage_aws">}}

- [`MachineDeployment`]({{< relref "/vintage/use-the-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`)
- [`AWSMachineDeployment`]({{< relref "/vintage/use-the-api/management-api/crd/awsmachinedeployments.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`)

{{< /tab >}}
{{< /tabs >}}

## Usage

To create the manifests for a new node pool, use this command:

```nohighlight
kubectl gs template nodepool
```

Here are the supported flags:

- `--provider` - The infrastructure provider, either `aws` or `azure`.
- `--availability-zones` - list of availability zones to use, instead of setting a number. Use comma to separate values. (e.g. `eu-central-1a,eu-central-1b`)
- `--cluster-name` - Unique identifier of the cluster the node pool should be added to.
- `--description` - User-friendly description of the purpose of the node pool. (default *Unnamed node pool*)
- `--nodes-max` - maximum number of worker nodes for the node pool. (default 10)
- `--nodes-min` - minimum number of worker nodes for the node pool. (default 3)
- `--output` - Sets a file path to write the output to. If not set, standard output will be used.
- `--organization` - Name of the organization owning the cluster.
- `--release` - The workload cluster release version.

### AWS specific

- `--aws-instance-type` - EC2 instance type to use for workers, e.g. *m5.2xlarge*. (default *m5.xlarge*)
- `--use-alike-instance-types` - Enables the use of instance types similar to the one specified via `--aws-instance-type` (default: false). This can increase the likelihood of getting the required instances, especially when requesting spot instances. See [our reference]({{< relref "/vintage/advanced/cluster-management/spot-instances/aws/similar-instance-types" >}}) for details.
- `--on-demand-percentage-above-base-capacity` - To use only on-demand instances, set this to 100. For any other value, the remainder to 100 will be filled with spot instances. For example, 50 will create a node pool that is half spot and half on-demand instances. 0 (zero) will use only spot instances. See [our AWS spot instances docs]({{< relref "/vintage/advanced/cluster-management/spot-instances/aws" >}}) for more information.
- `--on-demand-base-capacity` - Can be used to set a fixed number of on-demand instances, regardless of the percentage (see above) of spot vs. on-demand to be used otherwise.
- `--machine-deployment-subnet`: Size of the IPv4 subnet to reserve for the node pool. Must be a number between 20 and 28. For example, 24 stands for a /24 subnet with 256 addresses. Check the [`alpha.aws.giantswarm.io/aws-subnet-size`]({{< relref "/vintage/use-the-api/management-api/crd/awsmachinedeployments.infrastructure.giantswarm.io.md#v1alpha2-alpha.aws.giantswarm.io/aws-subnet-size" >}}) annotation for details.

### Azure specific

- `--azure-vm-size` - Azure VM size to use for workers (e.g. *Standard_D4s_v3*).
- `--azure-spot-vms` - Whether to use spot VMs for this node pool (defaults to false which means not to use spot VMs).
- `--azure-spot-vms-max-price` - Max hourly price in USD to pay for one spot VM. If the current price for the VM is exceeded, the VM is deleted. If not set, the on-demand price for the same machine size is used as limit.

## Examples

{{< tabs >}}
{{< tab id="command-examples-aws" for-impl="vintage_aws">}}

```nohighlight
kubectl gs template nodepool \
  --provider aws \
  --organization acme \
  --cluster-name a1b2c \
  --description "General purpose" \
  --availability-zones eu-central-1a \
  --aws-instance-type m5.4xlarge \
  --release 17.0.0
```

{{< /tab >}}
{{< /tabs >}}

## Output

The above example command would generate the following output:

{{< tabs >}}
{{< tab id="command-output-aws" for-impl="vintage_aws">}}

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineDeployment
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/machinedeployments.cluster.x-k8s.io/
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: 3.13.0
    cluster.x-k8s.io/cluster-name: a1b2c
    giantswarm.io/cluster: a1b2c
    giantswarm.io/machine-deployment: p3a9q
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
  name: p3a9q
  namespace: org-acme
spec:
  clusterName: a1b2c
  selector: {}
  template:
    metadata: {}
    spec:
      bootstrap: {}
      clusterName: a1b2c
      infrastructureRef:
        apiVersion: infrastructure.giantswarm.io/v1alpha3
        kind: AWSMachineDeployment
        name: p3a9q
        namespace: org-acme
status: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: AWSMachineDeployment
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/awsmachinedeployments.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: 10.7.0
    cluster.x-k8s.io/cluster-name: a1b2c
    giantswarm.io/cluster: a1b2c
    giantswarm.io/machine-deployment: p3a9q
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
  name: p3a9q
  namespace: org-acme
spec:
  nodePool:
    description: General purpose
    machine:
      dockerVolumeSizeGB: 100
      kubeletVolumeSizeGB: 100
    scaling:
      max: 10
      min: 3
  provider:
    availabilityZones:
    - eu-central-1a
    instanceDistribution:
      onDemandBaseCapacity: 0
      onDemandPercentageAboveBaseCapacity: 100
    worker:
      instanceType: m5.4xlarge
      useAlikeInstanceTypes: false
status:
  provider:
    worker: {}
```

{{< /tab >}}
{{< /tabs >}}
