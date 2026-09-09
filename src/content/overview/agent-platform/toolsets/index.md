---
title: Toolsets and presets
diataxis_content_type: explanation
linkTitle: Toolsets
description: How an agent on the Agent Platform declares its toolset, how Muster resolves it on every request, what presets are, and why a toolset is composition rather than authorization.
weight: 35
menu:
  principal:
    parent: overview-agent-platform
    identifier: overview-agent-platform-toolsets
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-08
user_questions:
  - What is an agent's toolset?
  - What are toolset presets?
  - Why does my agent see only some of the gateway's tools?
  - What does implicit full access mean?
  - Does a toolset replace RBAC?
---

Every agent on the platform reaches its tools through Muster, and Muster's catalog is big. It holds every registered MCP server's tools, every workflow, and Muster's own core tools—hundreds on a busy installation. Until an agent says otherwise, its model can discover and call everything in it. A **toolset** is how an agent says otherwise. It's a short list of selectors, declared on the agent's own release, that names which of the gateway's tools the agent is composed with.

Trust in an agent starts with knowing exactly what it can do. The toolset makes that a visible, reviewable property of the agent itself—not something buried in a runtime, and not something you have to infer from a chat transcript.

## The vocabulary

- **Toolset**: the selector list an agent declares. It's the agent chart's `toolset` value, it travels to Muster as the `X-Muster-Toolset` request header, and it's the `toolset` argument of agent-manager's `create_agent`. It bounds which of the gateway's tools the agent's [meta-tools]({{< relref "/overview/agent-platform/meta-tools" >}}) can see and call.
- **Selector**: one entry of a toolset, written as `preset:<name>`, `server:<name>`, `workflow:<name>`, or `tool:<name>`, each with an exact name. `toolset:<name>` is reserved for shared toolsets in a later release.
- **Preset** (toolset preset): a named selection in Muster's configuration (`toolsetPresets`), referenced as `preset:<name>`. Three are built in (`read-only`, `none`, `full`), two ship with the platform charts (`infrastructure`, `agent-platform`), and an installation adds its own.
- **Resolved tools**: the concrete tools a toolset selects right now for a given caller—the toolset intersected with the caller's own catalog. It's what `filter_tools` returns for a toolset, and what the portal shows on the Tools step and the agent page.
- **Implicit full access**: the label for an agent whose release carries no `toolset` and therefore sends no header. That's how every agent behaved before toolsets existed, made visible.
- **Tool group**: the platform's grouping of MCP servers into *Infrastructure*, *Agent Platform*, and *Registered servers*, plus *Workflows* on the Tools step. See the [three groups]({{< relref "/overview/agent-platform/introduction" >}}#three-groups-of-mcp-servers) in the introduction.

## How a toolset travels

1. The agent's release declares it: the agent chart's top-level `toolset` value, a list of selectors.
2. The chart renders the selectors, joined by commas, as a static request header on the agent's Muster tool entry. The agent runtime sends that header on every request to Muster.
3. Muster reads the header on **every request** and applies the toolset, without keeping any state, as the third filter on the caller's catalog—after the two filters it already applies: which servers the caller has signed in to, and which workflows are available. `list_tools`, `filter_tools`, `describe_tool`, `list_core_tools`, and the resource and prompt tools answer within the toolset. Muster refuses `call_tool` of a tool outside the toolset with an error that names the toolset.

Why per request, and not per session: Muster derives its session for a forwarded token from the token itself, so every agent one person drives shares one session. Evaluating the header per request is what keeps agent A's toolset from applying to agent B. It also means a request *without* the header behaves exactly as before, so IDEs, the CLI, and the portal's own session keep working unchanged.

The meta-tool surface itself doesn't change. What changes is what the meta-tools can see for that request.

## Presets are rules, not lists

A preset is Muster configuration—shipped as chart values through GitOps, reviewed like any other platform change. Inside a preset the selection is rule-based: exact tool names, name patterns, whole servers, workflows, the read-only annotation predicate, labels on `MCPServer` resources, other presets, and an exclude list. Muster evaluates those rules against the live catalog on each request, so a preset stays correct when a server adds tools or a new server joins the platform.

| Preset | What it resolves to |
|---|---|
| `read-only` (built in) | Every tool its server annotates as read-only, plus every workflow whose steps only call read-only tools |
| `none` (built in) | Nothing—the choice for a chat-only agent |
| `full` (built in) | The whole catalog, core tools included: the behavior before toolsets existed, chosen on purpose |
| `infrastructure` (platform charts) | Every server in the *Infrastructure* group: the `mcp-kubernetes`, `mcp-capi`, and `mcp-prometheus` families serving Giant Swarm installations' management clusters |
| `agent-platform` (platform charts) | Every server in the *Agent Platform* group (`agent-manager`, `model-manager`) plus Muster's `core_*` tools; the preset for an agent that manages the platform |

