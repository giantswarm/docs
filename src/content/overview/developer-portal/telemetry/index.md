---
title: Usage data collection in the developer portal
diataxis_content_type: reference
linkTitle: Usage data
description: Which anonymous usage data the developer portal collects, and how Giant Swarm uses it to prioritize the portal's development.
weight: 1000
menu:
  principal:
    parent: overview-developer-portal
    identifier: overview-developer-portal-telemetry
last_review_date: 2026-10-02
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - What usage data does the developer portal collect?
  - How does Giant Swarm use the usage data collected from the developer portal?
  - Where is usage data from the developer portal stored?
---

The developer portal collects anonymous usage data: which pages people open, and which meaningful actions they complete there, for example creating an agent or registering an MCP server. This tells us which parts of the portal are used and how, so we can prioritize its development.

## Details we collect

Usage data is only collected when it's configured for your portal. Each data point carries:

- A user identifier, salted and hashed before it leaves the browser. It allows counting users; it never contains a name or email address.
- The portal's release version.

### Page views

On every navigation, the name of the page (for example `Clusters index`) and its path.

### Actions

When a person completes an action that matters for the product, one data point named after the action, for example `AgentPlatform.agentCreated`. Its attributes take only values from a fixed list, such as `deploy` or `commit`. No prompts, names of agents, servers or clusters, URLs or search terms are part of it. A failed attempt sends nothing.

The [list of collected actions](https://github.com/giantswarm/backstage/blob/main/docs/telemetry.md#actions), with every attribute and its possible values, is kept in the portal's source code and checked by its tests, so it always matches what the portal sends.

Backstage's own built-in analytics events, such as searches, aren't collected.

## Data storage

Data is submitted to [TelemetryDeck](https://telemetrydeck.com/), who use Microsoft Azure servers in Amsterdam, Netherlands.

For more information, see the [TelemetryDeck privacy FAQ](https://telemetrydeck.com/docs/guides/privacy-faq/).
