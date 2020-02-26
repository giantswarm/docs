+++
title = "Prepare an AWS account to run Giant Swarm clusters"
description = "This guide will walk you through all necessary steps to set up an Amazon AWS account with appropriate IAM roles for operating Giant Swarm clusters."
date = "2019-10-25"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Prepare an AWS account to run Giant Swarm clusters

As detailed in the [Architecture](/basics/aws-architecture/) docs,
the tenant clusters (the clusters running your Kubernetes workloads) in a Giant
Swarm installation are running in an AWS account separate from the control plane.
This gives great flexibility depending on the requirements and the usage
scenario. For example, it allows the control plane to be running in an AWS account
dedicated to it, whilst tenant clusters operate in separate AWS accounts, depending
on a customer's department using them.

## Overview

In order to run Giant Swarm clusters, the AWS account(s) need to fulfill
these requirements:

- Control plane account:
  - IAM _user_ to be used by our `aws-operator` software.
  - IAM role to be assumed by Giant Swarm staff.
- Tenant cluster account:
  - Service limits set according to requirements.
  - IAM _role_ to be assumed by our `aws-operator` software.
  - IAM role to be assumed by Giant Swarm staff.

Each Giant Swarm tenant cluster belongs to an organization within Giant Swarm.
This organization will later be configured with information about the two
tenant cluster IAM roles mentioned above.

