---
linkTitle: Node pools
title: Node pools
description: A general description of node pools as a concept, its benefits, and some details you should be aware of.
weight: 45
menu:
  principal:
    identifier: tutorials-fleet-management-clusters-node-pools
    parent: tutorials-fleet-management-clusters
user_questions:
  - What is a node pool?
  - What are node pools?
  - In which cloud environments are node pools supported?
  - Which workload cluster releases introduced node pools?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2025-10-16
---

A node pool is a set of nodes within a Kubernetes cluster that share the same configuration (machine type, operating system, etc.). Each node in the pool is labeled by the node pool's name.

## Advantages

Prior to the introduction of node pools, a cluster could only comprise one type of worker node. The cluster would have to be scaled as a whole, and the availability zone distribution would apply to all worker nodes of a cluster. This would mean that every worker node would have to be big enough to run the largest possible workload, in terms of memory and CPU resources required. At the same time, all worker nodes in the cluster would have to use the same availability zone distribution, even if some workloads wouldn't require the increased availability.

Node pools are independent groups of worker nodes belonging to a cluster, where all nodes within a pool share a
common configuration. You can combine any type of node pool within one cluster. Node pools can differ regarding:

- Machine type
- Availability zone distribution
- Scaling configuration (number of nodes)
- Node labels (the pool name is added as node label by default)

## Configuration

Node pools can be created, deleted or updated by changing the configuration used [when creating the cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}})

{{< tabs >}}
{{< tab id="nodepool-capa-config" for-impl="capa_ec2" >}}

```sh
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

The node pool name will be a suffix of the cluster name. In the example above, the node pool name will be `mycluster-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the `giantswarm.io/machine-pool` label. You can identify the nodes' node pool using that label.

The example `kubectl` command below will list all nodes with role, node pool name, and node name.

```text
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.kubernetes\.io/role}{"\t"}{.metadata.labels.giantswarm\.io/machine-pool}{"\t"}{.metadata.name}{"\n"}{end}' | sort
master         ip-10-1-5-55.eu-central-1.compute.internal
worker  mycluster-pool0  ip-10-1-6-225.eu-central-1.compute.internal
worker  mycluster-pool0  ip-10-1-6-67.eu-central-1.compute.internal
```

{{< /tab >}}
{{< tab id="nodepool-capa-karpenter-config" for-impl="capa_ec2_karpenter" >}}

In your workload cluster values, you can specify the node pool configuration to use `karpenter`

```yaml
global:
  metadata:
    name: test-cluster
    organization: giantswarm
  nodePools:
    pool0:
      type: karpenter # This is the key difference that will make karpenter manage your worker nodes
      consolidateAfter: 6h
      consolidationPolicy: WhenEmptyOrUnderutilized
      consolidationBudgets: # You can control when and how nodes will be updated / rolled with the budgets
        - nodes: "20%"
        - schedule: "0 9 * * mon-fri"
          duration: "8h"
          nodes: "0"
          reasons:
            - "Drifted"
      customNodeLabels:
        - yourcustomlabel=canbeconfiguredhere
      customNodeTaints:
        - key: example.com/special-taint
          effect: NoSchedule
      expireAfter: 20h # The amount of time a Node can live on the cluster before being deleted by Karpenter
      requirements: # In the 'requirements' you can specify which nodes you want karpenter to consider or to ignore for your node pool
        - key: karpenter.k8s.aws/instance-cpu
          operator: In
          values:
            - "4"
            - "8"
            - "16"
            - "32"
        - key: karpenter.k8s.aws/instance-hypervisor
          operator: In
          values:
            - nitro
        - key: kubernetes.io/arch
          operator: In
          values:
            - amd64
        - key: karpenter.sh/capacity-type
          operator: In
          values:
            - spot
            - on-demand
        - key: kubernetes.io/os
          operator: In
          values:
            - linux
      terminationGracePeriod: 30m # The amount of time a Node can be draining before Karpenter forcibly cleans up the node
      limits: # Maximum amount of resources that the node pool can consume
        cpu: 1000
        memory: 1000Gi
  providerSpecific:
    region: "eu-west-1"
  release:
    version: 33.0.0
```

