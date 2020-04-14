---
title: Advanced CoreDNS Configuration
description: Here we describe how you can customize the configuration of the managed CoreDNS service in your clusters
date: 2018-10-30
type: page
weight: 50
tags: ["tutorial"]
---

# Advanced CoreDNS Configuration

The [CoreDNS addon](https://github.com/coredns/coredns) running inside your cluster has additional configuration options and features that can be customized.

You can customize two of these configuration options on a per cluster basis through a ConfigMap inside your clusters. The ConfigMap is named `coredns-user-values` and is located in the `kube-system` namespace.

__Note:__ This feature is only available in more recent cluster versions. To check if your cluster version supports customization through the ConfigMap, you can check if the above-mentioned ConfigMap is present.

```nohighlight
$ kubectl -n kube-system get cm coredns-user-values
NAME                                   DATA      AGE
coredns-user-values                    0         11m
```

On cluster creation the ConfigMap is empty and below-mentioned defaults will be applied to the final CoreDNS deployment. To customize any of the configuration options, you just need to add the respective line(s) in the data field of the user ConfigMap.

__Warning:__ Please do not edit any of the other CoreDNS related resources. Only the user ConfigMap is safe to edit.

## Cache settings

By default we set the cache TTL for CoreDNS to 30 seconds. You can customize the cache settings of CoreDNS by setting the value of the cache field in the user ConfigMap like this:

```yaml
data:
  cache: "60"
```

Above setting increases the TTL to 60 seconds.

The cache plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/cache/).

## Logs

By default, we set the log level for CoreDNS to `denial` and `error`. You can tun these settings by adding a property `log` in the user ConfigMap like this:

```yaml
data:
  log: |
    all
```

To know the exact details of each log level log plugin, please read the [upstream documentation](https://coredns.io/plugins/log/).

## Additional forwards (formerly known as proxy) {#additional-forwards}

In CoreDNS version `1.4.0` the proxy plugin has been deprecated. The same behaviour can be achieved now with forward although the syntax can be a bit different. The forward plugin has better performance because it reuses opened upstream connections.

The default forward entry we set in CoreDNS is

```yaml
forward . /etc/resolv.conf
```

You can add additional forward entries by adding a each as a line to the forward field of the user ConfigMap. They will be selected in sequential order.

You can use a simple line or multiple lines to define the upstreams of the default server block.

```yaml
data:
  forward: 1.1.1.1
```

```yaml
data:
  forward: |
    1.1.1.1
    8.8.8.8
```

__Warning:__ The number of forward upstreams is limited to 15.

Above example would result in the following additional forward entries in the CoreDNS configuration:

```yaml
forward . 1.1.1.1 /etc/resolv.conf
```

```yaml
forward . 1.1.1.1 8.8.8.8 /etc/resolv.conf
```

This setting would forward all requests to 1.1.1.1 which is Cloudflare's DNS. If the first upstream fails the second IP (8.8.8.8) will be used as resolver. In case it fails too, all requests will be resolved by the default DNS provider set for your cluster.

The forward plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/forward/).

## Advanced configuration

In case you need to have a finer granularity you can define custom server blocks with all desired configuration. They will be parsed after the catch-all block in the Corefile. As an example, let's define a block for a `example.com` with some custom configuration:

```yaml
data:
  custom: |
    example.com:1053 {
      forward . 9.9.9.9
      cache 2000
    }
```

This custom configuration allows CoreDNS resolve all `example.com` requests to a different upstream DNS resolver (9.9.9.9) than generic one. At the same time we use a different cache TTL(2000) setting. 

__Warning:__ By default our clusters come with Pod Security Policies and Network Policies for managed components. This means the CoreDNS container doesn't use a privileged port and listens to `1053` instead. Please make sure you test the final `Corefile` carefully. We do not take responsibility for incorrect custom configuration that could break workload communication.

## Further reading

- [CoreDNS Website](https://coredns.io/)
- [CoreDNS cache plugin](https://coredns.io/plugins/cache/)
- [CoreDNS forward plugin](https://coredns.io/plugins/forward/)
