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

&lt;!-- DOCS_START --&gt;

### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certExporter.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.certManager` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.metricsServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.netExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.nodeExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.nodeExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.nodeExporter.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.vpa` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.vpa.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.vpa.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|

### Apps

Properties within the `.apps` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apps.certExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.certExporter.extraConfigs[*]` |**None**||
| `apps.certExporter.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.chartOperatorExtensions.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.chartOperatorExtensions.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.chartOperatorExtensions.extraConfigs[*]` |**None**||
| `apps.chartOperatorExtensions.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.chartOperatorExtensions.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.chartOperatorExtensions.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.clusterResources.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.clusterResources.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.clusterResources.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.clusterResources.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.clusterResources.extraConfigs[*]` |**None**||
| `apps.clusterResources.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.clusterResources.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.clusterResources.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.clusterResources.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.metricsServer.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.metricsServer.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.metricsServer.extraConfigs[*]` |**None**||
| `apps.metricsServer.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.netExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.netExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.netExporter.extraConfigs[*]` |**None**||
| `apps.netExporter.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.netExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.nodeExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.nodeExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.nodeExporter.extraConfigs[*]` |**None**||
| `apps.nodeExporter.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.nodeExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.nodeExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.observabilityBundle.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.observabilityBundle.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.observabilityBundle.extraConfigs[*]` |**None**||
| `apps.observabilityBundle.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleportKubeAgent.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleportKubeAgent.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleportKubeAgent.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleportKubeAgent.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.teleportKubeAgent.extraConfigs[*]` |**None**||
| `apps.teleportKubeAgent.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleportKubeAgent.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleportKubeAgent.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleportKubeAgent.version` |**None**|**Type:** `string`&lt;br/&gt;|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `clusterName` |**None**|**Type:** `string`&lt;br/&gt;|
| `managementCluster` |**None**|**Type:** `string`&lt;br/&gt;|
| `organization` |**None**|**Type:** `string`&lt;br/&gt;|

&lt;!-- DOCS_END --&gt;


## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-cloud-director)
