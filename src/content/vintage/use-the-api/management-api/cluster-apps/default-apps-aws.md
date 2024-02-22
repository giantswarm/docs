---
title: Default-Apps-Aws chart reference
linkTitle: default-apps-aws chart reference
description: |
  A Helm chart for default-apps-aws
weight: 100
menu:
  main:
    identifier: default-apps-aws
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/default-apps-aws
source_repository_ref: v0.48.0
---

The `default-apps-aws` chart templates all the components required for a Cluster API AWS cluster like External DNS or CoreDNS.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

&lt;!-- DOCS_START --&gt;

### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certManager` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `userConfig.certManager.configMap.values.controller` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values.controller.extraArgs` |**None**|**Type:** `array`&lt;br/&gt;|
| `userConfig.certManager.configMap.values.controller.extraArgs[*]` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.certManager.configMap.values.dns01RecursiveNameserversOnly` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `userConfig.cluster-autoscaler` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.cluster-autoscaler.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.cluster-autoscaler.configMap.values` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.cluster-autoscaler.configMap.values.serviceAccount` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.cluster-autoscaler.configMap.values.serviceAccount.annotations` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.cluster-autoscaler.configMap.values.serviceAccount.annotations.eks.amazonaws.com/role-arn` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.cacertpath` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.certpath` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.hostPath` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.keypath` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.prefix` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.events` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.events.prefix` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.annotationFilter` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.aws` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.aws.batchChangeInterval` |**None**|**Type:** `null`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.aws.irsa` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.domainFilters` |**None**|**Type:** `array`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.domainFilters[*]` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.extraArgs` |**None**|**Type:** `array`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.extraArgs[*]` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.provider` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.serviceAccount` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.serviceAccount.annotations` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.serviceAccount.annotations.eks.amazonaws.com/role-arn` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.sources` |**None**|**Type:** `array`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.sources[*]` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.txtOwnerId` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values.txtPrefix` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.metricsServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap.values` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `userConfig.netExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values.NetExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values.NetExporter.NTPServers` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|

### Apps

Properties within the `.apps` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apps.aws-pod-identity-webhook` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.aws-pod-identity-webhook.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.capi-node-labeler.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.capi-node-labeler.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certManager.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certManager.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certManager.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certManager.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certManager.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.chartOperatorExtensions.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.chartOperatorExtensions.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.cluster-autoscaler` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.cluster-autoscaler.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.cluster-autoscaler.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.cluster-autoscaler.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.cluster-autoscaler.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.cluster-autoscaler.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.cluster-autoscaler.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.cluster-autoscaler.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.cluster-autoscaler.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.cluster-autoscaler.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.externalDns.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.externalDns.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.externalDns.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.externalDns.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.externalDns.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.metricsServer.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.metricsServer.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.netExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.netExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.nodeExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.nodeExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.observabilityBundle.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.observabilityBundle.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.securityBundle` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.securityBundle.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.securityBundle.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.securityBundle.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.securityBundle.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.securityBundle.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.securityBundle.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.securityBundle.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.securityBundle.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleport-kube-agent.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleport-kube-agent.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleport-kube-agent.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleport-kube-agent.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs[*].namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleport-kube-agent.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.vpa.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.vpa.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.version` |**None**|**Type:** `string`&lt;br/&gt;|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `clusterName` |**None**|**Type:** `string`&lt;br/&gt;|
| `organization` |**None**|**Type:** `string`&lt;br/&gt;|

&lt;!-- DOCS_END --&gt;


## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-aws)
