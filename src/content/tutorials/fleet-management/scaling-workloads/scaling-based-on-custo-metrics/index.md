---
title: Scaling workloads based on custom GPU metrics
description: Learn how to configure Horizontal Pod Autoscaling with Prometheus adapter to scale workloads based on custom GPU DCGM metrics in Giant Swarm clusters.
weight: 10
menu:
  principal:
    parent: tutorials-fleet-management-scaling
    identifier: tutorials-fleet-management-scaling-custom-gpu-metrics
last_review_date: 2025-10-22
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How can I scale workloads based on GPU utilization?
  - How do I configure HPA with custom GPU metrics?
  - How do I use Prometheus adapter with DCGM metrics?
  - How can I autoscale based on GPU memory usage?
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
- `DCGM_FI_DEV_FB_USED` - GPU framebuffer memory used
- `DCGM_FI_DEV_FB_TOTAL` - GPU framebuffer memory total

## Step 2: Install Prometheus adapter

The Prometheus adapter enables HPA to query custom metrics from Prometheus. Install it using the Giant Swarm App Platform:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: prometheus-adapter
  namespace: giantswarm-system
spec:
  catalog: giantswarm
  name: prometheus-adapter
  namespace: kube-system
  version: 4.10.0
  config:
    configMap:
      name: prometheus-adapter-user-values
      namespace: giantswarm-system
```

Create the configuration ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-adapter-user-values
  namespace: giantswarm-system
data:
  values: |
    prometheus:
      url: http://mimir-query-frontend.mimir-system.svc.cluster.local:8080
      port: 8080
    rules:
      custom:
      - seriesQuery: 'DCGM_FI_DEV_GPU_UTIL{namespace!="",pod!=""}'
        resources:
          overrides:
            namespace:
              resource: namespace
            pod:
              resource: pod
        name:
          matches: "^DCGM_FI_DEV_GPU_UTIL"
          as: "gpu_utilization"
        metricsQuery: 'avg(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)'
      - seriesQuery: 'DCGM_FI_DEV_MEM_COPY_UTIL{namespace!="",pod!=""}'
        resources:
          overrides:
            namespace:
              resource: namespace
            pod:
              resource: pod
        name:
          matches: "^DCGM_FI_DEV_MEM_COPY_UTIL"
          as: "gpu_memory_utilization"
        metricsQuery: 'avg(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)'
```

Apply both resources:

```bash
kubectl apply -f prometheus-adapter-app.yaml
kubectl apply -f prometheus-adapter-config.yaml
```

## Step 3: Verify custom metrics API

Once the Prometheus adapter is running, verify that custom metrics are available:

```bash
# Check if the custom metrics API is available
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1" | jq .

# List available custom metrics
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/default/pods/*/gpu_utilization" | jq .

# Check specific GPU utilization metrics for your pods
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/your-namespace/pods/*/gpu_utilization" | jq .
```

You should see your GPU metrics exposed through the custom metrics API.

## Step 4: Configure HPA with GPU metrics

Create an HPA resource that scales based on GPU utilization. Here's an example for a machine learning inference service:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ml-inference-hpa
  namespace: ml-workloads
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ml-inference-service
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Pods
    pods:
      metric:
        name: gpu_utilization
      target:
        type: AverageValue
        averageValue: "70"  # Scale when average GPU utilization exceeds 70%
  - type: Pods
    pods:
      metric:
        name: gpu_memory_utilization
      target:
        type: AverageValue
        averageValue: "80"  # Also consider GPU memory utilization
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 300  # Wait 5 minutes before scaling up
      policies:
      - type: Percent
        value: 50  # Scale up by 50% of current replicas
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 600  # Wait 10 minutes before scaling down
      policies:
      - type: Percent
        value: 25  # Scale down by 25% of current replicas
        periodSeconds: 60
```

Apply the HPA configuration:

```bash
kubectl apply -f ml-inference-hpa.yaml
```

## Step 5: Test the autoscaling behavior

Monitor your HPA to ensure it's working correctly:

```bash
# Check HPA status
kubectl get hpa ml-inference-hpa -n ml-workloads

# Watch HPA events
kubectl describe hpa ml-inference-hpa -n ml-workloads

# Monitor scaling events
kubectl get events -n ml-workloads --field-selector reason=SuccessfulRescale
```

Generate some GPU load to test scaling:

```bash
# Deploy a GPU stress test pod
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: gpu-stress-test
  namespace: ml-workloads
