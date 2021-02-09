---
linkTitle: Overview
title: Overview on spot instances on Azure
description: A general description of spot instances, it's benefits, usage and differences from on-demand instance types.
weight: 10
menu:
  main:
    identifier: advanced-spotinstances-azure-overview
    parent: advanced-spotinstances-azure
owner:
  - https://github.com/orgs/giantswarm/teams/team-celestial
---

# Overview on spot instances on Azure

## Introduction

As of workload cluster release v{{% first_azure_spotinstances_version %}} for Azure, it is possible to use spot virtual machines in clusters that will allow you to optimize your cost.

The main differences between spot and on-demand instances are that spot instances can be terminated any time by Microsoft Azure. They are also more frequently unavailable.

By default at Giant Swarm you can create node pool with spot VMs that will be dynamically billed up to the max price of the on-demand VMs. This is the generic [Azure feature](https://docs.microsoft.com/en-us/azure/virtual-machines/spot-vms#pricing) and the value is set as `-1` by default at creation for the max price.

Instead of default behaviour you can also set the hourly max price for a spot instance which is determined by Azure through a bidding system. The resulting price varies over time and is usually much lower than the cost of the same instance type when booked as on-demand instance.

On Azure it is not supported to have mixed node pools having on-demand and spot instances at the same time.

## Notes on using spot instances

Since the availability of spot instances is volatile, there are a few things you can consider:

- The more availability zones you cover with your node pool, the higher the likelihood that spot instances are available when required.
- When no spot instances are available, missing spot instances are _not_ replaced by on-demand instances. The affected node pool will fail in deployment on Azure, probably leaving some pods unscheduled. For a solution to this, check our guide on [using on-demand instances as fall-back when spot instances are unavailable]({{< relref "/advanced/spot-instances/azure/ondemand-fallback" >}}).
- It is not possible to change the defined max price for existing Node Pool, if there is a need for a lower price, it has to be recreated.
- To optimize your costs further, you can add reservations for spot VMs via the portal same as for on-demand machines.
- Before first deployment of spot instances, please remember to increase the quotas for spot virtual machines for the given subscription.
