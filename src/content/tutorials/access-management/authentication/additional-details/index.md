---
linkTitle: Additional details
title: Additional details on authentication for the platform API
description: Here we provide additional information about single sign-on with the platform API.
weight: 30
menu:
  principal:
    identifier: tutorials-access-management-authentication-details
    parent: tutorials-access-management-authentication
last_review_date: 2023-10-10
user_questions:
  - How long do ID tokens live?
  - How can I refresh my groups memberships for platform API authorization?
  - How can I inspect the ID token issued for authenticating to the platform API?
  - What requirements are there to use single sign-on with the platform API?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

## Resolving the Cluster Name with Management API

### Problem Statement

At times, you may encounter a scenario where the management API is not properly resolving the cluster name. If you are unsure what's causing the issue, it might be a situation with the RBAC, or it could rest with the API permissions. Below is a step-by-step workaround to tackle this problem.

### Instructions

To handle this potential hiccup:

1. First, you're advised to use the API address with `kubectl`. Here is an example: 
```bash
kubectl gs login <https://api.enigma.egg.gigantic.io> --workload-cluster w5o2x --organization egger --certificate-group system:masters --certificate-ttl 8h
```

2. In case this doesn't resolve the issue, check if the RBAC is present. To do this, you can run the command `kg rolebinding write-all-customer-group -n org-egger -o yaml`.

3. If the above steps don't seem to solve the issue, the problem could likely lie with the MC's api or the OIDC group id which might be hard coded or configured in multiple places.

### Detailed Workaround

1. Decrypt `egger dex-app` secret in `egger-configs`.

2. Under `oidc.customer.connectors` you'll see 2 entries. One with id `customer-developer` and one with `customer-azure`.

3. Replace `customer-developer` with just `customer`.

   As a reference, consider these examples: 
    ```bash
    id: customer-developers
    ```
   Modified to: 
    ```bash
    id: customer
    ```
4. After making the necessary changes, validate that the issue is resolved.

Remember, the existence of hard coding in the system could lead to such problems. In such scenarios, you are recommended to open an issue and communicate this to the team for further investigation and removal of hardcoded values.

## Details of the id token {#id-token-details}

Regardless of which login method is used, once this is done, the user's client (web UI, kubectl etc.) will send an ID token with every request to the platform API. The ID token contains information about the user which can then be used in [authorization]({{< relref "/tutorials/access-management/authorization/index.md" >}}) to decide which permissions the user should be granted.

The ID token is a [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) (JWT). The payload part of an ID token issued for the platform API can look like in the following example. Note that we omit some parts that aren't relevant for the purpose of this article.

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
| `iss` | The OIDC provider that has issued the token. In our case it's Dex running in the management cluster.|
| `exp` | When this ID token expires, in seconds since 1970-01-01 00:00. Read [ID token lifetime](##id-token-ttl) below for more information. |
| `iat` | When this ID token has been issued, in seconds since 1970-01-01 00:00. |
| `email` | Email address associated with the authenticated user. From the Kubernetes api-server perspective, this is the user name relevant for role-based access control (RBAC). |
| `groups` | List of groups the user is a member of, provided by the identity provider. Note that group names are prefixed by `dex`, usually prefixing `customer:` to the original name of a group as defined in your identity provider. |
| `name` | Friendly name of the authenticated user. |
| `preferred_username` | Name to use as an identifier, as an alternative to the user's email address. |

## Token lifetime {#id-token-ttl}

By default, ID tokens for the platform API are issued with a lifetime of {{% mapi_oidc_token_ttl_minutes %}} minutes.

After that period, clients like `kubectl` will automatically attempt to get a fresh token from the identity provider. This doesn't require any additional user interaction. However, when this happens, the round-trip time for a `kubectl` command can be increased by a few seconds.

It's possible to configure a shorter token lifetime at the cost of more frequent delays due to token refreshing. Please contact your account engineer for assistance.

When assigning users to groups in your identity provider, and when removing users from groups, it can take up to {{% mapi_oidc_token_ttl_minutes %}} minutes until the change becomes effective for end users. If a user has authenticated and obtained an ID token before the change, tools like `kubectl` will use that token until it expires.

## Single sign-on requirements {#sso-requirements}

Giant Swarm assists all customers with setting up single sign-on (SSO) for the platform API. During that process, we make sure that these requirements are met:

- As a customer, you need to decide on an identity provider to use. Most enterprise-grade organizations have a solution already in place. Since we use [Dex](https://github.com/dexidp/dex) as a connector between the platform API and your identity provider, we can support a variety of common standards like `OpenID Connect` (OIDC) and `LDAP`.

    For cases where no suitable identity provider is available, or not yet available, we recommend to use GitHub, where an organization and teams can be set up and managed easily.

- Your identity provider must define a group to be considered as admins for the Giant Swarm installation. All members of this group automatically get administrative permissions when authenticating with the platform API.

## Further reading

- [Authentication for programmatic access]({{< relref "/tutorials/access-management/authentication/automation" >}}) explains how to authenticate in an automation context
- [Authorization in the platform API]({{< relref "/tutorials/access-management/authorization" >}}) explains how to assign permissions to authenticated users