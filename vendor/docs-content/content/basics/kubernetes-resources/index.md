+++
title = "Kubernetes Resources"
description = "Pointers to the best resources about Kubernetes to get you up to speed with Kubernetes fast"
date = "2017-01-02"
type = "page"
weight = 20
categories = ["basics"]
+++

# Kubernetes Resources

As your Giant Swarm cluster offers you a fully-managed Kubernetes, the fundamentals you need are basically concluded by the userside documentation of Kubernetes. We have compiled a list of the best resources to get you started fast.

## Official Kubernetes Documentation

The first and most important source to enquire should be the [official Kubernetes documentation](http://kubernetes.io/docs/). And as the administration side is mostly taken care of by Giant Swarm, we recommend focussing on the [User Guide](http://kubernetes.io/docs/user-guide/) including the [Kubernetes 101](http://kubernetes.io/docs/user-guide/walkthrough/) and [201](http://kubernetes.io/docs/user-guide/walkthrough/k8s201/).

## Useful Primitives

### Pods 

Pods are the smallest deployable units of computing that can be created and managed in Kubernetes. They contain one or more containers that run inside the pod as if they were running on a single host.

[Pods Reference](http://kubernetes.io/docs/user-guide/pods/)

### Labels & Selectors

Labels are key/value pairs that can be attached to objects, such as pods, but also any other object in Kubernetes, even nodes. They should be used to specify identifying attributes of objects that are meaningful and relevant to users. You can then use Selectors to select single or groups of objects.

[Labels & Selectors Reference](http://kubernetes.io/docs/user-guide/labels/)

### Deployments

Deployments are a declarative way of defining the deployment of pods onto the cluster. They manage replication as well as updates of these pods and keep an audit log of all changes.

[Deployments Reference](http://kubernetes.io/docs/user-guide/deployments/)

### Services

Services work by defining a logical set of pods and a policy by which to access them. The selection of pods is based on label selectors. In case you select multiple pods, the service automatically takes care of load balancing and assigns them a single internal service IP.

[Services Reference](http://kubernetes.io/docs/user-guide/services/)

### Ingress

An Ingress is a collection of rules that allow inbound connections from outside the cluster to reach the cluster services. It can be configured to give services externally-reachable URLs, load balance traffic, terminate SSL, offer name based virtual hosting etc. 

[Ingress Reference](http://kubernetes.io/docs/user-guide/ingress/)

### Secrets & ConfigMaps

There are two primitives for keeping configuration out of your containers. The first is Secrets, which as the name suggest is for storing sensitive information. The second one is ConfigMaps, which you can use for storing general configuration. The two are quite similar in usage and support a variety of use cases.

[Secrets Reference](http://kubernetes.io/docs/user-guide/secrets/)

[ConfigMaps Reference](http://kubernetes.io/docs/user-guide/configmap/)

### Jobs

Unlike the typical pod that you use for long-running processes, jobs let you manage pods that are supposed to terminate and not be restarted. A job creates one or more pods and ensures a specified number of them terminate with success.

[Jobs Reference](http://kubernetes.io/docs/user-guide/jobs/)

### Daemon Sets

A daemon set ensures that an instance of a specific pod is running on all (or a selection of) nodes in a cluster. It creates pods on each added node and garbage collects pods when nodes are removed from the cluster.

[Daemon Sets Reference](http://kubernetes.io/docs/admin/daemons/)

### Namespaces

With namespaces you can split up your cluster into smaller separate environments. These environments are separate in terms of Kubernetes objects that they contain, but by default do not completely isolate from the rest of the cluster.

[Namespaces Reference](http://kubernetes.io/docs/user-guide/namespaces/)

### DNS

Giant Swarm clusters come with KubeDNS installed by default. You can use DNS to discover services and communicate between them.

[DNS Documentation](http://releases.k8s.io/master/build/kube-dns/README.md)

## Useful Tools and Content

There are some useful tools and content out there that help you with get to know Kubernetes.

- The [Kubernetes Blog](http://blog.kubernetes.io/) is a good resource for reading up on new features, examples, and user stories around Kubernetes.
- [Kompose](https://github.com/kubernetes-incubator/kompose) is a tool to move from `docker-compose` to Kubernetes.
- [Helm](https://github.com/kubernetes/helm/blob/master/docs/install.md) is a package manager for Kubernetes that helps you deploy common applications to your cluster.

## Useful Blog Posts

We have also written some more detailed out blog posts about the basic Kubernetes concepts and use cases for them.

- [Understanding Basic Kubernetes Concepts I - An Introduction To Pods, Labels, and Replicas](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-i-introduction-to-pods-labels-replicas/)
- [Understanding Basic Kubernetes Concepts II - Using Deployments To Manage Your Services Declaratively](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-using-deployments-manage-services-declaratively/)
- [Understanding Basic Kubernetes Concepts III - Services Give You Abstraction](https://blog.giantswarm.io/basic-kubernetes-concepts-iii-services-give-abstraction/)
- [Understanding Basic Kubernetes Concepts IV - Secrets and ConfigMaps](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-iv-secrets-and-configmaps/)
- [Understanding Basic Kubernetes Concepts V - Daemon Sets and Jobs](https://blog.giantswarm.io/understanding-basic-kubernetes-concepts-v-daemon-sets-and-jobs/)
- [Getting Started With A Local Kubernetes Environment](https://blog.giantswarm.io/getting-started-with-a-local-kubernetes-environment/)

## Extended Reading

For more extensive and deeper information on Kubernetes you should check out the [Reference Documentation](http://kubernetes.io/docs/reference/), which includes among others the [API documentation](http://kubernetes.io/docs/api/), [CLI documentation](http://kubernetes.io/docs/user-guide/kubectl-overview/), and a Glossary with deeper explanations of all resources.