We have created a Terraform module to automate the IAM role creation. You can check the code [here](https://github.com/giantswarm/giantswarm-aws-account-prerequisites). Otherwise you can still use the steps as described in this guide.

## Increase service limits in an AWS tenant cluster account {#limits}

A number of limits apply to an AWS account initially, which are described in the
[AWS Service Limits documentation](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).
The following overview lists the limits that have to be adjusted in order to use
the account to operate Giant Swarm tenant clusters.

Adjusting a service limit requires a support case in the
[AWS Support Center](https://console.aws.amazon.com/support/home),
where a specific entry form is provided for this type of case. Each limit type
requires a separate case. When creating these, make sure to be logged in to the
AWS account you want to adjust the limits for, and always select the correct
region.

The screenshot below shows the entry form.

![Screenshot](/img/aws-service-limits.png)

These are the limit increases to be requested, grouped by limit type:

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

(Please extend the list of EC2 instance to also contain the types you need frequently.)

When requesting a service limit increase, you will be asked for a description of your use case. You can use this text for the purpose:

> We intend to run multiple Kubernetes clusters in this account, potentially used
by various globally distributed teams. We will be creating and deleting new
clusters frequently.

> Each cluster needs its own VPC for security/isolation reasons and its own
Elastic IP address for the NAT gateway.

> Each cluster has at least 1 Auto Scaling Group, but can contain multiple ASGs if
multiple instance types are requested as cluster nodes. If we count with 50
clusters with up to 5 EC2 instances as worker nodes each, we need up to 250
ASGs. For updating the ASGs in a rolling manner we need to duplicate the ASGs
for a short time during update, hence the 500 Launch Configurations.

> The number of EC2 instances used as worker nodes is supposed to be scaled
dynamically based on traffic, hence the high numbers of EC2 instances requested.

## IAM setup for control plane accounts

The following steps must all take place in the control plane AWS account.

### Create an IAM user for aws-operator {#operator-iam-user}

Giant Swarm's service creating and maintaining your tenant clusters is
called [aws-operator](https://github.com/giantswarm/aws-operator). It is
running in the control plane. In order to handle resources in your AWS Tenant
Cluster account, it needs a prepared IAM user in your AWS control plane
account. Here we explain all the required steps to set up this user.

#### 1. Basic user setup

First, log in to the AWS console for your AWS account. Then open the
[IAM section](https://console.aws.amazon.com/iam/home) of the AWS console and
go to the [Users](https://console.aws.amazon.com/iam/home#/users) subsection.

Now hit the **Add user** button. Enter the user name as `aws-operator` and ensure
only _Programmatic access_ is enabled.

![AWS IAM console: Create user](/img/aws-user-create-user.png)

#### 2. Permissions setup

In the **Attach existing policies directly** section, hit the **Create policy** button.

Paste the JSON code from [tenant_cluster.json](https://raw.githubusercontent.com/giantswarm/aws-operator/master/policies/tenant_cluster.json) into the JSON editor field and then hit the **Review policy** button.

In the next step you have to assign a name to the policy. Please use the name:

```nohighlight
GiantSwarmAWSOperatorPolicy
```

Entering a description will also help distinguish the policy to other people.
We suggest:

> Policy required for the Giant Swarm AWS Operator.

#### 3. Attach policy to user

Once you created the policy, let's turn back to the point in the user creation
called *Attach existing policies directly*. Here you can now hit the *Refresh*
button to load all existing policies, then enter `GiantSwarmAWSOperatorPolicy`
into the search field to select the policy you just created. Check the box in
the row containing that policy.

![AWS IAM console: Attach policy to user](/img/aws-user-attach-policy.png)

Then proceed to the *Review* step.

#### 4. Review and create user

Please now review the user. Provided everything is correct, hit the *Create*
button. On the following page, you will be presented with an *Access key ID* and
a *Secret access key*. Click the 'show' link to display the access key secret,
and then copy both the key ID and key secret; these will need to be provided to
us later.

![AWS IAM console: User secrets](/img/aws-user-secrets.png)

### Create an IAM role for Giant Swarm staff {#gs-cp-iam-role}

Next, we create an IAM role for Giant Swarm support staff to assume in order to
access the control plane AWS account. This role must have Giant Swarm's account
as a trusted entity, and we recommend that it enforces multi-factor authentication.

#### 1. Basic role setup

- Go to the [Roles](https://console.aws.amazon.com/iam/home#/roles)
subsection of the AWS console and select **Create role**. When asked to
**Select type of trusted entity** choose **Another AWS account**.

- In **Account ID** enter the value `084190472784`.

- **Do not** enable **Require external ID**.

- We strongly recommended to check the option **Require MFA** (multi factor
  authentication). This adds an extra authentication step for users to assume the
  role, which increases security.

#### 2. Permission setup

Select **Create policy** to create another policy. Use the same JSON policy code
as you used for the `aws-operator` user. This time, call the policy

```nohighlight
GiantSwarmAdminPolicy
```

#### 3. Attach policy to role

Attach the new `GiantSwarmAdminPolicy` policy to the role you are creating.

#### 4. Name the role

Name this role:

```nohighlight
GiantSwarmAdmin
```

#### 5. Get the role's ARN

From the confirmation screen, copy the exact ARN. It should be in the form of:

```nohighlight
arn:aws:iam::<YOUR_ACCOUNT_ID>:role/GiantSwarmAdmin
```

This will need to be provided to us later.

## IAM setup for tenant cluster accounts

The following steps must all take place in the tenant cluster AWS account.

## Create an IAM role for aws-operator {#operator-iam-role}

Giant Swarm's service creating and maintaining your tenant clusters is
called [aws-operator](https://github.com/giantswarm/aws-operator). It is
running in the control plane. In order to handle resources in your AWS account,
it needs to assume a prepared IAM role in your AWS account. Here we explain all
the required steps to set up this role.

### 1. Determine the control plane's AWS account ID

First you need to know in which AWS account the Giant Swarm control plane is
(or will be) running. As Giant Swarm's customer you might have already decided
this yourself. Normally you yourself own this account.

Please have the ID of the account selected to run the control plane at hand, as
you will need it in step 2.

### 2. Basic role setup

First, log in to the AWS console for your AWS account. Then open the
[IAM section](https://console.aws.amazon.com/iam/home) of the AWS console and
go to the [Roles](https://console.aws.amazon.com/iam/home#/roles) subsection.

Now hit the **Create role** button. In the following screen, when asked to
_Select type of trusted entity_ chose _Another AWS account_.

![AWS IAM console: Create role](/img/aws-roles-create-role.png)

The **Account ID** you enter is the ID of the AWS account as determined in step 1.

It is important that the **Require external ID** and **Require MFA** options
remain unchecked!

Proceed to the next step to set up permissions.

### 3. Permissions setup

In the **Attach permissions policies** section, hit the **Create policy** button.

Paste the JSON code from [tenant_cluster.json](https://raw.githubusercontent.com/giantswarm/aws-operator/master/policies/tenant_cluster.json) into the JSON editor field and then hit the **Review policy** button.

In the next step you have to assign a name to the policy. Please use the name

```nohighlight
GiantSwarmAWSOperatorPolicy
```

### 4. Attach policy to role

Once you created the policy, let's turn back to the point in role creation called
*Attach permissions policies*. Here you can now hit the *Refresh* button to load
all existing policies, then enter `GiantSwarmAWSOperatorPolicy` into the search
field to select the policy you just created. Check the box in the row containing
that policy.

![AWS IAM console: Attach policy](/img/aws-roles-attach-policy.png)

Then proceed to the next step.

### 5. Name the role

The last step of role creation requires you to set a name for the role. Please
set the name to `GiantSwarmAWSOperator`.

![AWS IAM console: Review](/img/aws-roles-review.png)

You may also set a description for team members to better understand the reasons
for the existence of this role. It could be helpful to also paste a link to this
guide into the field for reference.

### 6. Get the role's ARN

After creating the new role, you should have a list of all IAM roles in front of
you. From that list, open the `GiantSwarmAWSOperator` role you just created.

The role details screen shows the _Role ARN_, which is a unique identifier for
the role. It should look like

```nohighlight
arn:aws:iam::<YOUR_ACCOUNT_ID>:role/GiantSwarmAWSOperator
```

Please copy the exact ARN from the screen, as you will have to provide it to us
later.

## Create an IAM role for Giant Swarm staff {#operator-iam-role}

The second IAM role to be created is similar to the one before, but in this case
it is used by Giant Swarm support staff. The main differences will be that this
role must have Giant Swarm's account as a trusted entity, instead of the account
running the control plane, and it can have multi-factor authentication enabled.

### 1. Basic role setup

- Like above, go to the [Roles](https://console.aws.amazon.com/iam/home#/roles)
subsection of the AWS console and select **Create role**. When asked to
**Select type of trusted entity** chose **Another AWS account**.

- In **Account ID** enter the value `084190472784`.

- As above, **do not** enable **Require external ID**.

- Different from above, instead, we strongly recommended to check the option
  **Require MFA** (multi factor authorization). This adds an extra
  authentication step for users to assume the role, which increases security.

### 2. Permission setup

Select **Create policy** to create another policy. Use the same JSON policy code
as before. This time, call the policy

```nohighlight
GiantSwarmAdminPolicy
```

**Background**: We ask you to create two distinct, but identical, IAM roles at
this point. This enables you to later adjust permissions independently if the
need arises.

### 3. Attach policy to role

Attach the new `GiantSwarmAdminPolicy` policy to the role you are creating.

### 4. Name the role

Name this role

```nohighlight
GiantSwarmAdmin
```

accordingly.

### 5. Get the role's ARN

From the conformation screen, copy the exact ARN again. It should be in the form of

```nohighlight
arn:aws:iam::<YOUR_ACCOUNT_ID>:role/GiantSwarmAdmin
```

## Configure the Giant Swarm organization {#configure-org}

In the previous sections, we explained how to create two IAM roles in the
AWS account that's going to run the Giant Swarm tenant clusters.

Giant Swarm tenant clusters are owned by _organizations_, which allows you to control
access to clusters, since only members of the owner organization have access to
the management functions of a cluster.

In order to run a tenant cluster in your AWS account, the organization owning
your cluster has to know about the roles you just created.

If you have direct access to the Giant Swarm API, please set the credentials of
your organization with our CLI [gsctl](/reference/gsctl/). Look for the
[`update organization set-credentials`](/reference/gsctl/update-org-set-credentials/#aws)
command.

In case you work with a Giant Swarm partner, it might be that you don't have
access to the Giant Swarm API. In that case, please hand over the role ARNs for
the `GiantSwarmAWSOperator` role and the `GiantSwarmAdmin` role to your partner
contact.

After the organization's credentials are set, you can create clusters owned by that
organization. These clusters' resources will be created in your AWS account.

## Further reading

- [Basics and Concepts: Bring Your Own Cloud](/basics/byoc/)
- [gsctl Reference: `update organization set-credentials`](/reference/gsctl/update-org-set-credentials/)
- [API: Set credentials](https://docs.giantswarm.io/api/#operation/addCredentials)
- [Giant Swarm Architecture](/basics/aws-architecture/)
- [Giant Swarm API documentation](https://docs.giantswarm.io/api/)
- [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [AWS Support Center](https://console.aws.amazon.com/support/home)
