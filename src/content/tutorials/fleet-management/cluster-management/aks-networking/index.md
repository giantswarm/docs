---
title: Configure Azure CNI Overlay, ACNS and User Defined Routing on AKS
diataxis_content_type: how-to-guide
linkTitle: AKS networking options
description: Configure Azure CNI Overlay, Advanced Container Networking Services and User Defined Routing on an AKS workload cluster, and learn their constraints.
weight: 21
menu:
  principal:
    identifier: tutorials-fleet-management-clusters-aks-networking
    parent: tutorials-fleet-management-clusters
last_review_date: 2026-11-04
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I use Azure CNI Overlay on AKS?
  - How do I set the pod CIDR of an AKS cluster?
  - How do I enable Advanced Container Networking Services on AKS?
  - How do I send AKS egress traffic through my own firewall?
  - Can I change the outbound type of an existing AKS cluster?
---

AKS workload clusters use AKS-managed networking (Azure CNI powered by Cilium) by default. On top of it, you can choose:

- [Azure CNI Overlay](https://learn.microsoft.com/azure/aks/azure-cni-overlay), which gives pods IPs from a private pod CIDR instead of the VNet;
- [Advanced Container Networking Services](https://learn.microsoft.com/azure/aks/advanced-container-networking-services-overview) (ACNS), for network observability and FQDN or L7 network policies;
- User Defined Routing, to send the cluster's egress through your own firewall or network virtual appliance (NVA).

These options require AKS release v36.2.0 or newer. They apply to AKS-managed networking only. On clusters that run [Giant Swarm's Cilium with BYO CNI]({{< relref "/overview/connectivity/cni" >}}), the cluster chart rejects overlay and ACNS.

All settings go in the cluster's user values. See the [cluster-aks README](https://github.com/giantswarm/cluster-aks#azure-cni-overlay-and-acns) for the full reference.

## Use Azure CNI Overlay

Set `networkPluginMode` to `overlay` and give exactly one pod CIDR block:

```yaml
global:
  connectivity:
    network:
      pods:
        cidrBlocks:
          - 100.64.0.0/16
  controlPlane:
    networking:
      networkPluginMode: overlay
```

Before you create the cluster, check these constraints:

- **Creation-time choice.** You can't migrate an existing cluster from Azure CNI node subnet to overlay.
- **No overlaps.** The pod CIDR must not overlap the VNet, peered or on-premises networks, or the service CIDR.
- **AKS reserved ranges.** The pod CIDR, the service CIDR and the VNet must not overlap `169.254.0.0/16`, `172.30.0.0/16`, `172.31.0.0/16`, `192.0.2.0/24` or `224.0.0.0/4`. AKS rejects the cluster otherwise.
- **Pod IPs stay inside the cluster.** Pod egress is SNATed to the node IP, and pod IPs aren't routable outside the cluster. Allowlists on external systems must use node or subnet IPs.
- **Plugin settings.** Overlay requires `networkPlugin: azure` and doesn't support `networkMode: bridge`. The defaults already fit.

## Enable ACNS

ACNS has two features:

- **Observability** provides Hubble network metrics and flow logs.
- **Security** provides FQDN filtering, which is the default, or L7 network policies.

Enable ACNS and the features you need:

```yaml
global:
  controlPlane:
    networking:
      advancedNetworking:
        enabled: true
        observability:
          enabled: true
        security:
          enabled: true
          advancedNetworkPolicies: L7
```

Keep in mind:

- **Paid add-on.** ACNS is billed by Azure to the cluster's subscription.
- **Cilium dataplane.** Security requires `networkDataplane: cilium`, which is the default.
- **Explicit switch.** Observability and security need `enabled: true`. If you leave `enabled` unset, the cluster keeps its current ACNS setting. Set it to `false` to turn ACNS off.
- **Existing clusters.** You can turn ACNS on or off on a running cluster.

ACNS works with or without overlay.

## Route egress through your own firewall

To send the cluster's egress through your own firewall or NVA, set `outboundType` to `userDefinedRouting` and use your own subnet:

```yaml
global:
  connectivity:
    network:
      vnet:
        subnetArmId: /subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Network/virtualNetworks/<vnet>/subnets/<subnet>
  controlPlane:
    networking:
      outboundType: userDefinedRouting
```

Prepare the subnet first:

- **Bring your own subnet.** A VNet created by the cluster has no route table, so `userDefinedRouting` requires `subnetArmId`.
- **Default route.** The subnet's route table must send `0.0.0.0/0` to your egress device. If node pools use their own subnets, each of them needs that route table too.

## Change the outbound type of an existing cluster

You can change `outboundType` on a running cluster along the [migration paths AKS supports](https://learn.microsoft.com/azure/aks/egress-outboundtype). On your own subnet, these are `loadBalancer`, `userAssignedNATGateway` and `userDefinedRouting`.

The change interrupts existing connections and changes the cluster's egress IP. Update firewall rules and authorized IP ranges that rely on the old IP.
