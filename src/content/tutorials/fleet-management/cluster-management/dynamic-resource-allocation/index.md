---
linkTitle: Dynamic Resource Allocation
title: Set up Dynamic Resource Allocation (DRA) for GPU workloads
description: Learn how to configure Dynamic Resource Allocation (DRA) in Giant Swarm Cluster API workload clusters to enable advanced GPU resource management with Kubernetes native scheduling.
weight: 75
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-clusters-dra
owner:
  - https://github.com/orgs/giantswarm/teams/team-tenet
user_questions:
  - How do I set up Dynamic Resource Allocation (DRA) in my Giant Swarm cluster?
  - What is Dynamic Resource Allocation and how does it differ from traditional GPU scheduling?
  - How can I use DRA for GPU workloads in Kubernetes?
  - What are the prerequisites for enabling DRA in my workload cluster?
last_review_date: 2025-10-14
---

Dynamic Resource Allocation (DRA) is a Kubernetes feature that provides a more flexible and extensible way to request and allocate hardware resources like GPUs. Unlike traditional device plugins that only support simple counting of identical resources, DRA enables fine-grained resource selection based on device attributes and capabilities.

This tutorial explains how to set up DRA in Giant Swarm Cluster API workload clusters to enable advanced GPU resource management.

## Overview

Dynamic Resource Allocation offers several advantages over traditional device plugins:

- **Attribute-based selection**: Request specific GPU models, memory sizes, or other hardware attributes
- **Flexible resource sharing**: Support for time-slicing and multi-instance GPUs (MIG)
- **Better resource visibility**: Detailed information about available hardware resources
- **Future-proof architecture**: Extensible framework for new resource types

DRA is available as a beta feature in Kubernetes 1.31+ and requires specific driver installations for GPU support.

## Prerequisites

Before setting up DRA, ensure you have:

- A Giant Swarm Cluster API workload cluster running Kubernetes 1.33 or later
- `kubectl` configured to access your workload cluster
- Access to the Giant Swarm platform API for cluster configuration
- GPU nodes configured in your cluster (see [GPU workloads tutorial]({{< relref "/tutorials/fleet-management/cluster-management/gpu" >}}))

## Supported hardware and cloud providers

### GPU support

DRA for GPUs is supported on:

**AWS (CAPA clusters)**:

- All GPU instance types supported by Giant Swarm (p2, p3, p4, p5, g3, g4dn, g5, g6 families)
- Requires NVIDIA DRA driver installation

**Note**: Talk to us if you need it on Azure.

## Enable DRA in your cluster

### Step 1: Enable the DRA feature gate

DRA requires the `DynamicResourceAllocation` feature gate to be enabled in your cluster (previous to 1.34 release). Update your cluster configuration to include this feature gate.

For Cluster API clusters, add the following to your cluster app values:

```yaml
    cluster:
      internal:
        advancedConfiguration:
          controlPlane:
            apiServer:
              featureGates:
              - name: DynamicResourceAllocation
                enabled: true
            controllerManager:
              featureGates:
              - name: DynamicResourceAllocation
                enabled: true
            scheduler:
              featureGates:
              - name: DynamicResourceAllocation
                enabled: true
          kubelet:
            featureGates:
            - name: DynamicResourceAllocation
              enabled: true
```

Apply the updated configuration and wait for the cluster to be updated.

### Step 2: Configure GPU nodes with DRA labels

When creating GPU node pools, add specific a taint to disable common workloads to run in GPU instances:

```yaml
nodePools:
  gpu-dra-pool:
    instanceType: g4dn.4xlarge
    minSize: 1
    maxSize: 3
    rootVolumeSizeGB: 50
    customNodeTaints:
    - key: "nvidia.com/gpu"
      value: "Exists"
      effect: "NoSchedule"
```

**Note**: Make sure the root volume is bigger than 15GB to have space for drivers.

## Install DRA drivers

### NVIDIA GPU DRA driver

Install the NVIDIA DRA driver using Helm:

1. Add the NVIDIA Helm repository:

```bash
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update
```

1. Install the NVIDIA DRA driver:

