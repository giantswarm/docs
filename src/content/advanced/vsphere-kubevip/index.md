---
linkTitle: vSphere Kube-vip
title: vSphere networking with Kube-vip
description: Here we describe how to work with Kube-vip in Giant Swarm CAPV clusters.
weight: 25
menu:
  main:
    parent: advanced
last_review_date: 2023-10-09
user_questions:
  - How to divide my subnet for Kube-vip with CAPV?
  - What IP should I use for Kube-vip with CAPV?
  - How to set a range of IPs for load balancer in Kube-vip with CAPV?
  - Where can I see the IPs in use by Kube-vip?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

While most infrastructure providers offer a load balancer to use for the Kubernetes API and services of type Load Balancer (AWS, Azure, VMware Cloud Director...), vSphere is a bit different in that it is a hypervisor as opposed to a cloud provider. Advanced networking use cases such as routing, firewalling, load balancing and the likes are handled by VMware NSX which is sold as a separate product. In order to offer a highly-available Kubernetes API to customers without NSX, CAPV comes with `kube-vip`, a layer-2 load balancer.

In order to inform the network of the location of a new address, `kube-vip` relies on [gratuitous ARP requests](https://www.practicalnetworking.net/series/arp/gratuitous-arp/) (layer 2 protocol) to ensure the network understands the link between the hardware address (MAC) and the logical address (IP).

As a result of working on layer 2, `Kube-vip` uses IP addresses in the same subnet as the nodes themselves and these IP addresses must be selected carefully to avoid collisions. This is particularly plausible if multiple users collaborate on the same platform and select the same IP for different clusters for instance.

## IPAM controller

In order to mitigate this risk, Giant Swarm CAPV clusters run `cluster-api-ipam-provider-in-cluster` to track IP address usage from within the management cluster (MC). For that reason, **customers shouldn't run more than one management cluster per subnet**.

The basic operations of `cluster-api-ipam-provider-in-cluster` work as follows:

* Create a pool of IPs with a `globalinclusterippools` custom resource (CR).
* Claim an IP by referencing the pool in a `ipaddressclaims` CR.
* An `ipaddresses` CR is created and the `Free/Used` status of the `globalinclusterippools` CR is updated.

```nohighlight
$ kubectl get globalinclusterippools.ipam.cluster.x-k8s.io
NAME        ADDRESSES                         TOTAL   FREE   USED
wc-cp-ips   ["10.10.222.232-10.10.222.239"]   8       7      1

$ kubectl get ipaddressclaims.ipam.cluster.x-k8s.io -A
NAMESPACE        NAME    POOL NAME   POOL KIND
org-giantswarm   pssss   wc-cp-ips   GlobalInClusterIPPool

$ kubectl get ipaddresses.ipam.cluster.x-k8s.io -A
NAMESPACE        NAME    ADDRESS         POOL NAME   POOL KIND
org-giantswarm   pssss   10.10.222.233   wc-cp-ips   GlobalInClusterIPPool
```

You can find more details about how it works in this [blog post](https://kremser.dev/post/ipam-for-capv/).

## Dividing the subnet

Here we will talk about how to "divide" the subnet where you will be deploying your workload clusters (provided they will all be on the same subnet of course).

The main goal here is to avoid IP address collisions so we want the subnet to accomodate for:

* DHCP range for node interface.
* One IP for the management clusters' Kubernetes API for use by kube-vip.
* One IP for the management clusters' Ingress for use by kube-vip.
* Pool of IPs for workload clusters' Kubernetes API.
* Pool of IPs for workload clusters' Ingresses (untracked by IPAM controller).

Below is an example of what it could look like but you are free to adjust the ranges as you see fit:

![kube-vip range](capv-kubevip-ipam.png)

## Workload cluster IPs

### Control plane

When creating a CAPV workload cluster, you don't need to select an IP address for the control plane, you can leave the `host` field empty and specify a `globalinclusterippools` instead. If there are free IPs in the pool, the pre-install job will mutate the cluster with the claimed IP address.

```yaml
connectivity:
  network:
    controlPlaneEndpoint:
      host: ""
      ipPoolName: wc-cp-ips
      port: 6443
```

### Services of type Load Balancer

Giant Swarm clusters are deployed with the `Kube-vip` cloud provider interface (CPI), meaning you can use an IP address from the underlying layer 2 subnet for services of type Load Balancer. However, as mentioned previously, those are not tracked by the `cluster-api-ipam-provider-in-cluster` controller, hence the importance of properly dividing your subnet.

When deploying a CAPV workload cluster, specify a CIDR range to assign to the `Kube-vip` CPI in the workload cluster.

```yaml
    connectivity:
      loadBalancers:
        cidrBlocks:
        - "10.10.222.180/30"
```
