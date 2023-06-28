---
description: A list of all external domains Giant Swarm clusters need access to in order to function.
last_review_date: 2022-12-07
linkTitle: Domain allowlist
menu:
  main:
    parent: platform-overview-security-cluster
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
title: Domain allowlist
weight: 40
user_questions:
  - What domains do Giant Swarm clusters need access to?
aliases:
  - /security/domain-allowlist
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
        - `ec2.eu-west-2.amazonaws.com`
        - `sts.eu-central-1.amazonaws.com`
    - AWS services are used for a variety of tasks, such as etcd backup storage.
- azurecr.io
    - domains:
        - `giantswarm.azurecr.io`
        - `giantswarmpublic.azurecr.io`
    - Container images and app catalogs are hosted on Azure Container Registry.
- auth0.com
    - domains:
        - `giantswarm.eu.auth0.com`
    - Used to secure access to Grafana and Prometheus.
- cloudfront.net
    - domains:
        - `*.cloudfront.net`
    - Operators may pull from sites behind Cloudfront.
- docker.com
    - domains:
        - `*.docker.com`
        - `production.cloudflare.docker.com`
    - Container images are hosted on Dockerhub.
    - Dockerhub uses Cloudflare as the CDN for serving Docker Image layer blobs, manifests, etc.
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
- githubusercontent.com
    - domains:
      - `raw.githubusercontent.com`
    - Flux applies some manifests using the raw domain. 
- gcr.io
    - domains:
        - `k8s.gcr.io`
    - (Legacy) K8s container images are hosted on Google Container Registry.
- googleapis.com
    - domains:
        - `storage.googleapis.com`
    - Google Container Registry is backed by a Google cloud storage bucket.
- grafana.com
    - domains:
        - `grafana.com`
    - Grafana may download plugins from the Grafana plugin registry.
- grafana.net
    - domains:
        - `prometheus-us-central1.grafana.net`
    - Some metrics are pushed to our hosted Grafana tenant.
- giantswarm.io
    - domains:
        - `vault.operations.giantswarm.io`
        - `schema.giantswarm.io`
    - Our operations Vault is used for unsealing customer Vault servers.
    - Our schema server hosts the schema's for container image validation.
- k8s.io
    - domains:
        - `registry.k8s.io`
    - Container registry and a global CDN for the K8s project’s container images.
- keybase.io
    - domains:
        - `*.keybase.io`
    - Vault initialisation and unsealing requires access to Keybase.
- letsencrypt.org
    - domains:
        - `*.api.letsencrypt.org`
    - cert-manager will request certificates from Lets Encrypt.
- microsoft.com
    - domains:
      - `graph.microsoft.com`
    - Used when logging into the cluster with Microsoft AD.
- microsoftonline.com
    - domains:
      - `login.microsoftonline.com`
    - Used when logging into the cluster with Microsoft AD.
- opsgenie.com
    - domains:
        - `api.opsgenie.com`
    - Opsgenie's API is used to send alerts.
- quay.io
    - domains:
        - `*.quay.io`
    - Container images are hosted on Quay.
- sentry.io
    - domains:
        - `o346224.ingest.sentry.io`
    - Monitoring and crash reporting for `happa`.
- slack.com
    - domains:
        - `hooks.slack.com`
    - Used to send alerts on slack channels

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
