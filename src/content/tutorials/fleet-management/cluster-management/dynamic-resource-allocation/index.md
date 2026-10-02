---
linkTitle: Dynamic Resource Allocation
title: Set up Dynamic Resource Allocation (DRA) for GPU workloads
diataxis_content_type: how-to-guide
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
  - Which NVIDIA driver version does the DRA driver need?
  - Why are no ResourceSlice objects appearing in my cluster?
  - How do I share one GPU between several workloads with DRA?
  - How do I use time-slicing, MPS or MIG with the NVIDIA DRA driver?
last_review_date: 2026-09-28
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

- GPU instance types supported by Giant Swarm (p3, p4, p5, g4dn, g5, g6 families)
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
    rootVolumeSizeGB: 100
    customNodeTaints:
    - key: "nvidia.com/gpu"
      value: "Exists"
      effect: "NoSchedule"
```

**Note**: Give the root volume at least 100 GB. It holds the NVIDIA driver built at first boot and the container images. CUDA images alone are several gigabytes each.

## Install DRA drivers

### NVIDIA GPU DRA driver

Giant Swarm publishes [`dra-driver-nvidia-gpu`](https://github.com/giantswarm/dra-driver-nvidia-gpu), a downstream build of the upstream NVIDIA DRA driver. Install it from the `giantswarm` catalog.

The chart version follows its own Giant Swarm line and is different from the upstream version it packages: chart `26.0.0` ships upstream `0.5.0`.

1. Create the configuration values:

```bash
cat > dra-values.yaml <<EOF
# Publish GPUs as DRA devices. The chart refuses this unless the override below
# is also set, because the DRA driver and the standard NVIDIA device plugin must
# not both manage GPUs on the same node until KEP 5004 is generally available.
gpuResourcesEnabledOverride: true
resources:
  # Compute domains need the nvidia-caps-imex-channels character device, which
  # only exists on NVLink-fabric hardware. Leave this disabled on g4dn, g5 and
  # g6 nodes, where the container otherwise crashes at startup.
  computeDomains:
    enabled: false
EOF
```

1. Create a configmap with the values in the organization namespace:

```bash
kubectl create configmap dra-driver-nvidia-gpu-user-values \
  --from-file=values=dra-values.yaml \
  --namespace=org-ORGANIZATION
```

1. Install the DRA driver:

```bash
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=CLUSTER_NAME \
  --organization=ORGANIZATION \
  --name=dra-driver-nvidia-gpu \
  --app-name=dra-driver-nvidia-gpu \
  --user-configmap=dra-driver-nvidia-gpu-user-values \
  --target-namespace=kube-system \
  --version=26.0.0 > dra-driver.yaml

kubectl apply -f dra-driver.yaml
```

**Note**: If the NVIDIA GPU Operator runs on the same cluster, disable its device plugin (`devicePlugin.enabled: false`) on the nodes where the DRA driver publishes GPUs. Both components managing the same GPUs isn't supported.

## Verify DRA setup

### Check DRA driver pods

Verify that the DRA driver pods are running:

```bash
kubectl get pods -n kube-system -l app.kubernetes.io/name=dra-driver-nvidia-gpu
```

Expected output:

```text
NAME                                         READY   STATUS    RESTARTS   AGE
dra-driver-nvidia-gpu-kubelet-plugin-52cdm   1/1     Running   0          46s
```

If no pod is listed at all, the DaemonSet has selected no nodes. Its affinity relies on node feature labels published by node feature discovery. Label the GPU node explicitly to force the deployment:

```bash
kubectl label node GPU_NODE nvidia.com/gpu.present=true --overwrite
```

### Verify ResourceSlice objects

Confirm that ResourceSlice objects are created and list your hardware devices:

```bash
kubectl get resourceslices -o yaml
```

For GPU nodes, you should see output similar to:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: example-gpu-slice
spec:
  devices:
  - attributes:
      architecture:
        string: Ampere
      brand:
        string: Nvidia
      cudaComputeCapability:
        version: 8.6.0
      cudaDriverVersion:
        version: 12.8.0
      driverVersion:
        version: 570.195.3
      productName:
        string: NVIDIA A10G
      type:
        string: gpu
      uuid:
        string: GPU-c8f2b23e-824f-5f24-57c8-f0a1c637b357
    capacity:
      memory:
        value: 23028Mi
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
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: gpu-template
spec:
  spec:
    devices:
      requests:
      - name: gpu
        exactly:
          deviceClassName: gpu.nvidia.com
```

