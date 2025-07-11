---
title: Prepare your AWS account
linkTitle: AWS
description: Prepare your AWS account to start building your cloud-native developer platform with Giant Swarm.
weight: 10
last_review_date: 2025-07-02
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

## Step 2: Permissions

Two types of IAM roles need to be created in the AWS account.

First, the CAPA controller in the management cluster uses the controller role to provision all infrastructure for managing workload clusters.

Second, the staff role is used by Giant Swarm engineers to access the AWS account for support purposes.

Here are the mandatory steps to create the required IAM resources, but we advocate following one of the [automated options](https://github.com/giantswarm/giantswarm-aws-account-prerequisites). There, you have Terraform or CloudFormation templates to create the necessary IAM roles and policies. Otherwise, follow the manual steps below.

### Controller permissions {#iam-capa-controller-role}

#### 1. Create all policies for the Cluster API controller {#iam-capa-controller-policies}

Open the [IAM section](https://console.aws.amazon.com/iam/home) of the AWS console and go to the [Policies](https://console.aws.amazon.com/iam/home#/policies) subsection.

Our platform needs different permissions to manage various resources on the AWS side. Here is the list of policies that need to be created. Click _Create policy_ and copy the policy content into the JSON editor field. Hit the `Next` button and add the policy name matching the policy link name. Repeat this process for each policy:

- [giantswarm-${INSTALLATION_NAME}-capa-controller-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/capa-controller-policy.json)
- [giantswarm-${INSTALLATION_NAME}-capa-controller-vpc-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/capa-controller-vpc-policy.json)
- [giantswarm-${INSTALLATION_NAME}-crossplane-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/crossplane-policy.json)
- [giantswarm-${INSTALLATION_NAME}-dns-controller-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/dns-controller-policy.json)
- [giantswarm-${INSTALLATION_NAME}-eks-controller-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/eks-controller-policy.json)
- [giantswarm-${INSTALLATION_NAME}-iam-controller-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/iam-controller-policy.json)
- [giantswarm-${INSTALLATION_NAME}-irsa-operator-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/irsa-operator-policy.json)
- [giantswarm-${INSTALLATION_NAME}-mc-bootstrap-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/mc-bootstrap-policy.json)
- [giantswarm-${INSTALLATION_NAME}-network-topology-operator-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/network-topology-operator-policy.json)
- [giantswarm-${INSTALLATION_NAME}-resolver-rules-operator-policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/refs/heads/main/capa-controller-role/policies/resolver-rules-operator-policy.json)

**Warning**: When filling out the policy name, remember to replace the `INSTALLATION_NAME` placeholder with the name of your installation.

![AWS IAM console: Create policy](aws-roles-create-policy.png)

**Note**: All policy names include the installation name to facilitate easier identification and prevent conflicts with other installations running within the same account.

#### 2. Create the role metadata {#iam-capa-controller-role-basic}

Now move to the IAM [Roles](https://console.aws.amazon.com/iam/home#/roles) subsection, and hit the _Create role_ button. In the following screen, when asked to _Select the type of trusted entity_, choose _AWS account_.

![AWS IAM console: Create role](aws-roles-create-role.png)

The _Account ID_ you need to enter is the AWS account where the management cluster runs. In case you run all your clusters in a single account, there is no need to change it, but if your management cluster runs in a separate account, you need to use that one for `Another AWS account` option.

It's crucial that the _Require external ID_ and _Require MFA_ options remain unchecked so that CAPA can run without requiring human intervention.

#### 3. Attach all policies to role {#iam-capa-controller-role-policy}

Now, you must go through all the policies created before and attach them to the role. You can just search for the installation name, select the policies and hit the _Next_ button.

![AWS IAM console: Attach policies](aws-roles-attach-policy.png)

#### 4. Name the role {#iam-capa-controller-role-name}

The last step of role creation requires you to set a name for the role. As with the policies, please use the name changing the `INSTALLATION_NAME` placeholder to the name of your management cluster.

```sh
giantswarm-${INSTALLATION_NAME}-capa-controller
```

![AWS IAM console: Review](aws-roles-review.png)

### Staff permissions {#iam-staff-role}

Finally, we create an IAM role for Giant Swarm support staff to assume access to both the management cluster's and workload clusters' AWS accounts. This role must have Giant Swarm's account as a trusted entity, and we recommend that it enforce multi-factor authentication.

#### 1. Create the admin policy {#iam-staff-policy}

Go to the [Policies](https://console.aws.amazon.com/iam/home#/policies) subsection and select _Create policy_ to set the admin permissions. Use the [admin JSON policy](https://github.com/giantswarm/giantswarm-aws-account-prerequisites/raw/master/admin-role/iam-policy.json) file as the policy content. This time, call the policy.

```text
GiantSwarmAdmin
```

#### 2. Create the admin role {#iam-staff-role}

Enter again in the [Roles](https://console.aws.amazon.com/iam/home#/roles) subsection of the AWS console and select _Create role_ When asked to _Select type of trusted entity_ choose _AWS account_.

- In _Account ID_ enter the value `084190472784`.
- Don't enable _Require external ID_.
- It's strongly recommended to check the option _Require MFA_ (multi factor authentication). This adds an extra authentication step for users to assume the role, which increases security.

#### 3. Attach policy to role {#iam-staff-role-policy}

Attach the newly created `GiantSwarmAdmin` policy to the role you are creating.

#### 4. Name the role {#iam-staff-role-name}

Name this role:

```text
GiantSwarmAdmin
```

Giant Swarm staff require access to all AWS resources, so please repeat the above steps for every account where you will run clusters.

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

**Warning**: If you AWS account is a China account, make sure to follow [the ICP Filing process](https://www.amazonaws.cn/en/support/icp/).

## Next steps

Contact your Giant Swarm account engineer to verify the setup and proceed with the provisioning of the management cluster. For sharing any secret with us please read [this article]({{< relref "/overview/security/sharing-secrets" >}}) first. In case you have already set up the management cluster and you have just configured a new AWS account, you can proceed with the [creation of the workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).
