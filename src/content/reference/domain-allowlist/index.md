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

- alpinelinux.org
    - `*.alpinelinux.org`
- amazonaws.com
    - `*.amazonaws.com`
- cloudfront.net
    - `*.cloudfront.net`
- coreos.com
    - `*.coreos.com`
- docker.com
    - `*.docker.com`
- docker.io
    - `*.docker.io`
- flatcar.com
    - `*.flatcar.com`
- github.com
    - `*.github.com`
- github.io
    - `*.github.io`
- keybase.io
    - `*.keybase.io`
- quay.io
    - `*.quay.io`
- `api.opsgenie.com`
- `vault.operations.giantswarm.io`

In the case of on-premise installations, we also need access to the DNS provider. This is likely to be Cloudflare, but may be somewhere else.
