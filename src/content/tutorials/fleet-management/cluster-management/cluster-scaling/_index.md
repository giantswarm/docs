---
title: Cluster scaling
description: How to configure and manage the scaling of your workload clusters on Giant Swarm.
weight: 20
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-clusters-scaling
last_review_date: 2024-12-13
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I scale my workload clusters on Giant Swarm using Karpenter and cluster autoscaler?
---

In Gs we combine cluster autoscaler and karpenter to have the better scaling possible in your workload clusters. This tutorial will guide you through the configuration and management of the scaling of your workload clusters on Giant Swarm.



## Introduction

Karpenter is an open-source Kubernetes cluster autoscaler that automatically adjusts the number of nodes in your cluster based on the resource requests of your workloads. It is designed to optimize resource utilization and cost efficiency by provisioning just the right amount of infrastructure, precisely when it is needed.

## How Karpenter Works

1. **Event-Driven Scaling**: Karpenter monitors the Kubernetes API for unschedulable pods, which occur when there are not enough resources to schedule a pod.

2. **Node Provisioning**: When unschedulable pods are detected, Karpenter decides the best way to provision new nodes by evaluating the pod’s resource requests and constraints. It uses cloud provider APIs to create new instances that can accommodate the workloads.

3. **Node Cleanup**: Karpenter also performs node termination, removing nodes that are underutilized to save costs, based on policies you define.

4. **Integration with Cloud Providers**: Karpenter interacts with the cloud provider’s APIs (AWS, GCP, etc.) to create and terminate instances. It considers factors such as instance types, zones, and pricing options to make optimal decisions.

## Prerequisites

- **Kubernetes Cluster**: Ensure you have access to a Kubernetes cluster where Karpenter is installed by default.
- **IAM Role/Permissions**: Karpenter needs permissions to manage instances on your cloud provider. Ensure that the Kubernetes service account used by Karpenter has the necessary permissions.

## Configuring Karpenter

### Step 1: Understand Provisioner Configuration

Karpenter uses a custom resource definition (CRD) called `Provisioner` to define how nodes should be provisioned. A `Provisioner` specifies constraints such as instance types, zones, and resource limits. Here is an example configuration:

```yaml
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: default
spec:
  limits:
    resources:
      cpu: 1000
      memory: 4000Gi
  provider:
    instanceType: t3.medium
    zone: us-west-2a
  ttlSecondsAfterEmpty: 300
  requirements:
    - key: "karpenter.sh/capacity-type"
      operator: In
      values: ["spot", "on-demand"]
  labels:
    environment: "production"
```

### Step 2: Create or Modify a Provisioner

1. **Create a new Provisioner**: If you need to create a new provisioner, you can apply a YAML configuration like the one above using `kubectl`.

   ```bash
   kubectl apply -f provisioner.yaml
   ```

2. **Modify an existing Provisioner**: To modify an existing provisioner, edit the resource directly.

   ```bash
   kubectl edit provisioner default
   ```

### Step 3: Configure Node Selection

- **Instance Types**: Specify which instance types are allowed to be used. This is crucial for cost management and performance requirements.

- **Zones and Regions**: Define which availability zones and regions your nodes can be provisioned in to ensure your data locality and redundancy requirements are met.

- **TTL for Empty Nodes**: `ttlSecondsAfterEmpty` specifies how long a node should remain in the cluster after it has become empty. This helps in reducing costs by terminating unused nodes.

### Step 4: Test Autoscaling

To test Karpenter's functionality, deploy a workload that exceeds the current cluster capacity.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cpu-hog
spec:
  replicas: 10
  selector:
    matchLabels:
      app: cpu-hog
  template:
    metadata:
      labels:
        app: cpu-hog
    spec:
      containers:
      - name: cpu-hog
        image: vish/stress
        resources:
          requests:
            cpu: "1"
        args:
        - -cpus
        - "1"
```

Apply this deployment with:

```bash
kubectl apply -f cpu-hog-deployment.yaml
```

### Step 5: Monitor and Validate

- **Check Pods**: Ensure that pods are scheduled as expected.

  ```bash
  kubectl get pods
  ```

- **Check Nodes**: Verify that new nodes are being provisioned by Karpenter.

  ```bash
  kubectl get nodes
  ```

- **Logs and Metrics**: Review Karpenter logs for any errors and monitor metrics to ensure it is functioning as expected.

  ```bash
  kubectl logs -n karpenter -l app.kubernetes.io/name=karpenter
  ```

## Best Practices

- **Cost Optimization**: Use a combination of on-demand and spot instances to balance cost and availability.
- **Resource Limits**: Set reasonable resource limits in your provisioners to prevent over-provisioning.
- **Regular Audits**: Periodically review and adjust provisioner settings based on workload changes and cost considerations.

## Conclusion

Karpenter provides a powerful and flexible solution for dynamically scaling your Kubernetes clusters. By configuring provisioners according to your workload needs and cost constraints, you can ensure optimal resource utilization and efficiency.

For more detailed information, consider referring to Karpenter's [official documentation](https://karpenter.sh/docs/).
