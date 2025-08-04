---
linkTitle: CoreDNS
title: Advanced CoreDNS configuration
description: Here we describe how you can customize the configuration of the managed CoreDNS service in your clusters.
weight: 25
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
last_review_date: 2025-08-04
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

Your Giant Swarm clusters come with a default configuration for the [CoreDNS addon](https://github.com/coredns/coredns). CoreDNS is installed as default application in your clusters using a [HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/). This guide explains how you can customize the CoreDNS configuration in your clusters.

## Where to store the user configuration

Given the cluster you are trying to configure is called: `123ab` you can create or extend the `<CLUSTER>-user-values` ConfigMap of the organization namespace on the management cluster. Inside the ConfigMap, the Helm values are passed as the field called `values` which lets you define a

```yaml
data:
  values: |
    global:
      ...
kind: ConfigMap
metadata:
  name: 123ab-user-values
  namespace: org-my-org
```

More information about cluster configuration[here](https://docs.giantswarm.io/tutorials/fleet-management/app-platform/configuring-default-apps/).

## Configuration Reference

### Cache settings

By default we set the cache TTL for CoreDNS to 30 seconds. You can customize the cache settings of CoreDNS by setting the value of the cache field in the user ConfigMap like this:

```yaml
data:
  values: |
    configmap:
      cache: "60"
```

Above setting increases the TTL to 60 seconds.

The cache plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/cache/).

### Logs

By default, we set the log level for CoreDNS to `denial` and `error`. You can tune these settings by adding a property `log` in the user ConfigMap like this:

```yaml
data:
  values: |
    configmap:
      log: |
        all
```

To learn more about the exact details of each log level log plugin, please read the [upstream documentation](https://coredns.io/plugins/log/).

### Resource limits

We set resource limits for the CoreDNS deployment. For larger clusters these may need to be increased. This can be done in the user ConfigMap like this:

```yaml
data:
  values: |
    resources:
      limits:
        memory: 512Mi
      requests:
        cpu: 250m
        memory: 512Mi
```

## Additional forwards (formerly known as proxy) {#additional-forwards}

The default forward entry we set in CoreDNS is

```yaml
forward . /etc/resolv.conf
```

You can add additional forward entries by adding each as a line to the forward field of the user values ConfigMap. They will be selected in random order.

You can use a simple line or multiple lines to define the upstreams of the default server block.

**Simple line:**

```yaml
data:
  values: |
    configmap:
      forward: . 1.1.1.1 /etc/resolv.conf
```

**Multiple lines:**

```yaml
data:
  values: |
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
data:
  values: |
    configmap:
      forward: 1.1.1.1 8.8.8.8
```

**Multiple lines:**

```yaml
data:
  values: |
    configmap:
      forward: |
        1.1.1.1
        8.8.8.8
```

### Advanced configuration

In case you need to have a finer granularity you can define custom server blocks with all desired configurations. They will be parsed after the catch-all block in the `Corefile`. As an example, let's define a block for a `example.com` with a custom configuration:

```yaml
data:
  values: |
    configmap:
      custom: |
        example.com:1053 {
          forward . 9.9.9.9
          cache 2000
        }
```

This custom configuration allows CoreDNS to resolve all `example.com` requests to a different upstream DNS resolver (9.9.9.9) than the generic one. At the same time we use a different cache TTL(2000) setting.

__Warning:__ By default our clusters come with Pod Security Standards and Network Policies for managed components. This means the CoreDNS container doesn't use a privileged port and listens to `1053` instead. Please make sure you test the final `Corefile` carefully. We do not take responsibility for incorrect custom configuration that could break workload communication.

## Further reading

- [CoreDNS Website](https://coredns.io/)
- [CoreDNS cache plugin](https://coredns.io/plugins/cache/)
- [CoreDNS forward plugin](https://coredns.io/plugins/forward/)
