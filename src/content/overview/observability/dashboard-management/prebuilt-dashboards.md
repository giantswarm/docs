---
title: Pre-built dashboards
linkTitle: Pre-built dashboards
diataxis_content_type: reference
description: Catalog of the pre-built Grafana dashboards that ship out of the box with the Giant Swarm observability platform, grouped by category.
weight: 20
menu:
  principal:
    parent: overview-observability-dashboard-management
    identifier: overview-observability-dashboard-management-prebuilt-dashboards
last_review_date: 2026-07-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What dashboards come out of the box?
  - Which pre-built dashboards does the platform provide?
  - Where do the pre-built dashboards come from?
---

This page catalogs the pre-built Grafana dashboards that the Giant Swarm Observability Platform provides out of the box. They're accessible to all users through the `Shared Org` and require no setup.

The catalog is built from the [`public_dashboards`](https://github.com/giantswarm/dashboards/tree/main/helm/dashboards/charts/public_dashboards/dashboards/shared/public) section of the Giant Swarm [dashboards repository](https://github.com/giantswarm/dashboards). Dashboards are continuously updated and deployed via Helm charts. Many are synchronized from upstream community monitoring projects to provide best-practice monitoring patterns.

To learn how to find and navigate these dashboards in Grafana, see the [dashboard exploration guide]({{< relref "/overview/observability/dashboard-management/dashboard-exploration" >}}).

## Core platform dashboards

Essential cluster and infrastructure monitoring:

- **Cluster Overview** - High-level cluster health and resource utilization
- **Node Overview** - Individual node metrics, CPU, memory, disk usage
- **Node Utilization** - Node resource allocation and capacity planning

## Kubernetes component dashboards

Core Kubernetes service monitoring:

- **API Server Performance** - Kubernetes API server metrics and latency
- **Certificate Details** - TLS certificate expiration and health monitoring
- **Persistent Volume Usage** - Storage metrics and volume health
- **Giant Swarm / Kubernetes Persistent Volumes** - Enhanced PV monitoring

## Network and ingress dashboards

Network infrastructure and traffic monitoring:

- **DNS** - DNS resolution performance and CoreDNS metrics
- **Ingress Nginx Controller** - Nginx ingress controller performance
- **Nginx Ingress Controller Connection Distribution** - Connection patterns
- **Cilium Performance** - Cilium CNI performance and BPF map pressure
- **External DNS** - External DNS controller metrics

## Application and workload dashboards

Application performance and resource monitoring:

- **Pod Requests vs Usage** - Resource requests vs actual consumption
- **SLO Reporting** - Service Level Objective compliance tracking
- **Container Images from docker.io** - Container image usage analytics
- **Kong Connection Distribution** - Kong ingress controller metrics

## Observability platform dashboards

Monitoring infrastructure health:

- **Prometheus** - Prometheus server performance and resource usage
- **Prometheus Remote Write** - Remote write performance metrics
- **Alertmanager / Overview** - Alert management and notification status

## Cluster automation dashboards

Platform automation and lifecycle management:

- **Flux Control Plane** - GitOps controller health and sync status
- **KEDA** - Kubernetes Event Driven autoscaling metrics
- **Karpenter** - Node autoscaling performance (AWS)
- **AWS Load Balancer Controller** - AWS LB controller metrics (AWS)

## See also

- [Dashboard exploration]({{< relref "/overview/observability/dashboard-management/dashboard-exploration" >}}): how to find, search, and navigate dashboards in Grafana
- [Dashboard creation]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}): how to build your own custom dashboards
