---
title: Agent Platform
linkTitle: Agent Platform
description: How-to guides for platform teams operating the Agent Platform, authoring workflows, managing MCP servers, and wiring multi-cluster access, RBAC, and single sign-on.
weight: 60
menu:
  principal:
    parent: tutorials
    identifier: tutorials-agent-platform
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - How do I author a Muster workflow?
  - How do I add an MCP server to Muster?
  - How do I give AI agents access to multiple clusters?
aliases:
  - /tutorials/ai-agents/
---

These guides are for platform teams and power users who operate the Agent Platform, rather than for people who just want to ask their AI assistant a question. If you only need to connect your IDE or the developer portal chat, start with [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) instead.

For the concepts behind everything here, see the [Agent Platform overview]({{< relref "/overview/agent-platform" >}}): what Muster is, how the [aggregator]({{< relref "/overview/agent-platform/architecture" >}}) works, the [meta-tools]({{< relref "/overview/agent-platform/meta-tools" >}}) agents actually see, and the [security model]({{< relref "/overview/agent-platform/security" >}}).

## In this section

- [Author a workflow]({{< relref "/tutorials/agent-platform/authoring-workflows" >}}): package a multi-step operation as a single `workflow_<name>` tool, written the code-grounded way.
- [Save tokens with workflows]({{< relref "/tutorials/agent-platform/saving-tokens-with-workflows" >}}): why one workflow call is dramatically cheaper than a raw-tool loop, with the measured numbers and the design rules that maximize the saving.
- [Manage MCP servers]({{< relref "/tutorials/agent-platform/managing-mcp-servers" >}}): add and configure downstream servers with `MCPServer` resources.
- [Connect custom MCP servers]({{< relref "/tutorials/agent-platform/connecting-custom-mcp-servers" >}}): bring third-party servers behind the gateway, including ones that don't publish standard discovery metadata.
- [Give agents multi-cluster access]({{< relref "/tutorials/agent-platform/multi-cluster-access" >}}): expose a whole fleet through one central Muster.
- [Map RBAC and SSO]({{< relref "/tutorials/agent-platform/access-control" >}}): connect identity-provider groups to cluster permissions.
- [Troubleshoot agent access]({{< relref "/tutorials/agent-platform/troubleshooting" >}}): work through authentication loops, missing tools, and disconnected clusters.

## Operating the platform versus self-hosting

The guides in this section are about **operating the platform**: authoring workflows, managing MCP servers, wiring multi-cluster access, mapping RBAC and SSO, and troubleshooting. They apply whether Muster is run for you on the managed Giant Swarm platform or you host it yourself.

If you also **run your own Muster**, the [self-hosting]({{< relref "/tutorials/agent-platform/self-hosting" >}}) subsection covers deploying the Helm charts, protecting the endpoint with OAuth, and bridging single sign-on across multiple management clusters. Those guides don't apply on the managed Giant Swarm platform, where Muster is already deployed and protected for you.
