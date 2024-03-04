---
title: Default-Apps-Azure chart reference
linkTitle: default-apps-azure chart reference
description: |
  A Helm chart defining the preinstalled apps running in all Giant Swarm Azure clusters.; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: default-apps-azure
    parent: uiapi-cluster-apps
layout: cluster-app
last_review_date: 2024-03-04
user_questions:
 - What properties can I configure for default-apps-azure?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/default-apps-azure
source_repository_ref: v0.8.3
---

The `default-apps-azure` chart templates all the components required for a Cluster API Azure cluster like External DNS or CoreDNS.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

<!-- DOCS_START -->


<div class="crd-schema-version">
  <h2 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Chart Configuration Reference
  </h2>
  <h3 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-certManager">
          <i class="fa fa-link"></i>
        </a>.userConfig.certManager</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-certManager-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.certManager.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-certManager-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.certManager.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-etcdKubernetesResourceCountExporter">
          <i class="fa fa-link"></i>
        </a>.userConfig.etcdKubernetesResourceCountExporter</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-etcdKubernetesResourceCountExporter-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.etcdKubernetesResourceCountExporter.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-etcdKubernetesResourceCountExporter-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.etcdKubernetesResourceCountExporter.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-external-dns">
          <i class="fa fa-link"></i>
        </a>.userConfig.external-dns</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-external-dns-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.external-dns.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-external-dns-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.external-dns.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-appName">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certExporter-version">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager">
          <i class="fa fa-link"></i>
        </a>.apps.certManager</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-appName">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-certManager-version">
          <i class="fa fa-link"></i>
        </a>.apps.certManager.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-appName">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.dependsOn</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-enabled">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-chartOperatorExtensions-version">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-appName">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-etcdKubernetesResourceCountExporter-version">
          <i class="fa fa-link"></i>
        </a>.apps.etcdKubernetesResourceCountExporter.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-appName">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-external-dns-version">
          <i class="fa fa-link"></i>
        </a>.apps.external-dns.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-appName">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-metricsServer-version">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-appName">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-netExporter-version">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-appName">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-nodeExporter-version">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-appName">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.inCluster</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-observabilityBundle-version">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-appName">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.extraConfigs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.extraConfigs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta">
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.extraConfigs[*].kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.extraConfigs[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-teleport-kube-agent-version">
          <i class="fa fa-link"></i>
        </a>.apps.teleport-kube-agent.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa">
          <i class="fa fa-link"></i>
        </a>.apps.vpa</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-appName">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.appName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.chartName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.clusterValues</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.clusterValues.configMap</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.clusterValues.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.forceUpgrade</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apps-vpa-version">
          <i class="fa fa-link"></i>
        </a>.apps.vpa.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Other">
      <i class="fa fa-link"></i>
    </a>Other
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#clusterName">
          <i class="fa fa-link"></i>
        </a>.clusterName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#organization">
          <i class="fa fa-link"></i>
        </a>.organization</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div></div>


<!-- DOCS_END -->


## Further reading

- [Source repository](https://github.com/giantswarm/default-apps-azure)
