+++
title = "Adding Metrics with Heapster"
description = "Recipe to get the Heapster monitoring solution running."
date = "2016-10-10"
type = "page"
weight = 140
tags = ["recipe"]
+++

# Adding Metrics with Heapster

Heapster is a simple monitoring solution that supports Kubernetes and CoreOS natively. Although we usually prefer [Prometheus](/guides/kubernetes-prometheus/), currently you need Heapster for integrating metrics in [Kubernetes Dashboard](http://docs.staging.gigantic.io/guides/install-kubernetes-dashboard/) or running the [Horizontal Pod Autoscaler](http://kubernetes.io/docs/user-guide/horizontal-pod-autoscaling/).

You can deploy Heapster as a standalone solution (recommended if you are running Prometheus for monitoring anyway) or as a complete monitoring solution, e.g. together with InfluxDB and Grafana (currently not documented here).

## Deploy Heapster (standalone)

Deploying Heapster is very straight forward.

```bash
kubectl apply --filename https://raw.githubusercontent.com/giantswarm/kubernetes-heapster/master/manifests-all.yaml
```

If you have the [Kubernetes Dashboard](http://docs.staging.gigantic.io/guides/install-kubernetes-dashboard/) installed, you should be able to see metrics being shown in the workload overview as well as on the pods after a reload. If they don't show up directly, just wait a moment and try again.
