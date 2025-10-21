---
linkTitle: Gateway API
title: Gateway API with Envoy Gateway
description: Learn how to use the Kubernetes Gateway API with Envoy Gateway in Giant Swarm workload clusters for advanced traffic management, load balancing, and API gateway functionality.
weight: 30
menu:
  principal:
    parent: tutorials-connectivity
    identifier: tutorials-connectivity-gateway-api
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I set up Gateway API in my Giant Swarm cluster?
  - What is the difference between Gateway API and Ingress?
  - How do I configure Envoy Gateway for my workloads?
  - What are the Gateway API components and how do they work together?
  - How do I migrate from Ingress to Gateway API?
last_review_date: 2025-10-17
---

The Kubernetes Gateway API is the next-generation standard for managing ingress traffic in Kubernetes clusters. It provides a more expressive, extensible, and role-oriented approach to traffic management compared to traditional Ingress resources. Giant Swarm supports Gateway API through Envoy Gateway, providing advanced load balancing, traffic routing, and API gateway capabilities.

This guide explains how to set up and use Gateway API with Envoy Gateway in Giant Swarm workload clusters.

## Overview

Gateway API introduces several key concepts that provide more flexibility and control over traffic management:

### Gateway API vs. Ingress

| Feature | Ingress | Gateway API |
|---------|---------|-------------|
| **Role separation** | Single resource | Separate resources for infrastructure (Gateway) and routing (HTTPRoute) |
| **Protocol support** | HTTP/HTTPS only | HTTP/HTTPS, TCP, UDP, TLS |
| **Extensibility** | Limited | Highly extensible with custom resources |
| **Traffic policies** | Basic | Advanced (retries, timeouts, load balancing) |
| **Multi-tenancy** | Limited | Built-in role-based access control |

### Key Components

The Gateway API consists of three main components available in Giant Swarm:

