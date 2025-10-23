---
title: Scaling workloads based on custom GPU metrics
linkTitle: Scaling GPU workloads
description: Learn how to configure Horizontal Pod Autoscaling with Prometheus adapter to scale workloads based on custom GPU metrics in Giant Swarm clusters.
weight: 10
menu:
  principal:
    parent: tutorials-fleet-management-scaling
    identifier: tutorials-fleet-management-scaling-custom-gpu-metrics
last_review_date: 2025-10-23
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How can I scale workloads based on GPU utilization?
  - How do I configure HPA with custom GPU metrics?
---

Horizontal Pod Autoscaling (HPA) with custom metrics allows you to scale your workloads based on GPU utilization and other specialized metrics beyond CPU and memory. This tutorial shows you how to configure HPA with the Prometheus adapter to scale workloads based on NVIDIA DCGM (Data Center GPU Manager) metrics in your Giant Swarm clusters.

This approach is particularly useful for GPU-intensive workloads like machine learning training, inference services, or scientific computing applications where scaling decisions should be based on actual GPU resource utilization rather than traditional CPU/memory metrics.

## Prerequisites

Before starting this tutorial, ensure you have:

- A Giant Swarm workload cluster with GPU-enabled nodes (see our [GPU workloads guide]({{< relref "/tutorials/fleet-management/cluster-management/gpu" >}}))
- `kubectl` configured to access your workload cluster
- Access to the platform API (see [accessing the platform API]({{< relref "/getting-started/access-to-platform-api" >}}))
- GPU workloads already running with DCGM exporter configured
- Basic understanding of Kubernetes HPA and Prometheus metrics

## Step 1: Verify GPU metrics collection

First, confirm that GPU metrics are being collected and available in your observability platform. The DCGM exporter should already be configured as described in the [GPU monitoring section]({{< relref "/tutorials/fleet-management/cluster-management/gpu#monitoring" >}}).

Check that GPU metrics are available:

```bash
# Verify DCGM exporter is running
kubectl get pods -n kube-system -l app=nvidia-dcgm-exporter

# Check if ServiceMonitor is configured
kubectl get servicemonitor -n kube-system dcgm-exporter
```

You should see DCGM metrics in your Grafana Explore view, such as:

- `DCGM_FI_DEV_GPU_UTIL` - GPU utilization percentage
- `DCGM_FI_DEV_MEM_COPY_UTIL` - GPU memory utilization
- `DCGM_FI_DEV_FB_USED` - GPU frame buffer memory used
- `DCGM_FI_DEV_FB_TOTAL` - GPU frame buffer memory total

## Step 2: Install KEDA

[KEDA (Kubernetes Event Driven Autoscaling)](https://keda.sh/) is a Kubernetes-based event-driven autoscaler that can scale workloads based on custom metrics, including GPU utilization metrics from Prometheus. KEDA provides a more flexible alternative to the standard Horizontal Pod Autoscaler (HPA) with built-in support for various metric sources.

Install KEDA using the Giant Swarm App Platform:

```bash
export CLUSTER=your-cluster-id

kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=${CLUSTER} \
  --name=keda \
  --target-namespace=keda-system \
  --version=3.1.0 > keda-app.yaml

kubectl apply -f keda-app.yaml
```

Verify the KEDA installation:

```bash
# Check if KEDA operator is running
kubectl get pods -n keda-system

# Verify KEDA CRDs are installed
kubectl get crd | grep keda

# Expected output should include:
# scaledobjects.keda.sh
# scaledjobs.keda.sh
# triggerauthentications.keda.sh
```

Since the metrics are stored in Mimir central deployment running in the management cluster, you need an ingress to expose the endpoint to enable KEDA query for the metrics. Talk to us to make ingress endpoint available. In this example, the Mimir endpoint is exposed like `mimir.mc.aws.gigantic.io`.

## Step 4: Deploy a test workload

You can use for test purposes [a demo ML inference service](https://github.com/giantswarm/ML-demo) which uses a GPU library to do some computations, and has an endpoint to generate load on the system and test the scaling scenario. Feel free to use your own application.

Now, you need to define a `ScaledObject` to configure which metrics exposed by Mimir endpoint will be used for scaling.

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: ml-demo
  namespace: ml-workloads
spec:
  scaleTargetRef:
    name: ml-demo
  minReplicaCount: 2
  maxReplicaCount: 10
  pollingInterval: 30
  cooldownPeriod: 300
  advanced:
    horizontalPodAutoscalerConfig:
      behavior:
        scaleUp:
          stabilizationWindowSeconds: 0
          policies:
          - type: Percent
            value: 100
            periodSeconds: 15
        scaleDown:
          stabilizationWindowSeconds: 300
          policies:
          - type: Percent
            value: 100
            periodSeconds: 15
  triggers:
    - type: prometheus
      metadata:
        serverAddress: https://mimir.mc.aws.gigantic.io/prometheus
        query: avg(DCGM_FI_DEV_GPU_UTIL{namespace!="",pod!=""}) by (pod)
        threshold: "70"
        authModes: "basic"
        unsafeSsl: "false"
      authenticationRef:
        name: mimir-auth-trigger
    - type: prometheus
      metadata:
        serverAddress: https://mimir.mc.aws.gigantic.io/prometheus
        query: avg(DCGM_FI_DEV_MEM_COPY_UTIL{namespace!="",pod!=""}) by (pod)
        threshold: "80"
        authModes: "basic"
        unsafeSsl: "false"
      authenticationRef:
        name: mimir-auth-trigger
```

**Note**: You have to preconfigure a `TriggerAuthentication` KEDA resource to authenticate against the Mimir endpoint. The values will be given by Giant Swarm when setting the Mimir endpoint.

You can see how the `ScaledObject` configures two triggers, one for GPU memory and another one for GPU utilization, establishing some reasonable thresholds. Together, it defines an HPA based on that metrics to select the percentage that will scale up or down the replicas.

Let's apply the manifests and check how those behave.

```bash
kubectl apply -f deploy/manifests
```

Verify the deployment and port forward the service to run some tests:

```bash
# Check pod status
kubectl get pods -n ml-workloads

# Check if the service is responding
kubectl port-forward -n ml-workloads svc/ml-demo 8080:80
```

## Step 5: Run some stress tests

Now, it is time to run some load tests to generate sufficient GPU compute and memory load to trigger the scale events. Test first that service works as expected:

```bash
curl http://localhost:8080/health
curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d '{}'
```

Later, generate load using the `/load` endpoint:

```bash
curl -X POST http://localhost:8080/load -H "Content-Type: application/json" -d '{"intensity": 5, "duration": 60}'
```

Observe the HPA status, to see how the average metrics looks like and how number of replicas adapt to that load.

```bash
kubectl get hpa keda-hpa-ml-demo -o jsonpath='{.status}' | jq .
```

You can also access the general [Grafana dashboard]({{< relref "/overview/observability/dashboard-management" >}}) to visualize the GPU consumption nicer.

## Next steps

Now that you have HPA configured with custom KEDA and Mimir, consider these additional optimizations:

- **[Configure cluster autoscaling]({{< relref "/tutorials/fleet-management/cluster-management/aws-cluster-scaling" >}})** to automatically provision GPU nodes when needed
- **[Create custom dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}})** to visualize your GPU scaling patterns
- **[Implement resource quotas]({{< relref "/tutorials/fleet-management/cluster-management/node-pools#resource-management" >}})** to control GPU allocation in multi-tenant environments

For more advanced scaling scenarios or troubleshooting, contact Giant Swarm support with your HPA configuration and scaling requirements.
