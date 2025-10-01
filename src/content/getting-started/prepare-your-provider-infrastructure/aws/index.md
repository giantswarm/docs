---
title: Prepare your AWS account
linkTitle: AWS
description: Prepare your AWS account to start building your cloud-native developer platform with Giant Swarm.
weight: 10
last_review_date: 2025-10-01
layout: single
menu:
  principal:
    parent: getting-started-prepare-provider-infrastructure
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How do I prepare my AWS account for the cloud-native developer platform?
  - What do I need to do to prepare my AWS account for the cloud-native developer platform?
aliases:
  - /getting-started/cloud-provider-accounts/cluster-api/aws/
  - /vintage/getting-started/cloud-provider-accounts/cluster-api/aws/
---

This guide provides the necessary steps to prepare your AWS accounts to run our platform, including Cluster API Provider for AWS (CAPA).

## Requirements

You can run the management and workload clusters in the same account or separate accounts in AWS environments. To help you take the decision, please read our [multi-account article]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/multi-account" >}}), where we explain the pros and cons of both approaches. Most requirements are related to configuring _Identity and Access Management (IAM)_ roles and service quotas.

![AWS Setup Diagram](aws_onboarding.png)

To perform the following steps, you must access the AWS console or have AWS CLI installed and pointed to the right account.

## Step 1: Service quotas {#quotas}

AWS establishes default quotas for all your cloud services as described in the [provider documentation](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). The following overview lists the quotas you must adjust to use the account to operate Giant Swarm clusters.

Adjusting a service quota requires issuing a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home), where you will find a specific entry form for each type of case. Each quota type requires a separate case. When creating these, log in to the proper account and select the correct region. If you plan to deploy clusters to multiple regions, ensure the quotas are raised for each region.

Below is a screenshot of a service quota entry form.

![AWS service quota screenshot](aws-service-limits.png)

Please request an increase in the following quotas (grouped by type):

