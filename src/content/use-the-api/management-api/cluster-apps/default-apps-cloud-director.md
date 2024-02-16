---
title: Default-Apps-Cloud-Director chart reference
linkTitle: default-apps-cloud-director chart reference
description: |
  A Helm chart which defines the pre-installed apps in all Giant Swarm Cloud Director (VCD) clusters
weight: 100
menu:
  main:
    identifier: default-apps-cloud-director
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/default-apps-cloud-director
source_repository_ref: v0.7.3
---

The `default-apps-cloud-director` chart templates all the components required for a Cluster API VMware cluster like External DNS or CoreDNS.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).



### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certExporter` |**None**|**Type:** `object`|
| `userConfig.certExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.certExporter.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.certManager` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.metricsServer` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.netExporter` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.nodeExporter` |**None**|**Type:** `object`|
| `userConfig.nodeExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.nodeExporter.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.vpa` |**None**|**Type:** `object`|
| `userConfig.vpa.configMap` |**None**|**Type:** `object`|
| `userConfig.vpa.configMap.values` |**None**|**Types:** `object, string`|

### Apps

Properties within the `.apps` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apps.certExporter` |**None**|**Type:** `object`|
| `apps.certExporter.appName` |**None**|**Type:** `string`|
| `apps.certExporter.catalog` |**None**|**Type:** `string`|
| `apps.certExporter.chartName` |**None**|**Type:** `string`|
| `apps.certExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.certExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.certExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.certExporter.dependsOn` |**None**|**Type:** `string`|
| `apps.certExporter.extraConfigs` |**None**|**Type:** `array`|
| `apps.certExporter.extraConfigs[*]` |**None**||
| `apps.certExporter.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.certExporter.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.certExporter.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.certExporter.inCluster` |**None**|**Type:** `boolean`|
| `apps.certExporter.namespace` |**None**|**Type:** `string`|
| `apps.certExporter.version` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions` |**None**|**Type:** `object`|
| `apps.chartOperatorExtensions.appName` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.catalog` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.chartName` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.clusterValues` |**None**|**Type:** `object`|
| `apps.chartOperatorExtensions.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.dependsOn` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.extraConfigs` |**None**|**Type:** `array`|
| `apps.chartOperatorExtensions.extraConfigs[*]` |**None**||
| `apps.chartOperatorExtensions.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.inCluster` |**None**|**Type:** `boolean`|
| `apps.chartOperatorExtensions.namespace` |**None**|**Type:** `string`|
| `apps.chartOperatorExtensions.version` |**None**|**Type:** `string`|
| `apps.clusterResources` |**None**|**Type:** `object`|
| `apps.clusterResources.appName` |**None**|**Type:** `string`|
| `apps.clusterResources.catalog` |**None**|**Type:** `string`|
| `apps.clusterResources.chartName` |**None**|**Type:** `string`|
| `apps.clusterResources.clusterValues` |**None**|**Type:** `object`|
| `apps.clusterResources.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.clusterResources.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.clusterResources.dependsOn` |**None**|**Type:** `string`|
| `apps.clusterResources.extraConfigs` |**None**|**Type:** `array`|
| `apps.clusterResources.extraConfigs[*]` |**None**||
| `apps.clusterResources.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.clusterResources.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.clusterResources.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.clusterResources.inCluster` |**None**|**Type:** `boolean`|
| `apps.clusterResources.namespace` |**None**|**Type:** `string`|
| `apps.clusterResources.version` |**None**|**Type:** `string`|
| `apps.metricsServer` |**None**|**Type:** `object`|
| `apps.metricsServer.appName` |**None**|**Type:** `string`|
| `apps.metricsServer.catalog` |**None**|**Type:** `string`|
| `apps.metricsServer.chartName` |**None**|**Type:** `string`|
| `apps.metricsServer.clusterValues` |**None**|**Type:** `object`|
| `apps.metricsServer.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.metricsServer.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.metricsServer.dependsOn` |**None**|**Type:** `string`|
| `apps.metricsServer.extraConfigs` |**None**|**Type:** `array`|
| `apps.metricsServer.extraConfigs[*]` |**None**||
| `apps.metricsServer.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.metricsServer.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.metricsServer.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.metricsServer.inCluster` |**None**|**Type:** `boolean`|
| `apps.metricsServer.namespace` |**None**|**Type:** `string`|
| `apps.metricsServer.version` |**None**|**Type:** `string`|
| `apps.netExporter` |**None**|**Type:** `object`|
| `apps.netExporter.appName` |**None**|**Type:** `string`|
| `apps.netExporter.catalog` |**None**|**Type:** `string`|
| `apps.netExporter.chartName` |**None**|**Type:** `string`|
| `apps.netExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.netExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.netExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.netExporter.dependsOn` |**None**|**Type:** `string`|
| `apps.netExporter.extraConfigs` |**None**|**Type:** `array`|
| `apps.netExporter.extraConfigs[*]` |**None**||
| `apps.netExporter.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.netExporter.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.netExporter.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.netExporter.inCluster` |**None**|**Type:** `boolean`|
| `apps.netExporter.namespace` |**None**|**Type:** `string`|
| `apps.netExporter.version` |**None**|**Type:** `string`|
| `apps.nodeExporter` |**None**|**Type:** `object`|
| `apps.nodeExporter.appName` |**None**|**Type:** `string`|
| `apps.nodeExporter.catalog` |**None**|**Type:** `string`|
| `apps.nodeExporter.chartName` |**None**|**Type:** `string`|
| `apps.nodeExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.nodeExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.dependsOn` |**None**|**Type:** `string`|
| `apps.nodeExporter.extraConfigs` |**None**|**Type:** `array`|
| `apps.nodeExporter.extraConfigs[*]` |**None**||
| `apps.nodeExporter.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.nodeExporter.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.nodeExporter.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.inCluster` |**None**|**Type:** `boolean`|
| `apps.nodeExporter.namespace` |**None**|**Type:** `string`|
| `apps.nodeExporter.version` |**None**|**Type:** `string`|
| `apps.observabilityBundle` |**None**|**Type:** `object`|
| `apps.observabilityBundle.appName` |**None**|**Type:** `string`|
| `apps.observabilityBundle.catalog` |**None**|**Type:** `string`|
| `apps.observabilityBundle.chartName` |**None**|**Type:** `string`|
| `apps.observabilityBundle.clusterValues` |**None**|**Type:** `object`|
| `apps.observabilityBundle.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.dependsOn` |**None**|**Type:** `string`|
| `apps.observabilityBundle.extraConfigs` |**None**|**Type:** `array`|
| `apps.observabilityBundle.extraConfigs[*]` |**None**||
| `apps.observabilityBundle.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.observabilityBundle.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.observabilityBundle.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent` |**None**|**Type:** `object`|
| `apps.teleportKubeAgent.appName` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.catalog` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.chartName` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.clusterValues` |**None**|**Type:** `object`|
| `apps.teleportKubeAgent.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.teleportKubeAgent.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.teleportKubeAgent.dependsOn` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.extraConfigs` |**None**|**Type:** `array`|
| `apps.teleportKubeAgent.extraConfigs[*]` |**None**||
| `apps.teleportKubeAgent.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.extraConfigs[*].name` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.teleportKubeAgent.inCluster` |**None**|**Type:** `boolean`|
| `apps.teleportKubeAgent.namespace` |**None**|**Type:** `string`|
| `apps.teleportKubeAgent.version` |**None**|**Type:** `string`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `clusterName` |**None**|**Type:** `string`|
| `managementCluster` |**None**|**Type:** `string`|
| `organization` |**None**|**Type:** `string`|




## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-cloud-director)
