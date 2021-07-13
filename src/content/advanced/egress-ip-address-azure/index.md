---
linkTitle: Egress IP address on Azure
title: Egress IP address on Azure
description: How to reuse an existing Public IP address for egress traffic of worker nodes on Azure.
weight: 125
menu:
  main:
    parent: advanced
owner:
  - https://github.com/orgs/giantswarm/teams/team-celestial
last_review_date: 2021-07-13
user_questions:
- How can I customize the public IP address for egress traffic?
---

# Egress IP address on Azure

Giant Swarm's `Workload Clusters` use [Azure NAT Gateways](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-overview?ocid=AID754288&wt.mc_id=azfr-c9-scottha,CFID0658) to provide internet access to node pool nodes.

By default a new dedicated Public IPv4 address is created during the `Workload Cluster` set up process to be used as the public
IP address for the NAT Gateway of Node Pools' nodes.
This means there is no way to know in advance what public IP address a certain `Workload Cluster` will have for egress
until it is created.

## Reuse of an existing Public IP address

Starting from Giant Swarm release 15.1.0 for Azure it is possible to use an existing, externally created Public IPv4 address for
the NAT gateway of Node Pools' Nodes.

In order to do so:

1. Create a Public IPv4 Address in the same subscription the `Workload Cluster` will be created into. The IP Address can
be in any `Resource Group`, but it needs to use the `Standard` SKU and be in the same Region as the `Workload Cluster`.
2. Set the `Resource ID` of the Public IP Address as a value for the `giantswarm.io/workers-egress-external-public-ip`
annotation in the `AzureCluster` `Custom Resource` as in the following example:

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

You can set the annotation to either an existing `Workload Cluster` or a brand-new one.

## Caveats and limitations

- You can't use the same Public IP address for more than one `Workload Cluster` at the same time. This is an Azure limitation.
- You can enable and disable the use of an External IP Address for a `Workload Cluster` at any time by adding or
  removing the `annotation` from the `AzureCluster` Custom Resource. Reconciliation takes just a few minutes to switch
  between the two modes and there shouldn't be any significant network packet loss while switching.
- This feature is only supported for Node Pools and not for the Master node.
- If you enable the feature in an existing `Workload Cluster`, the previously used `Public IP` will not be deleted. This can lead to some undesired increase in the Azure bill.
  If the external IP address feature is disabled again, the automatically generated public IP address will be reused.
- There is no frontend support for this feature. The only way of enabling it is by editing the `AzureCluster` Custom Resource via the `Management Cluster` Kubernetes API.