- VPC
    - VPCs per region: **50**
    - NAT Gateway per Availability Zone per region: **50** (not needed if you are creating a [private cluster]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/private-clusters" >}}))
    - IPv4 CIDR blocks per VPC: **50**
    - Routes per route table: **200**
- Route 53 Resolver
    - Endpoints per AWS region: **100** (needed if you are creating a [private cluster]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/private-clusters" >}}))
- Elastic IP
    - New VPC Elastic IP Address Limit per region: **50** (not needed if you are creating a [private cluster]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/private-clusters" >}}))
- Elastic Load Balancers
    - Application and Classic Load Balancers per region: **100**
- Auto Scaling
    - Auto Scaling Groups per region: **250**
    - Launch Configurations per region: **500**
- S3
    - Buckets per Account: **1000**
- EC2 Spot Instances
    - Set the limit according to your needs for every primary instance type you tend to use spot instances with.
- EC2 Instances
    - m4.xlarge per region: **250**
    - m4.2xlarge per region: **250**
    - m5.2xlarge per region: **250**
    - other instance types to be used as workers: increase accordingly

**Note**: Please extend the list of EC2 instances to contain the frequently needed types.

You will be asked to describe your use case when requesting a service quota increase. Use this text for the following purposes:

```nohighlight
We intend to run multiple Kubernetes clusters in this account, potentially used
by various globally distributed teams. We will be creating and deleting new
clusters frequently.

Every cluster needs its own VPC for security/isolation reasons and its own
Elastic IP address for the NAT gateway.

Every cluster has at least 1 Auto Scaling Group, but can contain multiple ASGs if
multiple instance types are requested as cluster nodes. If we count 50
clusters with up to 5 EC2 instances each, as worker nodes, we need up to 250
ASGs. To update the ASGs in a rolling manner, we need to duplicate the ASGs
for a short time during the update, hence the 500 Launch Configurations.

The number of EC2 instances used as worker nodes is supposed to be scaled
dynamically based on traffic, hence the high numbers of EC2 instances requested.
```

## Step 2: IAM setup {#iam-setup}

There are various IAM resources required to run our platform. To ensure fast and streamlined operations to our customers, these IAM resources are managed by Giant Swarm in an automated system. [Below](#iam-roles) are details of each IAM role we use for informational purposes only.

To onboard a new AWS account to use with the Giant Swarm platform, follow the instructions in the [`giantswarm-aws-account-prerequisites` repository](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/blob/main/onboarding/README.md), where you'll also find the OpenTofu we use to manage the IAM roles.

After that, make sure to notify your Giant Swarm account engineer to provide the new AWS account ID so we can bootstrap the rest of the required IAM resources.

Contact your Giant Swarm account engineer to provide the new AWS account ID so we can bootstrap the rest of the required IAM resources, and to verify the setup and proceed with the provisioning of the management cluster. For sharing any secret with us please read [this article]({{< relref "/overview/security/sharing-secrets" >}}) first. In case you have already set up the management cluster and you have just configured a new AWS account, you can proceed with the [creation of the workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).

## Step 3: Configure the cluster role identity {#configure-cluster-role-identity}

The last step involves storing the AWS credentials in the platform to allow the CAPA controller to manage your account's infrastructure. In Cluster API there is a custom resource called `AWSClusterRoleIdentity` that stores the AWS role ARN and the role's name. Take into account that this resource is namespaced.

By default, the controller uses a `default` configuration, which points to the role in the management cluster account. If you want to create a new workload cluster in a new AWS account, you need to create a new `AWSClusterRoleIdentity` resource that references the role of that AWS account. Example:

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AWSClusterRoleIdentity
metadata:
  labels:
    cluster.x-k8s.io/watch-filter: capi
  name: <ACCOUNT_NAME>
spec:
  allowedNamespaces:
    list: null
    selector: {}
  roleARN: arn:aws:iam::${ACCOUNT_ID}:role/giantswarm-golem-capa-controller
  sourceIdentityRef:
    kind: AWSClusterControllerIdentity
    name: default
```

The `<ACCOUNT_NAME>` is a short unique name referencing the AWS account (`development`, `sandbox` or `staging2`). We advocate using the same name as the [organization]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/organizations" >}}) to help map the resources and the accounts. The `<ACCOUNT_ID>` is the AWS account ID where the role is created and where the workload cluster will be provisioned.

**Note**: The [official documentation](https://cluster-api-aws.sigs.k8s.io/topics/multitenancy) provides more information about configuring AWS credentials.

In the [next step]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}) you define which role the `AWSCluster` uses to provision the cluster adjusting the value `aws.awsClusterRoleIdentityName`.

**Note**: In case you are working with a Giant Swarm partner, you might not have access to the platform API. In that case, please provide the role ARNs values, CAPA controller and staff to your partner contact.

**Warning**: If your AWS account is a China account, make sure to follow [the ICP Filing process](https://www.amazonaws.cn/en/support/icp/).

## IAM roles used by Giant Swarm {#iam-roles}

This is a non-exclusive list of the primary IAM roles used by the Giant Swarm platform. _For informational purposes only_.

### CAPA controller role {#iam-capa-controller-role}

The CAPA controller in the management cluster uses the controller role to provision all infrastructure for managing workload clusters.

Each management cluster has its own IAM role in each of the AWS accounts it manages clusters on.

Name pattern: `giantswarm-${installation_name}-capa-controller`

### GiantSwarmAdmin role {#iam-giantswarmadmin-role}

This IAM role is used by Giant Swarm engineers to access the AWS account for support purposes, specifically when changes need to be made on-the-fly.

It is also used by our account automation to manage the IAM resources.

### GiantSwarmReadOnly role {#iam-giantswarmreadonly-role}

This IAM role is used by Giant Swarm engineers to access the AWS account for support purposes in a view-only capacity.

It is also used by our account automation to plan and validate changes during pull-requests on our infrastructure code.
