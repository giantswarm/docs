---
linkTitle: Toolsets
title: Muster toolsets reference
diataxis_content_type: reference
description: Reference for toolset selectors, the X-Muster-Toolset header, the toolsetPresets configuration, built-in and platform presets, the agent chart's toolset value, and agent-manager's toolset argument.
weight: 25
menu:
  principal:
    parent: reference-muster
    identifier: reference-muster-toolsets
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - What selectors can a toolset contain?
  - How do I write a toolsetPresets rule?
  - Which presets are built into Muster?
  - How does the agent chart render a toolset?
  - What does agent-manager require for toolset?
last_review_date: 2026-09-07
---

A **toolset** is the selector list an agent declares to say which of the gateway's tools it's composed with. Muster evaluates it per request as the third filter on the caller's catalog. For the concept, see [Toolsets and presets]({{< relref "/overview/agent-platform/toolsets" >}}); for defining presets on your installation, see [Define toolset presets]({{< relref "/tutorials/agent-platform/toolset-presets" >}}). This page is the field-level reference, verified against Muster `5.12.0`, the Generic agent chart `0.6.0`, agent-manager `0.4.0`, and the fleet meta-package `agent-platform` `3.11.0`.

## Inline selectors {#selectors}

A toolset, wherever it's declared inline (header, chart value, agent-manager argument, `filter_tools` argument), is a list of selectors of these four forms:

| Selector | Selects |
|---|---|
| `preset:<name>` | A preset from `toolsetPresets`, or a built-in one |
| `server:<name>` | Every tool of the `MCPServer` resource `<name>`. For a family, the family name selects the family surface; a member's name selects it too |
| `workflow:<name>` | The workflow's execution tool, `workflow_<name>` |
| `tool:<name>` | One tool by its exposed name: `x_<server>_<tool>`, `workflow_<name>`, or `core_*` |

Names are exact and case-sensitive; a selector matches `^(preset|server|workflow|tool):[^\s,]+$`. At most **32** selectors inline—larger selections are presets. Core tools (`core_*`) aren't a server: select them with `tool:core_workflow_list` inline or a `core_*` pattern in a preset; since Muster 5.13.0 they also carry annotations, so `read-only` includes the read-only ones.

Rejected inline, with an error result naming the toolset and the selector:

| Input | Error |
|---|---|
| Empty header or empty list | `toolset [] is empty; use "preset:none" for an agent without tools` |
| `toolset:<name>` | `… selector "toolset:x" is reserved for shared toolsets` |
| `label:<key>=<value>` | `… selector "label:…" is allowed inside presets only` |
| Anything else | `… selector "…" is malformed; expected preset:<name>, server:<name>, workflow:<name> or tool:<name>` |
| More than 32 selectors | `toolset [...] has 33 selectors, more than the 32 allowed inline; define a preset` |
| Unknown preset | `toolset [preset:foo] names unknown preset "foo"; known presets: read-only, none, full, …` |

These are **error results on every meta-tool call**—`get_resource` and `get_prompt` included—never a silent fall-back to the unscoped catalog and never a silent degradation to the selectors that did parse. They aren't sticky: the next request without the header is unscoped again.

## The `X-Muster-Toolset` header {#header}

```text
X-Muster-Toolset: preset:read-only, workflow:incident-triage
```

A comma-separated list of inline selectors; whitespace around each selector is trimmed. Muster reads the header on **every** request, nothing is bound to the MCP session, and a request without the header is unscoped—exactly the behavior before toolsets existed. Two requests on the same session with different headers get different catalogs.

## Presets configuration {#presets}

Presets are `toolsetPresets` in Muster's `config.yaml`—chart value `muster.toolsetPresets` on the Muster chart, `muster.muster.toolsetPresets` on the fleet meta-package and the standalone chart, which forward their `muster:` block to the Muster release.

```yaml
toolsetPresets:
  <name>:
    description: <string>          # shown by filter_tools with include_presets
    include:                       # rules, exactly one key each
      - tool: <exact exposed name>
      - pattern: <glob on the exposed name>
      - server: <name>
      - workflow: <name>
      - label: <key>=<value>       # or <key>; presets only
      - readOnly: true
      - preset: <name>             # composition, include only
    exclude: []                    # optional; same shapes except preset
```

| Rule | Selects |
|---|---|
| `tool: <name>` | One tool by exposed name |
| `pattern: <glob>` | Tools whose exposed name matches the glob (`core_*`, `x_mcp-kubernetes_*`); Go `path.Match` syntax |
| `server: <name>` | Every tool of that server; family name or member name for families |
| `workflow: <name>` | The workflow's execution tool |
| `readOnly: true` | Every tool annotated `readOnlyHint: true`, including workflows carrying the derived hint |
| `preset: <name>` | Everything another preset selects. `include` only |
| `label: <key>=<value>`, `label: <key>`, `label: <key>=` | Tools of every `MCPServer` resource whose `metadata.labels` carries that label, read live on each request; `<key>` alone matches presence, `<key>=` an empty value. A family tool joins when any member providing it carries the label. Presets only |

