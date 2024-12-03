---
linkTitle: Multiple AZ
title: Clusters over multiple availability zones
description: Using multiple availability zones both for worker and control plane nodes increases the resilience of the cluster. Here you will see some details regarding support on different cloud providers and releases, plus how to configure workloads to leverage multiple availability zones.
weight: 20
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-clusters-multi-az
last_review_date: 2024-11-29
user_questions:
- Does Giant Swarm support multiple availability zones (AZ)?
- What are the benefits of using multiple availability zones (AZ)?
- How do I know which availability zone (AZ) my cluster nodes are running in?
- Can I influence the scheduling of my pods?
- How are availability zones (AZ) selected?
- Can I move standard volumes across availability zones (AZ)?
- What is the alternative to moving volumes across availability zones (AZ)?
- How do I ensure my pods and volumes are on the same nodes?
- Can I spread worker nodes over availability zones?
- How do I create clusters in multiple availability zones (AZ)?
- How do I make sure my workload is distributed evenly over availability zones (AZ)?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

In Giant Swarm platform you can easily launch clusters with worker nodes spread across multiple availability zones (`AZ`). This will lower the risk that your cluster will become unavailable due to an incident in a particular `AWS`, `Azure` or on-premise data center.

## What availability zones are good for {#benefits}

Cloud providers, and on-premise installations, supports availability zones within their regions. These zones still have good inter-connectivity but are separated from each other to isolate failures within one zone from the others. As a result, it's more likely that one zone goes down than the whole region. If your clusters are running within multiple availability zones then `Kubernetes` can easily shift your workloads from one zone to another.

Your cluster nodes have labels that indicate which availability zone they're running in. You can influence the scheduling of your pods via node affinity and/or inter-pod affinity or anti-affinity.

