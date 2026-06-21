---
title: Set up OAuth for Muster
linkTitle: OAuth setup
description: Protect the Muster endpoint with OAuth and Dex, configure the proxy that authenticates to downstream servers, and handle large enterprise tokens.
weight: 80
menu:
  principal:
    parent: tutorials-ai-agents-self-hosting
    identifier: tutorials-ai-agents-oauth-setup
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I protect Muster with OAuth?
  - How does Muster authenticate to downstream MCP servers?
  - Why do users with many groups fail to authenticate?
---

{{% notice note %}}
**Applies to self-hosted Muster only.** Follow this guide when you operate your own Muster. On the managed Giant Swarm platform, the endpoint is already protected for you.
{{% /notice %}}

Muster runs two distinct OAuth roles, and you configure them independently:

- **Resource server** (`oauth.server`): Muster protects its own MCP endpoint. Clients present a valid access token to reach any protected endpoint.
- **Client proxy** (`oauth.mcpClient`): Muster authenticates to downstream MCP servers on a user's behalf, so tokens never reach the client directly.

This guide assumes Muster is already [deployed]({{< relref "/tutorials/ai-agents/self-hosting/deploy-muster" >}}). For the security model behind it, see the [security overview]({{< relref "/overview/ai-agents/security" >}}).

## Protect the endpoint with the resource server

Enable the resource-server role and point it at your OIDC provider. On a Giant Swarm cluster, that's Dex.

```yaml
muster:
  oauth:
    server:
      enabled: true
      baseUrl: "https://muster.<management-cluster>.<base-domain>"
      provider: "dex"
      dex:
        issuerUrl: "https://dex.<management-cluster>.<base-domain>"
        clientId: "muster-server"
      existingSecret: "muster-oauth"
      encryptionKey: true
      storage:
        type: "valkey"
        valkey:
          url: "valkey.muster.svc:6379"
          tls:
            enabled: true
```

- `baseUrl` is Muster's own public HTTPS URL. Muster uses it as the OAuth issuer, so it must match how clients reach the endpoint. Production requires HTTPS for every OAuth endpoint.
- `dex.issuerUrl` is the Dex issuer. Muster validates user tokens against it.
- `dex.clientId` is the client registered for Muster in Dex's static clients, with a redirect URI of `{baseUrl}/oauth/callback`.

Muster enforces PKCE on the authorization-code flow and issues access tokens with a thirty-minute lifetime, matched to Dex. Clients refresh automatically.

### Provide the secrets

The resource server reads its secrets from mounted files, not from Helm values. Create the secret the chart expects and reference it through `existingSecret`:

```bash
kubectl create secret generic muster-oauth -n muster \
  --from-literal=dex-client-secret=<dex-client-secret> \
  --from-literal=registration-token=$(openssl rand -hex 32) \
  --from-literal=oauth-encryption-key=$(openssl rand -base64 32) \
  --from-literal=valkey-password=<valkey-password>
```

- `dex-client-secret`: the client secret for `dex.clientId`.
- `registration-token`: the shared secret a client presents to register (see below).
- `oauth-encryption-key`: a 32-byte base64 key for encrypting stored tokens at rest. Needed when `encryptionKey: true`.
- `valkey-password`: only when storage is Valkey.

### Choose token storage

In-memory storage is the default but loses every session on a pod restart and can't be shared across replicas. For production, use Valkey so sessions survive restarts and rolling updates and several replicas share state. The resource-server values shown earlier enable Valkey.

### Let clients register

MCP clients register with Muster before they can obtain a token. Pick the mechanism that fits each client:

- `registrationToken`: a shared secret for managed clients that can store it, such as a portal backend.
- `trustedPublicRegistrationSchemes`: custom URI schemes for native desktop apps, for example `["cursor", "vscode"]`.
- `trustedPublicRegistrationRedirectURIs`: stable HTTPS callbacks for hosted clients you control.
- `allowLocalhostRedirectURIs`: localhost callbacks for the local `muster agent` bridge. On by default.

Avoid `allowPublicClientRegistration` in production. It opens the registration endpoint to anyone.

## Authenticate to downstream servers with the proxy

The client-proxy role lets Muster handle a downstream server's OAuth flow for the user. When a protected downstream server returns a challenge, Muster generates the authorization URL, the user authenticates in a browser, and Muster stores the resulting token scoped to that user.

```yaml
muster:
  oauth:
    mcpClient:
      enabled: true
      publicUrl: "https://muster.<management-cluster>.<base-domain>"
```

- `publicUrl` is Muster's public URL, used to build the proxy callback at `/oauth/proxy/callback`.
- Leave `clientId` empty to use the self-hosted client metadata document. Muster derives the client identifier as `{publicUrl}/.well-known/oauth-client.json` and serves it there, so no external file hosting is needed.

How Muster reuses or exchanges the user's token per downstream server is set on each [`MCPServer`]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}#configure-authentication) resource, not here.

## Large tokens and ingress buffers {#large-tokens-and-ingress-buffers}

Enterprise tokens that carry many group claims hit two limits:

- **Ingress header buffers.** A token with many groups can exceed the default nginx header buffer, and the request is rejected before it reaches Muster. Raise `large_client_header_buffers` on the ingress that fronts Muster, and on any `mcp-kubernetes` ingress that receives forwarded tokens.
- **Group count.** Users in a very large number of groups were once rejected outright. The OAuth layer now truncates excessive groups to a configurable limit (default 500) instead of rejecting the request. If a user belongs to more groups than the limit, make sure the groups that matter for cluster RBAC fall within it.

If a user can authenticate from a small account but fails from one in many groups, suspect these limits first.

## Verify

After both charts reconcile, a user signs in with the CLI:

```bash
muster auth login
muster auth status
```

`muster auth status` shows the aggregator as authenticated and lists each downstream server's state. A protected MCP call without a token is rejected, while `/health` stays open for probes.

## Related

- [Deploy Muster]({{< relref "/tutorials/ai-agents/self-hosting/deploy-muster" >}}): install the charts this guide configures.
- [Map RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}): connect identity-provider groups to cluster permissions.
- [Multi-cluster token exchange]({{< relref "/tutorials/ai-agents/self-hosting/multi-mc-token-exchange" >}}): cross-cluster single sign-on with RFC 8693.
- [Security model]({{< relref "/overview/ai-agents/security" >}}): per-user visibility and token handling.
