---
linkTitle: update app
title: "'kubectl gs update app' command reference"
description: Reference documentation on how to update an app using the 'kubectl gs'.
weight: 100
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

# `kubectl gs update app`

This command helps with updating an in-cluster instance of the [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) custom resource.

## Usage

The command to execute is `kubectl gs update app`.

It supports the following required flags:

- `--name`: Name of the App CR to update.
- `--version`: New version to update the app to. The version package must exist in the `Catalog` storage.

See the example command updating the `starboard-app` to the `0.2.1` version:

```nohighlight
kubectl gs update app \
  --name starboard-app \
  --version 0.1.0
```

It produces the following output upon success:

```nohighlight
App starboard-app updated to version 0.1.0

```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
