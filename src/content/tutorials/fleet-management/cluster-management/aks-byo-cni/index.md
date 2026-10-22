---
title: Run Giant Swarm's Cilium on AKS with BYO CNI
diataxis_content_type: how-to-guide
linkTitle: AKS BYO CNI
description: Create an AKS workload cluster that runs Giant Swarm's Cilium instead of AKS-managed networking, and learn when to choose it.
weight: 20
menu:
  principal:
    identifier: tutorials-fleet-management-clusters-aks-byo-cni
    parent: tutorials-fleet-management-clusters
last_review_date: 2026-10-22
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How can I run Giant Swarm's Cilium on AKS?
  - How do I use FQDN network policies on AKS without ACNS?
  - What is BYO CNI on AKS?
---

By default, AKS workload clusters use AKS-managed networking (Azure CNI powered by Cilium). Microsoft decides the Cilium version and configuration, and supports the pod network. A new cluster can instead use [BYO CNI](https://learn.microsoft.com/azure/aks/use-byo-cni): AKS installs no CNI, and the cluster runs [Giant Swarm's Cilium]({{< relref "/overview/connectivity/cni" >}}), as on our other providers. Giant Swarm then supports the pod network.

BYO CNI requires AKS release v36.2.0 or newer.

## When to choose BYO CNI

Choose BYO CNI if you need:

- Giant Swarm's Cilium version and configuration, including BPF map sizes and identity label exclusion, which you can tune per cluster;
- FQDN and L7 network policies through Cilium's in-agent DNS proxy, without Advanced Container Networking Services (ACNS);
- the same Cilium monitoring and Hubble as on our other providers.

Keep AKS-managed networking if you need:

- ACNS;
- Application Gateway for Containers;
- Microsoft's support for the pod network;
- pod IPs reachable from your VNet, peered or on-premises networks;
- Windows node pools.

## Constraints

- **New clusters only.** AKS can't change the network plugin of a running cluster, so existing clusters can't move into or out of BYO CNI.
- **Overlay pod IPs.** Pods get IPs from the cluster's pod CIDR on a VXLAN overlay. They aren't reachable from the VNet, peered or on-premises networks except through Services, and their egress is SNATed to the node IP. Pods don't use VNet IPs.
- **One pod CIDR.** Give exactly one pod CIDR block. It must not overlap the VNet, peered or on-premises networks, the service CIDR or the [AKS reserved ranges](https://learn.microsoft.com/azure/aks/use-byo-cni).
- **No Windows node pools** and **no API server VNet integration.**
- **kube-proxy stays.** AKS keeps running kube-proxy (iptables mode), and Cilium runs without kube-proxy replacement. Cilium features that need kube-proxy replacement aren't available, such as eBPF host routing, Cilium Ingress and Gateway API, egress gateway, DSR and Maglev load balancing. Giant Swarm's Gateway API offering is based on Envoy Gateway and isn't affected.
- **Webhooks behind a default deny.** The API server reaches pods through the Konnectivity agent, which runs on the node network. If an admission webhook is behind a default-deny network policy, allow ingress from the `host` and `remote-node` Cilium entities on the webhook port. The webhooks Giant Swarm ships already do this.

## Support boundary

| Area | Supported by |
|---|---|
| AKS control plane and API server, Konnectivity, node VMs and node images, kube-proxy | Microsoft |
| Pod network, Cilium, Hubble, network policies | Giant Swarm |

Microsoft [doesn't support CNI issues](https://learn.microsoft.com/azure/aks/use-byo-cni) on BYO CNI clusters. Contact Giant Swarm for pod networking problems. For problems on the path from the API server to pods, such as webhooks or `kubectl logs`, Giant Swarm checks the pod network first and works with Microsoft when the cause is on the AKS side.

## Create an AKS cluster with BYO CNI

Set `global.connectivity.cni.managed` to `true` in the cluster's user values, and give one pod CIDR block:

{{< highlight yaml "hl_lines=6-12" >}}
apiVersion: v1
kind: ConfigMap
data:
  values: |
    global:
      connectivity:
        cni:
          managed: true
        network:
          pods:
            cidrBlocks:
              - 192.168.0.0/16
      metadata:
        name: mycluster
        organization: testing
      # [...]
metadata:
  name: mycluster-userconfig
  namespace: org-testing
{{< / highlight >}}

The rest of the cluster configuration stays as for any [AKS cluster](https://github.com/giantswarm/cluster-aks). With BYO CNI, `global.controlPlane.networking.networkDataplane`, `networkMode` and `networkPolicy` are ignored.

Once the cluster is created, the nodes become `Ready` after Cilium starts, and apps that need the pod network wait for it. Check that pods get IPs from the pod CIDR:

```sh
kubectl get pods -A -o wide
```

To tune Cilium for the cluster, set `global.apps.cilium.values`, as on other providers. See the [cluster-aks README](https://github.com/giantswarm/cluster-aks#byo-cni-opt-in) for the reference.
