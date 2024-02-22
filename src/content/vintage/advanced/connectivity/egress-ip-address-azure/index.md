---
linkTitle: Egress IP address on Azure
title: Setting an egress IP address on Azure
description: How to reuse an existing public IP address for outgoing traffic of worker nodes on Azure.
weight: 125
menu:
  main:
    parent: advanced-connectivity
user_questions:
  - How can I customize the public IP address for egress traffic on Azure?
last_review_date: 2023-11-07
aliases:
  - /advanced/connectivity/egress-ip-address-azure
  - /guides/egress-ip-address-azure
  - /advanced/egress-ip-address-azure
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

Giant Swarm's workload clusters on Azure use [NAT gateways](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-overview) to provide internet access to worker nodes.

By default, a new dedicated [public IPv4 address](https://docs.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses) is created during the workload cluster setup process to be used as the public
IP address for the NAT gateway of worker nodes.
This means there is no way to know in advance what public IP address a certain workload cluster will have for egress traffic
until it is created.

## Reuse of an existing public IP address

Starting from Giant Swarm release v15.1.0 for Azure it is possible to use an existing, externally created public IPv4 address for
the NAT gateway of worker nodes.

In order to do so:

1. Create a public IPv4 address in the same subscription the workload cluster will be created into. The IP address can
be in any resource group, but it needs to use the `Standard` SKU and be in the same region as the workload cluster.
2. Edit the workload cluster's [`AzureCluster`]({{< relref "/vintage/use-the-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) resource via the Management API and set the resource ID of the public IP address as a value for the `giantswarm.io/workers-egress-external-public-ip` annotation, as in the following example:

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
kind: AzureCluster
metadata:
  name: ab123
  ...
  annotations:
    giantswarm.io/workers-egress-external-public-ip: "/subscriptions/<subscription ID>/resourceGroups/<resource group>/providers/Microsoft.Network/publicIPAddresses/<public ip name>"
spec:
  ...
```

You can set the annotation to either an existing workload cluster or a brand-new one.

To enable and disable the use of an external IP address for an existing workload cluster, just add or remove the annotation from the `AzureCluster` resource at any time. Reconciliation takes just a few minutes to switch between the two modes and there shouldn't be any significant network packet loss while switching.

## Caveats and limitations

- You can't use the same public IP address for more than one workload cluster at the same time. This is an Azure limitation.

- This feature is only supported for node pools (worker nodes) and not for the control plane node.

- If you enable the feature in an existing workload cluster, the previously used public IP will not be deleted. This can lead to some undesired increase in the Azure bill.
  If the external IP address feature is disabled again, the automatically generated public IP address will be reused.

- There is no user interface support for enabling or disabling this setting.
