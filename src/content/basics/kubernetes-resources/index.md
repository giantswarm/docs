---
title: Kubernetes Resources
description: Pointers to the best resources about Kubernetes to get you up to speed with Kubernetes fast
date: 2020-02-03
weight: 140
type: page
categories: ["basics"]
last-review-date: 2020-03-31
---

# Kubernetes Resources

As your Giant Swarm cluster offers you fully-managed Kubernetes, the fundamentals you need are basically summarized by the userside documentation of Kubernetes. We have compiled a list of the best resources to get you started fast.

## Official kubernetes documentation

The first and most important source to read is the [official Kubernetes documentation](http://kubernetes.io/docs/). Since the administrative side is mostly taken care of by Giant Swarm, we recommend focussing on the [task-specific tutorials](https://kubernetes.io/docs/tutorials/).

## Useful primitives

### Pods 

Pods are the smallest deployable units of computing that can be created and managed in Kubernetes. They contain one or more containers that run inside the pod as if they were running on a single host.

[Pods Reference](https://kubernetes.io/docs/concepts/workloads/pods/pod/)

### Labels and selectors

Labels are key/value pairs that can be attached to objects, such as pods, but also any other object in Kubernetes, even nodes. They should be used to specify identifying attributes of objects that are meaningful and relevant to users. You can then use Selectors to select single or groups of objects.

[Labels & Selectors Reference](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

### Deployments

Deployments are a declarative way of defining the deployment of pods onto the cluster. They manage replication as well as updates of these pods and keep an audit log of all changes.

[Deployments Reference](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

### Services

Services work by defining a logical set of pods and a policy by which to access them. The selection of pods is based on label selectors. In case you select multiple pods, the service automatically takes care of load balancing and assigns them a single internal service IP.

[Services Reference](https://kubernetes.io/docs/concepts/services-networking/service/)

### Ingress

An Ingress is a collection of rules that allow inbound connections from outside the cluster to reach the cluster services. It can be configured to give services externally-reachable URLs, load balance traffic, terminate SSL, offer name based virtual hosting etc. 

[Ingress Reference](https://kubernetes.io/docs/concepts/services-networking/ingress/)

### Secrets & ConfigMaps

There are two primitives for keeping configuration out of your containers. The first is Secrets, which as the name suggest is for storing sensitive information. The second one is ConfigMaps, which you can use for storing general configuration. The two are quite similar in usage and support a variety of use cases.

[Secrets Reference](https://kubernetes.io/docs/concepts/configuration/secret/)

[ConfigMaps Reference](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)

### Jobs

Unlike the typical pod that you use for long-running processes, jobs let you manage pods that are supposed to terminate and not be restarted. A job creates one or more pods and ensures their termination after a specified number of successful completions.

[Jobs Reference](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/)

### Daemon Sets

A daemon set ensures that an instance of a specific pod is running on all (or a selection of) nodes in a cluster. It creates pods on each added node and garbage collects pods when nodes are removed from the cluster.

[Daemon Sets Reference](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

### Namespaces

With namespaces you can split up your cluster into smaller separate environments. These environments are separate in terms of Kubernetes objects that they contain. They do not completely isolate from the rest of the cluster by default.

[Namespaces Reference](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

### DNS

Giant Swarm clusters come with CoreDNS installed by default. You can use DNS to discover services and communicate between them.

[CoreDNS documentation](https://coredns.io/manual/toc/)

## Useful tools and content

There are some useful tools and content out there that help you with get to know Kubernetes.

- The [Kubernetes Blog](https://kubernetes.io/blog/) is a good resource for reading up on new features, examples, and user stories around Kubernetes.
- [Kompose](https://github.com/kubernetes-incubator/kompose) is a tool to move from `docker-compose` to Kubernetes.
- [Helm](https://github.com/kubernetes/helm/blob/master/docs/install.md) is a package manager for Kubernetes that helps you deploy common applications to your cluster.

## Useful blog posts

We have also written some more detailed out blog posts about the basic Kubernetes concepts and use cases for them.

- [Understanding Basic Kubernetes Concepts I - An Introduction To Pods, Labels, and Replicas](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-i-introduction-to-pods-labels-replicas/)
- [Understanding Basic Kubernetes Concepts II - Using Deployments To Manage Your Services Declaratively](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-using-deployments-manage-services-declaratively/)
- [Understanding Basic Kubernetes Concepts III - Services Give You Abstraction](https://blog.giantswarm.io/basic-kubernetes-concepts-iii-services-give-abstraction/)
- [Understanding Basic Kubernetes Concepts IV - Secrets and ConfigMaps](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-iv-secrets-and-configmaps/)
- [Understanding Basic Kubernetes Concepts V - Daemon Sets and Jobs](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-v-daemon-sets-and-jobs/)
- [Getting Started With A Local Kubernetes Environment](https://blog.giantswarm.io/getting-started-with-a-local-kubernetes-environment/)

## Extended reading

For more extensive and deeper information on Kubernetes you should check out the [Reference Documentation](https://kubernetes.io/docs/reference/), which includes among others the [API documentation](https://kubernetes.io/docs/concepts/overview/kubernetes-api/), [CLI documentation](https://kubernetes.io/docs/reference/kubectl/overview/), and a Glossary with deeper explanations of all resources.
