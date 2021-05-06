---
linkTitle: Domain whitelist
title: Domain whitelist
description: A list of all external domains Giant Swarm clusters need access to.
weight: 10
menu:
  main:
    parent: reference
user_questions:
  - What domains do Giant Swarm clusters need access to?
owner:
  - https://github.com/orgs/giantswarm/teams/se
---

# External Domains

Below is a list of the external domains we require access to for our clusters to function.

- flatcar.com
    - *.flatcar.com
- quay.io
    - *.quay.io
- github.com
    - *.github.com
- amazonaws.com
    - *.amazonaws.com
- docker.io
    - *.docker.io
- cloudfront.net
    - *.cloudfront.net
- keybase.io
    - *.keybase.io
- coreos.com
    - *.coreos.com
- docker.com
    - *.docker.com
- alpinelinux.org
    - *.alpinelinux.org
- vault.operations.giantswarm.io

In the case of on-premise installations, we also need access to the DNS provider. This is likely to be Cloudflare, but may be somewhere else.
