+++
title = "The Giant Swarm AWS Architecture"
description = "Architecture Overview showing how Giant Swarm is set up on Amazon Web Services"
date = "2020-01-08"
weight = 50
type = "page"
categories = ["basics"]
last-review-date = "2020-03-17"
+++

# The Giant Swarm AWS Architecture

Giant Swarm's Architecture is split into two logical parts, one being the Control Plane and the other being multiple Tenant Clusters. Among other services (for details see Service Architecture below), the control plane runs our [AWS Operator](https://github.com/giantswarm/aws-operator), which handles the full lifecycle management of Tenant Clusters.

## Giant Swarm control plane

![Control Plane Architecture](architecture-aws-control-plane.png)

The above diagram shows our control plane setup running over three availability zones. We setup two bastion hosts in different availability zones. All instances are in a private subnet and only accessible through the bastion hosts. Bastion hosts are available via AWS VPN connection only.

The cluster has several APIs and Interfaces. The Kubernetes API of the Control Plane is only available to Giant Swarm operations personnel and only through the Bastion hosts.

The Giant Swarm API, Monitoring and Alerting frontends as well as our Web User Interface, are exposed through the Control Plane Ingress Controller, which sits behind a public ELB.

Access to those interfaces can be configured to work with the customers' Identity Management System.

## Giant Swarm tenant cluster

![Tenant Cluster Architecture](architecture-aws-tenant-cluster.png)

Via the Giant Swarm API, our [CLI](https://github.com/giantswarm/gsctl), or our Web User Interface, you can start Tenant Clusters of different sizes. There's a selection of recommended EC2 instance types, which can be adjusted if needed.

Each cluster resides in its own VPC. All EC2 machines are in their own private subnet. There are two possible access routes into the cluster.

One is the Kubernetes API that can be connected to your Identity Management System using OIDC. The other is the Ingress Controller (exposed through a public ELB), with which you can expose services running inside your cluster publicly. The services will be mapped to domains handled through Route53. For the final URL, you can point a CNAME to the Ingress URL.

Networking within the cluster is handled through Calico.

## Service architecture

![Service Architecture](architecture-aws-services.png)

To make your life easier, we have developed a lot of different services within our Control Plane that allow both our operations team and you as users of our API and interfaces to easily manage Kubernetes clusters. Most of these services should be self explanatory.

We have three main parts:

* Core Infrastructure Services
* Infrastructure Monitoring (used by Giant Swarm)
* Tenant Clusters
