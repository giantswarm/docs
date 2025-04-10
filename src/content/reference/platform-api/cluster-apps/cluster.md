---
title: cluster chart reference
linkTitle: cluster
description:  Giant Swarm cluster chart with provider-independent cluster resources; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster
    parent: reference-cluster-apps
layout: cluster-app
last_review_date: 2024-03-05
user_questions:
 - What properties can I configure for cluster?
owner:
- https://github.com/orgs/giantswarm/teams/team-turtles
source_repository: https://github.com/giantswarm/cluster
source_repository_ref: v0.7.0
---

The `cluster` chart is the main entry point for the Giant Swarm platform. It is the first app that is installed on a new cluster. It is responsible for setting up the basic infrastructure and installing the necessary components to make the cluster operational.

<div class="crd-schema-version">
  <h2 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Chart Configuration Reference
  </h2>
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
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Configuration of connectivity and networking options.
  </h4>
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
        <a class="header-link" href="#global-connectivity-bastion">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Bastion host</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-bastion-enabled">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion.enabled</h3>
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
        <a class="header-link" href="#global-connectivity-bastion-replicas">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion.replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Number of hosts</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description"></div>
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
      <div class="property-meta"><span class="property-title">Kubernetes Service subnets</span><br /><span class="property-type">array</span>&nbsp;
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
      <div class="property-description">Comma-separated addresses to be passed to the NO_PROXY environment variable in all hosts.</div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Control-plane">
      <i class="fa fa-link"></i>
    </a>Control plane
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Configuration of the control plane.
  </h4>
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
        <a class="header-link" href="#global-controlPlane-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.customNodeTaints</h3>
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
        <a class="header-link" href="#global-controlPlane-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.customNodeTaints[*]</h3>
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
        <a class="header-link" href="#global-controlPlane-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.customNodeTaints[*].effect</h3>
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
        <a class="header-link" href="#global-controlPlane-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.customNodeTaints[*].key</h3>
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
        <a class="header-link" href="#global-controlPlane-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.customNodeTaints[*].value</h3>
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
        <a class="header-link" href="#global-controlPlane-replicas">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Replicas</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The number of control plane nodes.</div>
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
        <a class="header-link" href="#internal-advancedConfiguration">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Advanced configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Advanced configuration of cluster components, to be configured by Giant Swarm staff only.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-cgroupsv1">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.cgroupsv1</h3>
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
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control plane</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Advanced configuration of control plane components.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-apiServer">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.apiServer</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API server</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Advanced configuration of API server.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-apiServer-bindPort">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.apiServer.bindPort</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Bind port</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes API bind port used for API server pod.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-apiServer-etcdPrefix">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.apiServer.etcdPrefix</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">etcd prefix</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The prefix to prepend to all resource paths in etcd. If nothing is specified, the API server uses '/registry' prefix by default.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-apiServer-extraArgs">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.apiServer.extraArgs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra CLI args</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">A map with the additional CLI flags that are appended to the default flags. Use with caution, as there is no validation for these values, so you can set incorrect or duplicate flags.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-apiServer-extraCertificateSANs">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.apiServer.extraCertificateSANs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra certificate SANs</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The additional certificate SANs that are appended to the default SANs. Use with caution, as there is no validation for these values, so you can set incorrect or duplicate certificates.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-apiServer-extraCertificateSANs[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.apiServer.extraCertificateSANs[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra certificate SAN</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">etcd</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of etcd</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd-experimental">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd.experimental</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Experimental</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd-experimental-peerSkipClientSanVerification">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd.experimental.peerSkipClientSanVerification</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Peer skip client SAN verification</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Skip verification of SAN field in client certificate for peer connections.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd-extraArgs">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd.extraArgs</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Extra args</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd-initialCluster">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd.initialCluster</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Initial cluster</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Initial cluster configuration for bootstrapping.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd-initialClusterState">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd.initialClusterState</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Initial cluster state</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-etcd-quotaBackendBytesGiB">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.etcd.quotaBackendBytesGiB</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Quota backend bytes in GiB</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">Raise the etcd default backend bytes limit up to 16GiB.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Custom cluster-specific files that are deployed to control plane nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File from secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It defines a file with content in a Secret</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies where the file content is coming from.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes Secret resource with the file content.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Secret key where the file content is.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Secret resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]-path">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File path on the node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-files[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.files[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Permissions</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File permissions in form 0644</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-postKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.postKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Post-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run after kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-postKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.postKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-controlPlane-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.controlPlane.preKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#internal-advancedConfiguration-files">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Custom cluster-specific files that are deployed to all nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File from secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It defines a file with content in a Secret</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies where the file content is coming from.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes Secret resource with the file content.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Secret key where the file content is.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Secret resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]-path">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File path on the node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-files[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.files[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Permissions</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File permissions in form 0644</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-postKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.postKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Post-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run after kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-postKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.postKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#internal-advancedConfiguration-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.preKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#internal-advancedConfiguration-workers">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Workers</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Advanced configuration of worker nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Custom cluster-specific files that are deployed to worker nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File from secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It defines a file with content in a Secret</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies where the file content is coming from.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes Secret resource with the file content.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Secret key where the file content is.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Secret resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]-path">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File path on the node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-files[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.files[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Permissions</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File permissions in form 0644</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-postKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.postKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Post-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run after kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-postKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.postKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#internal-advancedConfiguration-workers-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#internal-advancedConfiguration-workers-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.internal.advancedConfiguration.workers.preKubeadmCommands[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
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
        <a class="header-link" href="#global-metadata-annotations">
          <i class="fa fa-link"></i>
        </a>.global.metadata.annotations</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Annotations</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">These annotations are added to all Kubernetes resources defining this cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-annotations-PATTERN">
          <i class="fa fa-link"></i>
        </a>.global.metadata.annotations.PATTERN</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Annotation</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
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
        <a class="header-link" href="#global-metadata-labels">
          <i class="fa fa-link"></i>
        </a>.global.metadata.labels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Labels</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">These labels are added to all Kubernetes resources defining this cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-metadata-labels-PATTERN">
          <i class="fa fa-link"></i>
        </a>.global.metadata.labels.PATTERN</h3>
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
      <div class="property-description">The name of organization that owns the cluster.</div>
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
      <div class="property-description">Setting this to true will set giantswarm.io/prevent-deletion label to true, which will block cluster deletion.</div>
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
        <a class="header-link" href="#global-nodePools-PATTERN-annotations">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.annotations</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Annotations</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">These annotations are added to all Kubernetes resources defining this node pool.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-annotations-PATTERN_2">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.annotations.PATTERN_2</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Annotation</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-labels">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.labels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Labels</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">These labels are added to all Kubernetes resources defining this node pool.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-labels-PATTERN_2">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.labels.PATTERN_2</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-nodeLabels">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeLabels</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Node labels</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Labels that are passed to kubelet argument 'node-labels'.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-nodePools-PATTERN-nodeLabels-*">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeLabels.*</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-nodeTaints">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeTaints</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-nodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeTaints[*]</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-nodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeTaints[*].effect</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-nodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeTaints[*].key</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-nodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.nodeTaints[*].value</h3>
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
        <a class="header-link" href="#global-nodePools-PATTERN-replicas">
          <i class="fa fa-link"></i>
        </a>.global.nodePools.PATTERN.replicas</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Replicas</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The number of node pool nodes.</div>
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
    <a class="header-link" href="#Provider-integration">
      <i class="fa fa-link"></i>
    </a>Provider integration
  </h3>
  <h4 class="headline-with-link">
    <a class="header-link" href="#">
      <i class="fa fa-link"></i>
    </a>Provider-specific properties that can be set by cluster-$provider chart in order to render correct templates for the provider.
  </h4>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Internal bastion configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubeadm config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of bastion nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Ignition</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Ignition-specific configuration.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Container Linux configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the system’s storage devices.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directories</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of directories to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directory</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The directory to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-filesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Filesystem</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the group of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The group ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The group name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-mode">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mode</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The directory’s permission mode.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-overwrite">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Overwrite</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether to delete preexisting nodes at the path.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the directory.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">User</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the directory’s owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The user ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The user name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File systems</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File system</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-device">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Device</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-format">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Format</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The filesystem format (ext4, btrfs, or xfs).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-label">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The label of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Options</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Any additional options to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An additional option to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-uuid">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">UUID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The uuid of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-wipeFilesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Wipe filesystem</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the systemd units.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Units</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The contents of the unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Install</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Install] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">WantedBy</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Units with (weak) requirement dependencies on this unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]</h3>
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
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Mount] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-type">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">A file system type to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-what">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">What</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a device node, file or other resource to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-where">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Where</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Unit] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-defaultDependencies">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">DefaultDependencies</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if this systemd unit should have the default systemd unit dependencies.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-description">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Description</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">systemd unit description.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-ins</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of drop-ins for the unit</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-in</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The contents of the drop-in.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the drop-in. This must be suffixed with “.conf”</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enabled?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-mask">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Masked?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-ignition-containerLinuxConfig-strict">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.strict</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Strict</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-bastion-kubeadmConfig-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.bastion.kubeadmConfig.preKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#providerIntegration-clusterAnnotationsTemplateName">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.clusterAnnotationsTemplateName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster annotations template name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the template that renders provider-specific annotations for the Cluster resource</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-components">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Components</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Internal configuration of various components that form the Kubernetes cluster.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-components-containerd">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components.containerd</h3>
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
        <a class="header-link" href="#providerIntegration-components-containerd-sandboxContainerImage">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components.containerd.sandboxContainerImage</h3>
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
        <a class="header-link" href="#providerIntegration-components-containerd-sandboxContainerImage-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components.containerd.sandboxContainerImage.name</h3>
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
        <a class="header-link" href="#providerIntegration-components-containerd-sandboxContainerImage-registry">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components.containerd.sandboxContainerImage.registry</h3>
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
        <a class="header-link" href="#providerIntegration-components-containerd-sandboxContainerImage-tag">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components.containerd.sandboxContainerImage.tag</h3>
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
        <a class="header-link" href="#providerIntegration-components-systemd">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.components.systemd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd</span><br />
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-connectivity">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Connectivity</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Internal connectivity configuration.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-connectivity-proxy">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity.proxy</h3>
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
        <a class="header-link" href="#providerIntegration-connectivity-proxy-noProxy">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity.proxy.noProxy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">No proxy</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">To be passed to the NO_PROXY environment variable in all hosts.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-connectivity-proxy-noProxy-templateName">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity.proxy.noProxy.templateName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Template name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of Helm template that renders a YAML array with NO_PROXY addresses.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-connectivity-proxy-noProxy-value">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity.proxy.noProxy.value</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Value</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Pre-defined static NO_PROXY values.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-connectivity-proxy-noProxy-value[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity.proxy.noProxy.value[*]</h3>
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
        <a class="header-link" href="#providerIntegration-connectivity-sshSsoPublicKey">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.connectivity.sshSsoPublicKey</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">SSH public key for single sign-on</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Provider-specific control plane configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubeadm config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of control plane nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of Kubernetes components.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API server</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of API server.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-additionalAdmissionPlugins">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.additionalAdmissionPlugins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional admission plugins</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">A list of plugins to enable, in addition to the default ones that include DefaultStorageClass, DefaultTolerationSeconds, LimitRanger, MutatingAdmissionWebhook, NamespaceLifecycle, PersistentVolumeClaimResize, Priority, ResourceQuota, ServiceAccount and ValidatingAdmissionWebhook.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-additionalAdmissionPlugins[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.additionalAdmissionPlugins[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional admission plugin</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-apiAudiences">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API audiences</span><br />
      </div>
      <div class="property-description">Identifiers of the API. The service account token authenticator will validate that tokens used against the API are bound to at least one of these audiences. If the --service-account-issuer flag is configured and this flag is not, 'api-audiences' field defaults to a single element list containing the issuer URL.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-featureGates">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Feature gates</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-featureGates[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates[*]</h3>
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
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-featureGates[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates[*].enabled</h3>
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
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-featureGates[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates[*].name</h3>
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
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-clusterConfiguration-apiServer-serviceAccountIssuer">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Service account issuer</span><br />
      </div>
      <div class="property-description">Configuration of the identifier of the service account token issuer. You must specify either URL or clusterDomainPrefix (only one, not both).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Provider-specific files that are deployed to control plane nodes. They are specified in the cluster-<provider> apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File from secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It defines a file with content in a Secret</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies where the file content is coming from.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes Secret resource with the file content.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Secret key where the file content is.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Secret resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File path on the node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-files[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.files[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Permissions</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File permissions in form 0644</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Ignition</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Ignition-specific configuration.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Container Linux configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the system’s storage devices.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directories</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of directories to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directory</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The directory to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-filesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Filesystem</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the group of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The group ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The group name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-mode">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mode</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The directory’s permission mode.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-overwrite">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Overwrite</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether to delete preexisting nodes at the path.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the directory.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">User</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the directory’s owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The user ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The user name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File systems</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File system</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-device">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Device</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-format">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Format</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The filesystem format (ext4, btrfs, or xfs).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-label">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The label of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Options</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Any additional options to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An additional option to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-uuid">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">UUID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The uuid of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-wipeFilesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Wipe filesystem</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the systemd units.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Units</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The contents of the unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Install</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Install] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">WantedBy</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Units with (weak) requirement dependencies on this unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]</h3>
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
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Mount] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-type">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">A file system type to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-what">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">What</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a device node, file or other resource to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-where">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Where</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Unit] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-defaultDependencies">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">DefaultDependencies</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if this systemd unit should have the default systemd unit dependencies.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-description">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Description</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">systemd unit description.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-ins</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of drop-ins for the unit</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-in</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The contents of the drop-in.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the drop-in. This must be suffixed with “.conf”</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enabled?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-mask">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Masked?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-ignition-containerLinuxConfig-strict">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.strict</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Strict</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-postKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.postKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Post-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run after kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-postKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.postKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-kubeadmConfig-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.kubeadmConfig.preKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#providerIntegration-controlPlane-resources">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resources configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">GVK and other configuration for control plane resources.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-controlPlane">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.controlPlane</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control plane resource config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-controlPlane-api">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.controlPlane.api</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Schema for Kubernetes API group, version and kind</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It can be used to specify which CustomResourceDefinition is used.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-controlPlane-api-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.controlPlane.api.group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-controlPlane-api-kind">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.controlPlane.api.kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-controlPlane-api-version">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.controlPlane.api.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-infrastructureMachineTemplate">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.infrastructureMachineTemplate</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Infrastructure Machine template</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Group, version and kind of provider-specific infrastructure Machine template resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-infrastructureMachineTemplate-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.infrastructureMachineTemplate.group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-infrastructureMachineTemplate-kind">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.infrastructureMachineTemplate.kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-infrastructureMachineTemplate-version">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.infrastructureMachineTemplate.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-controlPlane-resources-infrastructureMachineTemplateSpecTemplateName">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.controlPlane.resources.infrastructureMachineTemplateSpecTemplateName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Infrastructure Machine template spec template name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of Helm template that renders Infrastructure Machine template spec.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-hashSalt">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.hashSalt</h3>
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
        <a class="header-link" href="#providerIntegration-kubeadmConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Provider-specific kubeadm config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Provider-specific kubeadm config that is common for all nodes, including both control plane and workers.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Provider-specific files that are deployed to all nodes. They are specified in the cluster-<provider> apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File from secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It defines a file with content in a Secret</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies where the file content is coming from.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes Secret resource with the file content.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Secret key where the file content is.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Secret resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File path on the node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-files[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.files[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Permissions</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File permissions in form 0644</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Ignition</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Ignition-specific configuration.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Container Linux configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the system’s storage devices.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directories</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of directories to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directory</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The directory to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-filesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Filesystem</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the group of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The group ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The group name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-mode">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mode</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The directory’s permission mode.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-overwrite">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Overwrite</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether to delete preexisting nodes at the path.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the directory.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">User</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the directory’s owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The user ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The user name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File systems</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File system</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-device">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Device</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-format">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Format</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The filesystem format (ext4, btrfs, or xfs).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-label">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The label of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Options</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Any additional options to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An additional option to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-uuid">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">UUID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The uuid of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-wipeFilesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Wipe filesystem</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the systemd units.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Units</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The contents of the unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Install</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Install] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">WantedBy</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Units with (weak) requirement dependencies on this unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]</h3>
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
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Mount] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-type">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">A file system type to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-what">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">What</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a device node, file or other resource to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-where">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Where</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Unit] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-defaultDependencies">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">DefaultDependencies</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if this systemd unit should have the default systemd unit dependencies.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-description">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Description</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">systemd unit description.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-ins</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of drop-ins for the unit</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-in</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The contents of the drop-in.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the drop-in. This must be suffixed with “.conf”</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enabled?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-mask">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Masked?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-ignition-containerLinuxConfig-strict">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.strict</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Strict</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-postKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.postKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Post-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run after kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-postKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.postKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#providerIntegration-kubeadmConfig-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-kubeadmConfig-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubeadmConfig.preKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#providerIntegration-kubernetesVersion">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.kubernetesVersion</h3>
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
        <a class="header-link" href="#providerIntegration-pauseProperties">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.pauseProperties</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pause properties</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">A map of property names and their values that will affect setting pause annotation</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-pauseProperties-*">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.pauseProperties.*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>, <span class="property-type">number</span>, <span class="property-type">integer</span>, <span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-provider">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.provider</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Provider</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the Cluster API provider. The name here must match the name of the provider in cluster-<provider> app name.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Resources API</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Group, version and kind configuration that is required and used by a specific Cluster API provider.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-bastionResourceEnabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.bastionResourceEnabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Bastion resource enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if the Bastion resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-clusterResourceEnabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.clusterResourceEnabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster resource enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if the Cluster resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-controlPlaneResourceEnabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.controlPlaneResourceEnabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Control plane resource enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if the control plane resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-infrastructureCluster">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.infrastructureCluster</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Infrastructure cluster</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Group, version and kind of provider-specific infrastructure cluster resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-infrastructureCluster-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.infrastructureCluster.group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-infrastructureCluster-kind">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.infrastructureCluster.kind</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API kind</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-infrastructureCluster-version">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.infrastructureCluster.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">API version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-machineHealthCheckResourceEnabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.machineHealthCheckResourceEnabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">MachineHealthCheck resource enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if the MachineHealthCheck resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-resourcesApi-machinePoolResourcesEnabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.resourcesApi.machinePoolResourcesEnabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Machine pool resources enabled</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if the machine pool resources are enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-teleport">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.teleport</h3>
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
        <a class="header-link" href="#providerIntegration-teleport-enabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.teleport.enabled</h3>
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
        <a class="header-link" href="#providerIntegration-teleport-proxyAddr">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.teleport.proxyAddr</h3>
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
        <a class="header-link" href="#providerIntegration-teleport-version">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.teleport.version</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Teleport version</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Provider-specific workers configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubeadm config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of workers nodes.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Files</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Provider-specific files that are deployed to worker nodes. They are specified in the cluster-<provider> apps.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File from secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It defines a file with content in a Secret</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]-contentFrom">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*].contentFrom</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Content from</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies where the file content is coming from.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]-contentFrom-secret">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*].contentFrom.secret</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Secret</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes Secret resource with the file content.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]-contentFrom-secret-key">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*].contentFrom.secret.key</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Key</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Secret key where the file content is.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]-contentFrom-secret-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*].contentFrom.secret.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the Secret resource.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File path on the node.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-files[*]-permissions">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.files[*].permissions</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Permissions</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">File permissions in form 0644</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Ignition</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Ignition-specific configuration.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Container Linux configuration</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Storage</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the system’s storage devices.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directories</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of directories to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Directory</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The directory to be created.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-filesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Filesystem</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Group</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the group of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The group ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-group-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The group name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-mode">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mode</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The directory’s permission mode.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-overwrite">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Overwrite</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether to delete preexisting nodes at the path.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the directory.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">User</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It specifies the directory’s owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-id">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">ID</span><br /><span class="property-type">integer</span>&nbsp;
      </div>
      <div class="property-description">The user ID of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-directories[*]-user-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The user name of the owner.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File systems</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">File system</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-device">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Device</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-format">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Format</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The filesystem format (ext4, btrfs, or xfs).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-label">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Label</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The label of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Options</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Any additional options to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-options[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An additional option to be passed to the format-specific mkfs utility.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-uuid">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">UUID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The uuid of the filesystem.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-mount-wipeFilesystem">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Wipe filesystem</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-storage-filesystems[*]-path">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Path</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">It describes the desired state of the systemd units.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Units</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">systemd unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">The contents of the unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Install</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Install] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">WantedBy</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Units with (weak) requirement dependencies on this unit.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-install-wantedBy[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]</h3>
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
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mount</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Mount] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-type">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Type</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">A file system type to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-what">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">What</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a device node, file or other resource to mount.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-mount-where">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Where</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Configuration of the [Unit] section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-defaultDependencies">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">DefaultDependencies</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Flag that indicates if this systemd unit should have the default systemd unit dependencies.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-contents-unit-description">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Description</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">systemd unit description.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-ins</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">The list of drop-ins for the unit</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Unit drop-in</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-contents">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Contents</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The contents of the drop-in.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-dropins[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the drop-in. This must be suffixed with “.conf”</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-enabled">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Enabled?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-mask">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Masked?</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-additionalConfig-systemd-units[*]-name">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-ignition-containerLinuxConfig-strict">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.strict</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Strict</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-postKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.postKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Post-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run after kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-postKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.postKubeadmCommands[*]</h3>
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
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-preKubeadmCommands">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.preKubeadmCommands</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pre-kubeadm commands</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Extra commands to run before kubeadm runs.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerIntegration-workers-kubeadmConfig-preKubeadmCommands[*]">
          <i class="fa fa-link"></i>
        </a>.providerIntegration.workers.kubeadmConfig.preKubeadmCommands[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div></div>

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster)
