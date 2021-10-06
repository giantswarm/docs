---
description: A list of all external domains Giant Swarm clusters need access to in order to function.
last_review_date: 2021-10-05
linkTitle: Domain allowlist
menu:
  main:
    parent: reference
owner:
  - https://github.com/orgs/giantswarm/teams/se
title: Domain allowlist
weight: 10
user_questions:
  - What domains do Giant Swarm clusters need access to?
---

# External Domains

Below is a list of the external domains we require access to for our clusters to function.

- flatcar.com
    - `*.flatcar.com`
- quay.io
    - `*.quay.io`
- github.com
    - `*.github.com`
- amazonaws.com
    - `*.amazonaws.com`
- docker.io
    - `*.docker.io`
- cloudfront.net
    - `*.cloudfront.net`
- keybase.io
    - `*.keybase.io`
- coreos.com
    - `*.coreos.com`
- docker.com
    - `*.docker.com`
- alpinelinux.org
    - `*.alpinelinux.org`
- `vault.operations.giantswarm.io`
- `api.opsgenie.com`

In the case of on-premise installations, we also need access to the DNS provider. This is likely to be Cloudflare, but may be somewhere else.
