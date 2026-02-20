---
title: default-apps-eks chart reference
linkTitle: default-apps-eks
description:  A Helm chart for default-apps-eks; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: default-apps-eks
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for default-apps-eks?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/default-apps-eks
source_repository_ref: v0.5.1
---

The `default-apps-eks` chart templates all the standard apps deployed to AWS EKS clusters, like External DNS and CoreDNS.

## Chart configuration reference

###  {#}

---

`.apps.capi-node-labeler`

**Type:** `object`

---

`.apps.capi-node-labeler.appName`

**Type:** `string`

---

`.apps.capi-node-labeler.catalog`

**Type:** `string`

---

`.apps.capi-node-labeler.chartName`

**Type:** `string`

---

`.apps.capi-node-labeler.clusterValues`

**Type:** `object`

---

`.apps.capi-node-labeler.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.capi-node-labeler.clusterValues.secret`

**Type:** `boolean`

---

`.apps.capi-node-labeler.enabled`

**Type:** `boolean`

---

`.apps.capi-node-labeler.forceUpgrade`

**Type:** `boolean`

---

`.apps.capi-node-labeler.namespace`

**Type:** `string`

---

`.apps.capi-node-labeler.version`

**Type:** `string`

---

`.apps.certExporter`

**Type:** `object`

---

`.apps.certExporter.appName`

**Type:** `string`

---

`.apps.certExporter.catalog`

**Type:** `string`

---

`.apps.certExporter.chartName`

**Type:** `string`

---

`.apps.certExporter.clusterValues`

**Type:** `object`

---

`.apps.certExporter.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.certExporter.clusterValues.secret`

**Type:** `boolean`

---

`.apps.certExporter.dependsOn`

**Type:** `string`

---

`.apps.certExporter.enabled`

**Type:** `boolean`

---

`.apps.certExporter.forceUpgrade`

**Type:** `boolean`

---

`.apps.certExporter.namespace`

**Type:** `string`

---

`.apps.certExporter.version`

**Type:** `string`

---

`.apps.certManager`

**Type:** `object`

---

`.apps.certManager.appName`

**Type:** `string`

---

`.apps.certManager.catalog`

**Type:** `string`

---

`.apps.certManager.chartName`

**Type:** `string`

---

`.apps.certManager.clusterValues`

**Type:** `object`

---

`.apps.certManager.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.certManager.clusterValues.secret`

**Type:** `boolean`

---

`.apps.certManager.enabled`

**Type:** `boolean`

---

`.apps.certManager.forceUpgrade`

**Type:** `boolean`

---

`.apps.certManager.namespace`

**Type:** `string`

---

`.apps.certManager.version`

**Type:** `string`

---

`.apps.chartOperatorExtensions`

**Type:** `object`

---

`.apps.chartOperatorExtensions.appName`

**Type:** `string`

---

`.apps.chartOperatorExtensions.catalog`

**Type:** `string`

---

`.apps.chartOperatorExtensions.chartName`

**Type:** `string`

---

`.apps.chartOperatorExtensions.clusterValues`

**Type:** `object`

---

`.apps.chartOperatorExtensions.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.chartOperatorExtensions.clusterValues.secret`

**Type:** `boolean`

---

`.apps.chartOperatorExtensions.dependsOn`

**Type:** `string`

---

`.apps.chartOperatorExtensions.enabled`

**Type:** `boolean`

---

`.apps.chartOperatorExtensions.namespace`

**Type:** `string`

---

`.apps.chartOperatorExtensions.version`

**Type:** `string`

---

`.apps.externalDns`

**Type:** `object`

---

`.apps.externalDns.appName`

**Type:** `string`

---

`.apps.externalDns.catalog`

**Type:** `string`

---

`.apps.externalDns.chartName`

**Type:** `string`

---

`.apps.externalDns.clusterValues`

**Type:** `object`

---

`.apps.externalDns.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.externalDns.clusterValues.secret`

**Type:** `boolean`

---

`.apps.externalDns.enabled`

**Type:** `boolean`

---

`.apps.externalDns.forceUpgrade`

**Type:** `boolean`

---

`.apps.externalDns.namespace`

**Type:** `string`

---

`.apps.externalDns.version`

**Type:** `string`

---

`.apps.metricsServer`

**Type:** `object`

---

`.apps.metricsServer.appName`

**Type:** `string`

---

`.apps.metricsServer.catalog`

**Type:** `string`

---

`.apps.metricsServer.chartName`

**Type:** `string`

---

`.apps.metricsServer.clusterValues`

**Type:** `object`

---

`.apps.metricsServer.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.metricsServer.clusterValues.secret`

**Type:** `boolean`

---

`.apps.metricsServer.enabled`

**Type:** `boolean`

---

`.apps.metricsServer.forceUpgrade`

**Type:** `boolean`

---

`.apps.metricsServer.namespace`

**Type:** `string`

---

