---
title: cluster-eks chart reference
linkTitle: cluster-eks
description:  A helm chart for creating Cluster API EKS clusters with the AWS infrastructure provider (CAPA).; Check here the different properties of the chart.
weight: 100
menu:
  main:
    identifier: cluster-eks
    parent: uiapi-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-eks?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-eks
source_repository_ref: v0.12.0
---

The `cluster-eks` chart templates all the AWS infrastructure resources that are necessary to create a Cluster API EKS cluster.

<!-- INTRO_END -->
# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

Note that configuration options can change between releases. Use the GitHub function for selecting a branch/tag to view the documentation matching your cluster-eks version.

<!-- Update the content below by executing (from the repo root directory)

schemadocs generate helm/cluster-eks/values.schema.json -o helm/cluster-eks/README.md

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
        <a class="header-link" href="#global-providerSpecific-awsAccountId">
          <i class="fa fa-link"></i>
        </a>.global.providerSpecific.awsAccountId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">AWS account ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">AWS Account ID of the AWSClusterRoleIdentity IAM role, recommendation is to leave this value empty as it will be automatically calculated. This value is needed for tests.</div>
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
      <div class="property-description">Name of an AWSClusterRoleIdentity object. This in turn refers to the IAM role used to create all AWS cloud resources when creating the cluster. The role can be in another AWS account in order to create all resources in that account. Note: This name does not refer directly to an IAM role name/ARN.</div>
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
      <div class="property-description">IPv4 address range for pods, in CIDR notation. Must be within the 100.64.0.0/10 or 198.19.0.0/16 range. The CIDR block size must be betwen /16 and /28.</div>
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
        <a class="header-link" href="#global-connectivity-podSubnets">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Pod Subnets</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Pod Subnets are created and tagged based on this definition.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-connectivity-podSubnets[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*]</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-cidrBlocks">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].cidrBlocks</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-cidrBlocks[*]">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].cidrBlocks[*]</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-cidrBlocks[*]-availabilityZone">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].cidrBlocks[*].availabilityZone</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-cidrBlocks[*]-cidr">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].cidrBlocks[*].cidr</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-cidrBlocks[*]-tags">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].cidrBlocks[*].tags</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-cidrBlocks[*]-tags-*">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].cidrBlocks[*].tags.*</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-tags">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].tags</h3>
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
        <a class="header-link" href="#global-connectivity-podSubnets[*]-tags-*">
          <i class="fa fa-link"></i>
        </a>.global.connectivity.podSubnets[*].tags.*</h3>
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
  <h3 class="headline-with-link">
    <a class="header-link" href="#Control-plane">
      <i class="fa fa-link"></i>
    </a>Control plane
  </h3>
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
        <a class="header-link" href="#global-controlPlane-logging">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.logging</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Logging</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-logging-apiServer">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.logging.apiServer</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Api Server</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Enable or disable Api server logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-logging-audit">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.logging.audit</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Audit</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Enable or disable audit logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-logging-authenticator">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.logging.authenticator</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Authenticator</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Enable or disable IAM Authenticator logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-logging-controllerManager">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.logging.controllerManager</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Controller Manager</span><br /><span class="property-type">boolean</span>&nbsp;
      </div>
      <div class="property-description">Enable or disable Controller Manager logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">OIDC identity provider config</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">OIDC identity provider configuration for the Kubernetes API server.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-clientId">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.clientId</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Client ID</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Client ID of the OIDC identity provider.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-groupsClaim">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.groupsClaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Groups claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Claim to use for mapping groups.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-groupsPrefix">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.groupsPrefix</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Groups prefix</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Prefix to use for mapping groups.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-identityProviderConfigName">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.identityProviderConfigName</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Identity provider config name</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Name of the OIDC identity provider config.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-issuerUrl">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.issuerUrl</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Issuer URL</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">URL of the OIDC identity provider.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-requiredClaims">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.requiredClaims</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Required claims</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Required claims for the OIDC identity provider.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-requiredClaims-*">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.requiredClaims.*</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-tags">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.tags</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Tags</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">AWS resource tags to assign to the IAM OIDC provider.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-tags-*">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.tags.*</h3>
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
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-usernameClaim">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.usernameClaim</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username claim</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Claim to use for mapping usernames.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-oidcIdentityProviderConfig-usernamePrefix">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.oidcIdentityProviderConfig.usernamePrefix</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Username prefix</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Prefix to use for mapping usernames.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-roleMapping">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.roleMapping</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Role mappings</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description"></div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-roleMapping[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.roleMapping[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Role mapping</span><br /><span class="property-type">object</span>&nbsp;
      </div>
      <div class="property-description">Maps AWS IAM role to Kubernetes role.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-roleMapping[*]-groups">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.roleMapping[*].groups</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Groups</span><br /><span class="property-type">array</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes groups.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-roleMapping[*]-groups[*]">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.roleMapping[*].groups[*]</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Group</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes group, for example `system:masters`.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-roleMapping[*]-rolearn">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.roleMapping[*].rolearn</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">AWS Role ARN</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Full ARN of the AWS IAM role.</div>
    </div>
  </div>
  <div class="property depth-0">
    <div class="property-header">
      <h3 class="property-path headline-with-link">
        <a class="header-link" href="#global-controlPlane-roleMapping[*]-username">
          <i class="fa fa-link"></i>
        </a>.global.controlPlane.roleMapping[*].username</h3>
    </div>
    <div class="property-body">
      <div class="property-meta"><span class="property-title">Kubernetes username</span><br /><span class="property-type">string</span>&nbsp;
      </div>
      <div class="property-description">Kubernetes username, for example `cluster-admin`.</div>
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
      <div class="property-meta"><span class="property-title">Kubectl image</span><br /><span class="property-type">object</span>&nbsp;
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

- [Source repository](https://github.com/giantswarm/cluster-eks)
