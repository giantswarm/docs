---
title: Troubleshoot AI agent access
linkTitle: Troubleshooting
description: Work through the common Muster failure modes for platform teams, from authentication loops and disconnected clusters to missing tools and workflows agents can't find.
weight: 60
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-troubleshooting
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - Why does my AI agent keep asking me to authenticate?
  - Why are tools missing from my agent?
  - Why doesn't my agent find the workflow I wrote?
  - Why does a cluster show as disconnected?
---

This guide covers the failure modes platform teams hit when operating Muster. For the basic IDE setup checks—context, login, editor configuration—start with the [AI agent setup troubleshooting]({{< relref "/getting-started/ai-agent-setup" >}}#troubleshooting) section first.

## The agent keeps asking to authenticate

If the `authenticate_muster` tool keeps reappearing, or your assistant loops on login, the session has expired or the token can't be refreshed.

- Run `muster auth login` in a terminal, then restart the MCP server in your IDE.
- Check `muster auth status`. If the aggregator shows as authenticated but a downstream server shows `Auth Required`, that server needs its own login or its single sign-on is set up incorrectly.
- For a forwarding server, confirm the downstream trusts Muster's client and the `requiredAudiences` match what the server expects. A token without the right audience is rejected, which looks like an endless re-auth.

## A cluster shows as disconnected

In `muster auth status`, a single cluster reporting `Disconnected` or `Failed` while others are fine usually means that cluster's `mcp-kubernetes` is unreachable, not a Muster problem.

- Check the [`MCPServer`]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}) state: `kubectl get mcpservers -n muster`. A `Failed` state means the endpoint is unreachable. Verify the URL, DNS, and any network policy between Muster and that cluster.
- `Auth Required` isn't a failure: it's the normal state for a protected server until a user logs in.
- Other clusters keep working independently, so users can still operate the rest of the fleet while you fix the one.

## Tools are missing from the agent

If expected tools don't appear in the agent's discovery results:

1. Confirm the user is authenticated to the server those tools come from. Per-user visibility means a server a user hasn't authenticated with contributes no tools to **their** list, even though it's healthy.
2. Check the server's state is `Connected` or `Running` and that `autoStart` is set if it should always be available.
3. Remember discovery is dynamic—no IDE restart is needed. If a server only just started, the agent's next `list_tools` or `filter_tools` call reflects it.

## A workflow runs manually but the agent never uses it

This is the most common workflow-authoring trap, and it's about discoverability, not correctness. The workflow is live: `kubectl get workflow` shows it valid, and you can call it by name. But the agent falls back to raw tools.

The cause is almost always the description. An agent finds a workflow through `filter_tools`, whose description filter is a **case-insensitive substring match** over `spec.description`. If the agent searches for `pod health` and the description only says `check the pods in <mc>`, there's no substring match, and the workflow is invisible to that search.

Fix it by leading `spec.description` with both the topic keyword and the natural phrasing. See [authoring workflows]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}#the-description-also-controls-discoverability) for the full rule.

A related symptom: an agent told to "discover workflows" with a broad glob can pull every workflow's description into context at once, spiking token cost. Steer agents to a **narrow** filter—a specific topic term or name pattern—rather than a catch-all.

## A workflow runs but the agent over-explores

If a workflow returns a clean result and the agent keeps investigating anyway, the description is missing a **stop-when-healthy rule**. Without an explicit rule to write a one-line summary and stop when the result is empty, an agent treats a clean digest as a starting point. Add the rule to `spec.description`. This single change has swung a probe by an order of magnitude in token cost.

## A long chain drops with a network error

A single agent turn that runs many tool calls back to back can drop with a streaming network error before producing an answer—the HTTP response succeeds, but the stream aborts partway. Fewer, cheaper calls reduce this exposure, which is one more reason to encapsulate multi-step investigations as a [workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}) rather than letting the agent run the whole discover-query-correlate loop itself.

## Authentication fails for users in many groups

If a user can authenticate from one account but fails from one that belongs to many identity-provider groups, suspect token size limits: ingress header buffers and the group-count limit. See [RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}#large-tokens).

## Related

- [Author a workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}): discoverability and stop-when-healthy rules.
- [Manage MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}): server states and `autoStart`.
- [Security model]({{< relref "/overview/ai-agents/security" >}}): per-user visibility and sign-out operations.
