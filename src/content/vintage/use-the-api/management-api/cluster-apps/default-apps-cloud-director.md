---
title: Default-Apps-Cloud-Director chart reference
linkTitle: default-apps-cloud-director
description:  A Helm chart which defines the pre-installed apps in all Giant Swarm Cloud Director (VCD) clusters; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: default-apps-cloud-director
    parent: uiapi-cluster-apps
layout: cluster-app
last_review_date: 2024-03-04
user_questions:
 - What properties can I configure for default-apps-cloud-director?
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/default-apps-cloud-director
source_repository_ref: v0.7.3
---

The `default-apps-cloud-director` chart templates all the components required for a Cluster API VMware cluster like External DNS or CoreDNS.

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
        <a class="header-link" href="#apps-certExporter-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.dependsOn</h3>
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
        <a class="header-link" href="#apps-certExporter-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.extraConfigs</h3>
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
        <a class="header-link" href="#apps-certExporter-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-certExporter-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-certExporter-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-certExporter-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.certExporter.inCluster</h3>
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
        <a class="header-link" href="#apps-chartOperatorExtensions-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.extraConfigs</h3>
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
        <a class="header-link" href="#apps-chartOperatorExtensions-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-chartOperatorExtensions-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-chartOperatorExtensions-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-chartOperatorExtensions-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.forceUpgrade</h3>
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
        <a class="header-link" href="#apps-chartOperatorExtensions-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.chartOperatorExtensions.inCluster</h3>
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
        <a class="header-link" href="#apps-clusterResources">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources</h3>
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
        <a class="header-link" href="#apps-clusterResources-appName">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.appName</h3>
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
        <a class="header-link" href="#apps-clusterResources-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.catalog</h3>
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
        <a class="header-link" href="#apps-clusterResources-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.chartName</h3>
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
        <a class="header-link" href="#apps-clusterResources-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.clusterValues</h3>
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
        <a class="header-link" href="#apps-clusterResources-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.clusterValues.configMap</h3>
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
        <a class="header-link" href="#apps-clusterResources-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.clusterValues.secret</h3>
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
        <a class="header-link" href="#apps-clusterResources-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.dependsOn</h3>
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
        <a class="header-link" href="#apps-clusterResources-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.extraConfigs</h3>
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
        <a class="header-link" href="#apps-clusterResources-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-clusterResources-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-clusterResources-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-clusterResources-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.forceUpgrade</h3>
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
        <a class="header-link" href="#apps-clusterResources-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.inCluster</h3>
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
        <a class="header-link" href="#apps-clusterResources-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.namespace</h3>
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
        <a class="header-link" href="#apps-clusterResources-version">
          <i class="fa fa-link"></i>
        </a>.apps.clusterResources.version</h3>
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
        <a class="header-link" href="#apps-metricsServer-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.dependsOn</h3>
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
        <a class="header-link" href="#apps-metricsServer-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.extraConfigs</h3>
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
        <a class="header-link" href="#apps-metricsServer-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-metricsServer-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-metricsServer-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-metricsServer-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.metricsServer.inCluster</h3>
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
        <a class="header-link" href="#apps-netExporter-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.dependsOn</h3>
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
        <a class="header-link" href="#apps-netExporter-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.extraConfigs</h3>
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
        <a class="header-link" href="#apps-netExporter-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-netExporter-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-netExporter-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-netExporter-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.netExporter.inCluster</h3>
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
        <a class="header-link" href="#apps-nodeExporter-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.dependsOn</h3>
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
        <a class="header-link" href="#apps-nodeExporter-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.extraConfigs</h3>
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
        <a class="header-link" href="#apps-nodeExporter-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-nodeExporter-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-nodeExporter-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-nodeExporter-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.nodeExporter.inCluster</h3>
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
        <a class="header-link" href="#apps-observabilityBundle-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.dependsOn</h3>
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
        <a class="header-link" href="#apps-observabilityBundle-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.extraConfigs</h3>
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
        <a class="header-link" href="#apps-observabilityBundle-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-observabilityBundle-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-observabilityBundle-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.observabilityBundle.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-appName">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.appName</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-catalog">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.catalog</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-chartName">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.chartName</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-clusterValues">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.clusterValues</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-clusterValues-configMap">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.clusterValues.configMap</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-clusterValues-secret">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.clusterValues.secret</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-dependsOn">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.dependsOn</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.extraConfigs</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.extraConfigs[*]</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.extraConfigs[*].kind</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.extraConfigs[*].name</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-forceUpgrade">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.forceUpgrade</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-inCluster">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.inCluster</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-namespace">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.namespace</h3>
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
        <a class="header-link" href="#apps-teleportKubeAgent-version">
          <i class="fa fa-link"></i>
        </a>.apps.teleportKubeAgent.version</h3>
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
        <a class="header-link" href="#userConfig-certExporter">
          <i class="fa fa-link"></i>
        </a>.userConfig.certExporter</h3>
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
        <a class="header-link" href="#userConfig-certExporter-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.certExporter.configMap</h3>
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
        <a class="header-link" href="#userConfig-certExporter-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.certExporter.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>, <span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
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
      <div class="property-meta"><span class="property-type">object</span>, <span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-metricsServer">
          <i class="fa fa-link"></i>
        </a>.userConfig.metricsServer</h3>
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
        <a class="header-link" href="#userConfig-metricsServer-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.metricsServer.configMap</h3>
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
        <a class="header-link" href="#userConfig-metricsServer-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.metricsServer.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>, <span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-netExporter">
          <i class="fa fa-link"></i>
        </a>.userConfig.netExporter</h3>
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
        <a class="header-link" href="#userConfig-netExporter-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.netExporter.configMap</h3>
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
        <a class="header-link" href="#userConfig-netExporter-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.netExporter.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>, <span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-nodeExporter">
          <i class="fa fa-link"></i>
        </a>.userConfig.nodeExporter</h3>
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
        <a class="header-link" href="#userConfig-nodeExporter-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.nodeExporter.configMap</h3>
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
        <a class="header-link" href="#userConfig-nodeExporter-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.nodeExporter.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>, <span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#userConfig-vpa">
          <i class="fa fa-link"></i>
        </a>.userConfig.vpa</h3>
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
        <a class="header-link" href="#userConfig-vpa-configMap">
          <i class="fa fa-link"></i>
        </a>.userConfig.vpa.configMap</h3>
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
        <a class="header-link" href="#userConfig-vpa-configMap-values">
          <i class="fa fa-link"></i>
        </a>.userConfig.vpa.configMap.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">object</span>, <span class="property-type">string</span>&nbsp;
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
        <a class="header-link" href="#managementCluster">
          <i class="fa fa-link"></i>
        </a>.managementCluster</h3>
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

- [Source repository](https://github.com/giantswarm/default-apps-cloud-director)
