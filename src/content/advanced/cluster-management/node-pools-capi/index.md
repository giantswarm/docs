---
linkTitle: Node pools (CAPI)
title: Node pools (CAPI)
description: A general description of node pools as a concept, its benefits, and some details you should be aware of.
weight: 50
menu:
  main:
    parent: advanced-cluster-management
user_questions:
  - What is a node pool?
  - What are node pools?
  - In which cloud environments are node pools supported?
  - Which workload cluster releases introduced node pools?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-11-22
---

## Definition

A node pool is a set of nodes within a Kubernetes cluster that share the same configuration (machine type, CIDR range, etc.). Each node in the pool is labeled by the node pool's name.

## Advantages

Prior to the introduction of node pools, a cluster could only comprise one type of worker node. The cluster would have
to be scaled as a whole, and the availability zone distribution would apply to all worker nodes of a cluster. This
would mean that every worker node would have to be big enough to run the largest possible workload, in terms of
memory and CPU resources required. At the same time, all worker nodes in the cluster would have to use the same
availability zone distribution, even if some workloads wouldn't require the increased availability.

Node pools are independent groups of worker nodes belonging to a cluster, where all nodes within a pool share a
common configuration. You can combine any type of node pool within one cluster. Node pools can differ regarding:

- Machine type
- Availability zone distribution
- Scaling configuration (number of nodes)

A node pool is identified by a name that you can pick as a cluster administrator. The name of the node pool is set as a label on all nodes belonging to the pool.

## Configuration

Node pools can be created, deleted or updated by changing the configuration used when creating the cluster using [`kubectl`]({{< relref "/getting-started/create-workload-cluster" >}})

