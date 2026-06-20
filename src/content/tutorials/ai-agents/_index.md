---
title: AI agents and Muster
linkTitle: AI agents
description: How-to guides for platform teams operating Muster, authoring workflows, managing MCP servers, and wiring multi-cluster access, RBAC, and single sign-on.
weight: 60
menu:
  principal:
    parent: tutorials
    identifier: tutorials-ai-agents
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I author a Muster workflow?
  - How do I add an MCP server to Muster?
  - How do I give AI agents access to multiple clusters?
---

These guides are for platform teams and power users who operate Muster, rather than for people who just want to ask their AI assistant a question. If you only need to connect your IDE or the developer portal chat, start with [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) instead.

For the concepts behind everything here, see the [AI agents overview]({{< relref "/overview/ai-agents" >}}): what Muster is, how the [aggregator]({{< relref "/overview/ai-agents/architecture" >}}) works, the [meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}) agents actually see, and the [security model]({{< relref "/overview/ai-agents/security" >}}).

## In this section

- [Author a workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}): package a multi-step operation as a single `workflow_<name>` tool, written the code-grounded way.
- [Save tokens with workflows]({{< relref "/tutorials/ai-agents/saving-tokens-with-workflows" >}}): why one workflow call is dramatically cheaper than a raw-tool loop, with the measured numbers and the design rules that maximize the saving.
- [Manage MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}): add and configure downstream servers with `MCPServer` resources.
- [Connect custom MCP servers]({{< relref "/tutorials/ai-agents/connecting-custom-mcp-servers" >}}): bring third-party servers behind the gateway, including ones that don't publish standard discovery metadata.
- [Give agents multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}): expose a whole fleet through one central Muster.
- [Map RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}): connect identity-provider groups to cluster permissions.
- [Troubleshoot agent access]({{< relref "/tutorials/ai-agents/troubleshooting" >}}): work through authentication loops, missing tools, and disconnected clusters.