A node pool is identified by a name that you can pick as a cluster administrator. The name must follow these rules:

- must be between 5 and 20 characters long
- must start with a lowercase letter or number
- must end with a lowercase letter or number
- must contain only lowercase letters, numbers, and dashes

For example, `pool0`, `group-1` are valid node pool names.

The node pool name will be a suffix of the cluster name. In the example above, the node pool name will be `mycluster-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the `giantswarm.io/machine-pool` label. You can identify the nodes' node pool using that label.

When using `type: karpenter` in your node pool configuration, `karpenter` will be deployed in your cluster to manage your worker nodes.
The configuration values that you specify in the node pool configuration will be translated into the Custom Resources that `karpenter` is watching: [`NodePools` (`nodepools.karpenter.sh`)](https://karpenter.sh/docs/concepts/nodepools/) and [`EC2NodeClasses` (`ec2nodeclasses.karpenter.k8s.aws`)](https://karpenter.sh/docs/concepts/nodeclasses/).
There will be a pair of these Custom Resources for every node pool that you define in your cluster values.

Both `karpenter` Custom Resources [`NodePools`](https://karpenter.sh/docs/concepts/nodepools/) and [`EC2NodeClasses`](https://karpenter.sh/docs/concepts/nodeclasses/) offer many configuration options.
We expose most of those fields as values that you can set when defining your node pool in the cluster values.

Also, every EC2 instance that `karpenter` is managing is represented by a Custom Resource called [`NodeClaim` (`nodeclaims.karpenter.sh`)](https://karpenter.sh/docs/concepts/nodeclaims/).

In the `karpenter` node pools you can't specify the number of nodes in your cluster. Neither the minimum or maximum number of nodes that you want to have in your cluster.
Instead, you can specify [the maximum amount of resources](https://karpenter.sh/docs/concepts/nodepools/#speclimits) that the node pool can consume.

Depending on the workloads that are deployed, `karpenter` will try to optimize the number of nodes in your cluster. This process is called [consolidation](https://karpenter.sh/v0.32/concepts/disruption/#consolidation).
You can also configure your node pool to instruct `karpenter` about when and how to do the consolidation through [the `disruption` configurations](https://karpenter.sh/docs/concepts/disruption/).

{{< /tab >}}
{{< tab id="nodepool-capz-config" for-impl="capz_vms" >}}

```sh
kubectl gs template cluster --provider capz --name test-cluster \
  --organization giantswarm \
  --description "my test cluster" \
  --machine-pool-name pool0 \
  --machine-pool-min-size 3 \
  --machine-pool-max-size 5 \
  --machine-pool-instance-type Standard_D4s_v5
