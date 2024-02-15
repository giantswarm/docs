---
linkTitle: Overview
title: Customer support
description: The support we provide is an essential part of our offering. Here we explain various support service processes and workflows.
weight: 10
last_review_date: 2022-12-07
user_questions:
  - What should I know when working with Giant Swarm's support staff?
  - How is Giant Swarm organizing support?
menu:
  main:
    parent: support-training
    identifier: support-training-overview
    weight: 1
aliases:
  - /general/support
  - /basics/giant-swarm-support/
owner:
  - https://github.com/orgs/giantswarm/teams/team-horizon
---

In Giant Swarm we have developed a custom support model. In order to offer a great support we define different layers of assistance.

## Direct Support via Slack

Our first level support relies on close interactions via Slack, to ensure bi-directional feedback as quickly as possible. This interaction channel is also used to answer a variety of questions. The conversations are not limited to the platform itself, but can go broader and include anything cloud-native.

Our first level support shifts run from 08:00 to 18:00 (CET) on Monday-Friday. As we have a distributed team across the world, we  often answer questions well outside those times. We rotate support shifts across our teams, which is why we focus on support channels with clear internal handovers.

If there is a problem that the first line support cannot resolve, it is handed over to an engineer who is part of the team responsible for the component or application that is failing. This is a 24 hour rotating shift.

## Project Management

The shared goal is to build a developer platform together. Since you are the expert in your company domain we help you to construct a nice experience for your developers. To make this possible we work together creating a roadmap and defining the milestones need to achieve.

Each customer has a dedicated Account Engineer who holds regular sync meetings to discuss the progress of the project, any blocker or change in requirements. This go-to person provides additional support and acts as a first backup in case the person on first line support is overloaded.

## Operational support

We trust in the DevOps principle "You build it, you run it" and for that reasons each part of the platform is operated for a different team in Giant Swarm.

Our on-call engineers watch over all alerts coming in from all environments where our customers run workloads. The on-call engineers are available 24/7. Thus, ensuring that issues are handled promptly, even on nights and weekends.

Today our mean time to acknowledge an alert is around two minutes and we usually resolve incidents in less than two hours. Obviously, not all alerts result in downtime in a customer environment. As alerts are set to make sure we fix problems before they lead to real incidents.

Additionally, customers have a dedicated email address to reach our on-call engineer 24/7.  This is for cases in which customers notice problems that have not been caught by our monitoring.

### Fully monitor platform

The Giant Swarm platform comes with a monitoring and alerting system that helps our operations team maintain our SLAs across all customer platforms.

The monitoring stack observes the underlying infrastructure of the platform. This includes the networking layer, DNS resolution, Kubernetes core components, cloud providers and any other targets we need to monitor to give us a complete view of the health of the system.

On the other side the applications running on top offering observability, connectivity or security are instrumented to expose metrics to our monitoring system allowing us to maintain those up and running all time.

### Incident handling

Every time our on-call engineer receives an alert from our monitoring platform the incident process kicks off. There is a new Slack channel created specifically for this problem where the engineer can gather all information around. Thanks to [incident.io](https://incident.io) automation the ops team can quickly escalate an incident or generate an inform for the customer (postmortem).

Treating every alert as an incident has many benefits: the information of the incident is contained in a single channel, we can identify recurrent problems or any trends happening in order to improve the support process and we have historical record of the actions and information ocurred in a specific issue.

### Postmortem process

The `postmortem` culture [was created by Google](https://sre.google/sre-book/postmortem-culture/) and was established in order to document a problem correctly, find the root cause and fix it across all installations permanently. Every time we close an incident, if it is not a false positive, we create a postmortem.

Postmortems are created during the whole week. On Mondays, the product team meets and distributes the postmortems across our product teams. As each team plans their weekly sprint they assign a specific engineer to each postmortem. Postmortems have priority over feature development and engineers are used to spending at least a day a week to solve these problems.

The postmortem is closed only once the underlying issue is fixed and deployed to all affected environments. Additionally postmortems often result in new or tuned alerts and ops recipes to share knowledge through the operations team.

## Our future

Our support process is subject to change. As we continuously improve it we discover how to improve our policies, process and tools. But the goals are clear and unchanging. We are committed to seamlessly supporting our customers.

## Further reading

- [Giant Swarm P1 process]({{< relref "/vintage/support/p1-process" >}})
- [Giant Swarm Operation Layers]({{< relref "/vintage/platform-overview/security/operational-layers" >}})
- [Giant Swarm Cluster Upgrades]({{< relref "/vintage/platform-overview/cluster-management/cluster-upgrades" >}})
- [Giant Swarm Training Catalog]({{< relref "/vintage/support/training-catalog" >}})
