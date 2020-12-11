---
title: Preparing a Kubernetes cluster for the use of GPUs
description: Here we explain how to make the GPU driver for CoreOS available so that workloads can use GPUs.
type: page
weight: 150
tags: ["recipe"]
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# Preparing a Kubernetes cluster for the use of GPUs

In order to have GPU instances running Flatcar we need to follow these steps to install and configure the right libraries and drivers on the host machine.

## Requirements

- Your cluster must have running GPU instances (`p2` or `p3` families in AWS, `NC` or `NCs` families on Azure).
- Your cluster must be running a supported Giant Swarm tenant cluster release:
    - `9.0.5` on AWS with Kubernetes `1.15.11`
    - `11.3.0` on AWS with Kubernetes `1.16.9`
    - `13.0.0` on Azure with kubernetes `1.18.12`

## Installing

You need to install the `kubernetes-gpu-app` application, available in the `Giant Swarm Playground`.

If you want to use `helm` directly, you can install the `kubernetes-gpu-app` chart directly:

```bash
helm install helm/kubernetes-gpu-app
```

## Configuration

Based on the `CUDA` version you need, there are different driver versions to choose from:

| Driver Version | Chart Version (X.Y.Z) | CUDA compatible Version|
|--------|---------|------------|
|440.82|440.82.00|10.2|
|390.116|390.116.00|9.1|

## Nvidia GPU drivers

The idea here it is run a pod in every worker node to download, compile and install the Nvidia drivers on Flatcar/CoreOS. It is a fork from [Shelman Group](https://github.com/shelmangroup/coreos-gpu-installer) but adding the pod security policy needed to work in hardened clusters.

It will create a daemon set which runs a bunch of different commands by node. At the end, it displays a successful message in case there is not trouble found.

```bash
$ kubectl logs -f -l app.kubernetes.io/name=kubernetes-gpu-app -c nvidia-driver-installer
...
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 390.116                 Driver Version: 390.116                  |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:00:1E.0 Off |                    0 |
| N/A   47C    P0    43W / 300W |      0MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
Finished installing the drivers.
Updating host's ld cache
```

## Installing the device plugin

Instead of the official Nvidia device plugin, which requires a custom docker runtime, we choose to use Google's approach. In short, this device plugin expects that all the Nvidia libraries needed by the containers are present under a single directory on the host (`/opt/nvidia`).

Same as before we deploy a daemon set in the cluster which will mount the `/dev` host path and the `/var/lib/kubelet/device-plugin` path to make available the GPU device to pods that request it. Pointing out the we passed a flag to the container to indicate where the Nvidia libraries and binaries has been installed in our host.

```bash
kubectl logs -f -l app.kubernetes.io/name=kubernetes-gpu-app
```

When everything has gone as expected you should see some logs like

```nohighlight
device-plugin started
Found Nvidia GPU "nvidia0"
will use alpha API
starting device-plugin server at: /device-plugin/nvidiaGPU-1544782516.sock
device-plugin server started serving
falling back to v1beta1 API
device-plugin registered with the kubelet
device-plugin: ListAndWatch start
ListAndWatch: send devices &ListAndWatchResponse{Devices:[&Device{ID:nvidia0,Health:Healthy,}],}
```

## Considerations

Depend how your application make use of Nvidia driver you may need to mount the proper volume.

```yaml
  volumes:
  - name: nvidia-libs
    hostPath:
      path: /opt/nvidia/lib64
      type: Directory```
  containers:
    ...
    volumeMounts:
    - mountPath: /opt/nvidia/lib64
      name: nvidia-libs
```

Extend shared library to contain the nvidia directory

```yaml
    env:
    - name: LD_LIBRARY_PATH
      value: $LD_LIBRARY_PATH:/opt/nvidia/lib64
```

Taking into account that default Pod Security Policy in the tenant clusters, `restricted`, does not
allow mount host paths. You will need to extend:

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: your-psp-name
spec:
  ...
  volumes:
  - hostPath
```

## Verification

To run a test we are going to use a [cuda vecadd example](https://github.com/giantswarm/kubernetes-gpu/blob/master/demo-pod/vecadd.cu). It performs a simple vector addition using the device plugin installed before.

```bash
kubectl apply -f https://raw.githubusercontent.com/giantswarm/kubernetes-gpu/master/demo-pod/test-pod.yaml
```

If we inspect the logs, we should be able to see something like

```bash
$ kubectl  logs -f cuda-vector-add
Begin
Allocating device memory on host..
Copying to device..
Doing GPU Vector add
Doing CPU Vector add
10000000 0.000007 0.046845
```

Now you have successfully installed everything needed to run GPU workloads over your Kubernetes cluster.

## Development

Once you want to add a new driver version please follow these steps:

- Check the latest driver versions in [official web](https://www.nvidia.com/en-us/drivers/unix/).

- Run update version script which replaces all driver version appearances with new value.

`/update_driver_version.sh 390.116`

- Make a PR to the repo and tag your commit following the semver. To align it with driver version which  has `X.Y` format (like `390.116`) let's add an extra `.0` so we follow our container image tag convention and let our automation to build the image properly.

Example:

```nohighlight
git tag -a "390.116.00" -m "390.116.00"
git push --tags
```

## Credit

- [shelmangroup/coreos-gpu-installer](https://github.com/shelmangroup/coreos-gpu-installer) provided most of the functionality here.
