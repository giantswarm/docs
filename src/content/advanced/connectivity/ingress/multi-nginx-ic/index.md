---
linkTitle: Multiple Ingress NGINX Controllers
title: Running multiple Ingress NGINX Controllers
description: Deploy multiple Ingress NGINX Controllers in a Kubernetes cluster to separate different ingress traffic classes.
weight: 20
menu:
  main:
    parent: advanced-ingress
user_questions:
  - How do I install multiple Ingress NGINX Controllers?
  - How do I separate internal and external Services?
  - How do I configure Ingress NGINX Controller for internal traffic?
  - How do I override the NodePorts on KVM Ingresses?
  - How do I configure Ingress NGINX Controller to allow weak ciphers?
last_review_date: 2023-11-23
aliases:
  - /guides/multi-nginx/
  - /advanced/multi-nginx/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

Ingress NGINX Controller handles [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resources, routing traffic from outside the Kubernetes cluster to services within the cluster.

Starting with [Ingress NGINX Controller v1.8.0](/changes/managed-apps/nginx-ingress-controller-app/v1.8.0/), one can install multiple Ingress NGINX Controllers in a Kubernetes cluster. The optional Ingress NGINX Controller can be [installed as an App on your cluster]({{< relref "/content/getting-started/connectivity/ingress-controller/index.md" >}}).
[Ingress NGINX Controller v2.2.0](/changes/managed-apps/nginx-ingress-controller-app/v2.2.0/) will start installing a IngressClass with default name `nginx` and controller value `k8s.io/ingress-nginx`.

Some use cases for this might be:

- An Ingress Controller that is behind an internal ELB for traffic between services within the VPC (or a group of peered VPCs)
- An Ingress Controller behind an ELB that already terminates SSL
- An Ingress Controller with different functionality or performance

Most Ingress NGINX Controller configuration options have controller-wide defaults. They can also be overriden on a per-Ingress resource level.

In each case below, one installs a second Ingress NGINX Controller with a different global-only configuration and a separate IngressClass. Ingress resources managed by this Ingress NGINX Controller installation can still be customized on a per-Ingress resource level.

Further information on configuring Ingress NGINX Controller can be found on the [Advanced ingress configuration]({{< relref "/advanced/connectivity/ingress/configuration/index.md" >}}) page.

## Quick installation instructions for a second Ingress NGINX Controller

1. Install a second Ingress NGINX Controller App (and subsequent apps) with a different global-only configuration.
2. Change the `ingressClassName` to the appropriate IngressClass name. Make sure the IngressClass name and controller value of each Ingress Controller do not collide with each other.

## Set the ingressClassName of each Ingress

__Note__ that if you are running multiple Ingress Controllers you need to use the appropriate `ingressClassName` in your Ingress resources, e.g.

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

Not specifying the `ingressClassName` will lead to no Ingress Controller claiming your Ingress. Specifying a value which does not match the class of any existing Ingress Controller will result in all Ingress Controllers ignoring the Ingress.

Additionally, please ensure the IngressClass of each of your Ingress Controllers does not collide with each other and with the [preinstalled Ingress Controllers in legacy clusters]({{< relref "/platform-overview/cluster-management/releases/index.md#apps" >}}). For the community supported Ingress NGINX Controller this is described in the [official documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/).

## Separating public from internal ingress traffic

Having components in multi-tiered architecture or back-office applications not accessible via public internet is a common requirement for security or performance reasons.

This is how one can achieve it by using multiple Ingress NGINX Controllers:

- Deploy one Ingress NGINX Controller App using default settings, for making selected cluster services accessible via public internet
- Deploy second internal Ingress NGINX Controller App. Use these user configuration overrides:

```yaml
controller:
  ingressClassResource:
    name: nginx-internal
    controllerValue: k8s.io/ingress-nginx-internal
  service:
    public: false
    subdomain: ingress-internal
    # Required for KVM only.
    # Do not set on AWS, Azure & others.
    nodePorts:
      http: 30012
      https: 30013
```

Each Ingress NGINX Controller App installation has to have an unique IngressClass. Ingress resources can then declare which Ingress Controller should be handling their route definition by referencing the respective IngressClass in the `ingressClassName` field. The default Ingress NGINX Controller IngressClass is `nginx`. In the above example we configure `nginx-internal` as the second Ingress NGINX Controller installation's IngressClass.

On AWS and Azure, Ingress NGINX Controller's `LoadBalancer` Service is fronted by the cloud provider's managed load balancer service. By default, Ingress NGINX Controller will have a public load balancer. Changing `controller.service.public` flag to `false` declares that an internal load balancer should be created instead.

Similarly, the cloud load balancer created for each Ingress NGINX Controller installation on AWS and Azure has to have an unique hostname associated with it. The hostname suffix is common for all and equals to the workload cluster's base domain name. The prefix is configurable via the `controller.service.subdomain` configuration property and defaults to `ingress`. In the example configuration for the second internal Ingress NGINX Controller, it is overriden to `ingress-internal`.

For Ingress NGINX Controllers running on on-prem (KVM) workload clusters there's no out-of-the-box `LoadBalancer` service type support. Therefore, Ingress NGINX Controller Service type defaults to `NodePort`. For every Ingress NGINX Controller installation, one must assign a set of unique HTTP and HTTPS node ports. The default Ingress NGINX Controller's HTTP and HTTPS node ports are `30010` and `30011`. The example sets `30012` and `30013` as overrides for the internal Ingress NGINX Controller.

More information on this topic can be found in the document [Services of type LoadBalancer]({{< relref "/content/advanced/connectivity/ingress/service-type-loadbalancer/index.md" >}}).

It is also possible to only install a single Ingress NGINX Controller and to delegate both external and internal traffic to it. Here is a minimal working example on how to achieve this goal.

```yaml
controller:
  service:
    public: true # default value
    subdomain: ingress # default value
    internal:
      enabled: true # default is `false`
      subdomain: ingress-internal # default value
```

In other words, it is sufficient to set `controller.service.internal.enabled` to `true` to create two services: one for public traffic and one for internal one. On cloud providers, the Services we create will be of type `LoadBalancer`; on premise, depending on the platform, they might be either of type `LoadBalancer` or `NodePort`.

## Using weak ciphers for legacy clients

In [Ingress NGINX Controller v1.2.0](https://github.com/giantswarm/ingress-nginx-app/blob/main/CHANGELOG.md#120-2020-01-21), there was a notable security improvement: weak SSL ciphers were removed from the default configuration. Some older clients (like web browsers or HTTP libraries in apps) could no longer establish secure connections with cluster services exposed via the new Ingress NGINX Controller. This is because these clients only supported SSL ciphers that got removed.

With a single Ingress NGINX Controller, one could restore weak SSL ciphers configuration in order to support services with older clients until clients get upgraded. Problem with this approach, since SSL ciphers are global settings, was that changing default SSL ciphers back by restoring weak ciphers would apply to all Ingresses and services behind them, not just the one with old clients.

With multiple Ingress NGINX Controllers, one can have separate Ingress NGINX Controller installations with different SSL ciphers configuration. This allows one to limit restoring weak ciphers only to services used by legacy clients.

Here is how this can be achieved:

- Deploy one Ingress NGINX Controller using default settings
- Deploy second Ingress NGINX Controller. Use these user configuration overrides:

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

For the second Ingress NGINX Controller installation, IngressClass name and hostname subdomain are customized for uniqueness. Additionally, default SSL ciphers are overriden to include weak ciphers for legacy clients.

## Additional resources

- [Services of type LoadBalancer]({{< relref "/content/advanced/connectivity/ingress/service-type-loadbalancer/index.md" >}})
- [Installing an Ingress Controller]({{< relref "/content/getting-started/connectivity/ingress-controller/index.md" >}})
- [Ingress NGINX Controller configuration options](https://github.com/giantswarm/ingress-nginx-app/blob/main/helm/ingress-nginx/values.yaml)
- [Upstream Ingress NGINX Controller configuration documentation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/)
- [Upstream Ingress NGINX Controller multi-nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/)
