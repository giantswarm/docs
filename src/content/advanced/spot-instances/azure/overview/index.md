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

As of workload cluster release v{{% first_azure_spotinstances_version %}} for Azure, it is possible to use spot instances in clusters that will allow you to optimize your cost.

The main differences between spot and on-demand instances are that spot instances can be terminated any time by the cloud provider. They are also more frequently unavailable.

The hourly price for a spot instance is determined by the cloud provider through a bidding system. The resulting price varies over time and is usually much lower than the cost of the same instance type when booked as on-demand instance. To maximize the likelihood of getting a spot instance when needed, the configuration for Giant Swarm is set to bid up to the price of an on-demand instance with the same type, but not more. This is the generic [Azure feature](https://docs.microsoft.com/en-us/azure/virtual-machines/spot-vms#pricing) that allows to set spot instances dynamic price up to the standard VMs price

On Azure it is not supported to have mixed node pools having on-demand and spot instances at the same time. It is possible to set a custom bid price as a maximum value.

## Notes on using spot instances

Since the availability of spot instances is volatile, there are a few things you can consider:

- The more availability zones you cover with your node pool, the higher the likelihood that spot instances are available when required.
- When no spot instances are unavailable, missing spot instances are _not_ replaced by on-demand instances. The affected node pool will fail in deployment on Azure, probably leaving some pods unscheduled. For a solution to this, check our guide on [using on-demand instances as fall-back when spot instances are unavailable](/advanced/spot-instances/azure/on-demand-fallback/ ).
