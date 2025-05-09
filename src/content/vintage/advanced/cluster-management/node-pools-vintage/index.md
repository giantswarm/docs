---
linkTitle: Node pools (vintage)
title: Node pools (vintage)
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
aliases:
  - /advanced/cluster-management/node-pools-vintage
  - /basics/nodepools/
  - /guides/nodepools/
  - /advanced/nodepools/
  - /advanced/cluster-management/nodepools/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-04-04
---

{{< platform_support_table aws="beta=v10.0.0,ga=v11.0.0" azure="ga=v13.0.0" >}}

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

A node pool is identified by a unique ID that is generated on creation and by a name that you can pick as a cluster
administrator.

## Lifecycle

Node pools can be created when creating a cluster via the Giant Swarm web interface or any time after the cluster has been created

- via the Giant Swarm web interface
- via `kubectl` with the help of the [`gs` plugin]({{< relref "/reference/kubectl-gs/template-nodepool" >}})

Node pools can be modified and deleted using the web interface.

Once a node pool has been created, as soon as the workers are available, they will
join the cluster and appear in your `kubectl get nodes` listing. You can identify the
nodes' node pool using the `giantswarm.io/machine-deployment` label on AWS clusters and `giantswarm.io/machine-pool` label on Azure clusters.

The example `kubectl` command below will list all nodes with role, node pool ID, and name for an AWS cluster.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.kubernetes\.io/role}{"\t"}{.metadata.labels.giantswarm\.io/machine-deployment}{"\t"}{.metadata.name}{"\n"}{end}' | sort
master         ip-10-1-5-55.eu-central-1.compute.internal
worker  7zypn  ip-10-1-6-225.eu-central-1.compute.internal
worker  7zypn  ip-10-1-6-67.eu-central-1.compute.internal
```

Some details of a node pool can be modified after creation:

- The node pool name
- The scaling range (min/max) on AWS or fixed size on Azure.
- VM size (only on Azure)

Other settings like the availability zone assignment cannot be changed after creation.

## Assigning workloads to node pools {#assigning-workloads}

Knowing the node pool ID of the pool to use, you can use the `nodeSelector` method of assigning pods to the node pool.

Assuming that the node pool ID is `a1b2c`, your `nodeSelector` could for example look like this (for an AWS cluster):

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
    giantswarm.io/machine-deployment: a1b2c
```

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
    giantswarm.io/machine-pool: a1b2c
```

You can assign workloads to node pools in a more indirect way too. This is achieved by using other node attributes which are
specified via the node pool and which are exposed as node labels.

For example: In a case where you have node pools with one instance type. Using a `nodeSelector` with the label `node.kubernetes.io/instance-type` (or in Kubernetes before v1.17: `beta.kubernetes.io/instance-type`) you can assign workloads to matching nodes only.

Another example: In a case where you have different node pools using different availability zones. With a `nodeSelector` using the label `topology.kubernetes.io/zone` (or in Kubernetes before v1.17: `failure-domain.beta.kubernetes.io/zone`) you can assign your workload to the nodes in a particular availability zone.

## Node pool deletion

You can delete a node pool at any time using the Giant Swarm management API and user interfaces. When a node pool gets deleted the following things will happen:

- nodes in the pool will be marked as unschedulable and then drained, resulting in Pods being unassigned from the nodes
and containers being stopped (only on AWS clusters).
- Then the actual nodes will be removed.

If you are deleting a node pool running critical workloads, we recommend taking the following precautions:

- Make sure there is at least one node pool with enough nodes to pick up the workloads.
- Double-check any taints and node selectors of your workloads to make sure they can land on different nodes.
- For maximum control, cordon all of the node pool's nodes and then drain them manually, one by one.

Pay close attention to the workloads being rescheduled on other nodes once nodes are drained.

## On-demand and spot instances {#on-demand-spot}

As of workload cluster release v{{% first_aws_spotinstances_version %}} for AWS and v{{% first_azure_spotinstances_version %}} for Azure, node pools can contain a mix of [on-demand](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html) and [spot instances/VMs](https://aws.amazon.com/ec2/spot/) that will allow you to optimize your cost.

Please check our dedicated [section on spot instances/VMs]({{< relref "/vintage/advanced/cluster-management/spot-instances" >}}) to learn more about using them in your clusters.

## Using similar instance types {#similar-instance-types}

Starting with workload cluster release v{{% first_aws_spotinstances_version %}} for AWS you can activate the use of similar instance types per node pool. With this setting active, your node pool can use instance types that are nearly identical to the one you selected. For example, if you select `m5.xlarge`, the node pool can also use `m4.xlarge`.

Using multiple instance types in a node pool has some benefits:

- Together with spot instances, using multiple instance types allows better price optimization. Popular instance types tend to have more price adjustments. Allowing older-generation instance types that are less popular tends to result in lower costs and fewer interruptions.

- Even without spot instances, AWS has a limited number of instances per type in each Availability Zone. It can happen that your selected instance type is temporarily out of stock just in the moment you are in demand of more worker nodes. Allowing the node pool to use multiple instance types reduces this risk and increases the likelihood that your node pool can grow when in need.

Instances that contain the same amount of CPU and RAM are considered similar. We provide more information regarding which instance types are considered similar in our [reference]({{< relref "/vintage/advanced/cluster-management/spot-instances/aws/similar-instance-types" >}}).

## Node pools and autoscaling {#autoscaling}

With node pools, you set the autoscaling range per node pool (suppported on AWS clusters only). The Kubernetes cluster autoscaler has to decide which node pool to scale under which circumstances.

If you assign workloads to node pools as described [above](#assigning-workloads) and the autoscaler finds pods in `Pending` state, it will decide based on the node selectors which node pools to scale up.

In case there are workloads not assigned to any node pools, the autoscaler may pick any node pool for scaling. For details on the decision logic, please check the upstream FAQ for [AWS](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md).

## Limitations

- Clusters without worker nodes (= without node pools) cannot be considered fully functional. In order to have all
required components scheduled, worker nodes are required. For that reason, we deactivate any monitoring and alerts for
these clusters and don't provide any proactive support.

### AWS specific

- A node pool can have a maximum of 250 worker nodes. The architectural reason for this is that each node pool gets a `/24` IPv4 subnet assigned. However 5 IP addresses per availability zone used are not usable for worker nodes, as they are reserved for other AWS resources. Hence the limit depends on the number of availability zones used by a node pool. If the pool uses two zones, it's 245. With three zones, the limit is 240, and with four zones, it's 235.

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

## Azure specific

- Every node pool is mapped with a `Virtual Machine Scale Set`. That means that there is an upper bound of 100 nodes for each node pool.

- The maximum number of node pools for each workload cluster is 200.

## Further reading

- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) from the official Kubernetes documentation
