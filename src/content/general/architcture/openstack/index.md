---
linkTitle: Openstack
title: The Giant Swarm Openstack architecture
description: Architecture overview showing how Giant Swarm is set up within a customer data center on Open stack deployment, using cluster API.
weight: 30
menu:
  main:
    parent: general-architecture
last_review_date: 2022-02-02
user_questions:
  - Do you run Openstack?
aliases:
  - /basics/openstack-architecture/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---


# The Giant Swarm Openstack Architecture

Giant Swarm's architecture is split into two logical parts. One describes the management cluster and the other describes one or more workload clusters. We prefer running on bare metal machines, but can also work with virtualized infrastructure (e.g. VMWare) in cases where nested virtualization is possible.

## Giant Swarm on-premises management cluster

## Giant Swarm on-premises workload cluster(s)

## Service architecture

## Networking

How this works (?)

## Storage

OS Image sizing https://gigantic.slack.com/archives/C025SV21RP1/p1644155487565489

## Further Reading

* [Giant Swarm VPN and secure cluster access]({{< relref "/security/cluster-access" >}})
