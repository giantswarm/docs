---
title: Accelerated Networking on Azure
description: A general description of the Accelerated Networking for Azure VMs feature and how it works on Giant Swarm clusters.
date: 2020-10-02
weight: 120
type: page
categories: ["basics"]
---

# Accelerated Networking on Azure

## Synopsis

`Accelerated Networking` (or `AN` for short) is a feature provided by the `Azure Cloud` that allows for
«ultra-low network latency» thanks to Azure's in-house programmable hardware and technologies like [SR-IOV](https://docs.microsoft.com/en-us/windows-hardware/drivers/network/overview-of-single-root-i-o-virtualization--sr-iov-).

![Accelerated Networking](/img/accelerated_networking.png)

As shown in the drawing, when `AN` is enabled on a virtual machine the Host server's virtual network is not in use:
network traffic flows directly from the virtual machine to the physical network card.

## Benefits

As mentioned in [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli),
the key benefits of Accelerated Networking are:

- **Lower Latency / Higher packets per second (pps)**: Removing the virtual switch from the datapath removes the time packets spend in the host for policy processing and increases the number of packets that can be processed inside the VM.
- **Reduced jitter**: Virtual switch processing depends on the amount of policy that needs to be applied, and the workload of the CPU that is doing the processing. Offloading the policy enforcement to the hardware removes that variability by delivering packets directly to the VM, removing the host to VM communication and all software interrupts and context switches.
- **Decreased CPU utilization**: Bypassing the virtual switch in the host leads to less CPU utilization for processing network traffic.

Furthermore, accelerated networking feature is available free of charge for many (but not all) Virtual Machine types.

## Support in Giant Swarm Clusters

As of release v{{% first_azure_accelerated_networking_version %}}, `Accelerated Networking` is enabled by default
on all `Node Pools` that have a Virtual Machine type that support the feature, so there is nothing you need to do
in order to leverage the benefits of `AN`.

# Caveats

Please note that, once the node pool gets created for the first time, the `AN` feature is either enabled or disabled
according to the Virtual Machine type.
After that point, it is not possible to change the `AN` setting any more.

This means that if you create a Node Pool with an instance type that does not support accelerated networking, 
changing the instance type of that node pool to one that does will not enable `AN` on that node pool.
Alternatively, you can create a new node pool and delete the old one.

## Further reading

[Maximize your VM’s Performance with Accelerated Networking – now generally available for both Windows and Linux](https://azure.microsoft.com/en-us/blog/maximize-your-vm-s-performance-with-accelerated-networking-now-generally-available-for-both-windows-and-linux/)
[https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli)
