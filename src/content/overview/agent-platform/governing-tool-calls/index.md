---
title: Governing tool calls
linkTitle: Governing tool calls
description: How Allow, Ask and Block settings decide whether a tool call through muster runs, asks a person first, or is hidden, who sets them, what the governance mode adds, and how to configure it with the agent-platform chart.
weight: 50
menu:
  principal:
    parent: overview-agent-platform
    identifier: overview-agent-platform-governing-tool-calls
user_questions:
  - How do I make an agent ask before it changes something?
  - What do Allow, Ask and Block mean for a tool?
  - Who can let an agent run a tool without asking?
  - How do I turn on governed mode and protect it?
  - What is the difference between trusted and governed?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
diataxis_content_type: explanation
last_review_date: 2026-11-25
---

Every tool behind muster, the Agent Platform's tool gateway, has one of three settings. muster decides
and enforces it on every call, so it holds the same in the Dev Portal, Slack, Claude Code, a coding
agent's sandbox and any other client.

## Three settings, strictest wins

| Setting | What happens |
|---|---|
| **Allow** | The tool runs. |
| **Ask** | A person confirms the exact call first. |
| **Block** | The tool is hidden and can't be used. |

A connector's admins set them for the connector, and an agent's builder sets them for the agent's
tools. The stricter of the two holds. One exception: a connector admin can let one agent run a tool
the connector would ask for.

## Who sets what

- **Connector admins**, per connector: a **rule** (Allow, Ask or Block) that new tools follow, so a
  Block rule hides every tool nobody has reviewed yet, and a setting per tool. A connector admin is
  whoever may edit that connector: on the platform, the `connector-admin` role in its namespace.
- **Agent builders**, per agent: the agent's tool list, each entry optionally Allow, Ask or Block, and
  a `default` for every listed tool. These settings apply to everyone who uses the agent.
- **Exceptions**: only a connector admin can give an agent Allow on a tool their connector asks for,
  with `set_agent_approval`. Saving an agent drops every exception the saver isn't connector admin
  for; the tool asks again until it is granted again.
- **A person using a tool directly** — the portal's *Run*, their own client — gets the connector's
  settings only.

A connector without settings runs every tool and is shown as *not reviewed*; upgrading changes
nothing for connectors and agents nobody has reviewed.

## When a call asks

- The client shows a link to muster's approval page. It says in plain words what the tool does, with
  the exact arguments one click away. Only the person whose call it is can decide.
- An approved call runs exactly once, when the same client runs it again (any MCP session of that
  client will do); another client of the same person asks anew. A declined call returns to the agent
  as declined.
- A change shows what changes, old to new. A workflow asks once, up front, for all its steps.
- A client that can't show the prompt gets the link as text: decide on the page, then run the tool
  again.
- An agent running with nobody to open the link runs only what is Allow; the rest expires.
- At most 3 calls of one client, and 10 of one person, wait for a decision at a time.

## Trusted and governed

The platform's **governance mode** adds asking for agent callers. It never changes what a setting
means, and it never asks a person using a tool directly.

| | Trusted (default) | Governed |
|---|---|---|
| An agent runs a read on the platform's own servers (listing agents, sessions, clusters, VMs, models) | the connector's setting | the connector's setting |
| An agent runs anything else on the platform's own servers: creates, changes, starts or deletes an agent or session, a VM, cluster, model, workspace or toolchain, writes to Kubernetes, or a tool added later | the connector's setting | asks |
| An agent pauses, deletes, starts or stops a connector | runs | asks |

On governed, only the reads on each platform server's safe list (`governedServers`, shipped with the
chart) run unasked, so a new or renamed tool asks until someone lists it. A governed ask can't be
lifted for one agent.

In both modes an agent always asks before it adds or repoints a connector, changes the approval
settings of a connector or an agent, gives an agent an exception, creates, changes or deletes a
workflow, grants or changes access (organization members, an organization's connectors, models,
egress or credentials), adds a model backend, approves an action or a toolchain source, or changes
muster's configuration. Changing muster's configuration asks every caller.

Clients read the mode from muster (`governance` on `filter_tools`). An agent can propose a change of
mode, never approve it.

## Set the mode and the governed servers

The mode is the agent-platform chart value `governance.mode` (`trusted` or `governed`).
`governedServers` names each governed server with its `role` (which floors hold on it) and its
`safe` list (tools agents call unasked on governed). The chart ships an entry per server it
installs; override a `safe` list per key or add an entry for a server you register yourself.

```yaml
governance:
  mode: governed
governedServers:
  agent-manager:
    safe: [get_info, list_agents, get_agent]
```