A preset resolves to the union of its includes minus its excludes.

### Validation at startup {#presets-validation}

`muster serve` refuses to start when `toolsetPresets` redefines a built-in preset, when a rule sets no key or more than one, when a `pattern` doesn't compile, when `readOnly` is `false`, when `exclude` composes a preset, when a composition names an unknown preset, or when compositions cycle. Every error names the preset and the rule position. The `label:` rule requires Muster `5.12.0`; an older Muster refuses to start on it.

### Workflow read-only derivation {#workflow-readonly}

A workflow is read-only when every tool its steps reference—conditions, `forEach` and `parallel` sub-steps and `onFailure` handlers included, nested workflows followed—resolves in the caller's catalog to a tool annotated read-only. A step calling a core tool that writes (`core_workflow_delete`, `core_service_stop`, …), an unknown tool, or a cycle makes the workflow not read-only; a step calling a read-only core tool (`core_workflow_list`, …) keeps it read-only. The derived hint fills the workflow tool's `readOnlyHint` annotation, so `describe_tool` shows it and `preset:read-only` includes the pure-query workflows.

## Built-in presets {#built-in-presets}

Built into Muster and not redefinable by configuration:

| Preset | Resolves to |
|---|---|
| `read-only` | Every tool annotated `readOnlyHint: true`—Muster's own read-only core tools included since 5.13.0 (`core_*_list`, `core_*_get`, `core_*_validate`, `core_config_get*`, `core_events`, `core_mcpserver_detect`, `core_auth_login`)—plus every workflow whose step tools are all read-only |
| `none` | Nothing. A `preset:none` header hides and refuses every tool; the agent chart omits the Muster tool entry altogether for a toolset that's exactly `["preset:none"]` |
| `full` | The whole catalog, core tools included (`pattern: "*"`) |

## Platform presets {#platform-presets}

Shipped by the fleet meta-package `agent-platform` (`3.11.0` and later) as `muster.muster.toolsetPresets`, selecting by the label `agent-platform.giantswarm.io/tool-group` that every platform-shipped `MCPServer` resource carries:

| Preset | Rules | Resolves to | Label stamped by |
|---|---|---|---|
| `infrastructure` | `label: agent-platform.giantswarm.io/tool-group=infrastructure` | The `mcp-kubernetes`, `mcp-capi`, and `mcp-prometheus` families | `agent-platform-mcps` `0.9.0` and later (`muster.families.<group>.toolGroup`, default `infrastructure`; per-entry `mcpServers[].toolGroup` override); the standalone chart's bundled `mcp-kubernetes` from `0.36.0` |
| `agent-platform` | `label: agent-platform.giantswarm.io/tool-group=agent-platform` + `pattern: core_*` | `agent-manager`, `model-manager`, and Muster's `core_*` tools | `agent-manager` `0.3.0` and later, `model-manager` `0.18.0` and later (`muster.mcpServer.labels` can override) |

The standalone chart `0.37.0` runs Muster `5.12.0`; the two presets follow in a later standalone release and can be added to its values in the meantime (same key).

## What the meta-tools do with a toolset {#meta-tools}

- `list_tools`, `filter_tools`, `describe_tool`, and `list_core_tools` read the filtered catalog. `describe_tool` of a tool the session can see but the toolset excludes answers `tool "<name>" is outside the toolset [<selectors>]`; an unknown name is still `Tool not found`.
- `call_tool`—including workflow execution (`workflow_<name>`)—of a name outside the toolset is refused with `tool "<name>" is outside the toolset [<selectors>]` and logged once at info level with the tool, the toolset, and the session. The tools a workflow's steps call internally are the workflow author's composition and aren't re-checked.
- Resources and prompts follow the servers: a server is inside the toolset when at least one of its tools is selected. `list_resources`, `filter_resources`, `describe_resource`, `list_prompts`, `filter_prompts`, and `describe_prompt` hide the others; `get_resource` and `get_prompt` refuse them (`resource "<uri>" is outside the toolset […]`).
- `list_tools`' `servers_requiring_auth` isn't narrowed: it tells the caller which sign-in would make more of the toolset resolve.
- `tools/list`—the meta-tools themselves—is unchanged.

### `filter_tools` arguments and response {#filter-tools}

