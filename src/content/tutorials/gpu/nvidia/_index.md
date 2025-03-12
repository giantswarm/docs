---
linkTitle: GPU workloads in CAPI clusters with NVIDIA
title: Running GPU workloads in CAPI workload clusters with NVIDIA
description: This guide explains how to run NVIDIA GPU-accelerated workloads in CAPI workload clusters.
weight: 110
menu:
  principal:
    parent: tutorials-gpu
    identifier: tutorials-gpu-nvidia
user_questions:
  - How can I run NVIDIA GPU workloads in CAPI clusters?
  - How can I configure NVIDIA GPU-enabled nodes in CAPI clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-tenet
last_review_date: 2025-03-12
---

# Running NVIDIA GPU workloads in CAPI workload clusters

This guide explains how to configure and use GPU-enabled nodes in Cluster API (CAPI) workload clusters to run GPU-accelerated workloads.
GPU support is available starting with release v30.1.0.

## Overview

GPU-accelerated computing can significantly enhance performance for specific workloads like machine learning, video processing, scientific simulations, and other compute-intensive tasks. Giant Swarm's CAPI workload clusters support GPU nodes on AWS (CAPA) and Azure (CAPZ).

## Prerequisites

- A running CAPI workload cluster
- `kubectl` configured to access your workload cluster

## Supported cloud providers and GPU types

### AWS

Giant Swarm CAPI clusters on AWS support the following GPU instance types:

- `p2` family: Cost-effective GPU instances with NVIDIA K80 GPUs
- `p3` family: High-performance instances with NVIDIA V100 GPUs
- `p4` family: Latest generation with NVIDIA A100 GPUs
- `p5` family: Advanced performance with NVIDIA H100 GPUs
- `p5e` family: Enhanced performance with NVIDIA H200 GPUs
- `g3` family: Graphics-optimized with NVIDIA Tesla M60 GPUs
- `g4dn` family: Balanced GPU compute with NVIDIA T4 GPUs
- `g5` family: Latest generation graphics-optimized with NVIDIA A10G GPUs
- `g6` family: Next-generation GPU instances with NVIDIA L4 GPUs
- `g6e` family: Enhanced performance with NVIDIA L40S Tensor Core GPUs

### Azure

Giant Swarm CAPI clusters on Azure support the following GPU VM families and series:

#### NC-family (Compute-intensive, Graphics-intensive)
- `NC` series: NVIDIA K80 GPUs
- `NCv2` series and `NCv3` series: NVIDIA P100 and V100 GPUs
- `NCasT4_v3` series: NVIDIA T4 GPUs
- `NC_A100_v4` series: NVIDIA A100 GPUs
- `NCads_H100_v5` series and `NCCads_H100_v5` series: NVIDIA H100 GPUs

#### ND-family (Large memory compute-intensive workloads)
- `ND_A100_v4` series and `NDm_A100_v4` series: NVIDIA A100 GPUs
- `ND-H100-v5` series: NVIDIA H100 GPUs

#### NV-family (Visualization and rendering)
- `NV` series: NVIDIA M60 GPUs
- `NVv3` series: NVIDIA Tesla M60 GPUs
- `NVadsA10_v5` series: NVIDIA A10 GPUs

## Adding GPU nodes to your CAPI workload cluster

### Configuring a GPU-enabled machine deployment

To add GPU nodes to your CAPI workload cluster, you need to create a new node pool with the appropriate GPU instance type. The following example shows how to add GPU nodes to an AWS (CAPA) workload cluster.

1. Update your cluster app's values to add a new node pool with GPU instances:

```yaml
nodePools:
  gpu-worker-pool-1:
    # instance type with GPU
    instanceType: g5.2xlarge
    maxSize: 1
    minSize: 1
    # root volume size in GB needs to be at least 15
    rootVolumeSizeGB: 15
    instanceWarmup: 600
    minHealthyPercentage: 90
    # taints which are required for GPU workloads
    customNodeTaints:
    - key: "nvidia.com/gpu"
      value: "Exists"
      effect: "NoSchedule"
```

