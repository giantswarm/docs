+++
title = "Getting Basic Metrics in your Cluster"
description = "Recipe to enable a core metrics solution running on your Kubernetes cluster."
date = "2018-03-13"
type = "page"
weight = 140
tags = ["recipe"]
+++

# Metrics in Kubernetes

Getting core metrics like CPU and Memory usage of resources in your cluster is important not only for your own monitoring purposes, but also for extended functionality like horizontal Pod autoscaling.

The kubelet exposes core metrics of the nodes/pods via an endpoint, however, you need an additional monitoring tool to collect and expose those metrics. Until recently, the tool of choice for this was Heapster and its API. But with the recent move to a more general Metrics API you get such metrics directly from the Kubernetes API endpoint. However, for this to work you need to still run a monitoring tool that collects and exposes the metrics, as the Kubernetes API only aggregates monitoring backends to be exposed by it.

# Adding Metrics with Metrics Server

[Metrics Server](https://github.com/kubernetes-incubator/metrics-server) is a cluster-wide aggregator of resource usage data, which it collects from the Summary API of the kubelets of each node. It registers itself in the main API server through Kubernetes Aggregator and thus is discoverable through the same API endpoint as the rest of Kubernetes under `/apis/metrics.k8s.io/`.

To deploy it run:

```bash
git clone https://github.com/kubernetes-incubator/metrics-server/tree/master/deploy/1.8%2B
cd metrics-server
kubectl apply --filename deploy/1.8+/
```

__Note__: For Metrics Server to work you need to have Kubernetes API Aggregator enabled on your cluster. This is enabled by default on clusters started after February 14th 2018. For older clusters you can use Heapster as described below.

# Adding Metrics with Heapster (standalone)

In clusters with Kubernetes version under 1.9, Heapster can be deployed as a standalone solution.

Deploying Heapster is very straight forward.

```bash
kubectl apply --filename https://raw.githubusercontent.com/kubernetes/heapster/master/deploy/kube-config/rbac/heapster-rbac.yaml
kubectl apply --filename https://raw.githubusercontent.com/kubernetes/heapster/master/deploy/kube-config/standalone/heapster-controller.yaml
```

# Use cases

There are some common cases where Core Metrics are used by Kubernetes:

- Horizontal Pod Autoscaler: It scales pods automatically based on CPU or custom metrics (not explained here). More information [here](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale).
- Kubectl top: The command `top` of our beloved Kubernetes CLI display metrics directly in the terminal.
- Kubernetes dashboard: See Pod and Nodes metrics integrated into the main Kubernetes UI dashboard. More info [here](/guides/install-kubernetes-dashboard)
- Scheduler: In the future Core Metrics will be considered in order to schedule best-effort Pods.

# Further Reading

- [Kubernetes Monitoring Architecture](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/monitoring_architecture.md)
- [Resource Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/resource-metrics-api.md)