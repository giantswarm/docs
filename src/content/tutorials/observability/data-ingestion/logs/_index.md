---
title: Ingest logs into the Observability Platform
linkTitle: Logs
description: How to make new logs available in the Observability Platform in self-service.
menu:
  principal:
    parent: tutorials-observability-data-ingestion
    identifier: tutorials-observability-data-ingestion-logs
weight: 50
last_review_date: 2024-11-08
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How to ingest new logs?
  - Why do my clusters run Alloy?
---

By default, Giant Swarm clusters starting from release v29.0.0 are equipped with [Alloy](https://grafana.com/docs/alloy), it is a lightweight, high-performance log agent that collects system logs from your cluster and forwards them to a central [Loki](https://grafana.com/docs/loki) instance running on the management cluster.

The Giant Swarm Observability Platform allows you to ingest logs from your workloads in a self-service way using labels to select which pods to ingest logs from.

### Label your resources

The label `giantswarm.io/logging` can be set to `true` or `false` on any Namespace or Pod. When the label is not set it is considered `false`.

- Pods in any namespace can be labeled
- Namespace can be labeled, the value used for the namespace will be the default for all pods in this namespace
- Pods label take precedence over Namespace label, e.g. logging can be enabled for a pod in a namespace where logging is disabled and vice versa.

||Pod `giantswar.io/logging=true`|Pod `giantswar.io/logging=false`|Pod `unset`
|-|------------------------------|--------------------------------|--------------------------
**Namespace** `giantswar.io/logging=true`|<i class="fas fa-check"></i>|<i class="fas fa-times"></i>|<i class="fas fa-check"></i>
**Namespace** `giantswar.io/logging=false`|<i class="fas fa-check"></i>|<i class="fas fa-times"></i>|<i class="fas fa-times"></i>
**Namespace** `unset`|<i class="fas fa-check"></i>|<i class="fas fa-times"></i>|<i class="fas fa-times"></i>

You can use the following command to label a namespace or a pod:

```bash
kubectl label namespace <namespace> giantswarm.io/logging=true
kubectl label pod <pod> giantswarm.io/logging=true
```

Logs lines can then be viewed in Grafana Explore, learn more about this in [Exploring logs with LogQL]({{< relref "/tutorials/observability/data-exploration/exploring-logs" >}}).

### Performances considerations

Keep in mind that ingesting new logs into the Observability Platform comes with a cost. The resource consumption of the central Loki is related to the amount of logs it has to handle. This means ingesting more lokgs also leads to higher resource consumption of the Observability Platform overall. Also note that logs are tailed through Kubernetes API which has an impact on network traffic and CPU consumption of Kubernetes API server pods.

You can check the resources usage of Kubernetes API server pods in `Kubernetes / Compute Resources / Pod` dashboard in your installation's Grafana.
