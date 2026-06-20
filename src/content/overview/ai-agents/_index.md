---
title: AI agents
description: How AI agents work on the Giant Swarm platform, powered by Muster as an MCP gateway that gives assistants unified, secure access to your fleet.
weight: 35
menu:
  principal:
    parent: overview
    identifier: overview-ai-agents
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - What are AI agents on the Giant Swarm platform?
  - How do AI assistants access my clusters?
  - What is Muster?
---

The Giant Swarm platform is built to be operated by AI agents and people. You can ask an AI assistant—in your IDE or in the developer portal—questions like "are there any pods in CrashLoopBackOff on any cluster?" and get answers grounded in live cluster state, without switching between terminals and dashboards.

The piece that makes this possible is **Muster**, a universal control plane built on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Muster aggregates many MCP servers—Kubernetes and Prometheus access on every management cluster, plus optionally Grafana, Teleport, and others—behind a single, OAuth-protected endpoint. Your AI assistant connects to Muster instead of juggling a separate connection and set of credentials for each server.

## The pieces

- **Muster**: the MCP gateway. It aggregates downstream MCP servers, presents their combined capabilities through one connection, and handles authentication on your behalf.
- **mcp-kubernetes**: runs on each management cluster and exposes Kubernetes resources (pods, deployments, services, logs, events, and more) through a secure MCP API.
- **mcp-prometheus**: runs alongside it on each management cluster and exposes the cluster's metrics through MCP, so the assistant can correlate Kubernetes state with PromQL queries and alerts.
- **Your AI assistant**: VS Code with GitHub Copilot, Cursor, or the developer portal's built-in chat. It talks MCP to Muster and turns your plain-language questions into tool calls.

## In this section

- [Introduction]({{< relref "/overview/ai-agents/introduction" >}}): what Muster is and the problem it solves.
- [Architecture]({{< relref "/overview/ai-agents/architecture" >}}): the aggregator design and how fleet-wide aggregation works.
- [Meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}): the small tool surface agents actually see, and how lazy discovery keeps context lean.
- [Security]({{< relref "/overview/ai-agents/security" >}}): OAuth 2.1, per-user tool visibility, and single sign-on across clusters.

To set up an assistant in your IDE today, follow [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
