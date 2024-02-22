---
title: Default-Apps-Azure chart reference
linkTitle: default-apps-azure chart reference
description: |
  A Helm chart defining the preinstalled apps running in all Giant Swarm Azure clusters.
weight: 100
menu:
  main:
    identifier: default-apps-azure
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/default-apps-azure
source_repository_ref: v0.8.3
---

The `default-apps-azure` chart templates all the components required for a Cluster API Azure cluster like External DNS or CoreDNS.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

&lt;!-- DOCS_START --&gt;

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
| `apps.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.etcdKubernetesResourceCountExporter.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.external-dns` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.external-dns.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.external-dns.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.external-dns.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.external-dns.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.external-dns.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.external-dns.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.external-dns.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.external-dns.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.external-dns.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.metricsServer.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.metricsServer.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.metricsServer.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.metricsServer.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
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
| `apps.observabilityBundle.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleport-kube-agent.appName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.catalog` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.chartName` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.clusterValues` |**None**|**Type:** `object`&lt;br/&gt;|
| `apps.teleport-kube-agent.clusterValues.configMap` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleport-kube-agent.clusterValues.secret` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs` |**None**|**Type:** `array`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs[*]` |**None**||
| `apps.teleport-kube-agent.extraConfigs[*].kind` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.teleport-kube-agent.extraConfigs[*].name` |**None**|**Type:** `string`&lt;br/&gt;|
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
| `apps.vpa.forceUpgrade` |**None**|**Type:** `boolean`&lt;br/&gt;|
| `apps.vpa.namespace` |**None**|**Type:** `string`&lt;br/&gt;|
| `apps.vpa.version` |**None**|**Type:** `string`&lt;br/&gt;|

### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certManager` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.certManager.configMap.values` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values` |**None**|**Type:** `string`&lt;br/&gt;|
| `userConfig.external-dns` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.external-dns.configMap` |**None**|**Type:** `object`&lt;br/&gt;|
| `userConfig.external-dns.configMap.values` |**None**|**Type:** `string`&lt;br/&gt;|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `clusterName` |**None**|**Type:** `string`&lt;br/&gt;|
| `organization` |**None**|**Type:** `string`&lt;br/&gt;|

&lt;!-- DOCS_END --&gt;


## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-azure)
