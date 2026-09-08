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
last_review_date: 2026-09-07
user_questions:
  - What can I do in the portal's Agent Platform section?
  - Why is an MCP server read-only in the portal?
  - Where do I see my agent chat sessions?
  - What does the Toolset card on an agent page show?
---

The developer portal's **Agent Platform** section is the visual home of the [Agent Platform]({{< relref "/overview/agent-platform/introduction" >}}): browse the MCP servers behind the gateway, explore and run their tools, inspect workflows, create and manage agents, and review your chat sessions. Everything it shows is the live state of the platform's Kubernetes resources—the portal is a peer client of the same declarative API as `kubectl` and GitOps.

To turn the section on in your portal instance, see [Enable Agent Platform features in Backstage]({{< relref "/tutorials/agent-platform/enable-portal-features" >}}).

## What the section offers

- **MCP servers dashboard.** Fleet-wide health of the MCP servers registered with Muster, grouped by management cluster and server family, built from the `MCPServer` resources' status. A server showing **Auth Required** is healthy—it's waiting for a user sign-in, not broken.
- **MCP usage.** Tool-call volume, outcomes, latency, and top tools and servers, read from the same gateway metrics that feed the platform's Grafana dashboard.
- **Servers.** Every MCP server behind the gateway, sorted into the three groups **Agent Platform**, **Infrastructure**, and **Registered servers**, each with its authentication configuration and live tool listing, plus a registration wizard for adding your own. What you register lands under Registered servers.
- **Workflows.** The platform's [workflows]({{< relref "/tutorials/agent-platform/authoring-workflows" >}}) with their steps, validity, execution statistics, and a run button with execution history.
- **Tool explorer.** Browse and search every tool behind the gateway, inspect its schema, and execute it with a form generated from that schema. Authorization stays where it belongs: the portal executes what Muster exposes to *you*, and a call you aren't permitted to make is rejected downstream.
- **Agents.** The agents running on the platform, each with its readiness, configuration, system prompt, skills, toolset, and owning deployment—plus the [create-an-agent flow]({{< relref "/tutorials/agent-platform/create-an-agent" >}}), whose required **Tools** step composes the toolset.
- **Sessions.** Your own chat sessions with agents across the fleet: conversation timeline, tool calls, and token usage. Sessions are private to the signed-in user.
- **Models.** The model configurations agents can run on, per installation, each with the accepted state the runtime reports and the reason when it isn't, plus a form to add one with your own API key. Nothing is accepted until you [bring your own model]({{< relref "/tutorials/agent-platform/bring-your-own-model" >}}).

## Three groups of MCP servers

The servers page sorts MCP servers the way the whole platform does, and the names match the [introduction]({{< relref "/overview/agent-platform/introduction" >}}#three-groups-of-mcp-servers):

- **Agent Platform**: the platform's own management surface—agent-manager, model-manager, and Muster's core tools.
- **Infrastructure**: the servers for the management clusters of Giant Swarm installations—mcp-kubernetes, mcp-capi, and mcp-prometheus. A server federated across several management clusters is one row with a pill per cluster.
- **Registered servers**: everything an installation or a user registers, whether through GitOps or the portal's registration wizard.

The group is orientation, not authorization. Which tools you can call is still decided by each server's sign-in and the clusters' RBAC, exactly as in the tool explorer.

## What an agent can use

An agent page carries a **Toolset** card. It shows the [toolset]({{< relref "/overview/agent-platform/toolsets" >}}) the agent declares, read from the `X-Muster-Toolset` header on its gateway entry—the same declaration `kubectl` shows. It also shows what that toolset resolves to **for you**, per group and server, linking into the tool explorer. The resolution is yours because a toolset is always intersected with the viewer's own access. A selector that matches nothing for you is marked as such. Where your own sign-in is what's missing, the card offers the same **Sign in** as the servers page instead of showing the server empty. A teammate with access to more servers sees more.

Three labels stand out on purpose:

- **Implicit full access**: the agent's release declares no toolset, so its requests carry no header and it can reach everything the gateway exposes to whoever talks to it—how every agent behaved before toolsets existed. Agents created before the Tools step, and hand-written releases without a `toolset` value, show this label until someone assigns a toolset through agent-manager's `update_agent` or a new revision.
- **No tools**: the toolset is `preset:none`, or the agent has no gateway entry at all—a chat-only agent.
- **Full gateway access**: the `full` preset, chosen on purpose in the Tools step.

If the toolset names a preset the installation no longer defines, the card shows Muster's error verbatim, the same error the agent gets on every tool call. A removed preset is never a silent problem. And if the installation's Muster doesn't evaluate toolsets yet, the card says so and shows the declaration only.

## The provenance model

Every resource in the section carries its provenance, and that decides what the portal lets you do with it:

- **GitOps-managed** resources (deployed by Flux from a Git repository) are **read-only** in the portal. Editing or deleting one live would just be reverted by the reconciler on its next run—a confusing no-op. Instead of a live mutation, the portal hands you the edited manifest to commit where the resource is actually managed: in Git.
- **Manually added** resources (registered through the portal or the API, with no Git source behind them) are **live-editable**: create, edit, and delete take effect immediately.

One nuance worth knowing: *reconciled by Flux* isn't the same as *GitOps-managed*. An agent created through the portal is applied to the cluster and reconciled by Flux, but no file in Git describes it—so it stays editable through the portal's re-deploy path, and its detail page shows how it was deployed rather than a Git source.

## Identity in the section

The portal forwards **your** identity on every call: reading resources uses your token against the clusters' APIs, tool execution rides your Muster session, and deploying an agent applies manifests with your token. What you can see and do in the section is exactly what your Kubernetes RBAC and identity-provider groups allow—there's no separate portal permission system. The [platform integration]({{< relref "/overview/agent-platform/platform-integration" >}}) page explains the model.
