---
linkTitle: CoreDNS
title: Advanced CoreDNS configuration
description: Here we describe how you can customize the configuration of the managed CoreDNS service in your clusters.
weight: 35
menu:
  principal:
    parent: tutorials-connectivity
    identifier: tutorials-connectivity-coredns
aliases:
  - /advanced/connectivity/coredns
  - /guides/advanced-coredns-configuration/
  - /advanced/coredns/
user_questions:
  - How can I override the default CoreDNS configuration?
  - How can I customize the CoreDNS configuration?
  - How can I adjust resource limits for CoreDNS?
  - Where is the user values ConfigMap for CoreDNS?
  - How do I configure a different cache TTL per DNS zone?
  - How do I add an extra DNS zone to CoreDNS?
  - How do I migrate to the new CoreDNS values interface?
last_review_date: 2026-09-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

Your Giant Swarm clusters come with a default configuration for the [CoreDNS add-on](https://github.com/coredns/coredns). CoreDNS is installed as default application in your clusters using a [HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/). This guide explains how you can customize the CoreDNS configuration in your clusters.

## Before you start

This guide describes the zone-aware `coredns.*` values interface. You need cluster release **v35.0.0 or newer**, which ships coredns-app 1.32.0 on every provider. On older releases, see [migrating from the previous interface](#migration) for the keys that apply to you.

## Where to store the user configuration

Given the cluster you are trying to configure is called `123ab`, you can create or extend the `<CLUSTER>-user-values` ConfigMap of the organization namespace on the management cluster. Inside the ConfigMap, the Helm values are passed as the field called `values`:

```yaml
data:
  values: |
    global:
      apps:
        coreDns:
          values:
            coredns:
              ...
kind: ConfigMap
metadata:
  name: 123ab-userconfig
  namespace: org-my-org
```

Read more about [customizing default apps]({{< relref "/tutorials/fleet-management/app-platform/configuring-default-apps/" >}}).

Every example on this page shows only the `values` payload, so you have to nest it under `global.apps.coreDns.values` as in the snippet.

## How the configuration is organized

CoreDNS serves DNS through *server blocks*, one per zone. The chart renders three kinds of blocks, and each one is configured under its own key:

| Key | Server block | Purpose |
|---|---|---|
| `coredns.public` | `.` | Everything that isn't a local zone. Resolved through the `forward` plugin. |
| `coredns.cluster` | `cluster.local` | In-cluster service discovery. Resolved through the `kubernetes` plugin. |
| `coredns.additionalZones` | one per entry | Extra zones you define yourself. |
| `coredns.custom` | raw | A `Corefile` snippet appended verbatim. |

The important change compared to the previous interface: **cache, log, and load balancing are configured per zone**, not globally. Each of `coredns.public`, `coredns.cluster`, and every `coredns.additionalZones` entry carries its own `cache`, `log`, and `loadbalance`. So you can cache external answers for 5 minutes while keeping in-cluster answers fresh, or log every query for one zone only.

Zones that omit these keys fall back to the defaults: `success 9984 30` and `denial 9984 5` for cache, `denial` plus `error` for log, and `round_robin` for `loadbalance`.

## Cache settings

Cache lives under `<zone>.cache`. Positive and negative answers are tuned separately, each with a capacity and a time to live (TTL) in seconds. To raise the TTL of external answers to 60 seconds while leaving in-cluster answers at the default:

```yaml
coredns:
  public:
    cache:
      success:
        ttl: 60
```

To use a different TTL per zone:

```yaml
coredns:
  public:
    cache:
      success:
        capacity: 9984
        ttl: 60
      denial:
        capacity: 9984
        ttl: 10
  cluster:
    cache:
      success:
        ttl: 5
```

The chart also exposes `prefetch`, `serveStale`, `servfail`, `disable`, `keepttl`, `ttl`, and `zones`. For example, to fetch popular records again before they expire and serve stale answers while they refresh:

```yaml
coredns:
  public:
    cache:
      prefetch:
        amount: 2
        duration: 1m
      serveStale:
        enabled: true
        duration: 1h
        refreshMode: immediate
```

The cache plugin supports much more detailed configuration, which is documented in the [upstream documentation](https://coredns.io/plugins/cache/).

## Logs

By default we log the `denial` and `error` classes. `log` is a list of classes, set per zone:

```yaml
coredns:
  public:
    log:
      - all
```

To keep the default on external traffic but log everything in the cluster zone:

```yaml
coredns:
  cluster:
    log:
      - all
```

Valid classes are `success`, `denial`, `error`, and `all`. To learn more about each log class, read the [upstream documentation](https://coredns.io/plugins/log/).

## Load balancing

The `loadbalance` plugin shuffles A, AAAA, and MX records in the answer. Set it per zone to either `round_robin` or `random`:

```yaml
coredns:
  cluster:
    loadbalance: random
```

## Forwarding (formerly known as proxy) {#additional-forwards}

The default forward entry we set in CoreDNS is:

```text
forward . /etc/resolv.conf
```

List the upstreams under `coredns.public.forward.to`. They're selected in random order. Setting the list replaces the default, so include `/etc/resolv.conf` if you still want the cluster resolver as a fallback:

```yaml
coredns:
  public:
    forward:
      to:
        - 1.1.1.1
        - /etc/resolv.conf
```

This forwards all requests to 1.1.1.1, which is Cloudflare's DNS. If that upstream fails, requests are resolved by the default DNS provider set for your cluster. You can list several upstreams:

```yaml
coredns:
  public:
    forward:
      to:
        - 1.1.1.1
        - 8.8.8.8
        - /etc/resolv.conf
```

**Warning**: The number of forward upstreams is limited to 15.

Forward plugin options are siblings of `to` and each maps to one directive of the [upstream forward plugin](https://coredns.io/plugins/forward/):

```yaml
coredns:
  public:
    forward:
      to:
        - 9.9.9.9
      policy: round_robin
      forceTCP: true
      maxFails: 3
      healthCheck: 5s
      except:
        - example.internal
```

The full set of supported options is `except`, `forceTCP`, `preferUDP`, `expire`, `maxIdleConns`, `maxFails`, `maxConnectAttempts`, `dohMethod`, `tls`, `tlsServername`, `policy`, `healthCheck`, `maxConcurrent`, `next`, `nextOnNodata`, `failfastAllUnhealthyUpstreams`, `failover`, and `resolver`. Leave a key unset to keep the CoreDNS default.

## Search path expansion

The `autopath` plugin shortcuts search path expansion for pod queries. It applies to the public zone and is off by default:

```yaml
coredns:
  public:
    autopath: "@kubernetes"
```

## The cluster zone

`coredns.cluster` configures the `cluster.local` server block. The zone names and the reverse (PTR) ranges come from your cluster, so you don't normally need to set them:

```yaml
coredns:
  cluster:
    domains:
      - cluster.local
    serviceCIDR: 172.31.0.0/16
    podCIDR: 192.168.0.0/16
```

Kubernetes plugin parameters live under `coredns.cluster.kubernetes`. To expose only a subset of namespaces and return NXDOMAIN for services without ready endpoints:

```yaml
coredns:
  cluster:
    kubernetes:
      namespaces:
        - default
        - production
      ignoreEmptyService: true
      ttl: 30
```

The supported parameters are `pods`, `endpoint`, `tls`, `kubeconfig`, `apiserverQPS`, `apiserverBurst`, `apiserverMaxInflight`, `ttl`, `endpointPodNames`, `noendpoints`, `namespaces`, `namespaceLabels`, `labels`, `ignoreEmptyService`, `fallthrough`, `fallthroughZones`, `multicluster`, and `startupTimeout`. They map to the directives of the [upstream `kubernetes` plugin](https://coredns.io/plugins/kubernetes/).

## Additional zones

`coredns.additionalZones` renders one fully configured server block per entry. Each entry takes the same shape as `coredns.public` and `coredns.cluster`: `names` (required), plus optional `cidrs`, `cache`, `forward`, `kubernetes`, `log`, and `loadbalance`.

An entry that declares `kubernetes` resolves the zone through the Kubernetes API, which is what you want for a service mesh zone:

```yaml
coredns:
  additionalZones:
    - names:
        - linkerd.local
      kubernetes:
        pods: verified
```

An entry that declares `forward` sends the zone to a specific upstream, with its own cache and log settings:

```yaml
coredns:
  additionalZones:
    - names:
        - example.com
      forward:
        to:
          - 9.9.9.9
      cache:
        success:
          ttl: 2000
      log:
        - all
```

This resolves all `example.com` requests through a different upstream DNS resolver than the generic one, with a longer cache TTL. Because every zone is independent, adding one doesn't affect how the other zones behave.

## Raw configuration snippets

`coredns.additionalZones` covers most cases. When you need a directive the chart doesn't expose, `coredns.custom` is appended verbatim at the end of the `Corefile`:

```yaml
coredns:
  custom: |
    example.com:1053 {
      forward . 9.9.9.9
      cache 2000
    }
```

**Warning**: By default our clusters come with Pod Security Standards and network policies for managed components. This means the CoreDNS container doesn't use a privileged port and listens on `1053` instead. Please make sure you test the final `Corefile` carefully. We do not take responsibility for incorrect custom configuration that could break workload communication.

## Resource limits

We set resource limits for the CoreDNS deployment. For larger clusters these may need to be increased:

```yaml
resources:
  limits:
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 512Mi
```

## Migrating from the previous interface {#migration}

Before coredns-app 1.31.0, `Corefile` settings were spread across `configmap.*`, `loadbalancePolicy`, `additionalLocalZones`, and `cluster.*`, with no way to configure a zone individually. The table below maps every old key to its replacement.

| Old key | New key | Notes |
|---|---|---|
| `configmap.cache` | `coredns.public.cache.success.ttl`, `coredns.cluster.cache.success.ttl` | Now per zone. Integer, not a string. |
| `configmap.log` | `coredns.<zone>.log` | Now a list of classes instead of a newline-separated string. |
| `loadbalancePolicy` | `coredns.<zone>.loadbalance` | Now per zone. |
| `configmap.forward` | `coredns.public.forward.to` | Now a list of upstreams. The leading `.` is rendered for you, so drop it. |
| `configmap.forwardOptions` | `coredns.public.forward.<option>` | Each option is its own typed key, for example `policy` or `maxFails`. |
| `configmap.autopath` | `coredns.public.autopath` | |
| `configmap.custom` | `coredns.custom` | Unchanged shape. |
| `additionalLocalZones` | `coredns.additionalZones` | Now a list of zone objects instead of zone-name strings. |
| `cluster.kubernetes.clusterDomain` | `coredns.cluster.domains` | Now a list instead of a space-separated string. |
| `cluster.kubernetes.API.clusterIPRange` | `coredns.cluster.serviceCIDR` | |
| `cluster.calico.CIDR` | `coredns.cluster.podCIDR` | |
| `cluster.kubernetes.DNS.IP` | `service.clusterIP` | Moved out of the cluster topology, since it configures the DNS Service. |
| `userID` | `securityContext.runAsUser` | |
| `groupID` | `securityContext.runAsGroup` | |
| `ports.prometheus` | `ports.metrics.port` | Now an object, matching `ports.dns`. |
| `mastersInstance` | `controlPlane` | Same shape, clearer name. |

A worked example. This is the old form:

```yaml
configmap:
  cache: 60
  log: |
    all
  forward: . 1.1.1.1 8.8.8.8 /etc/resolv.conf
loadbalancePolicy: random
additionalLocalZones:
  - linkerd.local
```

And the same configuration in the new form:

```yaml
coredns:
  public:
    cache:
      success:
        ttl: 60
    log:
      - all
    loadbalance: random
    forward:
      to:
        - 1.1.1.1
        - 8.8.8.8
        - /etc/resolv.conf
  cluster:
    cache:
      success:
        ttl: 60
    log:
      - all
    loadbalance: random
  additionalZones:
    - names:
        - linkerd.local
      kubernetes:
        pods: verified
      log:
        - all
      loadbalance: random
```

Note how the old global keys have to be repeated per zone, including on the additional zone. The old `configmap.log` and `loadbalancePolicy` applied to every server block at once, so an equivalent migration has to set them on each zone you want to keep behaving the same way. That repetition is the point of the change: you're now free to give each zone different values.

**Warning**: `configmap.cache`, `configmap.log`, and `loadbalancePolicy` no longer take effect as of coredns-app 1.31.0. The per-zone keys ship with defaults that take precedence, so these three old keys are ignored without warning and your cluster runs the defaults instead. If you still set them, migrate now. The remaining old keys in the table keep working until coredns-app v2, but they're deprecated and will be removed then.

**Note**: `configmap.cache` was never applied to the `Corefile` before 1.31.0, so CoreDNS ran with the upstream default of 3600 seconds for positive answers. From 1.31.0 the cache block renders correctly, and the effective TTL is 30 seconds for positive and 5 seconds for negative answers. Raise `coredns.<zone>.cache.success.ttl` if your workloads depend on longer caching.

## Further reading

- [CoreDNS website](https://coredns.io/)
- [CoreDNS cache plugin](https://coredns.io/plugins/cache/)
- [CoreDNS forward plugin](https://coredns.io/plugins/forward/)
- [CoreDNS `kubernetes` plugin](https://coredns.io/plugins/kubernetes/)
- [coredns-app values reference](https://github.com/giantswarm/coredns-app/blob/main/helm/coredns-app/values.yaml)
