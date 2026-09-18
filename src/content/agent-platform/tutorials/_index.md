---
title: Agent Platform tutorials
linkTitle: Tutorials
description: How-to guides for platform teams operating the Agent Platform, authoring workflows, managing MCP servers, and wiring multi-cluster access, RBAC, and single sign-on.
weight: 30
menu:
  principal:
    parent: agent-platform
    identifier: agent-platform-tutorials
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-07
user_questions:
  - How do I author a Muster workflow?
  - How do I add an MCP server to Muster?
  - How do I give AI agents access to multiple clusters?
aliases:
  - /tutorials/agent-platform/
  - /tutorials/ai-agents/
---

These guides are for platform teams and power users who operate the Agent Platform, rather than for people who just want to ask their AI assistant a question. If you only need to connect your IDE or the developer portal chat, start with [Set up your AI agent]({{< relref "/agent-platform/getting-started/ai-agent-setup" >}}) instead.

For the concepts behind everything here, see the [Agent Platform overview]({{< relref "/agent-platform/overview" >}}): what Muster is, how the [aggregator]({{< relref "/agent-platform/overview/architecture" >}}) works, the [meta-tools]({{< relref "/agent-platform/overview/meta-tools" >}}) agents actually see, and the [security model]({{< relref "/agent-platform/overview/security" >}}).

## In this section

- [Author a workflow]({{< relref "/agent-platform/tutorials/authoring-workflows" >}}): package a multi-step operation as a single `workflow_<name>` tool, written the code-grounded way.
- [Save tokens with workflows]({{< relref "/agent-platform/tutorials/saving-tokens-with-workflows" >}}): why one workflow call is dramatically cheaper than a raw-tool loop, with the measured numbers and the design rules that maximize the saving.
- [Manage MCP servers]({{< relref "/agent-platform/tutorials/managing-mcp-servers" >}}): add and configure downstream servers with `MCPServer` resources.
- [Define toolset presets]({{< relref "/agent-platform/tutorials/toolset-presets" >}}): ship named tool selections as Muster configuration, so agent authors pick *Read-only tools* or *Test clusters* instead of composing from scratch.
- [Connect custom MCP servers]({{< relref "/agent-platform/tutorials/connecting-custom-mcp-servers" >}}): bring third-party servers behind the gateway, including ones that don't publish standard discovery metadata.
- [Give agents multi-cluster access]({{< relref "/agent-platform/tutorials/multi-cluster-access" >}}): expose a whole fleet through one central Muster.
- [Map RBAC and SSO]({{< relref "/agent-platform/tutorials/access-control" >}}): connect identity-provider groups to cluster permissions.
- [Troubleshoot agent access]({{< relref "/agent-platform/tutorials/troubleshooting" >}}): work through authentication loops, missing tools, and disconnected clusters.
- [Bring your own model]({{< relref "/agent-platform/tutorials/bring-your-own-model" >}}): give the agent runtime a model to run on, with your own API key or a self-hosted endpoint.

## Operating the platform versus self-hosting

The guides in this section are about **operating the platform**: authoring workflows, managing MCP servers, wiring multi-cluster access, mapping RBAC and SSO, and troubleshooting. They apply whether Muster is run for you on the managed Giant Swarm platform or you host it yourself.

If you also **run your own Muster**, the [self-hosting]({{< relref "/agent-platform/tutorials/self-hosting" >}}) subsection covers deploying the Helm charts, protecting the endpoint with OAuth, and bridging single sign-on across multiple management clusters. Those guides don't apply on the managed Giant Swarm platform, where Muster is already deployed and protected for you.
