---
title: What's the Agent Platform
diataxis_content_type: explanation
linkTitle: Introduction
description: What the Giant Swarm Agent Platform is, the two capabilities it provides on one foundation, and how governed tool access through Muster makes AI agents cheaper and safer.
weight: 10
menu:
  principal:
    parent: overview-agent-platform
    identifier: overview-agent-platform-introduction
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - What is the Giant Swarm Agent Platform?
  - What is Muster?
  - Why do I need an MCP gateway?
  - Where do agents run on the platform?
aliases:
  - /overview/ai-agents/introduction/
---

The **Giant Swarm Agent Platform** lets AI agents and people operate your Kubernetes fleet together. Ask an AI assistant—in your IDE, in the developer portal, or in chat—"are there any pods in CrashLoopBackOff on any cluster?" and get answers grounded in live cluster state. You can also run agents on the platform itself, where they work with the same identity rules as everyone else.

The platform provides two capabilities on one foundation:

- **Governed tool access.** Every tool call an agent makes—wherever the agent runs—goes through one gateway path: **agentgateway**, the data-plane choke point for observability and policy, in front of **Muster**, the MCP aggregator that enforces authentication and fans out to the tool servers behind it.
- **An agent runtime.** Agents run on the cluster as Kubernetes resources, managed by a controller and surfaced through the developer portal and chat channels. They reach their tools through the same gateway, carrying the identity of the human they act for.

The foundation both stand on is your Kubernetes cluster and your existing identity provider. Single sign-on, Kubernetes RBAC, and declarative management apply to agents the same way they apply to people.

## The components

| Component | What it does |
|---|---|
| **Muster** | The MCP gateway. Aggregates many MCP servers behind one OAuth-protected endpoint, enforces authentication, and handles downstream credentials on your behalf |
| **agentgateway** | The data-plane gateway in front of Muster. Every MCP call passes through it, making it the observability and policy choke point |
| **mcp-kubernetes** | Runs on each management cluster and exposes its Kubernetes resources through a secure MCP API |
| **mcp-prometheus** | Runs alongside it and exposes the cluster's metrics through MCP, so assistants can correlate Kubernetes state with queries and alerts |
| **Agent runtime** | Runs agents as Kubernetes resources on the cluster, based on the [kagent](https://kagent.dev/) project |
| **Developer portal** | The Agent Platform section in Backstage: browse MCP servers, explore tools, run workflows, create agents, and review sessions |
| **Valkey** | Session storage for Muster's OAuth state |
| **Avatar service** | Generates the identifying icons agents carry across every surface |

Your AI assistant talks to the same endpoint and turns your plain-language questions into tool calls. That covers Claude Code, Cursor, VS Code with GitHub Copilot, the developer portal's built-in chat, and any other MCP-capable client.

## No privileged client

The platform principle: **the Kubernetes API is the interface**. Agents, the developer portal, chat channels, the CLI, and plain `kubectl` are peer clients of the same declarative resources—none of them is privileged. An agent you create through the portal is a set of Kubernetes resources you could equally create with `kubectl apply` or manage through GitOps. What you see in the portal is what runs on the cluster.

## The MCP server sprawl problem

[MCP](https://modelcontextprotocol.io/) lets an AI assistant call tools exposed by an MCP server—for example, "list the pods in this namespace" against a Kubernetes cluster. That works well for a single server. It breaks down quickly once you have many.

A Giant Swarm customer typically operates a fleet: several management clusters, each with its own Kubernetes API, plus supporting systems such as Prometheus for metrics. Wiring an assistant directly to these means:

- A separate MCP server connection to configure and maintain for every cluster and every system.
- Separate credentials and authentication flows for each one.
- Every server's full tool list loaded into the assistant's context window at once—hundreds of tools, most of them irrelevant to the task at hand. That pollutes the context and drives up token cost on every interaction.

## Intelligent aggregation

Muster acts as a **meta-MCP server**: a single aggregation point that manages many downstream MCP servers and presents their combined capabilities through one connection. Your AI assistant connects to the platform's endpoint, not to each server individually.

Three properties make the aggregation "intelligent" rather than a simple proxy:

- **Conflict-free naming.** When two servers expose a tool with the same name, Muster prefixes external tools with their server name, so a tool such as `x_kubernetes_get_pods` or `x_prometheus_query` never collides.
- **A small, stable tool surface.** Instead of exposing every underlying tool, Muster exposes a handful of [meta-tools]({{< relref "/overview/agent-platform/meta-tools" >}}). Agents discover and invoke the full set of capabilities on demand, so the context stays lean and adding or removing a downstream server doesn't change the assistant's configuration.
- **Live lifecycle management.** Muster manages downstream server connections, monitors their health, and updates its tool registry dynamically—no IDE restart required when capabilities change.

## What you get

- **One endpoint, one login.** Authenticate once via your enterprise SSO and reach your whole fleet. Muster handles forwarding and exchanging tokens to downstream servers and clusters transparently—see [Security]({{< relref "/overview/agent-platform/security" >}}).
- **Lower cost.** Because agents only load the tools they actually use, and because multi-step operations can be packaged as single [workflow]({{< relref "/overview/agent-platform/architecture" >}}#workflows-cut-agent-token-cost) calls, the token cost of an AI interaction drops substantially.
- **Capabilities beyond Kubernetes.** Any MCP server can sit behind Muster—metrics, dashboards, and custom internal tools—all reachable through the same connection.
- **Agents as first-class platform citizens.** Agents you run on the platform are versioned, auditable Kubernetes resources that act with a real human identity, never with anonymous machine credentials.

Continue with the [architecture]({{< relref "/overview/agent-platform/architecture" >}}) to see how the pieces fit together, read how the platform [integrates with SSO, cluster management, and observability]({{< relref "/overview/agent-platform/platform-integration" >}}), or jump straight to [setting up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
