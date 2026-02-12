---
linkTitle: Network monitoring
title: Reduce cloud costs with network traffic monitoring
description: Learn how to enable network traffic monitoring to identify costly cross-AZ traffic and optimize your infrastructure spending.
weight: 10
menu:
  principal:
    parent: tutorials-observability
    identifier: tutorials-observability-network-monitoring
user_questions:
  - How can I reduce my cloud network costs?
  - How do I enable network monitoring?
  - How can I see cross-AZ traffic in my cluster?
  - Where can I find network traffic dashboards?
last_review_date: 2025-02-11
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

Network traffic, particularly cross-availability zone (cross-AZ) and egress traffic, is often a hidden but significant cost driver in cloud environments. Cloud providers typically charge for data transfer between availability zones (for example, AWS charges approximately $0.01/GB for cross-AZ traffic), and these costs can add up quickly in distributed systems.

This tutorial shows you how to enable network traffic monitoring on your clusters, interpret the provided dashboards, and identify opportunities to reduce your infrastructure costs.

## What you will learn

- How to enable network traffic monitoring on a workload cluster
- How to access and interpret the network traffic dashboards
- How to identify costly traffic patterns and optimization opportunities

## Prerequisites

Before starting this tutorial, ensure you have:

- A workload cluster running on the Giant Swarm platform
- The `observability-bundle` version 2.3.0 or later installed
- Access to Grafana dashboards in the platform

{{< note >}}
Network monitoring produces a significant amount of monitoring data, which may increase resource consumption on the management cluster. Consider this when enabling the feature on many clusters simultaneously.
{{< /note >}}

## Enable network monitoring {#enable}

Network monitoring is disabled by default and requires explicit opt-in. To enable it, add a label to your workload cluster's `Cluster` resource.

### Using kubectl

```sh
kubectl label cluster <cluster-name> giantswarm.io/network-monitoring=true
```

### Using a manifest

If you manage your cluster declaratively, add the label to your `Cluster` resource:

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  name: my-cluster
  labels:
    giantswarm.io/network-monitoring: "true"
spec:
  # ... rest of your cluster configuration
```

After applying the label, the platform automatically deploys the network monitoring components. The collector runs within the existing `alloy-logs` DaemonSet in the `kube-system` namespace, with one collector instance per node.

### Verify monitoring is active

You can verify that network monitoring is active by checking if the `beyla_network_flow_bytes_total` metric is being collected. In Grafana, navigate to **Explore** and run the following query:

```promql
beyla_network_flow_bytes_total{cluster_id="<your-cluster-id>"}
```

If data is returned, network monitoring is working correctly. Allow a few minutes after enabling for data to start appearing.

## Understanding the dashboards {#dashboards}

Two Grafana dashboards are available for analyzing network traffic. You can find them by searching for the tag `topic:networking-traffic-analysis` in Grafana.

### Network Traffic Analysis - Overview

This dashboard provides a high-level view of network traffic patterns over the **last 7 days**, aggregated at the namespace level. Use this dashboard for:

- **Trend analysis**: Spot changes in traffic patterns over time
- **Identifying top consumers**: See which namespaces generate the most cross-AZ or public traffic
- **Capacity planning**: Understand your network usage trends

Key panels:

| Panel | Description |
|-------|-------------|
| Average Public Network Traffic | Shows public-facing traffic by namespace |
| Average Cross-AZ Network Traffic | Shows traffic crossing availability zone boundaries by namespace |
| Total Public Traffic | Time series of aggregate public traffic |
| Total Cross-AZ Private Traffic | Time series of cross-AZ internal traffic |

### Network Traffic Analysis

This dashboard provides detailed, real-time visibility into network traffic over a **30-minute window**. Use this dashboard for:

- **Investigation**: Drill down into specific traffic patterns
- **Identifying top consumers**: See which namespaces generate the most traffic
- **Traffic classification**: Understand the split between private, public, and cross-AZ traffic

Key panels:

| Panel | Description |
|-------|-------------|
| Traffic Classification | Pie charts showing private vs public traffic distribution |
| Top Network Users | Tables ranking namespaces by private, public, and cross-AZ bandwidth |
| Top Destinations | Most common traffic destinations |
| Time Series | Graphs for public, private, in-AZ, and cross-AZ traffic over time |


### Example scenario: High cross-AZ traffic between services

/!\ WIP /!\

This is a example scenario where network monitoring helps you identify and reduce costs for cross-AZ traffic.

**What to look for**: In the Overview dashboard, check the "Average Cross-AZ Network Traffic" panel. Namespaces with consistently high cross-AZ traffic are candidates for optimization.

**Investigation**: Switch to the detailed dashboard and filter by the namespace. Review the traffic patterns and destinations to understand which services are communicating across zones.

**Optimization strategies**:

- **Topology-aware scheduling**: Configure your deployments to prefer scheduling pods in the same availability zone as the services they communicate with frequently. Kubernetes supports [topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) for this purpose.
- **Service topology**: For services with high internal traffic, consider using [topology-aware routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/) to prefer same-zone endpoints.
- **Co-location**: If two services communicate heavily, consider deploying them with pod affinity rules to increase the chance they run on the same node or in the same zone.

/!\ WIP /!\

## Understanding the metrics {#metrics}

Network monitoring collects data using the `beyla_network_flow_bytes_total` metric. Key labels include:

| Label | Description |
|-------|-------------|
| `src.namespace` / `dst.namespace` | Source and destination Kubernetes namespaces |
| `src.name` / `dst.name` | Source and destination pod names |
| `src.zone` / `dst.zone` | Availability zones (critical for cross-AZ analysis) |
| `direction` | Traffic direction (ingress/egress) |
| `transport` | Transport protocol (TCP/UDP) |

Traffic is classified as "cross-AZ" when `src.zone` and `dst.zone` have different values.

## Next steps

- Review the [network monitoring reference documentation]({{< relref "/reference/observability/network-monitoring" >}}) for detailed configuration options
- Learn about [Kubernetes topology-aware routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/) for reducing cross-AZ traffic
- Explore [topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) for workload placement optimization
