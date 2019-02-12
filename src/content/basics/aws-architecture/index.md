+++
title = "The Giant Swarm AWS Architecture"
description = "Architecture Overview showing how Giant Swarm is set up on Amazon Web Services"
date = "2018-08-16"
weight = 20
type = "page"
categories = ["basics"]
+++

# The Giant Swarm AWS Architecture

Giant Swarm's Architecture is split into two logical parts, one being the Control Plane and the other being multiple Tenant Clusters. Among other services (for details see Service Architecture below), the control plane runs our [AWS Operator](https://github.com/giantswarm/aws-operator), which handles the full lifecycle management of Tenant Clusters.

## Giant Swarm control plane

![Control Plane Architecture](/img/architecture-aws-control-plane.png)

The above diagram shows our PoC setup and runs over two availability zones. We setup two Bastion hosts, one in each Availability Zone. All EC2 machines are in a private subnet and only accessible through the Bastion hosts.

The cluster has several APIs and Interfaces. The Kubernetes API of the Control Plane is only available to Giant Swarm operations personel and only through the Bastion hosts. 

The Giant Swarm API, Monitoring and Alerting frontends as well as our Web Management Interface, Happa, are exposed through the Control Plane Ingress Controller, which sits behind a public ELB.

Access to those interfaces can be configured to work with the customers' Identity Management System.

## Giant Swarm tenant cluster

![Tenant Cluster Architecture](/img/architecture-aws-tenant-cluster.png)

Via the Giant Swarm API, our [CLI](https://github.com/giantswarm/gsctl), or our Happa interface, you can start Tenant Clusters of different sizes. There's a selection of recommended EC2 instance types, which can be adjusted if needed. 

Each cluster resides in its own VPC. All EC2 machines are in their own private subnet. There are two possible access routes into the cluster. 

One is the Kubernetes API that can be connected to your Identity Management System using OIDC. The other is the Ingress Controller (exposed through a public ELB), with which you can expose services running inside your cluster publicly. The services will be mapped to domains handled through Route53. For the final URL, you can point a CNAME to the Ingress URL. 

Networking within the cluster is handled through Calico. 

## Service architecture

![Service Architecture](/img/architecture-aws-services.png)

To make your life easier, we have developed a lot of different services within our Control Plane that allow both our operations team and you as users of our API and interfaces to easily manage Kubernetes clusters. Most of these services should be self explanatory. 

We have three main parts:

* Core Infrastructure Services
* Infrastructure Monitoring (used by Giant Swarm)
* Tenant Clusters
