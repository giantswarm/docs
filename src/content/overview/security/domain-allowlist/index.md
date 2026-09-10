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
Giant Swarm clusters need outbound access to the external domains listed here to function. Use this page to configure your firewall, proxy, or egress policy.

## How to read this page

Everything in the [required domains](#required-domains) and [on-premise installations](#on-premise-installations) tables is HTTP or HTTPS traffic over TCP on port 443, unless specified otherwise.

Two flows aren't HTTP, so a conventional firewall can't match them by hostname. They have their own section, [non-HTTP traffic](#non-http-traffic).

Because a wildcard never covers the domain it belongs to, every base domain we also need access to gets its own row next to its wildcard.

## Required domains

| Domain | Why we need it |
|---|---|
| `alpinelinux.org` | Alpine container images may update their package index. |
| `*.alpinelinux.org` | Alpine container images may update their package index. |
| `amazonaws.com` | AWS services are used for a variety of tasks, such as `etcd` backup storage. |
| `*.amazonaws.com` | AWS services are used for a variety of tasks, such as `etcd` backup storage. |
| `azure.microsoft.com` | Container images and app catalogs are hosted on the Azure container registry. |
| `management.azure.com` | Azure API required by the Azure cloud controller manager. |
| `blob.core.windows.net` | The Azure container registry serves image layer blobs from Azure blob storage. |
| `*.blob.core.windows.net` | The Azure container registry serves image layer blobs from Azure blob storage. |
| `giantswarm.azurecr.io` | Container images and app catalogs are hosted on the Azure container registry. |
| `gsoci.azurecr.io` | Container images and app catalogs are hosted on the Azure container registry. |
| `gsociprivate.azurecr.io` | Container images and app catalogs are hosted on the Azure container registry. |
| `cloudfront.net` | Operators may pull from sites behind `Cloudfront`. |
| `*.cloudfront.net` | Operators may pull from sites behind `Cloudfront`. |
| `cronitor.io` | Cronitor's API is used to ensure our alerting pipeline is fully functional (heartbeat monitoring). |
| `cronitor.link` | Cronitor's API is used to ensure our alerting pipeline is fully functional (heartbeat monitoring). |
| `docker.com` | Container images are hosted on `Dockerhub`, which uses `Cloudflare` as the `CDN` for serving image layer blobs, manifests, and more. |
| `*.docker.com` | Container images are hosted on `Dockerhub`, which uses `Cloudflare` as the `CDN` for serving image layer blobs, manifests, and more. |
| `docker.io` | Container images are hosted on `Dockerhub`. |
| `*.docker.io` | Container images are hosted on `Dockerhub`. |
| `flatcar-linux.org` | Flatcar OS images and signing keys. |
| `*.flatcar-linux.org` | Flatcar OS images and signing keys. |
| `ghcr.io` | Official `Falco` rules are hosted at `ghcr.io/falcosecurity`. Optional if you turn off the official rulesets or host them elsewhere. |
| `github.com` | Various operators need to pull information from GitHub repositories. |
| `*.github.com` | Various operators need to pull information from GitHub repositories. |
| `github.io` | Helm chart tarballs are pulled from GitHub Pages. |
| `*.github.io` | Helm chart tarballs are pulled from GitHub Pages. |
| `pkg-containers.githubusercontent.com` | `Falco` optionally loads resources from this domain. |
| `raw.githubusercontent.com` | `Flux` applies some manifests from this domain. |
| `k8s.gcr.io` | (Legacy) Kubernetes container images are hosted on Google Container Registry. |
| `schema.giantswarm.io` | Our schema server hosts the schemas for container image validation. |
| `teleport.giantswarm.io` | Used to securely access Kubernetes clusters and to get SSH access to nodes. |
| `vault.operations.giantswarm.io` | Our operations Vault is used for unsealing customer Vault servers. |
| `storage.googleapis.com` | Google Container Registry is backed by a Google Cloud Storage bucket. |
| `grafana.com` | Grafana may download plugins from the Grafana plugin registry. |
| `grafana.net` | Some metrics are pushed to our hosted Grafana tenant. |
| `*.grafana.net` | Some metrics are pushed to our hosted Grafana tenant. |
| `grafana.org` | Some metrics are pushed to our hosted Grafana tenant. |
| `*.grafana.org` | Some metrics are pushed to our hosted Grafana tenant. |
| `registry.k8s.io` | Container registry and global `CDN` for the Kubernetes project's container images. |
| `api.letsencrypt.org` | cert-manager requests certificates from Let's Encrypt. |
| `*.api.letsencrypt.org` | cert-manager requests certificates from Let's Encrypt. |
| `graph.microsoft.com` | Used when logging into the cluster with Microsoft AD. |
| `login.microsoftonline.com` | Used when logging into the cluster with Microsoft AD. |
| `events.eu.pagerduty.com` | PagerDuty's API is used to send alerts. |
| `quay.io` | Container images are hosted on Quay. |
| `*.quay.io` | Container images are hosted on Quay. |
| `o346224.ingest.sentry.io` | Monitoring and crash reporting for `happa`. |
| `sigstore.dev` | Used to verify signatures on artifacts signed with the cosign keyless signing method. |
| `*.sigstore.dev` | Used to verify signatures on artifacts signed with the cosign keyless signing method. |
| `slack.com` | Used to send alerts to Slack channels. |
| `*.slack.com` | Used to send alerts to Slack channels. |
| `xpkg.upbound.io` | Used to fetch `Crossplane` packages. |

## On-premise installations

These domains are only required for on-premise installations. They're HTTP or HTTPS traffic, like the required domains.

| Domain | Why we need it |
|---|---|
| `api.cloudflare.com` | cert-manager may create ACME challenge DNS records. |

## Non-HTTP traffic

Clusters open two kinds of connection that don't carry an HTTP request, so there's no hostname for a proxy to read and match. Handle them like this:

- **If your firewall can resolve and match hostnames itself on non-HTTP traffic**, put the hostnames below on the allowlist, exactly as you would for an HTTP domain.
- **If it can't**, use the fallback described for each flow.

### SSH to `ssh.github.com`

| Hostname | Port | Protocol |
|---|---|---|
| `ssh.github.com` | 443 | SSH over TCP |

Fallback: We can tunnel this connection through the HTTP proxy with a `CONNECT` request to `ssh.github.com:443`. Apply the following patches to Flux's Source Controller:

```yaml
- op: add
  path: "/spec/template/spec/hostAliases/-"
  value:
    ip: "127.0.0.1"
    hostnames:
      - "ssh.github.com"
- op: add
  path: "/spec/template/spec/containers/-"
  value:
    name: proxy
    image: gsoci.azurecr.io/giantswarm/socat:1.7.4.4
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      runAsUser: 100
    command:
      - /bin/sh
      - -c
      - |
        # Fallback to static argument if injected env var doesn't exist
        export HTTP_PROXY=$${HTTP_PROXY:=${proxy_hostname}:${proxy_port}}

        export PROXY_HOSTNAME=$(echo $${HTTP_PROXY#http://} | cut -d":" -f1)
        export PROXY_PORT=$(echo $${HTTP_PROXY#http://} | cut -d":" -f2)

        socat TCP4-LISTEN:8081,fork,reuseaddr PROXY:$${PROXY_HOSTNAME}:ssh.github.com:443,proxyport=$${PROXY_PORT}
```

### NTP time synchronization

| Hostname | Port | Protocol |
|---|---|---|
| `0.flatcar.pool.ntp.org` | 123 | NTP over UDP |
| `1.flatcar.pool.ntp.org` | 123 | NTP over UDP |
| `2.flatcar.pool.ntp.org` | 123 | NTP over UDP |
| `3.flatcar.pool.ntp.org` | 123 | NTP over UDP |

Flatcar nodes synchronize their clock with the Flatcar NTP pool by default. Each `pool.ntp.org` hostname resolves to a rotating set of servers, so don't translate these names into static IP rules, which go stale.

Fallback: permit all outbound NTP traffic on port 123. If that's too broad for your policy, point the nodes at an NTP server you run yourself, through the cluster app's `timesyncd` values, and restrict egress to that server.
