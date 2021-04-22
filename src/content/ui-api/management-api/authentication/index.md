---
linkTitle: Authentication
title: Authentication for the Management API
description: How to authenticate for the management API as a user using single sign-on, plus some information for admins regarding how to set up single sign-on with your own identity provider.
weight: 20
menu:
  main:
    identifier: uiapi-managementapi-authentication
    parent: uiapi-managementapi
---

# Authentication for the Management API

Here we explain how you'll authenticate against the management API as a user. For admins, we provide guidance regarding your own identity provider and initial authorization setup, to permit user access.

## Authenticating as a user {#user-auth}

As a user of the management API for any given installation, you need

- A **user account** in the customer's identity provider (single sign-on).
- The management API **endpoint URL** of the installation. Alternatively, the web user interface URL.

### Using kubectl gs login

Assuming that you want to work with the API using `kubectl`, the easiest method to authenticate is using the [Giant Swarm plug-in]({{< relref "/ui-api/kubectl-gs/_index.md" >}}) named `gs`. It can be [installed]({{< relref "/ui-api/kubectl-gs/installation/index.md" >}}) easily using `krew` and is recommended for all users of the management API.

To set up your `kubectl` configuration file, execute the following command:

```nohighlight
kubectl gs login <URL>
```

As a URL, use the management API endpoint URL (normally starting with `https://g8s.`) or the web user interface URL (normally starting with `https://happa.g8s.`) of the installation.

More information can be found in the [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login/index.md" >}}) manual page.

[![Authentication flow](sso-auth-flow-with-kubectl-gs-login.svg)](sso-auth-flow-with-kubectl-gs-login.svg)

In order to complete the authentication flow, `kubectl gs` will open your default web browser. If in that browser you are authenticated with your identity provider (determined e. g. via a cookie), you will see a confirmation page and can close the browser window again. However, if you weren't authenticated with your identity provider yet, you'll have to go through the authentication process you are used to. When this is done, a confirmation page will be shown.

As a result of running the command, your `kubectl` configuration has a new context, user, and cluster entry. The context is named according to the pattern

```nohighlight
gs-<installation-name>
```

This context is selected automatically as the current context, so you should be ready to use kubectl with the management API.

When switching back to this context, it should not be necessary to go through the web-based authentication flow again. `kubectl` will automatically refresh the authentication token when needed, without your interaction.

### Alternative method

You can alternatively initiate the single sign-on authentication directly in a browser, without a need to install the `kubectl` plug-in.

- When not using the plugin, you need to obtain the certificate authority (CA) certificate of the management API and either add it to your cluster entry in kubeconfig or import it to the system as trusted.



## Identity provider requirements {#todo}

- Need one group defining admins.
- Should have additional groups defining the user types which should get more restricted access to the Management API
