---
linkTitle: delete endpoint
title: "'gsctl delete endpoint' command reference"
description: The 'gsctl delete endpoint' command deletes an endpoint that you previously used from the configuration.
weight: 90
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /use-the-api/gsctl
  - /reference/gsctl/delete-endpoint/
  - /ui-api/gsctl/delete-endpoint/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I delete an endpoint from gsctl?
  - How can I delete an installation from gsctl?
last_review_date: 2023-03-06
---

{{% gsctl_deprecation_disclaimer %}}

The `gsctl delete endpoint` command deletes a Giant Swarm REST API endpoint that you previously used from your local gsctl configuration file.

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

- [`gsctl login`]({{< relref "/vintage/use-the-api/gsctl/login" >}})
- [`gsctl select endpoint`]({{< relref "/vintage/use-the-api/gsctl/select-endpoint" >}})
- [`gsctl list endpoints`]({{< relref "/vintage/use-the-api/gsctl/list-endpoints" >}})
