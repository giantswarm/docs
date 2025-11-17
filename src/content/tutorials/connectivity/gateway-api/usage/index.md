---
linkTitle: Usage
title: Using Gateway API with Envoy Gateway
description: Learn how to use the Kubernetes Gateway API with Envoy Gateway for traffic routing and management.
weight: 20
menu:
  principal:
    parent: tutorials-connectivity-gateway-api
    identifier: tutorials-connectivity-gateway-api-usage
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I create HTTPRoutes with Gateway API?
  - How do I do canary deployments with Gateway API?
  - How do I route traffic across namespaces?
last_review_date: 2025-10-17
---

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
    namespace: envoy-gateway-system
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
    namespace: envoy-gateway-system
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
    namespace: envoy-gateway-system
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

## Authentication

### Basic Auth

Using the SecurityPolicy custom resource, you can add basic authentication to your HTTPRoute. In this example, `basic-auth` is a secret containing the `.htpasswd` file in the [Apache htpasswd format](https://httpd.apache.org/docs/current/programs/htpasswd.html).

```yaml
---
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: SecurityPolicy
metadata:
  name: basic-auth
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: example-app-route
  basicAuth:
    users:
      name: "basic-auth"
```
