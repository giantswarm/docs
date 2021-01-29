---
linkTitle: Cluster upgrades
title: Workload cluster upgrades
description: How Kubernetes and other components are upgraded in a Giant Swarm workload cluster, and how to prepare your cluster and workloads to facilitate robust upgrades.
weight: 40
menu:
  main:
    parent: general
user_questions:
  - How do cluster upgrades work?
  - How can I prepare my workloads to tolerate a cluster upgrade?
  - What is a major upgrade?
  - What is a minor upgrade?
  - What is a patch upgrade?
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# Cluster upgrades

A workload cluster (formerly called _tenant cluster_) in a Giant Swarm installation is running a stack comprising many software components, provided by the Kubernetes project and other open source projects or software vendors, as well as by Giant Swarm.
In order to keep all components up-to-date, to allow you to benefit from latest improvements, features and security fixes, we provide upgrades for the entire software stack in workload clusters.

At Giant Swarm we believe that frequent, small updates are the way to keep the change in the system manageable. That is why our goal is to help you to run all the clusters in the latest version.
We invest a lot of effort in making this happen without disrupting your usage of your clusters.

In this article, we explain how upgrades work in detail and how you should provide your workloads in order to keep them running during a workload cluster upgrade and prevent disruptions of your applications.

## Background and concepts

### The workload cluster stack

Among the third party components building a workload cluster stack are

