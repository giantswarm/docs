---
linkTitle: Cost-optimization
title: Cost optimization tools
description: Cost is always a concern when running IT infrasturcture. This document is a curated list of cost optimization tools that we have found to be valuable for our customers and oursleves.
weight: 100
menu:
  main:
    parent: advanced
user_questions:
- What cost optimization tools do you reccomend?
- How can I tune my setup to optimize for cost?
aliases:
owner:
  - https://github.com/orgs/giantswarm/teams/team-horizon
---

# Cost optimization in Kubernetes

Adoption of Kuberenetes still requires monitoring cost drivers. Improving resource utilization allows you to get the most out of your infrastructure, while maintaining your budget. This document is comrpised of a curated list of helpful tools on the journey to cost optimization. The list is based on our experience building and running owr own infrastructure, in addition to learnings we gained from working with large global enterprise.

## Visualization

- [Open Core Cost visualization tool](https://kubecost.com) - A comprehensive cost monitoring & optimization solution for teams running Kubernetes
- [AWS cost explorer](https://aws.amazon.com/es/aws-cost-management/aws-cost-explorer/) - A tool that lets users visualize, understand, and manage  AWS costs and usage over time.
- [kubectl plugin](https://github.com/robscott/kube-capacity) - A simple CLI that provides an overview of the resource requests, limits and utilization in a Kubernetes cluster.
- [Prometheus + Grafana + exporters](https://github.com/giantswarm/prometheus-operator-app) - The Prometheus Operator provides Kubernetes native deployment and management of Prometheus and related monitoring components.
   - [Limit/Requests exporter](https://github.com/cloudworkz/kube-eagle) - Kube eagle is a prometheus exporter which exports various metrics of kubernetes pod resource requests, limits and it's actual usages.   
- [Kubernetes Opex Analytics](https://github.com/rchakode/kube-opex-analytics) - A tool to help organizations track the resources being consumed by their Kubernetes clusters to prevent overpaying.

## Optimization

- [Goldilocks](https://github.com/FairwindsOps/goldilocks) - A utility that can help you identify a starting point for resource requests and limits.

## Autoscaling

- [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) - A  tool that automatically adjusts the size of the Kubernetes cluster when there are pods that failed to run in the cluster due to insufficient resources or when there are nodes in the cluster that have been underutilized for an extended period of time.
- [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale) - The Horizontal Pod Autoscaler (HPA) automatically scales the number of Pods in a replication controller, deployment, replica set or stateful set based on observed CPU utilization or custom metrics.
  - [Custom Metrics](https://github.com/zalando-incubator/kube-metrics-adapter) - Kube Metrics Adapter is a general purpose metrics adapter for Kubernetes that can collect and serve custom and external metrics for Horizontal Pod Autoscaling.
- [Vertical Pod Autoscaler](https://github.com/giantswarm/vertical-pod-autoscaler-app) - Vertical Pod Autoscaler (VPA) frees the users from necessity of setting up-to-date resource limits and requests for the containers in their pods.

## Dev/Test clusters

- [Janitor](https://codeberg.org/hjacobs/kube-janitor) - Kubernetes Janitor cleans up (deletes) Kubernetes resources on (1) a configured TTL (time to live) or (2) a configured expiry date (absolute timestamp).
- [Kubedownscaler](https://codeberg.org/hjacobs/kube-downscaler) - A tool to scale down / "pause" Kubernetes workloads (Deployments, StatefulSets, and/or HorizontalPodAutoscalers and CronJobs too !) during non-work hours.

## Summary

Cost optimization is a journey. You will find you need to adopt different tools and continually tweak your setup to get the greatest benefit from cloud native.

