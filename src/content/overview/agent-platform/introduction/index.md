---
title: What's the Agent Platform
diataxis_content_type: explanation
linkTitle: Introduction
description: What the Giant Swarm Agent Platform is - composable, secure, sovereign AI agents at scale, for any task, with governed tool access, running on your own infrastructure.
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
  - What kinds of tasks can agents on the platform do?
  - What is Muster?
  - Why do agents need a platform instead of desktop tooling?
aliases:
  - /overview/ai-agents/introduction/
---

The **Giant Swarm Agent Platform** is an open, sovereign environment for running AI agents in production—for any task. You build agents from reusable, versioned building blocks and give them governed access to exactly the tools their work needs. They run on your own infrastructure: any conformant Kubernetes cluster, in the cloud, on-premises, at the edge, or air-gapped. Your models, your data, and your rules stay under your control.

## From copilots to agents that act

Most AI tooling makes one person faster at their keyboard: a chat window, an IDE copilot, a coding agent run from a terminal. That value stays with the person, at their machine, triggered by their hand.

Agents on the platform are a different kind of workload. They act on events—an alert, a ticket, a schedule, a chat message—rather than on clicks. Running unattended raises the bar: each agent runs isolated, holds scoped credentials for only the tools its task needs, and leaves a trail for every decision. That's what a platform provides and desktop tooling doesn't. It's also how an organization decides *how* agents run, instead of having engineers improvise it one unsupervised script at a time.

## What agents do here

The platform doesn't prescribe a domain. The pattern—an agent with governed tool access, acting on events, auditable end to end—applies wherever the work is:

- **Software engineering**: agents work through backlog items, review code, and run migrations, with their output landing as ordinary pull requests.
- **IT and platform operations**: agents triage incidents and investigate clusters. Ask "are there any pods in CrashLoopBackOff on any cluster?" and get an answer grounded in live cluster state—this is the scenario the platform ships reference tool servers for today.
- **Enterprise compliance**: agents collect evidence continuously instead of in a scramble before the audit.
- **Operational technology**: agents watch processes and inventory, and flag what needs attention before it fails.

The tool access layer is what makes the spectrum wide. Any system that speaks [MCP](https://modelcontextprotocol.io/) can sit behind the platform's gateway with the same governance—internal services, data stores, and third-party APIs alike.

## Two capabilities on one foundation

- **Governed tool access.** Every tool call an agent makes—wherever the agent runs—goes through one gateway path: **agentgateway**, the data-plane choke point for observability and policy, in front of **Muster**, the MCP aggregator that enforces authentication and fans out to the tool servers behind it.
- **An agent runtime.** Agents run on the cluster as Kubernetes resources, managed by a controller and surfaced through the developer portal and chat channels. An agent is versioned as one unit—prompt, toolchain, and skills together—so every version is reproducible and shareable.

The foundation both stand on is your Kubernetes cluster and your existing identity provider. Single sign-on, Kubernetes RBAC, and declarative management apply to agents the same way they apply to people.

## The components

| Component | What it does |
|---|---|
| **Muster** | The MCP gateway. Aggregates many MCP servers behind one OAuth-protected endpoint, enforces authentication, and handles downstream credentials on your behalf |
| **agentgateway** | The data-plane gateway in front of Muster. Every MCP call passes through it, making it the observability and policy choke point |
| **Agent runtime** | Runs agents as Kubernetes resources on the cluster, based on the [kagent](https://kagent.dev/) project |
| **mcp-kubernetes** | Reference tool server for the cluster-operations scenario: exposes a cluster's Kubernetes resources through a secure MCP API |
| **mcp-prometheus** | Reference tool server alongside it: exposes the cluster's metrics through MCP |
| **Developer portal** | The Agent Platform section in Backstage: browse MCP servers, explore tools, run workflows, create agents, and review sessions |
| **Valkey** | Session storage for Muster's OAuth state |
| **Avatar service** | Generates the identifying icons agents carry across every surface |

People use the same door as agents. Claude Code, Cursor, VS Code with GitHub Copilot, the developer portal's built-in chat, and any other MCP-capable client connect to the same endpoint.

## No privileged client

The platform principle: **the Kubernetes API is the interface**. Agents, the developer portal, chat channels, the CLI, and plain `kubectl` are peer clients of the same declarative resources—none of them is privileged. An agent you create through the portal is a set of Kubernetes resources you could equally create with `kubectl apply` or manage through GitOps. What you see in the portal is what runs on the cluster.

## Governed tool access, at falling cost

Wiring an assistant or agent directly to many tool servers means a connection, a credential, and a context-window full of tool definitions for each one. Muster acts as a **meta-MCP server**: one aggregation point that manages the downstream servers and presents their combined capabilities through a single connection.

- **Conflict-free naming.** When two servers expose a tool with the same name, Muster prefixes external tools with their server name, so a tool such as `x_kubernetes_get_pods` never collides.
- **A small, stable tool surface.** Instead of exposing every underlying tool, Muster exposes a handful of [meta-tools]({{< relref "/overview/agent-platform/meta-tools" >}}). Agents discover capabilities on demand, so context stays lean and adding a server doesn't change any client's configuration.
- **Live lifecycle management.** Muster manages downstream server connections, monitors their health, and updates its tool registry dynamically.

On top of that sits a loop that makes repeated agent work cheaper over time. A multi-step task an agent has figured out can be captured as a [workflow]({{< relref "/overview/agent-platform/architecture" >}}#workflows-cut-agent-token-cost): a deterministic, server-side sequence the agent then invokes as a single tool call. The next run leans on the codified path instead of the model, cutting tokens and tool calls substantially.

## Three commitments

- **Sovereign.** The platform is open source and runs entirely in your environment. Models, harnesses, and tools are swappable—there's no proprietary core and nothing calls home with your data.
- **Curated.** The agent landscape changes weekly. The platform integrates a proven selection, and any MCP-speaking tool plugs into the same governed path.
- **Enterprise-ready.** Multi-tenant, secure, and auditable from the first agent: every agent acts with a real human identity, every tool call is traceable, and Kubernetes RBAC gates what actually happens.

Continue with the [architecture]({{< relref "/overview/agent-platform/architecture" >}}) to see how the pieces fit together, read how the platform [integrates with SSO, cluster management, and observability]({{< relref "/overview/agent-platform/platform-integration" >}}), or connect your own assistant via [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
