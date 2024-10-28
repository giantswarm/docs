---
linkTitle: As a user
title: Authentication for the platform API as a user
description: Here you learn how to log in to the platform API as a user, using single sign-on (SSO), to use tools like kubectl.
weight: 10
menu:
  main:
    identifier: tutorials-access-management-authentication-user
    parent: tutorials-access-management-authentication
last_review_date: 2024-10-28
user_questions:
  - How can I authenticate as a user to the platform API?
  - How can I authenticate to the platform API without kubectl-gs?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

As a user of the platform API for any given installation, you need:

- A **user account** in the identity provider used by the installation (single sign-on).
- The platform API **endpoint URL** of the installation. Alternatively, the web user interface URL.

For command-line access to the cluster using `kubectl`, authentication via our `kubectl` plugin is required. Detailed instructions are provided below. If you prefer a graphical interface, we also outline the Web UI login method.

## Using `kubectl gs login` {#kubectl-gs-login}

Assuming that you want to work with the API using `kubectl`, we recommend you install the [Giant Swarm plug-in]({{< relref "/vintage/use-the-api/kubectl-gs/_index.md" >}}) named `gs`. It can be [installed]({{< relref "/vintage/use-the-api/kubectl-gs/installation/index.md" >}}) and updated using `krew`.

To set up your `kubectl` configuration with a context for your Giant Swarm installation's platform API, execute the following command:

```sh
kubectl gs login URL
```

As a `URL` you use the platform API endpoint URL (normally starting with `https://g8s.`).

More information can be found in the [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) manual page.

[![Authentication flow](sso-auth-flow-with-kubectl-gs-login.svg)](sso-auth-flow-with-kubectl-gs-login.svg)

In order to complete the authentication flow, `kubectl gs` will open your default web browser. The page in the browser will prompt you to select an identity provider you want to use for the authentication. If you are authenticated with the identity provider you select (determined e.g. via a cookie), you will see a confirmation page and can close the browser window again. However, if you weren't authenticated with your identity provider yet, you'll have to go through the authentication process you are used to. When this is done, a confirmation page will be shown.

You can also execute the `login` command with the `--connector-id` flag, and specify an identifier of the desired connector (related to your preferred identity provider) for the authentication:

```sh
kubectl gs login URL --connector-id CONNECTOR_ID
```

As a result of running the command, your `kubectl` configuration has a new context, user, and cluster entry. The context is named according to the pattern

```text
gs-INSTALLATION_NAME
```

`INSTALLATION_NAME` is the unique name of your Giant Swarm installation.

This context is selected automatically as the current context, so you are ready to use kubectl with the platform API.

When switching back to this context, it should not be necessary to go through the web-based authentication flow again. `kubectl` will automatically refresh the authentication token when needed, without your interaction.

## Further reading

- [Authentication for programmatic access]({{< relref "/tutorials/access-management/authentication/automation" >}}) explains how to authenticate in an automation context
- [Technical details]({{< relref "/tutorials/access-management/authentication/additional-details" >}}) on authentication and single sign-on (SSO) for the platform API
- [Authorization in the platform API]({{< relref "/tutorials/access-management/authorization" >}}) explains how to assign permissions to authenticated users
