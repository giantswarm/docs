---
linkTitle: Node pools (CAPI)
title: Node pools (CAPI)
description: A general description of node pools as a concept, its benefits, and some details you should be aware of.
weight: 45
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

A node pool is a set of nodes within a Kubernetes cluster that share the same configuration (machine type, operating system, etc.).
Each node in the pool is labeled by the node pool's name.

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
- Node labels (the pool name is added as node label by default)

## Configuration

Node pools can be created, deleted or updated by changing the configuration used when creating the cluster using [`kubectl-gs`]({{< relref "/getting-started/create-workload-cluster" >}})

{{< tabs >}}
{{< tab id="nodepool-capa-config" for-impl="nodepool-config" >}}

```nohighlight
kubectl gs template cluster --provider capa --name mycluster \
  --organization giantswarm \
  --description "my test cluster" \
  --machine-pool-name pool0 \
  --machine-pool-min-size 3 \
  --machine-pool-max-size 5 \
  --machine-pool-instance-type r6i.xlarge
```

A node pool is identified by a name that you can pick as a cluster administrator. The name must follow these rules:

- must be between 5 and 20 characters long
- must start with a lowercase letter or number
- must end with a lowercase letter or number
- must contain only lowercase letters, numbers, and dashes

For example, `pool0`, `group-1` are valid node pool names.

The node pool name will be prepended by the cluster name. In the example above, the node pool name will be `mycluster-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the `giantswarm.io/machine-pool` label.
You can identify the nodes' node pool using that label.
The example `kubectl` command below will list all nodes with role, node pool name, and node name.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.kubernetes\.io/role}{"\t"}{.metadata.labels.giantswarm\.io/machine-pool}{"\t"}{.metadata.name}{"\n"}{end}' | sort
master         ip-10-1-5-55.eu-central-1.compute.internal
worker  mycluster-pool0  ip-10-1-6-225.eu-central-1.compute.internal
worker  mycluster-pool0  ip-10-1-6-67.eu-central-1.compute.internal
```

{{< /tab >}}
{{< tab id="nodepool-capz-config" for-impl="nodepool-config" >}}

```nohighlight
kubectl gs template cluster --provider capz --name test-cluster \
  --organization giantswarm \
  --description "my test cluster" \
  --machine-pool-name pool0 \
  --machine-pool-min-size 3 \
  --machine-pool-max-size 5 \
  --machine-pool-instance-type Standard_D4s_v5
```

The node pool name will be prepended by the cluster name. In the example above, the node pool name will be `mycluster-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the `giantswarm.io/machine-deployment` label.
You can identify the nodes' node pool using that label.
The example `kubectl` command below will list all nodes with role, node pool name, and node name.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.kubernetes\.io/role}{"\t"}{.metadata.labels.giantswarm\.io/machine-deployment}{"\t"}{.metadata.name}{"\n"}{end}' | sort
master         mycluster-control-plane-34c45e6e-rrpnn
worker  mycluster-pool0  mycluster-pool0-8268227a-56x9n
worker  mycluster-pool0  mycluster-pool0-8268227a-hjf69
```

{{< /tab >}}
{{< /tabs >}}

## Assigning workloads to node pools {#assigning-workloads}

Knowing the node pool name of the pool to use, you can use the [`nodeSelector` method of assigning pods](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) to the node pool.

Assuming that the node pool name is `pool0`, and the cluster name is `mycluster`, your `nodeSelector` could for example look like this:

{{< tabs >}}
{{< tab id="nodepool-capa-scheduling" for-impl="nodepool-config" >}}

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
    giantswarm.io/machine-pool: mycluster-pool0
```

{{< /tab >}}
{{< tab id="nodepool-capz-scheduling" for-impl="nodepool-config" >}}

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
    giantswarm.io/machine-deployment: mycluster-pool0
```

{{< /tab >}}
{{< /tabs >}}

