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

&lt;!-- DOCS_START --&gt;

### Apps

Properties within the `.apps` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apps.capi-node-labeler` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.capi-node-labeler.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.capi-node-labeler.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.capi-node-labeler.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.capi-node-labeler.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certManager.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.certManager.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.certManager.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certManager.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certManager.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.certManager.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
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
| `apps.externalDns` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.externalDns.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.externalDns.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.externalDns.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.externalDns.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.externalDns.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.externalDns.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
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
| `apps.metricsServer.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
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
| `apps.netExporter.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.netExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
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
| `apps.nodeExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
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
| `apps.observabilityBundle.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.vpa.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.vpa.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.dependsOn` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.enabled` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.version` |**None**|**Type:** `string`&lt;br/&gt;|

### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certManager` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.externalDns` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.externalDns.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.metricsServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.metricsServer.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|
| `userConfig.netExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.netExporter.configMap.values` |**None**|**Types:** `object, string`&lt;br/&gt;|

### AWS settings

Properties within the `.providerSpecific` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `providerSpecific.awsAccountId` | **AWS account ID** - AWS Account ID of the AWSClusterRoleIdentity IAM role, recommendation is to leave this value empty as it will be automatically calculated. This value is needed for tests.|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[0-9]{0,12}$`&lt;br/&gt;**Default:** `&#34;&#34;`|
| `providerSpecific.awsClusterRoleIdentityName` | **Cluster role identity name** - Name of an AWSClusterRoleIdentity object. Recommendation is to leave this value empty as it will be automatically calculated.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;&#34;`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `awsAccoundID` |**None**|**Type:** `string`&lt;br/&gt;|
| `clusterName` |**None**|**Type:** `string`&lt;br/&gt;|
| `organization` |**None**|**Type:** `string`&lt;br/&gt;|

&lt;!-- DOCS_END --&gt;


## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-eks)
