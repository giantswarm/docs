---
title: AI chat in the developer portal
linkTitle: AI chat
description: Ask plain-language questions about your clusters and platform directly in the developer portal, answered by an AI assistant powered by Muster.
weight: 40
mermaid: true
menu:
  principal:
    parent: overview-developer-portal
    identifier: overview-developer-portal-ai-chat
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - What is the developer portal AI chat?
  - Can I ask questions about my clusters in the portal?
  - How does the portal chat answer questions?
---

The developer portal includes a built-in AI chat. You ask a question in plain language and get an answer grounded in live platform state, without leaving the portal or switching to a terminal. It's the same assistant experience you'd configure in your [IDE]({{< relref "/getting-started/ai-agent-setup" >}}), but already wired up and waiting in the browser.

Behind the chat is **Muster**, the platform's MCP gateway. The portal connects to your central Muster instance, so the assistant can reach your whole fleet through one secure, authenticated endpoint. For the concepts behind that gateway, see [AI agents on the platform]({{< relref "/overview/ai-agents" >}}).

## What you can ask

The chat answers questions about your clusters and about the portal and platform itself. A few examples:

- `check the pods in <management-cluster>`
- `is <workload-cluster> on <management-cluster> healthy?`
- `why is <app> failing?`
- `what's driving memory usage on <management-cluster>?`
- `what applications are available for deployment?`
- `what can I do here in the portal?`

For cluster questions, the assistant turns your request into live tool calls against the relevant cluster, reads the results, and replies with a focused answer rather than a raw resource dump. For platform and portal questions, it answers from the portal's own context without touching any cluster.

A focused question costs less and answers faster than a broad one. Asking about a specific cluster, app, or symptom lets the assistant go straight to the relevant data. An open-ended "what's broken everywhere?" makes it cast a much wider net.

## How it works

{{< mermaid >}}
flowchart LR
  chat["Portal AI chat"]
  muster["Central Muster"]
  k8sA["mcp-kubernetes<br/>(cluster A)"]
  promA["mcp-prometheus<br/>(cluster A)"]
  k8sB["mcp-kubernetes<br/>(cluster B)"]
  promB["mcp-prometheus<br/>(cluster B)"]

  chat -- "one connection, your identity" --> muster
  muster --> k8sA
  muster --> promA
  muster --> k8sB
  muster --> promB
{{< /mermaid >}}

The chat connects to the central Muster aggregator over its OAuth-protected endpoint. On each management cluster Muster aggregates both `mcp-kubernetes`, which exposes Kubernetes resources, and `mcp-prometheus`, which exposes metrics. So the assistant reaches your entire fleet through a single connection instead of a separate one per cluster and per system. The [architecture page]({{< relref "/overview/ai-agents/architecture" >}}) covers this fleet-wide aggregation in detail.

To keep responses fast and cheap, Muster doesn't load every cluster tool into the assistant at once. It exposes a small set of [meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}) that the assistant uses to discover and call only the tools a given question needs. Common investigations, such as summarizing pod health, can be packaged as single workflow calls that resolve a question in one step.

## Per-user access and security

The chat acts as you, not as a shared service account. It uses your portal sign-on to authenticate to Muster, and you only see and reach the clusters your identity is allowed to.

- **Per-user visibility**: you only see tools from the clusters you've authenticated with and that your identity provider grants you access to. Clusters you can't reach simply don't appear.
- **Cluster RBAC still applies**: a request you aren't permitted to make is rejected by the cluster's own Kubernetes RBAC, not allowed by the gateway.

The [AI agent security page]({{< relref "/overview/ai-agents/security" >}}) explains the OAuth flow, per-user tool visibility, and single sign-on across clusters.

## Current limitations

- **Cluster access is read-only.** The Kubernetes access behind the chat runs in a non-destructive mode: the assistant can inspect resources, logs, and events, but it can't create, change, or delete them. It answers questions and helps you investigate; cluster changes still go through your GitOps workflow.
- **Answers reflect live state at the moment you ask.** The assistant reasons over the data returned by each tool call. Cluster conditions can change between questions, so treat a health answer as a point-in-time snapshot.
- **Quality depends on how the question is scoped.** Specific, well-scoped questions get the best answers; very broad questions take longer, cost more, and can return less precise results.

To use the same assistant from your editor instead of the browser, follow [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
