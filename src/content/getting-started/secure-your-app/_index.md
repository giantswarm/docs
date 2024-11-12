---
description: Learn how security is applied to your application on the Giant Swarm platform.
title: Secure your app
weight: 70
last_review_date: 2024-11-12
menu:
  principal:
    parent: getting-started
    identifier: getting-started-security
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I observe the platform metrics and logs for my application?
  - What do I need to do to observe the platform metrics and logs for my application?
---

Giant Swarm platform is secured by default. The workload clusters are configured with security best practices in mind. The core functionality is built based on a policy enforcement engine. The `Kubernetes` project comes with [`Pod Security Standards (PSS)`](https://kubernetes.io/docs/concepts/security/pod-security-standards/) to ensure that the pods are running with the least privilege. The main problem of this technology is settings are cluster-wide and it's hard to create exceptions for specific workloads.

For that reason, the platform comes with an extended policy engine, `Kyverno`. A part of enforce the common pod security standards, your clusters have additional policies which can be customized to your needs. Your developers can create exceptions for their workloads without compromising the security of the cluster.

In this guide, you will learn how to make your application compliant with the secure baseline and how create policy exceptions when needed.

## Requirements

Before start, you need a running workload cluster. If you don't have one, please first [create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).

As a next step, you need to deploy an application, here the `hello-world` application, to the workload cluster. For explanation on how to deploy the application please read the [previous step]({{< relref "/getting-started/install-an-application" >}}).

## Step 1: Understand the security baseline

By default the clusters come with a `restricted` set of policies. You can read more about which policies are part of the `restricted` set in the [upstream documentation](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted). The `restricted` set of policies are applied to all the namespaces in the cluster.

As brief summary, the `restricted` set of policies includes:

- Containers can only run with `non-root` users
- Not allowing privileged containers
- Not allowing host namespaces
- Allowing only a set of capabilities (indeed, only `NET_BIND_SERVICE` is allowed)
- `HostPath` volumes aren't allowed
- Only default `Seccomp` and `AppArmor` profiles are allowed
- `ReadOnlyRootFilesystem` is enforced

In case you application needs to use any of the features that aren't allowed by the `restricted` policies, you need to create a policy exception.

## Step 2:  Configure the security context

In the `hello-world` application, the `restricted` policies aren't violated. The application is running with a `non-root` user and it's not using any special capability of the system.

In `Kubernetes`, the security context is defined in the `Pod` resource. Even if you don't need a special security configuration, you still need to add a minimal security context to your `Pod` resource. Inside the `Pod` manifest, you will find a general `securityContext` which is applied to all the containers within the resource. Additionally, you can define a `securityContext` for each container.

Inspecting the `hello-world` application, you can see pods are created without general `securityContext` but with a `securityContext` for the container.

```yaml
spec:
  containers:
  - name: hello-world
    ...
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      runAsNonRoot: true
      runAsUser: 1000
      seccompProfile:
        type: RuntimeDefault
```

Those are necessary to be compliant and pass the validation of the policy engine.

## Step 3:  Create a policy exception

Let’s assume the `hello-world` application needs to run as a `root` user because the container image is designed this way. You don't have more time and your CTO is pushing you to deploy the application.

First, you need to modify the deployment to configure the `securityContext` to allow the container to run as a `root` user.

```yaml
spec:
  containers:
  - name: hello-world
    ...
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      runAsNonRoot: false
      runAsUser: 0
      seccompProfile:
```

When you try to deploy the application, the policy engine will block the deployment with a message like:

```text
require-run-as-non-root-user:
  autogen-run-as-non-root-user: 'validation error: Running as root is not allowed.
    The fields spec.securityContext.runAsUser, spec.containers[*].securityContext.runAsUser,
    spec.initContainers[*].securityContext.runAsUser, and spec.ephemeralContainers[*].securityContext.runAsUser
    must be unset or set to a number greater than zero. rule autogen-run-as-non-root-user
    failed at path /spec/template/spec/containers/0/securityContext/runAsUser/'
```

It works as expected. Now, it's time to create a policy exception. Depending on your platform team the policy has to be approved before it's applied to the cluster. In this guide, we will assume the policy is approved.

In the platform, there is an extended API, `PolicyException`, to abstract the policy definition from the policy engine. If the underlying policy engine is changed, the `PolicyException` resource will be still valid. In our scenario, the resource looks like:

```yaml
apiVersion: policy.giantswarm.io/v1alpha1
kind: PolicyException
metadata:
  name: hello-world-allow-root
  namespace: policy-exceptions
spec:
  policies:
  - require-run-as-non-root-user
  - require-run-as-nonroot
  targets:
  - kind: Deployment
    names:
    - hello-world*
    namespaces:
    - default
```

This policy is translated to the policy engine as:

```yaml
apiVersion: kyverno.io/v2beta1
kind: PolicyException
metadata:
  name: hello-world-allow-root
  namespace: policy-exceptions
spec:
  exceptions:
  - policyName: require-run-as-non-root-user
    ruleNames:
    - run-as-non-root-user
    - autogen-run-as-non-root-user
    - autogen-cronjob-run-as-non-root-user
  ...
  match:
    any:
    - resources:
        kinds:
        - Deployment
        - Pod
        names:
        - hello-world*
        namespaces:
        - default
```

Note that the exception is created in the `policy-exceptions` namespace. The main reason behind this is to separate the policy exceptions from the workload resources, and the same time those can exists and be approved by security team before they're applied to the cluster.

Now you can apply again the deployment and the policy engine won't block the deployment.

## Next step

Learn more about security reading our [security tutorials]({{< relref "/tutorials/security" >}}).