Inline selectors, by contrast, are exact names only. Patterns, excludes, the read-only predicate, labels, and composition exist inside presets, so a header stays a flat, readable list. A selection too large for a header becomes a preset. Two consequences worth knowing:

- **Workflows are read-only when their steps are.** Muster derives a workflow's read-only hint from the tools its steps reference, so `read-only` includes the pure-query workflows, not only individual tools.
- **Core tools are selected by name or by their annotations.** Muster's `core_*` tools (registering servers, creating workflows, signing in) aren't a server, so `server:` can't name them. An agent gets them through `tool:core_workflow_list` and friends, or through a preset with a `core_*` pattern—which is how `agent-platform` includes them. Since Muster 5.13.0 the core tools carry annotations like every other tool, so `read-only` includes the ones that only read. `core_auth_login` is one of them: signing in to an SSO-protected server issues a link for the person and changes nothing on the platform, so a read-only agent can still connect servers as the person asking.

How to define presets for your installation is covered in [Define toolset presets]({{< relref "/tutorials/agent-platform/toolset-presets" >}}).

## No tools, and how failures behave

- **`preset:none` as the whole toolset** means the agent chart renders no Muster tool entry at all. The model sees no meta-tools, pays no context for them, and can't waste turns listing an empty catalog. The portal labels such an agent *No tools*.
- **An empty toolset is an error**, not "no tools" and not "everything": the chart refuses to render and agent-manager refuses the request, both pointing at `preset:none`. An empty list could otherwise send no header and mean full access, the one trap the design rules out.
- **A selector that matches nothing yields nothing.** A server the caller hasn't signed in to, a renamed tool, a workflow that doesn't exist here: each simply contributes no tool. The failure mode is closed. `filter_tools` reports such selectors as unmatched, and the portal marks them.
- **An unknown preset is an error on every meta-tool call**, naming the preset and the presets Muster knows. Never a silent fall-back to the full catalog, and never silent degradation to the selectors that did parse. The agent page shows the same error, so remove a preset from your values only when no agent names it.

## Composition, not authorization

A toolset controls which tools the *model* can discover and call through requests that carry it. That's the blast-radius control an agent's creator and a reviewer can reason about: a default tool set for the agent, visible to everyone.

What authorizes a call hasn't moved. The invoking person's identity is forwarded unchanged, and each backend's own authorization—Kubernetes RBAC for `mcp-kubernetes`, tenancy for Prometheus, a third-party service's own accounts—decides what happens. A toolset can never exceed the invoking person's access, because tools the person can't see aren't in the catalog: an agent is always bounded by *its toolset ∩ the invoking person's own access*. Read the [security model]({{< relref "/overview/agent-platform/security" >}}) for how that access is derived.

The toolset is *declared* by the request. Muster can't yet tell which agent is calling, because the only credential on the agent path is the human's token. A client that sends no header therefore reaches whatever the person behind it may reach—exactly what it could reach before toolsets existed. A toolset bounds the model, not the pod. When the platform adopts an agent identity Muster can trust, Muster will resolve the toolset from that identity instead of the header. Presets, the picker, and the agent page carry over unchanged.

Changing a toolset means changing the agent's release, through the portal's deploy path or agent-manager. That happens with your own identity, under Kubernetes RBAC in the agent's namespace, and is recorded in the API server's audit log. Presets change through GitOps on Muster's values. There's no second policy system.

## Where you meet toolsets

- **Creating an agent in the portal.** The creation wizard has a **Tools** step that opens with nothing selected—which means no tools—and leads with the presets; see [Create and deploy an agent]({{< relref "/tutorials/agent-platform/create-an-agent" >}}#step-3-compose-the-toolset).
- **Reviewing an agent.** The agent page's **Toolset** card shows the declaration, what it resolves to for you, and the *Implicit full access*, *No tools*, and *Full gateway access* labels; see the [portal section]({{< relref "/overview/developer-portal/agent-platform" >}}#what-an-agent-can-use).
- **Through agent-manager.** `create_agent` requires a `toolset`, `update_agent` replaces it, and `get_agent` and `list_agents` report it—or `implicitFullAccess: true` for a release without one. That's how the platform's meta agent gives every agent it creates a toolset, and how agents that predate toolsets get one.
- **In the agent chart and on the cluster.** The `toolset` value on the release, and the `X-Muster-Toolset` header on the rendered `Agent` resource, are the same declaration `kubectl` reads back.
- **From any MCP client.** The header is plain HTTP: a client that lets you set request headers can send a toolset too. See [Define toolset presets]({{< relref "/tutorials/agent-platform/toolset-presets" >}}#send-a-toolset-from-your-own-mcp-client).

The complete grammar, the preset rule shapes, the error texts, and the chart and agent-manager contracts are in the [toolsets reference]({{< relref "/reference/muster/toolsets" >}}).
