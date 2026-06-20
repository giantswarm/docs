---
title: Connect custom MCP servers
linkTitle: Connect custom servers
description: Bring third-party and internal MCP servers behind Muster, including servers that don't publish RFC 9728 metadata, using the authorizationServer override.
weight: 30
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-connecting-custom-mcp-servers
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I connect a third-party MCP server to Muster?
  - How do I connect an MCP server that doesn't publish OAuth metadata?
  - What is the authorizationServer override?
---

Any MCP server can sit behind Muster—internal tools, vendor services, the reference servers, or a commercial remote server. You register it the same way as any other server, with an [`MCPServer` resource]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}). This guide covers the parts specific to third-party servers: unauthenticated servers, bearer-token servers, and OAuth servers that don't advertise their authorization server the standard way.

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

The first time a user calls a tool from this server, Muster detects the `401` challenge and hands the agent an authorization URL. After the user authenticates in the browser, Muster retries the call with the acquired token. The [security model]({{< relref "/overview/ai-agents/security" >}}) walks through this exchange.

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

## Verify the connection

After applying the resource, check that the server registered and reached a sensible state:

```bash
kubectl get mcpservers -n muster
muster auth status
```

A custom OAuth server showing `Auth Required` is normal until a user logs in. If it shows `Failed`, the endpoint is unreachable—check the URL, network policy, and that the server actually speaks the transport you declared. The [troubleshooting guide]({{< relref "/tutorials/ai-agents/troubleshooting" >}}) covers the common failure modes.

## Related

- [Manage MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}): the full `MCPServer` field set.
- [Map RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}): when the custom server shares your identity provider.
