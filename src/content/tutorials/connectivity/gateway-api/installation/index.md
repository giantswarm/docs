---
linkTitle: Quick start
title: Installing Gateway API with Envoy Gateway
description: Learn how to install and configure the Kubernetes Gateway API with Envoy Gateway in Giant Swarm workload clusters.
weight: 10
menu:
  principal:
    parent: tutorials-connectivity-gateway-api
    identifier: tutorials-connectivity-gateway-api-installation
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I install Gateway API in my Giant Swarm cluster?
  - How do I install and configure the Gateway API Bundle?
last_review_date: 2025-12-04
---

## Prerequisites

Before setting up Gateway API, ensure you have:

- A Giant Swarm workload cluster
- `kubectl` configured to access your workload cluster
- Access to the Giant Swarm platform API for app installation
- Basic understanding of Kubernetes networking concepts
- On AWS based clusters, [`aws-load-balancer-controller`](https://github.com/giantswarm/aws-load-balancer-controller-app) is required for configuring AWS Network Load Balancers.

In case you can not install `aws-load-balancer-controller` or don't want to use AWS Network Load Balancers, you can set `gateways.default.provider.aws.useNetworkLoadBalancer=false` in `gatewayApiConfig.userConfig.configMap` of the bundle.

## Installation

Gateway API support is provided through three apps that work together. You can install them individually or use the Gateway API Bundle for simplified deployment. Our recommendation is to use the Gateway API Bundle, which installs all required components (Gateway API CRDs, [Envoy Gateway](https://gateway.envoyproxy.io/) and a preconfigured default Gateway):

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-gateway-api-bundle
  namespace: org-<ORGANIZATION>
data:
  values: |
    clusterID: <CLUSTER_NAME>
    organization: <ORGANIZATION>
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: <CLUSTER_NAME>-gateway-api-bundle
  namespace: org-<ORGANIZATION>
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: true
  name: gateway-api-bundle
  namespace: org-<ORGANIZATION>
  userConfig:
    configMap:
      name: <CLUSTER_NAME>-gateway-api-bundle
      namespace: org-<ORGANIZATION>
  version: 1.4.0
```

Run the `kubectl apply -f <bundle-config.yaml>` command on your management cluster to install the bundle, then wait until the child apps are deployed (CRDs, Envoy Gateway, and Gateway default config).

## Configuration

### Certificate management with cert-manager

In order to obtain TLS certificates for your domains served by Gateway API, cert-manager needs to be configured to handle Gateway resources.

In your clusters user ConfigMap, add the following section. Do this only after Gateway API CRDs are installed.

```yaml
global:
  apps:
    certManager:
      values:
        config:
          apiVersion: controller.config.cert-manager.io/v1alpha1
          enableGatewayAPI: true
          kind: ControllerConfiguration
```

### Using the default gateway

When you install the Gateway API Bundle, it automatically creates a default GatewayClass called `giantswarm-default` managed by the Envoy Gateway controller. You can verify it exists on your workload cluster:

```bash
kubectl get gatewayclass
```

Expected output:

```text
NAME                 CONTROLLER                                      ACCEPTED
giantswarm-default   gateway.envoyproxy.io/gatewayclass-controller   True
```

Additionally, it also creates the `giantswarm-default` Gateway ready to use in the cluster:

```text
NAME                 CLASS                ADDRESS                            PROGRAMMED
giantswarm-default   giantswarm-default   axx8.eu-west-2.elb.amazonaws.com   True
```

**Note**: Since DNS and TLS certificates in the Gateway API world are different from Ingress, you must configure which domains the Gateway accepts.

The default Gateway is configured to accept traffic for your cluster's base domain (`*.CLUSTER_ID.k8s.gigantic.io`) and is ready to attach any HTTPRoute resources matching that pattern. However, no TLS certificates or DNS records are automatically created based on the HTTPRoute resources.

#### Option 1: Adding each subdomain

You can define a list of subdomains inside the HTTPS listener. This will automatically create a CNAME (Canonical Name) DNS record pointing to the Gateway load balancer and add it to the `dnsNames` list in the certificate.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-gateway-api-bundle
  namespace: org-<ORGANIZATION>
data:
  values: |
    clusterID: <CLUSTER_NAME>
    organization: <ORGANIZATION>
    apps:
      gatewayApiConfig:
        userConfig:
          configMap:
            values: |
              gateways:
                default:
                  listeners:
                    https:
                      subdomains:
                      - myapplication
```

**Note**: The base domain is appended to each subdomain to compose the FQDN (Fully Qualified Domain Name), `myapplication.CLUSTER_ID.k8s.gigantic.io` in our example.

#### Option 2: Overriding the base domain

It's possible to completely override the base domain and make the Gateway only accept a domain that is not the cluster domain.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-gateway-api-bundle
  namespace: org-<ORGANIZATION>
data:
  values: |
    clusterID: <CLUSTER_NAME>
    organization: <ORGANIZATION>
    apps:
      gatewayApiConfig:
        userConfig:
          configMap:
            values: |
              gateways:
                default:
                  overrideBaseDomain: "example.com"
                  listeners:
                    https:
                      subdomains:
                      - myapplication
```

This results in a Gateway with an HTTPS listener that accepts traffic for `myapplication.example.com` with a TLS certificate attached.

#### Option 3: Adding a new listener

In this example, you observe how to add a new listener for the base domain `example.com`. In this case, TLS certificates are created by cert-manager, but external-dns integration is disabled.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-gateway-api-bundle
  namespace: org-<ORGANIZATION>
data:
  values: |
    clusterID: <CLUSTER_NAME>
    organization: <ORGANIZATION>
    apps:
      gatewayApiConfig:
        userConfig:
          configMap:
            values: |
              gateways:
                default:
                  listeners:
                    example-https:
                      name: example-https
                      protocol: HTTPS
                      hostname: '*.example.com'
                      port: 443
                      allowedRoutes:
                        namespaces:
                          from: All
                      tls:
                        mode: Terminate
                        certificateRefs: []
                      subdomains:
                      - myapplication
                      - docs
                      - otherapp
                      certificate:
                        enabled: true
                      dnsEndpoints:
                        enabled: false
```
