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

- Open Core Cost visualization tool https://kubecost.com
- AWS cost explorer https://aws.amazon.com/es/aws-cost-management/aws-cost-explorer/ 
- kubectl plugin https://github.com/robscott/kube-capacity
- Prometheus + Grafana + exporters https://github.com/giantswarm/prometheus-operator-app
   - Limit/Requests exporter https://github.com/cloudworkz/kube-eagle  
- Kubernetes Opex Analytics https://github.com/rchakode/kube-opex-analytics

## Optimization

- Goldilocks https://github.com/FairwindsOps/goldilocks

## Autoscaling

- Cluster Autoscaler https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler
- Horizontal Pod Autoscaler https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- Vertical Pod Autoscaler https://github.com/giantswarm/vertical-pod-autoscaler-app
- Custom Metrics https://github.com/zalando-incubator/kube-metrics-adapter 

## Dev/Test clusters

- Janitor https://codeberg.org/hjacobs/kube-janitor
- Kubedownscaler https://codeberg.org/hjacobs/kube-downscaler

## Summary

Cost optimization is a journey. You will find you need to adopt different tools and continually tweak your setup to get the greatest benefit from cloud native.

