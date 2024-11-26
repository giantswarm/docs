---
linkTitle: Overview
title: Customer support
description: The support we provide is an essential part of our offering. Here we explain various support service processes and workflows.
weight: 10
last_review_date: 2024-11-25
user_questions:
  - What should I know when working with Giant Swarm's support staff?
  - How is Giant Swarm organizing support?
menu:
  principal:
    parent: support
    identifier: support-overview
owner:
  - https://github.com/orgs/giantswarm/teams/team-planeteers
---

Giant Swarm has developed a custom support model to offer exceptional assistance by defining different layers of support.

## Direct support via Slack

Our first level of support involves close interactions via Slack, ensuring bi-directional feedback as quickly as possible. This channel is also used to answer a variety of questions, which can extend beyond the platform to include anything cloud-native.

The first level support is available from 08:00 to 18:00 (CET) on Monday-Friday. With a distributed team across the world, questions are often answered outside these hours. Support shifts rotate across teams, focusing on channels with clear internal handovers.

In case the first line support is unable to resolve your request, it's escalated to an engineer from the team responsible of the component or application in question. This is managed through a 24-hour rotating shift.

## Project management

The shared goal is to build a developer platform together. As the expert in your company's domain, you are supported in creating a valuable experience for your developers. This collaboration involves creating a roadmap and defining the necessary milestones. At the same time, our Solution Architects have created a [training program]({{< relref "/support/training-catalog" >}}) to help you get the most out of the platform.

Every customer is assigned a dedicated `Account Engineer` who holds regular sync meetings to discuss project progress, address any blockers, or manage changes in requirements. This go-to person provides additional support and acts as a backup if the first line support is overloaded.

## Operational support

Our team trust the `DevOps` principle `You build it, you run it` and for that reason each part of the platform is managed by a different team.

On-call engineers monitor all alerts from environments where your workloads run. These engineers are available every day, ensuring that issues are addressed promptly, even during nights and weekends.

Currently, the mean time to acknowledge an alert is around two minutes, with incident resolution typically taking less than two hours. Not all alerts result in downtime; alerts are configured to resolve issues before they lead to actual incidents.

Additionally, you have a dedicated email address to contact the on-call engineer at any time for cases where problems are noticed that haven't been detected by monitoring.

### Fully monitored platform

The Giant Swarm platform includes a monitoring and alerting system that helps the operations team maintain Service Level Agreements (SLAs) across all customer platforms.

The monitoring stack observes the platform's underlying infrastructure, including the networking layer, DNS resolution, Kubernetes core components, cloud providers, and other targets, providing a complete view of system health.

Applications running on top of the platform, offering observability, connectivity, or security, are instrumented to expose metrics to the monitoring system, ensuring continuous operation.

### Incident handling

Whenever an on-call engineer receives an alert from the monitoring platform, the incident process begins. A new Slack channel is created specifically for the issue, where information is gathered. Thanks to [incident.io](https://incident.io) automation, the ops team can quickly escalate an incident or generate a report for you (postmortem).

Treating every alert as an incident offers many benefits: information is contained in a single channel, recurrent problems or trends can be identified to improve the support process, and there is a historical record of actions and information related to specific issues. More information about the incident process can be found in the [Giant Swarm incident process]({{< relref "/support/p1-process" >}}).

### Postmortem process

The `postmortem` culture, [created by Google](https://sre.google/sre-book/postmortem-culture/), is established to document problems correctly, find root causes, and fix them permanently across all installations. Every time an incident is closed, if it's not a false positive, a postmortem is created.

Postmortems are developed throughout the week. On Mondays, the product team meets to distribute postmortems across product teams. During each team's weekly sprint planning, a specific engineer is assigned to each postmortem. Postmortems take priority over feature development, with engineers dedicating at least one day a week to solving these problems.

A postmortem is only closed once the underlying issue is fixed and deployed to all affected environments. Additionally, postmortems often result in new or refined alerts and operational recipes to share knowledge across the operations team.

## The future

The support process is always evolving. As improvements are made, policies, processes, and tools are refined. However, the goals remain clear and steadfast: to provide seamless support to you, the customer.
