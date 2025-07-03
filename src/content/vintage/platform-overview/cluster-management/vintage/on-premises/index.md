---
linkTitle: On-premises
title: The Giant Swarm on-premises architecture
description: Architecture overview showing how Giant Swarm is set up within a customer data center on bare metal or virtual machines, using KVM as a virtualization layer.
weight: 30
menu:
  main:
    parent: cluster-management-vintage
last_review_date: 2024-02-19
user_questions:
  - Do you run on bare metal?
  - Can you run on virtual machines (e.g. VMWare)?
  - What is required to enable access to the machines?
  - What does the on-prem architecture look like?
  - What are the best practices for setting up an on-prem installation?
  - How does Giant Swarm access an on-prem installation?
  - How can I setup a workload cluser?
  - What makes up the service architecture?
aliases:
  - /on-premises
  - /basics/onprem-architecture/
  - /general/architcture/on-premises/
  - /general/architecture/on-premises/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

Giant Swarm's architecture is split into two logical parts. One describes the management cluster and the other describes one or more workload clusters. We prefer running on bare metal machines, but can also work with virtualized infrastructure (e.g. VMWare) in cases where nested virtualization is possible.

We require VPN and SSH access to all machines, as well as outbound Internet connectivity from the machines (this can be limited to specific targets), to download images of various forms to automatically provision and update the cluster. All machines are to be configured with one PXE Boot network and a production network (separate VLANs). The machines will be started by us via an ILO-Interface, to boot from the PXE Boot Server in the network for bootstrap, and then restarted into the production network.

## Giant Swarm on-premises management cluster

![On-premises Control Plane architecture](architecture-onprem-control-plane.png)

Think of the management cluster as the Giant Swarm team’s Kubernetes cluster. The worker nodes of this cluster are where your workload clusters will be run. Workload cluster nodes are deployed as separate virtual machine instances and controlled by our [kvm-operator](https://github.com/giantswarm/kvm-operator/) running inside the management cluster. The diagram above shows the conceptual setup. Depending on the node's available resources, in most environments, the management cluster components (including monitoring) fit on 3 or fewer machines. Based on the number and sizes of workload clusters, our management cluster adapts accordingly and will deploy or remove monitoring or management components as needed. As a matter of best practice, we recommend having at least 5 worker machines to host your workload clusters. Any additional machines will also be set up as worker nodes and made available for workload clusters to be used by end users.

We access all machines, as well as the Kubernetes API of the management cluster, through VPN (and optionally via a bastion host). Your load balancer is configured to allow access to the Giant Swarm web user interface, and our monitoring components, optionally adding your Identity Management System for authentication. Traffic towards all workload clusters is routed via the management cluster first, as it knows exactly where all the workload clusters are at any point in time.

## Giant Swarm on-premises workload cluster

![On-premises workload cluster architecture](architecture-onprem-tenant-cluster.png)

Using the Giant Swarm Web UI, you can start workload clusters of different sizes. You choose the amount of vCores and RAM you want per Node of your workload cluster and click “Create Cluster”. Moments later your cluster will be ready to use. It will be running on the worker nodes of the management cluster, within KVM VMs networked together through a Flannel network. Each workload cluster is separated from the other workload clusters by a Flannel VXLAN bridge. Inside of that bridge, containers are networked with Calico BGP.

Access to the Kubernetes API goes through the management cluster. We can connect your load balancer for Ingress access. This load balancer can be either statically configured with health checks or controlled via an API. Depending on the data center setup, there may be multiple options which our engineers will evaluate with your infrastructure team.

## Service architecture

![Service Architecture](architecture-onprem-services.png)

To make your life easier, we have developed numerous automated services within our management cluster that allow both our operations team and you as a user to easily manage your Kubernetes clusters. Most of these services should be self explanatory.

We have three main parts:

* Core infrastructure services
* Infrastructure monitoring (used by Giant Swarm)
* Workload clusters running your application workloads

All of these are geared towards enabling you to run multiple projects independently and consistently in your data centers.
