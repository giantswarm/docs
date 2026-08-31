---
title: Agent Platform in the developer portal
diataxis_content_type: explanation
linkTitle: Agent Platform
description: What the developer portal's Agent Platform section offers, and how its safety model distinguishes GitOps-managed resources from ones registered through the portal.
weight: 45
menu:
  principal:
    parent: overview-developer-portal
    identifier: overview-developer-portal-agent-platform
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - What can I do in the portal's Agent Platform section?
  - Why is an MCP server read-only in the portal?
  - Where do I see my agent chat sessions?
---

The developer portal's **Agent Platform** section is the visual home of the [Agent Platform]({{< relref "/overview/agent-platform/introduction" >}}): browse the MCP servers behind the gateway, explore and run their tools, inspect workflows, create and manage agents, and review your chat sessions. Everything it shows is the live state of the platform's Kubernetes resources—the portal is a peer client of the same declarative API as `kubectl` and GitOps.

To turn the section on in your portal instance, see [Enable Agent Platform features in Backstage]({{< relref "/tutorials/agent-platform/enable-portal-features" >}}).

## What the section offers

- **MCP servers dashboard.** Fleet-wide health of the MCP servers registered with Muster, grouped by management cluster and server family, built from the `MCPServer` resources' status. A server showing **Auth Required** is healthy—it's waiting for a user sign-in, not broken.
- **MCP usage.** Tool-call volume, outcomes, latency, and top tools and servers, read from the same gateway metrics that feed the platform's Grafana dashboard.
- **Servers.** Every registered MCP server with its authentication configuration and live tool listing, plus a registration wizard for adding your own.
- **Workflows.** The platform's [workflows]({{< relref "/tutorials/agent-platform/authoring-workflows" >}}) with their steps, validity, execution statistics, and a run button with execution history.
- **Tool explorer.** Browse and search every tool behind the gateway, inspect its schema, and execute it with a form generated from that schema. Authorization stays where it belongs: the portal executes what Muster exposes to *you*, and a call you aren't permitted to make is rejected downstream.
- **Agents.** The agents running on the platform, each with its readiness, configuration, system prompt, skills, and owning deployment—plus the [create-an-agent flow]({{< relref "/tutorials/agent-platform/create-an-agent" >}}).
- **Sessions.** Your own chat sessions with agents across the fleet: conversation timeline, tool calls, and token usage. Sessions are private to the signed-in user.

## The provenance model

Every resource in the section carries its provenance, and that decides what the portal lets you do with it:

- **GitOps-managed** resources (deployed by Flux from a Git repository) are **read-only** in the portal. Editing or deleting one live would just be reverted by the reconciler on its next run—a confusing no-op. Instead of a live mutation, the portal hands you the edited manifest to commit where the resource is actually managed: in Git.
- **Manually added** resources (registered through the portal or the API, with no Git source behind them) are **live-editable**: create, edit, and delete take effect immediately.

One nuance worth knowing: *reconciled by Flux* isn't the same as *GitOps-managed*. An agent created through the portal is applied to the cluster and reconciled by Flux, but no file in Git describes it—so it stays editable through the portal's re-deploy path, and its detail page shows how it was deployed rather than a Git source.

## Identity in the section

The portal forwards **your** identity on every call: reading resources uses your token against the clusters' APIs, tool execution rides your Muster session, and deploying an agent applies manifests with your token. What you can see and do in the section is exactly what your Kubernetes RBAC and identity-provider groups allow—there's no separate portal permission system. The [platform integration]({{< relref "/overview/agent-platform/platform-integration" >}}) page explains the model.
