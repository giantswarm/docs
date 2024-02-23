---
title: Cluster-Aws chart reference
linkTitle: cluster-aws chart reference
description: |
  A helm chart for creating Cluster API clusters with the AWS infrastructure provider (CAPA).
weight: 100
menu:
  main:
    identifier: cluster-aws
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-aws
source_repository_ref: v0.60.1
---

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
        <a class="header-link" href="#providerSpecific-ami">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.ami</h3>
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
        <a class="header-link" href="#providerSpecific-awsClusterRoleIdentityName">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.awsClusterRoleIdentityName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Cluster role identity name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of an AWSClusterRoleIdentity object. This in turn refers to the IAM role used to create all AWS cloud resources when creating the cluster. The role can be in another AWS account in order to create all resources in that account. Note: This name does not refer directly to an IAM role name/ARN.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#providerSpecific-flatcarAwsAccount">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.flatcarAwsAccount</h3>
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
        <a class="header-link" href="#providerSpecific-region">
          <i class="fa fa-link"></i>
        </a>.providerSpecific.region</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Region</span><br /><span class="property-type">string</span>&nbsp;
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
        <a class="header-link" href="#global-connectivity-bastion-instanceType">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion.instanceType</h3>
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
        <a class="header-link" href="#global-connectivity-bastion-subnetTags">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion.subnetTags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Subnet tags</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Tags to filter which AWS subnets will be used for the bastion hosts.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-bastion-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion.subnetTags[*]</h3>
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
        <a class="header-link" href="#global-connectivity-bastion-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.bastion.subnetTags[*].*</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*]</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]-credentials">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*].credentials</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]-credentials-auth">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*].credentials.auth</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]-credentials-identitytoken">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*].credentials.identitytoken</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]-credentials-password">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*].credentials.password</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]-credentials-username">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*].credentials.username</h3>
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
        <a class="header-link" href="#global-connectivity-containerRegistries-*[*]-endpoint">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.containerRegistries.*[*].endpoint</h3>
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
        <a class="header-link" href="#global-connectivity-dns-additionalVpc">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.dns.additionalVpc</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Additional VPCs</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">If DNS mode is 'private', the VPCs specified here will be assigned to the private hosted zone.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-dns-additionalVpc[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.dns.additionalVpc[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">VPC identifier</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-dns-mode">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.dns.mode</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Mode</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Whether the Route53 hosted zone of this cluster should be public or private.</div>
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
        <a class="header-link" href="#global-connectivity-network-podCidr">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.podCidr</h3>
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
        <a class="header-link" href="#global-connectivity-network-serviceCidr">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.network.serviceCidr</h3>
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
        <a class="header-link" href="#global-connectivity-sshSsoPublicKey">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.sshSsoPublicKey</h3>
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
        <a class="header-link" href="#controlPlane-apiMode">
          <i class="fa fa-link"></i>
        </a>.controlPlane.apiMode</h3>
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
      <div class="property-meta"><span class="property-title">EC2 instance type</span><br /><span class="property-type">string</span>&nbsp;
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
        <a class="header-link" href="#controlPlane-machineHealthCheck">
          <i class="fa fa-link"></i>
        </a>.controlPlane.machineHealthCheck</h3>
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
        <a class="header-link" href="#controlPlane-machineHealthCheck-enabled">
          <i class="fa fa-link"></i>
        </a>.controlPlane.machineHealthCheck.enabled</h3>
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
        <a class="header-link" href="#controlPlane-machineHealthCheck-maxUnhealthy">
          <i class="fa fa-link"></i>
        </a>.controlPlane.machineHealthCheck.maxUnhealthy</h3>
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
        <a class="header-link" href="#controlPlane-machineHealthCheck-nodeStartupTimeout">
          <i class="fa fa-link"></i>
        </a>.controlPlane.machineHealthCheck.nodeStartupTimeout</h3>
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
        <a class="header-link" href="#controlPlane-machineHealthCheck-unhealthyNotReadyTimeout">
          <i class="fa fa-link"></i>
        </a>.controlPlane.machineHealthCheck.unhealthyNotReadyTimeout</h3>
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
        <a class="header-link" href="#controlPlane-machineHealthCheck-unhealthyUnknownTimeout">
          <i class="fa fa-link"></i>
        </a>.controlPlane.machineHealthCheck.unhealthyUnknownTimeout</h3>
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
      <div class="property-description">Exact issuer URL that will be included in identity tokens.</div>
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
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#controlPlane-subnetTags">
          <i class="fa fa-link"></i>
        </a>.controlPlane.subnetTags</h3>
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
        <a class="header-link" href="#controlPlane-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.controlPlane.subnetTags[*]</h3>
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
        <a class="header-link" href="#controlPlane-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.controlPlane.subnetTags[*].*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tag value</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <h3 class="headline-with-link">
    <a class="header-link" href="#Default-node-pool">
      <i class="fa fa-link"></i>
    </a>Default node pool
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#defaultMachinePools-PATTERN">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-availabilityZones">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.availabilityZones</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-availabilityZones[*]">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.availabilityZones[*]</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeLabels</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeLabels[*]</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeTaints</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeTaints[*]</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeTaints[*].effect</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeTaints[*].key</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.customNodeTaints[*].value</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-instanceType">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.instanceType</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-maxSize">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.maxSize</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-minSize">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.minSize</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.rootVolumeSizeGB</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-subnetTags">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.subnetTags</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.subnetTags[*]</h3>
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
        <a class="header-link" href="#defaultMachinePools-PATTERN-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.defaultMachinePools.PATTERN.subnetTags[*].*</h3>
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
  <h3 class="headline-with-link">
    <a class="header-link" href="#Node-pools">
      <i class="fa fa-link"></i>
    </a>Node pools
  </h3>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#nodePools-PATTERN">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-availabilityZones">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.availabilityZones</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-availabilityZones[*]">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.availabilityZones[*]</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeLabels">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeLabels</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeLabels[*]">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeLabels[*]</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeTaints">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeTaints</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeTaints[*]">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeTaints[*]</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeTaints[*]-effect">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeTaints[*].effect</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeTaints[*]-key">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeTaints[*].key</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-customNodeTaints[*]-value">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.customNodeTaints[*].value</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-instanceType">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.instanceType</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-maxSize">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.maxSize</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-minSize">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.minSize</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-rootVolumeSizeGB">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.rootVolumeSizeGB</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-subnetTags">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.subnetTags</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-subnetTags[*]">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.subnetTags[*]</h3>
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
        <a class="header-link" href="#nodePools-PATTERN-subnetTags[*]-*">
          <i class="fa fa-link"></i>
        </a>.nodePools.PATTERN.subnetTags[*].*</h3>
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
