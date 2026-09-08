---
title: Define toolset presets
diataxis_content_type: how-to-guide
linkTitle: Toolset presets
description: Ship named toolset presets as Muster configuration through your platform values, add installation-specific presets by server, label, or composition, and verify what they resolve to.
weight: 25
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-toolset-presets
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-07
user_questions:
  - How do I add a toolset preset to my installation?
  - Where are the infrastructure and agent-platform presets defined?
  - How do I give an agent only the tools of my test clusters?
  - How do I send a toolset from my own MCP client?
---

A [toolset]({{< relref "/overview/agent-platform/toolsets" >}}) names what an agent is composed with, and a **preset** is a named selection an agent refers to as `preset:<name>`. Presets are Muster configuration, so they ship through the same GitOps path as the rest of your platform values and are reviewed like any other change. This guide shows where they live, which ones you already have, how to add your own, and how to check what a preset resolves to. It's for platform teams. Agent authors pick presets in the portal's [Tools step]({{< relref "/tutorials/agent-platform/create-an-agent" >}}#step-3-compose-the-toolset).

## Where presets live

Muster reads presets from `toolsetPresets` in its configuration, which the Muster chart renders from its `muster.toolsetPresets` value. The `agent-platform` chart forwards its `muster:` block to the Muster release, so on the platform—run for you by Giant Swarm or [installed on your own cluster]({{< relref "/tutorials/agent-platform/install" >}})—the key is **`muster.muster.toolsetPresets`**—the first `muster` is the component block, the second is the Muster chart's own key. If you [run Muster's chart directly]({{< relref "/tutorials/agent-platform/self-hosting/deploy-muster" >}}), drop the outer level.

Presets that select by label need Muster 5.12.0 or later. An older Muster refuses to start on a `label:` rule, and the fleet meta-package pins that floor for you.

## The presets you already have

Three presets are built into Muster and can't be redefined: `read-only`, `none`, and `full`. A `toolsetPresets` entry with one of those names makes Muster refuse to start, naming the preset. The fleet meta-package fails the render first, so the mistake never reaches a cluster.

