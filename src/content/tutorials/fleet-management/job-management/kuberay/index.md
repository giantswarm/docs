---
linkTitle: KubeRay
title: Deploying Ray clusters with KubeRay on Giant Swarm
description: Learn how to deploy and manage distributed Ray clusters using KubeRay operator on Giant Swarm Kubernetes clusters for machine learning and distributed computing workloads.
weight: 10
menu:
  principal:
    parent: tutorials-fleet-management-job-management
    identifier: tutorials-fleet-management-job-management-kuberay
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I deploy Ray clusters on Giant Swarm using KubeRay?
  - How do I configure KubeRay for distributed machine learning workloads?
  - What are the best practices for running Ray on Kubernetes?
  - How can I scale Ray clusters dynamically on Giant Swarm?
  - How do I monitor Ray cluster performance and resource usage?
last_review_date: 2025-10-22
---

This tutorial explains how to deploy and manage distributed Ray clusters using the KubeRay operator on Giant Swarm Kubernetes clusters. Ray is an open-source framework for distributed computing that simplifies the development of scalable machine learning and distributed applications.

## Overview

[Ray](https://ray.io/) is a unified framework for scaling AI and Python applications. It provides a simple, universal API for building distributed applications and includes libraries for machine learning, reinforcement learning, and hyperparameter tuning. [KubeRay](https://ray-project.github.io/kuberay/) is the official Kubernetes operator for Ray that automates the deployment, scaling, and management of Ray clusters on Kubernetes.

Key benefits of using Ray with KubeRay on Giant Swarm:

- **Scalable distributed computing**: Automatically scale Ray clusters based on workload demands
- **Native Kubernetes integration**: Leverage Kubernetes features like resource management, networking, and monitoring
- **Machine learning workflows**: Run distributed training, hyperparameter tuning, and inference workloads
- **Resource efficiency**: Dynamic resource allocation and cluster autoscaling

## Prerequisites

Before starting this tutorial, ensure you have:

- A running Giant Swarm workload cluster with sufficient resources
- `kubectl` configured to access your workload cluster
- Basic understanding of Kubernetes concepts (pods, services, deployments)
- Familiarity with Python and distributed computing concepts

## Installing the KubeRay operator

The KubeRay operator manages the lifecycle of Ray clusters on Kubernetes. You can install it using the Giant Swarm App Platform.

### Using the App Platform

Create an `App` resource to install the KubeRay operator from the Giant Swarm catalog:

```bash
export CLUSTER=your-cluster-id

kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=${CLUSTER} \
  --name=kuberay-operator \
  --target-namespace=kuberay-system \
  --version=1.1.0 > kuberay-operator.yaml

kubectl apply -f kuberay-operator.yaml
```

### Verifying the installation

Check that the KubeRay operator is running:

```bash
kubectl get pods -n kuberay-system

NAME                                READY   STATUS    RESTARTS   AGE
kuberay-operator-7b5c8f6d4b-xyz12   1/1     Running   0          2m
```

Verify that the Custom Resource Definitions (CRDs) are installed:

```bash
kubectl get crd | grep ray

rayclusters.ray.io                    2025-10-22T10:00:00Z
rayjobs.ray.io                        2025-10-22T10:00:00Z
rayservices.ray.io                    2025-10-22T10:00:00Z
```

## Deploying a Ray cluster

Once the KubeRay operator is installed, you can deploy Ray clusters using the `RayCluster` custom resource.

### Basic Ray cluster configuration

Create a basic Ray cluster configuration:

```yaml
apiVersion: ray.io/v1alpha1
kind: RayCluster
metadata:
  name: sample-raycluster
  namespace: default
spec:
  rayVersion: '2.8.0'
  enableInTreeAutoscaling: true
  headGroupSpec:
    rayStartParams:
      dashboard-host: '0.0.0.0'
      block: 'true'
    template:
      spec:
        containers:
        - name: ray-head
          image: rayproject/ray:2.8.0
          ports:
          - containerPort: 6379
            name: gcs-server
          - containerPort: 8265
            name: dashboard
          - containerPort: 10001
            name: client
          resources:
            limits:
              cpu: "2"
              memory: "4Gi"
            requests:
              cpu: "1"
              memory: "2Gi"
  workerGroupSpecs:
  - replicas: 2
    minReplicas: 1
    maxReplicas: 5
    groupName: small-group
    rayStartParams: {}
    template:
      spec:
        containers:
        - name: ray-worker
          image: rayproject/ray:2.8.0
          resources:
            limits:
              cpu: "2"
              memory: "4Gi"
            requests:
              cpu: "1"
              memory: "2Gi"
```

Save this configuration as `ray-cluster.yaml` and apply it:

```bash
kubectl apply -f ray-cluster.yaml
```

### Verifying the Ray cluster deployment

Check the status of your Ray cluster:

```bash
kubectl get raycluster

NAME                 DESIRED WORKERS   AVAILABLE WORKERS   STATUS   AGE
sample-raycluster    2                 2                   ready    3m
```

List the Ray cluster pods:

```bash
kubectl get pods -l ray.io/cluster=sample-raycluster

NAME                                          READY   STATUS    RESTARTS   AGE
sample-raycluster-head-xxxxx                  1/1     Running   0          3m
sample-raycluster-worker-small-group-xxxxx    1/1     Running   0          3m
sample-raycluster-worker-small-group-yyyyy    1/1     Running   0          3m
```

## Accessing the Ray cluster

### Using the Ray Dashboard

The Ray Dashboard provides a web interface for monitoring your Ray cluster. Forward the dashboard port to access it locally:

```bash
kubectl port-forward service/sample-raycluster-head-svc 8265:8265
```

Open your browser and navigate to `http://localhost:8265` to access the Ray Dashboard.

### Connecting to the Ray cluster

To submit jobs to your Ray cluster, you can connect from within the cluster or from external clients.

#### From within the cluster

Execute commands directly in the Ray head pod:

```bash
export HEAD_POD=$(kubectl get pods --selector=ray.io/node-type=head -o custom-columns=POD:metadata.name --no-headers)

kubectl exec -it $HEAD_POD -- python -c "
import ray
ray.init()
print('Ray cluster resources:', ray.cluster_resources())
"
```

#### From external clients

Create a service to expose the Ray cluster externally:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ray-cluster-external
spec:
  type: LoadBalancer
  selector:
    ray.io/cluster: sample-raycluster
    ray.io/node-type: head
  ports:
  - name: client
    port: 10001
    targetPort: 10001
```

## Running distributed workloads

### Example: Distributed data processing

Here's an example of running a distributed data processing job on your Ray cluster:

```python
import ray
import numpy as np

# Connect to the Ray cluster
ray.init(address="ray://sample-raycluster-head-svc:10001")

@ray.remote
def process_data_chunk(data_chunk):
    # Simulate data processing
    return np.sum(data_chunk ** 2)

# Create sample data
data = np.random.rand(1000000)
chunks = np.array_split(data, 10)

# Process data in parallel
futures = [process_data_chunk.remote(chunk) for chunk in chunks]
results = ray.get(futures)

print(f"Processed {len(chunks)} chunks, total result: {sum(results)}")
```

### Example: Distributed machine learning

Ray integrates well with popular machine learning libraries. Here's an example using Ray Train:

```python
import ray
from ray import train
from ray.train import ScalingConfig
import torch
import torch.nn as nn

ray.init(address="ray://sample-raycluster-head-svc:10001")

def train_func():
    model = nn.Linear(10, 1)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(100):
        # Training logic here
        loss = torch.randn(1, requires_grad=True)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item()}")

