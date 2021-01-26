---
title: Similar AWS EC2 instance types reference
description: Here you find our reference regarding what is considered a similar instance type.
layout: subsection
weight: 500
user_questions:
  - Which EC2 instance types are used when I activate the use of similar instance types for a node pool?
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Similar EC2 Instance Types

## Introduction

Handling of similar instance types is done in [aws-operator](https://github.com/giantswarm/aws-operator) since version 8.3.1, which has been introduced with workload cluster release v{{% first_aws_spotinstances_version %}} for AWS.

Read more about the use of similar instance types in our general article about [node pools](/basics/nodepools/#similar-instance-types).

aws-operator creates an Auto Scaling Group (ASG) for every node pool. If the creator of the node pool activates the use of similar instance types, aws-operator looks up a list of similar instance types and configures the ASG to use all of them. The authoritative lookup list can be found [in the aws-operator source](https://github.com/giantswarm/aws-operator/blob/3ac1cff06b11f73cc5b0491cf3c139714552e7ce/service/controller/key/machine_deployment.go).

## Type mapping

| Series | Selected type | Enabled types              |
|--------|---------------|----------------------------|
| m4     | `m4.xlarge`   | `m4.xlarge`, `m5.xlarge`   |
| m4     | `m4.2xlarge`  | `m4.2xlarge`, `m5.2xlarge` |
| m4     | `m4.4xlarge`  | `m4.4xlarge`, `m5.4xlarge` |
| m5     | `m5.xlarge`   | `m4.xlarge` , `m5.xlarge`  |
| m5     | `m5.2xlarge`  | `m4.2xlarge`, `m5.2xlarge` |
| m5     | `m5.4xlarge`  | `m4.4xlarge`, `m5.4xlarge` |
| r4     | `r4.xlarge`   | `r4.xlarge`, `r5.xlarge`   |
| r4     | `r4.2xlarge`  | `r4.2xlarge`, `r5.2xlarge` |
| r4     | `r4.4xlarge`  | `r4.4xlarge`, `r5.4xlarge` |
| r4     | `r4.8xlarge`  | `r4.8xlarge`, `r5.8xlarge` |
| r5     | `r5.xlarge`   | `r4.xlarge`, `r5.xlarge`   |
| r5     | `r5.2xlarge`  | `r4.2xlarge`, `r5.2xlarge` |
| r5     | `r5.4xlarge`  | `r4.4xlarge`, `r5.4xlarge` |
| r5     | `r5.8xlarge`  | `r4.8xlarge`, `r5.8xlarge` |

If the type you are using for your node pool is not contained in the list above, activating the use of similar instance types has no effect.

## Further reading

- [AWS EC2 instance types](https://aws.amazon.com/ec2/instance-types/)
- [Auto Scaling Groups with Multiple Instance Types and Purchase Options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)
