---
linkTitle: Container network interface
title: Container network interface
description: An introduction to the container network interface used in Giant Swarm clusters.
weight: 20
menu:
  main:
    parent: platform-overview-connectivity
user_questions:
  - How does Giant Swarm configure Cilium on clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2025-02-17
---

Every Giant Swarm Kubernetes cluster uses [Cilium](https://cilium.io) as a container networking interface (CNI). This ensures proper connectivity between nodes, services and pods in the cluster.

## Configuration

Since the CNI is an important component when bootstrapping a cluster, Cilium is installed ahead of the [Giant Swarm App Platform]({{< relref "/overview/fleet-management/app-management" >}}).

To ensure smooth operation, some deviations from the default configuration of Cilium are taken. Among these are:

- Increased policy BPF map size (`bpf-policy-map-max: 65536`)
- [Hubble](https://docs.cilium.io/en/stable/observability/hubble/#hubble-intro) is enabled by default
- [Local redirect policies](https://docs.cilium.io/en/stable/network/kubernetes/local-redirect-policy/) are enabled
- Ignore common, high cardinality labels from identity computation of pods and services. This means, it is not possible to use these labels in network policies.
  In addition to the [default exclusions](https://docs.cilium.io/en/stable/operations/performance/scalability/identity-relevant-labels/#identity-relevant-labels), the following labels are ignored:
    - Flux labels (`.*fluxcd\.io/.*`)
    - PSS labels (`.*/enforce`)
    - `.*kubernetes\.io/managed-by.*`
    - `job-name`
- Install a PodDisruptionPolicy
- Disable built in Envoy Proxy DaemonSet
- Disable `kube-proxy` usage. See [Kubernetes Without kube-proxy](https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/)

All changes to the official Helm chart are recorded in [https://github.com/giantswarm/cilium-app/tree/main/diffs](https://github.com/giantswarm/cilium-app/tree/main/diffs).

## Troubleshooting

In case you experience any problems that could be related to Cilium or network connectivity, please consult these documents:

- [Cilium troubleshooting in the Giant Swarm handbook](https://handbook.giantswarm.io/docs/support-and-ops/ops-recipes/cilium-troubleshooting/)
- [Official Cilium troubleshooting docs](https://docs.cilium.io/en/stable/operations/troubleshooting/)
