---
title: Prepare your AWS account
description: Prepare your AWS account to start building your cloud-native developer platform with Giant Swarm.
weight: 10
last_review_date: 2024-05-23
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I prepare my AWS account for the cloud-native developer platform?
  - What do I need to do to prepare my AWS account for the cloud-native developer platform?
---

In order to run the Giant Swarm platform in your AWS account(s), several prerequisites must be satisfied to support Cluster API Provider AWS (CAPA).

## Requirements

In AWS environments you can run the management cluster and workload clusters in the same account or in separate accounts. Most of the requirements are related to configure `Identity and Access Management (IAM)` roles and policies.

![AWS Setup Diagram](aws_onboarding.png)

### Service limits in AWS accounts {#limits}


Several limits apply to an AWS account initially, which are described in the
[AWS Service Limits documentation](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).
The following overview lists the limits that must be adjusted to use
the account to operate Giant Swarm workload clusters.

Adjusting a service limit requires a support case in the
[AWS Support Center](https://console.aws.amazon.com/support/home),
where a specific entry form is provided for this type of case. Each limit type
requires a separate case. When creating these, make sure to be logged in to the
You want to adjust the limits for the AWS account, and always select the correct
region.

The screenshot below shows the entry form.

![Screenshot](aws-service-limits.png)

These are the limit increases to be requested, grouped by limit type:

- management cluster account:
    - VPC
        - Routes per route table: **200**
- Workload cluster account:
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
    - EC2 Instances
        - m4.xlarge per region: **250**
        - m4.2xlarge per region: **250**
        - m5.2xlarge per region: **250**
        - other instance types to be used as workers: increase accordingly
    - EC2 Spot Instances
        - For every primary instance type you tend to use spot instances with, set the limit according to your needs.
    - S3
        - Buckets per Account: **1000**

(Please extend the list of EC2 instances to contain the frequently needed types.)

When requesting a service limit increase, you will be asked for a description of your use case. You can use this text for the following purposes:

> We intend to run multiple Kubernetes clusters in this account, potentially used
by various globally distributed teams. We will be creating and deleting new
clusters frequently.

> Each cluster needs its own VPC for security/isolation reasons and its own
Elastic IP address for the NAT gateway.

> Each cluster has at least 1 Auto Scaling Group, but can contain multiple ASGs if
multiple instance types are requested as cluster nodes. If we count 50
clusters with up to 5 EC2 instances each, as worker nodes, we need up to 250
ASGs. To update the ASGs in a rolling manner, we need to duplicate the ASGs
for a short time during the update, hence the 500 Launch Configurations.

> The number of EC2 instances used as worker nodes is supposed to be scaled
dynamically based on traffic, hence the high numbers of EC2 instances requested.


#### Permissions

#### Create an IAM role for aws-operator {#iam-aws-operator-role}

A role which can be assumed by `aws-operator` user needs to be created in the
account.

##### 1. Basic role setup {#iam-aws-operator-role-basic}

Open the [IAM section](https://console.aws.amazon.com/iam/home) of the AWS
console and go to the [Roles](https://console.aws.amazon.com/iam/home#/roles)
subsection.

Now, hit the **Create role** button. In the following screen, when asked to
_Select type of trusted entity_ chose _Another AWS account_.

![AWS IAM console: Create role](aws-roles-create-role.png)

The **Account ID** you enter is the ID of the AWS account where `aws-operator`
use is created.

It is important that the **Require external ID** and **Require MFA** options
remain unchecked!

Then, please go ahead and proceed to the next step.

##### 2. Permissions setup {#iam-aws-operator-role-permissions}

In the **Attach permissions policies** section, hit the **Create policy** button.

Copy the JSON code with all instances of `${account_id}` and `${arn_prefix}`
replaced from [iam-policy.json] into the JSON editor field and then hit the
**Review policy** button. `${arn_prefix}` is usually `arn:aws`.

In the next step you need to assign a name to the policy. Please use the name.

```nohighlight
GiantSwarmAWSOperator
```

##### 3. Attach policy to role {#iam-aws-operator-role-policy}

Enter `GiantSwarmAWSOperator` into the search field to select the policy
you created before. Check the box in the row containing that policy.

![AWS IAM console: Attach policy](aws-roles-attach-policy.png)

Then, please go ahead and proceed to the next step.

##### 4. Name the role {#iam-aws-operator-role-name}

The last step of role creation requires you to set a name for the role. Please
set the name to `GiantSwarmAWSOperator`.

![AWS IAM console: Review](aws-roles-review.png)

You may also set a description for team members to understand better why this role exists. It could also be helpful to paste a link to this
guide into the field for reference.
