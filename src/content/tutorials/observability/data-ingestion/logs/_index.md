---
title: Ingest logs into the Observability Platform
linkTitle: Logs
description: How to make new logs available in the Observability Platform in self-service.
menu:
  principal:
    parent: tutorials-observability-data-ingestion
    identifier: tutorials-observability-data-ingestion-logs
weight: 50
last_review_date: 2025-03-05
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How to ingest new logs?
  - Why do my clusters run Alloy?
---

By default, Giant Swarm clusters starting from CAPA v29.2.0, and CAPZ v29.1.0 are equipped with [Alloy](https://grafana.com/docs/alloy), an Observability data collector. It's configured to collect system logs from the cluster and forward them to a central [Loki](https://grafana.com/docs/loki) instance running on the management cluster. See [Logging]({{< relref "/overview/observability/logging" >}}) for more details.

The observability platform allows to ingest logs from your workloads in a self-service way using [PodLogs][1] to select which pods to ingest logs.

From release `v29.5.0` in CAPA and CAPZ, and `v29.2.0` in CAPV and CAPVCD, additional targets to collect logs from can be configured either with a pod label or a [PodLogs][1] resource.

### Using pod labels

The Observability Platform automatically ingest all logs for pods that are labelled with the `observability.giantswarm.io/tenant` label via PodLogs resources.

Example:

```yaml
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: example-namespace
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        # This is where the tenant label must be configured
        observability.giantswarm.io/tenant: myteam
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
EOF
```

With this deployed manifest, Grafana Alloy will collect all logs for the `nginx` ingress pods and send the logs to the `myteam` tenant.

**Warning:** As our multi-tenancy aligns tenants across our platform on Grafana Organizations please make sure that the `observability.giantswarm.io/tenant` label references an existing tenant defined in a Grafana Organization. Any logs and events that are sent to a non-existing tenant will be dropped by Loki. If you want the logs and events to be ingested into the `Shared Org` you have to set the label to `giantswarm`. Learn more about our multi-tenancy in [Multi-tenancy in the observability platform]({{< relref "/tutorials/observability/multi-tenancy/" >}})

The following LogQL query can be used in `Grafana > Explore` UI to show all logs ingested for the `Deployment`, in our example:

```logql
{namespace="example-namespace", pod=~"nginx-deployment.+"}
```

Learn more about LogQL in [Exploring logs with LogQL]({{< relref "/tutorials/observability/data-exploration/exploring-logs" >}}).

### Using PodLogs

[PodLogs][1] resources are more flexible than pod labels as they can be used to:

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
  name: example-podlog
  namespace: example-namespace
spec:
  namespaceSelector:
    matchLabels:
      kubernetes.io/metadata.name: example-namespace
  relabelings:
  # This configures the tenant name under which the data will be stored in the observability platform
  - action: replace
    replacement: myteam
    targetLabel: giantswarm_observability_tenant
  - action: replace
    sourceLabels: [__meta_kubernetes_pod_node_name]
    targetLabel: node_name
  selector:
    matchLabels:
      foo: bar
EOF
```

This will select all pods with the `foo: bar` label in the namespace `example-namespace` and add the `node_name` label to the logs metadata. It will send all the logs extracted by this PodLog under the `myteam` tenant.

**Warning:** As our multi-tenancy aligns tenants across our platform on Grafana Organizations please make sure that the `giantswarm_observability_tenant` label references an existing Grafana Organization. Any logs and events that are sent to a non-existing tenant (speak: Grafana Organization) will be dropped by Loki. If you want the logs and events to be ingested into the `Shared Org` you have to set the label to `giantswarm`. Learn more about our multi-tenancy in [Multi-tenancy in the observability platform]({{< relref "/tutorials/observability/multi-tenancy/" >}})

More examples can be found [here](https://github.com/giantswarm/alloy-app/blob/main/helm/alloy/examples/logs/podlogs.yaml).

The following LogQL query can be used in `Grafana > Explore` UI to show all logs ingested for the `PodLogs` resource, in our example:

```logql
{job="example-namespace/example-podlog"}
```

Learn more about LogQL in [Exploring logs with LogQL]({{< relref "/tutorials/observability/data-exploration/exploring-logs" >}}).

### Technical considerations

By default, log ingestion is enabled for the following namespaces:

- `kube-system`
- `giantswarm`

This is done through a set of predefined [PodLogs][1] resources created in the `kube-system` namespace and labelled with `giantswarm.io/managed-by: alloy-logs`. These PodLogs shouldn't be overwritten or we can't guarantee the operational safety of the clusters.

### Performances considerations

Keep in mind that ingesting new logs into the observability platform comes with a cost. The resource consumption of the central `Loki` is related to the amount of logs it has to handle. This means ingesting more logs also leads to higher resource consumption of the observability platform overall. Also note that logs are tailed through Kubernetes API on the cluster, impacting network traffic and CPU consumption of the API server pods.

You can check the resources usage of Kubernetes API server pods in `Kubernetes / Compute Resources / Pod` dashboard in your installation's Grafana.

[1]: https://grafana.com/docs/alloy/latest/reference/components/loki/loki.source.podlogs/#podlogs-custom-resource
