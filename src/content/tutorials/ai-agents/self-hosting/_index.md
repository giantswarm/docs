---
title: Self-hosting Muster
linkTitle: Self-hosting
description: Operate your own Muster aggregator. Deploy the Helm charts, protect the endpoint with OAuth and Dex, and bridge single sign-on across multiple management clusters.
weight: 70
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-self-hosting
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-21
user_questions:
  - How do I deploy and run my own Muster?
  - How do I protect a self-hosted Muster with OAuth?
  - How do I host Muster across multiple management clusters?
---

{{% notice note %}}
**Applies to self-hosted Muster only.** These guides are for teams who operate their own Muster aggregator. On the managed Giant Swarm platform, Muster is deployed and protected for you, so you can skip this section and go straight to the operational guides such as [managing MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}) and [authoring workflows]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}).
{{% /notice %}}

If you run Muster yourself, these guides take you from an empty cluster to a single-sign-on-protected endpoint that an entire fleet can reach.

## In this section

- [Deploy Muster]({{< relref "/tutorials/ai-agents/self-hosting/deploy-muster" >}}): install the CRD and application Helm charts and run the aggregator in custom-resource discovery mode.
- [Set up OAuth]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}): protect the endpoint with Dex and configure the proxy that authenticates to downstream servers.
- [Multi-cluster token exchange]({{< relref "/tutorials/ai-agents/self-hosting/multi-mc-token-exchange" >}}): bridge single sign-on to remote management clusters with RFC 8693.
