+++
title = "The Giant Swarm On Premises Architecture"
description = "Architecture overview showing how Giant Swarm is set up within a customer data center on bare metal or virtual machines."
date = "2017-10-16"
type = "page"
weight = 10
+++

# The Giant Swarm On Premises Architecture

Giant Swarm's Architecture is split into two logical parts, one being the Host Cluster and the other being multiple Guest Clusters. We prefer running on bare metal machines, but can also work with virtualized infrastructure (e.g. VMWare) in case nested virtualization is possible.

We require VPN and SSH access to all machines, as well as outbound Internet connectivity from the machines (this can be limited to a few targets), to download images of various forms to automatically build and update the cluster. All machines are to be configured with one PXE Boot network and a production network (separate VLANs). The machines will be started by us via an ILO-Interface, to boot from the PXE Boot Server in the network for bootstrap, and then restart into the production network.

## Giant Swarm On Premises Host Cluster

![On Premises Host Cluster Architecture](/img/architecture-onprem-host-cluster.png)

Think of the Host Cluster as the Giant Swarm team’s Kubernetes Cluster. The worker nodes are where your Guest Clusters will end up on, controlled by our [kvm-operator](https://github.com/giantswarm/kvm-operator/) running inside the Host Cluster. The above diagram shows our PoC setup in that keeps the Host Cluster (including monitoring) on 3 machines. Based on amount and sizes of Guest Clusters, we recommend having distinct monitoring machines once we go into production. We further recommend having at least 5 worker machines. Any additional machines will also be set up as worker nodes and made available for Guest Clusters to be used by end users.

We access all machines, as well as the Kubernetes API of the Host Cluster, through VPN (and optionally via a Bastion host). We connect your load balancer for access to the Giant Swarm API, Happa, and our Monitoring, optionally adding your Identity Management System for authentication. Traffic towards all Guest Clusters is routed via the Host Cluster first, as it knows where exactly all the Guest Clusters are at any point in time.

## Giant Swarm On Premises Guest Cluster

![On Premises Guest Cluster Architecture](/img/architecture-onprem-guest-cluster.png)

Via the Giant Swarm API, our [CLI](https://github.com/giantswarm/gsctl), or our Web interface, you can start Guest Clusters of different sizes. You choose the amount of vCores and RAM you want per Node of your Guest Cluster and press “Create Cluster”. A few minutes later your cluster will be ready to use. It will be running on the Worker Nodes of the Host Cluster, within KVM VMs networked together through a Flannel network. Each Guest Cluster is separated from the other Guest Clusters by a flannel VXLAN bridge. Inside of that bridge, the containers are networked with Calico BGP.

Access to the K8s API goes through the Host Cluster. We can connected your Load Balancer for Ingress access. This Load Balancer can be either statically configured with healthchecks or controlled via API. Depending on the data center setup, there are different options that need to be evaluated.

## Service Architecture

![Service Architecture](/img/architecture-aws-services.png)

To make your life easier, we have developed a lot of different services within our Host Cluster that allow both our operations team and you as users of our API and interfaces to easily manage Kubernetes clusters. Most of these services should be self explanatory.

We have three main parts:

* Core Infrastructure Services
* Infrastructure Monitoring (used by Giant Swarm)
* Guest Clusters running your application workloads
