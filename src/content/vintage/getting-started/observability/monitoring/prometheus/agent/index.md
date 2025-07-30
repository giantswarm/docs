---
linkTitle: Prometheus agent
title: Prometheus Agent
description: This article explains what the prometheus agent is in Giant Swarm clusters.
weight: 50
menu:
  main:
    identifier: getting-started-observability-monitoring-prometheus-agent
    parent: getting-started-observability-monitoring-prometheus
user_questions:
  - What is the prometheus agent?
  - What does the prometheus agent imply for my clusters?
  - What does the prometheus agent imply for my clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-02-26
---

In this article you will learn what is the Prometheus Agent running inside Giant Swarm clusters.

**Note**: The Prometheus Agent is only running in releases starting from:

| Provider      | Release version                    |
|---------------|------------------------------------|
| Vintage AWS   | release v18.2.x                    |
| Vintage Azure | release v19.x.x                    |
| CAPA          | default-apps-aws v0.11.0           |
| CAPG          | default-apps-gcp v0.16.0           |
| CAPVCD        | default-apps-cloud-director v0.3.0 |
| CAPV          | default-apps-vsphere v0.6.0        |
| CAPZ          | default-apps-azure v0.0.8          |

## Introduction to monitoring

Each cluster created on the Giant Swarm platform benefits from our monitoring (a dedicated Prometheus instance) which allows us to provide you with 24/7 support to ensure best quality of service.

## What is the Prometheus Agent?

The **Prometheus Agent** is an in-cluster daemon used to scrape the metrics for all Giant Swarm managed components.
For users aware of what Prometheus is, the [Prometheus Agent](https://prometheus.io/blog/2021/11/16/agent/) is a lightweight version of a Prometheus Server equipped with a subset of Prometheus capabilities (mostly service discovery, metric scraping and remote write).

## Why do we need the Prometheus Agent?

For historical reasons, Giant Swarm monitoring used to only be deployed on the Management cluster (1 dedicated Prometheus per cluster) and the scraping of our targets was going through the `kube-apiserver` acting as a proxy for the service discovery and scraping of the target metrics.

However, with the evolution of Kubernetes and the arrival of CAPI clusters, our approach to scrape metrics from outside the cluster no longer works because:

- in CAPI clusters, workload cluster nodes are not reachable from the management clusters (no peering/no route to host) so `kube-apiserver` behind a load balancer cannot be scraped from outside the cluster
- in Kubernetes 1.22, `kube-scheduler` and `kube-controller-manager` metrics endpoint requires authentication that is stripped by the `kube-apiserver proxy`

Hence, we decided to release a Prometheus Agent alongside Giant Swarm managed [Prometheus operator](https://github.com/giantswarm/prometheus-operator-app)

## Prometheus Agent Architecture

![Architecture diagram of the Prometheus Agent architecture](prometheus-agent-architecture.png)
<!-- Source: https://drive.google.com/file/d/1Pr0J1x-nPF1klZEFfwJ3gZhxTRjuI1aM -->

**Note**: We are using an ingress with Ingress NGINX Controller not represented here on the management cluster so the Prometheus Agent can send its data to the workload cluster Prometheus on the Management Cluster using the Remote Write API

**Warning**: As of this writing, the agent is sending data to a Prometheus but we are thinking about moving to a Long Term Storage solution in the future.

The Prometheus Agent is scrapping [`Service Monitors`](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/user-guides/getting-started.md#deploying-a-sample-application) in the workload clusters labelled with `application.giantswarm.io/team`.
At the time of this writing, the targets include:

- kubernetes core components (kube-apiserver, kube-scheduler and kube-controller-manager)
- prometheus operator
- the agent itself

The other targets are scraped by the workload cluster prometheus and will transition to the agent over time.

If you are using Prometheus Operator, you can deploy your own service monitors as long as they do not carry this label.

## Access to the Prometheus Agent information

### Accessing the UI

As the Prometheus Agent is running in your workload cluster, you can gain access to its UI to inspect the list of currently configured targets it is scraping using the following command `kubectl port-forward -n kube-system prometheus-prometheus-agent-0 9090` then access the url `https://localhost:9090/targets` on your favorite browser.

You should see the following:

![Screenshot of Prometheus Agent User Interface](prometheus-agent-ui.png)

### Access to the metrics

The metrics of the Prometheus Agent can be found on the [grafana instance]({{< relref "/overview/observability/data-management/data-exploration/" >}}) running on your management cluster under the `Prometheus / Remote Write` and `Ingress NGINX Controller` dashboards
