---
linkTitle: Inference Extension
title: Installing Gateway API Inference Extension
description: Learn how to install the Kubernetes Gateway API Inference Extension in Giant Swarm workload clusters.
weight: 30
menu:
  principal:
    parent: tutorials-connectivity-gateway-api
    identifier: tutorials-connectivity-gateway-api-ia-extensions
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How do I install the Gateway API Inference Extension?
last_review_date: 2025-12-04
---

## Overview

The Kubernetes Gateway API Inference Extension enables AI/ML workloads to be exposed and managed through the Gateway API. This extension provides a standardized way to configure routing and load balancing for inference endpoints, making it easier to deploy and scale AI services in your Kubernetes clusters.

This guide walks you through installing the Gateway API Inference Extension on Giant Swarm workload clusters. You enable the inference pool Custom Resource Definitions (CRDs) in your Gateway API bundle configuration.

## Installation

Our Gateway API CRDs app already supports the inference extensions. In your Gateway API bundle configmap, add the following block:

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
      gatewayApiCrds:
        userConfig:
          configMap:
            values: |
              install:
                inferencepools: "standard"
```

Run the `kubectl apply -f <configmap-file.yaml>` command on your management cluster to apply the updated bundle configuration, then wait until the new CRDs are deployed.

## Further reading

- [Kubernetes Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/)
