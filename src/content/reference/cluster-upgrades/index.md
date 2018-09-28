+++
title = "Cluster Upgrades with Giant Swarm"
description = "A detailed explanation how Kubernetes and other components are upgraded in a Giant Swarm installation"
date = "2018-08-31"
weight = 30
type = "page"
+++

# Cluster Upgrades with Giant Swarm

A tenant cluster in a Giant Swarm installation is running a stack comprising many software components, provided by the Kubernetes project and other open source projects or software vendors, as well as by Giant Swarm.
In order to keep all components up-to-date, to allow you to benefit from latest improvements, features and security fixes, we provide upgrades for the entire software stack in tenant clusters.

At Giant Swarm we believe that frequent, small updates are a way to keep change in the system manageable.
We invest a lot of effort in making this happen without disrupting your usage of your clusters.

In this article, we explain how upgrades work in detail and how you should provide your workloads in order to keep them running during a tenant cluster upgrade and prevent disruptions of your applications.

## Background and Concepts

### The tenant cluster stack

Among the third party components building a tenant cluster stack are

- CoreOS container linux as the node's operating system
- Project Calico for virtual networking
- HashiCorp Vault as a public key infrastructure
- Docker as a container runtime environment
- CoreOS etcd as distributed storage for Kubernetes and Vault
- CoreDNS for cluster-internal name resolution
- Prometheus node exporter for hardware and OS metrics
- Kubernetes with its many sub-components
- NGINX Ingress Controller for connecting services with load balancers

as well as many operators and controllers created and maintained by Giant Swarm.

### Releases

All of the items in the list above are released independent of each other by their vendors.
At Giant Swarm we "bundle" specific versions of these components of the tenant cluster stack into a **release**.
A release is identified by a [semantic version number](https://semver.org/).

Once deployed, the tenant cluster stack is **immutible**.
All components are deployed based on images, either of virtual machines or of Docker containers.
No changes are ever made to components at runtime.
This ensures that the stack running in your environment is the exact stack we have tested before.

As a consequence, the only way to change the stack is to perform an upgrade, to switch to a new release.

#### Release upgrade semantics

As the semantic versioning system defines, an upgrade from one version to another is either one of these:

- *Patch*: The smallest type of upgrade occurs when we publish bugfixes, security fixes or make changes to the observability while maintaining the given functionality of the stack.
This can include any sort of patch upgrades of third party components.

- *Minor*: A minor upgrade occurs when we add functionality, while maintaining the functionality of the stack as it was in the previous version.
This can include minor upgrades of third party components, with the exception of Kubernetes.

- *Major*: A major upgrade occurs when (A) a minor Kubernetes version upgrade is picked up (e. g. from 1.10.* to 1.11.*), when we remove functionality or change functionality that my require changes in workloads, in automation working with the cluster or in administrator's interactions.

**Note:** The release version number is provider-specific.
Azure, AWS, and KVM based installations have independent versioning systems, as their stacks are also slightly different.

### Determining the release version and inspecting release details

As a user with access to the Giant Swarm API and being member of the organization owning the cluster, you can use both the web UI or the CLI to find out what release version your tenant cluster has currently.

In the web UI, both the cluster overview and the cluster details page show the release version number. 
In the cluster details page you can click the release version number to get more information about a release.

Likewise in the CLI, commands like [`gsctl list clusters`](/reference/gsctl/list-clusters/) and [`gsctl show cluster`](/reference/gsctl/show-cluster/) reveal the release version number.
To get information on all releases, use the [`gsctl list releases`](/reference/gsctl/list-releases/) command.

### Release lifecycle

**We hold two different major releases** available at any time to chose from when creating a new cluster, which means that you have two different Kubernetes minor versions to chose from.

Whenever a new Kubernetes minor version is released by the Kubernetes project, we make that version available in a new major release of our stack within 30 days from the Kubernetes release.

Once we publish a new major release, we deprecate the oldest major release.
This means that no new clusters can be created using that old release version.
Existing clusters however are not affected.

**Both patch and minor upgrades** can be rolled out at any time **automatically** by Giant Swarm without your interaction.

When a **new major release** becomes available, we inform you, but leave triggering the upgrade to you. This gives you the control to decide if and when it is time for you to upgrade, potentially updating workloads first. The upgrade can be triggered using either our web UI, our CLI or the API directly.

TODO: explain more, maybe show screenshot of happa upgrades, show link.

## How upgrades work

All levels of upgrades, patch, minor, or major, are happening at runtime.
Your Kubernetes workloads can continue to work as expected (given they meet a few requirements, as explained firther below).

In particular this means:

- The master node will be taken down, resulting in the Kubernetes API being unavailable.
- The worker nodes will be taken down, resulting in pods being rescheduled to other nodes.

**Note**: We have master node high-availability (multiple master nodes) on our roadmap, which will help prevent Kubernetes API downtimes during upgrades.

---

## Remainders of outline

* Testing (e2e and conformance)

## Releases

* old clusters will be force upgraded)
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

## How to prepare your workloads

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
