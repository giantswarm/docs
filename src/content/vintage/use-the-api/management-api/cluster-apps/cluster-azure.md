---
title: cluster-azure chart reference
linkTitle: cluster-azure
description:  A helm chart for creating Cluster API clusters with the Azure infrastructure provider (CAPZ).; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: cluster-azure
    parent: uiapi-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-azure?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-azure
source_repository_ref: v0.0.35
---

The `cluster-azure` chart templates all the Azure infrastructure resources that are necessary to create a Cluster API Azure cluster.

<!-- INTRO_END -->
# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

Note that configuration options can change between releases. Use the GitHub function for selecting a branch/tag to view the documentation matching your cluster-aws version.

<!-- Update the content below by executing (from the repo root directory)

schemadocs generate helm/cluster-azure/values.schema.json -o helm/cluster-azure/README.md

-->

<!-- DOCS_START -->

<div class="crd-schema-version">
  <h2 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Chart Configuration Reference
  </h2>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Azure-settings">
      <i class="fa fa-link"></i>
    </a>Azure settings
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-azureClusterIdentity">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.azureClusterIdentity</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Identity</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">AzureClusterIdentity resource to use for this cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-azureClusterIdentity-name">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.azureClusterIdentity.name</h3>
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
        <a class="header-link" href="#providerSpecific-azureClusterIdentity-namespace">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.azureClusterIdentity.namespace</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Namespace</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-location">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.location</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Location</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-network">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.network</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Azure network settings</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Azure VNet peering and other Azure-specific network settings.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-network-peerings">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.network.peerings</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VNet peerings</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Specifying VNets (their resource groups and names) to which the peering is established.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-network-peerings[*]">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.network.peerings[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VNet peering</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-network-peerings[*]-remoteVnetName">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.network.peerings[*].remoteVnetName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VNet name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the remote VNet to which the peering is established.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-network-peerings[*]-resourceGroup">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.network.peerings[*].resourceGroup</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resource group name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Resource group for the remote VNet to which the peering is established.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-subscriptionId">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.subscriptionId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subscription ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">ID of the Azure subscription this cluster will run in.</div>
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
        <a class="header-link" href="#connectivity-allowedCIDRs">
          <i class="fa fa-link"></i>
        </a>.connectivity.allowedCIDRs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">List of CIDRs which have to been allowed to connect to the API Server endpoint</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-allowedCIDRs[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.allowedCIDRs[*]</h3>
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
      <div class="property-meta"><span class="property-title">Registries</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Container registries and mirrors</div>
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
      <div class="property-meta"><span class="property-title">Registry</span><br /><span class="property-type">object</span>&nbsp;
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
      <div class="property-description"></div>
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
        <a class="header-link" href="#connectivity-network-controlPlane">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlane</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control plane</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-controlPlane-cidr">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlane.cidr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-hostCidr">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.hostCidr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range for nodes, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-mode">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Network mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Specifying if the cluster resources are publicly accessible or not.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-podCidr">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.podCidr</h3>
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
        <a class="header-link" href="#connectivity-network-serviceCidr">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.serviceCidr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Service subnet</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">IPv4 address range for services, in CIDR notation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-workers">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.workers</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Workers</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-workers-cidr">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.workers.cidr</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet</span><br /><span class="property-type">string</span>&nbsp;
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
        <a class="header-link" href="#controlPlane-containerdVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.controlPlane.containerdVolumeSizeGB</h3>
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
        <a class="header-link" href="#controlPlane-encryptionAtHost">
          <i class="fa fa-link"></i>
        </a>.controlPlane.encryptionAtHost</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Encryption at host</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Enable encryption at host for the control plane nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-etcdVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.controlPlane.etcdVolumeSizeGB</h3>
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
        <a class="header-link" href="#controlPlane-instanceType">
          <i class="fa fa-link"></i>
        </a>.controlPlane.instanceType</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node VM size</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-kubeletVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.controlPlane.kubeletVolumeSizeGB</h3>
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
        <a class="header-link" href="#controlPlane-oidc-caPem">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.caPem</h3>
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
        <a class="header-link" href="#controlPlane-oidc-clientId">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.clientId</h3>
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
        <a class="header-link" href="#controlPlane-oidc-groupsClaim">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.groupsClaim</h3>
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
        <a class="header-link" href="#controlPlane-oidc-issuerUrl">
          <i class="fa fa-link"></i>
        </a>.controlPlane.oidc.issuerUrl</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Issuer URL</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
      <div class="property-description"></div>
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
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.controlPlane.rootVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Root volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Internal-settings">
      <i class="fa fa-link"></i>
    </a>Internal settings
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-defaults">
          <i class="fa fa-link"></i>
        </a>.internal.defaults</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default settings</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-defaults-evictionMinimumReclaim">
          <i class="fa fa-link"></i>
        </a>.internal.defaults.evictionMinimumReclaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default settings for eviction minimum reclaim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-defaults-hardEvictionThresholds">
          <i class="fa fa-link"></i>
        </a>.internal.defaults.hardEvictionThresholds</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default settings for hard eviction thresholds</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-defaults-softEvictionGracePeriod">
          <i class="fa fa-link"></i>
        </a>.internal.defaults.softEvictionGracePeriod</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default settings for soft eviction grace period</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-defaults-softEvictionThresholds">
          <i class="fa fa-link"></i>
        </a>.internal.defaults.softEvictionThresholds</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Default settings for soft eviction thresholds</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-enableVpaResources">
          <i class="fa fa-link"></i>
        </a>.internal.enableVpaResources</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enable VPA Resources in helmreleases</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-identity">
          <i class="fa fa-link"></i>
        </a>.internal.identity</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Identity</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-identity-attachCapzControllerUserAssignedIdentity">
          <i class="fa fa-link"></i>
        </a>.internal.identity.attachCapzControllerUserAssignedIdentity</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Attach CAPZ controller UserAssigned identity</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-identity-systemAssignedScope">
          <i class="fa fa-link"></i>
        </a>.internal.identity.systemAssignedScope</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Scope of SystemAssignedIdentity</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-identity-type">
          <i class="fa fa-link"></i>
        </a>.internal.identity.type</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Type of Identity</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-identity-userAssignedCustomIdentities">
          <i class="fa fa-link"></i>
        </a>.internal.identity.userAssignedCustomIdentities</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">List of custom UserAssigned Identities to attach to all nodes</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-image">
          <i class="fa fa-link"></i>
        </a>.internal.image</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node Image</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-image-gallery">
          <i class="fa fa-link"></i>
        </a>.internal.image.gallery</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Gallery</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the community gallery hosting the image</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-image-name">
          <i class="fa fa-link"></i>
        </a>.internal.image.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Image Definition</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the image definition in the Gallery</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-image-version">
          <i class="fa fa-link"></i>
        </a>.internal.image.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Image version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-kubectlImage">
          <i class="fa fa-link"></i>
        </a>.internal.kubectlImage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubectl Image settings</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-kubectlImage-name">
          <i class="fa fa-link"></i>
        </a>.internal.kubectlImage.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Image name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the image Registry</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-kubectlImage-registry">
          <i class="fa fa-link"></i>
        </a>.internal.kubectlImage.registry</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubectl Image Registry</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Registry for the kubectl image</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-kubectlImage-tag">
          <i class="fa fa-link"></i>
        </a>.internal.kubectlImage.tag</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Image tag</span><br /><span class="property-type">string</span>&nbsp;
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
        <a class="header-link" href="#internal-network">
          <i class="fa fa-link"></i>
        </a>.internal.network</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Network configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Internal network configuration that is susceptible to more frequent change</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-subnets">
          <i class="fa fa-link"></i>
        </a>.internal.network.subnets</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VNet spec</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Customize subnets configuration</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-subnets-controlPlaneSubnetName">
          <i class="fa fa-link"></i>
        </a>.internal.network.subnets.controlPlaneSubnetName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ControlPlane subnet name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the control plane subnet.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-subnets-nodeSubnetNatGatewayName">
          <i class="fa fa-link"></i>
        </a>.internal.network.subnets.nodeSubnetNatGatewayName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Nodes subnet nat-gateway name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the nat gateway on the nodes subnet.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-subnets-nodesSubnetName">
          <i class="fa fa-link"></i>
        </a>.internal.network.subnets.nodesSubnetName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Nodes subnet name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the nodes subnet.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-vnet">
          <i class="fa fa-link"></i>
        </a>.internal.network.vnet</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VNet spec</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Existing VNet configuration. This is susceptible to more frequent change or removal.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-vnet-name">
          <i class="fa fa-link"></i>
        </a>.internal.network.vnet.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VNet name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the existing VNet.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-vnet-resourceGroup">
          <i class="fa fa-link"></i>
        </a>.internal.network.vnet.resourceGroup</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resource group name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Resource group where the existing VNet is deployed.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-vpn">
          <i class="fa fa-link"></i>
        </a>.internal.network.vpn</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPN configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Internal VPN configuration that is susceptible to more frequent change</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-network-vpn-gatewayMode">
          <i class="fa fa-link"></i>
        </a>.internal.network.vpn.gatewayMode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPN gateway mode</span><br /><span class="property-type">string</span>&nbsp;
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
      <div class="property-meta"><span class="property-title">The image used by sandbox / pause container</span><br /><span class="property-type">object</span>&nbsp;
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
        <a class="header-link" href="#metadata-name">
          <i class="fa fa-link"></i>
        </a>.metadata.name</h3>
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
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeLabels</h3>
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
        <a class="header-link" href="#nodePools[*]-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeLabels[*]</h3>
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
        <a class="header-link" href="#nodePools[*]-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeTaints</h3>
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
        <a class="header-link" href="#nodePools[*]-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeTaints[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node taint</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeTaints[*].effect</h3>
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
        <a class="header-link" href="#nodePools[*]-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeTaints[*].key</h3>
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
        <a class="header-link" href="#nodePools[*]-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].customNodeTaints[*].value</h3>
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
        <a class="header-link" href="#nodePools[*]-disableHealthCheck">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].disableHealthCheck</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Disable HealthChecks for the MachineDeployment</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-encryptionAtHost">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].encryptionAtHost</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Encryption at host</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Enable encryption at host for the worker nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-failureDomain">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].failureDomain</h3>
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
        <a class="header-link" href="#nodePools[*]-instanceType">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].instanceType</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VM size</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-name">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Unique identifier, cannot be changed after creation.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-replicas">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools[*]-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.nodePools[*].rootVolumeSizeGB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Root volume size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
      <div class="property-meta"><span class="property-title">Enforced Pod Security Standards</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Use PSSs instead of PSPs.</div>
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
      <div class="property-meta"><span class="property-title">The capi MC managing this cluster</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
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

- [Source repository](https://github.com/giantswarm/cluster-azure)
