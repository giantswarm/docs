---
title: Self-hosting Muster
linkTitle: Self-hosting
description: Operate your own Muster aggregator. Deploy the Helm charts, protect the endpoint with OAuth and Dex, and bridge single sign-on across multiple management clusters.
weight: 70
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-self-hosting
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - How do I deploy and run my own Muster?
  - How do I protect a self-hosted Muster with OAuth?
  - How do I host Muster across multiple management clusters?
aliases:
  - /tutorials/ai-agents/self-hosting/
---

{{% notice note %}}
**Applies to self-hosted Muster only.** These guides are for teams who operate their own Muster aggregator. On the managed Giant Swarm platform, Muster is deployed and protected for you, so you can skip this section and go straight to the operational guides such as [managing MCP servers]({{< relref "/tutorials/agent-platform/managing-mcp-servers" >}}) and [authoring workflows]({{< relref "/tutorials/agent-platform/authoring-workflows" >}}).
{{% /notice %}}

There are two self-hosting tracks. This section covers running **just the MCP gateway**: Muster, its OAuth protection, and multi-cluster single sign-on, assembled piece by piece. If you want the **whole Agent Platform** (the gateway plus agentgateway, the agent runtime, and the developer portal), install it with one Helm chart instead: [Install the Agent Platform on your own cluster]({{< relref "/tutorials/agent-platform/install-standalone" >}}).

If you run Muster yourself, these guides take you from an empty cluster to a single-sign-on-protected endpoint that an entire fleet can reach.

## In this section

- [Deploy Muster]({{< relref "/tutorials/agent-platform/self-hosting/deploy-muster" >}}): install the CRD and application Helm charts and run the aggregator in custom-resource discovery mode.
- [Set up OAuth]({{< relref "/tutorials/agent-platform/self-hosting/oauth-setup" >}}): protect the endpoint with Dex and configure the proxy that authenticates to downstream servers.
- [Multi-cluster token exchange]({{< relref "/tutorials/agent-platform/self-hosting/multi-mc-token-exchange" >}}): bridge single sign-on to remote management clusters with RFC 8693.
