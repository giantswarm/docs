---
title: "gsctl Command Reference: delete endpoint"
description: "The 'gsctl delete endpoint' command deletes an endpoint that you previously used from the configuration."
date: "2020-05-13"
type: page
weight: 41
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

- [`gsctl login`](../login/)
- [`gsctl select endpoint`](../select-endpoint/)
- [`gsctl list endpoints`](../list-endpoints/)
