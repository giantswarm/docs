---
linkTitle: Additional details
title: Additional details on authentication for the Management API
description: Here we provide additional information about single sign-on with the Management API.
weight: 30
menu:
  main:
    identifier: uiapi-managementapi-authentication-details
    parent: uiapi-managementapi-authentication
last_review_date: 2023-05-02
aliases:
  - /reference/management-api/authentication/additional-details
  - /ui-api/management-api/authentication/additional-details
user_questions:
  - How long do ID tokens live?
  - How can I refresh my groups memberships for Management API authorization?
  - How can I inspect the ID token issued for authenticating to the Management API?
  - What requirements are there to use single sign-on with the Management API?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

## Details of an ID token {#id-token-details}

Regardless of which login method is used, once this is done, the user's client (web UI, kubectl etc.) will send an ID token with every request to the Management API. The ID token contains information about the user which can then be used in [authorization]({{< relref "/vintage/use-the-api/management-api/authorization/index.md" >}}) to decide which permissions the user should be granted.

The ID token is a [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) (JWT). The payload part of an ID token issued for the Management API can look like in the following example. Note that we omit some parts that are not relevant for the purpose of this article.

```json
{
  "iss": "https://dex.g8s.garlic.eu-west-1.aws.gigantic.io",
  "exp": 1645533923,
  "iat": 1645532123,
  "email": "jane@example.com",
  "groups": [
    "customer:GiantSwarmAdmins"
  ],
  "name": "Jane Smith",
  "preferred_username": "janes",
  ...
}
```

Let's go into details for the most relevant properties (also called "claims") of this payload object.

| Claim | Description |
|-|-|
| `iss` | The OIDC provider that has issued the token. In our case it is Dex running in the management cluster.|
| `exp` | When this ID token expires, in seconds since 1970-01-01 00:00. Read [ID token lifetime](##id-token-ttl) below for more information. |
| `iat` | When this ID token has been issued, in seconds since 1970-01-01 00:00. |
| `email` | Email address associated with the authenticated user. From the Kubernetes api-server perspective, this is the user name relevant for role-based access control (RBAC). |
| `groups` | List of groups the user is a member of, provided by the identity provider. Note that group names are prefixed by Dex, usually prepending `customer:` to the original name of a group as defined in your identity provider. |
| `name` | Friendly name of the authenticated user. |
| `preferred_username` | Name to use as an identifier, as an alternative to the user's email address. |

## ID-token lifetime {#id-token-ttl}

By default, ID tokens for the Management API are issued with a lifetime of **{{% mapi_oidc_token_ttl_minutes %}} minutes**.

After that period, clients like `kubectl` will automatically attempt to get a fresh token from the identity provider. This does not require any additional user interaction. However, when this happens, the round-trip time for a `kubectl` command can be increased by a few seconds.

It is possible to configure a shorter token lifetime at the cost of more frequent delays due to token refreshing. Please contact your account engineer for assistance.

When assigning users to groups in your identity provider, and when removing users from groups, it can take up to {{% mapi_oidc_token_ttl_minutes %}} minutes until the change becomes effective for end users. If a user has authenticated and obtained an ID token before the change, tools like `kubectl` will use that token until it expires.

## Single sign-on requirements {#sso-requirements}

Giant Swarm assists all customers with setting up single sign-on (SSO) for the Management API. During that process, we make sure that these requirements are met:

- As a customer, you need to decide on an **identity provider** to use. Most enterprise-grade organizations have a solution already in place. Since we use [Dex](https://github.com/dexidp/dex) as a connector between the Management API and your identity provider, we can support a variety of common standards like OpenID Connect (OIDC) and LDAP.

    For cases where no suitable identity provider is available, or not yet available, we recommend to use GitHub, where an organization and teams can be set up and managed easily.

- Your identity provider must define a **group to be considered as admins** for the Giant Swarm installation. All members of this group automatically get administrative permissions when authenticating with the Management API.

## Further reading

- [Authentication for programmatic access]({{< relref "/vintage/use-the-api/management-api/authentication/automation" >}}) explains how to authenticate in an automation context
- [Authorization in the Management API]({{< relref "/vintage/use-the-api/management-api/authorization" >}}) explains how to assign permissions to authenticated users
