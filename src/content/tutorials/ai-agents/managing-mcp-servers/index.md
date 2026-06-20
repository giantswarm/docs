---
title: Manage MCP servers in Muster
linkTitle: Manage MCP servers
description: Add and configure downstream MCP servers behind Muster with MCPServer resources, covering stdio and remote transports, tool prefixes, server families, startup control, and authentication.
weight: 20
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-managing-mcp-servers
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I add an MCP server to Muster?
  - What's the difference between stdio and remote MCP servers?
  - How do I expose the same tools across multiple clusters?
---

Muster aggregates downstream MCP servers and presents their combined tools through one endpoint. You register each server as an `MCPServer` resource. Muster's reconciler picks it up, connects or starts the server, prefixes its tools to avoid name clashes, and makes them discoverable through the [meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}). No agent restart is required.

## Choose a transport

Every `MCPServer` declares a `type`:

- `stdio`: Muster starts a local process and talks to it over standard input and output. Use it for servers shipped as a command, such as the reference servers run through `npx`. Requires `command` (and usually `args`).
- `streamable-http`: a remote server reachable over HTTP. Use it for servers that run as their own service, including `mcp-kubernetes` and `mcp-prometheus`. Requires `url`.
- `sse`: a remote server using the Server-Sent Events transport. Requires `url`.

A stdio server must set `command`; a remote server must set `url`. Muster's admission rules reject a resource that mixes them. The `args` and `command` fields apply only to stdio, and `headers` applies only to remote servers.

### A stdio server

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: git-tools
  namespace: muster
spec:
  type: stdio
  autoStart: true
  command: npx
  args: ["@modelcontextprotocol/server-git"]
  description: Git tools for repository operations.
```

### A remote server

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: remote-api-tools
  namespace: muster
spec:
  type: streamable-http
  url: "https://api.example.com/mcp"
  timeout: 30
  description: Remote MCP server providing API tools.
```

## Avoid tool-name clashes with `toolPrefix`

When two servers expose a tool with the same name, the prefix keeps them distinct. By default Muster prefixes external tools with the server name, so `get` from a server named `kubernetes` becomes `x_kubernetes_get`. Set `toolPrefix` to choose a shorter or clearer prefix:

```yaml
spec:
  type: streamable-http
  url: "https://mcp-kubernetes.example.com/mcp"
  toolPrefix: "k8s"
```

## Group equivalent servers with `family`

When you run several instances of the same server—for example, one `mcp-kubernetes` per management cluster—a **family** exposes them under one tool name with a required argument that selects the instance. Without it, an agent would see one prefixed copy of every tool per cluster, multiplying the surface.

```yaml
spec:
  family:
    name: kubernetes
    instanceArg: management_cluster
```

With this, both clusters' `list` tools appear once as `x_kubernetes_list`, and the agent passes `management_cluster: <instance>` to pick the target. The instance argument is **always required**, even for a single-instance family, so tools written against the family name keep working as you add or remove instances.

All servers that share a `family.name` must agree on `instanceArg`. If they disagree, Muster falls back to per-server prefixing for the whole family and logs a warning. The value an agent passes is the **full server name**, for example `my-cluster-mcp-kubernetes`. See [multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}) for the contract.

The per-cluster `mcp-prometheus` servers follow the same pattern in their own `prometheus` family, so the cluster's metrics tools (`x_prometheus_query` and friends) collapse to one set selected by the same instance argument. Each downstream server type gets its own family.

## Control startup with `autoStart`

`autoStart: false` (the default) means the server is defined but not started until it's needed, so Muster doesn't spin up a process or load tool definitions for a server irrelevant to the current task. Set `autoStart: true` for servers that should always be available, such as per-cluster `mcp-kubernetes`. When a server starts, its tools are discovered and registered immediately, and the agent's next discovery call reflects them.

## Configure authentication

Remote servers are usually protected. The `auth` block tells Muster how to authenticate on the user's behalf. For servers that trust the same identity provider as Muster, **token forwarding** reuses the user's ID token:

```yaml
spec:
  type: streamable-http
  url: "https://mcp-kubernetes.example.com/mcp"
  auth:
    type: oauth
    forwardToken: true
    requiredAudiences:
      - "dex-k8s-authenticator"
```

`requiredAudiences` lists extra audiences the forwarded token must carry. Muster collects them from every forwarding server at login and requests them from the identity provider, so the downstream server—Kubernetes OIDC in this case—accepts the token.

For cross-cluster single sign-on, where a remote cluster runs its own identity provider, use RFC 8693 **token exchange** instead. That's covered in [multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}). For servers that don't publish standard discovery metadata, see [connecting custom MCP servers]({{< relref "/tutorials/ai-agents/connecting-custom-mcp-servers" >}}).

## Check status

Each `MCPServer` reports a `state` you can inspect:

```bash
kubectl get mcpservers -n muster
```

- Stdio servers report `Running`, `Starting`, `Stopped`, or `Failed`.
- Remote servers report `Connected`, `Auth Required`, `Connecting`, `Disconnected`, or `Failed`.

`Auth Required` means the server is reachable but needs a login—it's a normal first-connect state for a protected server, not an error. A user authenticates with `muster auth login` and the server moves to `Connected` for that user. The resource-level `state` reflects infrastructure; whether a specific user is authenticated and which tools they see is tracked per user. See the [security model]({{< relref "/overview/ai-agents/security" >}}) for how per-user visibility works.

## Apply and iterate

```bash
kubectl apply -f mcpserver.yaml
```

Muster reconciles within seconds. As with workflows, iterate directly while you're configuring, then manage the resource through your GitOps pipeline for production.