Two more ship with the platform charts. Both select by the tool-group label every platform-shipped `MCPServer` resource carries (see [Read a server's group from its label]({{< relref "/tutorials/agent-platform/managing-mcp-servers" >}}#read-a-servers-group-from-its-label)). A new manager or a fourth infrastructure family therefore joins its preset with no values change. As shipped by the fleet meta-package:

```yaml
muster:
  muster:
    toolsetPresets:
      infrastructure:
        description: The servers for the infrastructure underneath the platform (Giant Swarm installations' management clusters) — mcp-kubernetes, mcp-capi, mcp-prometheus.
        include:
          - label: agent-platform.giantswarm.io/tool-group=infrastructure
      agent-platform:
        description: The platform's own management surface — agent-manager, model-manager, cluster-manager and muster's core tools.
        include:
          - label: agent-platform.giantswarm.io/tool-group=agent-platform
          - pattern: core_*
```

The `core_*` pattern is what makes `agent-platform` the preset for an agent that manages the platform: no other shipped preset except `full` reaches Muster's core tools. A server registered through the portal carries no label and belongs to neither preset—select it by name.

An [installation on your own cluster]({{< relref "/tutorials/agent-platform/install" >}}) gets both presets with the same chart, which also pins the Muster floor they need. Don't add them by hand on an older platform release: a Muster older than 5.12.0 refuses to start on a preset with a `label:` rule.

## Add your own presets

Add entries next to the shipped ones. Helm merges the map, so the platform presets stay and yours join them. `preset:<name>` is then valid for every agent on the installation, and the portal's Tools step lists it with its description. Each preset has a `description`, an `include` list, and an optional `exclude` list. Every rule sets exactly one key:

| Rule | Selects |
|---|---|
| `tool: <name>` | One tool by its exposed name (`x_<server>_<tool>`, `workflow_<name>`, `core_*`) |
| `pattern: <glob>` | Every tool whose exposed name matches the glob, for example `x_mcp-kubernetes_*` |
| `server: <name>` | Every tool of that `MCPServer` resource—the family name or a member's name for a [family]({{< relref "/tutorials/agent-platform/managing-mcp-servers" >}}#group-equivalent-servers-with-family) |
| `workflow: <name>` | The workflow's `workflow_<name>` tool |
| `readOnly: true` | Every tool annotated read-only, including workflows whose steps only call read-only tools |
| `label: <key>=<value>` or `label: <key>` | Every tool of every `MCPServer` resource carrying that label, read live on each request |
| `preset: <name>` | Everything another preset selects—composition, in `include` only |

A preset resolves to the union of its includes minus its excludes. The exclude list takes the same shapes except `preset`.

### By server name

A preset for the servers of two test management clusters, without deletes:

```yaml
muster:
  muster:
    toolsetPresets:
      test-clusters:
        description: The kubernetes and prometheus servers of the test management clusters, without deletes
        include:
          - server: test-01-mcp-kubernetes
          - server: test-02-mcp-kubernetes
          - server: test-01-mcp-prometheus
          - server: test-02-mcp-prometheus
        exclude:
          - pattern: "*_delete"
```

### By a label you stamp yourself

Label the `MCPServer` resources instead, and the preset follows the label as servers come and go. For a resource you manage in Git, add the label under `metadata.labels`. The agent-manager and model-manager charts expose their resource's labels as the `muster.mcpServer.labels` value. The fleet's per-cluster infrastructure servers already carry the tool-group label, which is what the shipped presets select by.

```yaml
muster:
  muster:
    toolsetPresets:
      test-clusters:
        description: Every server labelled for the test pipeline
        include:
          - label: example.com/pipeline=testing
```

### By composition

Everything the `infrastructure` preset selects, plus one workflow, without deletes:

```yaml
muster:
  muster:
    toolsetPresets:
      infra-triage:
        description: Every infrastructure tool plus the incident-triage workflow, without deletes
        include:
          - preset: infrastructure
          - workflow: incident-triage
        exclude:
          - pattern: "*_delete"
```

The `include` list is a union. `preset: infrastructure` next to `readOnly: true` selects every infrastructure tool *and* every read-only tool anywhere, not the read-only subset of the infrastructure. Narrow a preset with `exclude` rules instead.

## Rules of the road

- **Never name a preset `read-only`, `none`, or `full`.** Muster refuses to start on it.
- **A preset that matches nothing isn't an error.** An agent using it simply has no tool from it, and `filter_tools` reports the selector as unmatched. On an installation whose servers don't carry the tool-group label yet, `preset:infrastructure` resolves to nothing until the label arrives.
- **Remove a preset only when no agent names it.** An agent whose toolset names a preset that no longer exists gets an error on every meta-tool call, and its agent page shows the same error. `list_agents` in agent-manager reports every agent's toolset, so you can find the ones that reference it first.
- **Muster validates presets at startup.** A rule with no key or more than one, a pattern that doesn't compile, `readOnly: false`, a composition naming an unknown preset, or a cycle stops Muster with an error naming the preset and the rule position—so a broken preset never serves a partial catalog.

## Roll out and verify

Commit the values through your GitOps pipeline. The configuration change rolls the Muster pod once. Then, with an [authenticated CLI context]({{< relref "/reference/muster/cli/auth" >}}), ask Muster what a preset resolves to for you:

```bash
muster call filter_tools --json '{"include_presets": true, "toolset": ["preset:test-clusters"]}'
```

The response carries three things. `presets` lists the built-ins first, then the shipped and installation presets with their descriptions. `tools` holds the tools the toolset resolves to for the caller. `toolset_unmatched` names the selectors that selected nothing. A server you haven't signed in to contributes nothing to the result, which is what an agent driven by you would see too. Sign in with `muster auth login` and call again.

## Send a toolset from your own MCP client

An agent on the platform gets its header from the agent chart. Any other MCP client can send the same header by hand: put `X-Muster-Toolset` on the requests to the gateway with a comma-separated list of selectors, for example `preset:read-only, workflow:incident-triage`. Most clients that connect to remote MCP servers let you set request headers in their server configuration.

Muster reads the header on every request and answers every meta-tool call within it. A request without the header sees the catalog as before. A header that's empty, names an unknown preset, uses the reserved `toolset:` prefix, or exceeds 32 selectors gets an error result on every meta-tool call rather than a silent fall-back. See the [toolsets reference]({{< relref "/reference/muster/toolsets" >}}) for the exact grammar and texts.

## Related

- [Toolsets and presets]({{< relref "/overview/agent-platform/toolsets" >}}): the concept, and why a toolset is composition rather than authorization.
- [Toolsets reference]({{< relref "/reference/muster/toolsets" >}}): selector grammar, rule shapes, built-in and platform presets, the chart value, and agent-manager's argument.
- [Manage MCP servers]({{< relref "/tutorials/agent-platform/managing-mcp-servers" >}}): the `MCPServer` resources and labels the presets select over.
- [Create and deploy an agent]({{< relref "/tutorials/agent-platform/create-an-agent" >}}): where agent authors pick from the presets you define.
