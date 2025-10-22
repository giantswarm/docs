---
linkTitle: Job management
title: Job management with Kueue
description: Learn how to use Kueue for Kubernetes-native job queueing and resource management in Giant Swarm workload clusters to manage batch workloads efficiently, AI and ML training jobs, or resource quotas.
weight: 50
menu:
  principal:
    parent: tutorials-fleet-management
    identifier: tutorials-fleet-management-job-management
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How do I set up job queueing in my Giant Swarm cluster?
  - What is Kueue and how does it help with resource management?
  - How do I manage batch workloads and ML training jobs efficiently?
  - How do I set up gang scheduling for distributed workloads?
  - How do I configure all-or-nothing scheduling for coordinated jobs?
  - How do I install and configure Kueue in Giant Swarm?
last_review_date: 2025-10-16
---

Kueue is a Kubernetes-native system that manages quotas and how jobs consume them. It provides advanced job queueing, resource management, and fair sharing capabilities for batch workloads, machine learning training jobs, and other compute-intensive tasks. Giant Swarm supports Kueue through a managed app that simplifies installation and configuration.

This guide explains how to set up and use Kueue for job management in Giant Swarm workload clusters.

## Overview

Kueue addresses the challenges of managing compute resources in multi-tenant Kubernetes environments by providing:

### Why use Kueue

- **Resource quotas and fair sharing**: Implement quotas and policies for fair resource distribution among different teams and tenants
- **Advanced job queueing**: Queue jobs based on priorities with different strategies like `StrictFIFO` and `BestEffortFIFO`
- **Resource fungibility**: Automatically use alternative resource flavors when preferred resources are unavailable
- **Preemption support**: Allow higher-priority jobs to preempt lower-priority ones when resources are constrained
- **Gang scheduling support**: All-or-nothing scheduling semantics for distributed workloads that require coordinated resource allocation
- **Multi-cluster functionality**: Scale out jobs to different cluster targets to distribute your workloads, reducing costs and improving availability.

### Core concepts

- **ClusterQueue**: Defines resource quotas and admission policies for a cluster
- **LocalQueue**: Provides a namespace-scoped interface to submit jobs to a ClusterQueue
- **ResourceFlavor**: Represents different types of resources (for example, different instance types, zones)
- **Workload**: Kueue's representation of a job that needs resources
- **Cohort**: Groups ClusterQueues to enable resource borrowing between them

## Prerequisites

Before setting up Kueue, ensure you have:

- A Giant Swarm workload cluster
- `kubectl` configured to access your workload cluster
- Access to the Giant Swarm platform API for app installation
- Have `JobSet` extension on the workload cluster (`helm install jobset oci://registry.k8s.io/jobset/charts/jobset --version 0.10.1`). It will be automatically deployed in the near future as Kueue dependency.
- Basic understanding of Kubernetes batch workloads and resource management

## Installation

Kueue is available as a managed app in the Giant Swarm catalog. You can install it using the Giant Swarm app platform.

### Install Kueue app

Install the Kueue app using `kubectl gs`:

```bash
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=CLUSTER_NAME \
  --organization=ORGANIZATION \
  --name=kueue \
  --target-namespace=kueue-system \
  --version=0.1.0 > kueue.yaml

kubectl apply -f kueue.yaml
```

Replace `CLUSTER_NAME` and `ORGANIZATION` with your actual cluster name and organization.

### Verify Installation

Check that Kueue components are running:

```bash
kubectl get pods -n kueue-system
```

Expected output:

```text
NAME                                        READY   STATUS    RESTARTS   AGE
kueue-controller-manager-74c8f8c7c4-x7jwz   2/2     Running   0          2m
```

Verify that Kueue CRDs are installed:

```bash
kubectl get crd | grep kueue
```

Expected output:

```text
clusterqueues.kueue.x-k8s.io                    2025-10-16T10:00:00Z
localqueues.kueue.x-k8s.io                      2025-10-16T10:00:00Z
resourceflavors.kueue.x-k8s.io                  2025-10-16T10:00:00Z
workloads.kueue.x-k8s.io                        2025-10-16T10:00:00Z
...
```

## Configuration

### Basic setup

Create a basic Kueue configuration with resource flavors, cluster queue, and local queue:

#### Step 1: Create resource flavors

