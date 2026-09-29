---
title: Connect Slack as a per-person Connector
diataxis_content_type: how-to-guide
linkTitle: Connect Slack
description: Give agents Slack reads and posts through Slack's hosted MCP server behind Muster, where every tool call runs as the person who consented, with one internal Slack app per installation.
weight: 35
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-connecting-slack
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-29
user_questions:
  - How do I let agents read and post to Slack through Muster?
  - How do I create the Slack app for Muster's Slack Connector?
  - Which Slack scopes do agents need?
  - Why does a Slack message posted by an agent carry my name?
---

Slack runs a hosted MCP server at `https://mcp.slack.com/mcp`. It issues user tokens only, so every tool call runs as the person who consented. The agent reads the channels that person can read. A message it posts carries that person's name, with Slack's own line "Sent using" and the app's name under it. Behind Muster this makes Slack a *Connector*: Muster is the OAuth client of Slack's authorization server, and it holds one grant per person. Nothing runs as a shared bot.

This guide registers that server on one installation. It takes a Slack app, a Secret, and an `MCPServer` resource. Muster needs no change, and neither does the Slack app your agents already talk through.

## Slack's requirements

Slack's authorization server publishes standard metadata at `https://mcp.slack.com`, but it accepts no dynamic client registration. An MCP client must be backed by a Slack app with a fixed app ID. Only apps published in the Slack Marketplace, or internal apps of your workspace, may use the MCP server. Workspace admins approve the app like any other. The token endpoint accepts `client_secret_post` only and supports PKCE with `S256`.

Two consequences shape the setup:

- Muster identifies itself with the app's client ID and secret, through `clientCredentialsSecretRef`. The general pattern is described in [Connect custom MCP servers]({{< relref "/tutorials/agent-platform/connecting-custom-mcp-servers#a-provider-that-registers-no-clients" >}}).
- Create one app per installation. Each app carries exactly one redirect URL, Muster's callback on that installation.

## Step 1: Create the Slack app

You need the exact callback URL first. Muster publishes it in its client metadata:

```bash
curl -s https://<your Muster host>/.well-known/oauth-client.json | jq -r '.redirect_uris[]'
```

The answer has the form `https://<your Muster host>/oauth/proxy/callback`. Slack matches it exactly.

Then create the app from a manifest:

