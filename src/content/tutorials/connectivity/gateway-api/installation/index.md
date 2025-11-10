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
last_review_date: 2025-10-17
---

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
  version: 1.1.0
```

In the configuration, you enable the gateway to be the default ingress method for your cluster. Also, the [Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/) CRDs are installed in the workload cluster.

Run `kubectl apply -f` command on your management cluster to install the bundle then wait until the child apps are deployed (CRDs, envoy gateway and gateway default config).

## Configuration

### Using the default gateway

When you install the Gateway API Bundle, it automatically creates a default Gateway Class called `giantswarm-default` that's pointing to the envoy controller. You can verify it exists on your workload cluster:

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

**Note**: In case you have already running the ingress-nginx controller in your cluster, talk to us to help you with the migration.

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
