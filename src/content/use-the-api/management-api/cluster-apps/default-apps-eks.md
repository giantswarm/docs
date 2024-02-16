---
title: Default-Apps-Eks chart reference
linkTitle: default-apps-eks chart reference
description: |
  A Helm chart for default-apps-eks
weight: 100
menu:
  main:
    identifier: default-apps-eks
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/default-apps-eks
source_repository_ref: v0.5.1
---

The `default-apps-eks` chart templates all the components required for a Cluster API EKS cluster like External DNS or CoreDNS.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).



### Apps

Properties within the `.apps` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apps.capi-node-labeler` |**None**|**Type:** `object`|
| `apps.capi-node-labeler.appName` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.catalog` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.chartName` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.clusterValues` |**None**|**Type:** `object`|
| `apps.capi-node-labeler.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.enabled` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.capi-node-labeler.namespace` |**None**|**Type:** `string`|
| `apps.capi-node-labeler.version` |**None**|**Type:** `string`|
| `apps.certExporter` |**None**|**Type:** `object`|
| `apps.certExporter.appName` |**None**|**Type:** `string`|
| `apps.certExporter.catalog` |**None**|**Type:** `string`|
| `apps.certExporter.chartName` |**None**|**Type:** `string`|
| `apps.certExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.certExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.certExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.certExporter.dependsOn` |**None**|**Type:** `string`|
| `apps.certExporter.enabled` |**None**|**Type:** `boolean`|
| `apps.certExporter.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.certExporter.namespace` |**None**|**Type:** `string`|
| `apps.certExporter.version` |**None**|**Type:** `string`|
| `apps.certManager` |**None**|**Type:** `object`|
| `apps.certManager.appName` |**None**|**Type:** `string`|
| `apps.certManager.catalog` |**None**|**Type:** `string`|
| `apps.certManager.chartName` |**None**|**Type:** `string`|
| `apps.certManager.clusterValues` |**None**|**Type:** `object`|
| `apps.certManager.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.certManager.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.certManager.enabled` |**None**|**Type:** `boolean`|
| `apps.certManager.forceUpgrade` |**None**|**Type:** `boolean`|
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
| `apps.externalDns` |**None**|**Type:** `object`|
| `apps.externalDns.appName` |**None**|**Type:** `string`|
| `apps.externalDns.catalog` |**None**|**Type:** `string`|
| `apps.externalDns.chartName` |**None**|**Type:** `string`|
| `apps.externalDns.clusterValues` |**None**|**Type:** `object`|
| `apps.externalDns.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.externalDns.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.externalDns.enabled` |**None**|**Type:** `boolean`|
| `apps.externalDns.forceUpgrade` |**None**|**Type:** `boolean`|
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
| `apps.metricsServer.forceUpgrade` |**None**|**Type:** `boolean`|
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
| `apps.netExporter.enabled` |**None**|**Type:** `boolean`|
| `apps.netExporter.forceUpgrade` |**None**|**Type:** `boolean`|
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
| `apps.nodeExporter.forceUpgrade` |**None**|**Type:** `boolean`|
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
| `apps.observabilityBundle.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`|
| `apps.vpa` |**None**|**Type:** `object`|
| `apps.vpa.appName` |**None**|**Type:** `string`|
| `apps.vpa.catalog` |**None**|**Type:** `string`|
| `apps.vpa.chartName` |**None**|**Type:** `string`|
| `apps.vpa.clusterValues` |**None**|**Type:** `object`|
| `apps.vpa.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.vpa.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.vpa.dependsOn` |**None**|**Type:** `string`|
| `apps.vpa.enabled` |**None**|**Type:** `boolean`|
| `apps.vpa.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.vpa.namespace` |**None**|**Type:** `string`|
| `apps.vpa.version` |**None**|**Type:** `string`|

### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certManager` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.externalDns` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap` |**None**|**Type:** `object`|
| `userConfig.externalDns.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.metricsServer` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap` |**None**|**Type:** `object`|
| `userConfig.metricsServer.configMap.values` |**None**|**Types:** `object, string`|
| `userConfig.netExporter` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.netExporter.configMap.values` |**None**|**Types:** `object, string`|

### AWS settings

Properties within the `.providerSpecific` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `providerSpecific.awsAccountId` | **AWS account ID** - AWS Account ID of the AWSClusterRoleIdentity IAM role, recommendation is to leave this value empty as it will be automatically calculated. This value is needed for tests.|**Type:** `string`**Default:** `&#34;&#34;`|
| `providerSpecific.awsClusterRoleIdentityName` | **Cluster role identity name** - Name of an AWSClusterRoleIdentity object. Recommendation is to leave this value empty as it will be automatically calculated.|**Type:** `string`**Default:** `&#34;&#34;`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `awsAccoundID` |**None**|**Type:** `string`|
| `clusterName` |**None**|**Type:** `string`|
| `organization` |**None**|**Type:** `string`|




## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-eks)