1. Open [Slack's app management page](https://api.slack.com/apps) and select **Create New App**, then **From a manifest**.
2. Select your workspace and the **YAML** tab, and paste this manifest. Replace the name suffix and the redirect URL.

   ```yaml
   display_information:
     name: Agent Platform Slack Connector (<installation>)
     description: Slack MCP server for agents, acting as the signed-in person.
     background_color: "#2c3e50"
   oauth_config:
     redirect_urls:
       - https://<your Muster host>/oauth/proxy/callback
     scopes:
       user:
         - search:read.public
         - channels:history
         - channels:read
         - users:read
         - chat:write
         - reactions:write
   settings:
     is_mcp_enabled: true
     token_rotation_enabled: true
     org_deploy_enabled: false
     socket_mode_enabled: false
   ```

3. After creation, open the app's **Agents** section and confirm that the **Slack Model Context Protocol (MCP) Server** feature is on. Without it, Slack refuses MCP requests although OAuth looks configured.
4. Open **OAuth & Permissions** and confirm the redirect URL and that **Token Rotation** is on. Don't select **Install to Workspace**: Muster installs the app per person through the user OAuth flow.
5. Open **Collaborators** and add a second member of your team, so the app keeps an owner when people change roles.
6. Open **Basic Information** and copy the **Client ID** and the **Client Secret** into your password manager. They go into a Secret in the next step and nowhere else.

About the scopes: this list gives public channels only. The agent can search public messages, read public channels and threads, look up people, post, and react. It can't read private channels, direct messages, or files. What an agent reads on a person's behalf ends up in a thread other people read, so start narrow. A later scope change is a new consent for every person, on both the app and the `MCPServer` resource.

Token rotation makes Slack issue user tokens that expire after 12 hours, with single-use refresh tokens. Muster refreshes them itself, ahead of expiry, and logs each refresh. Rotation can't be switched off again once it's on.

## Step 2: Store the client credentials

Create a Secret next to your other Muster credentials, in the namespace of the `MCPServer` resource, with the keys `client-id` and `client-secret`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: slack-oauth-client
  namespace: agent-platform
type: Opaque
stringData:
  client-id: "1234567890.1234567890"
  client-secret: "<the client secret>"
```

Quote both values. A Slack client ID looks like a number, and an unquoted one is stored as a float. Encrypt the file the way your installation encrypts its other Secrets before you commit it. Muster reads the Secret on each login, so a rotated secret takes effect on the next login without a restart.

## Step 3: Register the server

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: slack
  namespace: agent-platform
spec:
  autoStart: true
  type: streamable-http
  url: https://mcp.slack.com/mcp
  timeout: 60
  toolPrefix: slack
  auth:
    type: oauth
    forwardToken: false
    authorizationServer:
      issuer: https://mcp.slack.com
      scopes: search:read.public channels:history channels:read users:read chat:write reactions:write
      clientCredentialsSecretRef:
        name: slack-oauth-client
        namespace: agent-platform
      grantScope: subject
```

The pin names the issuer only. Slack publishes RFC 8414 metadata there, so Muster discovers the authorization and token endpoints and takes the RFC 8707 `resource` value from Slack's protected-resource metadata. The `scopes` line must equal the app's user scopes. `grantScope: subject` gives each person one grant for all their sessions. That matters in Slack: the gateway in front of the agents mints a fresh Muster token per turn, so a session-scoped grant would ask for consent on every turn.

Apply the Secret and the resource together. A resource without its Secret shows an error until the Secret arrives. Once both are in place, the server shows `Auth Required` with the message that it connects once a person has signed in to it, and Muster logs the pin:

```text
oauth_authorization_server_pinned issuer=https://mcp.slack.com preregisteredClient=true subjectScoped=true
```

## Step 4: Sign in and verify

From the command line:

```bash
muster auth login --server slack
muster call x_slack_search_channels --query=general --limit=3
```

The login opens Slack's consent screen with the six permissions. After consent the server state changes to `Connected`, and the search answers as you.

With the six scopes, Slack exposes eight tools. Four are annotated read-only: `x_slack_search_public`, `x_slack_search_channels`, `x_slack_read_channel`, and `x_slack_read_thread`. Four write: `x_slack_send_message`, `x_slack_schedule_message`, `x_slack_add_reaction`, and `x_slack_send_message_draft`. An agent with the `read-only` [toolset preset]({{< relref "/tutorials/agent-platform/toolset-presets" >}}) sees the four read tools as soon as the person is connected. An agent with `full` sees all eight. To let a specific agent post, add one selector to its toolset:

```yaml
toolset:
  - preset:read-only
  - tool:x_slack_send_message
```

## How people connect from Slack

A person asks an agent in Slack for something that needs a Slack tool, but hasn't connected Slack yet. Muster answers the agent's `core_auth_login` call with a sign-in link. The gateway turns that result into a **Connect slack** button, posted in the thread and visible only to that person. They select it, consent at Slack, and the turn continues. The link is valid for 10 minutes. A later click asks for a fresh one.

Two things to know about that flow:

- The button appears when the agent calls `core_auth_login` for the server. An agent that only looks for a Slack tool finds none before the person is connected, because Muster hides the tools of a server the session isn't signed in to, and answers that it has no Slack tool. Naming the server in the request, or a prompt that tells the agent to sign in to `slack`, avoids that dead end.
- In a thread shared by several people, the agent acts under the identity the gateway forwards for the turn. Check your gateway version for whose identity that's before you rely on a collaborator's post carrying their own name.

## Related

- [Connect custom MCP servers]({{< relref "/tutorials/agent-platform/connecting-custom-mcp-servers" >}}): the general pattern for providers that register no clients.
- [Toolset presets]({{< relref "/tutorials/agent-platform/toolset-presets" >}}): which agents see which tools.
- [Authentication]({{< relref "/overview/agent-platform/authentication" >}}): how the outbound OAuth flow works.
