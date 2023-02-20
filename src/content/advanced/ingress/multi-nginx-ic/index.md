---
linkTitle: Multiple NGINX ingress controllers
title: Running multiple NGINX ingress controllers
description: Deploy multiple NGINX ingress controllers in a Kubernetes cluster to separate different ingress traffic classes.
weight: 20
menu:
  main:
    parent: advanced-ingress
aliases:
  - /guides/multi-nginx/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I install multiple NGINX Ingress Controllers?
  - How do I separate internal and external Services?
  - How do I configure NGINX Ingress Controller for internal traffic?
  - How do I override the NodePorts on KVM Ingresses?
  - How do I configure NGINX Ingress Controller to allow weak ciphers?
last_review_date: 2022-07-19
---

NGINX ingress controller handles [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resources, routing traffic from outside the Kubernetes cluster to services within the cluster.

Starting with [NGINX IC v1.8.0](/changes/managed-apps/nginx-ingress-controller-app/v1.8.0/), one can install multiple NGINX ingress controllers in a Kubernetes cluster. The optional NGINX Ingress Controller can be [installed as an App on your cluster]({{< relref "/content/getting-started/ingress-controller/index.md" >}}).
[NGINX IC v2.2.0](/changes/managed-apps/nginx-ingress-controller-app/v2.2.0/) will start installing a IngressClass with default name `nginx` and controller value `k8s.io/ingress-nginx`.

Some use cases for this might be:

- An Ingress Controller that is behind an internal ELB for traffic between services within the VPC (or a group of peered VPCs)
- An Ingress Controller behind an ELB that already terminates SSL
- An Ingress Controller with different functionality or performance

Most NGINX configuration options have NGINX-wide defaults. They can also be overriden on a per-Ingress resource level.

In each case below, one installs a second NGINX with a different NGINX global-only configuration and separate IngressClass. Ingress resources managed by this NGINX installation cannot be customized on a per-Ingress resource level.

Further information on configuring NGINX Ingress Controller can be found on the [Advanced ingress configuration]({{< relref "/advanced/ingress/configuration/index.md" >}}) page.

## Quick installation instructions for a second NGINX Ingress controller

1. Install a second NGINX IC app (and subsequent apps) with a different NGINX global-only configuration. Ingress resources managed by this NGINX installation cannot be customized on a per-Ingress resource level.
2. Change the ingressClassName to the appropriate IngressClass name. Make sure the IngressClass name and controller value of each Ingress Controller do not collide with each other.

## Set the ingressClassName of each Ingress

__Note__ that if you are running multiple Ingress Controllers you need to use the appropriate ingressClassName in your Ingress resources, e.g.

```yaml
...
spec:
  ingressClassName: "nginx"
...
```

or

```yaml
...
spec:
  ingressClassName: "nginx-internal"
...
```

Not specifying the ingressClassName will lead to no ingress controller claiming your Ingress. Specifying a value which does not match the class of any existing ingress controllers will result in all ingress controllers ignoring the ingress.

Additionally, please ensure the Ingress Class of each of your Ingress Controllers do not collide with each other and with the [preinstalled Ingress Controllers in legacy clusters]({{< relref "/platform-overview/cluster-management/releases/index.md#apps" >}}). For the community supported NGINX Ingress Controller this is described in the [official documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/).

## Separating public from internal ingress traffic

Having components in multi-tiered architecture or back-office applications not accessible via public internet is a common requirement for security or performance reasons.

This is how one can achieve it by using multiple NGINX Ingress Controllers:

- Deploy one NGINX IC App using default settings, for making selected cluster services accessible via public internet
- Deploy second internal NGINX IC App. Use these user configuration overrides:

    - on AWS and Azure

    ```yaml
    controller:
      ingressClassResource:
        name: "nginx-internal"
        controllerValue: "k8s.io/ingress-nginx-internal"
      service:
        public: false
        subdomain: "ingress-internal"
    ```

    - on KVM

    ```yaml
    controller:
      ingressClassResource:
        name: "nginx-internal"
        controllerValue: "k8s.io/ingress-nginx-internal"
      service:
        # enabled: true
        public: false
        subdomain: "ingress-internal"
        # type: NodePort
        nodePorts:
          http: 31010
          https: 31011
    ```

Each NGINX IC App installation has to have an unique IngressClass. Ingress resources can then declare which ingress controller should be handling their route definition by referencing the respective IngressClass in the `ingressClassName` spec field. Default NGINX IC App IngressClass is `nginx`. In the above example we configure `nginx-internal` as the second NGINX IC App installation's IngressClass.

On AWS and Azure, NGINX LoadBalancer Service is fronted by the cloud provider's managed load balancer service. By default, NGINX IC App will have a public load balancer. Changing `controller.service.public` flag to `false` declares that internal load balancer should be created instead.

Similarly, cloud load balancer created for each NGINX installation on AWS and Azure has to have unique host name associated with it. Host name suffix is common for all, and equals to the workload cluster's base domain name. Prefix is configurable via `controller.service.subdomain` configuration property and defaults to `ingress`. In example configuration for second internal NGINX IC app, it is overriden to `ingress-internal`.

For NGINX IC running on on-prem (KVM) workload clusters there's no out-of-the-box `LoadBalancer` Service type support. Therefore, NGINX Service type defaults to `NodePort`. For every NGINX IC App installation, one must assign a set of unique http and https node ports. The default NGINX http and https node ports are `30010` and `30011`. The example sets `31010` and `31011` as overrides for the internal NGINX.

More information on this topic can be found in document [Services of type LoadBalancer]({{< relref "/content/advanced/ingress/service-type-loadbalancer/index.md" >}}).

It is also possible to only install a single Nginx Ingress Controller App and to delegate both internal and external traffic to it. Here is a minimal working example on how to achieve this goal.

```yaml
controller:
  service:
    public: true  # default value
    subdomain: "ingress"  # default value
    internal:
      enabled: true  # default is `false`
      subdomain: "ingress-internal"  # default value
```

In other words, it is sufficient to set `controller.service.internal.enabled` to `true` to create two services: one for public traffic and one for private one. On cloud providers, the Services we create will be of type `LoadBalancer`; on premise, depending on the platform, they might be either of type `LoadBalancer` or `NodePort`.

## Using weak ciphers for legacy clients

In [NGINX IC App v1.2.0](https://github.com/giantswarm/nginx-ingress-controller-app/blob/main/CHANGELOG.md#120-2020-01-21), there was a notable security improvement: weak SSL ciphers were removed from the default configuration. Some older clients (like web browsers, http libraries in apps) could no longer establish secure connections with cluster services exposed via new NGINX. This is because these clients only supported SSL ciphers that got removed.

With single NGINX, one could restore weak SSL ciphers configuration in order to support services with older clients until clients get upgraded. Problem with this approach, since SSL ciphers are global settings, was that changing default SSL ciphers back by restoring weak ciphers would apply to all Ingresses and service behind them, not just the one with old clients.

With multiple NGINX ingress controllers, one can have separate NGINX installations with different SSL ciphers configuration. This allows one to limit restoring weak ciphers only to services used by legacy clients.

Here is how this can be achieved:

- Deploy one NGINX IC App using default settings
- Deploy second internal NGINX IC App. Use these user configuration overrides:

  ```yaml
  controller:
    ingressClassResource:
      name: "nginx-weak"
      controllerValue: "k8s.io/ingress-nginx-weak"
    service:
      subdomain: "ingress-weak"
  configmap:
    ssl-ciphers: "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256"
  ```

For the second NGINX IC App installation, ingress class and host name subdomain are customized for uniqueness. Additionally, default SSL ciphers are overriden to include weak ciphers for legacy clients.

## Additional resources

- [Services of type LoadBalancer]({{< relref "/content/advanced/ingress/service-type-loadbalancer/index.md" >}})
- [Installing an Ingress Controller]({{< relref "/content/getting-started/ingress-controller/index.md" >}})
- [NGINX IC App configuration options](https://github.com/giantswarm/nginx-ingress-controller-app/blob/main/helm/nginx-ingress-controller-app/values.yaml)
- [Upstream ingress-nginx configuration documentation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/)
- [Upstream ingress-nginx multi-nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/)
