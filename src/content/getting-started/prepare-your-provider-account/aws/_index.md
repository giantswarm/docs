---
title: Prepare your AWS account
description: Prepare your AWS account to start building your cloud-native developer platform with Giant Swarm.
weight: 10
last_review_date: 2024-05-28
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I prepare my AWS account for the cloud-native developer platform?
  - What do I need to do to prepare my AWS account for the cloud-native developer platform?
---

In order to run the Giant Swarm platform in your AWS accounts, several prerequisites must be satisfied to support Cluster API Provider for AWS (CAPA).

## Requirements

In AWS environments, you can run the management and workload clusters in the same account or separate accounts. Most requirements are related to configuring _Identity and Access Management (IAM)_ roles and service quotas.

![AWS Setup Diagram](aws_onboarding.png)

### Service quotas {#quotas}

AWS establishes default quotas for all your cloud services as described in the [provider documentation](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). The following overview lists the quotas you must adjust to use the account to operate Giant Swarm clusters.

Adjusting a service quota requires issuing a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home), where you will find a specific entry form for each type of case. Each quota type requires a separate case. Log in to the proper account and select the correct region when creating these.

Below is a screenshot of a service quota entry form.

![Screenshot](aws-service-limits.png)

Next, there is the list of quotas to be modified, grouped by type:

```nohighlight
- management cluster account:
    - VPC
        - Routes per route table: **200** ??
- workload cluster account:
    - VPC
        - VPCs per region: **50**
        - NAT Gateway per Availability Zone per region: **50**
        - IPv4 CIDR blocks per VPC: **50**
    - Elastic IP
        - New VPC Elastic IP Address Limit per region: **50**
    - Elastic Load Balancers
        - Application and Classic Load Balancers per region: **100**
    - Auto Scaling
        - Auto Scaling Groups per region: **250**
        - Launch Configurations per region: **500**
    - S3
        - Buckets per Account: **1000**
    - EC2 Spot Instances
        - For every primary instance type you tend to use spot instances with, set the limit according to your needs.
    - EC2 Instances
        - m4.xlarge per region: **250**
        - m4.2xlarge per region: **250**
        - m5.2xlarge per region: **250**
        - other instance types to be used as workers: increase accordingly
```

__Note__: Please extend the list of EC2 instances to contain the frequently needed types.

When requesting a service quota increase, you will be asked for a description of your use case. Use this text for the following purposes:

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

### Permissions

There are two types of IAM roles that need to be created in the AWS account. First, the controller role which is used by the CAPA controller in the management cluster to provision all infrastructure to manage workload clusters. Second, the staff role is used by Giant Swarm engineers to access the AWS account for support purposes.

Here are the mandatory steps to create the required IAM resources but we advocate to follow one of the [automated options](https://github.com/giantswarm/giantswarm-aws-account-prerequisites). There you have terraform or cloudformation templates to create the necessary IAM roles and policies.

#### Controller permissions {#iam-capa-controller-role}

##### 1. Basic role setup {#iam-capa-controller-role-basic}

Open the [IAM section](https://console.aws.amazon.com/iam/home) of the AWS console and go to the [Roles](https://console.aws.amazon.com/iam/home#/roles) subsection.

Now, hit the **Create role** button. In the following screen, when asked to _Select type of trusted entity_ chose _AWS account_.

![AWS IAM console: Create role](aws-roles-create-role.png)

The **Account ID** you enter is the ID of the AWS account where management cluster is running. Could it be the current account in case you running all your infrastructure in a single account or different one if you are using separate accounts for management and workload clusters.

It is important that the **Require external ID** and **Require MFA** options remain unchecked!

Then, please go ahead and proceed to the next step.

##### 2. Permissions setup {#iam-capa-controller-role-permissions}

In the **Attach permissions policies** section, hit the **Create policy** button.

Copy the JSON code with all instances of `${account_id}` and `${arn_prefix}` replaced from [iam-policy.json] into the JSON editor field and then hit the **Review policy** button. `${arn_prefix}` is usually `arn:aws`.

In the next step you need to assign a name to the policy. Please use the name changing the INSTALLATION_NAME placeholder to the name of your installation.

```nohighlight
giantswarm-${INSTALLATION_NAME}-capa-controller-policy
```

__Note__: The role name contains the installation name to make it easier to identify the role and avoid conflicts with other installations.

##### 3. Attach policy to role {#iam-capa-controller-role-policy}

Enter `capa-controller-policy` into the search field to select the policy you created before. Check the box in the row containing that policy.

![AWS IAM console: Attach policy](aws-roles-attach-policy.png)

Then, please go ahead and proceed to the next step.


<LIST ALL POLICIES SHOULD BE CREATED resolver, network, crossplane,...>


##### 4. Name the role {#iam-capa-controller-role-name}

The last step of role creation requires you to set a name for the role. Same as with the policy, please use the name changing the INSTALLATION_NAME placeholder to the name of your installation.

```nohighlight
giantswarm-${INSTALLATION_NAME}-capa-controller
```

![AWS IAM console: Review](aws-roles-review.png)

### Staff permissions {#iam-staff-role}

Finally, we create an IAM role for Giant Swarm support staff to assume in order to
access both AWS accounts. This role must have Giant Swarm's account as a trusted
entity, and we recommend that it enforces multi-factor authentication.

Giant Swarm staff require access to **all** accounts, so **the following steps must
be duplicated in both the management cluster and workload cluster accounts**.

#### 1. Basic role setup {#iam-staff-role-basic}

- Go to the [Roles](https://console.aws.amazon.com/iam/home#/roles) subsection of the AWS console and select **Create role**. When asked to **Select type of trusted entity** choose **Another AWS account**.

- In **Account ID** enter the value `084190472784`.

- **Do not** enable **Require external ID**.

- We strongly recommended to check the option **Require MFA** (multi factor authentication). This adds an extra authentication step for users to assume the role, which increases security.

#### 2. Permission setup {#iam-staff-role-permissions}

Select **Create policy** to create another policy. Use the [admin JSON policy](https://raw.githubusercontent.com/giantswarm/giantswarm-aws-account-prerequisites/master/admin-role/iam-policy.json) file as the policy content. This time, call the policy

```nohighlight
GiantSwarmAdmin
```

#### 3. Attach policy to role {#iam-staff-role-policy}

Attach the new `GiantSwarmAdmin` policy to the role you are creating.

#### 4. Name the role {#iam-staff-role-name}

Name this role:

```nohighlight
GiantSwarmAdmin
```

## Configure the organization {#configure-org}
<!-- IS THIS STILL VALID??-->
In the previous sections, we explained how to create two IAM roles in the
AWS account that's going to run the Giant Swarm workload clusters.

Giant Swarm workload clusters are owned by _organizations_, which allows you to control
access to clusters. Only members of the owner organization have access to
the management functions of a cluster.

In order to run a workload cluster in your AWS account, the organization owning
your cluster has to know about the roles you just created.

If you have direct access to the Giant Swarm REST API, please set the credentials of
your organization with our CLI [gsctl]({{< relref "/vintage/use-the-api/gsctl" >}}). Look for the
[`update organization set-credentials`]({{< relref "/vintage/use-the-api/gsctl/update-org-set-credentials" >}})/#aws)
command.

In case you are working with a Giant Swarm partner, you might not have
access to the Giant Swarm REST API. In that case, please provide the role ARNs for
the `GiantSwarmAWSOperator` role and the `GiantSwarmAdmin` role to your partner
contact.

After the organization's credentials are set, you can create clusters owned by that
organization. These clusters' resources will be created in your AWS account.