```

The node pool name will be a suffix of the cluster name. In the example above, the node pool name will be `mycluster-pool0`.

All nodes in the node pool will be labeled with the node pool name, using the `giantswarm.io/machine-deployment` label. You can identify the nodes' node pool using that label.

The example `kubectl` command below will list all nodes with role, node pool name, and node name.

```text
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
{{< tab id="nodepool-capa-scheduling" for-impl="capa_ec2" >}}

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
{{< tab id="nodepool-capa-karpenter-scheduling" for-impl="capa_ec2_karpenter" >}}

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
{{< tab id="nodepool-capz-scheduling" for-impl="capz_vms" >}}

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
[There is a set of labels](https://kubernetes.io/docs/reference/labels-annotations-taints/) that are automatically added by `Kubernetes` to all nodes, that you can use for scheduling.

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

You can add a new node pool like this:

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

**Warning:** Please be aware that changing the name of a node pool will result in the deletion of the old node pool and the creation of a new one.

If you still want to change the name of a node pool, our recommendation is to add a new node pool with the new name. Then waiting for it to be healthy, and finally removing the old one.

{{< tabs >}}
{{< tab id="nodepool-update-trigger-capa" for-impl="capa_ec2" >}}

Instances in the node pool will be rolled whenever these properties are changed in the node pool definition:

- `instanceType`
- `additionalSecurityGroups`
- `customNodeLabels`

Instances will also be rolled if these values are changed:

- `providerSpecific.ami`

{{< /tab >}}
{{< tab id="nodepool-update-trigger-capa-karpenter" for-impl="capa_ec2_karpenter" >}}

Instances in the node pool will be rolled whenever these properties are changed in the node pool definition:

- `additionalSecurityGroups`
- `customNodeLabels`
- `expireAfter`
- `terminationGracePeriod`

Instances will also be rolled if these values are changed:

- `providerSpecific.ami`

{{< /tab >}}
{{< tab id="nodepool-update-trigger-capz" for-impl="capz_vms" >}}

Instances in the node pool will be rolled whenever these properties are changed in the node pool definition:

- `instanceType`
- `additionalSecurityGroups`
- `customNodeLabels`

Instances will also be rolled if these values are changed:

- `providerSpecific.ami`

{{< /tab >}}
{{< /tabs >}}

### What happens when a node pool is updated {#what-happens-when-rolling-nodes}

{{< tabs >}}
{{< tab id="nodepool-update-general" title="General" >}}

On cluster update, nodes get replaced if their configuration changed (called "rolling nodes"). This means that pods running on the old nodes will be stopped and moved to new nodes automatically.

Nodes may also get replaced involuntarily, for example if the node becomes unhealthy (for example disk full, out of memory), the cloud provider has a hardware fault, or you are using AWS spot instances that can shut down at any time. Therefore, please make sure that your applications can handle pod restarts. This topic is too large to cover here. Our advise is to research "zero-downtime deployments" and "stateless applications" since with those best practices, typical applications survive pod restarts without any problems.

{{< /tab >}}
{{< tab id="nodepool-update-capa" for-impl="capa_ec2" >}}

During a cluster upgrade, creating new EC2 instances (called "rolling nodes") can be necessary. That only happens if anything changes in the node configuration, such as configuration files or newer version of Kubernetes or Flatcar Linux. For such planned node replacements, the default [instance warmup settings](https://github.com/search?q=repo%3Agiantswarm%2Fcluster-aws%20refreshPreferences&type=code) to ensure that AWS doesn't replace the old nodes too quickly all at once, but rather in steps so a human could still intervene if something goes wrong (for example roll back to previous version). One node will be replaced every 10 minutes for a small node pool. Instead, for bigger node pools, small sets of nodes would be replaced every 10 minutes.

When node pool instances need to be rolled, each instance receives a terminate signal from AWS. With `aws-node-termination-handler` preinstalled on the cluster, affected nodes are first gracefully drained before allowing AWS to finally continue terminating the EC2 instance. By default, the timeout for draining is [`global.nodePools.PATTERN.awsNodeTerminationHandler.heartbeatTimeoutSeconds=1800`](https://github.com/giantswarm/cluster-aws/blob/main/helm/cluster-aws/README.md#node-pools) (30 minutes). For nodes which could not be fully drained within that time, for example, because a pod did not terminate gracefully, the handler lets AWS continue the termination of the instance.

{{< /tab >}}
{{< tab id="nodepool-update-capa-karpenter" for-impl="capa_ec2_karpenter" >}}

During a cluster upgrade, creating new EC2 instances (called "rolling nodes") can be necessary. That only happens if anything changes in the node configuration, such as configuration files or newer version of Kubernetes or Flatcar Linux.
The [`disruption.budgets` configuration](https://karpenter.sh/docs/concepts/disruption/#nodepool-disruption-budgets) of your node pool control the speed in which `karpenter` can scale down nodes in your cluster.

When node pool instances need to be rolled, `karpenter` automatically taints, drains, and terminates the nodes.
By setting the `terminationGracePeriod` field on your node pool, you can configure the amount of time a `Node` can be draining before `karpenter` forcibly cleans up the node. Pods blocking eviction like `PodDisruptionBudgets` and do-not-disrupt will be respected during draining until the `terminationGracePeriod` is reached, where those pods will be forcibly deleted.

{{< /tab >}}
{{< /tabs >}}

## Node pool deletion

In a similar way, you can remove a node pool at any time by removing its configuration from the values and updating the cluster. When a node pool is deleted, all instances in the node pool will be terminated, and a similar process [as described above]({{< relref "#what-happens-when-rolling-nodes" >}}) will take place.

## Using mixed instance types (only {{% impl_title "capa_ec2" %}}) {#mixed-instance-types}

On {{% impl_title "capa_ec2" %}}, you can override the instance type of the node pool to enable [mixed instances policy on AWS](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateOverrides.html).

This can provide `Amazon EC2 Auto Scaling` with a larger selection of instance types to choose from when fulfilling node capacities.

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

Also, the order in which you define the instance types in `instanceTypeOverrides` is important.
The first instance type in the list that's available in the selected availability zone will be used.

**Note:** Changing the `instanceTypeOverrides` value won't trigger a rolling update of the node pool.

Using multiple instance types in a node pool has some benefits:

- Together with spot instances, using multiple instance types allows better price optimization. Popular instance types tend to have more price adjustments. Allowing older-generation instance types that are less popular tends to result in lower costs and fewer interruptions.

- Even without spot instances, AWS has a limited number of instances per type in each Availability Zone. It can happen that your selected instance type is temporarily out of stock just in the moment you are in demand of more worker nodes. Allowing the node pool to use multiple instance types reduces this risk and increases the likelihood that your node pool can grow when in need.

## Node pools and autoscaling {#autoscaling}

{{< tabs >}}
{{< tab id="nodepool-autoscaling-capa" title="General" >}}

With node pools, you set the autoscaling range per node pool. The `Kubernetes` cluster autoscaler has to decide which node pool to scale under which circumstances.

If you assign workloads to node pools as described [above](#assigning-workloads) and the autoscaler finds pods in `Pending` state, it will decide based on the node selectors which node pools to scale up.

In case there are workloads not assigned to any node pools, the autoscaler may pick any node pool for scaling. For details on the decision logic, please check the upstream FAQ for [AWS](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md).

{{< /tab >}}
{{< tab id="nodepool-autoscaling-capa-karpenter" for-impl="capa_ec2_karpenter" >}}

`karpenter` is watching the `Pods` in the cluster, and [it will scale up the node pool](https://karpenter.sh/docs/) based on the `Pods` that are in `Pending` state.

{{< /tab >}}
{{< tab id="nodepool-autoscaling-capz" for-impl="capz_vms" >}} >}}

Not supported at the moment.

{{< /tab >}}
{{< /tabs >}}

## On-demand and spot instances {#on-demand-spot}

{{< tabs >}}
{{< tab id="nodepool-capa-spot-instances" for-impl="capa_ec2" >}}

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
{{< tab id="nodepool-capa-karpenter-spot-instances" for-impl="capa_ec2_karpenter" >}}

Node pools may use [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/). On the node pool definition, you can enable it in the `requirements` field

```yaml
global:
  metadata:
    name: test-cluster
    organization: giantswarm
  nodePools:
    pool0:
      type: karpenter
      requirements:
        - key: karpenter.sh/capacity-type
          operator: In
          values:
            - spot
            - on-demand
  providerSpecific:
    region: "eu-west-1"
  release:
    version: 33.0.0
```

{{< /tab >}}
{{< tab id="nodepool-capz-spot-instances" for-impl="capz_vms" >}}

This is currently not supported.

{{< /tab >}}
{{< /tabs >}}

## Limitations

- Clusters without worker nodes (= without node pools) can't be considered fully functional. In order to have all required components scheduled, worker nodes are required. For that reason, it's deactivated any monitoring and alerts for these clusters and don't provide any proactive support.

Learn more about [how to assign `Pods` to `Nodes`](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) from the official documentation.