# Run distributed training
trainer = train.torch.TorchTrainer(
    train_func,
    scaling_config=ScalingConfig(num_workers=2, use_gpu=False)
)

result = trainer.fit()
```

## Scaling and resource management

### Autoscaling configuration

KubeRay supports automatic scaling of worker nodes based on resource demands:

```yaml
apiVersion: ray.io/v1alpha1
kind: RayCluster
metadata:
  name: autoscaling-raycluster
spec:
  rayVersion: '2.8.0'
  enableInTreeAutoscaling: true
  autoscalerOptions:
    upscalingMode: Default
    idleTimeoutSeconds: 60
    resources:
      limits:
        cpu: "4"
        memory: "8Gi"
      requests:
        cpu: "2"
        memory: "4Gi"
  # ... rest of the configuration
```

### Resource requests and limits

Configure appropriate resource requests and limits for your workloads:

```yaml
resources:
  limits:
    cpu: "4"
    memory: "8Gi"
    # For GPU workloads
    nvidia.com/gpu: "1"
  requests:
    cpu: "2"
    memory: "4Gi"
```

## Monitoring and observability

### Using Giant Swarm's observability platform

Giant Swarm provides built-in observability capabilities. Create a `ServiceMonitor` to collect Ray metrics:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: ray-cluster-metrics
  namespace: default
  labels:
    observability.giantswarm.io/tenant: my-tenant
    giantswarm.io/service-type: managed
spec:
  endpoints:
  - interval: 30s
    path: /metrics
    port: metrics
    scrapeTimeout: 25s
  selector:
    matchLabels:
      ray.io/cluster: sample-raycluster
```

