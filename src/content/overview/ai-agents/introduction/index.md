---
title: Introduction to Muster
linkTitle: Introduction
description: What Muster is, the MCP-server-sprawl problem it solves, and how intelligent tool aggregation makes AI assistants on the platform cheaper and more capable.
weight: 10
menu:
  principal:
    parent: overview-ai-agents
    identifier: overview-ai-agents-introduction
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-22
user_questions:
  - What is Muster?
  - Why do I need an MCP gateway?
  - What problem does Muster solve?
---

The Giant Swarm platform is built to be operated by AI agents and people. You can ask an AI assistant—in your IDE or in the developer portal—questions like "are there any pods in CrashLoopBackOff on any cluster?" You get answers grounded in live cluster state, without switching between terminals and dashboards.

The piece that makes this possible is **Muster**, a universal control plane built on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). It aggregates many MCP servers—Kubernetes and Prometheus access on every management cluster, plus optionally Grafana, Teleport, and others—behind a single, OAuth-protected endpoint, and gives AI agents intelligent tool discovery, OAuth-based authentication, workflow orchestration, and dynamic tool loading. Your AI assistant connects to Muster instead of juggling a separate connection and set of credentials for each server.

## The pieces

- **Muster**: the MCP gateway. It aggregates downstream MCP servers, presents their combined capabilities through one connection, and handles authentication on your behalf.
- **mcp-kubernetes**: runs on each management cluster and exposes Kubernetes resources (pods, deployments, services, logs, events, and more) through a secure MCP API.
- **mcp-prometheus**: runs alongside it on each management cluster and exposes the cluster's metrics through MCP, so the assistant can correlate Kubernetes state with PromQL queries and alerts.
- **Your AI assistant**: Claude Code, Cursor, VS Code with GitHub Copilot, the developer portal's built-in chat, and other MCP-capable tools. It talks MCP to Muster and turns your plain-language questions into tool calls.

## The MCP server sprawl problem

MCP lets an AI assistant call tools exposed by an MCP server—for example, "list the pods in this namespace" against a Kubernetes cluster. That works well for a single server. It breaks down quickly once you have many.

A Giant Swarm customer typically operates a fleet: several management clusters, each with its own Kubernetes API, plus supporting systems such as Prometheus for metrics or Teleport for access. Wiring an assistant directly to these means:

- A separate MCP server connection to configure and maintain for every cluster and every system.
- Separate credentials and authentication flows for each one.
- Every server's full tool list loaded into the assistant's context window at once—hundreds of tools, most of them irrelevant to the task at hand. That pollutes the context and drives up token cost on every interaction.

## Intelligent aggregation

Muster acts as a **meta-MCP server**: a single aggregation point that manages many downstream MCP servers and presents their combined capabilities through one connection. Your AI assistant connects to Muster, not to each server individually.

Three properties make the aggregation "intelligent" rather than a simple proxy:

- **Conflict-free naming.** When two servers expose a tool with the same name, Muster prefixes external tools with their server name, so a tool such as `x_kubernetes_get_pods` or `x_prometheus_query` never collides.
- **A small, stable tool surface.** Instead of exposing every underlying tool, Muster exposes a handful of [meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}). Agents discover and invoke the full set of capabilities on demand, so the context stays lean and adding or removing a downstream server doesn't change the assistant's configuration.
- **Live lifecycle management.** Muster manages downstream server processes, monitors their health, and updates its tool registry dynamically—no IDE restart required when capabilities change.

## What you get

- **One endpoint, one login.** Authenticate once via your enterprise SSO and reach your whole fleet. Muster handles forwarding and exchanging tokens to downstream servers and clusters transparently—see [Security]({{< relref "/overview/ai-agents/security" >}}).
- **Lower cost.** Because agents only load the tools they actually use, and because multi-step operations can be packaged as single [workflow]({{< relref "/overview/ai-agents/architecture" >}}#workflows-cut-agent-token-cost) calls, the token cost of an AI interaction drops substantially.
- **Capabilities beyond Kubernetes.** Any MCP server can sit behind Muster—metrics, dashboards, access brokers, and custom internal tools—all reachable through the same connection.

Continue with the [architecture]({{< relref "/overview/ai-agents/architecture" >}}) to see how the gateway is structured, or jump straight to [setting up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
