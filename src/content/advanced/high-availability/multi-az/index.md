---
linkTitle: Multiple AZ
title: Clusters over multiple availability zones
description: Using multiple availability zones both for worker and control plane nodes increases the resilience of the cluster. Here we explain some details regarding support on different cloud providers and releases, plus how to configure workloads to leverage multiple availability zones.
weight: 20
menu:
  main:
    parent: advanced-highavailability
last_review_date: 2023-04-04
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
aliases:
  - /basics/multiaz/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

{{< platform_support_table aws="ga" azure="ga" >}}

## Introduction

With Giant Swarm on AWS and Azure you can easily launch clusters with worker nodes spread across multiple availability zones (AZ). This will lower the risk that your cluster will become unavailable due to an incident in a particular AWS or Azure data center.

On AWS, starting with workload cluster release {{% first_aws_ha_controlplane_version %}}, control plane nodes of a cluster are spread over different availability zones by default, for high availability of the Kubernetes API. You can choose to run only a single control plane node. Read [High-availability Kubernetes control plane]({{< relref "/advanced/high-availability/control-plane" >}}) for more information.

## What availability zones are good for {#benefits}

Both AWS and Azure support AZ within their regions. These zones still have good interconnectivity but are separated from each other to isolate failures within one zone from the others. As a result, it is more likely that one AZ goes down than the whole region. If your clusters are running within multiple AZ then Kubernetes can easily shift your workloads from one AZ to another.

Your cluster nodes have labels that indicate which availability zone they are running in. You can influence the scheduling of your pods via node affinity and/or inter-pod affinity or anti-affinity.

- [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
- [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/)

This enables use cases such as:

- Running stateless services balanced over multiple AZ

- Grouping certain services that communicate with each other often and make sure they always run together within the same availability zone.

- Setup replication of your data across multiple AZ by keeping each instance of your StatefulSet in a different AZ.

## Details you should know about {#details}

- On both AWS and Azure availability zones are randomized across accounts. There is no way to determine which AZ you are really in, based on the name. E.g. the zone `eu-central-1a` in the account of the cluster is not necessarily the same `eu-central-1a` in your account.

- Availability zones get selected randomly by the Giant Swarm management cluster. You only need to specify the required number of availability zones.

- Nodes will get distributed evenly across availability zones. There is currently no way to determine which or how many nodes should be started in a particular availability zone. But the nodes will have a label `topology.kubernetes.io/zone` (or in Kubernetes before 1.17: `failure-domain.beta.kubernetes.io/zone`) that indicates which availability zone the node is running in.

- Single availability zone clusters start in a random availability zone too. This is a means to minimize the risk of all your clusters becoming unavailable due to a failure in one particular AZ.

- Standard volumes can not be moved across availability zones. You need to take this into account when designing for high availability. If the AZ with your volume goes down, there will be no way to reschedule the pod to another availability zone. You either need to create a new volume from a snapshot or you will have to replicate your data across AZ. On AWS, you can also consider using [EFS]({{< relref "/advanced/storage/efs" >}}) as a storage provider to be able to access volumes from several availability zones.

- To make sure your pods and volumes end up on the same nodes, we recommend to specify `WaitForFirstConsumer` as `volumeBindingMode` in your storage classes. Your clusters come with a default storage class that contains this setting already. See the [Volume Binding Mode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode) section in the Kubernetes storage documentation for more information.

Spreading worker nodes over multiple availability zones can be configured per [node pool]({{< relref "/advanced/node-pools" >}}) and independent of the choice of a single control plane node vs. using multiple control plane nodes (currently multiple control plane nodes are only supported on AWS).

## Example Pod Topology Spread Constraints and Affinity

To make sure your workload gets scheduled over available worker nodes over availability zones you can make use of [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/) and [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity).

In this example, the two constraints make sure, pods with the given labels are distributed across available zones. The first constraint makes sure the number of Pods across Nodes with the same `topology.kubernetes.io/zone` label is one at max. The second constraint picks the Node with the lowest number of Pods still across all nodes and all zones. This might collide with the first constraint and no schedule would happen at all unless `whenUnsatisfiable` is set to `ScheduleAnyway`. The `affinity` makes sure to not schedule any Pods on `master` Nodes.

The following fields are part of the `spec.template.spec` of Deployments, StatefulSets, and DaemonSets:

```
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

These constraints are checked during scheduling of new Pods. In case some dis-balancing happened because of other reasons, [Descheduler for Kubernetes](https://github.com/kubernetes-sigs/descheduler) can be used to re-schedule Pods to be more balanced.
Please be aware of some undesirable edge-cases and caveats. These might show up on more complex `topologySpreadConstraints` and `affinity` setups. Discussions in issues [kubernetes/kubernetes#106127](https://github.com/kubernetes/kubernetes/issues/106127), [kubernetes/kubernetes#105977](https://github.com/kubernetes/kubernetes/issues/105977) and [kubernetes/kubernetes#105291](https://github.com/kubernetes/kubernetes/issues/105291) touch some of the problems that could arise.
## Get started

You can create clusters in several ways:

- In the [web interface]({{< relref "/platform-overview/web-interface/" >}}).
- In `gsctl` using the [`create cluster`]({{< relref "/use-the-api/gsctl/create-cluster" >}}) command with the appropriate details set in a [cluster definition]({{< relref "/use-the-api/gsctl/cluster-definition" >}}).
- Via the [Giant Swarm REST API](/api/#operation/addCluster).

When inspecting details of such a cluster, or using the [`gsctl show cluster`]({{< relref "/use-the-api/gsctl/show-cluster" >}}) command, we display the list of availability zones used by the cluster.

Where worker nodes are organized in node pools, the availability zone distribution must be configured when creating a node pool. This is supported both in the web UI as well as the CLI with the [`gsctl create nodepool`]({{< relref "/use-the-api/gsctl/create-nodepool" >}}) or [`kubectl gs template nodepool`]({{< relref "/use-the-api/kubectl-gs/template-nodepool" >}}) command. For inspection, both the [`gsctl list nodepools`]({{< relref "/use-the-api/gsctl/list-nodepools" >}}) and [`kubectl gs get nodepools`]({{< relref "/use-the-api/kubectl-gs/get-nodepools" >}}) commands provide AZ information.

Also exclusively on AWS, for control plane nodes, the choice to use high-availability (three control plane nodes, placed in one AZ each) is made on cluster creation. It is also possible to switch from a single control plane node to high availability after cluster creation, but not vice versa.

## Further reading

- [The Giant Swarm AWS Architecture]({{< relref "/platform-overview/cluster-management/vintage/aws" >}}) explains in more detail the setup of Giant Swarm on AWS.
- [The Giant Swarm Azure Architecture]({{< relref "/platform-overview/cluster-management/vintage/azure" >}}) explains in more detail the setup of Giant Swarm on Azure.