`.apps.metricsServer.version`

**Type:** `string`

---

`.apps.netExporter`

**Type:** `object`

---

`.apps.netExporter.appName`

**Type:** `string`

---

`.apps.netExporter.catalog`

**Type:** `string`

---

`.apps.netExporter.chartName`

**Type:** `string`

---

`.apps.netExporter.clusterValues`

**Type:** `object`

---

`.apps.netExporter.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.netExporter.clusterValues.secret`

**Type:** `boolean`

---

`.apps.netExporter.dependsOn`

**Type:** `string`

---

`.apps.netExporter.enabled`

**Type:** `boolean`

---

`.apps.netExporter.forceUpgrade`

**Type:** `boolean`

---

`.apps.netExporter.namespace`

**Type:** `string`

---

`.apps.netExporter.version`

**Type:** `string`

---

`.apps.nodeExporter`

**Type:** `object`

---

`.apps.nodeExporter.appName`

**Type:** `string`

---

`.apps.nodeExporter.catalog`

**Type:** `string`

---

`.apps.nodeExporter.chartName`

**Type:** `string`

---

`.apps.nodeExporter.clusterValues`

**Type:** `object`

---

`.apps.nodeExporter.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.nodeExporter.clusterValues.secret`

**Type:** `boolean`

---

`.apps.nodeExporter.enabled`

**Type:** `boolean`

---

`.apps.nodeExporter.forceUpgrade`

**Type:** `boolean`

---

`.apps.nodeExporter.namespace`

**Type:** `string`

---

`.apps.nodeExporter.version`

**Type:** `string`

---

`.apps.observabilityBundle`

**Type:** `object`

---

`.apps.observabilityBundle.appName`

**Type:** `string`

---

`.apps.observabilityBundle.catalog`

**Type:** `string`

---

`.apps.observabilityBundle.chartName`

**Type:** `string`

---

`.apps.observabilityBundle.clusterValues`

**Type:** `object`

---

`.apps.observabilityBundle.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.observabilityBundle.clusterValues.secret`

**Type:** `boolean`

---

`.apps.observabilityBundle.enabled`

**Type:** `boolean`

---

`.apps.observabilityBundle.forceUpgrade`

**Type:** `boolean`

---

`.apps.observabilityBundle.inCluster`

**Type:** `boolean`

---

`.apps.observabilityBundle.namespace`

**Type:** `string`

---

`.apps.observabilityBundle.version`

**Type:** `string`

---

`.apps.vpa`

**Type:** `object`

---

`.apps.vpa.appName`

**Type:** `string`

---

`.apps.vpa.catalog`

**Type:** `string`

---

`.apps.vpa.chartName`

**Type:** `string`

---

`.apps.vpa.clusterValues`

**Type:** `object`

---

`.apps.vpa.clusterValues.configMap`

**Type:** `boolean`

---

`.apps.vpa.clusterValues.secret`

**Type:** `boolean`

---

`.apps.vpa.dependsOn`

**Type:** `string`

---

`.apps.vpa.enabled`

**Type:** `boolean`

---

`.apps.vpa.forceUpgrade`

**Type:** `boolean`

---

`.apps.vpa.namespace`

**Type:** `string`

---

`.apps.vpa.version`

**Type:** `string`

###  {#}

---

`.userConfig.certManager`

**Type:** `object`

---

`.userConfig.certManager.configMap`

**Type:** `object`

---

`.userConfig.certManager.configMap.values`

**Types:** `string`, `object`

---

`.userConfig.externalDns`

**Type:** `object`

---

`.userConfig.externalDns.configMap`

**Type:** `object`

---

`.userConfig.externalDns.configMap.values`

**Types:** `string`, `object`

---

`.userConfig.metricsServer`

**Type:** `object`

---

`.userConfig.metricsServer.configMap`

**Type:** `object`

---

`.userConfig.metricsServer.configMap.values`

**Types:** `string`, `object`

---

`.userConfig.netExporter`

**Type:** `object`

---

`.userConfig.netExporter.configMap`

**Type:** `object`

---

`.userConfig.netExporter.configMap.values`

**Types:** `string`, `object`

### AWS settings {#aws-settings}

---

`.providerSpecific.awsAccountId`

**Type:** `string`

**AWS account ID**

AWS Account ID of the AWSClusterRoleIdentity IAM role, recommendation is to leave this value empty as it will be automatically calculated. This value is needed for tests.

**Value pattern:** `^[0-9]{0,12}$`

**Default:** `""`

---

`.providerSpecific.awsClusterRoleIdentityName`

**Type:** `string`

**Cluster role identity name**

Name of an AWSClusterRoleIdentity object. Recommendation is to leave this value empty as it will be automatically calculated.

**Default:** `""`

### Other {#other}

---

`.awsAccoundID`

**Type:** `string`

---

`.clusterName`

**Type:** `string`

---

`.organization`

**Type:** `string`

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-eks)