```bash
helm install nvidia-dra-driver-gpu nvidia/nvidia-dra-driver-gpu \
  --version="25.3.2" \
  --namespace kube-system \
  --set kubeletPlugin.tolerations[0].key="nvidia.com/gpu" \
  --set kubeletPlugin.tolerations[0].operator="Exists" \
  --set kubeletPlugin.tolerations[0].effect="NoSchedule" \
  --set resources.gpus.enabled=false
```

## Verify DRA setup

### Check DRA driver pods

Verify that the DRA driver pods are running:

```bash
kubectl get pods -n kube-system -l app.kubernetes.io/name=nvidia-dra-driver-gpu
```

Expected output:

```text
NAME                                         READY   STATUS    RESTARTS   AGE
nvidia-dra-driver-gpu-kubelet-plugin-52cdm   1/1     Running   0          46s
```

### Verify ResourceSlice objects

Confirm that ResourceSlice objects are created and list your hardware devices:

```bash
kubectl get resourceslices -o yaml
```

For GPU nodes, you should see output similar to:

```yaml
apiVersion: resource.k8s.io/v1beta1
kind: ResourceSlice
metadata:
  name: example-gpu-slice
spec:
  devices:
  - basic:
      attributes:
        architecture:
          string: Ampere
        brand:
          string: Nvidia
        productName:
          string: NVIDIA Tesla 4
        type:
          string: gpu
        uuid:
          string: GPU-4d403095-4294-6ddd-66fd-cfe5778ef56e
      capacity:
        memory:
          value: 15360Mi
    name: gpu-0
  driver: gpu.nvidia.com
  nodeName: ip-100-12-233-34.eu-west-2.compute.internal
```

## Deploy workloads with DRA

### Basic GPU workload with DRA

Create a pod that uses DRA to request GPU resources:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dra-gpu-workload
spec:
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
  runtimeClassName: nvidia
  restartPolicy: OnFailure
  resourceClaims:
  - name: gpu-claim
    resourceClaimTemplateName: gpu-template
  containers:
  - name: cuda-container
    image: "gsoci.azurecr.io/giantswarm/gpu-operator-validator:v25.3.2"
    resources:
      claims:
      - name: gpu-claim
---
apiVersion: resource.k8s.io/v1beta1
kind: ResourceClaimTemplate
metadata:
  name: gpu-template
spec:
  spec:
    devices:
      requests:
      - name: gpu
        deviceClassName: gpu.nvidia.com
        selectors:
        - cel:
            expression: 'device.attributes["type"].string == "gpu"'
```

### Advanced GPU selection with attributes

Request specific GPU models or memory requirements:

```yaml
apiVersion: resource.k8s.io/v1beta1
kind: ResourceClaimTemplate
metadata:
  name: specific-gpu-template
spec:
  spec:
    devices:
      requests:
      - name: high-memory-gpu
        deviceClassName: gpu.nvidia.com
        selectors:
        - cel:
            expression: |
              device.attributes["productName"].string == "NVIDIA A100" &&
              device.capacity["memory"].quantity >= quantity("40Gi")
```

## Troubleshooting

### Common issues

1. **DRA driver pods not starting**: Check that the feature gate is enabled and nodes have the correct labels.

2. **ResourceSlice objects not created**: Verify that the DRA controller a kubelet plugins to ensure there are no errors. Contact Giant Swarm support if it is the case.

3. **Workloads not scheduling**: Ensure that:
   - ResourceClaimTemplate selectors match available devices
   - Pods have appropriate tolerations for GPU nodes
   - The correct runtime class is specified

## Limitations and considerations

- DRA is currently in beta and may have API changes in future Kubernetes versions
- Not all GPU features are immediately available through DRA drivers
- Performance overhead compared to traditional device plugins is minimal but measurable
- DRA requires Giant Swarm release 1.33+

## Next steps

- Learn about [GPU workloads]({{< relref "/tutorials/fleet-management/cluster-management/gpu" >}}) for traditional GPU scheduling
- Explore [cluster autoscaling]({{< relref "/tutorials/fleet-management/cluster-management/cluster-autoscaler" >}}) for dynamic GPU node provisioning

## Further reading

- [Kubernetes Dynamic Resource Allocation KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/3063-dynamic-resource-allocation)
- [NVIDIA DRA Driver Documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)
- [Kubernetes Device Plugin vs DRA Comparison](https://kubernetes.io/blog/2023/08/15/dynamic-resource-allocation/)
