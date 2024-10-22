---
title: Ingest logs into the Observability Platform
linkTitle: Logs
description: How to make new logs available in the Observability Platform in self-service.
menu:
  principal:
    parent: tutorials-observability-data-ingestion
    identifier: tutorials-observability-data-ingestion-logs
weight: 50
last_review_date: 2024-10-09
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How to ingest new logs?
  - Why do my clusters run Alloy?
---

By default, Giant Swarm clusters starting from CAPA v29.2.0, and CAPZ v29.1.0 are equipped with [Alloy](https://grafana.com/docs/alloy), a lightweight, high-performance [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) collector. It's configured to collect system logs from the cluster and forward them to a central [Loki](https://grafana.com/docs/loki) instance running on the management cluster. See [Logging architecture]({{< relref "/vintage/getting-started/observability/logging/architecture" >}}) for more details.

The observability platform allows to ingest logs from your workloads in a self-service way using [PodLogs][1] to select which pods to ingest logs.

### Using PodLogs

From release `v30.0.0` additional targets to collect logs from can be configured using [PodLogs][1] resource. Those resources can be created in any namespace. [PodLogs][1] resources can be used to:

- Filter pods targets using label selector
- Filter pods' namespaces using label selector
- Modify labels using relabeling

[PodLogs][1] can be created via a Helm Chart or [GitOps]({{< relref "/vintage/advanced/gitops" >}}). Alternatively it can also be directly created in the cluster.

Example:

```yaml
cat <<EOF | kubectl apply -f -
apiVersion: monitoring.grafana.com/v1alpha2
kind: PodLogs
metadata:
  name: example-podlogs
spec:
  selector:
    matchLabels:
      foo: bar
  namespaceSelector:
    matchLabels:
      kubernetes.io/metadata.name: charlie
  relabelings:
  - action: replace
    sourceLabels: [__meta_kubernetes_pod_node_name]
    targetLabel: node_name
EOF
```

This will select all pods with the `foo: bar` label in the namespace `charlie` and add the `node_name` label to the logs metadata. More examples can be found [here](https://github.com/giantswarm/alloy-app/blob/main/helm/alloy/examples/logs/podlogs.yaml).

Logs lines can then be viewed in `Grafana`UI on the `Explore` page; learn more about this in [Exploring logs with LogQL]({{< relref "/tutorials/observability/data-exploration/exploring-logs" >}}).

### Technical considerations

Per default log ingestion is enabled for the following namespaces:

- `kube-system`
- `giantswarm`

This is done through a set of predefined [PodLogs][1] resources created in the `kube-system` namespace and labelled with `giantswarm.io/managed-by: alloy-logs`. These PodLogs shouldn't be overwritten or we can't guarantee the operational safety of the clusters.

### Performances considerations

Keep in mind that ingesting new logs into the observability platform comes with a cost. The resource consumption of the central `Loki` is related to the amount of logs it has to handle. This means ingesting more logs also leads to higher resource consumption of the observability platform overall. Also note that logs are tailed through Kubernetes API on the cluster, impacting network traffic and CPU consumption of the API server pods.

You can check the resources usage of Kubernetes API server pods in `Kubernetes / Compute Resources / Pod` dashboard in your installation's Grafana.

[1]: https://grafana.com/docs/alloy/latest/reference/components/loki/loki.source.podlogs/#podlogs-custom-resource
