+++
title = "Clusters Over Multiple Availability Zones"
description = "By default, cluster get started within a single availability zone. But you can define how many availability zones a cluster should have to get higher a availability for your clusters."
date = "2020-03-18"
weight = 100
type = "page"
categories = ["basics"]
last-review-date = "2020-03-31"
+++

# Clusters Over Multiple Availability Zones

With Giant Swarm you can easily launch clusters across multiple availability zones (AZs). This will lower the risk that your cluster will become unavailable due to an incident in a particular AWS or Azure data center.

## What availability zones are good for {#benefits}

Both AWS and Azure support AZs within their regions. These zones still have good interconnectivity but are separated from each other to isolate failures within one zone from the others. As a result, it is more likely that one AZ goes down than the whole region. If your clusters are running within multiple AZs then Kubernetes can easily shift your workloads from one AZ to another.

Your cluster nodes have labels that indicate which availability zone they are running in. You can influence the scheduling of your pods via node affinity and/or inter-pod affinity or anti-affinity.

- [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)

This enables use cases such as:

- Running stateless services balanced over multiple AZs

- Grouping certain services that communicate with each other often and make sure they always run together within the same availability zone. 

- Setup replication of your data across multiple AZs by keeping each instance of your StatefulSet in a different AZ.

## Details you should know about {#details}

- On both AWS and Azure availability zones are randomized across accounts. There is no way to determine which AZ you are really in, based on the name. E.g. the zone `eu-central-1a` in the account of the cluster is not necessarily the same `eu-central-1a` in your account.

- Availability zones get selected randomly by the Giant Swarm control plane. You only need to specify the required number of availability zones. 

- Nodes will get distributed evenly across availability zones. There is currently no way to determine which or how many nodes should be started in a particular availability zone. But the nodes will have a label `failure-domain.beta.kubernetes.io/zone` that indicates which availability zone the node is running in.

- Single availability zone clusters start in a random availability zone too. This is a means to minimize the risk of all your clusters becoming unavailable due to a failure in one particular AZ.

- Volumes can not be moved across availability zones. You need to take this into account when designing for high availability. If the AZ with your volume goes down, there will be no way to reschedule the pod to another availability zone. You either need to create a new volume from a snapshot or you will have to replicate your data across AZs.

- To make sure your pods and volumes end up on the same nodes, we recommend to specify `WaitForFirstConsumer` as `volumeBindingMode` in your storage classes. Your clusters come with a default storage class that contains this setting already. See [Volume Binding Mode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode)

## Get started

You can create clusters in several ways:

- In `gsctl` using the [`create cluster --availability-zones`](/reference/gsctl/create-cluster/) command
- Via the [Giant Swarm API](/api/#operation/addCluster)
- In happa (multiple availability zones are not yet supported)

When inspecting details of such a cluster, or using the [`gsctl show cluster`](/reference/gsctl/show-cluster/) command, we display the list of availability zones used by the cluster.

## Further reading

- [The Giant Swarm AWS Architecture](/basics/aws-architecture/) explains in more detail the setup of Giant Swarm on AWS.
- [The Giant Swarm Azure Architecture](/basics/azure-architecture/) explains in more detail the setup of Giant Swarm on Azure.
