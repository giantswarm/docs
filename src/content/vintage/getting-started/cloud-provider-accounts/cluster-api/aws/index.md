---
linkTitle: AWS
title: Prepare an AWS account to run Cluster API Giant Swarm clusters
description: This guide will walk you through all necessary steps to set up an Amazon AWS account with appropriate IAM roles for operating Cluster API Giant Swarm clusters.
weight: 10
menu:
  main:
    identifier: gettingstarted-infraprovider-clusterapi-aws
    parent: gettingstarted-infraprovider-clusterapi
user_questions:
  - What are the recommended service limit/quotas for AWS accounts?
  - How prepare AWS account for the Cluster API clusters?
aliases:
  - /getting-started/cloud-provider-accounts/cluster-api/aws
  - /guides/prepare-aws-account-for-tenant-clusters/
  - /guides/prepare-aws-account/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2024-02-16
---

The Cluster API workload clusters (the clusters running your Kubernetes workloads) in a Giant Swarm installation can run in an AWS account separate from the management cluster. This gives great flexibility depending on requirements and usage scenarios. For example, it allows the management cluster to be running in an AWS account dedicated to it, whilst workload clusters operate in several different AWS accounts, depending
on the customer's needs.

## Overview

Aside from the following prerequisites, please fill in the _Giant Swarm Pre-installation checklist for AWS (CAPA) installations_, The document will be shared with you by your account engineer.

In order to run Giant Swarm Cluster API clusters, all AWS account(s) need to fulfil these requirements (there is [repository](https://github.com/giantswarm/giantswarm-aws-account-prerequisites) that can help with creating the necessary resources in AWS)

- Create [GiantSwarmAdmin](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/tree/master/admin-role) IAM role, which is used by Giant Swarm employees to support and debug Cluster API workload clusters via AWS console.
- Create [capa-controller-role](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/tree/master/capa-controller-role) IAM role, which is used by the controllers and operators to create necessary AWS resources for the Cluster API workload clusters.
- Service limits are set according to requirements.

We have created a Terraform module to automate the IAM role creation. You can view the code [here](https://github.com/giantswarm/giantswarm-aws-account-prerequisites). You can also use the steps as described in this guide.

## Service limits in AWS accounts {#limits}

A number of limits apply to an AWS account initially, which are described in the [AWS Service Limits documentation](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). The following overview lists the limits that have to be adjusted in order to use the account to operate Giant Swarm Cluster API workload clusters.

Adjusting a service limit requires a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home), where a specific entry form is provided for this type of case. Each limit type requires a separate case. When creating these, make sure to be logged in to the AWS account you want to adjust the limits for, and always select the correct region.

The screenshot below shows the entry form.

![Screenshot](aws-service-limits.png)

These are the limit increases to be requested, grouped by limit type:

- All AWS accounts
    - VPC
        - Routes per route table: **200**
        - VPCs per region: **50**
        - IPv4 CIDR blocks per VPC: **50**
    - Elastic Load Balancers
        - Application and Classic Load Balancers per region: **100**
    - Auto Scaling
        - Auto Scaling Groups per region: **250**
        - Launch Configurations per region: **500**
    - EC2 Instances
        - m5.xlarge per region: **250**
        - m5.2xlarge per region: **250**
        - other instance types to be used as workers: increase accordingly
    - EC2 Spot Instances
        - For every primary instance type you tend to use spot instances with, set the limit according to your needs.
- AWS account intended to run public clusters (outgoing traffic goes to public internet)
    - VPC
        - NAT Gateway per Availability Zone per region: **50**
    - Amazon Elastic Compute Cloud (Amazon EC2)
        - EC2-VPC Elastic IPs: **50**

- AWS account intended to run private clusters (outgoing traffic goes to public internet only thru proxy)
    - Route 53 Resolver
        - Endpoints per AWS Region: **100**

(Please extend the list of EC2 instances to also contain the types you need frequently.)

## Configure the `AWSClusterRoleIdentity`

When you want to create a new Cluster API workload cluster in a new AWS account you need to create a CR `AWSClusterRoleIdentity` which will reference the role in the new AWS Account.

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AWSClusterRoleIdentity
metadata:
  labels:
    cluster.x-k8s.io/watch-filter: capi
  name: ${ROLE_NAME}
spec:
  allowedNamespaces:
    list: null
    selector: {}
  roleARN: ${ROLE_ARN}
  sourceIdentityRef:
    kind: AWSClusterControllerIdentity
    name: default
```

Where:

- `${ROLE_NAME}` is a short unique name referencing AWS account (ie: `development`, `sandbox` or `staging2`)
- `${ROLE_ARN}` is full ARN of the role created in previous step with `giantswarm-aws-account-prerequisites` repository.

This CR needs to be created only once for each AWS Account. It can be then referenced in the `cluster-aws` repo in the value [`aws.awsClusterRoleIdentityName`](https://github.com/giantswarm/cluster-aws/blob/master/helm/cluster-aws/values.yaml#L14).

## Further reading

- [Basics and Concepts: Multi Account Support]({{< relref "/vintage/advanced/infrastructure-management/multi-account" >}})
- [API: Set credentials](/api/#operation/addCredentials)
- [Giant Swarm Architecture]({{< relref "/vintage/platform-overview/cluster-management/vintage/aws" >}})
- [Giant Swarm REST API documentation](/api/)
- [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [AWS Support Center](https://console.aws.amazon.com/support/home)
