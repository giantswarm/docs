---
linkTitle: Overview
title: Overview on spot instances on AWS
description: A general description of spot instances, it's benefits, usage and differences from on-demand instance types.
weight: 10
menu:
  main:
    identifier: advanced-spotinstances-aws-overview
    parent: advanced-spotinstances-aws
user_questions:
  - How can I use EC2 spot instances in my clusters?
  - As of which release are AWS EC2 spot instances supported?
  - What's the difference between spot instances and on-demand instances on AWS?
last_review_date: 2023-11-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

{{< platform_support_table aws="ga=v11.2.0" >}}

## Introduction

As of workload cluster release v{{% first_aws_spotinstances_version %}} for AWS, it is possible to use spot instances in clusters that will allow you to optimize your cost.

The main differences between spot and on-demand instances are that spot instances can be terminated any time by AWS. They are also more frequently unavailable.

The hourly price for a spot instance is determined by AWS through a bidding system. The resulting price varies over time and is usually much lower than the cost of the same instance type when booked as on-demand instance. To maximize the likelihood of getting a spot instance when needed, the configuration for Giant Swarm is set to bid up to the price of an on-demand instance with the same type, but not more.

There are two parameters on the node pool level that will allow you to configure which instances are going to be used:

- **On-demand base capacity**: controls how much of the initial capacity is made up of on-demand instances. Note that this capacity is static and does not automatically replace any unavailable spot instances.

- **Spot instance percentage above base capacity**: controls the percentage of spot instances to be used for worker nodes beyond the number of _on-demand base capacity_.

## Notes on using spot instances

Since the availability of spot instances is volatile, there are a few things you can consider:

- The more availability zones you cover with your node pool, the higher the likelihood that spot instances are available when required.
- Activating the [use of similar instance types]({{< relref "/vintage/advanced/cluster-management/spot-instances/aws/similar-instance-types" >}}) also increases the likelihood of getting spot instances when using common instance types. Read more about this below.
- When no spot instances are available, missing spot instances are _not_ replaced by on-demand instances. The affected node pool will instead have less nodes than desired, probably leaving some pods unscheduled. For a solution to this, check our guide on [using on-demand instances as fall-back when spot instances are unavailable]({{< relref "/vintage/advanced/cluster-management/spot-instances/aws/ondemand-fallback" >}}).

## Examples

The following table shows four examples to illustrate how different settings of spot instance percentage and on-demand base capacity influence the outcome.

| On-demand base capacity | Spot instance percentage | Total Instances  | On-Demand Instances| Spot Instances |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 % | 50 | 50 | 0 |
| 0 | 100 % | 50 | 0 | 50 |
| 10 | 50 % | 50 | 30 | 20 |
| 10 | 100 % | 50 | 10 | 40 |