You can assign workloads to node pools in a more indirect way too.
[There is a set of labels](https://kubernetes.io/docs/reference/labels-annotations-taints/) that are automatically added by Kubernetes to all nodes, that you can use for scheduling.

For example: you have several node pools with different instance types. Using a `nodeSelector` with the label `node.kubernetes.io/instance-type`, you can assign workloads only to matching nodes.

Another example: you have different node pools using different availability zones. With a `nodeSelector` using the label `topology.kubernetes.io/zone`, you can assign your workload to the nodes in a particular availability zone.

## Adding more node pools

You can add new node pools at any time. You just need to update the cluster configuration and specify the details of the node pools that you want to add.

For example, if this was the cluster configuration

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

We can add a new node pool like this

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
  nodepool1:
    instanceType: m5.xlarge
    maxSize: 3
    minSize: 1
```

## Updating an existing node pool

Instances in the node pool will be rolled whenever these properties are changed in the node pool definition:
- `instanceType`
- `additionalSecurityGroups`

Instances will also be rolled if these values are changed:
- `providerSpecific.ami`

### What happens when a node pool is updated

When node pool instances need to be rolled, each instance receives a terminate signal from AWS.
This is propagated as shutdown signal to the OS and then to each running process like the `kubelet`, which will send a `NodeShutDown` event to the pod.

The `kubelet` will wait up to 5 minutes for all pods to terminate and after that it will terminate itself and the shutdown of the AWS EC2 instance will finally proceed.

Please, be aware that it may happen that AWS decides to force-terminate the instance before the 5 minutes. We recommend draining the respective nodes and moving workloads to other nodes before such an update operation.

## Node pool deletion

TBD

## Using mixed instance types (only {{% impl_title "capa_ec2" %}}) {#mixed-instance-types}

**Note:** This feature was called ["Similar instance types" on vintage]({{< relref "/advanced/cluster-management/node-pools-vintage#similar-instance-types" >}}).

On {{% impl_title "capa_ec2" %}}, you can override the instance type of the node pool to enable [mixed instances policy on AWS](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateOverrides.html).
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

**Note:** Changing the `instanceTypeOverrides` value won't trigger a rolling update of the node pool.

Using multiple instance types in a node pool has some benefits:

- Together with spot instances, using multiple instance types allows better price optimization. Popular instance types tend to have more price adjustments. Allowing older-generation instance types that are less popular tends to result in lower costs and fewer interruptions.

- Even without spot instances, AWS has a limited number of instances per type in each Availability Zone. It can happen that your selected instance type is temporarily out of stock just in the moment you are in demand of more worker nodes. Allowing the node pool to use multiple instance types reduces this risk and increases the likelihood that your node pool can grow when in need.

## Node pools and autoscaling {#autoscaling}

With node pools, you set the autoscaling range per node pool (suppported on {{% impl_title "capa_ec2" %}} clusters only). The Kubernetes cluster autoscaler has to decide which node pool to scale under which circumstances.

If you assign workloads to node pools as described [above](#assigning-workloads) and the autoscaler finds pods in `Pending` state, it will decide based on the node selectors which node pools to scale up.

In case there are workloads not assigned to any node pools, the autoscaler may pick any node pool for scaling. For details on the decision logic, please check the upstream FAQ for [AWS](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md).

## On-demand and spot instances {#on-demand-spot}

{{< tabs >}}
{{< tab id="nodepool-capa-spot-instances" for-impl="nodepool-spot" >}}

Node pools can make use of [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/). On the node pool definition, you can enable it and select the maximum price to pay.

```yaml
metadata:
  description: "my cluster"
  name: test-cluster
  organization: giantswarm
nodePools:
  pool0:
    maxSize: 2
    minSize: 2
    spotInstances:
      enabled: true
      maxPrice: 1.2
```

{{< /tab >}}
{{< tab id="nodepool-capz-spot-instances" for-impl="nodepool-spot" >}}

This is currently not supported.

{{< /tab >}}
{{< /tabs >}}

## Limitations

- Clusters without worker nodes (= without node pools) cannot be considered fully functional. In order to have all
required components scheduled, worker nodes are required. For that reason, we deactivate any monitoring and alerts for
these clusters and don't provide any proactive support.

## Further reading

- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) from the official Kubernetes documentation
