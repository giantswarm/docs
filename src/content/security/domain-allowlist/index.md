---
description: A list of all external domains Giant Swarm clusters need access to in order to function.
last_review_date: 2021-10-05
linkTitle: Domain allowlist
menu:
  main:
    parent: security
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
title: Domain allowlist
weight: 40
user_questions:
  - What domains do Giant Swarm clusters need access to?
aliases:
  - /reference/domain-allowlist/
---

Below is a list of the external domains we require access to for our clusters to function.

- alpinelinux.org
    - domains:
        - `*.alpinelinux.org`
    - Alpine container images may update their package index.
- amazonaws.com
    - domains:
        - `*.amazonaws.com`
    - AWS services are used for a variety of tasks, such as etcd backup storage.
- azurecr.io
    - domains:
        - `giantswarm.azurecr.io`
    - Container images are hosted on Azure Container Registry.
- cloudfront.net
    - domains:
        - `*.cloudfront.net`
    - Operators may pull from sites behind Cloudfront.
- docker.com
    - domains:
        - `*.docker.com`
    - Container images are hosted on Dockerhub.
- docker.io
    - domains:
        - `*.docker.io`
    - Container images are hosted on Dockerhub.
- flatcar.com
    - domains:
        - `*.flatcar-linux.org`
    - Flatcar OS images and signing keys.
- github.com
    - domains:
        - `*.github.com`
    - Various operators need to pull information from GitHub repositories.
- github.io
    - domains:
        - `*.github.io`
    - Helm chart tarballs are pulled from GitHub Pages.
- keybase.io
    - domains:
        - `*.keybase.io`
    - Vault initialisation and unsealing requires access to Keybase.
- letsencrypt.org
    - domains:
        - `*.api.letsencrypt.org`
    - cert-manager will request certificates from Lets Encrypt.
- quay.io
    - domains:
        - `*.quay.io`
    - Container images are hosted on Quay.
- sentry.io
    - domains:
        - `o346224.ingest.sentry.io`
    - Monitoring and crash reporting for `happa`.
- `api.opsgenie.com`
    - Opsgenie's API is used to send alerts.
- `grafana.com`
    - Grafana may download plugins from the Grafana plugin registry.
- `prometheus-us-central1.grafana.net`
    - Some metrics are pushed to our hosted Grafana tenant.
- `vault.operations.giantswarm.io`
    - Our operations Vault is used for unsealing customer Vault servers.

## On-premise installations

These domains are only required for on-premise installations.

- cloudflare.com
    - domains:
        - `api.cloudflare.com`
    - cert-manager may create ACME challenge DNS records.
- api.mailgun.net
    - domains:
        - `api.mailgun.net`
    - This is the mail service we use to send the invites for our Rest API user accounts.
