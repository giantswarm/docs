---
linkTitle: delete endpoint
title: "'gsctl delete endpoint' command reference"
description: The 'gsctl delete endpoint' command deletes an endpoint that you previously used from the configuration.
weight: 90
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/delete-endpoint/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - How can I delete an endpoint from gsctl?
  - How can I delete an installation from gsctl?
---

# `gsctl delete endpoint`

The `gsctl delete endpoint` command deletes a Giant Swarm API endpoint that you previously used from your local gsctl configuration file.

## Usage

```nohighlight
gsctl delete endpoint <endpoint-url-or-alias>
```

Example:

```nohighlight
gsctl delete endpoint https://api.g8s.example.eu-central-1.aws.gigantic.io
```

A message will be printed letting you know if the endpoint has been deleted.

## Related

- [`gsctl login`]({{< relref "/ui-api/gsctl/login" >}})
- [`gsctl select endpoint`]({{< relref "/ui-api/gsctl/select-endpoint" >}})
- [`gsctl list endpoints`]({{< relref "/ui-api/gsctl/list-endpoints" >}})
