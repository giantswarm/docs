+++
title = "Limiting Pod Communication with Network Policies"
description = "Guide on how to limit Pod communication using Network Policies"
date = "2017-11-10"
type = "page"
weight = 60
tags = ["tutorial"]
+++

# Limiting Pod Communication with Network Policies

You can limit communication to Pods using the Network Policy API of Kubernetes.

Currently the API only includes Ingress rules, i.e. you can only limit traffic to groups of Pods. Egress rules, limiting outgoing traffic from Pods, are coming to the API soon. Until then you have to use the Egress functionality of our Network Plugin, Calico, directly.

Here we give an overview and introduction of how to create and use these policies.

## Ingress Network Policies

NetworkPolicy resources in Kubernetes use labels to select pods and define rules which specify what traffic is allowed to the selected pods.

By default all Pods in a cluster are non-isolated and accept traffic from any source.

As soon as you have a NetworkPolicy that selects a certain group of Pods, those Pods become isolated and reject any traffic that is not allowed by any NetworkPolicy.

Note that Network Policies are additive, so having two Network Policies that select the same Pods will result in allowing both defined policies.

Keep in mind that a NetworkPolicy is applied to a particular Namespace and only selects Pods in that particular Namespace.

### Default Policies

You can create default policies for a Namespace by creating a NetworkPolicy that select all Pods:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

Applying the above policy with 

```nohighlight
kubectl -n <namespace> apply -f default-deny.yaml 
```

will result in all traffic to all Pods in the Namespace to be denied.

Note that the namespace needs to exist before you apply the NetworkPolicy to it.

### Creating Selective Network Policies

No matter if you set default policies or not, you can limit access to certain Pods by creating a NetworkPolicy that selects them.

#### Allowing Specific Pod to Pod Access

In the following example we allow traffic to Pods labeled `role: backend` from Pods with the `role: frontend` label and only on TCP port 6379.

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: backend-access
spec:
  podSelector:
    matchLabels:
      role: backend
  ingress:
    - from:
      - podSelector:
          matchLabels:
            role: frontend
      ports:
        - protocol: TCP
          port: 6379
```

You need to apply this policy to the Namespace that the backend Pods live in.

```nohighlight
kubectl -n <namespace> apply -f backend-access.yaml
```

#### Allowing Pod to Pod Access within a Namespace

In some cases you might want to allow all intra-namespace communication. For this you can use open Pod selectors that catch all Pods.

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: intra-namespace
  namespace: freeforall
spec:
  podSelector:
  ingress:
    - from:
      - NamespaceSelector:
          matchLabels:
            name: freeforall
```

Note that the namespace you apply this policy to needs to carry a label `name:` similar to the actual name key in its metadata:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: freeforall
  labels:
    name: freeforall
```

After creating the namespace, you can then create the `NetworkPolicy`.

```nohighlight
kubectl apply -f freeforall-namespace.yaml
kubectl apply -f intra-namespace-policy.yaml
```

#### Allowing Traffic from Outside the Cluster

In the case that you have publicly exposed a Service through Ingress and you have a default-deny policy in place or just want to limit that traffic to a specific port, you need a Network Policy like the following.

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-external
spec:
  podSelector:
    matchLabels:
      app: web
  ingress:
  - from: []
    ports:
    - port: 80
```

The above will allow any traffic (no matter if outside or inside your cluster) to the Pods on port 80.

## Limiting Egress Traffic with Calico Policies

For creating Egress Policies we currently have to circumvent Kubernetes and talk directly to Calico [using `calicoctl`](https://docs.projectcalico.org/v2.2/getting-started/kubernetes/tutorials/using-calicoctl).

__Note__: Running and configuring `calicoctl` in your cluster requires privileged access to your nodes and etcd. Please do not do this without consulting Giant Swarm Support first, as these actions can pose significant risk to the health of your cluster.

Let's take the following use case as an example:

> We have a Kubernetes cluster that has a connection to a legacy backend in our data center. The legacy backend can be reached through certain IP (here 8.8.8.8 for testing purposes). Now, we want to have control over which Pods should be allowed to access that backend. As the backend does not live inside of our cluster we cannot work with Ingress rules. We decide to limit access to the backend to a specific trusted namespace.

For this we need two policies:

1. Deny Egress for the whole cluster
2. Allow Egress for the trusted namespace

### 1. Default Deny Egress

Following Egress policy denies outgoing connections from all sources to our specified destination. With `order: 500` we ensure that this is applied before any Kubernetes policies.

```yaml
apiVersion: v1
kind: policy
metadata:
  name: default-deny-egress
spec:
  order: 500
  egress:
  - action: deny
    destination:
      net: 8.8.8.8
    source: {}
```

We apply the policy with

```nohighlight
calicoctl create -f default-deny-egress.yaml
```

### 2. Allow Egress for Trusted Namespace

For this we create another policy, just selecting our `trusted` namespace. Again, the order of 400 will ensure this is applied before any Kubernetes policies.

```yaml
apiVersion: v1
kind: policy
metadata:
  name: trusted-namespace
spec:
  order: 400
  egress:
  - action: allow
    destination:
      net: 8.8.8.8
    source:
      selector: calico/k8s_ns == 'trusted'
```

and apply the policy with

```nohighlight
calicoctl create -f trusted-namespace.yaml
```

Now connections to `8.8.8.8` will only be possible from Pods living in the namespace called `trusted`. As with Ingress Policies all other connections from the Pods will be disallowed.

## Further Reading

- [The Unoffical Guide to Kubernetes Network Policies](https://ahmet.im/blog/kubernetes-network-policy/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
- [Declare Network Policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)
- [Calico Getting Started](https://docs.projectcalico.org/v2.2/getting-started/)