- muster reads the mode once, at start: change the value and let the release roll muster.
- A safe list holds reads only; muster refuses to start when one names a floor.
- `governed` is refused until the chart's release floors are set, so a chart or muster too old for
  tool approval fails the render instead of asking nothing.

### Floors for your own servers

A floor is a tool that asks agents in both modes, whatever the connector's setting says. muster
ships floors for the platform's components, grouped by role. For a server you register yourself,
declare a role under `governance.roleFloors` and point the server at it:

```yaml
governance:
  roleFloors:
    exampleManager: [approve_change, merge_change]
governedServers:
  example-manager:
    role: exampleManager
    safe: [get_info, list_changes]
```

Configured floors are added to the built-in ones for the same role; they never remove or narrow a
built-in floor. A `role` named nowhere fails the start.

### Protect the values repository

Whoever can change these values can switch the mode or shorten a safe list, and nobody else approves
it on the platform. The values repository is the control: require pull request reviews and branch
protection, and trust those who may merge like the platform's admins.

## Presets

Creating a connector starts from a preset, written out as one setting per tool you see before saving:

| Preset | Settings |
|---|---|
| **Recommended** | Read-only tools run. The rest ask. New tools ask. |
| **Allow all** | Everything runs. |
| **Ask all** | Everything asks. |

Creating a connector over MCP requires a preset or explicit settings. The wizard pre-selects *Allow
all* on a trusted platform and *Recommended* on a governed one. Tool annotations only fill in a
preset; they decide nothing later.

The platform's own connectors arrive with explicit settings: its managers and kagent's session tools
on *Allow all*, the infrastructure servers (Kubernetes, Prometheus, Cluster API) on *Recommended*.

## Where to configure

| Where | What |
|---|---|
| Dev Portal | *Connectors* → connector → *Tools*; the connector wizard's *Test & Tools* step; an agent's *Tools* step |
| GitOps | `MCPServer` `spec.approval` (`rule`, `tools`); the agent chart's `tools` and `default`; agent-platform's `governance.mode`, `governedServers` (each server's role and safe list), `governance.roleFloors` (floors for roles you declare) and the `connector-admin` role (`muster.rbac.mcpServerEditor.subjects`, `tenants.platformTeam`); a shipped connector's chart value (`<component>.muster.mcpServer.approval`, `mcp-kubernetes.mcpServer.approval`, `kagent.controllerRoute.mcp.approval`, agent-platform-mcps' `muster.families.<group>.approval`) |
| MCP | `core_mcpserver_create` (with `preset` or `approval`), `core_mcpserver_set_approval` (with `expectedGeneration` from `core_mcpserver_get`, so concurrent saves conflict instead of overwriting); agent-manager's `create_agent`, `update_agent_access`, `set_agent_approval` |

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: github
spec:
  # ...
  approval:
    rule: Ask                    # new tools ask (Block: new tools are hidden)
    tools:
      get_issue: Allow
      create_issue_comment: Ask
      delete_repository: Block
```

## Prerequisites

Asking needs muster's shared store (Valkey), muster's own OAuth server for the browser sign-in
(behind Dex) and a public URL on its origin (`muster.muster.oauth.mcpClient.publicUrl`). The
platform chart ships Valkey storage and the OAuth server; point the latter at your identity
provider. Without a prerequisite every call that would ask is refused with the reason
(`approval.unavailable`). muster returns the browser after a decision only to URLs in
`muster.muster.oauth.mcpClient.postLoginRedirectAllowlist`; the platform chart derives them
(portal port from `backstage.publicPort` when not 443) and sets `muster.approval.installation` from
`backstage.installationName`. muster refuses every connector's tools while the `MCPServer` CRD
lacks `spec.approval`. An air-gapped installation needs an identity provider on site behind Dex.

Resources and prompts are not governed; they are reads.

## Upgrading

- Move muster and the platform chart together; `governed` on a muster too old for it fails the
  platform chart's render.
- A connector applied while the old `MCPServer` CRD was served lost its `spec.approval`; reconcile
  its release again after muster's upgrade (`flux reconcile helmrelease <name> --force`).
- Connector editing is no longer open to everyone: name the groups in
  `muster.rbac.mcpServerEditor.subjects` and `tenants.platformTeam`. An upgrade that would remove the
  old everyone-binding without naming anyone fails until you do or allow the removal.
- An edge on another port than 443 sets `backstage.publicPort` so the portal's return is admitted.

## Giant Swarm-managed installations

On an installation Giant Swarm manages, Giant Swarm switches the governance mode for you.
