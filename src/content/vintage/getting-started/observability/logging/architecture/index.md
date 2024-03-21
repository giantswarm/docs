---
linkTitle: Logging architecture
title: Logging architecture
description: Documentation on the logging architecture deployed and maintained by Giant Swarm.
weight: 80
menu:
  main:
    identifier: getting-started-observability-logging-architecture
    parent: getting-started-observability-logging
user_questions:
  - What is the logging architecture?
  - Why is Giant Swarm using loki?
  - Why is Giant Swarm recommending loki?
  - Which logs are stored by Giant Swarm?
aliases:
  - /getting-started/observability/logging/architecture
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-03-21
---

Logging is an important pillar of observability and so it is expected that Giant Swarm provides and manages a logging solution for operational purposes.

This documentation will teach you about which logs are stored by Giant Swarm, which technology we use to ship and store them as well as why we use those tools.

## Logs stored by Giant Swarm

Which logs are expected to be found in Loki (and which ones not)

## Overview of the logging pipeline

Logging agents, Loki and grafana, log pipeline overall.

### Why we prefer Loki over its competitors

Explain why we use this instead of other stuff (elastic?)
