---
linkTitle: Similar EC2 instance types
title: Similar AWS EC2 instance types reference
description: Here you find our reference regarding what is considered a similar instance type.
weight: 50
menu:
  main:
    parent: advanced-spotinstances-aws
user_questions:
  - Which EC2 instance types are used when I activate the use of similar instance types?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-04-04
aliases:
  - /reference/similar-ec2-instance-types/
---

{{< platform_support_table aws="ga=11.2.0" >}}

## Introduction

Handling of similar instance types is done in [aws-operator](https://github.com/giantswarm/aws-operator) since version 8.3.1, which has been introduced with workload cluster release v{{% first_aws_spotinstances_version %}} for AWS.

Read more about the use of similar instance types in our general article about [node pools]({{< relref "/advanced/node-pools#similar-instance-types" >}}).

aws-operator creates an Auto Scaling Group (ASG) for every node pool. If the creator of the node pool activates the use of similar instance types, aws-operator looks up a list of similar instance types and configures the ASG to use all of them.

## Type mapping

| Series | Selected type  | Enabled types                                                                                 |
|--------|----------------|-----------------------------------------------------------------------------------------------|
 c6 | `c6a.2xlarge` | `c6a.2xlarge`,`c6i.2xlarge`,`c5a.2xlarge`,`c5.2xlarge` |
 c6 | `c6a.4xlarge` | `c6a.4xlarge`,`c6i.4xlarge`,`c5a.4xlarge`,`c5.4xlarge` |
 c6 | `c6a.8xlarge` | `c6a.8xlarge`,`c6i.8xlarge`,`c5a.8xlarge`,`c5.8xlarge` |
 c6 | `c6a.12xlarge` | `c6a.12xlarge`,`c6i.12xlarge`,`c5a.12xlarge`,`c5.12xlarge` |
 c6 | `c6a.16xlarge` | `c6a.16xlarge`,`c6i.16xlarge`,`c5a.16xlarge`,`c5.16xlarge` |
 c6 | `c6a.24xlarge` | `c6a.24xlarge`,`c6i.24xlarge`,`c5a.24xlarge`,`c5.24xlarge` |
 c6 | `c6a.32xlarge` | `c6a.32xlarge`,`c6i.32xlarge` |
 c6 | `c6i.12xlarge` | `c6a.12xlarge`,`c6i.12xlarge`,`c5a.12xlarge`,`c5.12xlarge` |
 c6 | `c6i.16xlarge` | `c6a.16xlarge`,`c6i.16xlarge`,`c5a.16xlarge`,`c5.16xlarge` |
 c6 | `c6i.24xlarge` | `c6a.24xlarge`,`c6i.24xlarge`,`c5a.24xlarge`,`c5.24xlarge` |
 c6 | `c6i.2xlarge` | `c6a.2xlarge`,`c6i.2xlarge`,`c5a.2xlarge`,`c5.2xlarge` |
 c6 | `c6i.32xlarge` | `c6a.32xlarge`,`c6i.32xlarge` |
 c6 | `c6i.4xlarge` | `c6a.4xlarge`,`c6i.4xlarge`,`c5a.4xlarge`,`c5.4xlarge` |
 c6 | `c6i.8xlarge` | `c6a.8xlarge`,`c6i.8xlarge`,`c5a.8xlarge`,`c5.8xlarge` |
 m4 | `m4.xlarge` | `m4.xlarge`,`m5.xlarge`,`m6i.xlarge` |
 m4 | `m4.2xlarge` | `m4.2xlarge`,`m5.2xlarge`,`m6i.2xlarge` |
 m4 | `m4.4xlarge` | `m4.4xlarge`,`m5.4xlarge`,`m6i.4xlarge` |
 m4 | `m4.16xlarge` | `m4.16xlarge`,`m5.16xlarge`,`m6i.16xlarge` |
 m5 | `m5.xlarge` | `m5.xlarge`,`m4.xlarge`,`m6i.xlarge` |
 m5 | `m5.2xlarge` | `m5.2xlarge`,`m4.2xlarge`,`m6i.2xlarge` |
 m5 | `m5.4xlarge` | `m6i.4xlarge`,`m5.4xlarge`,`m4.4xlarge` |
 m5 | `m5.16xlarge` | `m5.16xlarge`,`m4.16xlarge`,`m6i.16xlarge` |
 m5 | `m5.24xlarge` | `m5.24xlarge`,`m6i.24xlarge` |
 m5 | `m5a.xlarge` | `m5a.xlarge`,`m6a.xlarge` |
 m5 | `m5a.2xlarge` | `m5a.2xlarge`,`m6a.2xlarge` |
 m5 | `m5a.4xlarge` | `m5a.4xlarge`,`m6a.4xlarge` |
 m5 | `m5a.12xlarge` | `m5a.12xlarge`,`m6a.12xlarge` |
 m5 | `m5a.16xlarge` | `m5a.16xlarge`,`m6a.16xlarge` |
 m5 | `m5a.24xlarge` | `m5a.24xlarge`,`m6a.24xlarge` |
 m6 | `m6a.xlarge` | `m6a.xlarge`,`m6i.xlarge`,`m5.xlarge`,`m5a.xlarge` |
 m6 | `m6a.2xlarge` | `m6a.2xlarge`,`m6i.2xlarge`,`m5a.2xlarge`,`m5.2xlarge` |
 m6 | `m6a.4xlarge` | `m6a.4xlarge`,`m6i.4xlarge`,`m5a.4xlarge`,`m5.4xlarge` |
 m6 | `m6a.8xlarge` | `m6i.8xlarge`,`m6a.8xlarge`,`m5a.8xlarge`,`m5.8xlarge` |
 m6 | `m6a.12xlarge` | `m6a.12xlarge`,`m6i.12xlarge`,`m5a.12xlarge`,`m5.12xlarge` |
 m6 | `m6a.16xlarge` | `m6a.16xlarge`,`m6i.16xlarge`,`m5a.16xlarge`,`m5.16xlarge` |
 m6 | `m6a.24xlarge` | `m6a.24xlarge`,`m6i.24xlarge`,`m5.24xlarge`,`m5a.24xlarge` |
 m6 | `m6i.xlarge` | `m6i.xlarge`,`m6a.xlarge`,`m5a.xlarge`,`m5.xlarge` |
 m6 | `m6i.2xlarge` | `m6i.2xlarge`,`m6a.2xlarge`,`m5a.2xlarge`,`m5.2xlarge` |
 m6 | `m6i.4xlarge` | `m6i.4xlarge`,`m6a.4xlarge`,`m5a.4xlarge`,`m5.4xlarge` |
 m6 | `m6i.8xlarge` | `m6i.8xlarge`,`m6a.8xlarge`,`m5a.8xlarge`,`m5.8xlarge` |
 m6 | `m6i.16xlarge` | `m6i.16xlarge`,`m6a.16xlarge`,`m5.16xlarge`,`m5a.16xlarge` |
 m6 | `m6i.24xlarge` | `m6i.24xlarge`,`m6a.24xlarge`,`m5.24xlarge`,`m5a.24xlarge` |
 r4 | `r4.xlarge` | `r4.xlarge`,`r5.xlarge`,`r6i.xlarge` |
 r4 | `r4.2xlarge` | `r4.2xlarge`,`r5.2xlarge`,`r6i.2xlarge` |
 r4 | `r4.4xlarge` | `r4.4xlarge`,`r5.4xlarge`,`r6i.4xlarge` |
 r4 | `r4.8xlarge` | `r4.8xlarge`,`r5.8xlarge`,`r6i.8xlarge` |
 r5 | `r5.xlarge` | `r5.xlarge`,`r4.xlarge`,`r6i.xlarge` |
 r5 | `r5.2xlarge` | `r5.2xlarge`,`r4.2xlarge`,`r6i.2xlarge` |
 r5 | `r5.4xlarge` | `r5.4xlarge`,`r4.4xlarge`,`r6i.4xlarge` |
 r5 | `r5.8xlarge` | `r5.8xlarge`,`r4.8xlarge`,`r6i.8xlarge` |
 r5 | `r5.16xlarge` | `r5.16xlarge`,`r6i.16xlarge` |
 r5 | `r5.24xlarge` | `r5.24xlarge`,`r6i.24xlarge` |
 r6 | `r6a.xlarge` | `r6a.xlarge`,`r6i.xlarge`,`r5.xlarge`,`r5a.xlarge`,`r4.xlarge` |
 r6 | `r6a.2xlarge` | `r6a.2xlarge`,`r6i.2xlarge`,`r5.2xlarge`,`r5a.2xlarge`,`r4.2xlarge` |
 r6 | `r6a.4xlarge` | `r6a.4xlarge`,`r6i.4xlarge`,`r5.4xlarge`,`r5a.4xlarge`,`r4.4xlarge` |
 r6 | `r6a.8xlarge` | `r6a.8xlarge`,`r6i.8xlarge`,`r5a.8xlarge`,`r5.8xlarge`,`r4.8xlarge` |
 r6 | `r6a.16xlarge` | `r6a.16xlarge`,`r6i.16xlarge`,`r5.16xlarge`,`r5a.16xlarge` |
 r6 | `r6a.24xlarge` | `r6a.24xlarge`,`r6i.24xlarge`,`r5.24xlarge`,`r5a.24xlarge` |
 r6 | `r6i.xlarge` | `r6a.xlarge`,`r6i.xlarge`,`r5.xlarge`,`r5a.xlarge`,`r4.xlarge` |
 r6 | `r6i.2xlarge` | `r6i.2xlarge`,`r6a.2xlarge`,`r5.2xlarge`,`r5a.2xlarge`,`r4.2xlarge` |
 r6 | `r6i.4xlarge` | `r6i.4xlarge`,`r6a.4xlarge`,`r5.4xlarge`,`r5a.4xlarge`,`r4.4xlarge` |
 r6 | `r6i.8xlarge` | `r6i.8xlarge`,`r6a.8xlarge`,`r5a.8xlarge`,`r5.8xlarge`,`r4.8xlarge` |
 r6 | `r6i.16xlarge` | `r6i.16xlarge`,`r6a.16xlarge`,`r5.16xlarge`,`r5a.16xlarge` |
 r6 | `r6i.24xlarge` | `r6i.24xlarge`,`r6a.24xlarge`,`r5.24xlarge`,`r5a.24xlarge` |

If the type you are using for your node pool is not contained in the list above, activating the use of similar instance types has no effect.

## Further reading

- [AWS EC2 instance types](https://aws.amazon.com/ec2/instance-types/)
- [Auto Scaling Groups with Multiple Instance Types and Purchase Options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)
