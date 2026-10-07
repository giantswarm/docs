---
title: Enable Agent Platform features in Backstage
diataxis_content_type: how-to-guide
linkTitle: Enable portal features
description: Turn on the Agent Platform section in a Backstage developer portal instance, from making the section appear to letting users create and deploy agents.
weight: 67
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-enable-portal-features
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-10-05
user_questions:
  - How do I enable the Agent Platform section in Backstage?
  - Why does the installation picker show the wrong name?
  - Why don't agent avatars render in the portal?
  - What's needed before agents can be deployed from the portal?
---

The [Agent Platform section]({{< relref "/overview/developer-portal/agent-platform" >}}) ships with the Giant Swarm Backstage plugins but is off by default. Enabling it takes several independent configuration changes—none of them discoverable from the portal itself. This guide walks them in order: first the browse experience, then what deploying agents needs.

All configuration goes into the instance's Backstage app-config.

{{% notice warning %}}
**Inline app-config instances inherit no defaults.** A portal instance configured with its own inline app-config (rather than the shared configuration base) inherits none of the shared defaults—including safety defaults such as the content-security-policy baseline. Every snippet below must be present in the instance's own configuration. Backstage also *replaces* configuration arrays rather than merging them. When you override an array such as the CSP image sources, re-list the base entries.
{{% /notice %}}

## Make the section appear

Enable the two UI extensions—the plugin is off by default, and this alone makes the section show up:

```yaml
app:
  extensions:
    - page:agent-platform
    - nav-item:agent-platform
```

The section's tabs (Agents, Sessions, MCP Servers) come along automatically.

## Name the Muster installations

Without an explicit installation list, the MCP Servers view falls back to a legacy single-server entry and the installation picker mislabels your installation. Configure each installation the portal should reach:

```yaml
muster:
  installations:
    - name: <cluster name>
      url: https://muster.<cluster>.<base domain>/mcp
      authProvider: <auth provider name>
```

The `name` must match the Kubernetes cluster name the portal knows, so the resource views and the MCP proxy line up. The `authProvider` names the auth provider used for the user's Muster sign-in. Without it, no per-user Muster session can exist and per-server sign-in is suppressed.

## Let agent avatars render

Agents render their identifying icons from the installation's avatar service at `avatars.<base domain>`. The portal's content security policy blocks that host unless it's allowed:

```yaml
backend:
  csp:
    imgSrc:
      - "'self'"
      - 'data:'
      - https://avatars.<base domain>
```

Remember the array-replacement rule from the warning at the start: keep `'self'` and `data:` in the list.

## Configure skill repositories

The create-an-agent flow offers skills discovered from Git repositories. With no repositories configured, the skills step is skipped and every agent starts skill-less:

```yaml
agentPlatform:
  skills:
    repositories:
      - https://github.com/giantswarm/agent-skills
```

Every `SKILL.md` file in a listed repository defines one selectable skill.

That's the browse experience complete. Deploying agents needs no further portal configuration: the portal creates agents through agent-manager's tools, called over the installation's Muster as the signed-in person. The installation picker offers only installations whose Muster lists `agent-manager`.

## Accept the portal's token at the agent runtime

The Sessions tab reads the agent runtime API, which sits behind an OAuth proxy. That proxy accepts a bearer token only when the token's audience matches its own client or an explicitly allowed extra audience. Each portal instance has its own OIDC client, so add the portal's client ID as an extra audience in the platform deployment's values:

```yaml
kagent:
  oauth2-proxy:
    extraArgs:
      oidc-extra-audience: <portal OIDC client ID>
```

Several portal instances share one comma-separated value—don't add a second `oidc-extra-audience` key, since a duplicate YAML map key drops one of them with no error. Without this, the Sessions tab answers `401` and reports it couldn't read the installation.

## What each capability needs

| Configuration | Browse | Deploy |
|---|---|---|
| UI extensions | required | required |
| `muster.installations` | required | required |
| CSP image origin | required | required |
| Skill repositories | optional | recommended |
| Runtime OAuth audience | Sessions tab only | Sessions tab only |

## Related

- [Agent Platform in the developer portal]({{< relref "/overview/developer-portal/agent-platform" >}}) - What you just enabled.
- [Create and deploy an agent]({{< relref "/tutorials/agent-platform/create-an-agent" >}}) - The flow these settings unlock.
- [Install the Agent Platform on your own cluster]({{< relref "/tutorials/agent-platform/install" >}}) - Where the platform side of this configuration lives.
