---
title: MCPServer CRD schema reference (group muster.giantswarm.io)
diataxis_content_type: reference
linkTitle: MCPServer
description: |
  MCPServer is the Schema for the mcpservers API
weight: 100
crd:
  name_camelcase: MCPServer
  name_plural: mcpservers
  name_singular: mcpserver
  group: muster.giantswarm.io
  technical_name: mcpservers.muster.giantswarm.io
  scope: Namespaced
  source_repository: https://github.com/giantswarm/muster
  source_repository_ref: v0.22.10
  versions:
    - v1alpha1
  topics:
    - managementcluster
    - agent-platform
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
aliases:
  - /use-the-api/management-api/crd/mcpservers.muster.giantswarm.io/
technical_name: mcpservers.muster.giantswarm.io
source_repository: https://github.com/giantswarm/muster
source_repository_ref: v0.22.10
---

# MCPServer


<p class="crd-description">MCPServer is the Schema for the mcpservers API</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">mcpservers.muster.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">muster.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">mcpserver</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">mcpservers</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: git-tools
  namespace: default
spec:
  type: stdio
  autoStart: true
  command: npx
  args: ["@modelcontextprotocol/server-git"]
  env:
    GIT_ROOT: "/workspace"
    LOG_LEVEL: "info"
  description: "Git tools MCP server for repository operations"