`filter_tools` accepts two toolset-related arguments next to its [discovery arguments]({{< relref "/reference/muster/meta-tools" >}}#filter-tools-args):

| Argument | Type | Description |
|---|---|---|
| `toolset` | string[] | Inline selectors to resolve. When the request also carries `X-Muster-Toolset`, the argument resolves **within** the header's toolset and never widens it. Errors use the header's texts |
| `include_presets` | boolean | Return the known presets with their descriptions |

```json
{"name": "filter_tools", "arguments": {"toolset": ["preset:read-only", "server:pro"], "include_presets": true}}
```

Response additions:

| Field | Description |
|---|---|
| `toolset` | The selectors as given, echoed when the argument was set |
| `toolset_unmatched` | The selectors that selected nothing for the caller—for example a server the caller hasn't signed in to. `preset:none` is never reported |
| `presets` | `[{name, description, built_in}]`, built-ins first. Present when `include_presets` or `toolset` was given |

### Tool information {#tool-info}

Every entry of `list_tools` and `filter_tools`, and the `describe_tool` response, carries:

| Field | Description |
|---|---|
| `server` | The owning `MCPServer` resource (the family name for a family tool); omitted for workflows and core tools |
| `kind` | `tool` (served by an `MCPServer`), `workflow`, or `core` |
| `annotations` | The hints the server declared—`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`—or the derived `readOnlyHint` of a workflow; omitted when the tool carries none |

## The Generic agent chart's `toolset` value {#agent-chart}

The [Generic agent chart](https://github.com/giantswarm/agent) (`0.6.0` and later) takes the toolset as a top-level value, a list of selector strings:

```yaml
toolset:
  - preset:read-only
  - workflow:incident-triage
```

| Value | Rendered `Agent` resource |
|---|---|
| Unset (the default) | No header. Byte-identical to the render before toolsets existed: the agent has *implicit full access* |
| One or more selectors | The Muster tool entry gains `headersFrom: [{name: X-Muster-Toolset, value: "<selectors joined by ,>"}]`—kagent's `spec.declarative.tools[].headersFrom`, a sibling of the entry's `mcpServer` reference |
| Exactly `["preset:none"]` | No Muster tool entry at all, and no `tools` key when `extraTools` is empty |
| `[]` | Render fails, pointing at `preset:none` |
| More than 32 selectors | Render fails: define a preset |
| `toolset:<name>`, `label:<key>=<value>`, or a malformed selector | Render fails, naming the selector |

The schema declares `toolset` as `[array, null]` of strings; the cap and the empty-list rule are template checks so they can carry those messages. `muster.toolNames` is a different knob: kagent applies it to Muster's *meta-tools* (`list_tools`, `call_tool`, …), so it never narrows the tools behind the gateway—a toolset is the way to do that.

## agent-manager's `toolset` argument {#agent-manager}

[agent-manager](https://github.com/giantswarm/agent-manager) (`0.4.0` and later) composes the same chart value. Its tools and the REST routes behind them:

| Tool | Route | `toolset` |
|---|---|---|
| `create_agent` | `POST /api/v1/agents` | **Required.** The refusal names the shipped presets—`read-only`, `none`, `infrastructure`, `agent-platform`, `full`—and points at `preset:none` for a chat-only agent and `preset:full` for the deliberate choice of every tool |
| `validate_agent` | `POST /api/v1/agents/validate` | Validated like `create_agent`, without writing |
| `update_agent` | `PATCH /api/v1/agents/{ns}/{name}` | Replaces the whole list. The edit path, and the way agents that predate toolsets get one |
| `get_agent`, `list_agents` | `GET /api/v1/agents…` | Report `toolset` when the release declares one, `implicitFullAccess: true` when it doesn't |

agent-manager validates the inline grammar—non-empty, at most 32 selectors, the four forms, `toolset:` reserved, `label:` refused—and writes the list to the chart's `toolset` value exactly as given. It never resolves a toolset; resolution is Muster's, per caller. The former `toolNames` argument is removed; a caller still passing it gets `toolNames never narrowed anything against muster (kagent filters muster's meta-tools only); declare a toolset instead, e.g. toolset: ["preset:read-only"]`.

## Versions {#versions}

| Component | Version | What it brings |
|---|---|---|
| Muster | `5.11.0` | `X-Muster-Toolset` per request, `toolsetPresets` with the built-ins, `filter_tools` `toolset` and `include_presets`, `server`/`kind`/`annotations` on tool entries, workflow read-only derivation |
| Muster | `5.12.0` | The `label:` preset rule |
| Generic agent chart | `0.6.0` | The `toolset` value |
| agent-manager | `0.4.0` | `toolset` on create (required), validate, update; `toolNames` removed; `implicitFullAccess` on reads |
| Developer portal (Backstage) | `0.239.0` | The Tools step in the agent creation wizard, the `toolset` value in the composed release, the Toolset card on the agent page |
| `agent-platform` meta-package | `3.11.0` | The `infrastructure` and `agent-platform` presets; Muster floored at `5.12.0` |
| `agent-platform-mcps` | `0.9.0` | The tool-group label on the fleet's infrastructure families |
| `model-manager` | `0.18.0` | The tool-group label on its `MCPServer` resource |

## Related

- [Toolsets and presets]({{< relref "/overview/agent-platform/toolsets" >}}) - The concept, and why a toolset is composition rather than authorization.
- [Define toolset presets]({{< relref "/tutorials/agent-platform/toolset-presets" >}}) - Adding an installation's own presets and verifying them.
- [Meta-tools]({{< relref "/reference/muster/meta-tools" >}}) - The full `filter_tools` argument and response reference.
- [`MCPServer`]({{< relref "/reference/platform-api/crd/mcpservers.muster.giantswarm.io.md" >}}) - The resource whose labels the platform presets select over.
