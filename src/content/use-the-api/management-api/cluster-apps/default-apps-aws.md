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



### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certManager` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`|
| `userConfig.certManager.configMap.values.controller` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values.controller.extraArgs` |**None**|**Type:** `array`|
| `userConfig.certManager.configMap.values.controller.extraArgs[*]` |**None**|**Type:** `string`|
| `userConfig.certManager.configMap.values.dns01RecursiveNameserversOnly` |**None**|**Type:** `boolean`|
| `userConfig.cluster-autoscaler` |**None**|**Type:** `object`|
| `userConfig.cluster-autoscaler.configMap` |**None**|**Type:** `object`|
| `userConfig.cluster-autoscaler.configMap.values` |**None**|**Type:** `object`|
| `userConfig.cluster-autoscaler.configMap.values.serviceAccount` |**None**|**Type:** `object`|
| `userConfig.cluster-autoscaler.configMap.values.serviceAccount.annotations` |**None**|**Type:** `object`|
| `userConfig.cluster-autoscaler.configMap.values.serviceAccount.annotations.eks.amazonaws.com/role-arn` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.cacertpath` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.certpath` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.hostPath` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.keypath` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.etcd.prefix` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.events` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values.events.prefix` |**None**|**Type:** `string`|
| `userConfig.externalDns` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values.annotationFilter` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.aws` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values.aws.batchChangeInterval` |**None**|**Type:** `null`|
| `userConfig.externalDns.configMap.values.aws.irsa` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`|
| `userConfig.externalDns.configMap.values.domainFilters` |**None**|**Type:** `array`|
| `userConfig.externalDns.configMap.values.domainFilters[*]` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.extraArgs` |**None**|**Type:** `array`|
| `userConfig.externalDns.configMap.values.extraArgs[*]` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.provider` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.serviceAccount` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values.serviceAccount.annotations` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values.serviceAccount.annotations.eks.amazonaws.com/role-arn` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.sources` |**None**|**Type:** `array`|
| `userConfig.externalDns.configMap.values.sources[*]` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.txtOwnerId` |**None**|**Type:** `string`|
| `userConfig.externalDns.configMap.values.txtPrefix` |**None**|**Type:** `string`|
| `userConfig.metricsServer` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap.values` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`|
| `userConfig.netExporter` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap.values` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap.values.NetExporter` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap.values.NetExporter.NTPServers` |**None**|**Type:** `string`|
| `userConfig.netExporter.configMap.values.ciliumNetworkPolicy` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap.values.ciliumNetworkPolicy.enabled` |**None**|**Type:** `boolean`|

### Apps

Properties within the `.apps` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apps.aws-pod-identity-webhook` |**None**|**Type:** `object`|
| `apps.aws-pod-identity-webhook.appName` |**None**|**Type:** `string`|
| `apps.aws-pod-identity-webhook.catalog` |**None**|**Type:** `string`|
| `apps.aws-pod-identity-webhook.chartName` |**None**|**Type:** `string`|
| `apps.aws-pod-identity-webhook.clusterValues` |**None**|**Type:** `object`|
| `apps.aws-pod-identity-webhook.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.aws-pod-identity-webhook.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.aws-pod-identity-webhook.dependsOn` |**None**|**Type:** `string`|
| `apps.aws-pod-identity-webhook.enabled` |**None**|**Type:** `boolean`|
| `apps.aws-pod-identity-webhook.namespace` |**None**|**Type:** `string`|
| `apps.aws-pod-identity-webhook.version` |**None**|**Type:** `string`|
| `apps.capi-node-labeler` |**None**|**Type:** `object`|
| `apps.capi-node-labeler.appName` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.catalog` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.chartName` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.clusterValues` |**None**|**Type:** `object`|
| `apps.capi-node-labeler.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.enabled` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.namespace` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.version` |**None**|**Type:** `string`|
| `apps.certExporter` |**None**|**Type:** `object`|
| `apps.certExporter.appName` |**None**|**Type:** `string`|
| `apps.certExporter.catalog` |**None**|**Type:** `string`|
| `apps.certExporter.chartName` |**None**|**Type:** `string`|
| `apps.certExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.certExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.certExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.certExporter.enabled` |**None**|**Type:** `boolean`|
| `apps.certExporter.namespace` |**None**|**Type:** `string`|
| `apps.certExporter.version` |**None**|**Type:** `string`|
| `apps.certManager` |**None**|**Type:** `object`|
| `apps.certManager.appName` |**None**|**Type:** `string`|
| `apps.certManager.catalog` |**None**|**Type:** `string`|
| `apps.certManager.chartName` |**None**|**Type:** `string`|
| `apps.certManager.clusterValues` |**None**|**Type:** `object`|
| `apps.certManager.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.certManager.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.certManager.dependsOn` |**None**|**Type:** `string`|
| `apps.certManager.enabled` |**None**|**Type:** `boolean`|
| `apps.certManager.namespace` |**None**|**Type:** `string`|
| `apps.certManager.version` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions` |**None**|**Type:** `object`|
| `apps.chartOperatorExtensions.appName` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.catalog` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.chartName` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.clusterValues` |**None**|**Type:** `object`|
| `apps.chartOperatorExtensions.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.dependsOn` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.enabled` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.namespace` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.version` |**None**|**Type:** `string`|
| `apps.cluster-autoscaler` |**None**|**Type:** `object`|
| `apps.cluster-autoscaler.appName` |**None**|**Type:** `string`|
| `apps.cluster-autoscaler.catalog` |**None**|**Type:** `string`|
| `apps.cluster-autoscaler.chartName` |**None**|**Type:** `string`|
| `apps.cluster-autoscaler.clusterValues` |**None**|**Type:** `object`|
| `apps.cluster-autoscaler.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.cluster-autoscaler.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.cluster-autoscaler.enabled` |**None**|**Type:** `boolean`|
| `apps.cluster-autoscaler.namespace` |**None**|**Type:** `string`|
| `apps.cluster-autoscaler.version` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`|
| `apps.etcdKubernetesResourceCountExporter.appName` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.catalog` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.chartName` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.etcdKubernetesResourceCountExporter.enabled` |**None**|**Type:** `boolean`|
| `apps.etcdKubernetesResourceCountExporter.namespace` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.version` |**None**|**Type:** `string`|
| `apps.externalDns` |**None**|**Type:** `object`|
| `apps.externalDns.appName` |**None**|**Type:** `string`|
| `apps.externalDns.catalog` |**None**|**Type:** `string`|
| `apps.externalDns.chartName` |**None**|**Type:** `string`|
| `apps.externalDns.clusterValues` |**None**|**Type:** `object`|
| `apps.externalDns.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.externalDns.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.externalDns.enabled` |**None**|**Type:** `boolean`|
| `apps.externalDns.namespace` |**None**|**Type:** `string`|
| `apps.externalDns.version` |**None**|**Type:** `string`|
| `apps.metricsServer` |**None**|**Type:** `object`|
| `apps.metricsServer.appName` |**None**|**Type:** `string`|
| `apps.metricsServer.catalog` |**None**|**Type:** `string`|
| `apps.metricsServer.chartName` |**None**|**Type:** `string`|
| `apps.metricsServer.clusterValues` |**None**|**Type:** `object`|
| `apps.metricsServer.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.metricsServer.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.metricsServer.enabled` |**None**|**Type:** `boolean`|
| `apps.metricsServer.namespace` |**None**|**Type:** `string`|
| `apps.metricsServer.version` |**None**|**Type:** `string`|
| `apps.netExporter` |**None**|**Type:** `object`|
| `apps.netExporter.appName` |**None**|**Type:** `string`|
| `apps.netExporter.catalog` |**None**|**Type:** `string`|
| `apps.netExporter.chartName` |**None**|**Type:** `string`|
| `apps.netExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.netExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.netExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.netExporter.enabled` |**None**|**Type:** `boolean`|
| `apps.netExporter.namespace` |**None**|**Type:** `string`|
| `apps.netExporter.version` |**None**|**Type:** `string`|
| `apps.nodeExporter` |**None**|**Type:** `object`|
| `apps.nodeExporter.appName` |**None**|**Type:** `string`|
| `apps.nodeExporter.catalog` |**None**|**Type:** `string`|
| `apps.nodeExporter.chartName` |**None**|**Type:** `string`|
| `apps.nodeExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.nodeExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.enabled` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.namespace` |**None**|**Type:** `string`|
| `apps.nodeExporter.version` |**None**|**Type:** `string`|
| `apps.observabilityBundle` |**None**|**Type:** `object`|
| `apps.observabilityBundle.appName` |**None**|**Type:** `string`|
| `apps.observabilityBundle.catalog` |**None**|**Type:** `string`|
| `apps.observabilityBundle.chartName` |**None**|**Type:** `string`|
| `apps.observabilityBundle.clusterValues` |**None**|**Type:** `object`|
| `apps.observabilityBundle.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.enabled` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`|
| `apps.securityBundle` |**None**|**Type:** `object`|
| `apps.securityBundle.appName` |**None**|**Type:** `string`|
| `apps.securityBundle.catalog` |**None**|**Type:** `string`|
| `apps.securityBundle.chartName` |**None**|**Type:** `string`|
| `apps.securityBundle.clusterValues` |**None**|**Type:** `object`|
| `apps.securityBundle.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.securityBundle.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.securityBundle.namespace` |**None**|**Type:** `string`|
| `apps.securityBundle.version` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent` |**None**|**Type:** `object`|
| `apps.teleport-kube-agent.appName` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.catalog` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.chartName` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.clusterValues` |**None**|**Type:** `object`|
| `apps.teleport-kube-agent.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.teleport-kube-agent.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.teleport-kube-agent.enabled` |**None**|**Type:** `boolean`|
| `apps.teleport-kube-agent.extraConfigs` |**None**|**Type:** `array`|
| `apps.teleport-kube-agent.extraConfigs[*]` |**None**|**Type:** `object`|
| `apps.teleport-kube-agent.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.extraConfigs[*].namespace` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.teleport-kube-agent.namespace` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.version` |**None**|**Type:** `string`|
| `apps.vpa` |**None**|**Type:** `object`|
| `apps.vpa.appName` |**None**|**Type:** `string`|
| `apps.vpa.catalog` |**None**|**Type:** `string`|
| `apps.vpa.chartName` |**None**|**Type:** `string`|
| `apps.vpa.clusterValues` |**None**|**Type:** `object`|
| `apps.vpa.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.vpa.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.vpa.dependsOn` |**None**|**Type:** `string`|
| `apps.vpa.enabled` |**None**|**Type:** `boolean`|
| `apps.vpa.namespace` |**None**|**Type:** `string`|
| `apps.vpa.version` |**None**|**Type:** `string`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `clusterName` |**None**|**Type:** `string`|
| `organization` |**None**|**Type:** `string`|




## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-aws)