spec:
  restartPolicy: Never
  runtimeClassName: nvidia
  containers:
  - name: gpu-stress
    image: nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04
    resources:
      limits:
        nvidia.com/gpu: 1
    command: ["/bin/sh"]
    args: ["-c", "while true; do /usr/local/cuda/samples/1_Utilities/deviceQuery/deviceQuery; sleep 10; done"]
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
EOF
```

## Step 6: Monitor and fine-tune

Use Grafana to monitor your scaling behavior and GPU utilization:

1. **Create a custom dashboard** with panels showing:

   - GPU utilization over time
   - Number of pod replicas
   - HPA scaling events
   - Application performance metrics

2. **Set up alerts** for unusual scaling patterns:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: gpu-scaling-alerts
  namespace: ml-workloads
  labels:
    observability.giantswarm.io/tenant: my-team
spec:
  groups:
  - name: gpu-scaling
    rules:
    - alert: GPUUtilizationHigh
      expr: avg(DCGM_FI_DEV_GPU_UTIL{namespace="ml-workloads"}) > 90
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High GPU utilization detected"
        description: "GPU utilization has been above 90% for more than 5 minutes"

    - alert: HPAScalingStuck
      expr: increase(kube_hpa_status_current_replicas{namespace="ml-workloads"}[30m]) == 0 and avg(DCGM_FI_DEV_GPU_UTIL{namespace="ml-workloads"}) > 80
      for: 10m
      labels:
        severity: critical
      annotations:
        summary: "HPA not scaling despite high GPU utilization"
        description: "HPA hasn't scaled for 30 minutes despite high GPU usage"
```

## Advanced configuration

### Multiple GPU metrics

You can combine multiple GPU metrics for more sophisticated scaling decisions:

```yaml
metrics:
- type: Pods
  pods:
    metric:
      name: gpu_utilization
    target:
      type: AverageValue
      averageValue: "70"
- type: Pods
  pods:
    metric:
      name: gpu_memory_utilization
    target:
      type: AverageValue
      averageValue: "80"
- type: Resource
  resource:
    name: cpu
    target:
      type: Utilization
      averageUtilization: 60
```

### Custom metric calculations

For more complex scenarios, create custom recording rules in Prometheus:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: gpu-custom-metrics
  namespace: ml-workloads
spec:
  groups:
  - name: gpu-metrics
    interval: 30s
    rules:
    - record: gpu:utilization:rate5m
      expr: avg_over_time(DCGM_FI_DEV_GPU_UTIL[5m])
    - record: gpu:memory_pressure:ratio
      expr: DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL
```

## Troubleshooting

### Common issues and solutions

**HPA shows "unknown" metrics:**

- Verify the Prometheus adapter is running: `kubectl get pods -n kube-system -l app=prometheus-adapter`
- Check adapter logs: `kubectl logs -n kube-system -l app=prometheus-adapter`
- Ensure your metrics query returns data in Grafana

**Scaling is too aggressive:**

- Increase `stabilizationWindowSeconds` in the HPA behavior configuration
- Reduce the scaling percentage in policies
- Adjust the target metric values

**GPU metrics not available:**

- Verify DCGM exporter is running and configured correctly
- Check ServiceMonitor configuration and labels
- Ensure GPU workloads are actually running and generating metrics

**Prometheus adapter can't reach Mimir:**

- Verify the Mimir query frontend URL in the adapter configuration
- Check network policies that might block communication
- Ensure the adapter has proper RBAC permissions

## Best practices

1. **Start conservative**: Begin with higher metric thresholds and longer stabilization windows, then optimize based on your workload patterns.

2. **Monitor costs**: GPU instances are expensive. Set appropriate `maxReplicas` limits and consider using mixed instance types.

3. **Use multiple metrics**: Combine GPU utilization with memory usage and application-specific metrics for better scaling decisions.

4. **Test thoroughly**: Use load testing to validate your scaling configuration before production deployment.

5. **Set up proper monitoring**: Create dashboards and alerts to track scaling behavior and catch issues early.

## Next steps

Now that you have HPA configured with custom GPU metrics, consider these additional optimizations:

- **[Configure cluster autoscaling]({{< relref "/tutorials/fleet-management/cluster-management/aws-cluster-scaling" >}})** to automatically provision GPU nodes when needed
- **[Set up Karpenter]({{< relref "/tutorials/fleet-management/cluster-management/aws-cluster-scaling#karpenter" >}})** for faster and more efficient node provisioning
- **[Create custom dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}})** to visualize your GPU scaling patterns
- **[Implement resource quotas]({{< relref "/tutorials/fleet-management/cluster-management/node-pools#resource-management" >}})** to control GPU allocation in multi-tenant environments

For more advanced scaling scenarios or troubleshooting, contact Giant Swarm support with your HPA configuration and scaling requirements.
