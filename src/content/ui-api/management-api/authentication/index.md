---
linkTitle: Authentication
title: Authentication for the Management API
description: How to authenticate for the Management API as a user using single sign-on, plus some information for admins regarding how to set up single sign-on with your own identity provider.
weight: 20
menu:
  main:
    identifier: uiapi-managementapi-authentication
    parent: uiapi-managementapi
last_review_date: 2021-05-31
user_questions:
  - How can I authenticate as a user to the Management API?
  - How can I inspect the ID token issued for authenticating to the Management API?
  - What requirements are there to use single sign-on with the Management API?
  - How can I refresh my groups memberships for Management API authorization?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
---

# Authentication for the Management API

Here we explain how you'll authenticate against the Management API as a user. Also on this page, we provide some information for customer admins regarding the requirements for the initial [single sign-on setup](#sso-requirements) and some [technical details](#technical-details) you might be interested in.

## Authenticating as a user {#user-auth}

As a user of the Management API for any given installation, you need

- A **user account** in the identity provider used by the installation (single sign-on).
- The Management API **endpoint URL** of the installation. Alternatively, the web user interface URL.

### Using `kubectl gs login` {#kubectl-gs-login}

Assuming that you want to work with the API using `kubectl`, we recommend you install the [Giant Swarm plug-in]({{< relref "/ui-api/kubectl-gs/_index.md" >}}) named `gs`. It can be [installed]({{< relref "/ui-api/kubectl-gs/installation/index.md" >}}) and updated using `krew`.

To set up your `kubectl` configuration with a context for your Giant Swarm installation's Management API, execute the following command:

```nohighlight
kubectl gs login <URL>
```

As a URL, use the Management API endpoint URL (normally starting with `https://g8s.`) or the web user interface URL (normally starting with `https://happa.g8s.`) of the installation.

More information can be found in the [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login/index.md" >}}) manual page.

[![Authentication flow](sso-auth-flow-with-kubectl-gs-login.svg)](sso-auth-flow-with-kubectl-gs-login.svg)

In order to complete the authentication flow, `kubectl gs` will open your default web browser. If in that browser you are authenticated with your identity provider (determined e.g. via a cookie), you will see a confirmation page and can close the browser window again. However, if you weren't authenticated with your identity provider yet, you'll have to go through the authentication process you are used to. When this is done, a confirmation page will be shown.

As a result of running the command, your `kubectl` configuration has a new context, user, and cluster entry. The context is named according to the pattern

```nohighlight
gs-<installation-name>
```

This context is selected automatically as the current context, so you are ready to use kubectl with the Management API.

When switching back to this context, it should not be necessary to go through the web-based authentication flow again. `kubectl` will automatically refresh the authentication token when needed, without your interaction.

### Alternative method

You can alternatively initiate the single sign-on authentication directly in a browser, without the need of installing the `kubectl gs` plug-in.

We provide a web-based login helper utility, available under a URL specific for each installation. If you have your installation's Management API endpoint URL, you can construct the utility's URL by prepending `login.` to the host name.

If, for example, your Management API URL is

```nohighlight
https://g8s.base.domain.tld
```

then the login utility can be accessed via

```nohighlight
https://login.g8s.base.domain.tld
```

The tool will immediately redirect you to your identity provider's authentication flow where you proceed providing your credentials as usual. After that, or if you are already authenticated in the current browser, you will be redirected to a resulting page.

The screenshot shows an example of that result page.

![Login helper screenshot](login-utility-results.png)

Here you can inspect the details that will be passed to the Management API as part of the ID token. You can use this to verify the details coming from your identity provider, especially the `email` (which is used as your user identifier) and `groups` claim.

This page will also present your Management API endpoint's certificate authority (CA) certificate. In order to connect to your Management API endpoint, you should add this CA certificate to your client's trusted (root) certificates.

The rest of the page helps you set up `kubectl` manually, adaptable for various operating systems.

## Authenticating for programmatic access {#service-auth}

For programmatic access, for example from CI/CD pipelines, you should not rely on the above authentication mechanism. Instead, please use [service accounts](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/).

Each Giant Swarm installation provides a service account named `automation` in the `default` namespace.

**Note:** This service account comes with a quite powerful set permissions. **We strongly recommend to create a specific service account for each application**, binding it to specific roles granting only the required permissions in the required namespaces.

## Single sign-on requirements {#sso-requirements}

Giant Swarm assists all customers with setting up single sign-on (SSO) for the Management API. During that process, we make sure that these requirements are met:

- As a customer, you need to decide on an **identity provider** to use. Most enterprise-grade organizations have a solution already in place. Since we use [Dex](https://github.com/dexidp/dex) as a connector between the Management API and your identity provider, we can support a variety of common standards like OpenID Connect (OIDC) and LDAP.

    For cases where no suitable identity provider is available, or not yet available, we recommend to use GitHub, where an organization and teams can be set up and managed easily.

- Your identity provider must define a **group to be considered as admins** for the Giant Swarm installation. All members of this group automatically get administrative permissions when authenticating with the Management API.

## Technical details {#technical-details}

### ID-token lifetime {#id-token-ttl}

By default, ID tokens for the Management API are issued with a lifetime of **{{% mapi_oidc_token_ttl_minutes %}} minutes**.

After that period, clients like `kubectl` will automatically attempt to get a fresh token from the identity provider. This does not require any additional user interaction. However, when this happens, the round-trip time for a `kubectl` command can be increased by a few seconds.

It is possible to configure a shorter token lifetime at the cost of more frequent delays due to token refreshing. Please contact your account engineer for assistance.

<!--

TODO: once we recommend assigning groups and users (non-admin MAPI users)

When assigning users to groups in your identity provider, and when removing users from groups, it can take up to {{% mapi_oidc_token_ttl_minutes %}} minutes until the change becomes effective for end users. If a user has authenticated and obtained an ID token before the change, tools like `kubectl` will use that token until it expires.

To force the adoption of up-to-date user information and group assignments, a user can manually remove the `id-token` value from the user entry in their `kubectl` configuration file.

-->