2. Apply the updated configuration to your cluster.

### Installing the NVIDIA GPU Operator

The recommended way to enable NVIDIA GPU support in your cluster is to use the NVIDIA GPU Operator, which is needed for scheduling and running GPU workloads.

2. Install the NVIDIA GPU Operator from the Giant Swarm Catalog in the `kube-system` namespace.

The GPU Operator installs several components:
- NVIDIA Device Plugin
- NVIDIA MIG Manager (for A100 GPUs)
- Node Feature Discovery
- GPU Feature Discovery

We don't install the NVIDIA driver and toolkit by the GPU Operator, because it's already provided by default.

### Verifying the installation

To verify that the GPU operator is installed and works correctly and wait for all the pods to be running:

```bash
gpu-feature-discovery-tjj65                                          0/1     Init:0/2    0          6s
gpu-operator-6d5b78c78f-f7dg8                                        0/1     Running     0          15s
gpu-operator-node-feature-discovery-gc-554ccf9b5-vzwd2               1/1     Running     0          15s
gpu-operator-node-feature-discovery-master-567bf66c77-xvsbz          1/1     Running     0          15s
gpu-operator-node-feature-discovery-worker-2lhks                     1/1     Running     0          15s
gpu-operator-node-feature-discovery-worker-jp7dm                     1/1     Running     0          15s
gpu-operator-node-feature-discovery-worker-mvq4t                     1/1     Running     0          15s
gpu-operator-node-feature-discovery-worker-pxtxq                     1/1     Running     0          15s
gpu-operator-node-feature-discovery-worker-s5zr6                     1/1     Running     0          15s
gpu-operator-node-feature-discovery-worker-xfbl7                     1/1     Running     0          15s
nvidia-dcgm-exporter-6l8vx                                           0/1     Init:0/1    0          6s
nvidia-device-plugin-daemonset-rr49p                                 0/1     Init:0/1    0          6s
nvidia-operator-validator-vjhxh                                      0/1     Init:0/4    0          7s
```

## Running GPU workloads

To run workloads on GPU nodes, you need to request GPU resources and the runtimeClassName `nvidia` needs to be specified in your pod specification:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-vector-add
  namespace: kube-system
spec:
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
  # runtimeClassName is required to run GPU workloads
  runtimeClassName: nvidia
  restartPolicy: OnFailure
  containers:
    - name: cuda-vector-add
      image: "nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04"
      resources:
        limits:
          nvidia.com/gpu: 1 # Requesting 1 GPU
```

### Resource management

GPUs are only available through limits, not requests. The number specified in limits determines how many GPUs will be allocated to the pod.

## Best practices

1. **Taints and tolerations**: Use taints on GPU nodes to prevent non-GPU workloads from being scheduled on expensive GPU resources.

2. **Resource quotas**: Implement resource quotas to control GPU allocation in multi-tenant environments.

3. **Node auto-provisioning**: Consider using cluster autoscaling or Karpenter with GPU node pools to automatically scale GPU resources based on demand.

### Getting support

If you encounter issues that cannot be resolved using the troubleshooting steps above, contact Giant Swarm support with the following information:

- Output of `kubectl get nodes -o wide`
- Output of `kubectl describe node <gpu-node-name>`
- Logs from the GPU Operator pods: `kubectl logs -n kube-system gpu-operator-<deployment-id>-<pod-id>`

## Limitations

- GPU memory overcommitment is not supported by default
- Dynamic allocation of GPUs is not supported (GPUs are allocated at container start time)
- Specific GPU driver versions may be required for certain CUDA applications

## Further reading

- [NVIDIA GPU Operator Documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/overview.html)
- [Kubernetes Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
- [NVIDIA Tesla Driver Documentation](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html) 
