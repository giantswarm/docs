---
title: Workload cluster releases
description: Learn about workload cluster releases offered by Giant Swarm and how to find more details.
weight: 30
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement-concepts
    identifier: overview-fleetmanagement-clustermanagement-concepts-releases
user_questions:
  - What is a workload cluster release?
  - Where can I find details about workload cluster releases?
  - What is a major workload cluster release?
  - What is a minor workload cluster release?
  - What is a patch workload cluster release?
  - How long are workload cluster releases supported?
  - What does it mean when a workload cluster release is deprecated?
  - How soon does Giant Swarm provide new Kubernetes versions?
  - How are workload cluster releases announced?
  - What is a pre-release?
  - What is an alpha release?
  - What is a beta release?
  - What is a release candidate?
aliases:
  - /platform-overview/cluster-management/releases
  - /reference/workload-cluster-release-versions/
last_review_date: 2025-07-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-tenet
---

Our workload cluster releases define the capabilities of the clusters you create in your installations. Here we explain our versioning and give details on workload cluster releases for certain providers.

**TL;DR**: Workload cluster releases bundle tested components together. We follow Kubernetes versioning - when Kubernetes 1.31 comes out, we release version 31.x.x. We support at least two major versions simultaneously.

## Introduction

When you create a cluster, you'll first choose a workload cluster release. Later you're likely to upgrade the cluster from release to release. Understanding the differences between major, minor, and patch releases and their impact is crucial.

Each workload cluster release bundles a stack of components with their specific versions. The workload cluster release itself is distinguished by the provider it's designed for (AWS, Azure, or vSphere) and the version number, which follows the [Semantic Versioning (SemVer)](https://semver.org/) standard.

We test workload cluster releases as a whole. To upgrade a component to a newer version, you upgrade the entire cluster to a new workload cluster release. It's our best way to ensure that all elements in the cluster work well together.

## How we version releases {#versioning-conventions}

The SemVer standard specifies version numbers in the form of `Major.Minor.Patch`.

Each new workload cluster release defines a set of changes regarding exactly one previous workload cluster release. What changed influences the version number of the latest release.

### Major version {#major}

Kubernetes is the most critical component of our workload clusters. So we align our workload cluster release versioning with Kubernetes releases.

**Convention**: For each new _minor_ Kubernetes release we provide a new _major_ workload cluster release version.

For example, the cluster release **31.x.x** will include a Kubernetes version of **1.31.x**.

