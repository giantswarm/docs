---
linkTitle: Overview
title: Overview on spot virtual machines on Azure
description: A general description of spot instances, it's benefits, usage and differences from on-demand instance types.
weight: 10
menu:
  main:
    identifier: advanced-spotinstances-azure-overview
    parent: advanced-spotinstances-azure
user_questions:
  - How can I use Azure spot VMs in my clusters?
  - How can I use Azure spot virtual machines in my clusters?
  - As of which release are Azure spot VMs supported?
  - What's the difference between spot VMs and on-demand VMs on Azure?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2021-01-01
---

{{< platform_support_table azure="ga=v14.1.0" >}}

## Introduction

As of workload cluster release v{{% first_azure_spotinstances_version %}} for Azure, it is possible to use spot virtual machines (VMs) in clusters that will allow you to optimize your cost.

The main differences between spot and on-demand VMs are that spot VMs can be terminated any time by Microsoft Azure. They are also more frequently unavailable.

By default at Giant Swarm you can create node pool with spot VMs that will be dynamically billed up to the max price of the on-demand VMs. This is the generic [Azure feature](https://docs.microsoft.com/en-us/azure/virtual-machines/spot-vms#pricing) and the value is set as `-1` by default at creation for the max price.

Instead of default behavior you can also set the hourly max price for a spot VM which is determined by Azure through a bidding system. The resulting price varies over time and is usually much lower than the cost of the same VM size when booked as on-demand VM.

On Azure it is not supported to have mixed node pools having on-demand and spot VMs at the same time.

## Notes on using spot VMs

Since the availability of spot VMs is volatile, there are a few things you can consider:

- The more availability zones you cover with your node pool, the higher the likelihood that spot VMs are available when required.
- When no spot VMs are available, missing spot VMs are _not_ replaced by on-demand VMs. The affected node pool will fail in deployment on Azure, probably leaving some pods unscheduled. For a solution to this, check our guide on [using on-demand VMs as fall-back when spot VMs are unavailable]({{< relref "/advanced/cluster-management/spot-instances/azure/ondemand-fallback" >}}).
- It is not possible to change the defined max price for an existing Node Pool. If you want to lower the price limit, please create a new node pool.
- To optimize your costs further, you can add reservations for spot VMs via the portal, just as for on-demand VMs.
- Before the first deployment of spot VMs, please remember to increase the quotas for spot virtual machines for the given subscription.
