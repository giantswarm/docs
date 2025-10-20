---
linkTitle: Job management
title: Job management with Kueue
description: Learn how to use Kueue for Kubernetes-native job queueing and resource management in Giant Swarm workload clusters to efficiently manage batch workloads, ML training jobs, and resource quotas.
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

### Why use Kueue?

- **Resource quotas and fair sharing**: Implement quotas and policies for fair resource distribution among different teams and tenants
- **Advanced job queueing**: Queue jobs based on priorities with different strategies like `StrictFIFO` and `BestEffortFIFO`
- **Resource fungibility**: Automatically use alternative resource flavors when preferred resources are unavailable
- **Preemption support**: Allow higher-priority jobs to preempt lower-priority ones when resources are constrained
- **Gang scheduling support**: All-or-nothing scheduling semantics for distributed workloads that require coordinated resource allocation

### Key Features

Based on the [official Kueue documentation](https://kueue.sigs.k8s.io/docs/overview/), Kueue provides:

- **Job management**: Support for job queueing with priority-based scheduling strategies
- **Advanced resource management**: Resource flavor fungibility, fair sharing, cohorts, and preemption policies
- **Wide integration support**: Built-in support for Kubernetes Jobs, Kubeflow training jobs, RayJob, RayCluster, JobSet, AppWrappers, and plain Pods
- **System insights**: Built-in Prometheus metrics and on-demand visibility for monitoring pending workloads
- **Admission checks**: Mechanisms for internal or external components to influence workload admission
- **Topology-aware scheduling**: Optimize pod-to-pod communication by scheduling based on data center topology

### Core Concepts

- **ClusterQueue**: Defines resource quotas and admission policies for a cluster
- **LocalQueue**: Provides a namespace-scoped interface to submit jobs to a ClusterQueue
- **ResourceFlavor**: Represents different types of resources (e.g., different instance types, zones)
- **Workload**: Kueue's representation of a job that needs resources
- **Cohort**: Groups ClusterQueues to enable resource borrowing between them

## Prerequisites

Before setting up Kueue, ensure you have:

- A Giant Swarm workload cluster
- `kubectl` configured to access your workload cluster
- Access to the Giant Swarm platform API for app installation
- Basic understanding of Kubernetes batch workloads and resource management

## Installation

Kueue is available as a managed app in the Giant Swarm catalog. You can install it using the Giant Swarm app platform.

### Install Kueue App

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
```
NAME                                        READY   STATUS    RESTARTS   AGE
kueue-controller-manager-74c8f8c7c4-x7jwz   2/2     Running   0          2m
```

Verify that Kueue CRDs are installed:

```bash
kubectl get crd | grep kueue
```

Expected output:
```
clusterqueues.kueue.x-k8s.io                    2025-10-16T10:00:00Z
localqueues.kueue.x-k8s.io                      2025-10-16T10:00:00Z
resourceflavors.kueue.x-k8s.io                  2025-10-16T10:00:00Z
workloads.kueue.x-k8s.io                        2025-10-16T10:00:00Z
...
```

## Configuration

### Basic Setup

Create a basic Kueue configuration with resource flavors, cluster queue, and local queue:

#### Step 1: Create Resource Flavors

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

## Usage Examples

### Basic Batch Job

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

### Machine Learning Training Job

Example using a PyTorch training job with GPU resources:

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: pytorch-training
  namespace: default
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      template:
        metadata:
          labels:
            kueue.x-k8s.io/queue-name: local-queue
        spec:
          containers:
          - name: pytorch
            image: pytorch/pytorch:latest
            command: ["python", "train.py"]
            resources:
              requests:
                nvidia.com/gpu: 1
                cpu: 2
                memory: 4Gi
    Worker:
      replicas: 2
      template:
        metadata:
          labels:
            kueue.x-k8s.io/queue-name: local-queue
        spec:
          containers:
          - name: pytorch
            image: pytorch/pytorch:latest
            command: ["python", "train.py", "--worker"]
            resources:
              requests:
                nvidia.com/gpu: 1
                cpu: 2
                memory: 4Gi
```

### Gang Scheduling with All-or-Nothing Semantics

Kueue supports gang scheduling through its "All-or-Nothing" semantics, ensuring that either all pods in a job are scheduled together or none are scheduled. This is particularly useful for distributed training jobs and tightly coupled workloads.

#### Basic Gang Scheduling Configuration

Enable all-or-nothing scheduling in your ClusterQueue:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: gang-scheduling-queue
spec:
  namespaceSelector: {}
  queueingStrategy: BestEffortFIFO
  resourceGroups:
  - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
    flavors:
    - name: default-flavor
      resources:
      - name: "cpu"
        nominalQuota: 100
      - name: "memory"
        nominalQuota: 200Gi
    - name: gpu-flavor
      resources:
      - name: "nvidia.com/gpu"
        nominalQuota: 8
  # Enable all-or-nothing scheduling with timeout
  admissionChecksStrategy:
    admissionChecks:
    - name: all-or-nothing-check
```

#### JobSet with Gang Scheduling

Use JobSet for complex multi-job workflows that need coordinated scheduling:

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
          kueue.x-k8s.io/queue-name: user-queue
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
          kueue.x-k8s.io/queue-name: user-queue
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
                  cpu: 1
                  memory: 1Gi
            restartPolicy: Never
```

## Monitoring and Observability

### Check Queue Status

Monitor queue status and pending workloads:

```bash
# Check cluster queues
kubectl get clusterqueue

# Check local queues
kubectl get localqueue -A

# Check workloads
kubectl get workload -A

# Describe a specific queue for detailed information
kubectl describe clusterqueue cluster-queue
```

### Prometheus Metrics

Kueue provides built-in Prometheus metrics for monitoring:

- `kueue_admitted_workloads_total`: Total number of admitted workloads
- `kueue_pending_workloads`: Number of pending workloads per queue
- `kueue_cluster_queue_resource_usage`: Resource usage per cluster queue
- `kueue_admission_wait_time_seconds`: Time workloads wait before admission

You can check [our Observability platform]({{< relref "/overview/observability" >}}) to observe the status of the queues and workloads.

## Advanced Features

### Cohorts for Resource Sharing

Enable resource borrowing between cluster queues:

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
      maxPriorityThreshold: 100
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

## Troubleshooting

### Common Issues

1. **Jobs not being admitted**:

   ```bash
   kubectl describe workload -n NAMESPACE WORKLOAD_NAME
   # Check for admission conditions and resource availability
   ```

2. **Resource quota exceeded**:

   ```bash
   kubectl describe clusterqueue QUEUE_NAME
   # Check resource usage vs. quotas
   ```

3. **Queue not accepting jobs**:

   ```bash
   kubectl get clusterqueue
   # Ensure queue is active and not stopped
   ```

### Performance Tuning

For high-throughput environments, consider:

- Adjusting the `updateIntervalSeconds` in the visibility configuration
- Tuning the `queueingStrategy` (StrictFIFO vs BestEffortFIFO)
- Configuring appropriate `borrowingLimit` values for cohorts
- Setting up multiple cluster queues for different workload types

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
