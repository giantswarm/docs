---
linkTitle: Prometheus RemoteWrite
title: Prometheus RemoteWrite
description: A guide explaining how to set up your Prometheus remote write integration.
weight: 50
menu:
  main:
    identifier: getting-started-observability-monitoring-prometheus-remotewrite
    parent: getting-started-observability-monitoring-prometheus
user_questions:
  - What is Prometheus RemoteWrite?
  - How Prometheus RemoteWrite works?
  - How do I get access to management cluster metrics?
aliases:
  - /getting-started/observability/monitoring/prometheus/remotewrite
  - /observability/prometheus/remotewrite
  - /observability/monitoring/prometheus/remotewrite
  - /ui-api/observability/prometheus/remotewrite
  - /ui-api/observability/monitoring/prometheus/remotewrite
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-02-26
---

In this document you will learn how to set up your Prometheus remote write integration.

__Warning:__ This feature and the documentation is quite new, so do not hesitate to ask for support or help us improve this documentation.

## Introduction to Prometheus RemoteWrite

Prometheus allows users to replicate its data into 3rd party systems like Grafana Cloud or even another Prometheus using its [remote APIs](https://prometheus.io/blog/2019/10/10/remote-read-meets-streaming/#remote-apis).
To enable this behavior, Prometheus needs to be configured using [remote_write config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) to define which endpoints to send data to.

## What is the Giant Swarm Prometheus RemoteWrite feature

The Prometheus `RemoteWrite` feature allows you to configure remote write targets in the Giant Swarm managed prometheus running on your management cluster.
That way, you can replicate and send metrics to your own 3rd party system and use the data as you see fit.

Example:

This `RemoteWrite` Custom Resource configures all clusters (`clusterSelector: {}`) to send the data to a single Prometheus (`url: https://your-prometheus-instance.io/api/prom/push`)

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: RemoteWrite
metadata:
  name: your-prometheus-instance
  namespace: monitoring
spec:
  ## Defines the cluster to configure prometheus remote write for
  ## It select the Prometheus resource to be configured using a label selector
  ## see https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.21/#labelselector-v1-meta
  clusterSelector: {}
  remoteWrite:
    ## Configure the authentication to use values from the your-prometheus-instance secret
    basicAuth:
      password:
        key: password
        name: your-prometheus-instance
      username:
        key: username
        name: your-prometheus-instance
    name: your-prometheus-instance
    queueConfig:
      capacity: 10000
      maxSamplesPerSend: 1000
      minShards: 10
    url: https://your-prometheus-instance.io/api/prom/push
  ## Secret values to be used for authentication
  secrets:
  - data:
      password: base64-encoded-string
      username: base64-encoded-string
    name: your-prometheus-instance
```

## RemoteWrite CRD

The RemoteWrite CRD documentation can be found [here](https://doc.crds.dev/github.com/giantswarm/prometheus-meta-operator/monitoring.giantswarm.io/RemoteWrite/v1alpha1@v4.5.1) or on any management cluster using `kubectl explain`.

## Data filtering

The amount of metrics sent by our Prometheus can be quite high. In order to prevent this you can filter out metrics being sent over remote write.

This is achieved using the relabeling feature via the `writeRelabelConfigs` field, here are some examples :

Wildcard filtering, only allowing metrics starting with `aggregation:` or `prometheus_` to be sent

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: RemoteWrite
metadata:
  name: your-prometheus-instance
  namespace: monitoring
spec:
  clusterSelector: {}
  remoteWrite:
    name: your-prometheus-instance
    url: https://your-prometheus-instance.com/api/prom/push
    writeRelabelConfigs:
      - action: keep
        regex: (^aggregation:.+|^prometheus_.+)
        sourceLabels:
          - __name__
```

Blacklist filtering, sending all metrics expect the ones starting with `aggregation:` or `prometheus_`

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: RemoteWrite
metadata:
  name: your-prometheus-instance
  namespace: monitoring
spec:
  clusterSelector: {}
  remoteWrite:
    name: your-prometheus-instance
    url: https://your-prometheus-instance.com/api/prom/push
    writeRelabelConfigs:
      - action: drop
        regex: (^aggregation:.+|^prometheus_.+)
        sourceLabels:
          - __name__
```

More details on how to use relabeling can be found in the official doc [here](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config)