- [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
- [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/)

This enables use cases such as:

- Running stateless services balanced over multiple availability zones to increase availability.

- Grouping certain services that communicate with each other often and make sure they always run together within the same availability zone.

- Setup replication of your data across multiple availability zones by keeping each instance of your StatefulSet in a different zone.

## Details you should know about {#details}

- On AWS and Azure availability zones are randomized across accounts. There is no way to determine which zone you are really in, based on the name. For example, the zone `eu-central-1a` in the account of the cluster isn't necessarily the same `eu-central-1a` in your account.

- Availability zones get selected randomly by the Giant Swarm management cluster. You only need to specify the required number of availability zones.

- Nodes will get distributed evenly across availability zones. There is currently no way to determine which or how many nodes should be started in a particular availability zone. But the nodes will have a label `topology.kubernetes.io/zone` (or in Kubernetes before 1.17: `failure-domain.beta.kubernetes.io/zone`) that indicates which availability zone the node is running in.

- Single availability zone clusters start in a random availability zone too. This is a means to minimize the risk of all your clusters becoming unavailable due to a failure in one particular zone.

- Standard volumes can not be moved across availability zones. You need to take this into account when designing for high availability. If the zone with your volume goes down, there will be no way to reschedule the pod to another availability zone. You either need to create a new volume from a snapshot or you will have to replicate your data across zones. On AWS, you can also consider using [EFS]({{< relref "/vintage/advanced/storage/efs" >}}) as a storage provider to be able to access volumes from several availability zones.

- To make sure your pods and volumes end up on the same nodes, our recommendation is to specify `WaitForFirstConsumer` as `volumeBindingMode` in your storage classes. Your clusters come with a default storage class that contains this setting already. See the [Volume Binding Mode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode) section in the Kubernetes storage documentation for more information.

Spreading worker nodes over multiple availability zones can be configured per [node pool]({{< relref "/vintage/advanced/cluster-management/node-pools-vintage" >}}) and independent of the choice of a single control plane node vs. using multiple control plane nodes (currently multiple control plane nodes are only supported on AWS).

## Example pod topology spread constraints and affinity

To make sure your workload gets scheduled over available worker nodes over availability zones you can make use of [`Pod Topology Spread Constraints`](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/) and [affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity).

In this example, the two constraints make sure, pods with the given labels are distributed across available zones. The first constraint makes sure the number of pods across nodes with the same `topology.kubernetes.io/zone` label is one at max. The second constraint picks the Node with the lowest number of Pods still across all nodes and all zones. This might collide with the first constraint and no schedule would happen at all unless `whenUnsatisfiable` is set to `ScheduleAnyway`. The `affinity` makes sure to not schedule any Pods on `master` Nodes.

The following fields are part of the `spec.template.spec` of `Deployments`, `StatefulSets`, and `DaemonSets`:

```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app.kubernetes.io/name: hello-world-app
        app.kubernetes.io/version: 0.1.0
  - maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: ScheduleAnyway
    labelSelector:
      matchLabels:
        app.kubernetes.io/name: hello-world-app
        app.kubernetes.io/version: 0.1.0
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/role
          operator: NotIn
          values:
          - master
```

These constraints are checked during scheduling of new pods. In case some dis-balancing happened because of other reasons, [`Descheduler` for `Kubernetes`](https://github.com/kubernetes-sigs/descheduler) can be used to re-schedule pods to be more balanced.

Please be aware of some undesirable edge-cases and caveats. These might show up on more complex `topologySpreadConstraints` and `affinity` setups. Discussions in issues [kubernetes/kubernetes#106127](https://github.com/kubernetes/kubernetes/issues/106127), [kubernetes/kubernetes#105977](https://github.com/kubernetes/kubernetes/issues/105977) and [kubernetes/kubernetes#105291](https://github.com/kubernetes/kubernetes/issues/105291) touch some of the problems that could arise.

## Get started

You can read [`kubectl gs template cluster`]({{< relref "/reference/kubectl-gs/template-cluster" >}}) to learn how to create a cluster with multiple availability zones.

When inspecting details of such a cluster, you can get the node pool information using the node pool infrastructure resource depending on the provider.

{{< tabs >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2">}}

The node pools in Cluster API for AWS are managed by the `AWSMachinePool` resource. When you create a cluster with `kubectl gs template cluster` you can define the availability zones for the worker nodes as shown below.

```text
$ kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing --user-configmap=/tmp/values.yaml
```

Get the node pool information by querying the `AWSMachinePool` resource as shown below.

```text
$ kubectl get AWSManagedMachinePool -l cluster.x-k8s.io/cluster-name=mycluster -oyaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSManagedMachinePool
metadata:
  name: mycluster-np001
  namespace: org-testing
spec:
  availabilityZones:
  - eu-west-1a
  ...
```

{{< /tab >}}
{{< tab id="cluster-capa-eks" for-impl="capa_eks">}}

The node pools in EKS are managed by the `AWSManagedMachinePool` resource. When you create a cluster with `kubectl gs template cluster` you can define the availability zones for the worker nodes as shown below.

```text
$ kubectl gs template cluster \
  --provider eks \
  --name mycluster \
  --organization testing --user-configmap=/tmp/values.yaml
```

Get the node pool information by querying the `AWSManagedMachinePool` resource as shown below.

```text
$ kubectl get AWSManagedMachinePool -l cluster.x-k8s.io/cluster-name=mycluster -oyaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSManagedMachinePool
metadata:
  name: mycluster-np001
  namespace: org-testing
spec:
  availabilityZones:
  - eu-west-1a
  ...
```

{{< /tab >}}
{{< tab id="cluster-capz-azure-vms" for-impl="capz_vms">}}

The node pools in Cluster API for Azure are managed by the `MachineDeployment` resource. When you create a cluster with `kubectl gs template cluster` you can define the availability zones for the worker nodes as shown below.

```text
$ kubectl gs template cluster \
  --provider capz \
  --name mycluster \
  --organization testing --user-configmap=/tmp/values.yaml
```

Get the node pool information by querying the `MachineDeployment` resource as shown below.

```text
$ kubectl get MachineDeployment -l cluster.x-k8s.io/cluster-name=mycluster -oyaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineDeployment
metadata:
  name: mycluster-np001
  namespace: org-testing
spec:
  failureDomain: 2
  ...
```

{{< /tabs >}}

Learn more about [node pools]({{< relref "/tutorials/fleet-management/cluster-management/node-pools" >}}) and how to manage them.
