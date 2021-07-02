---
title: "Create your own App Catalog"
description: "Understand how the Giant Swarm App Platform works creating your own App Catalog"
date: "2020-08-18"
type: page
weight: 100
tags: ["tutorial", "app-platform"]
---

# Create your own App Catalog

## But Why?

Let's start reasoning why you should create your own App Catalog. The raise of Kubernetes has made the deployment and testability of tooling, databases, logging systems, ... became extremely easy. Both using direct API access via `kubectl` or a templating tool like `helm` or `kustomize`, developers can create resources easily without thinking too much on the configuration or the provision of the infrastructure that support these tools. This is a great fact and helps to speed up the prototyping or validation of our new setups. But at the same time brings the problematic that arises when the prototype or proof of concept becomes a real production implementation. 

The default configurations used in these tool packages are not targeted for production. Even some vendors provide [a good production defaults](https://bitnami.com/application-catalog), the reality is that each scenario or use case is totally different. A mongo production setup can completely depending on the amount of data has to be stored, the concurrent access model or the type of queries our application performs. 

The outcome is every Ops Team has developed an internal catalog or inventory to serve the different dev teams. In Giant Swarm we thought we could make our contribution to the field open sourcing the system that manage our deployments. Here we will go through the process of creating a catalog to illustrate from the very beginning how you can achieve it using our platform.

## Goals

Considering our customers run multiple clusters and they have several teams accessing to them, the App Platform team designed the system having in mind several tenets:

- Adopt existing artifact registries instead of enforcing customer to use a single flavour
- Flexibility to configure the applications through the different clusters and deployments
- Kubernetes native way to the define an application deployment via Custom Resource Definitions
- Use existing mature tools in the community to manage the Kubernetes resources
- Provide a way to keep the applications up to date easily
- Expose the system information in way that users can debug problems

## Create your catalog

GIant Swarm relies in a common patern to run multi-cluster setups. It provides a Control Plane Kubernetes cluster (indeed a meta cluster) where we run all our automation, same way our customer do for their own workloads, to provide an API to manage the (tenant) clusters.

Inside this Control Plane cluster we run our App Platform. It is composed by an [Kubernetes operator](https://github.com/giantswarm/app-operator) and some [custom resources](https://docs.giantswarm.io/reference/app-configuration/).


### How to store the App definitions

<Talk a bit of helm>

#### Helm as defacto way

#### Create a policy chart for testing

A catalog for Giant Swarm is just a HTTPS server that implement [Helm Repository Spec](https://helm.sh/docs/topics/chart_repository/#create-a-chart-repository) (though our idea could be able to support other alternatives). 

At the end it means any server that supports `tar` and `YAML` files downloading is enough for the task. A helm repository is just a list of packaged charts (in `tar` format) and an index `YAML` file. The index file list the different application charts and some metadata of those.

### Create your own package

### Create your own index file

### Use ChartMuseum as alternative 
APIs always help

### Show App Catalog Schema

### Install App Catalog Schema


- Create an example packing RBAC rules
- Create an example using a helm chart that is a stack of security (Or something else)




