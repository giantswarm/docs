---
title: "gsctl Reference: Configuration file"
description: "Documentation of the configuration file format of gsctl"
date: "2020-05-14"
type: page
weight: 1000
---

# Configuration file

gsctl by default stores its configuration in a YAML file located at
`$HOME/.config/gsctl/config.yaml`.

**Warning:** gsctl frequently overwrites its configuration file. If you
manually edit the file, some edits unknown to gsctl, like comments for example,
will get lost.

## Example

```yaml
endpoints:
  http://localhost:9000:
    alias: local
    email: developer@example.com
    token: 7d5b1161-87e6-4dfd-8017-5ab9f4e1cb14
  https://api.g8s.cloud.europe.gigantic.io:
    alias: cloud
    email: developer@example.com
    token: 103dc680-1b53-4ad3-b5cb-ac9b2f86134d
  https://api.g8s.onprem.example.com:
    alias: onprem
    email: developer@example.com
    token: ""
selected_endpoint: https://api.g8s.cloud.europe.gigantic.io
last_version_check: 2018-01-25T13:50:25.353937+01:00
updated: 2018-01-26T09:17:24+01:00
```

## Schema description

- `endpoints`: All API endpoint known to gsctl are sub-entries of this key.
  Each entry has the canonical endpoint URL as a key. The following attributes
  are allowed per endpoint entry:
  - `alias`: Shorthand for selecting the endpoint. This must be unique within
    the configuration.
  - `email`: Email used for authentication with this endpoint.
  - `token`: Authentication token used with this endpoint.
- `selected_endpoint`: The currently selected endpoint URL. Can be empty.
- `last_version_check`: Date and time gsctl has last checked for a newer
  gsctl version (when calling `gsctl --version`).
- `updated`: Date and time when the configuration file has been modified.
