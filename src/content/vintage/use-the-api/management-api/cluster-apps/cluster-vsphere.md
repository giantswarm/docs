---
title: Cluster-Vsphere chart reference
linkTitle: cluster-vsphere chart reference
description: |
  A helm chart for creating Cluster API clusters with the vSphere provider (CAPV).; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: cluster-vsphere
    parent: uiapi-cluster-apps
layout: cluster-app
last_review_date: 2024-03-04
user_questions:
 - What properties can I configure for cluster-vsphere?
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/cluster-vsphere
source_repository_ref: v0.9.8
---

The `default-apps-vsphere` chart templates all the VMware infrastructure resources that are necessary to create a Cluster API vSphere cluster.

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
        <a class="header-link" href="#internal-sandboxContainerImage">
          <i class="fa fa-link"></i>
        </a>.internal.sandboxContainerImage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Sandbox Container image</span><br /><span class="property-type">object</span>&nbsp;
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
    <a class="header-link" href="#Cluster">
      <i class="fa fa-link"></i>
    </a>Cluster
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#cluster-kubernetesVersion">
          <i class="fa fa-link"></i>
        </a>.cluster.kubernetesVersion</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubernetes version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
        <a class="header-link" href="#connectivity-network-allowAllEgress">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.allowAllEgress</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Allow all egress</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-containerRegistries">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*]</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]-credentials">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*].credentials</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]-credentials-auth">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*].credentials.auth</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]-credentials-identitytoken">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*].credentials.identitytoken</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]-credentials-password">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*].credentials.password</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]-credentials-username">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*].credentials.username</h3>
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
        <a class="header-link" href="#connectivity-network-containerRegistries-*[*]-endpoint">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.containerRegistries.*[*].endpoint</h3>
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
        <a class="header-link" href="#connectivity-network-controlPlaneEndpoint">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlaneEndpoint</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Endpoint</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes API configuration.</div>
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
      <div class="property-description">IP for access to the Kubernetes API.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#connectivity-network-controlPlaneEndpoint-ipPoolName">
          <i class="fa fa-link"></i>
        </a>.connectivity.network.controlPlaneEndpoint.ipPoolName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Ip Pool Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Ip for control plane will be drawn from this GlobalInClusterIPPool resource.</div>
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
      <div class="property-description">Port for access to the Kubernetes API.</div>
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
      <div class="property-meta"><span class="property-title">Load balancers</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
  <h3 class="headline-with-link">
    <a class="header-link" href="#Control-plane">
      <i class="fa fa-link"></i>
    </a>Control plane
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-etcd">
          <i class="fa fa-link"></i>
        </a>.controlPlane.etcd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Etcd</span><br /><span class="property-type">object</span>&nbsp;
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
      <div class="property-meta"><span class="property-title">Image repository</span><br /><span class="property-type">string</span>&nbsp;
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
      <div class="property-meta"><span class="property-title">Image tag</span><br /><span class="property-type">string</span>&nbsp;
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
  <h3 class="headline-with-link">
    <a class="header-link" href="#Kubeadm">
      <i class="fa fa-link"></i>
    </a>Kubeadm
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#kubeadm-users">
          <i class="fa fa-link"></i>
        </a>.kubeadm.users</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Users</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#kubeadm-users[*]">
          <i class="fa fa-link"></i>
        </a>.kubeadm.users[*]</h3>
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
        <a class="header-link" href="#kubeadm-users[*]-authorizedKeys">
          <i class="fa fa-link"></i>
        </a>.kubeadm.users[*].authorizedKeys</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Authorized keys</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#kubeadm-users[*]-authorizedKeys[*]">
          <i class="fa fa-link"></i>
        </a>.kubeadm.users[*].authorizedKeys[*]</h3>
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
        <a class="header-link" href="#kubeadm-users[*]-name">
          <i class="fa fa-link"></i>
        </a>.kubeadm.users[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
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
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
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
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Kubernetes-API-server">
      <i class="fa fa-link"></i>
    </a>Kubernetes API server
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apiServer-certSANs">
          <i class="fa fa-link"></i>
        </a>.apiServer.certSANs</h3>
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
        <a class="header-link" href="#apiServer-certSANs[*]">
          <i class="fa fa-link"></i>
        </a>.apiServer.certSANs[*]</h3>
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
        <a class="header-link" href="#apiServer-enableAdmissionPlugins">
          <i class="fa fa-link"></i>
        </a>.apiServer.enableAdmissionPlugins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Admission plugins</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Comma-separated list of admission plugins to enable.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#apiServer-featureGates">
          <i class="fa fa-link"></i>
        </a>.apiServer.featureGates</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gates</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Enabled feature gates, as a comma-separated list.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Kubernetes-Controller-Manager">
      <i class="fa fa-link"></i>
    </a>Kubernetes Controller Manager
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controllerManager-featureGates">
          <i class="fa fa-link"></i>
        </a>.controllerManager.featureGates</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gates</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Enabled feature gates, as a comma-separated list.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Node-template">
      <i class="fa fa-link"></i>
    </a>Node template
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Provisioning options for node templates.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-cloneMode">
          <i class="fa fa-link"></i>
        </a>.template.cloneMode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Clone mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Method used to clone template image.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-diskGiB">
          <i class="fa fa-link"></i>
        </a>.template.diskGiB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Disk size (GB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Node disk size in GB. Must be at least as large as the source image.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-folder">
          <i class="fa fa-link"></i>
        </a>.template.folder</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Folder</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">VSphere folder to deploy instances in. Must already exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-memoryMiB">
          <i class="fa fa-link"></i>
        </a>.template.memoryMiB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Memory (MB)</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Node memory allocation in MB.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-networkName">
          <i class="fa fa-link"></i>
        </a>.template.networkName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Segment name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Segment name to attach nodes to. Must already exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-numCPUs">
          <i class="fa fa-link"></i>
        </a>.template.numCPUs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">CPU cores</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Number of CPUs to assign per node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-resourcePool">
          <i class="fa fa-link"></i>
        </a>.template.resourcePool</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resource pool</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Resource pool to allocate nodes from. Must already exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-storagePolicyName">
          <i class="fa fa-link"></i>
        </a>.template.storagePolicyName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage policy</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Storage policy to use. If specified, it must already exist.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#template-templateName">
          <i class="fa fa-link"></i>
        </a>.template.templateName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Image template name to use for nodes.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#VCenter">
      <i class="fa fa-link"></i>
    </a>VCenter
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Configuration for vSphere API access.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-datacenter">
          <i class="fa fa-link"></i>
        </a>.vcenter.datacenter</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Datacenter</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the datacenter to deploy nodes into.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-datastore">
          <i class="fa fa-link"></i>
        </a>.vcenter.datastore</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Datastore</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the datastore for node disk storage.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-password">
          <i class="fa fa-link"></i>
        </a>.vcenter.password</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Password</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Password for the VSphere API.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-region">
          <i class="fa fa-link"></i>
        </a>.vcenter.region</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Region</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Category name in VSphere for topology.kubernetes.io/region labels.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-server">
          <i class="fa fa-link"></i>
        </a>.vcenter.server</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Server</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">URL of the VSphere API.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-thumbprint">
          <i class="fa fa-link"></i>
        </a>.vcenter.thumbprint</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Thumbprint</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">TLS certificate signature of the VSphere API.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-username">
          <i class="fa fa-link"></i>
        </a>.vcenter.username</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Username for the VSphere API.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#vcenter-zone">
          <i class="fa fa-link"></i>
        </a>.vcenter.zone</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Zone</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Category name in VSphere for topology.kubernetes.io/zone labels.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Worker">
      <i class="fa fa-link"></i>
    </a>Worker
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#worker-replicas">
          <i class="fa fa-link"></i>
        </a>.worker.replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Number of nodes</span><br /><span class="property-type">integer</span>&nbsp;
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
        <a class="header-link" href="#organization">
          <i class="fa fa-link"></i>
        </a>.organization</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Organization</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div></div>


<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-vsphere)
