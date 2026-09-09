---
title: Domain allowlist
diataxis_content_type: reference
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
last_review_date: 2026-09-04
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
---

Giant Swarm clusters need outbound access to the external domains listed here to function. Use this page to configure your firewall, proxy, or egress policy. Every entry is an outbound connection initiated from the cluster.

## Required domains

| Domain | Ports | Protocol | Why we need it |
|---|---|---|---|
| `alpinelinux.org` | 443 | HTTPS | Alpine container images may update their package index. |
| `*.alpinelinux.org` | 443 | HTTPS | Alpine container images may update their package index. |
| `amazonaws.com` | 443 | HTTPS | AWS services are used for a variety of tasks, such as `etcd` backup storage. |
| `*.amazonaws.com` | 443 | HTTPS | AWS services are used for a variety of tasks, such as `etcd` backup storage. |
| `azure.microsoft.com` | 443 | HTTPS | Container images and app catalogs are hosted on the Azure container registry. |
| `management.azure.com` | 443 | HTTPS | Azure API required by the Azure cloud controller manager. |
| `blob.core.windows.net` | 443 | HTTPS | The Azure container registry serves image layer blobs from Azure blob storage. |
| `*.blob.core.windows.net` | 443 | HTTPS | The Azure container registry serves image layer blobs from Azure blob storage. |
| `giantswarm.azurecr.io` | 443 | HTTPS | Container images and app catalogs are hosted on the Azure container registry. |
| `gsoci.azurecr.io` | 443 | HTTPS | Container images and app catalogs are hosted on the Azure container registry. |
| `gsociprivate.azurecr.io` | 443 | HTTPS | Container images and app catalogs are hosted on the Azure container registry. |
| `cloudfront.net` | 443 | HTTPS | Operators may pull from sites behind `Cloudfront`. |
| `*.cloudfront.net` | 443 | HTTPS | Operators may pull from sites behind `Cloudfront`. |
| `cronitor.io` | 443 | HTTPS | Cronitor's API is used to ensure our alerting pipeline is fully functional (heartbeat monitoring). |
| `cronitor.link` | 443 | HTTPS | Cronitor's API is used to ensure our alerting pipeline is fully functional (heartbeat monitoring). |
| `docker.com` | 443 | HTTPS | Container images are hosted on `Dockerhub`, which uses `Cloudflare` as the `CDN` for serving image layer blobs, manifests, and more. |
| `*.docker.com` | 443 | HTTPS | Container images are hosted on `Dockerhub`, which uses `Cloudflare` as the `CDN` for serving image layer blobs, manifests, and more. |
| `docker.io` | 443 | HTTPS | Container images are hosted on `Dockerhub`. |
| `*.docker.io` | 443 | HTTPS | Container images are hosted on `Dockerhub`. |
| `flatcar-linux.org` | 443 | HTTPS | Flatcar OS images and signing keys. |
| `*.flatcar-linux.org` | 443 | HTTPS | Flatcar OS images and signing keys. |
| `ghcr.io` | 443 | HTTPS | Official `Falco` rules are hosted at `ghcr.io/falcosecurity`. Optional if you turn off the official rulesets or host them elsewhere. |
| `github.com` | 443 | HTTPS | Various operators need to pull information from GitHub repositories. |
| `*.github.com` | 443 | HTTPS | Various operators need to pull information from GitHub repositories. |
| `ssh.github.com` | 22, 443 | SSH | Git repositories accessed over SSH, for example `Flux` sources using an `ssh://` URL. GitHub serves SSH on port 443 (as well as 22) through this hostname. |
| `github.io` | 443 | HTTPS | Helm chart tarballs are pulled from GitHub Pages. |
| `*.github.io` | 443 | HTTPS | Helm chart tarballs are pulled from GitHub Pages. |
| `pkg-containers.githubusercontent.com` | 443 | HTTPS | `Falco` optionally loads resources from this domain. |
| `raw.githubusercontent.com` | 443 | HTTPS | `Flux` applies some manifests from this domain. |
| `k8s.gcr.io` | 443 | HTTPS | (Legacy) Kubernetes container images are hosted on Google Container Registry. |
| `schema.giantswarm.io` | 443 | HTTPS | Our schema server hosts the schemas for container image validation. |
| `teleport.giantswarm.io` | 443 | HTTPS | Used to securely access Kubernetes clusters and to get SSH access to nodes. |
| `vault.operations.giantswarm.io` | 443 | HTTPS | Our operations Vault is used for unsealing customer Vault servers. |
| `storage.googleapis.com` | 443 | HTTPS | Google Container Registry is backed by a Google Cloud Storage bucket. |
| `grafana.com` | 443 | HTTPS | Grafana may download plugins from the Grafana plugin registry. |
| `grafana.net` | 443 | HTTPS | Some metrics are pushed to our hosted Grafana tenant. |
| `*.grafana.net` | 443 | HTTPS | Some metrics are pushed to our hosted Grafana tenant. |
| `grafana.org` | 443 | HTTPS | Some metrics are pushed to our hosted Grafana tenant. |
| `*.grafana.org` | 443 | HTTPS | Some metrics are pushed to our hosted Grafana tenant. |
| `registry.k8s.io` | 443 | HTTPS | Container registry and global `CDN` for the Kubernetes project's container images. |
| `api.letsencrypt.org` | 443 | HTTPS | cert-manager requests certificates from Let's Encrypt. |
| `*.api.letsencrypt.org` | 443 | HTTPS | cert-manager requests certificates from Let's Encrypt. |
| `graph.microsoft.com` | 443 | HTTPS | Used when logging into the cluster with Microsoft AD. |
| `login.microsoftonline.com` | 443 | HTTPS | Used when logging into the cluster with Microsoft AD. |
| `0.flatcar.pool.ntp.org` | 123 | NTP (UDP) | Flatcar nodes synchronize their clock with the Flatcar NTP pool. |
| `1.flatcar.pool.ntp.org` | 123 | NTP (UDP) | Flatcar nodes synchronize their clock with the Flatcar NTP pool. |
| `2.flatcar.pool.ntp.org` | 123 | NTP (UDP) | Flatcar nodes synchronize their clock with the Flatcar NTP pool. |
| `3.flatcar.pool.ntp.org` | 123 | NTP (UDP) | Flatcar nodes synchronize their clock with the Flatcar NTP pool. |
| `events.eu.pagerduty.com` | 443 | HTTPS | PagerDuty's API is used to send alerts. |
| `quay.io` | 443 | HTTPS | Container images are hosted on Quay. |
| `*.quay.io` | 443 | HTTPS | Container images are hosted on Quay. |
| `o346224.ingest.sentry.io` | 443 | HTTPS | Monitoring and crash reporting for `happa`. |
| `sigstore.dev` | 443 | HTTPS | Used to verify signatures on artifacts signed with the cosign keyless signing method. |
| `*.sigstore.dev` | 443 | HTTPS | Used to verify signatures on artifacts signed with the cosign keyless signing method. |
| `slack.com` | 443 | HTTPS | Used to send alerts to Slack channels. |
| `*.slack.com` | 443 | HTTPS | Used to send alerts to Slack channels. |
| `xpkg.upbound.io` | 443 | HTTPS | Used to fetch `Crossplane` packages. |

The NTP entries are the Flatcar defaults. Each `pool.ntp.org` hostname resolves to a rotating set of servers, so use the hostnames in your firewall rules rather than IP addresses. If you point the nodes at your own NTP servers through the cluster app's `timesyncd` values, use those domains instead of these four.

## On-premise installations

These domains are only required for on-premise installations.

| Domain | Ports | Protocol | Why we need it |
|---|---|---|---|
| `api.cloudflare.com` | 443 | HTTPS | cert-manager may create ACME challenge DNS records. |