1. **[Gateway API CRDs](https://github.com/giantswarm/gateway-api-crds-app)**: Core custom resource definitions for Gateway API
2. **[Envoy Gateway](https://github.com/giantswarm/envoy-gateway-app)**: The gateway implementation based on Envoy Proxy
3. **[Gateway API Config](https://github.com/giantswarm/gateway-api-config-app)**: Default configuration for quick setup

Those are bundle together in [Gateway API bundle](https://github.com/giantswarm/gateway-api-bundle/tree/main/helm/gateway-api-bundle) to help with the installation.

### Gateway API Resources

- **GatewayClass**: Defines the type of gateway (managed by platform team)
- **Gateway**: Configures load balancer and listeners (managed by platform team)
- **HTTPRoute**: Defines HTTP routing rules (managed by application teams)
- **TCPRoute/UDPRoute**: Defines TCP/UDP routing rules
- **ReferenceGrant**: Enables cross-namespace references

## Prerequisites

Before setting up Gateway API, ensure you have:

- A Giant Swarm workload cluster
- `kubectl` configured to access your workload cluster
- Access to the Giant Swarm platform API for app installation
- Basic understanding of Kubernetes networking concepts

## Installation

Gateway API support is provided through three apps that work together. You can install them individually or use the Gateway API Bundle for simplified deployment. Our recommendation is to use the Gateway API Bundle, which installs all required components:

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
                  dnsName: ingress
      gatewayApiCrds:
        userConfig:
          configMap:
            values: |
              install:
                inferencepools: "standard"
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
  version: 0.5.1
```

In the configuration, you enable the gateway to be the default ingress method for your cluster. Also, the inference CRDs are installed in the workload cluster.

Run `kubectl apply -f` command to install the bundle and way till the app is finally deployed and all the child applications are deployed too (CRDs, envoy gateway and gateway default config).

## Configuration

### Using the default gateway

When you install the Gateway API Bundle, it automatically creates a default Gateway Class called `giantswarm-default` that's pointing to the envoy controller. You can verify it exists:

```bash
kubectl get gatewayclass
```

Expected output:

```text
NAME                 CONTROLLER                                      ACCEPTED
giantswarm-default   gateway.envoyproxy.io/gatewayclass-controller   True
```

Additionally, it also creates a default gateway ready to use in the cluster:

```text
NAME                 CLASS                ADDRESS                            PROGRAMMED
giantswarm-default   giantswarm-default   axx8.eu-west-2.elb.amazonaws.com   True
```

This default Gateway is configured to handle traffic for your cluster's base domain (`*.CLUSTER_ID.k8s.gigantic.io`) and is ready to use immediately with HTTPRoutes.

**Note**: In case you have already running ingress controller in your cluster, talk to us to help you with the migration.

### Custom gateway setup (optional)

If you need additional Gateways for specific requirements, you can create custom ones:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: custom-gateway
  namespace: envoy-gateway-system
spec:
  gatewayClassName: giantswarm-default
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    hostname: "*.example.com"
  - name: https
    protocol: HTTPS
    port: 443
    hostname: "*.example.com"
    tls:
      mode: Terminate
      certificateRefs:
      - name: example-tls-cert
        kind: Secret
```

### Custom gateway configuration

For production use, customize the Gateway API Config app with your specific requirements:

```yaml
# gateway-api-config-values.yaml
gateways:
  production:
    hostnames:
      - "api.example.com"
      - "*.apps.example.com"
    tls:
      enabled: true
      certificateRef:
        name: production-tls
        namespace: giantswarm
  staging:
    hostnames:
      - "staging.example.com"
    tls:
      enabled: false
```

Apply the configuration:

```bash
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=CLUSTER_NAME \
  --organization=ORGANIZATION \
  --name=gateway-api-config \
  --target-namespace=giantswarm \
  --user-configmap=gateway-api-config-values.yaml \
  --version=0.5.1 > gateway-api-config.yaml

kubectl apply -f gateway-api-config.yaml
```

## Usage examples

### Basic HTTP routing

Create an HTTPRoute to route traffic to your application using the default Gateway:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: example-app-route
  namespace: default
spec:
  parentRefs:
  - name: giantswarm-default
    namespace: giantswarm
  hostnames:
  - "app.CLUSTER_ID.k8s.gigantic.io"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: example-app-service
      port: 8080
```

### Advanced routing with path-based rules

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: multi-service-route
  namespace: default
spec:
  parentRefs:
  - name: giantswarm-default
    namespace: giantswarm
  hostnames:
  - "example-api.CLUSTER_ID.k8s.gigantic.io"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /api/v1
    backendRefs:
    - name: api-v1-service
      port: 8080
  - matches:
    - path:
        type: PathPrefix
        value: /api/v2
    backendRefs:
    - name: api-v2-service
      port: 8080
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: frontend-service
      port: 3000
```

### Traffic splitting and canary deployments

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: canary-deployment
  namespace: default
spec:
  parentRefs:
  - name: giantswarm-default
    namespace: giantswarm
  hostnames:
  - "canary.CLUSTER_ID.k8s.gigantic.io"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: stable-service
      port: 8080
      weight: 90
    - name: canary-service
      port: 8080
      weight: 10
```

### Cross-namespace routing

To route traffic to services in different namespaces, create a ReferenceGrant:

```yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-gateway-access
  namespace: production
spec:
  from:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    namespace: giantswarm
  to:
  - group: ""
    kind: Service
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: cross-namespace-route
  namespace: giantswarm
spec:
  parentRefs:
  - name: giantswarm-default
  hostnames:
  - "prod.CLUSTER_ID.k8s.gigantic.io"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: production-service
      namespace: production
      port: 8080
```

## Limitations

- Gateway API is still evolving; some features may be experimental
- Not all Ingress controller features have direct Gateway API equivalents
- Cross-namespace routing requires explicit ReferenceGrant configuration
- Some advanced Envoy features may require custom EnvoyProxy configuration

## Further reading

- [Kubernetes Gateway API documentation](https://gateway-api.sigs.k8s.io/)
- [Envoy Gateway documentation](https://gateway.envoyproxy.io/)
- [Gateway API CRDs app repository](https://github.com/giantswarm/gateway-api-crds-app)
- [Envoy Gateway app repository](https://github.com/giantswarm/envoy-gateway-app)
- [Gateway API Config app repository](https://github.com/giantswarm/gateway-api-config-app)
