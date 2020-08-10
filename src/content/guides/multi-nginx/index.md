---
title: Multi-NGINX ingress controller support
description: Deploy multiple NGINX ingress controllers in a Kubernetes cluster to separate different ingress traffic classes.
date: 2020-08-05
type: page
tags: ["tutorial"]
---

# Multi-NGINX ingress controller support

NGINX ingress controller handles [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resources, routing the traffic from outside of the Kubernetes cluster to services within the cluster. Starting with App version 1.8.0 one can install multiple NGINX ingress controllers in same Kubernetes cluster. Here we cover common cases where having multiple NGINX ingress controllers can be useful.

Most of the NGINX configuration options have NGINX wide defaults but can also be overriden on per Ingress resource level. In each of the covered multi-NGINX use cases, one essentially installs second NGINX with different NGINX global-only configuration, i.e. configuration that applies to all Ingress resources managed by that NGINX installation which cannot be customized on per-Ingress resource level.

## Separating public from internal ingress traffic

Having some components in multi-tierd architecture or back-office applications not accessible via public internet is a common requirement for security or performance reasons. This is how one can achieve it by using multi-NGINX ingress controller support:

- Deploy one NGINX IC App using default settings, for making selected cluster services accessible via the public internet
- Deploy second internal NGINX IC App using following user configuration overrides

  - on AWS and Azure

    ```yaml
    controller:
      ingressClass: "nginx-internal"
      service:
        public: false
        subdomain: "ingress-internal"
    ```

  - on KVM

    ```yaml
    controller:
      ingressClass: "nginx-internal"
      service:
        # enabled: true
        public: false
        subdomain: "ingress-internal"
        # type: NodePort
        nodePorts:
          http: 31010
          https: 31011
    ```

Each NGINX IC App installation has to have unique ingress class. Ingress resources can then declare which ingress controller should be handling their route definition by referencing appropriate ingress class in `kubernetes.io/ingress.class` annotation. Default NGINX IC App ingress class is `nginx`. In the above example we configure `nginx-internal` as the second NGINX IC App installation's ingress class.

On AWS and Azure, NGINX LoadBalancer Service is fronted by cloud provider managed load balancer service. By default NGINX IC App will have a public load balancer. Changing `controller.service.public` flag to `false` declares that internal load balancer should be created instead.

Similarly, cloud load balancer created for each NGINX installation on AWS and Azure has to have unique host name associated with it. Host name suffix is common for all, and equals to the tenant cluster's base domain name. Prefix is configurable via `controller.service.subdomain` configuration property and defaults to `ingress`. In example configuration override for second internal NGINX IC App it is overriden to `ingress-internal`.

For NGINX IC running on on-prem (KVM) tenant clusters there's no out-of-the-box `LoadBalancer` Service type support. Therefore NGINX Service type defaults to `NodePort`. For every NGINX IC App installation a set of unique http and https node ports ought to be assigned. The default NGINX http and https node ports are `30010` and `30011`. The example sets `31010` and `31011` as overrides for the internal NGINX.

## Using weak ciphers for legacy clients

In NGINX IC App v1.2.0 upgrade to ingress-nginx 0.27.1 was included. Among other things this upgrade brought in security improvements - SSL ciphers which are considered as weak got removed from the default configuration. Some of the older clients (like web browsers, http libraries in apps) could no longer establish secure connections with cluster services exposed via new NGINX, since these legacy clients only supported SSL ciphers that got removed.

With single NGINX one had option of restoring weak SSL ciphers configuration, to support few services with older clients until the clients get upgraded. Problem with this approach, since SSL ciphers are global settings, was that changing default SSL ciphers back by restoring weak ciphers would apply to all Ingresses and service behind them, not just the one with old clients.

With multiple NGINX ingress controller support, one can have separate NGINX installations with different SSL ciphers configuration, to localize but still make accessible services used by the legacy clients.

Here is how this can be achieved:

- Deploy one NGINX IC App using default settings
- Deploy second internal NGINX IC App using following user configuration overrides

  ```yaml
  controller:
    ingressClass: "nginx-weak"
    service:
      subdomain: "ingress-weak"
  configmap:
    ssl-ciphers: "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256"
  ```

For the second NGINX IC App installation ingress class and host name subdomain are customized for uniqueness. Additionally, default SSL ciphers are overriden to include weak ciphers for legacy clients.

## Further reading

- [Official ingress-nginx multi-nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/)