Each claim is satisfied by exactly one GPU, and a GPU already allocated to one pod isn't offered to another. If more pods request GPUs than the node has, the extra pods stay `Pending` with `cannot allocate all claims` rather than sharing a device.

### Advanced GPU selection with attributes

Request specific GPU models or memory requirements:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: specific-gpu-template
spec:
  spec:
    devices:
      requests:
      - name: high-memory-gpu
        exactly:
          deviceClassName: gpu.nvidia.com
          selectors:
          - cel:
              expression: |
                device.attributes["productName"].string == "NVIDIA A100" &&
                device.capacity["memory"].quantity >= quantity("40Gi")
```

## Share GPUs between workloads

By default each claim gets exclusive use of a whole GPU. The DRA driver also supports three ways of
sharing one physical GPU between workloads: time-slicing, MPS and MIG.

Sharing happens when several containers reference the **same** claim. The examples below put two
containers in one pod. To share across pods, create a standalone `ResourceClaim` instead of a
`ResourceClaimTemplate` and reference it from each pod with `resourceClaimName`.

**Time-slicing and MPS are alpha features and turned off by default.** Enable the matching feature gate
in the chart values, otherwise the driver rejects any `sharing` block with
`invalid GPU sharing settings`:

```yaml
featureGates:
  TimeSlicingSettings: true   # for time-slicing
  MPSSupport: true            # for MPS
```

{{< tabs >}}
{{< tab title="Time-slicing">}}

Time-slicing lets several workloads take turns on the same GPU. The GPU context-switches between
them, so each sees the full device but gets a share of its time. There's no memory isolation
between the workloads.

Requires the `TimeSlicingSettings` feature gate. `interval` accepts `Default`, `Short`, `Medium`
or `Long`.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: rct-timeslicing-gpu
spec:
  spec:
    devices:
      requests:
      - name: gpu
        exactly:
          deviceClassName: gpu.nvidia.com
      config:
      - requests: ["gpu"]
        opaque:
          driver: gpu.nvidia.com
          parameters:
            apiVersion: resource.nvidia.com/v1beta1
            kind: GpuConfig
            sharing:
              strategy: TimeSlicing
              timeSlicingConfig:
                interval: Short
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-timeslicing
spec:
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
  containers:
  - name: ctr0
    image: ubuntu:24.04
    command: ["bash", "-c"]
    args: ["nvidia-smi -L; sleep 9999"]
    resources:
      claims:
      - name: gpu
  - name: ctr1
    image: ubuntu:24.04
    command: ["bash", "-c"]
    args: ["nvidia-smi -L; sleep 9999"]
    resources:
      claims:
      - name: gpu
  resourceClaims:
  - name: gpu
    resourceClaimTemplateName: rct-timeslicing-gpu
```

Both containers report the same GPU from `nvidia-smi -L`.

{{< /tab >}}
{{< tab title="MPS">}}

Multi-Process Service (MPS) runs the workloads' CUDA contexts concurrently through a single GPU
context instead of context-switching between them. That avoids time-slicing's switching overhead and
lets you cap each workload's share of threads and memory.

Requires the `MPSSupport` feature gate.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: rct-mps-gpu
spec:
  spec:
    devices:
      requests:
      - name: gpu
        exactly:
          deviceClassName: gpu.nvidia.com
      config:
      - requests: ["gpu"]
        opaque:
          driver: gpu.nvidia.com
          parameters:
            apiVersion: resource.nvidia.com/v1beta1
            kind: GpuConfig
            sharing:
              strategy: MPS
              mpsConfig:
                defaultActiveThreadPercentage: 50
                defaultPinnedDeviceMemoryLimit: 10Gi
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-mps
spec:
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
  containers:
  - name: ctr0
    image: ubuntu:24.04
    command: ["bash", "-c"]
    args: ["nvidia-smi -L; sleep 9999"]
    resources:
      claims:
      - name: gpu
  - name: ctr1
    image: ubuntu:24.04
    command: ["bash", "-c"]
    args: ["nvidia-smi -L; sleep 9999"]
    resources:
      claims:
      - name: gpu
  resourceClaims:
  - name: gpu
    resourceClaimTemplateName: rct-mps-gpu
