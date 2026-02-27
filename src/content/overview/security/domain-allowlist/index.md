---
title: Domain allowlist
description: A list of all external domains Giant Swarm clusters need access to in order to function.
weight: 40
menu:
  principal:
    parent: overview-security
user_questions:
  - What domains do Giant Swarm clusters need access to?
aliases:
  - /vintage/platform-overview/security/cluster-security/domain-allowlist/
  - /platform-overview/security/cluster-security/domain-allowlist
last_review_date: 2025-10-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
---

List of the external domains we require access to for our clusters to function.

- `alpinelinux.org`
    - domains:
        - `*.alpinelinux.org`
    - Alpine container images may update their package index.
- `amazonaws.com`
    - domains:
        - `*.amazonaws.com`
    - AWS services are used for a variety of tasks, such as `etcd` backup storage.
- `azurecr.io`
    - domains:
        - `giantswarm.azurecr.io`
        - `giantswarmpublic.azurecr.io`
        - `gsoci.azurecr.io`
        - `gsociprivate.azurecr.io`
        - `.blob.core.windows.net`
        - `azure.microsoft.com`
    - Container images and app catalogs are hosted on Azure container registry.
- `cloudfront.net`
    - domains:
        - `*.cloudfront.net`
    - Operators may pull from sites behind `Cloudfront`.
- `cronitor.io`
    - domains:
        - `cronitor.io`
        - `cronitor.link`
    - Cronitor's API is used to ensure our alerting pipeline is fully functional (heartbeat monitoring).
- `docker.com`
    - domains:
        - `*.docker.com`
    - Container images are hosted on `Dockerhub`.
    - `Dockerhub` uses `Cloudflare` as the `CDN` for serving Docker image layer blobs, manifests, etc.
- `docker.io`
    - domains:
        - `*.docker.io`
    - Container images are hosted on `Dockerhub`.
- `flatcar.com`
    - domains:
        - `*.flatcar-linux.org`
    - Flatcar OS images and signing keys.
- `ghcr.io`
    - domains:
        - `ghcr.io`
    - Official `Falco` rules are hosted at `ghcr.io/falcosecurity`. This domain is optional if official rulesets are disabled or hosted elsewhere.
- `github.com`
    - domains:
        - `*.github.com`
    - Various operators need to pull information from GitHub repositories.
- `github.io`
    - domains:
        - `*.github.io`
    - Helm chart tarballs are pulled from GitHub Pages.
- `githubusercontent.com`
    - domains:
        - `raw.githubusercontent.com`
        - `pkg-containers.githubusercontent.com`
    - `Flux` applies some manifests using the raw domain.
    - `Falco` optionally loads resources from the pkg-containers domain.
- `gcr.io`
    - domains:
        - `k8s.gcr.io`
    - (Legacy) k8s container images are hosted on Google Container Registry.
- `googleapis.com`
    - domains:
        - `storage.googleapis.com`
    - Google container registry is backed by a Google cloud storage bucket.
- `grafana.com`
    - domains:
        - `grafana.com`
    - Grafana may download plugins from the Grafana plugin registry.
- `grafana.net`
    - domains:
        - `*.grafana.net`
        - `*.grafana.org`
    - Some metrics are pushed to our hosted Grafana tenant.
- `giantswarm.io`
    - domains:
        - `vault.operations.giantswarm.io`
        - `schema.giantswarm.io`
    - Our operations Vault is used for unsealing customer Vault servers.
    - Our schema server hosts the schemas for container image validation.
- `k8s.io`
    - domains:
        - `registry.k8s.io`
    - Container registry and a global `CDN` for the k8s project’s container images.
- `letsencrypt.org`
    - domains:
        - `*.api.letsencrypt.org`
    - cert-manager will request certificates from Lets Encrypt.
- `microsoft.com`
    - domains:
        - `graph.microsoft.com`
    - Used when logging into the cluster with Microsoft AD.
- `microsoftonline.com`
    - domains:
        - `login.microsoftonline.com`
    - Used when logging into the cluster with Microsoft AD.
- `pagerduty.com`
    - domains:
        - `events.eu.pagerduty.com`
    - PagerDuty's API is used to send alerts.
- `quay.io`
    - domains:
        - `*.quay.io`
    - Container images are hosted on Quay.
- `sentry.io`
    - domains:
        - `o346224.ingest.sentry.io`
    - Monitoring and crash reporting for `happa`.
- `sigstore.dev`
    - domains:
        - `*.sigstore.dev`
    - Used for verifying signatures on artifacts signed with the cosign keyless signing method.
- `slack.com`
    - domains:
        - `*.slack.com`
    - Used to send alerts on slack channels
- `teleport.giantswarm.io`
    - domains:
        - `teleport.giantswarm.io`
    - Used to securely access Kubernetes cluster and SSH access to nodes.
- `xpkg.upbound.io`
    - domains:
        - `xpkg.upbound.io`
    - Used to fetch `Crossplane` packages.

## On-premise installations

These domains are only required for on-premise installations.

- `cloudflare.com`
    - domains:
        - `api.cloudflare.com`
    - cert-manager may create ACME challenge DNS records.
