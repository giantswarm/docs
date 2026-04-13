---
linkTitle: Workload cluster OIDC authentication
title: Configure OIDC authentication for workload clusters with structured authentication
description: Use Kubernetes structured authentication configuration to connect one or more OIDC providers to the API server of a workload cluster.
weight: 30
menu:
  principal:
    parent: tutorials-security
    identifier: tutorials-security-structured-authentication
user_questions:
  - How can I connect an OIDC provider to a workload cluster?
  - Can I configure multiple OIDC providers on the same cluster?
  - How do I migrate from the legacy OIDC flags to structured authentication?
  - How do I map OIDC claims to Kubernetes usernames and groups?
  - How do I use CEL expressions to validate OIDC tokens?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
last_review_date: 2026-04-13
---

Kubernetes [structured authentication configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration) replaces the legacy `--oidc-*` API server flags with a declarative, file-based configuration. Giant Swarm workload clusters now expose this mechanism through the `cluster` app values, which lets you wire one or more identity providers into the API server without rolling your own kubeconfig distribution.

This tutorial walks you through enabling structured authentication on a workload cluster, connecting multiple OIDC providers, mapping claims to Kubernetes identities, and migrating from the legacy configuration.

If you are looking for information on how to authorize authenticated users once they reach the API server, read our [cluster access control guide]({{< relref "/tutorials/security/rbac" >}}). For platform API authentication (the management cluster), see [platform API authentication]({{< relref "/tutorials/access-management/authentication" >}}).

## Before you begin

Structured authentication is available from the following workload cluster releases onward:

- `aws-34.0.0` (CAPA)
- `cloud-director-34.0.0` (CAPVCD)
- `vsphere-34.0.0` (CAPV)
- `azure-34.0.0` (CAPZ)

You configure it through the `global.controlPlane.oidc.structuredAuthentication` field of your `cluster` app values. Changes trigger a rolling update of the control plane nodes, so test the configuration on a non-production cluster first.

You will also need:

- Cluster-admin access to the workload cluster (to create `ClusterRoleBinding` resources for the groups you authenticate).
- At least one OIDC provider with a registered client/application for your cluster. The provider must expose a discovery document at `<issuer>/.well-known/openid-configuration`.

## Why use structured authentication

The legacy `--oidc-*` flags only allowed a single issuer per API server and offered limited control over how claims become Kubernetes identities. Structured authentication lifts both restrictions:

- Multiple issuers on the same API server, so you can serve internal and external users from different Identity Providers (IdPs) at once.
- Common Expression Language (CEL) expressions for validating tokens and mapping claims, including conditional logic on arbitrary claims.
- Per-issuer CA bundles and discovery URLs, useful for private providers whose issuer URL doesn't match the discovery endpoint.
- Declarative configuration that ships via a `ConfigMap` and is picked up by the API server on a rolling restart.

