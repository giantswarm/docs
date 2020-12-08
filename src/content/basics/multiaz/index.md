---
title: Clusters Over Multiple Availability Zones
description: Using multiple availability zones both for worker and for master nodes increases the resilience for clusters. Here we explain some details regarding support on different cloud providers and in different tenant cluster releases. And we give basic information on how to configure workloads to leverage multiple availability zones.
weight: 100
type: page
categories: ["basics"]
last_review_date: 2020-04-09
owner:
  - https://github.com/orgs/giantswarm/teams/team-celestial
---

# Clusters Over Multiple Availability Zones

With Giant Swarm on AWS and Azure you can easily launch clusters with worker nodes spread across multiple availability zones (AZs). This will lower the risk that your cluster will become unavailable due to an incident in a particular AWS or Azure data center.

On AWS, starting with tenant cluster release {{% first_aws_ha_masters_version %}}, master nodes of a cluster are spread over different availability zones by default, for high availability of the Kubernetes API. You can chose however to run only a single master node. Read [High availability Kubernetes masters](/basics/ha-masters/) for more information.

## What availability zones are good for {#benefits}

Both AWS and Azure support AZs within their regions. These zones still have good interconnectivity but are separated from each other to isolate failures within one zone from the others. As a result, it is more likely that one AZ goes down than the whole region. If your clusters are running within multiple AZs then Kubernetes can easily shift your workloads from one AZ to another.

Your cluster nodes have labels that indicate which availability zone they are running in. You can influence the scheduling of your pods via node affinity and/or inter-pod affinity or anti-affinity.

- [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)

This enables use cases such as:

- Running stateless services balanced over multiple AZs

- Grouping certain services that communicate with each other often and make sure they always run together within the same availability zone.

- Setup replication of your data across multiple AZs by keeping each instance of your StatefulSet in a different AZ.

## Details you should know about {#details}

- On both AWS and Azure availability zones are randomized across accounts. There is no way to determine which AZ you are really in, based on the name. E.g. the zone `eu-central-1a` in the account of the cluster is not necessarily the same `eu-central-1a` in your account.

- Availability zones get selected randomly by the Giant Swarm control plane. You only need to specify the required number of availability zones.

- Nodes will get distributed evenly across availability zones. There is currently no way to determine which or how many nodes should be started in a particular availability zone. But the nodes will have a label `topology.kubernetes.io/zone` (or in Kubernetes before 1.17: `failure-domain.beta.kubernetes.io/zone`) that indicates which availability zone the node is running in.

- Single availability zone clusters start in a random availability zone too. This is a means to minimize the risk of all your clusters becoming unavailable due to a failure in one particular AZ.

- Standard volumes can not be moved across availability zones. You need to take this into account when designing for high availability. If the AZ with your volume goes down, there will be no way to reschedule the pod to another availability zone. You either need to create a new volume from a snapshot or you will have to replicate your data across AZs. On AWS, you can also consider using [EFS](/guides/using-persistent-volumes-on-aws-with-efs/) as a storage provider to be able to access volumes from several availability zones.

- To make sure your pods and volumes end up on the same nodes, we recommend to specify `WaitForFirstConsumer` as `volumeBindingMode` in your storage classes. Your clusters come with a default storage class that contains this setting already. See the [Volume Binding Mode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode) section in the Kubernetes storage documentation for more information.

Spreading worker nodes over multiple availability zones can be configured per [node pool](/basics/nodepools/) and independent of the choice of a single master node vs. using multiple master nodes (currently multiple master nodes are only supported on AWS).

## Get started

You can create clusters in several ways:

- In the [web interface](/reference/web-interface/).
- In `gsctl` using the [`create cluster`](/reference/gsctl/create-cluster/) command with the appropriate details set in a [cluster definition](/reference/cluster-definition/).
- Via the [Giant Swarm API](/api/#operation/addCluster).

When inspecting details of such a cluster, or using the [`gsctl show cluster`](/reference/gsctl/show-cluster/) command, we display the list of availability zones used by the cluster.

Where worker nodes are organized in node pools, the availability zone distribution must be configured when creating a node pool. This is supported both in the web UI as well as the CLI with the [`gsctl create nodepool`](/reference/gsctl/create-nodepool/) command. For inspection, both the [`gsctl list nodepools`](/reference/gsctl/list-nodepools/) and [`gsctl show nodepool`](/reference/gsctl/show-nodepool/) commands provide AZ information.

Also exclusively on AWS, for master nodes, the choice to use high availability (three master nodes, placed in one AZ each) is made on cluster creation. It is also possible to switch from a single master node to high availability after cluster creation, but not vice versa.

## Further reading

- [The Giant Swarm AWS Architecture](/basics/aws-architecture/) explains in more detail the setup of Giant Swarm on AWS.
- [The Giant Swarm Azure Architecture](/basics/azure-architecture/) explains in more detail the setup of Giant Swarm on Azure.
