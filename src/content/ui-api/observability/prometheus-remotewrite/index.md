---
linkTitle: Prometheus RemoteWrite
title: Prometheus RemoteWrite
description: A guide explaining how to set up your Prometheus remote write integration.
weight: 50
menu:
  main:
    identifier: uiapi-observability-prometheusremotewrite
    parent: uiapi-observability
user_questions:
  - What is Prometheus RemoteWrite?
  - How Prometheus RemoteWrite works?
  - How do I get access to management cluster metrics?
aliases:
  - /observability/remotewrite/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2022-09-12
---

In this document you will learn how to set up your Prometheus remote write integration.

__Warning:__ This feature and the documentation is quite new, so do not hesitate to ask for support or help us improve this documentation.

## Introduction to Prometheus RemoteWrite

Prometheus allows users to replicate its data into 3rd party systems like Grafana Cloud or even another Prometheus using its [remote APIs](https://prometheus.io/blog/2019/10/10/remote-read-meets-streaming/#remote-apis).
To enable this behavior, Prometheus needs to be configured using [remote_write config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) to define which endpoints to send data to.

## What is the Giant Swarm Prometheus RemoteWrite feature

The Prometheus `RemoteWrite` feature allows you to configure remote write targets in the Giant Swarm managed prometheus running on your management cluster.
That way, you can replicate and send metrics to your own 3rd party system and use the data as you see fit.

Giant Swarm provides and uses a `RemoteWrite` Custom Resource Definition that you can use to configure `remote_write` targets.

For example, this `RemoteWrite` Custom Resource indicates that we configure the remote write feature for all clusters (`clusterSelector: {}`) to send the data to grafana cloud (`url: https://prometheus-us-central1.grafana.net/api/prom/push`)

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: RemoteWrite
metadata:
  name: grafana-cloud
  namespace: monitoring
spec:
  ## Defines the cluster to configure prometheus remote write for
  ## It select the Prometheus resource to be configured using a label selector
  ## see https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.21/#labelselector-v1-meta
  clusterSelector: {}
  remoteWrite:
    ## Configure the authentication to use using the values from the grafana-cloud secret
    basicAuth:
      password:
        key: password
        name: grafana-cloud
      username:
        key: username
        name: grafana-cloud
    name: grafana-cloud
    queueConfig:
      capacity: 10000
      maxSamplesPerSend: 1000
      minShards: 10
    url: https://prometheus-us-central1.grafana.net/api/prom/push
  ## Secret values to be used for authentication
  secrets:
  - data:
      password: ...
      username: ...
    name: grafana-cloud
```

## RemoteWrite CRD

The RemoteWrite CRD documentation can be found [here](https://doc.crds.dev/github.com/giantswarm/prometheus-meta-operator/monitoring.giantswarm.io/RemoteWrite/v1alpha1@v4.5.1) or on any management cluster using `kubectl explain`.