We test every new major workload cluster release with a new Kubernetes minor version against the Cloud Native Foundation [conformance test suite](https://github.com/cncf/k8s-conformance).
Every workload cluster release, from patch to major, also undergoes automated integration testing.

A major workload cluster release may contain other important changes, apart from a new Kubernetes release. Check the [Details about releases and features](#release-details) section for more information.

### Minor version {#minor}

We increase (bump) the minor version number when a workload cluster release adds new functionality, while maintaining the functionality of the stack as it was in the previous version. This can include minor upgrades of third party components, except for Kubernetes.

### Patch version {#patch}

The general rule for patch releases is that they have zero impact on customers and don't require restarting cluster nodes. They fix a problem in the previous release (bug fix or security fix), implement a temporary patch, or make other changes that don't require customer action.

### Lifecycle {#lifecycle}

For every provider, we maintain at least **two major versions** of workload cluster releases simultaneously, so you have two different Kubernetes minor versions to choose from.

With our development of **new functionality** we focus on our latest major version. The older major version is mostly maintained to fix security issues and stability problems.

Workload cluster releases get [deprecated](#deprecation) when replaced by newer ones. After deprecation, and once no longer in use by any customer, a workload cluster release is archived, which means that it's no longer accessible to you.

### Deprecation {#deprecation}

Once we've released a new workload cluster release, whether it's major, minor, or patch, we usually deprecate an older version.

- As soon as we publish a new major release, we can deprecate all active releases in the two major versions preceding it, since they're no longer needed as an upgrade path.
- When we release a new minor or patch version, we deprecate the previous version. For example, when 31.1.0 comes out, the previous version 31.0.1 gets deprecated.

Once deprecated, you can continue to use the workload cluster release with existing clusters. Also, as long as you have at least one cluster in your installation running the deprecated release, you can also create new clusters using that release. This allows you to create test clusters to test an upgrade from that release.

### Pre-releases

Pre-releases (when available) let you test new features or use new functionality before the feature is officially released. At the same time, it helps us release new features and test them in a real-world scenario with your help. When you test a pre-release, it helps identify bugs or assess the impact of new functionality on the system.

Currently, not all Giant Swarm releases become available as pre-releases. We communicate pre-releases when they're available for customer testing.

Pre-releases can be alpha, beta, or release candidates (RC). This depends on the needs of the team wanting to test their feature.

When to use pre-releases:

- A new feature with unclear impact is done and the team wants to test and check its impact before deciding the scope of the release (alpha). You get early access to the feature and can see if it meets your requirements. You can report bugs and provide feedback. This lets us test the feature in a less controlled way than in our testing environments. It may also uncover unknown bugs, letting us fix them early. It could also lead to a reassessment of the feature or solution.

- A new high-impact feature is done but needs to wait for the next major release (beta). You get early access to the feature to verify it works well with your configuration and environment. You can report bugs as needed. This lets us fix unknown bugs.

- A new high-impact feature is done and is urgently needed (release candidate `rc`). You can get a pre-release to test and roll out as soon as possible. This release is complete and stable. It may not meet the quality standards of a general availability (GA) release.

### Check available releases {#inspecting}

You've got several options to inspect workload cluster release details:

- We announce new workload cluster releases in your Slack support channel. Each announcement includes a link to the release notes in our [changes and releases]({{< relref "/changes" >}}) section here on the docs site.

- Using the [`kubectl gs get release`]({{< relref "/vintage/platform-overview/web-interface/" >}}) command, you can get more information about the workload cluster releases available in your installation. This command lists all available workload cluster releases, their versions, and the Kubernetes version they contain.

### Default applications {#apps}

#### All providers

- [capi-node-labeler](https://github.com/giantswarm/capi-node-labeler-app)
- [cert-exporter](https://github.com/giantswarm/cert-exporter)
- [cert-manager](https://github.com/giantswarm/cert-manager-app)
- [chart-operator-extensions](https://github.com/giantswarm/chart-operator-extensions)
- [cilium](https://github.com/giantswarm/cilium-app)
- [cilium-servicemonitors](https://github.com/giantswarm/cilium-servicemonitors-app)
- [coredns](https://github.com/giantswarm/coredns-app)
- [coredns-extensions](https://github.com/giantswarm/coredns-extensions-app)
- [ETCD-defrag](https://github.com/giantswarm/etcd-defrag-app)
- [ETCD-k8s-resources-count](https://github.com/giantswarm/etcd-kubernetes-resources-count-exporter)
- [external-dns](https://github.com/giantswarm/external-dns-app)
- [k8s-audit-metrics](https://github.com/giantswarm/k8s-audit-metrics)
- [k8s-dns-node-cache](https://github.com/giantswarm/k8s-dns-node-cache-app)
- [metrics-server](https://github.com/giantswarm/metrics-server-app)
- [net-exporter](https://github.com/giantswarm/net-exporter)
- [network-policies](https://github.com/giantswarm/network-policies-app)
- [node-exporter](https://github.com/giantswarm/node-exporter-app)
- [observability-bundle](https://github.com/giantswarm/observability-bundle)
- [alloy-app](https://github.com/giantswarm/alloy-app)
- [prometheus-operator-crd](https://github.com/giantswarm/prometheus-operator-crd)
  * [kube-prometheus-stack-app](https://github.com/giantswarm/kube-prometheus-stack-app)
- [prometheus-agent](https://github.com/giantswarm/prometheus-agent-app)
- [promtail-app](https://github.com/giantswarm/promtail-app)
- [grafana-agent-app](https://github.com/giantswarm/grafana-agent-app)
- [observability-policies](https://github.com/giantswarm/observability-policies-app)
- [prometheus-blackbox-exporter](https://github.com/giantswarm/prometheus-blackbox-exporter-app)
- [security-bundle](https://github.com/giantswarm/security-bundle)
- [cloudnative-pg](https://github.com/giantswarm/cloudnative-pg-app)
  * [edgedb](https://github.com/giantswarm/edgedb-app)
  * [exception-recommender](https://github.com/giantswarm/exception-recommender)
  * [falco](https://github.com/giantswarm/falco-app)
  * [jiralert](https://github.com/giantswarm/jiralert-app)
  * [kyverno](https://github.com/giantswarm/kyverno-app)
  * [kyverno-crds](https://github.com/giantswarm/kyverno-crds)
  * [kyverno-policy-operator](https://github.com/giantswarm/kyverno-policy-operator)
  * [kyverno-policies](https://github.com/giantswarm/kyverno-policies)
  * [policy-api-crds](https://github.com/giantswarm/policy-api-crds)
  * [reports-server](https://github.com/giantswarm/reports-server-app)
  * [starboard-exporter](https://github.com/giantswarm/starboard-exporter)
  * [trivy](https://github.com/giantswarm/trivy-app)
  * [trivy-operator](https://github.com/giantswarm/trivy-operator-app)
- [teleport-kube-agent](https://github.com/giantswarm/teleport-kube-agent-app)
- [vertical-pod-autoscaler](https://github.com/giantswarm/vertical-pod-autoscaler-app)
- [vertical-pod-autoscaler-crd](https://github.com/giantswarm/vertical-pod-autoscaler-crd)

#### AWS

- [aws-ebs-csi-driver](https://github.com/giantswarm/aws-ebs-csi-driver-app)
- [aws-ebs-csi-driver-servicemonitors](https://github.com/giantswarm/aws-ebs-csi-driver-servicemonitors-app)
- [aws-nth-bundle](https://github.com/giantswarm/aws-nth-bundle)
- [aws-pod-identity-webhook](https://github.com/giantswarm/aws-pod-identity-webhook)
- [cert-manager-crossplane-resources](https://github.com/giantswarm/cert-manager-crossplane-resources)
- [cilium-crossplane-resources](https://github.com/giantswarm/cilium-crossplane-resources)
- [cloud-provider-aws](https://github.com/giantswarm/aws-cloud-controller-manager-app)
- [cluster-autoscaler](https://github.com/giantswarm/cluster-autoscaler-app)
- [irsa-servicemonitors](https://github.com/giantswarm/irsa-servicemonitors-app)
- [karpenter-bundle](https://github.com/giantswarm/karpenter-bundle)
- [karpenter-nodepools](https://github.com/giantswarm/karpenter-nodepools)

### Azure

- [azure-cloud-controller-manager](https://github.com/giantswarm/azure-cloud-controller-manager-app)
- [azure-cloud-node-manager](https://github.com/giantswarm/azure-cloud-node-manager-app)
- [azuredisk-csi-driver](https://github.com/giantswarm/azuredisk-csi-driver-app)
- [azurefile-csi-driver](https://github.com/giantswarm/azurefile-csi-driver-app)

### VSphere

- [cloud-provider-vsphere](https://github.com/giantswarm/cloud-provider-vsphere-app)
- [kube-vip](https://github.com/giantswarm/kube-vip-app)
- [kube-vip-cloud-provider](https://github.com/giantswarm/kube-vip-cloud-provider-app)
- [vsphere-csi-driver](https://github.com/giantswarm/vsphere-csi-driver-app)

### Cloud Director

- [cloud-provider-cloud-director](https://github.com/giantswarm/cloud-provider-cloud-director-app)


## Further reading

- [Cluster upgrades]({{< relref "/tutorials/fleet-management/cluster-management/cluster-upgrades" >}}) explains how upgrades work and suggests some best practices to keep a cluster ready to upgrade.