```

`mpsConfig` also accepts `defaultPerDevicePinnedMemoryLimit` for per-device limits and `multiUser`.

{{< /tab >}}
{{< tab title="MIG">}}

Multi-Instance GPU (MIG) partitions a physical GPU into hardware-isolated instances, each with its
own memory and compute slices. Unlike time-slicing and MPS, MIG gives real isolation between
workloads.

MIG needs hardware that supports it on AWS: the A100 and H100 families (`p4`, `p5`). It isn't
available on `g4dn`, `g5` or `g6`.

The GPU must already be in MIG mode with its partitions created, for example by the NVIDIA GPU
Operator's MIG manager. The DRA driver then discovers the existing instances and publishes them in
the separate `mig.nvidia.com` device class. This needs no feature gate.

Request any available instance:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: rct-anymig
spec:
  spec:
    devices:
      requests:
      - name: anymig
        exactly:
          deviceClassName: mig.nvidia.com
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-anymig
spec:
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
  containers:
  - name: ctr
    image: ubuntu:24.04
    command: ["bash", "-c"]
    args: ["nvidia-smi -L; sleep 9999"]
    resources:
      claims:
      - name: migdev
  resourceClaims:
  - name: migdev
    resourceClaimTemplateName: rct-anymig
```

Or select an instance by capacity rather than by profile name:

```yaml
      requests:
      - name: mig1g
        exactly:
          deviceClassName: mig.nvidia.com
          selectors:
          - cel:
              expression: |
                device.capacity['gpu.nvidia.com'].multiprocessors.isGreaterThan(quantity("10"))
                &&
                device.capacity['gpu.nvidia.com'].memory.isGreaterThan(quantity("10Gi"))
```

Having the driver create and reshape MIG partitions on demand is a separate alpha feature
(`DynamicMIG`), which is mutually exclusive with `MPSSupport`.

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

### Common issues

1. **kubelet plugin stuck in `Init:0/1`**: The node runs an NVIDIA driver older than 570, which means a release predating the node image that defaults to 570. Check the init container log for `Option --version is not recognized` and see [NVIDIA driver requirement](#nvidia-driver-requirement).

2. **No DRA driver pods at all**: The DaemonSet selected no nodes. Label the GPU node with `nvidia.com/gpu.present=true` as described earlier.

3. **Pods running but no ResourceSlice objects**: The kubelet plugin registers with kubelet but can't reach the API server. Check its log for `dial tcp <apiserver>:443: i/o timeout`. Chart `26.0.0` and later ship the required network policies by default. Earlier versions don't, so on a cluster with a default-deny policy the plugin publishes nothing and logs no error.

4. **`invalid GPU sharing settings`**: A claim asks for time-slicing or MPS while the matching feature gate is off. Enable `TimeSlicingSettings` or `MPSSupport` in the chart values. See [Share GPUs between workloads](#share-gpus-between-workloads).

5. **Workloads not scheduling**: Ensure that:
   - ResourceClaimTemplate selectors match available devices
   - Pods have appropriate tolerations for GPU nodes
   - The node has a free GPU, since an allocated device isn't shared between claims

## Limitations and considerations

- DRA is currently in beta and may have API changes in future Kubernetes versions
- Not all GPU features are immediately available through DRA drivers
- Performance overhead compared to traditional device plugins is minimal but measurable
- DRA requires Giant Swarm release 1.33+
- Chart `26.0.0` requires NVIDIA driver 570 or newer on GPU nodes
- The DRA driver can't run alongside the NVIDIA device plugin on the same node
- Compute domains require NVLink-fabric hardware and must be turned off otherwise
- Time-slicing and MPS are alpha features, turned off by default, and provide no memory isolation between workloads
- MIG requires A100 or H100 class hardware and partitions created outside the DRA driver

## Next steps

- Learn about [GPU workloads]({{< relref "/tutorials/fleet-management/cluster-management/gpu" >}}) for traditional GPU scheduling
- Explore [cluster autoscaling]({{< relref "/tutorials/fleet-management/cluster-management/cluster-autoscaler" >}}) for dynamic GPU node provisioning

## Further reading

- [Kubernetes Dynamic Resource Allocation KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/3063-dynamic-resource-allocation)
- [NVIDIA DRA Driver Documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)
- [Kubernetes Device Plugin vs DRA Comparison](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
