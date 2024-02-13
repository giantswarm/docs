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
| `apps.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`|
| `apps.etcdKubernetesResourceCountExporter.appName` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.catalog` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.chartName` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.clusterValues` |**None**|**Type:** `object`|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.etcdKubernetesResourceCountExporter.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.etcdKubernetesResourceCountExporter.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.etcdKubernetesResourceCountExporter.namespace` |**None**|**Type:** `string`|
| `apps.etcdKubernetesResourceCountExporter.version` |**None**|**Type:** `string`|
| `apps.external-dns` |**None**|**Type:** `object`|
| `apps.external-dns.appName` |**None**|**Type:** `string`|
| `apps.external-dns.catalog` |**None**|**Type:** `string`|
| `apps.external-dns.chartName` |**None**|**Type:** `string`|
| `apps.external-dns.clusterValues` |**None**|**Type:** `object`|
| `apps.external-dns.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.external-dns.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.external-dns.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.external-dns.namespace` |**None**|**Type:** `string`|
| `apps.external-dns.version` |**None**|**Type:** `string`|
| `apps.metricsServer` |**None**|**Type:** `object`|
| `apps.metricsServer.appName` |**None**|**Type:** `string`|
| `apps.metricsServer.catalog` |**None**|**Type:** `string`|
| `apps.metricsServer.chartName` |**None**|**Type:** `string`|
| `apps.metricsServer.clusterValues` |**None**|**Type:** `object`|
| `apps.metricsServer.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.metricsServer.clusterValues.secret` |**None**|**Type:** `boolean`|
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
| `apps.observabilityBundle.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.inCluster` |**None**|**Type:** `boolean`|
| `apps.observabilityBundle.namespace` |**None**|**Type:** `string`|
| `apps.observabilityBundle.version` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent` |**None**|**Type:** `object`|
| `apps.teleport-kube-agent.appName` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.catalog` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.chartName` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.clusterValues` |**None**|**Type:** `object`|
| `apps.teleport-kube-agent.clusterValues.configMap` |**None**|**Type:** `boolean`|
| `apps.teleport-kube-agent.clusterValues.secret` |**None**|**Type:** `boolean`|
| `apps.teleport-kube-agent.extraConfigs` |**None**|**Type:** `array`|
| `apps.teleport-kube-agent.extraConfigs[*]` |**None**||
| `apps.teleport-kube-agent.extraConfigs[*].kind` |**None**|**Type:** `string`|
| `apps.teleport-kube-agent.extraConfigs[*].name` |**None**|**Type:** `string`|
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
| `apps.vpa.forceUpgrade` |**None**|**Type:** `boolean`|
| `apps.vpa.namespace` |**None**|**Type:** `string`|
| `apps.vpa.version` |**None**|**Type:** `string`|

### User Config

Properties within the `.userConfig` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `userConfig.certManager` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap` |**None**|**Type:** `object`|
| `userConfig.certManager.configMap.values` |**None**|**Type:** `string`|
| `userConfig.etcdKubernetesResourceCountExporter` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap` |**None**|**Type:** `object`|
| `userConfig.etcdKubernetesResourceCountExporter.configMap.values` |**None**|**Type:** `string`|
| `userConfig.external-dns` |**None**|**Type:** `object`|
| `userConfig.external-dns.configMap` |**None**|**Type:** `object`|
| `userConfig.external-dns.configMap.values` |**None**|**Type:** `string`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `clusterName` |**None**|**Type:** `string`|
| `organization` |**None**|**Type:** `string`|




## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-azure)