Resource flavors represent different types of compute resources:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: default-flavor
spec:
  nodeLabels:
    node.kubernetes.io/instance-type: m5.xlarge
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: gpu-flavor
spec:
  nodeLabels:
    node.kubernetes.io/instance-type: g4dn.4xlarge
  tolerations:
  - key: nvidia.com/gpu
    value: "true"
    effect: NoSchedule
```

#### Step 2: Create queues

First, lets create a cluster queue like:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: cluster-queue
spec:
  namespaceSelector: {}  # Allow all namespaces
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: default-flavor
      resources:
      - name: "cpu"
        nominalQuota: 100
      - name: "memory"
        nominalQuota: 200Gi
  - coveredResources: ["nvidia.com/gpu"]
    flavors:
    - name: gpu-flavor
      resources:
      - name: "nvidia.com/gpu"
        nominalQuota: 4
```

And later create a local one for our example:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: LocalQueue
metadata:
  namespace: default
  name: local-queue
spec:
  clusterQueue: cluster-queue
```

## Usage examples

### Basic batch job

Create a simple batch job that uses Kueue for scheduling:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: sample-job
  namespace: default
  labels:
    kueue.x-k8s.io/queue-name: local-queue
spec:
  parallelism: 3
  completions: 3
  suspend: true
  template:
    metadata:
      labels:
        kueue.x-k8s.io/queue-name: local-queue
    spec:
      containers:
      - name: sample-workload
        image: gcr.io/k8s-staging-perf-tests/sleep:latest
        args: ["30s"]
        resources:
          requests:
            cpu: 1
            memory: 200Mi
      restartPolicy: Never
```

### Gang scheduling

Kueue supports gang scheduling through its "All-or-Nothing" semantics, ensuring that either all pods in a job are scheduled together or none are scheduled. This is particularly useful for distributed training jobs and tightly coupled workloads.

#### Basic configuration

First, you need to customize the Kueue configuration to enable the `waitForPodsReady` setting:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-kueue-userconfig
  namespace: org-<ORGANIZATION>
data:
  values: |
    waitForPodsReady:
      enable: true
      timeout: 10m
```

Now update the app resource to point to the configmap:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: <CLUSTER_NAME>-kueue
  namespace: org-fer
spec:
  ...
  userConfig:
    configMap:
      name: <CLUSTER_NAME>-kueue-userconfig
      namespace: org-<ORGANIZATION>
```

Now define two new queues (Cluster and Local) to run the tests:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: gang-cluster-queue
spec:
  namespaceSelector: {}
  resourceGroups:
  - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
    flavors:
    - name: default-flavor
      resources:
      - name: "cpu"
        nominalQuota: 10
      - name: "memory"
        nominalQuota: 20Gi
    - name: gpu-flavor
      resources:
      - name: "nvidia.com/gpu"
        nominalQuota: 2
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: LocalQueue
metadata:
  namespace: default
  name: gang-queue
spec:
  clusterQueue: "gang-cluster-queue"
```

Now, you create a `JobSet` to define a driver controller and some workers:

```yaml
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: gang-jobset
  namespace: default
spec:
  replicatedJobs:
  - name: driver
    replicas: 1
    template:
      metadata:
        labels:
          kueue.x-k8s.io/queue-name: gang-queue
      spec:
        parallelism: 1
        completions: 1
        template:
          spec:
            containers:
            - name: driver
              image: busybox:latest
              command: ["sh", "-c", "echo 'Driver job running'; sleep 60"]
              resources:
                requests:
                  cpu: 1
                  memory: 1Gi
            restartPolicy: Never
  - name: workers
    replicas: 3
    template:
      metadata:
        labels:
          kueue.x-k8s.io/queue-name: gang-queue
      spec:
        parallelism: 2
        completions: 2
        template:
          spec:
            containers:
            - name: worker
              image: busybox:latest
              command: ["sh", "-c", "echo 'Worker job running'; sleep 45"]
              resources:
                requests:
                  cpu: 2
                  memory: 2Gi
                  nvidia.com/gpu: 1
            restartPolicy: Never
            tolerations:
            - key: nvidia.com/gpu
              value: "true"
              effect: NoSchedule
