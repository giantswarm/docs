---
linkTitle: Multiple ingress nginx controllers
title: Running multiple ingress nginx controllers
description: Deploy multiple ingress nginx controllers in a Kubernetes cluster to separate different ingress traffic classes.
weight: 20
menu:
  principal:
    parent: tutorials-connectivity-ingress
    identifier: tutorials-connectivity-ingress-multi-ic
user_questions:
  - How do I install multiple ingress nginx controllers?
  - How do I separate internal and external Services?
  - How do I configure ingress nginx controller for internal traffic?
  - How do I override the NodePorts on KVM ingresses?
  - How do I configure ingress nginx controller to allow weak ciphers?
last_review_date: 2024-08-26
aliases:
  - /vintage/advanced/connectivity/ingress/multi-nginx-ic
  - /advanced/connectivity/ingress/multi-nginx-ic
  - /guides/multi-nginx/
  - /advanced/multi-nginx/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

ingress nginx controller handles [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resources, routing traffic from outside the Kubernetes cluster to services within the cluster.

It's possible to install multiple ingress controllers in a Kubernetes cluster. The ingress nginx controller can be [installed as an App on your cluster]({{< relref "/getting-started/install-an-application#install-ingress-controller" >}}). Ingress nginx installs an `IngressClass` with the default name `nginx` and controller value `k8s.io/ingress-nginx`.

Some use cases for this might be:

- An ingress controller that's behind an internal ELB for traffic between services within the VPC (or a group of peered VPCs)
- An ingress controller behind an ELB that already terminates SSL
- An ingress controller with different functionality or performance

Most ingress nginx controller configuration options have controller-wide defaults. They can also be override on a per-ingress resource level.

In each case below, one installs a second ingress nginx controller with a different global-only configuration and a separate ingress class. Ingress resources managed by this ingress nginx controller installation can still be customized on a per-ingress resource level.

Further information on configuring ingress nginx controller can be found on the [Advanced ingress configuration]({{< relref "/tutorials/connectivity/ingress/configuration/index.md" >}}) page.

## Quick installation instructions for a second ingress nginx controller

1. Install a second ingress nginx controller App (and subsequent apps) with a different global-only configuration.
2. Change the `ingressClassName` to the appropriate ingress class name. Make sure the ingress class name and controller value of each ingress controller don't collide with each other.

## Set the ingress class name of each ingress

__Note__: if you are running multiple ingress controllers, you need to use the appropriate `ingressClassName` in your ingress resources, for example.

```yaml
...
spec:
  ingressClassName: nginx
...
```

or

```yaml
...
spec:
  ingressClassName: nginx-internal
...
```

Not specifying the `ingressClassName` will lead to no ingress controller claiming your ingress. Specifying a value which doesn't match the class of any existing ingress controller will result in all ingress controllers ignoring the ingress.

Additionally, please ensure the ingress class of each of your ingress controllers doesn't collide with each other. For the community supported ingress nginx controller this is described in the [official documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/).

## Separating public from internal ingress traffic

Having components in multi-tiered architecture or back-office applications not accessible via public internet is a common requirement for security or performance reasons.

This is how one can achieve it by using multiple ingress nginx controllers:

- Deploy one ingress nginx controller App using default settings, for making selected cluster services accessible via public internet
- Deploy second internal ingress nginx controller App. Use these user configuration overrides:

```yaml
controller:
  ingressClassResource:
    name: nginx-internal
    controllerValue: k8s.io/ingress-nginx-internal
  service:
    public: false
    subdomain: ingress-internal
    # Required for KVM only.
    # Don't set on AWS, Azure & others.
    nodePorts:
      http: 30012
      https: 30013
```

Each ingress nginx controller App installation has to have an unique ingress class. ingress resources can then declare which ingress controller should be handling their route definition by referencing the respective ingress class in the `ingressClassName` field. The default ingress nginx controller ingress class is `nginx`. In the above example we configure `nginx-internal` as the second ingress nginx controller installation's ingress class.

On AWS and Azure, ingress nginx controller's `LoadBalancer` service is fronted by cloud provider's managed load balancer service. By default, ingress nginx controller will have a public load balancer. Changing `controller.service.public` flag to `false` declares that an internal load balancer should be created instead.

Similarly, cloud load balancer created for each ingress nginx controller installation on AWS and Azure has to have an unique host name associated with it. The host name suffix is common for all and equals to the workload cluster's base domain name. The prefix is configurable via the `controller.service.subdomain` configuration property and defaults to `ingress`. In the example configuration for the second internal ingress nginx controller, it's override to `ingress-internal`.

For ingress nginx controllers running on on-prem (KVM) workload clusters there's no out-of-the-box `LoadBalancer` service type support. Therefore, ingress nginx controller Service type defaults to `NodePort`. For every ingress nginx controller installation, one must assign a set of unique HTTP and HTTPS node ports. The default ingress nginx controller's HTTP and HTTPS node ports are `30010` and `30011`. The example sets `30012` and `30013` as overrides for the internal ingress nginx controller.

More information on this topic can be found in the document [Services of type LoadBalancer]({{< relref "/tutorials/connectivity/ingress/service-type-loadbalancer" >}}).

It's also possible to only install a single ingress nginx controller and to delegate both external and internal traffic to it. Here is a minimal working example on how to achieve this goal.

```yaml
controller:
  service:
    public: true # default value
    subdomain: ingress # default value
    internal:
      enabled: true # default is `false`
      subdomain: ingress-internal # default value
```

In other words, it's sufficient to set `controller.service.internal.enabled` to `true` to create two services: one for public traffic and one for internal one. On cloud providers, the Services we create will be of type `LoadBalancer`; on premise, depending on the platform, they might be either of type `LoadBalancer` or `NodePort`.

## Using weak ciphers for legacy clients

In [ingress nginx controller v1.2.0](https://github.com/giantswarm/ingress-nginx-app/blob/main/CHANGELOG.md#120-2020-01-21), there was a notable security improvement: weak SSL ciphers were removed from the default configuration. Some older clients (like web browsers or HTTP libraries in apps) could no longer establish secure connections with cluster services exposed via the new ingress nginx controller. This is because these clients only supported SSL ciphers that got removed.

With a single ingress nginx controller, one could restore weak SSL ciphers configuration in order to support services with older clients until clients get upgraded. Problem with this approach, since SSL ciphers are global settings, was that changing default SSL ciphers back by restoring weak ciphers would apply to all ingresses and services behind them, not just the one with old clients.

With multiple ingress nginx controllers, one can have separate ingress nginx controller installations with different SSL ciphers configuration. This allows one to limit restoring weak ciphers only to services used by legacy clients.

Here is how this can be achieved:

- Deploy one ingress nginx controller using default settings
- Deploy second ingress nginx controller. Use these user configuration overrides:

  ```yaml
  controller:
    config:
      ssl-ciphers: ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256
    ingressClassResource:
      name: nginx-weak
      controllerValue: k8s.io/ingress-nginx-weak
    service:
      subdomain: ingress-weak
  ```

For the second ingress nginx controller installation, ingress class name and host name subdomain are customized for uniqueness. Additionally, default SSL ciphers are override to include weak ciphers for legacy clients.

## Additional resources

- [Services of type LoadBalancer]({{< relref "/tutorials/connectivity/ingress/service-type-loadbalancer" >}})
- [Installing an ingress controller]({{< relref "/getting-started/install-an-application#install-ingress-controller" >}})
- [Ingress nginx controller configuration options](https://github.com/giantswarm/ingress-nginx-app/blob/main/helm/ingress-nginx/values.yaml)
- [Upstream ingress nginx controller configuration documentation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/)
- [Upstream ingress nginx controller multi-nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/)
