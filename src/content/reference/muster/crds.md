---
linkTitle: Custom resources
title: Muster custom resource reference
description: Field reference for the Muster MCPServer and Workflow custom resources, grounded in the API types shipped at version 0.10.0.
weight: 30
menu:
  principal:
    parent: reference-muster
    identifier: reference-muster-crds
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - What fields does the Muster MCPServer resource support?
  - What fields does a Muster Workflow support?
  - How do I shape a workflow's returned result?
last_review_date: 2026-06-21
---

Muster defines two custom resources: `MCPServer`, which registers a downstream MCP server, and `Workflow`, which packages a multi-step operation into one agent-callable tool. Both belong to the API group `muster.giantswarm.io/v1alpha1`. This reference is grounded in the API types shipped at version `0.10.0`.

In Kubernetes mode, you author these as custom resources. With file-based configuration, the same schema applies under `mcpservers/` and `workflows/`. To create one from the CLI, see [`muster create`]({{< relref "/reference/muster/cli/create" >}}).

## MCPServer {#mcpserver}

An `MCPServer` tells Muster how to reach a downstream MCP server and how to expose its tools.

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: kubernetes
  namespace: muster
spec:
  type: streamable-http
  url: https://mcp-kubernetes.<management-cluster>.<base-domain>/mcp
  autoStart: true
  family:
    name: kubernetes
    instanceArg: management_cluster
  auth:
    type: oauth
    forwardToken: true
```

### `spec` fields {#mcpserver-spec}

| Field | Type | Description |
|---|---|---|
| `type` | string | Required. One of `stdio`, `streamable-http`, or `sse` |
| `command` | string | Executable for a `stdio` server. Required when `type` is `stdio` |
| `args` | array | Command-line arguments. Only allowed when `type` is `stdio` |
| `url` | string | Endpoint URL. Required when `type` is `streamable-http` or `sse` |
| `env` | map | Environment variables for the server |
| `headers` | map | HTTP headers for requests to a remote server. Only allowed for `streamable-http` or `sse` |
| `toolPrefix` | string | Prefix prepended to the server's tool names, to avoid conflicts |
| `family` | object | Group equivalent instances under one exposed surface. See [families](#mcpserver-family) |
| `description` | string | Human-readable description. Up to 500 characters |
| `autoStart` | boolean | Start the server when Muster initializes or when dependencies become available. Defaults to `false` |
| `auth` | object | Authentication for a remote server. See [auth](#mcpserver-auth) |
| `timeout` | integer | Connection timeout in seconds for remote operations. Defaults to `30`, between `1` and `300` |

### Families {#mcpserver-family}

A family groups equivalent servers, such as one `mcp-kubernetes` per management cluster, under a single exposed name. Tools appear as `<prefix>_<family-name>_<tool>` with a required argument that selects the instance.

| Field | Type | Description |
|---|---|---|
| `family.name` | string | Required. Family identifier. Servers sharing this name share the exposed surface |
| `family.instanceArg` | string | Required. Name of the required argument callers use to select the instance, for example `management_cluster` |

All servers in a family must agree on `instanceArg`. When they diverge, Muster falls back to per-server prefixing for the family and logs a warning. The argument is always required, even for a single-instance family, so agent skills stay stable as instances come and go.

### Authentication {#mcpserver-auth}

`spec.auth` configures Single Sign-On to a remote server. For the concepts, see the [security overview]({{< relref "/overview/ai-agents/security" >}}).

| Field | Type | Description |
|---|---|---|
| `auth.type` | string | `oauth` or `none`. Defaults to `none` |
| `auth.forwardToken` | boolean | Forward the user's ID token to this server instead of a separate OAuth flow. The server must trust Muster's client ID. Defaults to `false` |
| `auth.requiredAudiences` | array | Extra audiences the forwarded ID token should carry, requested from the IdP at login |
| `auth.tokenExchange` | object | RFC 8693 token exchange for cross-cluster SSO. See [token exchange](#mcpserver-token-exchange) |
| `auth.authorizationServer` | object | Opt-out for backends without RFC 9728 metadata. See [authorization server](#mcpserver-authz-server) |

`authorizationServer` is mutually exclusive with `forwardToken: true` and with `tokenExchange.enabled: true`. It's only valid when `type` is `oauth`. Token exchange takes precedence over `forwardToken` when both are set.

#### Token exchange {#mcpserver-token-exchange}

`auth.tokenExchange` exchanges Muster's local token for one valid on a remote cluster's IdP. Use it when the remote cluster runs its own Dex.

| Field | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to attempt token exchange. Defaults to `false` |
| `dexTokenEndpoint` | string | URL of the remote Dex token endpoint. Required when `enabled` is `true` |
| `expectedIssuer` | string | Expected `iss` claim in the exchanged token. Derived from `dexTokenEndpoint` when unset |
| `connectorId` | string | ID of the remote Dex OIDC connector that trusts the local Dex. Required when `enabled` is `true` |
| `scopes` | string | Scopes for the exchanged token. Defaults to `openid profile email groups` |
| `clientCredentialsSecretRef` | object | Reference to a `Secret` with client credentials, when the remote Dex requires client authentication |

`clientCredentialsSecretRef` takes `name`, optional `namespace` (defaults to the `MCPServer` namespace), `clientIdKey` (defaults to `client-id`), and `clientSecretKey` (defaults to `client-secret`). For a worked example, see [multi-cluster token exchange]({{< relref "/tutorials/ai-agents/self-hosting/multi-mc-token-exchange" >}}).

#### Authorization server {#mcpserver-authz-server}

`auth.authorizationServer` pins the OAuth authorization server for backends that publish RFC 8414 metadata at their origin instead of RFC 9728. See [connecting custom MCP servers]({{< relref "/tutorials/ai-agents/connecting-custom-mcp-servers" >}}).

| Field | Type | Description |
|---|---|---|
| `issuer` | string | Required. The OAuth 2.0 / OIDC issuer URL. Must be HTTPS, no trailing slash |
| `scopes` | string | Space-separated OAuth scope tokens |

### `status` {#mcpserver-status}

The reconciler reports infrastructure state in `status.state`. For a `stdio` server: `Running`, `Starting`, `Stopped`, or `Failed`. For a remote server: `Connected`, `Auth Required`, `Connecting`, `Disconnected`, or `Failed`. Per-user authentication state is tracked separately, not in the resource status.

## Workflow {#workflow}

A `Workflow` defines an ordered set of steps that Muster runs server-side, exposed to agents as a `workflow_<name>` tool. To author one, see [Author a Muster workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}).

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: Workflow
metadata:
  name: crashlooping-pods
spec:
  description: List pods in CrashLoopBackOff on a cluster.
  args:
    cluster:
      type: string
      required: true
  steps:
    - id: pods
      tool: x_kubernetes_get_pods
      args:
        management_cluster: "{{ .input.cluster }}"
  output:
    pods: "{{ .results.pods.items }}"
    count: "{{ len .results.pods.items }}"
```