**Note**: Before Kubernetes v1.34, clusters could use [Dex (Auth Bundle)](https://docs.giantswarm.io/tutorials/access-management/configure-dex-in-your-cluster/) to plug more than one IdPs to authenticate your users. The solution will still work with newer versions but it is encouraged to switch to standard method and avoid maintain multiple on-top components. In case of migration feel free to contact your account engineer to assists on the steps.

## Enable structured authentication with a single issuer

The minimal configuration enables the feature and declares one issuer. This is the recommended starting point when migrating to or adopting the feature.

```yaml
global:
  controlPlane:
    oidc:
      structuredAuthentication:
        enabled: true
        issuers:
          - issuerUrl: https://your-idp.example.com
            clientId: kubernetes
```

Apply the values to the cluster app and wait for the control plane rolling update to finish. Use [kubectl gs login]({{< relref "/reference/kubectl-gs/login/" >}}) to get access to the cluster API.

## Configure multiple OIDC providers

To trust more than one identity provider, add additional entries to the `issuers` list. Each entry is a self-contained issuer with its own client, claim mappings, and prefixes.

The following example trusts both an internal `Keycloak` instance for engineers and an external `Okta` tenant for contractors. Prefixes keep the two namespaces of identities separate so that RBAC bindings are unambiguous.

```yaml
global:
  controlPlane:
    oidc:
      structuredAuthentication:
        enabled: true
        issuers:
          - issuerUrl: https://keycloak.internal.example.com/realms/platform
            clientId: workload-cluster
            usernameClaim: email
            usernamePrefix: "keycloak:"
            groupsClaim: groups
            groupsPrefix: "keycloak:"
          - issuerUrl: https://example.okta.com
            clientId: 0oa1b2c3d4EXAMPLE
            usernameClaim: sub
            usernamePrefix: "okta:"
            groupsClaim: roles
            groupsPrefix: "okta:"
```

With this configuration, a user authenticated via `Keycloak` with `email=jane@example.com` and group `platform-admins` appears to the API server as user `keycloak:jane@example.com` in group `keycloak:platform-admins`. You can then bind that group to a role as usual:

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: keycloak-platform-admins
subjects:
  - kind: Group
    name: keycloak:platform-admins
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

See [binding roles]({{< relref "/tutorials/security/rbac#binding-role" >}}) for more examples of how to grant permissions to OIDC groups and users.

**Note**__**: Issuer URLs must be unique across the list. The API server rejects configurations with duplicate issuers.

## Claim mapping options

Each issuer entry supports the following basic fields:

| Field | Purpose |
|---|---|
| `issuerUrl` | The URL of the OIDC provider. Must match the `iss` claim in issued tokens. |
| `clientId` | The audience the API server expects to see in the token. |
| `usernameClaim` | The token claim used as the Kubernetes username. Defaults to `sub`. |
| `usernamePrefix` | Prefix added in front of the username. Set an explicit value to avoid collisions across issuers. |
| `groupsClaim` | The token claim used as the list of Kubernetes groups. |
| `groupsPrefix` | Prefix added in front of each group. |

Pick `email` as `usernameClaim` only if your IdP guarantees the claim is verified and immutable. Otherwise stick with `sub`, which is always stable.

## Advanced configuration

The `issuers` entries support the full set of options from the upstream `AuthenticationConfiguration` resource. The most common advanced fields are:

- `audiences` and `audienceMatchPolicy`: accept tokens issued for more than one audience, for example when a single client ID is shared across several components.
- `discoveryUrl`: point to a discovery endpoint whose host differs from the issuer URL. Typical when the issuer lives behind a reverse proxy.
- `caPem`: inline Privacy Enhanced Mail (PEM) encoded CA bundle for providers that use a private certificate authority.
- `claimValidationRules`: CEL expressions that must evaluate to `true` for a token to be accepted. Use this to require specific claims, enforce tenant IDs, or reject tokens without multi-factor authentication.
- `userValidationRules`: CEL expressions that run after the user object has been constructed. Useful to enforce invariants like `username must start with okta:`.
- `claimMappings`: advanced mappings that build usernames, groups, unique identifiers, and extra attributes from CEL expressions instead of plain claim names.

The following example requires an `mfa` claim with value `true` and extracts the username from the `preferred_username` claim:

```yaml
global:
  controlPlane:
    oidc:
      structuredAuthentication:
        enabled: true
        issuers:
          - issuerUrl: https://your-idp.example.com
            clientId: kubernetes
            audiences:
              - kubernetes
              - kubernetes-api
            audienceMatchPolicy: MatchAny
            claimValidationRules:
              - expression: 'claims.mfa == true'
                message: "Multi-factor authentication is required to access this cluster."
            claimMappings:
              username:
                expression: '"sso:" + claims.preferred_username'
              groups:
                expression: 'claims.roles'
```

For the full schema and semantics of these fields, refer to the [Kubernetes structured authentication documentation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration).

## Migrate from legacy OIDC configuration

If your cluster already uses the legacy `global.controlPlane.oidc` fields such as `issuerUrl` and `clientId`, you don't need to rewrite them. Add `structuredAuthentication.enabled: true` alongside the existing keys and the cluster app converts the legacy configuration to the new structured format automatically:

```yaml
global:
  controlPlane:
    oidc:
      issuerUrl: https://your-idp.example.com
      clientId: kubernetes
      structuredAuthentication:
        enabled: true
```

Once the rolling update completes and you have confirmed that existing users can still authenticate, you can move to the richer `issuers` list at your own pace, for example to add a second provider or CEL rules. The legacy top-level fields are ignored when `issuers` is set, so remove them at that point to keep the configuration unambiguous.

## Verify the configuration

After the control plane rolling update, sign in with a token from each configured issuer and check that the API server recognizes you with the expected identity:

```nohighlight
$ kubectl auth whoami
ATTRIBUTE         VALUE
Username          keycloak:jane@example.com
Groups            [keycloak:platform-admins system:authenticated]
```

You can impersonate the expected username to validate your RBAC bindings before handing the cluster to users:

```nohighlight
$ kubectl auth can-i get pods \
  --all-namespaces \
  --as "keycloak:jane@example.com" \
  --as-group "keycloak:platform-admins"
yes
```

If authentication fails, check the API server logs for entries from the `authentication` component. Typical failure modes are a mismatched `issuerUrl` (it must match the `iss` claim byte-for-byte), an audience mismatch, or a CEL rule that rejects the token.

## Further reading

- [Kubernetes structured authentication configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration)
- [Cluster access control with RBAC]({{< relref "/tutorials/security/rbac" >}})
- [Platform API authentication]({{< relref "/tutorials/access-management/authentication" >}})
