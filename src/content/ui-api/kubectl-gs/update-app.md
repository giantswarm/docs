---
linkTitle: update app
title: "'kubectl gs update app' command reference"
description: Reference documentation on how to update an App CR using 'kubectl gs'.
weight: 120
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/update-app/
last_review_date: 2021-10-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I update an app version from the command line?
---

This command helps with updating [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) custom resources.

## Usage

The command to execute is `kubectl gs update app`.

It supports the following required flags:

- `--name`: Name of the App CR to update.
- `--version`: New version to update the app to. The version must exist in the [Catalog]({{< relref "/developer-platform/app-platform/overview/index.md#what-kind-of-app-catalogs-are-there" >}}).

**Important:** ensure you have selected the correct namespace for your cluster with the `--namespace` flag.

See the example command updating `starboard-app` to version `0.2.1`:

```nohighlight
kubectl gs update app \
  --name starboard-app \
  --namespace ab01c \
  --version 0.2.1
```

It produces the following output upon success:

```nohighlight
App 'starboard-app' updated to version '0.2.1'
```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
