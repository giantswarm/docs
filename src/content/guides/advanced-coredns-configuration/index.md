+++
title = "Advanced CoreDNS Configuration"
description = "Here we describe how you can customize the configuration of the managed CoreDNS service in your clusters"
date = "2018-10-30"
type = "page"
weight = 50
tags = ["tutorial"]
+++

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

By default we set the cache TTL for CoreDNS to 30 seconds. You can customize the cache settings of CoreDNS by setting the value of the cache field in the user ConfigMap like following.

```yaml
data:
  cache: 60
```

Above setting increases the TTL to 60 seconds.

The cache plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/cache/).

## Additional proxies

The default proxy entry we set in CoreDNS is

```yaml
proxy . /etc/resolv.conf
```

You can add additional proxy entries by adding a each as a line to the proxy field of the user ConfigMap.

For a single entry you can use the same line.

```yaml
data:
  proxy: foo.com 1.1.1.1

```

For multplie entries you add a string with a proxy entry per line.

```yaml
data:
  proxy: |
    foo.com 1.1.1.1
    bar.com 8.8.8.8
```

Above example would result in following additional proxy entries in the CoreDNS configuration:

```yaml
proxy foo.com 1.1.1.1
proxy bar.com 8.8.8.8
```

This setting would proxy all requests within foo.com to 1.1.1.1 which is Cloudflare's DNS and all requests within bar.com to 8.8.8.8 which is Google Public DNS. All other requests will be resolved by the default DNS provider set for your cluster.

The proxy plugin also supports much more detailed configuration which is documented in the [upstream documentation](https://coredns.io/plugins/proxy/).

## Advanced configuration

In case you need to use an additional plugin or existing plugin but with special configuration, you can use the `custom` block in the configmap. It will be parsed directly to the Corefile.

```yaml
data:
  custom: |
    proxy foo.com 1.1.1.1 {
      policy least_conn
      spray
    }
    cache 200 {
      denial 1024 10
    }
```

__Warning:__ Please make sure you test the final `Corefile`carefully. We do not take responsibility of wrong custom configuration that could break workload communication.

## Further reading

- [CoreDNS Website](https://coredns.io/)
- [CoreDNS cache plugin](https://coredns.io/plugins/cache/)
- [CoreDNS proxy plugin](https://coredns.io/plugins/proxy/)
