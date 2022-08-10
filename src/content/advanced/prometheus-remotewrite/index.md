---
linkTitle: Prometheus RemoteWrite
title: Prometheus RemoteWrite
description: A guide explainig what the Giant Swarm Prometheus Remote Write feature is and how to use it.
weight: 50
menu:
  main:
    parent: advanced
user_questions:
  - What is a Prometheus RemoteWrite?
  - How Prometheus RemoteWrite work?
  - How do I get access to management cluster metrics?
aliases:
  - /advanced/remotewrite/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2022-07-19
---

In this document you will learn how to use the Prometheus RemoteWrite feature provided out of the box by Giant Swarm.

## Introduction to Prometheus RemoteWrite

Prometheus allows users to replicate its data into 3rd party systems like Grafana Cloud or even another Prometheus using its [remote APIs](https://prometheus.io/blog/2019/10/10/remote-read-meets-streaming/#remote-apis).
To enable this behavior, Prometheus needs to be configured using [remote_write config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) to define which endpoints to send data to.

## What is the Giant Swarm Prometheus RemoteWrite feature

The Prometheus `RemoteWrite` feature that allows you to configure remote write targets in the Giant Swarm managed prometheus set up on your management cluster.
That way, you can replicate and send metrics to your own 3rd party system and use the data as you see fit for the component running on the management clusters such as Flux

Giant Swarm provides and uses a `RemoteWrite` Custom Resource Definition that you can use to configure `remote_write` targets.

For example, this "RemoteWrite" Custom Resource indicates that we configure the remote write feature for all clusters (`clusterSelector: {}`) to send the data to grafana cloud (`url: https://prometheus-us-central1.grafana.net/api/prom/push`)

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: RemoteWrite
metadata:
  name: grafana-cloud
  namespace: monitoring
spec:
  ## Defines the cluster to configure prometheus remote write for
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