### `spec` fields {#workflow-spec}

| Field | Type | Description |
|---|---|---|
| `description` | string | Human-readable description. Up to 1000 characters. This is the only text the agent uses to discover the workflow |
| `args` | map | Argument schema, keyed by argument name. See [argument definitions](#workflow-args) |
| `steps` | array | Required, at least one. The execution flow. See [steps](#workflow-step) |
| `onFailure` | array | Best-effort cleanup sub-steps run when the workflow fails on a step that doesn't allow failure. They run sequentially and tolerate their own failures |
| `output` | object | Templated projection that shapes the returned document. See [output projection](#workflow-output) |

### Argument definitions {#workflow-args}

Each entry under `spec.args` validates one workflow argument.

| Field | Type | Description |
|---|---|---|
| `type` | string | Required. One of `string`, `integer`, `boolean`, `number`, `object`, `array` |
| `required` | boolean | Whether the argument must be provided. Defaults to `false` |
| `default` | any | Default value when the argument is omitted |
| `description` | string | Human-readable documentation. Up to 500 characters |

### Steps {#workflow-step}

A step is exactly one of: a tool call (`tool`), a sequential loop (`forEach`), or a concurrent group (`parallel`). The CRD enforces this with a validation rule.

| Field | Type | Description |
|---|---|---|
| `id` | string | Required. Unique within the workflow. Pattern `^[a-zA-Z0-9_-]+$`, up to 63 characters |
| `tool` | string | Name of the tool to run. Mutually exclusive with `forEach` and `parallel` |
| `args` | map | Arguments for the tool. Values may be any JSON type and support templating |
| `condition` | object | Gate that decides whether the step runs. See [conditions](#workflow-condition) |
| `forEach` | object | Run a body of sub-steps once per list item. See [forEach](#workflow-foreach) |
| `parallel` | array | Run a group of sub-steps concurrently. Each resolves its arguments from the state before the group started; siblings can't reference each other |
| `output` | boolean | Whether this step's result is included in the returned document. See [output flag](#workflow-output-flag) |
| `store` | boolean | Deprecated alias for `output`. See [output flag](#workflow-output-flag) |
| `allowFailure` | boolean | Continue to the next step on error. Defaults to `false` |
| `description` | string | Human-readable documentation. Up to 500 characters |

#### `forEach` {#workflow-foreach}

A `forEach` step runs a flat body of sub-steps once per item. It can't nest another `forEach` or `parallel`.

| Field | Type | Description |
|---|---|---|
| `items` | string | Required. Template that resolves to an array, for example `{{ .input.clusters }}` |
| `as` | string | Loop variable name, available as `{{ .vars.<as> }}`. Defaults to `item` |
| `steps` | array | Required, at least one. The sub-steps run for each item |

Inside the loop, the current item is `{{ .vars.<as> }}` and its index is `{{ .vars.<as>_index }}`. A sub-step result is addressable per iteration as `{{ .results.<id>_<index> }}`; the plain `{{ .results.<id> }}` holds the last iteration's result.

#### Sub-steps {#workflow-substep}

The entries of `forEach.steps`, `parallel`, and `onFailure` are sub-steps. A sub-step is always a tool call, never a nested loop or group, which keeps the schema non-recursive. It takes `id` and `tool` (both required), plus the optional `args`, `condition`, `output`, `store` (deprecated), `allowFailure`, and `description` fields, with the same meaning as on a step.

### Conditions {#workflow-condition}

A condition selects its evaluation source with exactly one of `template`, `tool`, or `fromStep`. A `tool` or `fromStep` condition must declare `expect` or `expectNot`. Both rules are enforced at apply time and on the structured authoring path.

| Field | Type | Description |
|---|---|---|
| `template` | string | Boolean Go-template gate. The step runs only when it renders to `true`, for example `{{ eq .input.env "production" }}`. When set, `expect`/`expectNot` are ignored |
| `tool` | string | Tool to run for the check |
| `args` | map | Arguments for the condition tool |
| `fromStep` | string | Step ID whose result the check reads |
| `expect` | object | Positive expectation. See [expectations](#workflow-condition-expect) |
| `expectNot` | object | Negative expectation |

#### Expectations {#workflow-condition-expect}

| Field | Type | Description |
|---|---|---|
| `success` | boolean | Whether the tool call should succeed |
| `jsonPath` | map | Path-to-value checks against the result |

As of version `0.10.0`, `jsonPath` and `expectNot.jsonPath` use the same path navigator as step arguments and templates. Paths support array indexing such as `items[0].name`, and an optional full Go-template form that exposes the result as `.result`, for example `{{ (index .result.items 0).name }}`. Existing dotted paths keep working.

### Output flag {#workflow-output-flag}

As of version `0.10.0`, every step result is always referenceable by later steps as `{{ .results.<id>.<field> }}`, regardless of any flag. Chaining one value from a step into the next no longer forces that step's whole result into the response.

The per-step `output` flag controls only whether a result appears in the returned document. `store` is a deprecated alias kept for backward compatibility: it affects visibility only, and a workflow that still uses it logs a one-line deprecation warning on both the structured authoring path and the reconciler. Prefer `output`.

### Output projection {#workflow-output}

`spec.output` is a templated object, rendered once after all steps complete, against `.input`, `.results`, and `.vars`. It replaces the default `{execution_id, workflow, status, input, steps[], ...}` envelope, so a workflow can return a small, shaped response. When omitted, the default envelope is returned unchanged.

The projection preserves JSON types: a leaf's type comes from the value it evaluates to, not from how its rendered text looks.

- A bare reference such as `{{ .results.pods.items }}` keeps its original JSON type, so an array stays an array.
- A computed leaf keeps its result type, so `{{ len .results.events.items }}` is a number.
- A leaf that mixes literal text with an action, such as `v{{ .version }}`, renders to a string.

This preserves values whose form matters, such as versions or zero-padded IDs like `08`, without any coercion.

When `spec.output` is declared, the per-step `output` and `store` flags no longer affect the returned document. Muster logs a one-line warning naming the now-inert flags.

### `status` {#workflow-status}

The reconciler validates the spec and reports `status.valid`, any `status.validationErrors`, the `status.referencedTools` (informational; actual availability depends on the user's session), the `status.stepCount`, and standard conditions.

### Templating context {#workflow-templating}

Step arguments and templates render with the [Sprig](https://masterminds.github.io/sprig/) function library. The available context:

| Reference | Description |
|---|---|
| `{{ .input.<arg> }}` | A workflow argument |
| `{{ .results.<id>.<field> }}` | A field from an earlier step's result, always available |
| `{{ .vars.<name> }}` | A loop variable inside `forEach` |
| `{{ .context.<x> }}` | Execution context values |

The engine renders with `missingkey=error`, so a reference to a missing key fails the step rather than rendering empty.

## Related

- [Author a Muster workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}) - Write workflows step by step.
- [Managing MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}) - Register and operate `MCPServer` resources.
- [Meta-tools]({{< relref "/reference/muster/meta-tools" >}}) - The tools these resources expose to agents.