- [Kubernetes](https://kubernetes.io/) with its many sub-components
- [Flatcar Container Linux](https://docs.flatcar-linux.org/) as the node's operating system
- [Docker](https://docs.docker.com/engine/) as a container runtime environment
- [etcd](https://etcd.io/) as distributed storage for Kubernetes and Vault
- [Project Calico](https://www.projectcalico.org/) and [AWS CNI](https://github.com/aws/amazon-vpc-cni-k8s)/[Azure CNI](https://github.com/Azure/azure-container-networking)/[Flannel](https://github.com/coreos/flannel) for virtual networking
- [CoreDNS](https://coredns.io/) for cluster-internal name resolution
- [Prometheus node exporter](https://github.com/prometheus/node_exporter) for hardware and OS metrics
- [NGINX Ingress Controller](https://github.com/kubernetes/ingress-nginx) for connecting services with load balancers

as well as many operators and controllers created and maintained by Giant Swarm.

All of the items in the list above are released independent of each other by their vendors.
At Giant Swarm we bundle specific versions of these components of the workload cluster stack into a **workload cluster release**. A workload cluster release is specific for a provider (AWS, Azure, or KVM) and identified by a version number. To learn more about workload cluster releases and our versioning, check the [workload cluster releases reference](/reference/workload-cluster-release-versions/).

Once deployed, the workload cluster stack is **immutable**.
All components are deployed based on images, either of virtual machines or of Docker containers.
No changes are ever made to components at runtime.
This ensures that the stack running in your environment is the exact stack we tested before.

As a consequence, the only way to change the stack is to perform an upgrade, to switch to a new workload cluster release.

### Upgrade semantics {#semantics}

According to our workload cluster release versioning, three different levels of upgrades can occur:

- *Patch upgrade*: Only the patch version number is increased.

- *Minor upgrade*: The minor version number is increased, while the major version number stays the same.

- *Major upgrade*: The major version number is increased.

#### Patch upgrade {#patch-upgrade}

Patches contain bug fixes only. Individual patches are as minimal as possible and they are needed to increase the stability of the cluster or to fix a CVE. They are released based on upstream information and/or learnings from managing clusters for customers.

#### Minor upgrade {#minor-upgrade}

In case we are releasing features in a nondisruptive way (i.e. feature flagged) we will put those in minor releases. Those will actually have even less impact than a patch as they will not change anything that is in place if the customer doesn't explicitly enable it.

#### Major upgrade {#major-upgrade}

Every few months, typically in synchronization with Kubernetes Upstream Minor Releases, we provide a new major release. It includes the new Kubernetes Minor Release, other components by third parties, and any new versions of our software that contain deeper new functionality. It means that new developments, like node pools or networking changes, are delivered within a major release.

As always we provide release notes with all the information needed. Under this new structure, we are working to provide them for major Releases early to allow for your preparation.

#### Considerations {#considerations}

Once we publish a new major release, we deprecate the oldest major release.
This means that new clusters with deprecated releases can only be created using `gsctl`.
Existing clusters, however, are not affected.

Creating clusters with deprecated releases is not recommended. Testing workload cluster upgrades in a separate cluster should be the only use case.

### Upgrade automation

**Both patch and minor upgrades** can be rolled out at any time by Giant Swarm without your interaction. Currently, we agree with customers which time windows are available for upgrades in the different environments. We are working towards creating automation that will manage all the upgrade logic for us. This will be based on letting customers plan maintenance periods and policies to ensure it does not disrupt business as usual.

**New major versions** are not automated. Instead, we inform you but leave the scheduling of the upgrade to you. This gives you the control to decide if and when it is time for you to upgrade, potentially updating workloads first. These upgrades are also accompanied or even triggered by Giant Swarm staff, to ensure we keep a close eye on the upgrade process and the uptime of your workloads.

### Skipping workload cluster release

We **don't support omitting any major version** when upgrading from one workload cluster release to another.

Example: Going from v11.x.x directly to v13.x.x is not supported. An upgrade to v12.x.x would be required as an intermediate step.

On the Minor and Patch level, you can skip any number of workload cluster releases if desired.

Note that by default, our user interfaces upgrade to the next active workload cluster release. In order to skip a release version, you have several options, depending on the tool you use:

- In the **web interface**, open the details page for a cluster. Click the release version of the cluster. If upgrades are available for this release, they will be listed in the dialog. Simply click the desired target version in order to start the upgrade process. You will have an additional step for reviewing the changes before actually triggering the cluster upgrade.

- In **gsctl**, the [`upgrade cluster`](/reference/gsctl/upgrade-cluster/) command provides an optional flag `--release` which allows to specify the version to upgrade to.

- Alternatively, you can use the [Rest API](/api/#operation/modifyClusterV5) or the [Management API](/basics/api/#management-api) to trigger the upgrade. Please talk to your solution engineer in case you have any questions regarding this.

## How upgrades work

All levels of upgrades, patch, minor, or major, are happening at runtime.
Your Kubernetes workloads should continue to work as expected (given they meet a few requirements, as explained further below).

In particular this means:

- Nodes will be drained, then stopped, then recreated.
- As a consequence of draining, Pods running on a node will be rescheduled to other nodes.
- Once the master node is taken down and recreated, the Kubernetes API will be unavailable for a short time.

**Note**: By default, workload clusters have one master node each. [Consider using a High Availability masters setup](#checklist-ha-masters) to avoid API downtime during upgrades.

### Specific details for AWS

AWS resources are managed by the [aws-operator](https://github.com/giantswarm/aws-operator) component through a nested CloudFormation stack. For a workload cluster upgrade, the CloudFormation stacks are updated, in several steps.

The master node re-creation is started first. Meanwhile, the recreation of worker nodes starts, where all worker nodes are recreated in batches. During the upgrade, **up to 33 percent of the worker nodes may become unavailable**.

From workload cluster release v12.7.0 some of the parameters of the upgrade can be configured. Check [Fine-tuning upgrade disruption on AWS](/guides/fine-tuning-upgrade-disruption-on-aws/) guide for more details.

After recreation, worker nodes are **not expected to have the same names** they had before.

In process of the worker node recreation, any data stored in worker node's local storage, i. e. outside of EBS volumes, is lost.

**Note:** We are in the process of making upgrades on AWS less disruptive.
For example, we are aware that for larger clusters, one thirds of worker nodes becoming unavailable at the same time is often too much.

### Specific details for Azure

Our [azure-operator](https://github.com/giantswarm/azure-operator) manages workload clusters on Azure via Azure Resource Manager (ARM) templates and Virtual Machine Scale Sets (VMSS).

In an upgrade, all Virtual Machines (VM) are updated by reimaging with a new OS image and then rebooting.
Master and worker nodes are updated one by one, where each node is first drained (Pods re-scheduled to other nodes) and then reimaged and rebooted.

On Azure, the node names visible to Kubernetes (e. g. `kubectl get nodes`) are not changed in an upgrade.

**Note:** Any local storage in the node is erased. Persistent volumes are not affected by that.

### Specific details for KVM

In a KVM-based cluster, our [kvm-operator](https://github.com/giantswarm/kvm-operator) builds each workload cluster node out of a Kubernetes Deployment and Pod in the management cluster.
In an upgrade, each of these deployments is updated after the according node has been drained, one after another, starting with the master node.
This leads to removal and recreation of the Pods.

## How to upgrade a cluster {#how-to-upgrade-a-cluster}

As an authenticated user you can upgrade the cluster to the **next active workload cluster release**, using the web UI or the CLI. The web UI shows a yellow link next to the version information if there is an upgrade available. For the CLI you can use the command [`gsctl upgrade cluster`](/reference/gsctl/upgrade-cluster/) for the same purpose.

When the upgrade process is managed by our tools, the workload cluster release version chosen is selected by Giant Swarm according to best practices. It means it will not upgrade a cluster by more than one major version at a time. In case you use the raw API to upgrade your cluster please test the process against a non-production cluster first.

## Checklist {#checklist}

We recommend to work through the following list of checks and best practices before performing an upgrade on a cluster.

### Overview

- [Ensure redundancy for workloads](#checklist-ensure-redundancy)
- [Distribute workloads across nodes](#checklist-distribute-workloads)
- [Use liveness and readiness probes](#checklist-liveness-readiness)
- [Handle termination signals in Pods](#checklist-termination-signals)
- [Manage disruption budgets](#checklist-disruption-budgets)
- [Set scheduling priorities](#checklist-scheduling-priorities)
- [Consider high-availability masters](#checklist-ha-masters)
- [Avoid ephemeral resources](#checklist-avoid-ephemeral-resources)
- [Configure webhook timeouts](#checklist-webhook-timeouts)
- [Verify that all your pods are running](#checklist-verify-pods-running)
- [General container hygiene](#checklist-general-hygiene)

### Ensure redundancy for workloads {#checklist-ensure-redundancy}

Make sure you have **two or more replicas** for all your deployments. For critical components you might want to go with more than just the bare minimum of two.

You can adjust this depending on your environments, e.g. running 2 to 3 replicas in development, and 5 or more in production.

In case you are using the Horizontal Pod Autoscaler, above recommendations should depict your minimum replica setting.

### Distribute workloads across nodes {#checklist-distribute-workloads}

To avoid all replicas of the same deployment being unavailable at the same time, make sure they are distributed across several worker nodes using [inter-pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity).

We recommend to always use soft anti-affinity to avoid exclusivity of nodes. However, this can, in cases, lead to less distributed workloads on resource pressure or node failure, which will need a rescheduling to be balanced again.

For such rescheduling or rebalancing you should have a look at the incubation project called [descheduler](https://github.com/kubernetes-sigs/descheduler) and evaluate its use in your clusters. It has settings for avoiding affinities, but also for rebalancing clusters with under-utilized nodes.

### Use liveness and readiness probes {#checklist-liveness-readiness}

Have well implemented [liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

Often, a container being up does not mean it is ready to receive traffic. By differentiating between liveness and readiness you can not only control when traffic gets routed to a fresh container, you can also influence graceful termination of your container.

Also make sure to set proper values for `initialDelaySeconds`. This field tells the kubelet how long to wait before performing the first probe.

### Handle termination signals in Pods {#checklist-termination-signals}

When a node is drained in order to be upgraded, all workloads receive a termination signal (`TERM`) first. Make sure your pods are handling this signal to shut down gracefully. Otherwise they will be killed forcefully after a grace period. Check the [Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) documentation upstream for details.

If a pod takes a long time for a proper shutdown, configure the `terminationGracePeriodSeconds` to gain more time.

### Manage disruption budgets {#checklist-disruption-budgets}

Configure [PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) for all your deployments. This tells Kubernetes to keep a minimum amount of Pods running at all times and is respected by the draining/eviction mechanisms during upgrades.

### Set scheduling priorities {#checklist-scheduling-priorities}

Consider using Pod priority to ensure that higher priority Pods are scheduled favorably in times of resource pressure.

We recommend reading the upstream documentation about [priority classes and pod preemption](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/) to get a better understanding of how the scheduler works with these.

To help the scheduler further with being able to correctly (re-)schedule your Pods, you should [set resource request and limits](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/). This also sets the Quality of Service of a Pod, which again has influence on scheduling priorities.

### Consider high-availability masters {#checklist-ha-masters}

Some, but not all, cluster upgrades require nodes to be upgraded. With single master clusters, this causes a downtime of the Kubernetes API that can last a few minutes.

If you are running Giant Swarm on AWS, since workload cluster release v{{% first_aws_ha_masters_version %}} you have the option to use [high-availability masters](/basics/ha-masters/) instead. This will keep the Kubernetes API available even during an upgrade where nodes are rolled.

Consider this option before performing an upgrade. However, keep in mind that a cluster cannot be converted back from high-availability masters to a single master cluster.

### Avoid ephemeral resources {#checklist-avoid-ephemeral-resources}

In Kubernetes it is possible to schedule ephemeral resources.

For example a Pod by itself, i.e. without a Deployment, DaemonSet, StatefulSet, etc., is an ephemeral resource that will not be rescheduled when it dies or gets killed. A Pod definition should thus only be used for use cases like debugging or quick manual tests. Be sure to always use a controller-managed resource for your containers.

Furthermore, local storage in form of `emptyDir` is also ephemeral, and should not be used to persist data. It should only be used as a cache or temporary storage that you can live without in case of failure or rescheduling. In most cases this is also true of `hostPath` as the local storage of a new node might not be the same as the one of the old node.

### Configure webhook timeouts {#checklist-webhook-timeouts}

- In case there is a validation or mutation webhook configured you should check there is a [timeout](https://github.com/kubernetes/kubernetes/issues/71508#issuecomment-470315405) configured correctly to not break the upgrade process. We recommend using low timeouts for the webhooks resources.

```yaml
apiVersion: admissionregistration.k8s.io/v1beta1
kind: ValidatingWebhookConfiguration
metadata:
  name: <name of this configuration object>
webhooks:
- name: <webhook name>
  ...
  timeoutSeconds: 5
```

### Verify that all your pods are running {#checklist-verify-pods-running}

Verify all your important pods are running correctly, and there are no deployments stuck because of failures. Here is a `kubectl` command you can use for the purpose:

```nohighlight
kubectl get pods --all-namespaces | grep -v "Running\|ContainerCreating"
```

### General container hygiene {#checklist-general-hygiene}

There's additional general container hygiene recommendations that will help smoothen the upgrade process.

As container images might not be already available on the new node that the Pod gets rescheduled to, you should make sure that all container images (and tags) that you are using are available in the registry that is configured for the Pods.

Furthermore, you should make your containers are as lightweight (in terms of size) as possible to make the image pulling and the rescheduling process faster.

## Further reading

- [Workload cluster releases](/reference/workload-cluster-release-versions/) explains the semantics of workload cluster releases.