```


<h3 id="property-details-v1alpha1">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.apiVersion">.apiVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIVersion defines the versioned schema of this representation of an object.
Servers should convert recognized schemas to the latest internal value, and
may reject unrecognized values.
More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.kind">.kind</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Kind is a string value representing the REST resource this object represents.
Servers may infer this from the endpoint the client submits requests to.
Cannot be updated.
In CamelCase.
More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>MCPServerSpec defines the desired state of MCPServer</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.args">.spec.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Args specifies the command line arguments for stdio type servers.
This field is only available when Type is &ldquo;stdio&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.args[*]">.spec.args[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth">.spec.auth</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Auth configures authentication behavior for this MCP server.
This is only relevant for remote servers (streamable-http or sse).</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.authorizationServer">.spec.auth.authorizationServer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AuthorizationServer is an opt-out for backends that don&rsquo;t publish RFC 9728
Protected Resource Metadata. When set, muster&rsquo;s per-server OAuth login flow
(core_auth_login) skips PRM probing and uses these values directly. muster
logs each override use at INFO so non-compliance is observable.</p>

<p>This override does NOT bypass mcp-go&rsquo;s connect-time PRM probe; backends
without RFC 9728 metadata still reconcile to &ldquo;Auth Required&rdquo; on first
connect, then transition to &ldquo;Connected&rdquo; after <code>muster auth login</code>.</p>

<p>Setting AuthorizationServer does NOT change the RFC 8707 <code>resource</code>
parameter — that remains driven by the MCP server URL.</p>

<p>AuthorizationServer is mutually exclusive with ForwardToken: true and
TokenExchange.Enabled: true. The CRD admission rules above reject any
CR that combines them. Only valid when Type is &ldquo;oauth&rdquo;.</p>

<p>Use case: Atlassian Remote MCP and similar backends that publish RFC 8414
metadata at their resource origin instead of via RFC 9728.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.authorizationServer.issuer">.spec.auth.authorizationServer.issuer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Issuer is the OAuth 2.0 / OIDC issuer URL.
muster fetches AS metadata via the existing OAuth client, which performs
RFC 8414 / OIDC discovery against this issuer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.authorizationServer.scopes">.spec.auth.authorizationServer.scopes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Scopes is the OAuth scope parameter value (RFC 6749 §3.3 wire format:
space-separated scope tokens). Matches existing TokenExchangeConfig.Scopes.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.forwardToken">.spec.auth.forwardToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ForwardToken enables ID token forwarding for SSO.
When true, muster forwards the user&rsquo;s ID token to this server instead of
triggering a separate OAuth flow. The downstream server must be configured
to trust muster&rsquo;s client ID in its TrustedAudiences.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.localMint">.spec.auth.localMint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalMint enables downstream auth via a per-backend token minted by muster
from its own signing key. On each call muster reads the caller&rsquo;s bearer as
the subject and an optional X-Actor-Token header as the actor, then mints a
token (sub=subject, act=actor, aud=Audience, iss=muster) through muster&rsquo;s
RFC 8693 broker.</p>

<p>Use LocalMint when the backend must authorize an agent acting on behalf of a
human (OBO) and no shared remote IdP can issue a token with the backend&rsquo;s
audience. Requires muster&rsquo;s OAuth server to run in
JWT mode with a broker local-mint target whose audience equals Audience.</p>

<p>LocalMint is mutually exclusive with ForwardToken, TokenExchange, and
AuthorizationServer (the CRD admission rules above reject combinations).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.localMint.audience">.spec.auth.localMint.audience</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Audience is the minted token&rsquo;s aud claim: the backend&rsquo;s resource identifier.
It must equal a configured broker local-mint target; the mint fails closed
when no matching target exists.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.localMint.enabled">.spec.auth.localMint.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Enabled turns on local minting for this server.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.requiredAudiences">.spec.auth.requiredAudiences</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>RequiredAudiences specifies additional audience(s) that the forwarded ID token
should contain. When ForwardToken is true, muster will request these audiences
from the upstream IdP (e.g., Dex) using cross-client scopes.</p>

<p>This is used when the downstream server requires tokens with specific audiences,
for example when forwarding tokens to Kubernetes for OIDC authentication:
  requiredAudiences:
    - &ldquo;dex-k8s-authenticator&rdquo;</p>

<p>At user authentication, muster collects all requiredAudiences from MCPServers
with forwardToken: true and requests them all from the IdP.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.requiredAudiences[*]">.spec.auth.requiredAudiences[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange">.spec.auth.tokenExchange</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>TokenExchange enables SSO via RFC 8693 Token Exchange for cross-cluster SSO.
When configured, muster exchanges its local token for a token valid on the
remote cluster&rsquo;s Identity Provider (e.g., Dex).</p>

<p>Use TokenExchange when:
  - The remote cluster has its own Dex instance
  - The remote Dex is configured with an OIDC connector for muster&rsquo;s Dex
  - You need a token issued by the remote cluster&rsquo;s IdP (not just forwarded)</p>

<p>Token exchange takes precedence over ForwardToken if both are configured.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.clientCredentialsSecretRef">.spec.auth.tokenExchange.clientCredentialsSecretRef</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ClientCredentialsSecretRef references a Kubernetes Secret containing
client credentials for authenticating with the remote Dex&rsquo;s token endpoint.
This is required when the remote Dex requires client authentication for
token exchange (RFC 8693).</p>

<p>The secret should contain:
  - client-id: The OAuth client ID registered on the remote Dex
  - client-secret: The OAuth client secret for authentication</p>

<p>Example secret:</p>

<pre><code>apiVersion: v1
kind: Secret
metadata:
  name: grizzly-token-exchange-credentials
  namespace: muster
type: Opaque
stringData:
  client-id: muster-token-exchange
  client-secret: &lt;secret-value&gt;
</code></pre>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.clientCredentialsSecretRef.clientIdKey">.spec.auth.tokenExchange.clientCredentialsSecretRef.clientIdKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ClientIDKey is the key in the secret data that contains the client ID.
Defaults to &ldquo;client-id&rdquo; if not specified.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.clientCredentialsSecretRef.clientSecretKey">.spec.auth.tokenExchange.clientCredentialsSecretRef.clientSecretKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ClientSecretKey is the key in the secret data that contains the client secret.
Defaults to &ldquo;client-secret&rdquo; if not specified.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.clientCredentialsSecretRef.name">.spec.auth.tokenExchange.clientCredentialsSecretRef.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the Kubernetes Secret.
Required.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.clientCredentialsSecretRef.namespace">.spec.auth.tokenExchange.clientCredentialsSecretRef.namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Namespace is the Kubernetes namespace where the secret is located.
If not specified, defaults to the MCPServer&rsquo;s namespace.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.connectorId">.spec.auth.tokenExchange.connectorId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ConnectorID is the ID of the OIDC connector on the remote Dex that
trusts the local cluster&rsquo;s Dex.
Required when Enabled is true.
Example: &ldquo;cluster-a-dex&rdquo;</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.dexTokenEndpoint">.spec.auth.tokenExchange.dexTokenEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DexTokenEndpoint is the URL used to connect to the remote cluster&rsquo;s Dex token endpoint.
This may differ from the issuer URL when access goes through a proxy.
Required when Enabled is true.
Example: <a href="https://dex.cluster-b.example.com/token">https://dex.cluster-b.example.com/token</a> (direct)
Example: <a href="https://dex-cluster.proxy.example.com/token">https://dex-cluster.proxy.example.com/token</a> (via proxy)</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.enabled">.spec.auth.tokenExchange.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Enabled determines whether token exchange should be attempted.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.expectedIssuer">.spec.auth.tokenExchange.expectedIssuer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ExpectedIssuer is the expected issuer URL in the exchanged token&rsquo;s &ldquo;iss&rdquo; claim.
This should match the remote Dex&rsquo;s configured issuer URL.
When access goes through a proxy, this differs from DexTokenEndpoint.
If not specified, the issuer is derived from DexTokenEndpoint (backward compatible).
Example: <a href="https://dex.cluster-b.example.com">https://dex.cluster-b.example.com</a></p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.tokenExchange.scopes">.spec.auth.tokenExchange.scopes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Scopes are the scopes to request for the exchanged token.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.auth.type">.spec.auth.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Type specifies the authentication type.
Supported values:
  - &ldquo;oauth&rdquo;: OAuth 2.0/OIDC authentication
  - &ldquo;none&rdquo;: No authentication</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.autoStart">.spec.autoStart</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AutoStart determines whether this MCP server should be automatically started
when the muster system initializes or when dependencies become available.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.command">.spec.command</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Command specifies the executable path for stdio type servers.
This field is required when Type is &ldquo;stdio&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.description">.spec.description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides a human-readable description of this MCP server&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.env">.spec.env</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Env contains environment variables to set for the MCP server.
For stdio servers, these are passed to the process when it is started.
For remote servers, these can be used for authentication or configuration.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.family">.spec.family</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Family declares that this MCP server is an instance of a family of
equivalent servers (for example, multiple kubernetes MCP servers pointed
at different clusters). When set, the aggregator exposes tools from all
servers in the same family under a single name
({musterPrefix}<em>{family.name}</em>{toolName}) with a required parameter
(named by family.instanceArg) that selects which instance handles the
call. The parameter is always required even for single-instance families
so skills written against the family name remain stable as instances are
added or removed. When unset, the legacy per-server prefixing applies
({musterPrefix}<em>{toolPrefix-or-name}</em>{toolName}).</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.family.instanceArg">.spec.family.instanceArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>InstanceArg names the required parameter callers use to select which
family member handles the tool call (for example &ldquo;management_cluster&rdquo;,
&ldquo;country&rdquo;, &ldquo;model&rdquo;). All servers declaring the same family.name must
agree on InstanceArg; if they diverge, the aggregator falls back to
per-server prefixing for the entire family and logs a warning.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.family.name">.spec.family.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the family identifier. Servers sharing the same Name expose
their tools as {musterPrefix}<em>{Name}</em>{toolName}.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.headers">.spec.headers</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Headers contains HTTP headers to send with requests to remote MCP servers.
This field is only relevant when Type is &ldquo;streamable-http&rdquo; or &ldquo;sse&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.timeout">.spec.timeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Timeout specifies the connection timeout for remote operations (in seconds)</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.toolPrefix">.spec.toolPrefix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ToolPrefix is an optional prefix that will be prepended to all tool names
provided by this MCP server. This helps avoid naming conflicts when multiple
servers provide tools with similar names.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.type">.spec.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Type specifies how this MCP server should be executed.
Supported values: &ldquo;stdio&rdquo; for local processes, &ldquo;streamable-http&rdquo; for HTTP-based servers, &ldquo;sse&rdquo; for Server-Sent Events</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.url">.spec.url</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>URL is the endpoint where the remote MCP server can be reached
This field is required when Type is &ldquo;streamable-http&rdquo; or &ldquo;sse&rdquo;.
Examples: <a href="http://mcp-server:8080/mcp">http://mcp-server:8080/mcp</a>, <a href="https://api.example.com/mcp">https://api.example.com/mcp</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>MCPServerStatus defines the observed state of MCPServer.</p>

<p>This status reflects server-side observable state including auth requirements.
It captures infrastructure connectivity as well as whether the server demands
authentication (e.g. &ldquo;Auth Required&rdquo;). Per-user session state (which specific
user is authenticated, token expiry, etc.) is tracked separately in the
Session Registry (internal/aggregator/session_registry.go).</p>

<p>Server-Side State (CRD):
  - State: Running/Connected/Starting/Connecting/Stopped/Disconnected/Auth Required/Failed
  - Conditions: Standard K8s conditions for detailed status</p>

<p>Per-User Session State (Session Registry):
  - ConnectionStatus: Connected, PendingAuth, Failed (per-user)
  - AuthStatus: Authenticated, AuthRequired, TokenExpired (per-user)
  - AvailableTools: Tools visible to this specific user</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions">.status.conditions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Conditions represent the latest available observations of the MCPServer&rsquo;s current state.
Standard condition types:
  - Ready: True if infrastructure is reachable (process running or TCP connectable)</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*]">.status.conditions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition contains details for one aspect of the current state of this API Resource.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].lastTransitionTime">.status.conditions[*].lastTransitionTime</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].message">.status.conditions[*].message</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>message is a human readable message indicating details about the transition.
This may be an empty string.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].observedGeneration">.status.conditions[*].observedGeneration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].reason">.status.conditions[*].reason</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>reason contains a programmatic identifier indicating the reason for the condition&rsquo;s last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].status">.status.conditions[*].status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>status of the condition, one of True, False, Unknown.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].type">.status.conditions[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>type of condition in CamelCase or in foo.example.com/CamelCase.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.consecutiveFailures">.status.consecutiveFailures</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>ConsecutiveFailures tracks the number of consecutive connection failures.
This is used for exponential backoff and to identify unreachable servers.
Reset to 0 when a connection succeeds.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.lastAttempt">.status.lastAttempt</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>LastAttempt indicates when the last connection attempt was made.
Used with ConsecutiveFailures to implement exponential backoff.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.lastConnected">.status.lastConnected</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>LastConnected indicates when the server was last successfully connected</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.lastError">.status.lastError</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>LastError contains any error message from the most recent server operation.
Note: Per-user authentication errors are tracked in the Session Registry,
not here. This field only contains infrastructure-level errors.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.nextRetryAfter">.status.nextRetryAfter</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>NextRetryAfter indicates the earliest time when the next retry should be attempted.
This is calculated based on exponential backoff from ConsecutiveFailures.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.restartCount">.status.restartCount</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>RestartCount tracks how many times this server has been restarted (stdio only)</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.state">.status.state</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>State represents the high-level infrastructure state of the MCP server.
This is independent of user session state (authentication, connection status).</p>

<p>For stdio servers: Running, Starting, Stopped, Failed
For remote servers: Connected, Auth Required, Connecting, Disconnected, Failed</p>

</div>

</div>
</div>





</div>



