+++
title = "Prepare an AWS account to run Giant Swarm tenant clusters"
description = "This guide will walk you through all necessary steps to set up an Amazon AWS account with approriate IAM roles for operating Giant Swarm tenant clusters."
date = "2018-09-12"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Prepare an AWS account to run Giant Swarm tenant clusters

As detailed in the [Architecture](/reference/giantswarm-aws-architecture/) docs,
the tenant clusters (the clusters running your Kubernetes workloads) in a Giant
Swarm installation are running in an AWS account separate from the control plane.
This gives great flexibility depending on the requirements and the usage
scenario. For example, it allows the control plane to be running in an AWS account
owned by Giant Swarm, while tenant clusters operate in different AWS accounts
each, depending on a customer's department using them.

## Overview

In order to run Giant Swarm tenant clusters, an AWS account needs to fulfill
these requirements:

- Service limits set according to requirements
- IAM role to be assumed by our aws-operator software
- IAM role to be assumed by Giant Swarm staff

Each Giant Swarm tenant cluster belongs to an organization within Giant Swarm.
This organization will later be configured with information about the two
IAM roles mentioned above.

## Increase service limits in AWS {#limits}

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
- Elastic IP
  - New VPC Elastic IP Address Limit per region: **50**
- Elastic Load Balancers
  - Application and Classic Load Balancers per region: **100**
- Auto Scaling
  - Auto Scaling Groups per region: **250**
  - Launch Configurations per region: **500**
- EC2 Instances
  - m3.large per region: **250**
  - m4.2xlarge per region: **250**
  - m5.2xlarge per region: **250**
  - other instance types to be used as workers: increase accordingly

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
- [Giant Swarm Architecture](/reference/giantswarm-aws-architecture/)
- [Giant Swarm API documentation](https://docs.giantswarm.io/api/)
- [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [AWS Support Center](https://console.aws.amazon.com/support/home)
