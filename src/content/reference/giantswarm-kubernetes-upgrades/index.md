+++
title = "Cluster Upgrades with Giant Swarm"
description = "A detailed explanation how Kubernetes and other components are upgraded with Giant Swarm"
date = "2018-08-31"
weight = 10
type = "page"
+++

# Cluster Upgrades with Giant Swarm

## Intro

The clusters created and managed by Giant Swarm consist of many components. There isn't only Kubernetes but also many other components like etcd, calico, prometheus, coredns and many others more. Each of these components has its own lifecycle and is released independently. We compile all these different projects into a Cloud Native Stack. This stack is continuously updated, both the individual project as well as the components in the control plane that manage these stacks in form of Kubernetes clusters. Each of your clusters have a version number in form of a Giant Swarm release attached to it. 

Our versioning system is based on a rolling release. This means that clusters can and will be upgraded continuously. We have invested a lot of time to provide automated and graceful upgrades. It doesn't matter which components are changed in the stack. However there are some differences between releases and also the way how certain services are upgraded. This article will give you a better overview about how upgrades are done with Giant Swarm.

## Concepts

### Rolling update

Out of experience we all know that smaller and more frequent upgrades are much easier to handle than big changes. Having one bug on a cluster that is easy to spot or to look for, because you know what was upgraded, is much simpler to deal with. On the same hand regularly doing upgrades means that the automation and the handling of the upgrades will get much better and robust compared to if you make an upgrade a rare event.

### Immutability

All components of the Giant Swarm stack are composed via images (vm and container). No components are patched or modified during their lifecycle.

### Reproducability

This one is easy once everything is already immutable. But this is very important to us too. Every cluster started with the same release version will be identical. Within one version nothing changes over time.

* Testing (e2e and conformance)

## Releases

* Explain patch, minor and major upgrades
    * Kubernetes minor releases are major releases at Giant Swarm
    * Minor and patch releases of Giant Swarm will be rolled out automatically
* Explain auto-updates vs control of upgrades
    * Major upgrades can be done by customers themselves
* Explain the lifecycle of releases (two active major versions are available at the same time. 30 days after kubernetes release it will be available to the user as a stable release. old clusters will be force upgraded)
    * 
* Explain versions of subcomponents

## Upgrades

* Explain upgrades in each provider. 
* Maybe include a highlevel diagram of how cluster-operator, node-operator and provider specific operators deal with upgrades

### AWS

* Cloudformation upgrade. Master first. Then rolling update of the ASG. 
    * more control over the ASG update is still in progress. goal here: new nodes are created first, until they are in the kubernetes api and ready and then the old nodes are drained and terminated.

### Azure

* Azure resource manager. All nodes get reimaged and the updated including the master. Master first.
    * This happens one by one. Nodes are drained and then rebooted with the new image and configuration
    * A delete has been discussed here instead of update of existing nodes. But this is not clear yet.

### KVM

* kvm-operator updating one node after each other.
    * Master first?
    * Nodes are drained and then the pod is replaced with a new version.

## Best practises so your services survive upgrades without downtime

* Having 2 or more replicas for deployments
* Have well implemented live and ready probes
* Set proper values for initialDelaySeconds and termincationGracePeriod (related to previous point)
* Configure PodDisruptionBudget for deployments
* Try to make containers as light as possible
* Consider running descheduler
* Ensure all container images (tags) are in the registry
* Set resource limits (not a must have but could help)
* Consider using pod priority preemption to ensure critical pods run always
* Avoid using pods without backed up resource (deployment, daemonset, ...)
* Avoid using local storage (or use it as cache)
