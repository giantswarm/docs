---
title: Advanced CoreDNS Configuration
description: Here we describe how you can customize the configuration of the managed CoreDNS service in your clusters
date: 2020-05-13
type: page
weight: 50
tags: ["tutorial"]
---

# Advanced CoreDNS Configuration

Your Giant Swarm installation comes with a default configuration for the [CoreDNS addon](https://github.com/coredns/coredns)

You can override these defaults in a ConfigMap named `coredns-user-values`.

## Where is the user values ConfigMap?

Given the cluster you are trying to configure has id: `123ab`

**Release Version 9.0.1 and greater:**

If your cluster is on release version `9.0.1` or greater then you will find the `coredns-user-values` ConfigMap on the Control Plane in the `123ab` namespace:

```nohighlight
$ kubectl -n 123ab get cm coredns-user-values --context=control-plane
NAME                                   DATA      AGE
coredns-user-values                    0         11m
```

**Release Version 9.0.0 and below:**

If the cluster has a release version equal to `9.0.0` or lower, then you will find the `coredns-user-values` ConfigMap on the Tenant Cluster itself in the `kube-system` namespace:

```nohighlight
$ kubectl -n kube-system get cm coredns-user-values --context=tenant-cluster
NAME                                   DATA      AGE
coredns-user-values         0         11m
```

-----

Upgrading from `9.0.0` to a higher release will automatically migrate these user values from the Tenant Cluster to the
Control Plane for you. If you have any automation or existing workflows you should keep this location change in mind.

------

__Warning:__

Please do not edit any other coredns related ConfigMaps.

Only the user values ConfigMap is safe to edit.

------

## How to set configuration options using the user values ConfigMap

### 9.0.1 and greater

On the Control Plane, create or edit a ConfigMap named `coredns-user-values`
in the Tenant Cluster namespace:

```yaml
# On the Control Plane, in the abc12 namespace
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: coredns
    name: coredns-user-values
    namespace: abc12
data:
  values: |
    configmap:
      cache: "60"

```

### 9.0.0 and below

On the Tenant Cluster for which you are trying to configure coredns,
create or edit a ConfigMap named `coredns-user-values` in the `kube-system`
namespace:

```yaml
# On the Tenant Cluster, in the kube-system namespace
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: coredns
    name: coredns-user-values
    namespace: kube-system
data:
  cache: "60"
```

## Configuration Reference

### Cache settings

By default we set the cache TTL for CoreDNS to 30 seconds. You can customize the cache settings of CoreDNS by setting the value of the cache field in the user ConfigMap like this:

```yaml
# 9.0.1 and greater
data:
  values: |
    configmap:
      cache: "60"

# 9.0.0 and below
data:
  cache: "60"
```

Above setting increases the TTL to 60 seconds.

The cache plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/cache/).

### Logs

By default, we set the log level for CoreDNS to `denial` and `error`. You can tune these settings by adding a property `log` in the user ConfigMap like this:

```yaml
# 9.0.1 and greater
data:
  values: |
    configmap:
      log: |
        all

# 9.0.0 and below
data:
  log: |
    all
```

To learn more about the exact details of each log level log plugin, please read the [upstream documentation](https://coredns.io/plugins/log/).

## Additional forwards (formerly known as proxy) {#additional-forwards}

The default forward entry we set in CoreDNS is

```yaml
forward . /etc/resolv.conf
```

You can add additional forward entries by adding each as a line to the forward field of the user values ConfigMap. They will be selected in random order.

You can use a simple line or multiple lines to define the upstreams of the default server block.

**Simple line:**
```yaml
# 9.0.1 and greater
data:
  values: |
    configmap:
      forward: . 1.1.1.1 /etc/resolv.conf

# 9.0.0 and below
data:
  forward: . 1.1.1.1 /etc/resolv.conf
```

**Multiple lines:**
```yaml
# 9.0.1 and greater
data:
  values: |
    forward: |
      .
      1.1.1.1
      8.8.8.8
      /etc/resolv.conf

# 9.0.0 and below
data:
  forward: |
    .
    1.1.1.1
    8.8.8.8
    /etc/resolv.conf
```

__Warning:__ The number of forward upstreams is limited to 15.

The example above results in the following additional forward entries in the CoreDNS configuration:

```yaml
forward . 1.1.1.1 /etc/resolv.conf
```

```yaml
forward . 1.1.1.1 8.8.8.8 /etc/resolv.conf
```

This setting would forward all requests to 1.1.1.1 which is Cloudflare's DNS. If the first upstream fails the second IP (8.8.8.8) will be used as resolver. In case it fails too, all requests will be resolved by the default DNS provider set for your cluster.

The forward plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/forward/).

__Notes:__ For releases using the CoreDNS chart in versions 1.1.3 and below, the upstreams must not include `.` and `/etc/resolv.conf` as they are rendered by the chart. They can be configured using simple or multiple lines:

**Simple lines:**
```yaml
# 9.0.1 and greater
data:
  values: |
    configmap:
      forward: 1.1.1.1 8.8.8.8

# 9.0.0 and below
data:
  forward: 1.1.1.1 8.8.8.8
```

**Multiple lines:**
```yaml
# 9.0.1 and greater
data:
  values: |
    configmap:
      forward: |
        1.1.1.1
        8.8.8.8

# 9.0.0 and below
data:
  forward:
    1.1.1.1
    8.8.8.8
```

### Advanced configuration

In case you need to have a finer granularity you can define custom server blocks with all desired configurations. They will be parsed after the catch-all block in the Corefile. As an example, let's define a block for a `example.com` with a custom configuration:

```yaml
# 9.0.1 and greater
data:
  values: |
    custom: |
      example.com:1053 {
        forward . 9.9.9.9
        cache 2000
      }

# 9.0.0 and below
data:
  custom: |
    example.com:1053 {
      forward . 9.9.9.9
      cache 2000
    }
```

This custom configuration allows CoreDNS to resolve all `example.com` requests to a different upstream DNS resolver (9.9.9.9) than the generic one. At the same time we use a different cache TTL(2000) setting.

__Warning:__ By default our clusters come with Pod Security Policies and Network Policies for managed components. This means the CoreDNS container doesn't use a privileged port and listens to `1053` instead. Please make sure you test the final `Corefile` carefully. We do not take responsibility for incorrect custom configuration that could break workload communication.

## Further reading

- [CoreDNS Website](https://coredns.io/)
- [CoreDNS cache plugin](https://coredns.io/plugins/cache/)
- [CoreDNS forward plugin](https://coredns.io/plugins/forward/)
