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
  - Where are the logs stored by Giant Swarm?
aliases:
  - /getting-started/observability/logging/architecture
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-03-21
---

Logging is an important pillar of observability and it is thus only natural that Giant Swarm provides and manages a logging solution for operational purposes.

This documentation will give you an overview of how logging is managed by Giant Swarm : which logs are stored, which tools we use to ship and store them as well as why we chose those tools in the first place.

## Overview of the logging pipeline

Logging agents, Loki and grafana, log pipeline overall.

## Logs stored by Giant Swarm

Kubernetes clusters produces a vast amount of logs, whether they come from machines or containers.

The loggings agents that we have deployed on both management and workload clusters currently send the following logs to Loki:
- `Kubernetes container logs` in the `kube-system` and `giantswarm` namespaces.
- `Kubernetes events` happenning in the `kube-system` and `giantswarm` namespaces.
- [`Kubernetes audit logs`]({{< relref "./audit-logs#kubernetes-audit-logs" >}})

In the future, we will also store the following logs:
- [`Machine audit logs`]({{< relref "./audit-logs#machine-audit-logs" >}})
- `Teleport audit logs` currently being worked on here: https://github.com/giantswarm/roadmap/issues/3250
- Giant Swarm `customer workload logs` as part of our observability platform being worked on https://github.com/giantswarm/roadmap/issues/2771

## Why we prefer Loki over its competitors

The reasons that lead us to using Grafana Loki in favor of its competitors (which is mostly opendistro in our case) are numerous.

First, we are **strong believers in Open Source** so the full Elastic stack is obviously out of the question.

Second, we are quite used to the Grafana ecosystem and the different tools are made to work with one another whereas the existing logging solutions are either supposed to work on their own (like OpenDistro) or you need to use the full fledge solution (i.e. being able to **collect and correlate all observability data**) which is rarely open-source (coming back to the first point above).

Third, we are full-fledge users of Prometheus and PromQL and **LogQL, the Loki Query Language is a natural extension to PromQL**, which makes it easy for our platform engineers to use and love.

The fourth reason is **cost and resource consumption** as Loki is cheaper to run than because it does not rely that much on persistent storage and uses Object storage instead which is always cheaper in the cloud. The storage of the index is also cheaper for Loki as it uses label-based indexing which is definitely smaller than any kind of text-based indexing solution that full-text search engine can provide.

Finally, the last reason comes down to the history of Giant Swarm and it mostly boil down to **operation and maintenance**. Before we decided to run Loki, we used to run elasticsearch as our logging solution. Elasticsearch in itself is really hard to operate, especially at scale, even more so on Kubernetes because it is by its nature a stateful application (and for good reasons). This was an especially important factor in our decision since we do not need the full capabilities of OpenDistro like full-text search.
