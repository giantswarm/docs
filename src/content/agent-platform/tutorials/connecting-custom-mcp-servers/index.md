---
title: Connect custom MCP servers
diataxis_content_type: how-to-guide
linkTitle: Connect custom servers
description: Bring third-party and internal MCP servers behind Muster, including servers that don't publish RFC 9728 metadata and providers that register no OAuth clients, such as GitHub and Slack.
weight: 30
menu:
  principal:
    parent: agent-platform-tutorials
    identifier: agent-platform-tutorials-connecting-custom-mcp-servers
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-29
user_questions:
  - How do I connect a third-party MCP server to Muster?
  - How do I connect an MCP server that doesn't publish OAuth metadata?
  - What is the authorizationServer override?
  - How do I connect a provider that doesn't support dynamic client registration, like GitHub or Slack?
aliases:
  - /tutorials/agent-platform/connecting-custom-mcp-servers/
  - /tutorials/ai-agents/connecting-custom-mcp-servers/
---

Any MCP server can sit behind Muster—internal tools, vendor services, the Model Context Protocol project's reference servers, or a commercial remote server. You register it the same way as any other server, with an [`MCPServer` resource]({{< relref "/agent-platform/tutorials/managing-mcp-servers" >}}). It shows up in the developer portal under **Registered servers**, next to the platform's own Infrastructure and Agent Platform servers. This guide covers the parts specific to third-party servers: unauthenticated servers, bearer-token servers, and OAuth servers that don't advertise their authorization server the standard way. It also covers providers that only accept an app you registered with them in advance.

## An unauthenticated or token-header server

The simplest custom servers need no OAuth. A public or internal server that takes a static bearer token accepts it through `headers`:

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: vendor-tools
  namespace: muster
spec:
  type: streamable-http
  url: "https://tools.vendor.example.com/mcp"
  headers:
    Authorization: "Bearer <token>"
  description: Vendor MCP server with a static token.
```

Store the token in a secret and inject it through your deployment pipeline rather than committing it to Git.

## An OAuth server with standard discovery

When a remote server publishes RFC 9728 Protected Resource Metadata, Muster discovers its authorization server automatically. Declare `auth.type: oauth` and Muster runs the login flow for you:

```yaml
spec:
  type: streamable-http
  url: "https://api.example.com/mcp"
  auth:
    type: oauth
```

The first time a user calls a tool from this server, Muster detects the `401` challenge and hands the agent an authorization URL. After the user authenticates in the browser, Muster retries the call with the acquired token. The [security model]({{< relref "/agent-platform/overview/security" >}}) walks through this exchange.

## A server that doesn't publish RFC 9728 metadata

Some OAuth servers publish RFC 8414 metadata at their own origin instead of advertising it through RFC 9728. The Atlassian remote MCP server is one example. For these, point Muster at the authorization server directly with `auth.authorizationServer`:

```yaml
spec:
  type: streamable-http
  url: "https://mcp.atlassian.com/v1/sse"
  auth:
    type: oauth
    authorizationServer:
      issuer: "https://auth.atlassian.com"
      scopes: "read:jira-work offline_access"
```

What this does and doesn't change:

- It tells Muster's per-server login flow to skip metadata probing and use the issuer you give. Muster fetches the issuer's metadata through standard OIDC discovery.
- It **doesn't** suppress the connect-time probe. A server without RFC 9728 metadata still reconciles to `Auth Required` on first connect, then moves to `Connected` after the user logs in. That's expected.
- It's **mutually exclusive** with `forwardToken: true` and with token exchange. A custom OAuth server uses its own login, not Muster's identity—so don't combine the override with token forwarding. Muster's admission rules reject a resource that sets both.

Muster logs each use of the override, so non-standard servers stay visible to operators.

## A provider that registers no clients

Some hosted MCP servers publish their OAuth metadata but refuse dynamic client registration. GitHub's hosted MCP server and Slack's hosted MCP server are two examples. Both accept only an app that you registered with them by hand, identified by a fixed client ID and a client secret. Muster supports this through three more fields under `auth.authorizationServer`:

```yaml
spec:
  type: streamable-http
  url: "https://mcp.slack.com/mcp"
  auth:
    type: oauth
    authorizationServer:
      issuer: "https://mcp.slack.com"
      scopes: "search:read.public channels:history channels:read users:read chat:write reactions:write"
      clientCredentialsSecretRef:
        name: slack-oauth-client
      grantScope: subject
```

- `clientCredentialsSecretRef` names a Secret in the `MCPServer`'s namespace with the keys `client-id` and `client-secret`. Muster then identifies itself with that client instead of registering one, and presents the same client when it refreshes a token. When you rotate the secret, the next login picks up the new value; no restart is needed.
- `grantScope: subject` files the person's tokens under their identity instead of under one session. The person consents once. Every later session of theirs, from another MCP client, from a chat surface, or after a Muster restart, reuses the grant without a new login, until they sign out of that server or Muster.
- `scopes` lists exactly what the app requests. Keep it equal to the scopes you configured in the provider's app; a change on either side is a new consent for every person.

Two things to prepare in the provider:

1. **The redirect URL.** The app's only redirect URL is Muster's outbound OAuth callback: `https://<your Muster host>/oauth/proxy/callback`. Muster publishes the exact value in its client metadata at `https://<your Muster host>/.well-known/oauth-client.json`, under `redirect_uris`. Copy it from there. Providers match this URL exactly.
2. **The credentials.** Put the client ID and the client secret into the Secret. Quote both values if you write the Secret as YAML: a client ID that looks like a number, such as Slack's `1234567890.1234567890`, otherwise ends up stored as a float.

When the provider publishes RFC 8414 metadata at the issuer, as Slack does, leave `authorizationEndpoint` and `tokenEndpoint` unset. Muster discovers the endpoints and checks the document's issuer against the pin. Set both endpoints only for a provider that publishes no document at all, such as GitHub. They must appear together.

The person's experience doesn't change: the server shows `Auth Required` until they log in, `core_auth_login` returns a link to the provider's consent screen, and after consent the tools work. The result reports `clientIdMethod: preregistered`. For Slack step by step, see [Connect Slack]({{< relref "/agent-platform/tutorials/connecting-slack" >}}).

## Verify the connection

After applying the resource, check that the server registered and reached a sensible state:

```bash
kubectl get mcpservers -n muster
muster auth status
```

A custom OAuth server showing `Auth Required` is normal until a user logs in. If it shows `Failed`, the endpoint is unreachable—check the URL, network policy, and that the server actually speaks the transport you declared. The [troubleshooting guide]({{< relref "/agent-platform/tutorials/troubleshooting" >}}) covers the common failure modes.

## Related

- [Manage MCP servers]({{< relref "/agent-platform/tutorials/managing-mcp-servers" >}}): the full `MCPServer` field set.
- [Connect Slack]({{< relref "/agent-platform/tutorials/connecting-slack" >}}): a worked example of a provider that registers no clients.
- [Map RBAC and SSO]({{< relref "/agent-platform/tutorials/access-control" >}}): when the custom server shares your identity provider.
