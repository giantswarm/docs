---
title: Control the application connectivity
description: Understand how basic connectivity works in the platform and which options are available for exposing your app.
weight: 60
last_review_date: 2024-09-01
menu:
  principal:
    parent: getting-started
    identifier: getting-started-understand-connectivity
owner:
  - https://github.com/orgs/giantswarm/teams/sig-cabbage
user_questions:
  - How does basic connectivity work in the platform?
  - What are the options for service connectivity in the platform?
---

By default, the workload clusters created by the platform expose the Kubernetes API endpoint publicly, and the cluster workloads have internet access. It's what we call a `public` cluster. This guide focuses on understanding how these cluster's networking works and which options are available for managing your app's connectivity. In case you want to know more about `private clusters`, read [this guide]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/private-clusters" >}}).

The Container Network Interface (CNI) plugin manages connectivity within the cluster. Our platform uses [Cilium](https://docs.cilium.io/en/stable/index.html) as a network interface implementation. In addition to offering connectivity between workloads, it also provides network security policies to control traffic between your applications.

In this guide, we give an overview and introduction to how to create and use these policies.

## Requirements

First of all, you need a running workload cluster. If you don't have one, please first [create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}). Second, you need to deploy the `hello-world` application explained [here]({{< relref "/getting-started/install-an-application" >}}).

## Step 1: Understand network policies

By default, with an exception for `kube-system` and `giantswarm` namespaces, all pods in the cluster are non-isolated and accept traffic from any source.

As soon as a `NetworkPolicy` resource is applied that selects a certain group of pods, those pods become isolated and reject any traffic that's not allowed by any other `NetworkPolicy`.

Note that network policies are additive, so having two network policies that select the same pods will allow both defined policies.

Keep in mind that a `NetworkPolicy` is applied to a particular namespace and only selects pods for that specific namespace.

### Network policy syntax

The network policy resource is part of the API group `networking.k8s.io`. Currently, it's in version `v1`.

The `spec` of the resource mainly consists of three parts:

- `podSelector`: Use labels to select the group of pods for which the rules will be applied.

- `policyTypes`: Which could be `Ingress`, `Egress` or both. This field will determine if the rules will be applied to incoming and/or outgoing traffic. If it's not defined, then `Ingress` will be enabled by default, and `Egress` will only be enabled when the rules are defined.

- `ingress`/`egress`: these sections allow a list of `from` (Ingress) or `to` (Egress) and `ports` blocks. Each `from`/`to` block contains a range of IPs (`ipBlock`) and/or a list of namespaces selected by label (`namespaceSelector`) and/or a list of pods by label (`podSelector`). Select which IPs, namespaces or pods can talk to our target pod or to which IPs, namespaces, or pod our target can speak to. The `ports` block defines which ports are affected by this rule.

### Hello-world example

In our example, a `hello-world` application is running in the `default` namespace. It has a `NetworkPolicy` that allows traffic on port `8080` for the specific application.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: hello-world
  namespace: default
spec:
  ingress:
  - ports:
    - port: 8080
      protocol: TCP
  podSelector:
    matchLabels:
      app.kubernetes.io/instance: hello-world
      app.kubernetes.io/name: hello-world
  policyTypes:
  - Ingress
  - Egress
```

Let's deploy a [debug-toolbok](https://github.com/giantswarm/debug-toolbox) to check the connectivity.

```sh
$ kubectl gs template app \
  --catalog=giantswarm \
  --organization=testing \
  --cluster-name=fer01 \
  --name=debug-toolbox --app-name=fer01-debug-toolbox \
  --target-namespace=default \
  --version=1.0.0 | kubectl apply -f -
```

Wait few seconds until the pod is up and running and then run the command below to check the connectivity.

```sh
$ kubectl debug-toolbox -- sh
/ # curl -Is hello-world.default
/ HTTP/1.1 200 OK
/ Accept-Ranges: bytes ...

```

The avid reader will have wondered why you need a specific network policy for `hello-world` if there is no default deny policy limiting the traffic in the `default` namespace. The reason is because it's a good practice to ensure the application will work in environments where the default deny policy is in place. You can try removing the `hello-world` network policy and see that the application will still work.

## Step 2: Create a default network policy

Since the zero trust principle is well known and established widely in the industry, the recommendation is to deploy a default deny policy for all your namespaces. This way, you can control the traffic that goes in and out of your pods.

Let's create default policy for our `default` namespace by creating a `NetworkPolicy` that selects all pods as follows:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

The default policy shown above will limit ingress and egress traffic in the namespace applied. You can also restrict only for `egress` or `ingress`. Let's apply this policy to the `default` namespace and check hello-world application access.

```sh
$ kubectl apply -f default-deny.yaml
```

Now if you remove the `hello-world` network policy, the application won't work anymore.

```sh
$ kubectl delete netpol hello-world
$ kubectl exec -it debug-toolbox -- sh
/ curl -Is hello-world.default
/ <TIMEOUT>
```

## Step 3: Allow DNS traffic

As we mentioned before, we harden the clusters restricting the communication with pods in `kube-system` and `giantswarm` namespaces. In case you need to allow communication with a running pod in one of those namespaces you have to explicitly declare it. In the next example we enable the DNS traffic from the `debug-toolbox` pod:

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: debug-toolbox-dns
  namespace: default
spec:
  egress:
  - ports:
    - port: 53
      protocol: UDP
    - port: 1053
      protocol: UDP
    to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
  podSelector:
    matchLabels:
      app: debug-toolbox
  policyTypes:
  - Egress
```

__Warning__: By default, clusters run CoreDNS listening on port 1053 (for security reasons). So, you will need to include port `1053` on the list of ports.

Note that the policy is already deployed in the `default` namespace due to the chart enabled by default. It allows the DNS queries to be resolved like:

```sh
$ kubectl exec debug-toolbox -- nslookup hello-world
Server:		172.31.0.10
Address:	172.31.0.10:53

Name:	hello-world.default.svc.cluster.local
Address: 172.31.104.47
```

But removing the policy make it fail as following:

```sh
$ kubectl delete netpol debug-toolbox-dns
$ kubectl exec debug-toolbox -- nslookup hello-world
;; connection timed out; no servers could be reached
```

## Step 4: Allowing specific pod to pod access

Doing a step further, you can allow specific pod to pod access. In the following example, we allow the `debug-toolbox` pod to access the `hello-world` pod on port `8080` only, any other traffic will be blocked.

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-debug-toolbox-to-hello-world
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/name: hello-world
  ingress:
    - from:
      - podSelector:
          matchLabels:
            app: debug-toolbox
      ports:
        - port: 8080
          protocol: TCP
```

Apply the policy and check the connectivity:

```sh
$ kubectl apply -f allow-debug-toolbox-to-hello-world.yaml
$ kubectl exec -it debug-toolbox -- sh
/ curl -Is hello-world.default
/ HTTP/1.1 200 OK
/ ...
```

### Step 5: Allowing pod to pod access within a namespace

One last interesting scenario to explore is allowing pod-to-pod access within a namespace. In some cases, like in a test environment, you should enable all pods to communicate by default within the same namespace. In the following example, we allow pods to in the `default` namespace to communicate with each other.

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-default-namespace
  namespace: default
spec:
  podSelector:
  ingress:
 - from:
 - namespaceSelector:
          matchLabels:
            name: default
```

Note that the namespace you apply this policy too needs to carry a label `name:` similar to the actual name key in its metadata:

```sh
$ kubectl label namespace default name=default
```

Now let's delete all network policies and apply the `allow-default-namespace` policy so we can verify it works:

```sh
kubectl delete netpol --all -n default
kubectl apply -f allow-default-namespace.yaml
$ kubectl exec -it debug-toolbox -- sh
/ curl -Is hello-world.default
/ HTTP/1.1 200 OK
```

We've learnt how network policies work and the peculiarities in Giant Swarm clusters. However, the ideal configuration is to have a default deny policy in all your namespaces and allow only the necessary traffic to your applications. This way, you can control the traffic in your cluster and avoid any security issues.

## Next step

Since you learnt how to configure your application to communicate with other services, now let's dive into how [observe your application]({{< relref "/getting-started/observe-your-app" >}}).