### Ray-specific monitoring

Ray provides built-in metrics and monitoring capabilities:

- **Ray Dashboard**: Web interface for cluster monitoring
- **Ray State API**: Programmatic access to cluster state
- **Custom metrics**: Export application-specific metrics

## Best practices

### Resource management

1. **Set appropriate resource requests and limits**: Ensure containers have sufficient resources while preventing resource contention
2. **Use node selectors and taints**: Isolate Ray workloads on dedicated nodes when needed
3. **Configure autoscaling**: Enable cluster autoscaling to handle varying workloads efficiently

### Security considerations

1. **Network policies**: Implement network policies to control traffic between Ray components
2. **RBAC**: Configure appropriate role-based access control for Ray resources
3. **Secrets management**: Use Kubernetes secrets for sensitive configuration

### Performance optimization

1. **Cluster sizing**: Start with smaller clusters and scale based on actual usage
2. **Resource allocation**: Monitor resource utilization and adjust requests/limits accordingly
3. **Data locality**: Consider data placement and network topology for optimal performance

## Troubleshooting

### Common issues

**Ray cluster not starting**:

- Check resource availability in your cluster
- Verify the Ray image version compatibility
- Review pod logs for startup errors

```bash
kubectl logs -l ray.io/cluster=sample-raycluster
```

**Connection issues**:

- Verify service configurations and port forwarding
- Check network policies and firewall rules
- Ensure Ray client and cluster versions are compatible

**Performance issues**:

- Monitor resource utilization using the Ray Dashboard
- Check for resource bottlenecks in Kubernetes metrics
- Review Ray application logs for performance insights

### Getting support

If you encounter issues that cannot be resolved using the troubleshooting steps above, contact Giant Swarm support with the following information:

- Output of `kubectl get raycluster -o yaml`
- Ray cluster pod logs: `kubectl logs -l ray.io/cluster=your-cluster-name`
- Resource utilization metrics from the Ray Dashboard

## Cleanup

To remove the Ray cluster and operator:

```bash
# Delete the Ray cluster
kubectl delete raycluster sample-raycluster

# Delete the KubeRay operator app
kubectl delete -f kuberay-operator.yaml

# Clean up any additional resources
kubectl delete namespace kuberay-system
```

## Next steps

Now that you have a working Ray cluster on Giant Swarm, consider exploring:

- [Ray's machine learning libraries](https://docs.ray.io/en/latest/ray-overview/ray-libraries.html) for advanced ML workflows
- [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) for model serving and inference
- [Ray Tune](https://docs.ray.io/en/latest/tune/index.html) for hyperparameter optimization
- Integration with Giant Swarm's [GPU support]({{< relref "/tutorials/fleet-management/cluster-management/gpu" >}}) for accelerated workloads

## Further reading

- [Ray Documentation](https://docs.ray.io/)
- [KubeRay Documentation](https://ray-project.github.io/kuberay/)
- [Ray on Kubernetes Best Practices](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
- [Giant Swarm App Platform]({{< relref "/tutorials/fleet-management/app-platform" >}})