```

Once you submit the `JobSet`, it will create two `ReplicatedJobs`, which, in turn, will make three worker replicas with two jobs assigned to each. Since those jobs require way more memory, CPU, and GPU resources, the job will not be scheduled, and the whole group will be requeued after a timeout. You can relax the requests and see how the Kueue controller schedules the jobs altogether when capacity is available.

### Prometheus metrics

Kueue comes with a set of built-in Prometheus metrics for observe the state of the jobs and queues. You need to pass the proper configuration at deployment time to get those into the Observability platform.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-kueue-userconfig
  namespace: org-<ORGANIZATION>
data:
  values: |
    ...
    enablePrometheus: true
```

It will create a `ServiceMonitor` in the Kueue namespace which instruct the alloy agent to collect the specific metrics. Some of these metrics are:

- `kueue_admitted_workloads_total`: Total number of admitted workloads
- `kueue_pending_workloads`: Number of pending workloads per queue
- `kueue_cluster_queue_resource_usage`: Resource usage per cluster queue
- `kueue_admission_wait_time_seconds`: Time workloads wait before admission

You can access [our Observability platform UI]({{< relref "/overview/observability/dashboard-management/dashboard-exploration/" >}}) to get a glance of those metrics.

## Advanced Features

### Cohorts for Resource Sharing

In multi-team environments where different teams have varying workload patterns competing for resources, you may need some higher abstractions to manage those resource properly. Cohorts enable dynamic resource redistribution, improving overall cluster utilization and reducing job wait times.

This is an example for enabling resource borrowing between cluster queues:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: team-a-queue
spec:
  cohort: shared-cohort
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: default-flavor
      resources:
      - name: "cpu"
        nominalQuota: 50
        borrowingLimit: 100
      - name: "memory"
        nominalQuota: 100Gi
        borrowingLimit: 200Gi
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: team-b-queue
spec:
  cohort: shared-cohort
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: default-flavor
      resources:
      - name: "cpu"
        nominalQuota: 50
        borrowingLimit: 100
      - name: "memory"
        nominalQuota: 100Gi
        borrowingLimit: 200Gi
```

### Preemption Policies

Preemption policies are essential when you need to ensure that critical, can access resources immediately, even when the cluster is fully utilized by lower-priority jobs. Preemption may help too maintaining SLA compliance and ensures that business-critical workloads are never blocked by less important tasks.

First, let's configure the workload priority classes:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: WorkloadPriorityClass
metadata:
  name: high-priority
value: 1000
description: "Priority class for critical jobs"
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: WorkloadPriorityClass
metadata:
  name: low-priority
value: 100
description: "Priority class for non critical jobs"
```

Configure preemption to allow higher-priority jobs to preempt lower-priority ones:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: preemption-queue
spec:
  preemption:
    reclaimWithinCohort: Any
    borrowWithinCohort:
      policy: LowerPriority
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: default-flavor
      resources:
      - name: "cpu"
        nominalQuota: 100
      - name: "memory"
        nominalQuota: 200Gi
```

Now configure the job with the proper label:

```yaml
  labels:
    ...
    kueue.x-k8s.io/priority-class: [low|hight]-priority
```

Now you can submit first the low priority job and after it is scheduled, you deploy the high priority one. You can observe how first one is evicted to leave space for the second one.

You can configure more complex scenarios using [fair sharing](https://kueue.sigs.k8s.io/docs/concepts/preemption/#fair-sharing).

## Best Practices

1. **Resource Planning**: Design resource flavors that match your actual node types and availability zones
2. **Queue Organization**: Create separate queues for different workload types (batch, ML training, gang-scheduled jobs)
3. **Quota Management**: Set realistic quotas based on actual cluster capacity and usage patterns
4. **Gang Scheduling**: Use all-or-nothing semantics for distributed workloads that require coordinated scheduling
5. **Monitoring**: Implement monitoring for queue depths, admission rates, and resource utilization
6. **Preemption Strategy**: Use preemption carefully to balance resource efficiency with job stability
7. **Testing**: Test queue configurations in development environments before applying to production
8. **Timeout Configuration**: Set appropriate timeouts for gang-scheduled jobs to avoid resource deadlocks

## Further Reading

- [Kueue Official Documentation](https://kueue.sigs.k8s.io/docs/overview/)
- [Kueue GitHub Repository](https://github.com/kubernetes-sigs/kueue)
- [Giant Swarm Kueue App Repository](https://github.com/giantswarm/kueue-app)
- [Kubernetes Job Management Best Practices](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
