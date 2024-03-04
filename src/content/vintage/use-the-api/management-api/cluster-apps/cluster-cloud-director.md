---
title: Cluster-Cloud-Director chart reference
linkTitle: cluster-cloud-director chart reference
description: |
  A helm chart for creating Cluster API clusters with the VMware Cloud Director (VCD) infrastructure provider (CAPVCD).; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: cluster-cloud-director
    parent: uiapi-cluster-apps
layout: cluster-app
last_review_date: 2024-03-04
user_questions:
 - What properties can I configure for cluster-cloud-director?
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/cluster-cloud-director
source_repository_ref: v0.14.2
---

The `default-apps-cloud-director` chart templates all the VMware infrastructure resources that are necessary to create a Cluster API VCD cluster.

# cluster-cloud-director values

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
        <a class="header-link" href="#internal-apiServer">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer</h3>
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
        <a class="header-link" href="#internal-apiServer-enableAdmissionPlugins">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer.enableAdmissionPlugins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Admission plugins</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">List of admission plugins to be passed to the API server via the --enable-admission-plugins flag.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-apiServer-enableAdmissionPlugins[*]">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer.enableAdmissionPlugins[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Plugin</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-apiServer-featureGates">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer.featureGates</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gates</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">API server feature gate activation/deactivation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-apiServer-featureGates[*]">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer.featureGates[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gate</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-apiServer-featureGates[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer.featureGates[*].enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-apiServer-featureGates[*]-name">
          <i class="fa fa-link"></i>
        </a>.internal.apiServer.featureGates[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-ciliumNetworkPolicy">
          <i class="fa fa-link"></i>
        </a>.internal.ciliumNetworkPolicy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">CiliumNetworkPolicies</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-ciliumNetworkPolicy-enabled">
          <i class="fa fa-link"></i>
        </a>.internal.ciliumNetworkPolicy.enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable CiliumNetworkPolicies</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Installs the network-policies-app (deny all by default) if set to true</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-controllerManager">
          <i class="fa fa-link"></i>
        </a>.internal.controllerManager</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Controller manager</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-controllerManager-featureGates">
          <i class="fa fa-link"></i>
        </a>.internal.controllerManager.featureGates</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gates</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Controller manager feature gate activation/deactivation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-controllerManager-featureGates[*]">
          <i class="fa fa-link"></i>
        </a>.internal.controllerManager.featureGates[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gate</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-controllerManager-featureGates[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.internal.controllerManager.featureGates[*].enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-controllerManager-featureGates[*]-name">
          <i class="fa fa-link"></i>
        </a>.internal.controllerManager.featureGates[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
        <a class="header-link" href="#internal-parentUid">
          <i class="fa fa-link"></i>
        </a>.internal.parentUid</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Management cluster UID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">If set, create the cluster from a specific management cluster associated with this UID.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-rdeId">
          <i class="fa fa-link"></i>
        </a>.internal.rdeId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Runtime defined entity (RDE) identifier</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">This cluster's RDE ID in the VCD API.</div>
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
      <div class="property-meta"><span class="property-title">Sandbox Container image (pause container)</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
        <a class="header-link" href="#internal-skipRde">
          <i class="fa fa-link"></i>
        </a>.internal.skipRde</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Skip RDE</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Set to true if the API schema extension is installed in the correct version in VCD to create CAPVCD entities in the API. Set to false otherwise.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-useAsManagementCluster">
          <i class="fa fa-link"></i>
        </a>.internal.useAsManagementCluster</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Display as management cluster</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Connectivity">
      <i class="fa fa-link"></i>
    </a>Connectivity
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Configurations related to cluster connectivity such as container registries.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-containerRegistries">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*]</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*[*]-credentials">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*].credentials</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Credentials</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Credentials for the endpoint.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-containerRegistries-*[*]-credentials-auth">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*].credentials.auth</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*[*]-credentials-identitytoken">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*].credentials.identitytoken</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*[*]-credentials-password">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*].credentials.password</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*[*]-credentials-username">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*].credentials.username</h3>
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
        <a class="header-link" href="#connectivity-containerRegistries-*[*]-endpoint">
          <i class="fa fa-link"></i>
        </a>.connectivity.containerRegistries.*[*].endpoint</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Endpoint</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Endpoint for the container registry.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network">
          <i class="fa fa-link"></i>
        </a>.connectivity.network</h3>
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
        <a class="header-link" href="#connectivity-network-controlPlaneEndpoint">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlaneEndpoint</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control plane endpoint</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes API endpoint.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-controlPlaneEndpoint-host">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlaneEndpoint.host</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Host</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-controlPlaneEndpoint-port">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlaneEndpoint.port</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Port number</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-extraOvdcNetworks">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.extraOvdcNetworks</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra OVDC networks</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">OVDC networks to attach VMs to, additionally.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-extraOvdcNetworks[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.extraOvdcNetworks[*]</h3>
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
        <a class="header-link" href="#connectivity-network-hostEntries">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.hostEntries</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Host entries</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-hostEntries[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.hostEntries[*]</h3>
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
        <a class="header-link" href="#connectivity-network-hostEntries[*]-fqdn">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.hostEntries[*].fqdn</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">FQDN</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-hostEntries[*]-ip">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.hostEntries[*].ip</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">IP address</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-loadBalancers">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.loadBalancers</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Load Balancers</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-loadBalancers-vipSubnet">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.loadBalancers.vipSubnet</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Virtual IP subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Virtual IP CIDR for the external network.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-pods">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.pods</h3>
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
        <a class="header-link" href="#connectivity-network-pods-cidrBlocks">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.pods.cidrBlocks</h3>
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
        <a class="header-link" href="#connectivity-network-pods-cidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.pods.cidrBlocks[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-services">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.services</h3>
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
        <a class="header-link" href="#connectivity-network-services-cidrBlocks">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.services.cidrBlocks</h3>
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
        <a class="header-link" href="#connectivity-network-services-cidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.services.cidrBlocks[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-staticRoutes">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.staticRoutes</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Static routes</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-staticRoutes[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.staticRoutes[*]</h3>
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
        <a class="header-link" href="#connectivity-network-staticRoutes[*]-destination">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.staticRoutes[*].destination</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Destination</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-staticRoutes[*]-via">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.staticRoutes[*].via</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Via</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-ntp">
          <i class="fa fa-link"></i>
        </a>.connectivity.ntp</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Time synchronization (NTP)</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Servers/pools to synchronize this cluster's clocks with.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-ntp-pools">
          <i class="fa fa-link"></i>
        </a>.connectivity.ntp.pools</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pools</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-ntp-pools[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.ntp.pools[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pool</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-ntp-servers">
          <i class="fa fa-link"></i>
        </a>.connectivity.ntp.servers</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Servers</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-ntp-servers[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.ntp.servers[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Server</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-proxy">
          <i class="fa fa-link"></i>
        </a>.connectivity.proxy</h3>
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
        <a class="header-link" href="#connectivity-proxy-enabled">
          <i class="fa fa-link"></i>
        </a>.connectivity.proxy.enabled</h3>
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
        <a class="header-link" href="#connectivity-proxy-secretName">
          <i class="fa fa-link"></i>
        </a>.connectivity.proxy.secretName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of a secret resource used by containerd to obtain the HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables. If empty the value will be defaulted to <clusterName>-cluster-values.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Shell access</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell-osUsers">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell.osUsers</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">OS Users</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Configuration for OS users in cluster nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell-osUsers[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell.osUsers[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">User</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell-osUsers[*]-name">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell.osUsers[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Username of the user.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell-osUsers[*]-sudo">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell.osUsers[*].sudo</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Sudoers configuration</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Permissions string to add to /etc/sudoers for this user.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell-sshTrustedUserCAKeys">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell.sshTrustedUserCAKeys</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Trusted SSH cert issuers</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">CA certificates of issuers that are trusted to sign SSH user certificates.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-shell-sshTrustedUserCAKeys[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.shell.sshTrustedUserCAKeys[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
        <a class="header-link" href="#controlPlane-catalog">
          <i class="fa fa-link"></i>
        </a>.controlPlane.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Catalog</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD catalog in which the VM template is stored.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-certSANs">
          <i class="fa fa-link"></i>
        </a>.controlPlane.certSANs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subject alternative names (SAN)</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Alternative names to encode in the API server's certificate.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-certSANs[*]">
          <i class="fa fa-link"></i>
        </a>.controlPlane.certSANs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">SAN</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.controlPlane.customNodeLabels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node labels</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.controlPlane.customNodeLabels[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-diskSizeGB">
          <i class="fa fa-link"></i>
        </a>.controlPlane.diskSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Disk size</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-dns">
          <i class="fa fa-link"></i>
        </a>.controlPlane.dns</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">DNS container image</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-dns-imageRepository">
          <i class="fa fa-link"></i>
        </a>.controlPlane.dns.imageRepository</h3>
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
        <a class="header-link" href="#controlPlane-dns-imageTag">
          <i class="fa fa-link"></i>
        </a>.controlPlane.dns.imageTag</h3>
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
        <a class="header-link" href="#controlPlane-etcd">
          <i class="fa fa-link"></i>
        </a>.controlPlane.etcd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Etcd container image</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-etcd-imageRepository">
          <i class="fa fa-link"></i>
        </a>.controlPlane.etcd.imageRepository</h3>
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
        <a class="header-link" href="#controlPlane-etcd-imageTag">
          <i class="fa fa-link"></i>
        </a>.controlPlane.etcd.imageTag</h3>
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
        <a class="header-link" href="#controlPlane-image">
          <i class="fa fa-link"></i>
        </a>.controlPlane.image</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node container image</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-image-repository">
          <i class="fa fa-link"></i>
        </a>.controlPlane.image.repository</h3>
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
        <a class="header-link" href="#controlPlane-oidc">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc</h3>
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
        <a class="header-link" href="#controlPlane-oidc-caFile">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.caFile</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Certificate authority file</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Path to identity provider's CA certificate in PEM format.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-oidc-clientId">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.clientId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Client ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">OIDC client identifier to identify with.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-oidc-groupsClaim">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.groupsClaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Groups claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the identity token claim bearing the user's group memberships.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-oidc-groupsPrefix">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.groupsPrefix</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Groups prefix</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Prefix prepended to groups values to prevent clashes with existing names.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-oidc-issuerUrl">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.issuerUrl</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Issuer URL</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">URL of the provider which allows the API server to discover public signing keys, not including any path. Discovery URL without the '/.well-known/openid-configuration' part.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-oidc-usernameClaim">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.usernameClaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the identity token claim bearing the unique user identifier.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-oidc-usernamePrefix">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.usernamePrefix</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username prefix</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Prefix prepended to username values to prevent clashes with existing names.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-placementPolicy">
          <i class="fa fa-link"></i>
        </a>.controlPlane.placementPolicy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VM placement policy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD VM placement policy to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-replicas">
          <i class="fa fa-link"></i>
        </a>.controlPlane.replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Number of control plane instances to create. Must be an odd number.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-resourceRatio">
          <i class="fa fa-link"></i>
        </a>.controlPlane.resourceRatio</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resource ratio</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Ratio between node resources and apiserver resource requests.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-sizingPolicy">
          <i class="fa fa-link"></i>
        </a>.controlPlane.sizingPolicy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Sizing policy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD sizing policy to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-storageProfile">
          <i class="fa fa-link"></i>
        </a>.controlPlane.storageProfile</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage profile</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD storage profile to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-template">
          <i class="fa fa-link"></i>
        </a>.controlPlane.template</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Template</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the template used to create the node VMs.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Kubectl-image">
      <i class="fa fa-link"></i>
    </a>Kubectl image
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Used by cluster-shared library chart to configure coredns in-cluster.
  </h4>
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
        <a class="header-link" href="#metadata-description">
          <i class="fa fa-link"></i>
        </a>.metadata.description</h3>
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
        <a class="header-link" href="#metadata-labels">
          <i class="fa fa-link"></i>
        </a>.metadata.labels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Labels</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">These labels are added to the Kubernetes resources defining this cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#metadata-labels-PATTERN">
          <i class="fa fa-link"></i>
        </a>.metadata.labels.PATTERN</h3>
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
        <a class="header-link" href="#metadata-organization">
          <i class="fa fa-link"></i>
        </a>.metadata.organization</h3>
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
        <a class="header-link" href="#metadata-preventDeletion">
          <i class="fa fa-link"></i>
        </a>.metadata.preventDeletion</h3>
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
        <a class="header-link" href="#metadata-servicePriority">
          <i class="fa fa-link"></i>
        </a>.metadata.servicePriority</h3>
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
    </a>Groups of worker nodes with identical configuration.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools-PATTERN">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-class">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.class</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node class</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">A valid node class name, as specified in VMware Cloud Director (VCD) settings > Node classes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools-PATTERN-replicas">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#VMware-Cloud-Director-(VCD)-settings">
      <i class="fa fa-link"></i>
    </a>VMware Cloud Director (VCD) settings
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-cloudProviderInterface">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.cloudProviderInterface</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cloud provider interface (CPI)</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-cloudProviderInterface-enableVirtualServiceSharedIP">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.cloudProviderInterface.enableVirtualServiceSharedIP</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Share IPs in virtual services</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">If enabled, multiple virtual services can share the same virtual IP address.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-cloudProviderInterface-oneArm">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.cloudProviderInterface.oneArm</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">One-arm</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">If enabled, use an internal IP for the virtual service with a NAT rule to expose the external IP. Otherwise the virtual service will be exposed directly with the external IP.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-cloudProviderInterface-oneArm-enabled">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.cloudProviderInterface.oneArm.enabled</h3>
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
        <a class="header-link" href="#providerSpecific-containerStorageInterface">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Container storage interface (CSI)</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-create storage class</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Pre-create storage class for the VCD CSI.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-delete">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.delete</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-create delete storage class</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-delete-isDefault">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.delete.isDefault</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default storage class</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-delete-vcdStorageProfileName">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.delete.vcdStorageProfileName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name of storage profile in VCD</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-enabled">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.enabled</h3>
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
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-retain">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.retain</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-create retain storage class</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-retain-isDefault">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.retain.isDefault</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default storage class</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-containerStorageInterface-storageClass-retain-vcdStorageProfileName">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.containerStorageInterface.storageClass.retain.vcdStorageProfileName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name of storage profile in VCD</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node classes</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Re-usable node configuration.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN</h3>
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
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-catalog">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.catalog</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Catalog</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD catalog in which the VM template is stored.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeLabels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node labels</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeLabels[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeTaints</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node taints</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Custom node taint</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].effect</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">One of NoSchedule, PreferNoSchedule or NoExecute</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the label on a node</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].value</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">value of the label identified by the key</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-diskSizeGB">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.diskSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Disk size</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-placementPolicy">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.placementPolicy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VM placement policy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD VM placement policy to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-sizingPolicy">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.sizingPolicy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Sizing policy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD sizing policy to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-storageProfile">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.storageProfile</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage profile</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the VCD storage profile to use.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-nodeClasses-PATTERN-template">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.nodeClasses.PATTERN.template</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Template</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the template used to create the node VMs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-org">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.org</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Organization</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">VCD organization name.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-ovdc">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.ovdc</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">OvDC name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the organization virtual datacenter (OvDC) to create this cluster in.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-ovdcNetwork">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.ovdcNetwork</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">OvDC network</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">VCD network to connect VMs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-site">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.site</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Endpoint</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">VCD endpoint URL in the format https://VCD_HOST, without trailing slash.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-userContext">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.userContext</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VCD API access token</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-userContext-secretRef">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.userContext.secretRef</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret reference</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-userContext-secretRef-secretName">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.userContext.secretRef.secretName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the secret containing the VCD API token.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-vmNamingTemplate">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.vmNamingTemplate</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VM naming template</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Go template to specify the VM naming convention.</div>
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
      <div class="property-meta"><span class="property-title">Management cluster name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The Cluster API management cluster that manages this cluster.</div>
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

- [Source repository](https://github.com/giantswarm/cluster-cloud-director)
