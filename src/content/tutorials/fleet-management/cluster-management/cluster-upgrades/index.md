---
title: Cluster upgrades deep dive
description: General information about how cluster upgrades work and how to tune them.
weight: 10
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-cluster-upgrades
user_questions:
  - How do cluster upgrades work?
  - How can I prepare my workloads to tolerate a cluster upgrade?
  - How can I limit the disruption caused by cluster upgrades?
last_review_date: 2025-01-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

This guide is focus on explaining the details on how workload cluster upgrades work and how to prepare your workloads to remain operational during a workload cluster upgrade. A workload cluster in a Giant Swarm platform is running a stack comprising many software components, provided by the Kubernetes project and other open source projects or software vendors, as well as by Giant Swarm. In order to keep all components up-to-date, to allow you to benefit from latest improvements, features and security fixes, the platform provides upgrades for the entire software stack in workload clusters.

Giant Swarm advocates for frequent, small updates to keep the change in the system manageable. Our goal is to help you run all clusters on the latest version without disrupting your operations.

## Background and concepts

### The workload cluster stack

The workload cluster stack includes third-party components such as:

- [Kubernetes](https://kubernetes.io/) with its sub-components
- [Flatcar Container Linux](https://www.flatcar-linux.org/docs/latest/) as the node's operating system
- [Containerd](https://github.com/containerd/containerd) as a container runtime environment
- [Etcd](https://etcd.io/) for distributed storage
- [Cilium](https://cilium.io/) for networking and security
- [An observability bundle](https://github.com/giantswarm/observability-bundle)
- [A security bundle](https://github.com/giantswarm/security-bundle)
- [Ingress controller](https://github.com/kubernetes/ingress-nginx) for routing traffic

among other operators and APIs maintained by Giant Swarm.

These components are bundled into a **workload cluster release** specific to the provider (AWS, Azure, or VMware), identified by a version number. For more information, see the [workload cluster releases](https://github.com/giantswarm/releases/) repository with all available releases.

The stack is **immutable** once deployed, ensuring consistency with the tested stack. Changes are only made through upgrades to a new workload cluster release.

### Upgrade semantics {#semantics}

Workload cluster release versioning allows for three upgrade levels:

- _Patch upgrade_: Increases the patch version for bug fixes and stability improvements.
- _Minor upgrade_: Introduces non-disruptive features that are typically less significant than major updates, unless the features are actively enabled.
- _Major upgrade_: Includes new Kubernetes minor releases, third-party components, and significant new features.

Major releases are aligned with Kubernetes upstream minor releases and include comprehensive release notes to aid preparation.

#### Considerations {#considerations}

Upon releasing a new major version, the oldest major release is deprecated. Deprecated releases can only create clusters using `kubectl-gs`. Existing clusters remain unaffected.

Creating new clusters with deprecated releases is discouraged. Testing workload cluster upgrades in a separate environment is recommended.

### Upgrade automation

**Patch and minor upgrades** are rolled out automatically by Giant Swarm, respecting agreed maintenance windows. Our team is developing the automation necessary to further streamline this process, allowing customers to manage maintenance windows effectively.

**Major upgrades** are not automated. You are notified to schedule the upgrade, possibly after updating workloads. Giant Swarm staff may assist or initiate these upgrades to ensure continuity.

### Skipping workload cluster release

Skipping major versions when upgrading is unsupported. Upgrades must proceed sequentially through major versions.

You can skip minor and patch releases if needed. Our interfaces default to the next active workload cluster release. To skip a version:

- In the **GitOps** workflow, update the cluster configuration file with the desired release version.
- Using **kubectl-gs**, use the [`update cluster`]({{< relref "/reference/kubectl-gs/update-cluster" >}}) command with the `--release-version` flag.

## How upgrades work

Upgrades occur at runtime, maintaining workload functionality (with certain requirements). Key steps include:

- Nodes are drained, stopped, and recreated.
- Pods are rescheduled during node draining.
- Control plane node recreation could causes brief Kubernetes API unavailability though the API server is highly available minimizing the impact.

### Specific details for AWS

The control plane machines are rotated first, followed by worker nodes. The control plane nodes are replaced one by one, ensuring the cluster remains operational.

The Cluster API for AWS controller manages the cluster control plane using EC2 instances. The default configuration of [instance warmup](https://github.com/search?q=repo%3Agiantswarm%2Fcluster-aws%20refreshPreferences&type=code) ensures AWS doesn't replace all nodes at once but in steps, allowing human intervention if needed. For a small node pool, one node is replaced every 10 minutes. For larger pools, small sets of nodes are replaced every 10 minutes.

Once the worker nodes are rolled, each instance receives a terminate signal from AWS. Thanks to [`aws-node-termination-handler`](https://github.com/aws/aws-node-termination-handler) the machines are drained gracefully before being terminated. By default, the timeout configure to complete the draining operation is [`global.nodePools.PATTERN.awsNodeTerminationHandler.heartbeatTimeoutSeconds=1800`](https://github.com/giantswarm/cluster-aws/blob/main/helm/cluster-aws/README.md#node-pools). Customers can adjust this value to fit their needs in case they have specific requirements.

### Specific details for Azure

TBD

### Specific details for vSphere

TBD

### Specific details for vCloud Director

TBD

## How to upgrade a cluster {#how-to-upgrade-a-cluster}

Authenticated users can upgrade clusters to the **next active workload cluster release** using the platform API. Our CLI extensions allows to trigger the action thanks to the command [`kubectl-gs update cluster`]({{< relref "/reference/kubectl-gs/update-cluster" >}}).

Giant Swarm selects upgrade versions following best practices, avoiding skips over major versions. Test upgrades in non-production environments if using raw API methods.

## Checklist {#checklist}

Before upgrading, complete the following checks and best practices:

### Overview

- [Ensure redundancy for workloads](#checklist-ensure-redundancy)
- [Distribute workloads across nodes](#checklist-distribute-workloads)
- [Use liveness and readiness probes](#checklist-liveness-readiness)
- [Handle termination signals in Pods](#checklist-termination-signals)
- [Manage disruption budgets](#checklist-disruption-budgets)
- [Set scheduling priorities](#checklist-scheduling-priorities)
- [Consider high-availability control planes](#checklist-ha-masters)
- [Avoid ephemeral resources](#checklist-avoid-ephemeral-resources)
- [Configure webhook timeouts](#checklist-webhook-timeouts)
- [Verify that all your pods are running](#checklist-verify-pods-running)
- [General container hygiene](#checklist-general-hygiene)

### Ensure redundancy for workloads {#checklist-ensure-redundancy}

Ensure **two or more replicas** for all critical deployments, with higher counts for production environments. Adjust based on environment needs, ensuring `Horizontal Pod Autoscaler` settings reflect minimum replica requirements.

### Distribute workloads across nodes {#checklist-distribute-workloads}

Use [inter-pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) to distribute replicas across nodes, avoiding simultaneous unavailability. Consider using the [descheduler](https://github.com/kubernetes-sigs/descheduler) to balance workloads.

### Use liveness and readiness probes {#checklist-liveness-readiness}

Implement [liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) to manage traffic routing and container termination gracefully. Set appropriate `initialDelaySeconds` values.

### Handle termination signals in Pods {#checklist-termination-signals}

Pods receive a termination signal (`TERM`) during node draining. Ensure they handle this signal gracefully. Configure `terminationGracePeriodSeconds` for longer shutdowns if necessary. See [`Pod Termination`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).

### Manage disruption budgets {#checklist-disruption-budgets}

Use [PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to maintain minimum pod counts during upgrades. Avoid setting `maxUnavailable=0` for single-replica deployments to prevent upgrade blocks.

### Set scheduling priorities {#checklist-scheduling-priorities}

Utilize Pod priority classes to manage scheduling under resource pressure. Set resource requests and limits to influence scheduling decisions.

### Avoid ephemeral resources {#checklist-avoid-ephemeral-resources}

Avoid using ephemeral resources like standalone Pods or local storage for persistent data. Use controllers (Deployments, StatefulSets) for reliability.

### Configure webhook timeouts {#checklist-webhook-timeouts}

Ensure validation and mutation webhooks have appropriate [timeouts](https://github.com/kubernetes/kubernetes/issues/71508#issuecomment-470315405) to prevent upgrade disruptions. Use low timeout values:

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

Ensure all critical pods are operational, and no deployments are stuck. Use this command to check:

```nohighlight
kubectl get pods --all-namespaces | grep -v "Running\|ContainerCreating"
```

### General container hygiene {#checklist-general-hygiene}

There’s additional general container hygiene recommendations that will help smoothen the upgrade process.

As container images might not be already available on the new node that the `Pod` gets rescheduled to, you should make sure that all container images (and tags) that you are using are available in the registry that is configured for the pods.

Furthermore, you should make your containers are as lightweight (in terms of size) as possible to make the image pulling and the rescheduling process faster.