{{< tabs >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2" >}}

```nohighlight
kubectl gs template cluster --provider capa --name a1b2c3 \
  --organization giantswarm \
  --description "my test cluster" \
  --machine-pool-name pool0 \
  --machine-pool-min-size 3 \
  --machine-pool-max-size 5 \
  --machine-pool-instance-type r6i.xlarge
```

The node pool name will be prepended by the cluster name. In the example above, the node pool name will be `a1b2c3-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the  `giantswarm.io/machine-pool` label.
You can identify the nodes' node pool using that label.
The example `kubectl` command below will list all nodes with role, node pool name, and node name.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.kubernetes\.io/role}{"\t"}{.metadata.labels.giantswarm\.io/machine-pool}{"\t"}{.metadata.name}{"\n"}{end}' | sort
master         ip-10-1-5-55.eu-central-1.compute.internal
worker  a1b2c3-pool0  ip-10-1-6-225.eu-central-1.compute.internal
worker  a1b2c3-pool0  ip-10-1-6-67.eu-central-1.compute.internal
```

{{< /tab >}}
{{< tab id="cluster-capz-azure-vms" for-impl="capz_vms" >}}

```nohighlight
kubectl gs template cluster --provider capz --name test-cluster \
  --organization giantswarm \
  --description "my test cluster" \
  --machine-pool-name pool0 \
  --machine-pool-min-size 3 \
  --machine-pool-max-size 5 \
  --machine-pool-instance-type r6i.xlarge
```

The node pool name will be prepended by the cluster name. In the example above, the node pool name will be `a1b2c3-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the  `giantswarm.io/machine-deployment` label.
You can identify the nodes' node pool using that label.
The example `kubectl` command below will list all nodes with role, node pool name, and node name.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.kubernetes\.io/role}{"\t"}{.metadata.labels.giantswarm\.io/machine-deployment}{"\t"}{.metadata.name}{"\n"}{end}' | sort
master         ip-10-1-5-55.eu-central-1.compute.internal
worker  a1b2c3-pool0  ip-10-1-6-225.eu-central-1.compute.internal
worker  a1b2c3-pool0  ip-10-1-6-67.eu-central-1.compute.internal
```

{{< /tab >}}
{{< /tabs >}}

## Assigning workloads to node pools {#assigning-workloads}

Knowing the node pool name of the pool to use, you can use the `nodeSelector` method of assigning pods to the node pool.

Assuming that the node pool name is `pool0`, and the cluster name is `a1b2c3`, your `nodeSelector` could for example look like this:

{{< tabs >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2" >}}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    giantswarm.io/machine-pool: a1b2c3-pool0
```

{{< /tab >}}
{{< tab id="cluster-capz-azure-vms" for-impl="capz_vms" >}}

```yaml
A similar example for an Azure cluster:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    giantswarm.io/machine-deployment: a1b2c3-pool0
```

{{< /tab >}}
{{< /tabs >}}

You can assign workloads to node pools in a more indirect way too. This is achieved by using other node attributes which are
specified via the node pool and which are exposed as node labels.

For example: In a case where you have node pools with one instance type. Using a `nodeSelector` with the label `node.kubernetes.io/instance-type` you can assign workloads to matching nodes only.

Another example: In a case where you have different node pools using different availability zones. With a `nodeSelector` using the label `topology.kubernetes.io/zone` you can assign your workload to the nodes in a particular availability zone.

## Using mixed instance types {#mixed-instance-types}

**Note:** This feature was called ["Similar instance types" on vintage]({{< relref "/advanced/cluster-management/node-pools-vintage#similar-instance-types" >}}).

On AWS EC2 (CAPA) you can override the instance type of the node pool to enable [mixed instances policy on AWS](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateOverrides.html).
This can provide Amazon EC2 Auto Scaling with a larger selection of instance types to choose from when fulfilling node capacities.

You can set the `instanceTypeOverrides` value when defining your node pool in the cluster values. For example:

```yaml
metadata:
  description: "my cluster"
  name: test-cluster
  organization: giantswarm
nodePools:
  nodepool0:
    maxSize: 4
    minSize: 3
    instanceTypeOverrides:
    - r6i.xlarge
    - r5.xlarge
    - m5.xlarge
```

Please notice that when setting `instanceTypeOverrides`, the `instanceType` value will be ignored, and the instance types defined in `instanceTypeOverrides` will be used instead.
Also, the order in which we define the instance types in `instanceTypeOverrides` is important.
The first instance type in the list that is available in the selected availability zone will be used.

Using multiple instance types in a node pool has some benefits:

- Together with spot instances, using multiple instance types allows better price optimization. Popular instance types tend to have more price adjustments. Allowing older-generation instance types that are less popular tends to result in lower costs and fewer interruptions.

- Even without spot instances, AWS has a limited number of instances per type in each Availability Zone. It can happen that your selected instance type is temporarily out of stock just in the moment you are in demand of more worker nodes. Allowing the node pool to use multiple instance types reduces this risk and increases the likelihood that your node pool can grow when in need.

## Node pools and autoscaling {#autoscaling}

With node pools, you set the autoscaling range per node pool (suppported on AWS EC2 (CAPA) clusters only). The Kubernetes cluster autoscaler has to decide which node pool to scale under which circumstances.

If you assign workloads to node pools as described [above](#assigning-workloads) and the autoscaler finds pods in `Pending` state, it will decide based on the node selectors which node pools to scale up.

In case there are workloads not assigned to any node pools, the autoscaler may pick any node pool for scaling. For details on the decision logic, please check the upstream FAQ for [AWS](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md).

## Limitations

- Clusters without worker nodes (= without node pools) cannot be considered fully functional. In order to have all
required components scheduled, worker nodes are required. For that reason, we deactivate any monitoring and alerts for
these clusters and don't provide any proactive support.

### Things to keep in mind

{{< tabs >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2" >}}

- At times, the EC2 instance type required by a node pool can be unavailable in certain availability zones. This can
result in node pools providing less than the desired number of nodes. The more availability zones a node pool spans,
the less likely this problem is to occur.

- By default, clusters can have up to 5 node pools. This is limited by the AWS service quota named "IPv4 CIDR blocks
per VPC" in the [VPC section](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). As the AWS
account owner, you can request an increase of this limit via the AWS console.

- Node pools can span a maximum of four availability zones. This limit affects both the number of availability zones
a single node pool can cover, as well as the number of different availability zones all node pools of a cluster can
cover. Once an availability zone has been assigned for use in a cluster, either for a control plane node or for worker
nodes, it cannot be unassigned from that cluster. It will remain assigned even if there are no more node pools using
that availability zone.

    - **Example:** The control plane node(s) are in availability zone A. Node pool 1 uses availability zones B and C. Node pool 2 uses
  availability zone D. With A, B, C, and D, the limit of four availability zones assigned is reached. New node pools of this
  cluster can only use these four availability zones.

{{< /tab >}}
{{< /tabs >}}

## Further reading

- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) from the official Kubernetes documentation
