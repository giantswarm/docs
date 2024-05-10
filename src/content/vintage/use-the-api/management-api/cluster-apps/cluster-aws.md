---
title: cluster-aws chart reference
linkTitle: cluster-aws
description:  A helm chart for creating Cluster API clusters with the AWS infrastructure provider (CAPA).; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: cluster-aws
    parent: uiapi-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-aws?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-aws
source_repository_ref: v0.60.1
---

The `cluster-aws` chart templates all the AWS infrastructure resources that are necessary to create a Cluster API cluster.

<!-- INTRO_END -->
# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

Note that configuration options can change between releases. Use the GitHub function for selecting a branch/tag to view the documentation matching your cluster-aws version.

<!-- Update the content below by executing (from the repo root directory)

schemadocs generate helm/cluster-aws/values.schema.json -o helm/cluster-aws/README.md

-->

<!-- DOCS_START -->

<div class="crd-schema-version">
  <h2 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Chart Configuration Reference
  </h2>
  <h3 class="headline-with-link">
    <a class="header-link" href="#AWS-settings">
      <i class="fa fa-link"></i>
    </a>AWS settings
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-providerSpecific-additionalResourceTags">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.additionalResourceTags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional resource tags</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Additional tags to add to AWS resources created by the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-providerSpecific-additionalResourceTags-*">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.additionalResourceTags.*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-providerSpecific-ami">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.ami</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Amazon machine image (AMI)</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">If specified, this image will be used to provision EC2 instances.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-providerSpecific-awsClusterRoleIdentityName">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.awsClusterRoleIdentityName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster role identity name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of an AWSClusterRoleIdentity object. Learn more at https://docs.giantswarm.io/getting-started/cloud-provider-accounts/cluster-api/aws/#configure-the-awsclusterroleidentity .</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-providerSpecific-flatcarAwsAccount">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.flatcarAwsAccount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">AWS account owning Flatcar image</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">AWS account ID owning the Flatcar Container Linux AMI.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-providerSpecific-region">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.region</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Region</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Apps">
      <i class="fa fa-link"></i>
    </a>Apps
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Configuration of apps that are part of the cluster.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">App</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of an default app that is part of the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager.extraConfigs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra config maps or secrets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager.extraConfigs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Config map or secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager.extraConfigs[*].kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Specifies whether the resource is a config map or a secret.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager.extraConfigs[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the config map or secret. The object must exist in the same namespace as the cluster App.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager-extraConfigs[*]-optional">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager.extraConfigs[*].optional</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Optional</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsCloudControllerManager-values">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsCloudControllerManager.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Values</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Values to be passed to the app. Values will have higher priority than values from configmaps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">App</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of an default app that is part of the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver.extraConfigs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra config maps or secrets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver.extraConfigs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Config map or secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver.extraConfigs[*].kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Specifies whether the resource is a config map or a secret.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver.extraConfigs[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the config map or secret. The object must exist in the same namespace as the cluster App.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver-extraConfigs[*]-optional">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver.extraConfigs[*].optional</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Optional</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-awsEbsCsiDriver-values">
          <i class="fa fa-link"></i>
        </a>.global.apps.awsEbsCsiDriver.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Values</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Values to be passed to the app. Values will have higher priority than values from configmaps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">App</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of an default app that is part of the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium.extraConfigs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra config maps or secrets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium.extraConfigs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Config map or secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium.extraConfigs[*].kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Specifies whether the resource is a config map or a secret.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium.extraConfigs[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the config map or secret. The object must exist in the same namespace as the cluster App.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium-extraConfigs[*]-optional">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium.extraConfigs[*].optional</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Optional</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-cilium-values">
          <i class="fa fa-link"></i>
        </a>.global.apps.cilium.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Values</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Values to be passed to the app. Values will have higher priority than values from configmaps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">App</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of an default app that is part of the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns.extraConfigs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra config maps or secrets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns.extraConfigs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Config map or secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns.extraConfigs[*].kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Specifies whether the resource is a config map or a secret.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns.extraConfigs[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the config map or secret. The object must exist in the same namespace as the cluster App.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns-extraConfigs[*]-optional">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns.extraConfigs[*].optional</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Optional</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-coreDns-values">
          <i class="fa fa-link"></i>
        </a>.global.apps.coreDns.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Values</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Values to be passed to the app. Values will have higher priority than values from configmaps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">App</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of an default app that is part of the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd-extraConfigs">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd.extraConfigs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra config maps or secrets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd-extraConfigs[*]">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd.extraConfigs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Config map or secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd-extraConfigs[*]-kind">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd.extraConfigs[*].kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Specifies whether the resource is a config map or a secret.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd-extraConfigs[*]-name">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd.extraConfigs[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the config map or secret. The object must exist in the same namespace as the cluster App.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd-extraConfigs[*]-optional">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd.extraConfigs[*].optional</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Optional</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-apps-verticalPodAutoscalerCrd-values">
          <i class="fa fa-link"></i>
        </a>.global.apps.verticalPodAutoscalerCrd.values</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Values</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Values to be passed to the app. Values will have higher priority than values from configmaps.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Components">
      <i class="fa fa-link"></i>
    </a>Components
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Advanced configuration of components that are running on all nodes.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Containerd</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of containerd.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Container registries</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Endpoints and credentials configuration for container registries.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Registries</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Container registries and mirrors</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Registry</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]-credentials">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*].credentials</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Credentials</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]-credentials-auth">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*].credentials.auth</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Auth</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Base64-encoded string from the concatenation of the username, a colon, and the password.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]-credentials-identitytoken">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*].credentials.identitytoken</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Identity token</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Used to authenticate the user and obtain an access token for the registry.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]-credentials-password">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*].credentials.password</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Password</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Used to authenticate for the registry with username/password.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]-credentials-username">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*].credentials.username</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Used to authenticate for the registry with username/password.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-components-containerd-containerRegistries-*[*]-endpoint">
          <i class="fa fa-link"></i>
        </a>.global.components.containerd.containerRegistries.*[*].endpoint</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Endpoint</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Endpoint for the container registry.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Connectivity">
      <i class="fa fa-link"></i>
    </a>Connectivity
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-availabilityZoneUsageLimit">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.availabilityZoneUsageLimit</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Availability zones</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Maximum number of availability zones (AZ) that should be used in a region. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating subnets.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-baseDomain">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.baseDomain</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Base DNS domain</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-dns">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.dns</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">DNS</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-dns-resolverRulesOwnerAccount">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.dns.resolverRulesOwnerAccount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resolver rules owner</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the AWS account that created the resolver rules to be associated with the workload cluster VPC.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Network</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-internetGatewayId">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.internetGatewayId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Internet Gateway ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the Internet gateway for the VPC.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-pods">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.pods</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pods</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-pods-cidrBlocks">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.pods.cidrBlocks</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pod subnets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-pods-cidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.pods.cidrBlocks[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pod subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range for pods, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-services">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.services</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Services</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-services-cidrBlocks">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.services.cidrBlocks</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">K8s Service subnets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-services-cidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.services.cidrBlocks[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Service subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range for kubernetes services, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-vpcCidr">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.vpcCidr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPC subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range to assign to this cluster's VPC, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-network-vpcId">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.vpcId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPC id</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the VPC, where the cluster will be deployed. The VPC must exist and it case this is set, VPC wont be created by controllers.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-proxy">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.proxy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Proxy</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Whether/how outgoing traffic is routed through proxy servers.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-proxy-enabled">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.proxy.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-proxy-httpProxy">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.proxy.httpProxy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">HTTP proxy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">To be passed to the HTTP_PROXY environment variable in all hosts.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-proxy-httpsProxy">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.proxy.httpsProxy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">HTTPS proxy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">To be passed to the HTTPS_PROXY environment variable in all hosts.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-proxy-noProxy">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.proxy.noProxy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">No proxy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">To be passed to the NO_PROXY environment variable in all hosts.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Subnets are created and tagged based on this definition.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-cidrBlocks">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].cidrBlocks</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Network</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-cidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].cidrBlocks[*]</h3>
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
        <a class="header-link" href="#global-connectivity-subnets[*]-cidrBlocks[*]-availabilityZone">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].cidrBlocks[*].availabilityZone</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Availability zone</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-cidrBlocks[*]-cidr">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].cidrBlocks[*].cidr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Address range</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-cidrBlocks[*]-tags">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].cidrBlocks[*].tags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tags</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">AWS resource tags to assign to this subnet.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-cidrBlocks[*]-tags-*">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].cidrBlocks[*].tags.*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-id">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID of the subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of an existing subnet. When set, this subnet will be used instead of creating a new one.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-isPublic">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].isPublic</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Public</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-natGatewayId">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].natGatewayId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID of the NAT Gateway</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the NAT Gateway used for this existing subnet.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-routeTableId">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].routeTableId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID of route table</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the route table, assigned to the existing subnet. Must be provided when defining subnet via ID.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-tags">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].tags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tags</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">AWS resource tags to assign to this CIDR block.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-subnets[*]-tags-*">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.subnets[*].tags.*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-topology">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.topology</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Topology</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Networking architecture between management cluster and workload cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-topology-mode">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.topology.mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Valid values: GiantSwarmManaged, UserManaged, None.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-topology-prefixListId">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.topology.prefixListId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Prefix list ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the managed prefix list to use when the topology mode is set to 'UserManaged'.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-topology-transitGatewayId">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.topology.transitGatewayId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Transit gateway ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">If the topology mode is set to 'UserManaged', this can be used to specify the transit gateway to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-vpcEndpointMode">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.vpcEndpointMode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPC endpoint mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Who is reponsible for creation and management of VPC endpoints.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-vpcMode">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.vpcMode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPC mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Whether the cluser's VPC is created with public, internet facing resources (public subnets, NAT gateway) or not (private).</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Control-plane">
      <i class="fa fa-link"></i>
    </a>Control plane
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-additionalSecurityGroups">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.additionalSecurityGroups</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control Plane additional security groups</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Additional security groups that will be added to the control plane nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-additionalSecurityGroups[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.additionalSecurityGroups[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Security group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-additionalSecurityGroups[*]-id">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.additionalSecurityGroups[*].id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Id of the security group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the security group that will be added to the control plane nodes. The security group must exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-apiExtraArgs">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.apiExtraArgs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API extra arguments</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Extra arguments passed to the kubernetes API server.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-apiExtraArgs-PATTERN">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.apiExtraArgs.PATTERN</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">argument</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-apiExtraCertSANs">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.apiExtraCertSANs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API extra cert SANs</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra certs SANs passed to the kubeadmcontrolplane CR.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-apiExtraCertSANs[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.apiExtraCertSANs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">cert SAN</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-apiMode">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.apiMode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Whether the Kubernetes API server load balancer should be reachable from the internet (public) or internal only (private).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-apiServerPort">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.apiServerPort</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API server port</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The API server Load Balancer port. This option sets the Spec.ClusterNetwork.APIServerPort field on the Cluster CR. In CAPI this field isn't used currently. It is instead used in providers. In CAPA this sets only the public facing port of the Load Balancer. In CAPZ both the public facing and the destination port are set to this value. CAPV and CAPVCD do not use it.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-containerdVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.containerdVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Containerd volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-etcdVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.etcdVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Etcd volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-instanceType">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.instanceType</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">EC2 instance type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-kubeletVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.kubeletVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubelet volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-loadBalancerIngressAllowCidrBlocks">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.loadBalancerIngressAllowCidrBlocks</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Load balancer allow list</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address ranges that are allowed to connect to the control plane load balancer, in CIDR notation. When setting this field, remember to add the Management cluster Nat Gateway IPs provided by Giant Swarm so that the cluster can still be managed. These Nat Gateway IPs can be found in the Management Cluster AWSCluster '.status.networkStatus.natGatewaysIPs' field.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-loadBalancerIngressAllowCidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.loadBalancerIngressAllowCidrBlocks[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Address range</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-machineHealthCheck">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.machineHealthCheck</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Machine health check</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-machineHealthCheck-enabled">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.machineHealthCheck.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-machineHealthCheck-maxUnhealthy">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.machineHealthCheck.maxUnhealthy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Maximum unhealthy nodes</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-machineHealthCheck-nodeStartupTimeout">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.machineHealthCheck.nodeStartupTimeout</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node startup timeout</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Determines how long a machine health check should wait for a node to join the cluster, before considering a machine unhealthy.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-machineHealthCheck-unhealthyNotReadyTimeout">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.machineHealthCheck.unhealthyNotReadyTimeout</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Timeout for ready</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">If a node is not in condition 'Ready' after this timeout, it will be considered unhealthy.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-machineHealthCheck-unhealthyUnknownTimeout">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.machineHealthCheck.unhealthyUnknownTimeout</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Timeout for unknown condition</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">If a node is in 'Unknown' condition after this timeout, it will be considered unhealthy.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidc">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidc</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">OIDC authentication</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidc-caPem">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidc.caPem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Certificate authority</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Identity provider's CA certificate in PEM format.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidc-clientId">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidc.clientId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Client ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidc-groupsClaim">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidc.groupsClaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Groups claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidc-issuerUrl">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidc.issuerUrl</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Issuer URL</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Exact issuer URL that will be included in identity tokens.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidc-usernameClaim">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidc.usernameClaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.rootVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Root volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-subnetTags">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.subnetTags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tags</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Tags to select AWS resources for the control plane by.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.subnetTags[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tag</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.subnetTags[*].*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Internal">
      <i class="fa fa-link"></i>
    </a>Internal
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>For Giant Swarm internal use only, not stable, or not supported by UIs.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-cgroupsv1">
          <i class="fa fa-link"></i>
        </a>.internal.cgroupsv1</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">CGroups v1</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Force use of CGroups v1 for whole cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-hashSalt">
          <i class="fa fa-link"></i>
        </a>.internal.hashSalt</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Hash salt</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">If specified, this token is used as a salt to the hash suffix of some resource names. Can be used to force-recreate some resources.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-kubernetesVersion">
          <i class="fa fa-link"></i>
        </a>.internal.kubernetesVersion</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubernetes version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration">
          <i class="fa fa-link"></i>
        </a>.internal.migration</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Migration values</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Section used for migration of cluster from vintage to CAPI</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-apiBindPort">
          <i class="fa fa-link"></i>
        </a>.internal.migration.apiBindPort</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubernetes API bind port</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes API bind port used for kube api pod</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control Plane extra files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Additional fiels that will be provisioned to control-plane nodes, reference is from secret in the same namespace.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">file</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">secret key for file content</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">secret name for file content</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]-path">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">file path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlaneExtraFiles[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlaneExtraFiles[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">file permissions in form 0644</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlanePostKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlanePostKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control Plane Post Kubeadm Commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Additional Post-Kubeadm Commands executed on the control plane node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlanePostKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlanePostKubeadmCommands[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">command</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlanePreKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlanePreKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control Plane Pre Kubeadm Commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Additional Pre-Kubeadm Commands executed on the control plane node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-controlPlanePreKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.migration.controlPlanePreKubeadmCommands[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">command</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-etcdExtraArgs">
          <i class="fa fa-link"></i>
        </a>.internal.migration.etcdExtraArgs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Etcd extra arguments</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-etcdExtraArgs-PATTERN">
          <i class="fa fa-link"></i>
        </a>.internal.migration.etcdExtraArgs.PATTERN</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">argument</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-migration-irsaAdditionalDomain">
          <i class="fa fa-link"></i>
        </a>.internal.migration.irsaAdditionalDomain</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">IRSA additional domain</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Additional domain to be added to IRSA trust relationship.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default node pool</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node pool</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-additionalSecurityGroups">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.additionalSecurityGroups</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Machine pool additional security groups</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Additional security groups that will be added to the machine pool nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-additionalSecurityGroups[*]">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.additionalSecurityGroups[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">security group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-additionalSecurityGroups[*]-id">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.additionalSecurityGroups[*].id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Id of the security group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the security group that will be added to the machine pool nodes. The security group must exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-availabilityZones">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.availabilityZones</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Availability zones</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-availabilityZones[*]">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.availabilityZones[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Availability zone</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeLabels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node labels</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeLabels[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeTaints</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node taints</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeTaints[*]</h3>
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
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeTaints[*].effect</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Effect</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeTaints[*].key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.customNodeTaints[*].value</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-instanceType">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.instanceType</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">EC2 instance type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-instanceTypeOverrides">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.instanceTypeOverrides</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Instance type overrides</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Ordered list of instance types to be used for the machine pool. The first instance type that is available in the region will be used. Read more in our docs https://docs.giantswarm.io/advanced/cluster-management/node-pools-capi/</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-instanceTypeOverrides[*]">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.instanceTypeOverrides[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">EC2 instance type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-maxSize">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.maxSize</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Maximum number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-minSize">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.minSize</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Minimum number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.rootVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Root volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-spotInstances">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.spotInstances</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Spot instances</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Compared to on-demand instances, spot instances can help you save cost.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-spotInstances-enabled">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.spotInstances.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-spotInstances-maxPrice">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.spotInstances.maxPrice</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Maximum price to pay per instance per hour, in USD.</span><br /><span class="property-type">number</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-subnetTags">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.subnetTags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tags</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Tags to filter which AWS subnets will be used for this node pool.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.subnetTags[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tag</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-nodePools-PATTERN-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.internal.nodePools.PATTERN.subnetTags[*].*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-sandboxContainerImage">
          <i class="fa fa-link"></i>
        </a>.internal.sandboxContainerImage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Sandbox image</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The image used by sandbox / pause container</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-sandboxContainerImage-name">
          <i class="fa fa-link"></i>
        </a>.internal.sandboxContainerImage.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Repository</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-sandboxContainerImage-registry">
          <i class="fa fa-link"></i>
        </a>.internal.sandboxContainerImage.registry</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Registry</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-sandboxContainerImage-tag">
          <i class="fa fa-link"></i>
        </a>.internal.sandboxContainerImage.tag</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-teleport">
          <i class="fa fa-link"></i>
        </a>.internal.teleport</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Teleport</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-teleport-enabled">
          <i class="fa fa-link"></i>
        </a>.internal.teleport.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable teleport</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-teleport-proxyAddr">
          <i class="fa fa-link"></i>
        </a>.internal.teleport.proxyAddr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Teleport proxy address</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-teleport-version">
          <i class="fa fa-link"></i>
        </a>.internal.teleport.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Teleport version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Kubectl-image">
      <i class="fa fa-link"></i>
    </a>Kubectl image
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#kubectlImage-name">
          <i class="fa fa-link"></i>
        </a>.kubectlImage.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Repository</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#kubectlImage-registry">
          <i class="fa fa-link"></i>
        </a>.kubectlImage.registry</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Registry</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#kubectlImage-tag">
          <i class="fa fa-link"></i>
        </a>.kubectlImage.tag</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Metadata">
      <i class="fa fa-link"></i>
    </a>Metadata
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-description">
          <i class="fa fa-link"></i>
        </a>.global.metadata.description</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster description</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">User-friendly description of the cluster's purpose.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-name">
          <i class="fa fa-link"></i>
        </a>.global.metadata.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Unique identifier, cannot be changed after creation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-organization">
          <i class="fa fa-link"></i>
        </a>.global.metadata.organization</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Organization</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-preventDeletion">
          <i class="fa fa-link"></i>
        </a>.global.metadata.preventDeletion</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Prevent cluster deletion</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-servicePriority">
          <i class="fa fa-link"></i>
        </a>.global.metadata.servicePriority</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Service priority</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The relative importance of this cluster.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Node-pools">
      <i class="fa fa-link"></i>
    </a>Node pools
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Node pools of the cluster. If not specified, this defaults to the value of `internal.nodePools`.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node pool</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-additionalSecurityGroups">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.additionalSecurityGroups</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Machine pool additional security groups</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Additional security groups that will be added to the machine pool nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-additionalSecurityGroups[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.additionalSecurityGroups[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">security group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-additionalSecurityGroups[*]-id">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.additionalSecurityGroups[*].id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Id of the security group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the security group that will be added to the machine pool nodes. The security group must exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-availabilityZones">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.availabilityZones</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Availability zones</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-availabilityZones[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.availabilityZones[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Availability zone</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeLabels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node labels</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeLabels[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeTaints</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node taints</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeTaints[*]</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeTaints[*].effect</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Effect</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeTaints[*].key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.customNodeTaints[*].value</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-instanceType">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.instanceType</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">EC2 instance type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-instanceTypeOverrides">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.instanceTypeOverrides</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Instance type overrides</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Ordered list of instance types to be used for the machine pool. The first instance type that is available in the region will be used. Read more in our docs https://docs.giantswarm.io/advanced/cluster-management/node-pools-capi/</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-instanceTypeOverrides[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.instanceTypeOverrides[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">EC2 instance type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-maxSize">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.maxSize</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Maximum number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-minSize">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.minSize</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Minimum number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.rootVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Root volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-spotInstances">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.spotInstances</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Spot instances</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Compared to on-demand instances, spot instances can help you save cost.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-spotInstances-enabled">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.spotInstances.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-spotInstances-maxPrice">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.spotInstances.maxPrice</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Maximum price to pay per instance per hour, in USD.</span><br /><span class="property-type">number</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-subnetTags">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.subnetTags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tags</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Tags to filter which AWS subnets will be used for this node pool.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.subnetTags[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tag</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.subnetTags[*].*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Other-global">
      <i class="fa fa-link"></i>
    </a>Other global
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-managementCluster">
          <i class="fa fa-link"></i>
        </a>.global.managementCluster</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Management cluster</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Cluster API cluster managing this workload cluster.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Pod-Security-Standards">
      <i class="fa fa-link"></i>
    </a>Pod Security Standards
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-podSecurityStandards-enforced">
          <i class="fa fa-link"></i>
        </a>.global.podSecurityStandards.enforced</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enforced</span><br /><span class="property-type">boolean</span>&nbsp;
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
        <a class="header-link" href="#baseDomain">
          <i class="fa fa-link"></i>
        </a>.baseDomain</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Base DNS domain</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#cluster">
          <i class="fa fa-link"></i>
        </a>.cluster</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Helm values for the provider-independent cluster chart</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#cluster-shared">
          <i class="fa fa-link"></i>
        </a>.cluster-shared</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Library chart</span><br /><span class="property-type">object</span>&nbsp;
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
      <div class="property-meta"><span class="property-title">Management cluster</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Cluster API cluster managing this workload cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#provider">
          <i class="fa fa-link"></i>
        </a>.provider</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster API provider name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div></div>

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-aws)
