---
title: "'kubectl gs login' command reference"
description: Reference documentation on how to ensure an authenticated kubectl context for a Giant Swarm management cluster, using 'kubectl gs'.
type: page
weight: 10
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `kubectl gs login`

{{% kgs_alias_assumption %}}

This command allows to ensure an authenticated kubectl context is selected.

## Usage

The command is called with the general syntax

```nohighlight
kubectl gs login [argument]
```

where `argument` can be either:

- **Empty:** If the current kubectl context is a Giant Swarm management cluster, this ensures that the OIDC auth token will be refreshed and show the name of the current context.

- **Web interface URL:** The URL of the management cluster's [web UI](/reference/web-interface/) instance.

- **Management Cluster API endpoint:** The URL of the management cluster's Kubernetes API endpoint.

- **Context name:** Name of a Giant Swarm management cluster kubectl context, with or without `gs-` prefix.

## Examples

Using the Web URL as an argument:

```nohighlight
kubectl gs login https://happa.g8s.gattaca.westeurope.azure.gigantic.io
```
