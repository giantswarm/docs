---
linkTitle: update app
title: "'kubectl gs update app' command reference"
description: Reference documentation on how to update an App CR using 'kubectl gs'.
weight: 120
menu:
  principal:
    parent: reference-kubectlgs
last_review_date: 2026-06-08
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How can I update an app version from the command line?
aliases:
  - /vintage/use-the-api/kubectl-gs/update-app/
---

**Deprecated:** This command updates the legacy `App` custom resource, which is being phased out in favor of Flux HelmRelease. For HelmRelease, update the chart version by editing the `OCIRepository`'s `spec.ref.tag` field; values are updated by editing the referenced ConfigMap or Secret. See [App management]({{< relref "/overview/fleet-management/app-management" >}}) for the conceptual overview.

This command helps with updating [App]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) custom resources.

## Usage

The command to execute is `kubectl gs update app`.

It supports the following required flags:

- `--name`: Name of the App CR to update.
- `--version`: New version to update the app to. The version must exist in the [Catalog]({{< relref "/overview/fleet-management/app-management" >}}).

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

- [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
