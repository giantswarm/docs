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
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - How does basic connectivity work in the platform?
  - What are the options for service connectivity in the platform?
---

By default, workload clusters created by the platform expose the Kubernetes API endpoint publicly, and cluster workloads have outbound internet access. This is what we call a "public" cluster, in contrast to "private" clusters, which aren't reachable from the public internet. This guide covers how public cluster networking works and which options are available for managing an app's connectivity. To learn more about private clusters, read [this guide]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/private-clusters" >}}).

The Container Network Interface (CNI) plugin manages connectivity within the cluster. Our platform uses [Cilium](https://docs.cilium.io/en/stable/index.html) as a network interface implementation. In addition to offering connectivity between workloads, it also provides network security policies to control traffic between applications.

In this guide, we give an overview and introduction to how to create and use these policies.

## Requirements

This guide will configure networking for the `hello-world` app on a workload cluster. [Create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}) to use, or choose an already running cluster. Then, deploy the `hello-world` application as explained [here]({{< relref "/getting-started/install-an-application" >}}).

## Step 1: Understand network policies

By default, all pods in the cluster, except for those in Giant Swarm-controlled namespaces, are non-isolated and accept traffic from any source.

As soon as a `NetworkPolicy` resource is applied that selects a certain group of pods, those pods become isolated and reject any traffic that's not allowed by any other `NetworkPolicy`.

Note that network policies are additive, so having two network policies that select the same pods will allow both defined policies.

Keep in mind that a `NetworkPolicy` is applied to a particular namespace and only selects pods for that specific namespace.

### Network policy syntax

The network policy resource is part of the API group `networking.k8s.io`. Currently, it's in version `v1`.

The `spec` of the resource mainly consists of three parts:

- `podSelector`: Use labels to select the group of pods for which the rules will be applied.

- `policyTypes`: Which could be `Ingress`, `Egress` or both. This field will determine if the rules will be applied to incoming and/or outgoing traffic. If it's not defined, then `Ingress` will be enabled by default, and `Egress` will only be enabled when the rules are defined.

- `ingress`/`egress`: these sections allow a list of `from` (Ingress) or `to` (Egress) and `ports` blocks. Each `from`/`to` block contains a range of IPs (`ipBlock`) and/or a list of namespaces selected by label (`namespaceSelector`) and/or a list of pods by label (`podSelector`). These blocks declare which IPs, namespaces or pods can connect to the target pod or to which IPs, namespaces, or pods the target can connect. The `ports` block defines which ports are affected by this rule.

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

Let's deploy a [debug-toolbox](https://github.com/giantswarm/debug-toolbox) to check the connectivity.

```sh
kubectl gs template app \
  --catalog=giantswarm \
  --organization=testing \
  --cluster-name=fer01 \
  --name=debug-toolbox --app-name=fer01-debug-toolbox \
  --target-namespace=default \
  --version=1.0.0 | kubectl apply -f -
```

Wait few seconds until the pod is up and running and then run the command below to check the connectivity.

```text
$ kubectl debug-toolbox -- sh
/ # curl -Is hello-world.default
/ HTTP/1.1 200 OK
/ Accept-Ranges: bytes ...

```

The attentive reader may have wondered why a specific network policy is needed for `hello-world` if there is no default deny policy limiting the traffic in the `default` namespace. The reason is because it's a good practice to ensure the application will work in environments where the default deny policy is in place. You can try removing the `hello-world` network policy and see that the application will still work.

## Step 2: Create a default network policy

Network segmentation is an important measure for reducing risk in the cluster. It's strongly recommended to create a default network policy that denies all traffic by default in each namespace. This way, pods can only send or receive traffic that has been explicitly allowed.

Let's create a default deny-all policy for the `default` namespace by creating a `NetworkPolicy` that selects all pods as follows:

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

```text
$ kubectl apply -f default-deny.yaml
networkpolicy.networking.k8s.io/default-deny created
```

Now if you remove the `hello-world` network policy, the application won't work anymore.

```text
$ kubectl delete netpol hello-world
$ kubectl exec -it debug-toolbox -- sh
/ curl -Is hello-world.default
/ <TIMEOUT>
```

## Step 3: Allow DNS traffic

As previously mentioned, workload clusters are hardened by default and restrict communication with pods in Giant Swarm-managed namespaces, like `kube-system` and `giantswarm`. If an application needs access to a pod running on one of those namespaces, the access must be explicitly declared. The next example will enable traffic from the `debug-toolbox` pod to the cluster DNS service, which runs in a restricted namespace:

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

```text
$ kubectl exec debug-toolbox -- nslookup hello-world
Server: 172.31.0.10
Address: 172.31.0.10:53

Name: hello-world.default.svc.cluster.local
Address: 172.31.104.47
```

Removing the policy will make DNS requests to fail, as demonstrated below:

```text
$ kubectl delete netpol debug-toolbox-dns
$ kubectl exec debug-toolbox -- nslookup hello-world
;; connection timed out; no servers could be reached
```

## Step 4: Allowing specific pod to pod access

Going a step further, pod-to-pod access can be enabled for specific pods. The following example allows the `debug-toolbox` pod to access the `hello-world` pod on port `8080` only, rejecting all other traffic.

__Note__: This policy is written as an ingress rule targeting the `hello-world` pod but could have been equivalently written as an egress rule targeting the `debug-toolbox` pod. The NetworkPolicy implementation is stateful, meaning writing a separate rule allowing responses to permitted requests isn't necessary.

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

```text
$ kubectl apply -f allow-debug-toolbox-to-hello-world.yaml
$ kubectl exec -it debug-toolbox -- sh
/ curl -Is hello-world.default
/ HTTP/1.1 200 OK
/ [...]
```

### Step 5: Allowing pod to pod access within a namespace

One last interesting scenario to explore is allowing pod-to-pod access within a namespace. In some cases, like in a test environment, it may be necessary to enable all pods to communicate by default within the same namespace. The following example allows all pods in the `default` namespace to communicate with each other.

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

Note that the namespace to which this policy applies needs to carry a label `name:` similar to the actual name key in its metadata:

```sh
kubectl label namespace default name=default
```

Now let's delete all network policies and apply the `allow-default-namespace` policy so we can verify it works:

```text
$ kubectl delete netpol --all -n default
$ kubectl apply -f allow-default-namespace.yaml
$ kubectl exec -it debug-toolbox -- sh
/ curl -Is hello-world.default
/ HTTP/1.1 200 OK
```

This guide has introduced how network policies work and some peculiarities to be aware of when working in Giant Swarm clusters. However, the ideal configuration is to have a default deny policy in all namespaces, and allow only the necessary traffic to and from each application. This approach improves security, and ensures cluster traffic is intentionally and declaratively managed.

## Next step

Now that you've learned how to configure your application to communicate with other services, let's dive into how [observe your application]({{< relref "/getting-started/observe-your-clusters-and-apps" >}}).
