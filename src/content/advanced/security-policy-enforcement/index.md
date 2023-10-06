---
linkTitle: Security policy enforcement
title: Security policy enforcement
description: This article describes the security policies enforced in a cluster and how to resolve failing resources.
weight: 60
menu:
  main:
    parent: advanced
user_questions:
 -  Why won't my workload deploy?
 -  How do I fix a Kyverno policy violation?
 -  How can I exclude a workload from a Kyverno policy?
 -  What security policies are enforced in my cluster?
 -  What are Pod Security Standards (PSS)?
 -  How do I migrate from PSPs to PSS?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
last_review_date: 2023-03-21
---

<!-- {{< platform_support_table aws="alpha=v17.2.0" aws="ga=v17.4.0">}} -->

__Note__: this content is applicable to Giant Swarm v19.2.0 and above, which include PSS `baseline` and `restricted` policies deployed in `enforce` mode.

__Note__: additional information for cluster admins can be found in a separate cluster admin guide.

## Compliance Scanning and Enforcement

To enforce security best practices, several policies mapped to the [Kubernetes Pod Security Standards][k8s-pss] are pre-installed in Giant Swarm clusters.

These policies validate Pod and Pod controller (i.e. Deployment, DaemonSet, StatefulSet) resources and deny admission of the resource if it does not comply.
Individual policies forbid deploying resources with various kinds of known risky configurations, and require some additional defensive options to be set in order to reduce the likelihood and/or impact of a workload becoming compromised.

Users who are unaware of those requirements may be surprised when their workloads fail to deploy, so this guide attempts to outline a basic workflow for resolving failing policies.

### Kyverno

Giant Swarm clusters currently use Kyverno to perform the actual enforcement of the policies we manage.
Our Policy API, along with other platform internals, manage the Kyverno ClusterPolicy resources as well as any necessary Kyverno PolicyExceptions.

Kyverno is an admission controller, which inspects incoming requests to the API server and checks them against configured policies.

Kyverno policies can be configured in two modes: `audit` and `enforce`.

In `audit` mode, Kyverno will not reject admission of a resource even if it fails the policy. It will instead create a report and add an Event to the resource indicating that the resource has failed the policy.

In `enforce` mode, Kyverno will block the creation of a resource if it fails a policy. No report or event will be created, because the resource will never exist in the cluster.

By default, Kyverno will periodically re-scan all existing resources in a cluster and generate reports about their compliance.

Resources which fail a policy will receive an Event similar to the example below, indicating which policy has failed.

These Events are useful for evaluating which resources are affected by a policy or potential policy change.

If a resource has these warning events for a given policy, it means that the resource would be rejected if that policy were to change to `enforce` mode.

Much more extensive documentation about Kyverno configuration and policy behavior is available [in the official docs][kyverno-docs].

### Sample Policy Warnings

```text
Events:
  Type     Reason           Age   From          Message
  ----     ------           ----  ----          -------
  Warning  PolicyViolation  18m   kyverno-scan  policy restrict-volume-types/restricted-volumes fail: Only the following types of volumes may be used: configMap, csi, downwardAPI, emptyDir, ephemeral, persistentVolumeClaim, projected, and secret.
  Warning  PolicyViolation  18m   kyverno-scan  policy disallow-host-path/host-path fail: validation error: HostPath volumes are forbidden. The field spec.volumes[*].hostPath must be unset. rule host-path failed at path /spec/volumes/2/hostPath/
```

This example shows that the Pod resource fails two policies: the `restrict-volume-types` and `disallow-host-path` policies. It also indicates the rule which failed from each policy, specifically the `restricted-volumes` rule and the `host-path` rule. With this information, the owner of the resource should change the Pod configuration to comply with the policies, or if it is not possible to comply, apply for a PolicyException.

## Sample Compliant Deployment

This Deployment is compliant with all Baseline and Restricted PSS policies:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app.kubernetes.io/instance: nginx
    app.kubernetes.io/name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/instance: nginx
      app.kubernetes.io/name: nginx
  template:
    metadata:
      labels:
        app.kubernetes.io/instance: nginx
        app.kubernetes.io/name: nginx
    spec:
      securityContext:
        runAsGroup: 1000
        runAsNonRoot: true
        runAsUser: 1000
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          privileged: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          seccompProfile:
            type: RuntimeDefault
```

## Common Pitfalls

- The PSS policies described here apply to Pods as well as their controller types, like Deployments, DaemonSets, and StatefulSets. However, cluster administrators can deploy additional policies which apply to any arbitrary Kubernetes resource type, like Services, ConfigMaps, etc. For that reason, this guide often uses the term "resource" instead of "Pod" when referring to the object being targeted by a Kyverno policy.
- Many policies target configuration set at the container level, so *all* containers in a Pod must satisfy each policy, including `init` and `ephemeral` containers.
- Some policies contain multiple rules. Resources must be compliant with *all* of the rules in order to pass validation by that policy.
- Many policies are satisfied if the fields they target are simply omitted or left unset. However, some `restricted` level policies require that the resource explicitly sets a particular value. It may be necessary to add new content to an existing resource in order to make it compliant.

## Default Policies

These policies are pre-installed and enforced by default. Expand each policy for more information.

### PSS Baseline

{{%details "Disallow Capabilities (disallow-capabilities)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-capabilities/disallow-capabilities/

This policy specifies a list of permitted capabilities and rejects Pods which add any capabilities not in the list.

__Note__: The Restricted PSS policy `disallow-capabilities-strict` imposes additional restrictions and requires explicitly dropping ALL other capabilities.

#### Examples

This Pod satisfies the policy, because it does not add any capabilities to the container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

This Pod also satisfies the policy, because adding the `CHOWN` policy is allowed:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
    securityContext:
      capabilities:
        add: ["CHOWN"]
```

This Pod does NOT satisfy the policy, because it adds the `NET_ADMIN` capability, which is not permitted by the policy:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
    securityContext:
      capabilities:
        add: ["NET_ADMIN"]
```

{{% /details %}}

{{%details "Disallow Host Namespaces (disallow-host-namespaces)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-host-namespaces/disallow-host-namespaces/

This policy rejects Pods using host networking, host IPC, or host PID.
If any of those fields are present in the Pod spec, they must be set to `false`.

 <!-- markdownlint-disable no-duplicate-heading -->

#### Examples

This Pod satisfies the policy, because the Pod spec `hostNetwork` field is set to `false` and the `hostIPC` and `hostPID` fields are not set:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  hostNetwork: false
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

This Pod does NOT satisfy the policy, because it enables host networking, which is not permitted by the policy:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  hostNetwork: true
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

{{% /details %}}

{{%details "Disallow hostPath (disallow-host-path)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-host-path/disallow-host-path/

This policy rejects Pods which use a `HostPath` type volume.

__Note__: The Restricted PSS policy `restrict-volume-types` imposes additional restrictions on volume types.

#### Examples

This Pod satisfies the policy, because it does not use any volumes:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

This Pod also satisfies the policy, because other volume types, like `configMap`, are allowed:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
    volumeMounts:
    - mountPath: /etc/config
      name: config
  volumes:
  - name: config
    configMap:
      name: my-configmap
```

This Pod does NOT satisfy the policy, because it uses a `hostPath` type volume, which is not permitted by the policy:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
    volumeMounts:
    - mountPath: /host-k8s
      name: host-k8s
  volumes:
  - name: host-k8s
    hostPath:
      path: /etc/kubernetes
      type: ""
```

{{% /details %}}

{{%details "Disallow hostPorts (disallow-host-ports)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-host-ports/disallow-host-ports/

This policy rejects Pods which use host network ports.

#### Examples

This Pod satisfies the policy, because it does not specify any host or container ports to be exposed:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it only publishes an informational `containerPort`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

Note that the `containerPort` field is mostly informational and in both of the above examples, the application is still able to communicate on container ports not listed in the `container.ports` list.

This Pod does NOT satisfy the policy, because it uses a `hostPort`, which is not permitted by the policy:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - hostPort: 80
```

{{% /details %}}

{{%details "Disallow hostProcess (disallow-host-process)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-host-process/disallow-host-process/

This policy rejects Windows pods which enable the `hostProcess` feature.

{{% /details %}}

{{%details "Disallow Privileged Containers (disallow-privileged-containers)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-privileged-containers/disallow-privileged-containers/

This policy rejects Pods which attempt to use `privileged` mode.

#### Examples

This Pod satisfies the policy, because it does not set the `privileged` field:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it explicitly sets `privileged` to `false` in its only container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      privileged: false
```

This Pod does NOT satisfy the policy, because it enables `privileged` mode, which is not permitted by the policy:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      privileged: true
```

{{% /details %}}

{{%details "Disallow procMount (disallow-proc-mount)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-proc-mount/disallow-proc-mount/

This policy rejects Pods which set non-default `procMount` values.

#### Examples

This Pod satisfies the policy, because it does not set the `procMount` field:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it explicitly sets `procMount` to `Default` in its only container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      procMount: Default
```

This Pod does NOT satisfy the policy, because it sets `procMount` to `Unmasked`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      procMount: Unmasked
```

{{% /details %}}

{{%details "Disallow SELinux (disallow-selinux)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/disallow-selinux/disallow-selinux/

This policy rejects Pods which set SELinux values which are not known to be safe.

There are two rules associated with this policy: one which limits the SELinux type and one limiting the SELinux user and role.

#### Examples

This Pod satisfies the policy, because it does not set any `seLinuxOptions`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it sets an approved SELinux type in its only container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      seLinuxOptions:
        type: container_t
```

This Pod does NOT satisfy the policy, because it attempts to set an SELinux user:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      seLinuxOptions:
        user: root
```

{{% /details %}}

{{%details "Restrict AppArmor (restrict-apparmor-profiles)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/restrict-apparmor-profiles/restrict-apparmor-profiles/

This policy rejects Pods which set an AppArmor profile other than `runtime/default` or `localhost/*`.

#### Examples

This Pod satisfies the policy, because it does not set an AppArmor annotation:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it sets an approved AppArmor profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  container.apparmor.security.beta.kubernetes.io/nginx: runtime/default
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod does NOT satisfy the policy, because it attempts to use the `unconfined` profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  container.apparmor.security.beta.kubernetes.io/nginx: unconfined
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

{{% /details %}}

{{%details "Restrict Seccomp (restrict-seccomp)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/restrict-seccomp/restrict-seccomp/

This policy rejects Pods which set a seccomp profile other than `RuntimeDefault` or `Localhost`.

__Note__: The Restricted PSS policy `restrict-seccomp-strict` requires containers to explicitly set one of the approved profiles.**

#### Examples

This Pod satisfies the policy, because it does not set a seccomp profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it sets an approved seccomp profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      seccompProfile:
        type: RuntimeDefault
```

This Pod does NOT satisfy the policy, because it attempts to use the `Unconfined` profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      seccompProfile:
        type: Unconfined
```

{{% /details %}}

{{%details "Restrict sysctls (restrict-sysctls)" %}}
Policy source: https://kyverno.io/policies/pod-security/baseline/restrict-sysctls/restrict-sysctls/

This policy rejects Pods which set [sysctls][k8s-sysctl] aside from an approved list.

#### Examples

This Pod satisfies the policy, because it does not add any sysctls:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because it adds only an approved sysctl:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      sysctls:
        - name: net.ipv4.ip_local_port_range
          value: "32768 60999"
```

This Pod does NOT satisfy the policy, because it attempts to add a non-approved sysctl:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      sysctls:
        - name: kernel.stack_erasing
          value: "0"
```

{{% /details %}}

### PSS Restricted

{{%details "Disallow Capabilities (Strict) (disallow-capabilities-strict)" %}}
Policy source: https://kyverno.io/policies/pod-security/restricted/disallow-capabilities-strict/disallow-capabilities-strict/

This policy only allows adding the `NET_BIND_SERVICE` capability and requires all containers to explicitly drop all others.

#### Examples

This Pod satisfies the policy, because its only container explicitly drops `ALL` capabilities:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      capabilities:
        drop:
        - ALL
```

This Pod does NOT satisfy the policy, because it does not explicitly drop `ALL` capabilities:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

{{% /details %}}
{{%details "Disallow Privilege Escalation (disallow-privilege-escalation)" %}}
Policy source: https://kyverno.io/policies/pod-security/restricted/disallow-privilege-escalation/disallow-privilege-escalation/

This policy rejects Pods if any of the containers do not explicitly disallow privilege escalation.

#### Examples

This Pod satisfies the policy, because its only container explicitly forbids privilege escalation:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      allowPrivilegeEscalation: false
```

This Pod does NOT satisfy the policy, because its only container allows privilege escalation:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      allowPrivilegeEscalation: true
```

This Pod also does NOT satisfy the policy, because it does not explicitly disallow privilege escalation:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

{{% /details %}}
{{%details "Require Run As Non-Root User (require-run-as-non-root-user)" %}}
Policy source: https://kyverno.io/policies/pod-security/restricted/require-run-as-non-root-user/require-run-as-non-root-user/

This policy rejects Pods if any of the containers or the Pod itself sets a user id of 0.

#### Examples

This Pod satisfies the policy, because the Pod sets a user id of 10000:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  securityContext:
    runAsUser: 10000
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because the only container sets a user id of 10000:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      runAsUser: 10000
```

This Pod does NOT satisfy the policy, because its container runs as root (user id 0):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      runAsUser: 0
```

This Pod also does NOT satisfy the policy, because even though the Pod specifies a users of 10000, the container still sets an user id of 0:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  securityContext:
    runAsUser: 10000
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      runAsUser: 0
```

{{% /details %}}
{{%details "Require runAsNonRoot (require-run-as-nonroot)" %}}
Policy source: https://kyverno.io/policies/pod-security/restricted/require-run-as-nonroot/require-run-as-nonroot/

This policy requires that either the Pod or all of its containers set the `runAsNonRoot` value to `true`.

#### Examples

This Pod satisfies the policy, because the Pod sets the `runAsNonRoot` value:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  securityContext:
    runAsNonRoot: true
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because the only container sets the `runAsNonRoot` value:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      runAsNonRoot: true
```

This Pod does NOT satisfy the policy, because its container sets the `runAsNonRoot` value to `false`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      runAsNonRoot: false
```

This Pod also does NOT satisfy the policy, because even though the only container sets the `runAsNonRoot` value to `true`, the Pod itself sets it to `false`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  securityContext:
    runAsNonRoot: false
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      runAsNonRoot: true
```

{{% /details %}}
{{%details "Restrict Seccomp (Strict) (restrict-seccomp-strict)" %}}
Policy source: https://kyverno.io/policies/pod-security/restricted/restrict-seccomp-strict/restrict-seccomp-strict/

This policy requires either the Pod or all containers to explicitly set a seccomp profile of either `RuntimeDefault` or `Localhost`.

__Note__: The Baseline PSS policy `restrict-seccomp` requires Pods/containers to use one of these profiles *if they set one*. This policy requires the value to be set.

#### Examples

This Pod satisfies the policy, because its container sets an approved seccomp profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      seccompProfile:
        type: RuntimeDefault
```

This Pod satisfies the policy, because the Pod sets an approved seccomp profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod does NOT satisfy the policy, because it does not set a seccomp profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod does NOT satisfy the policy, because it attempts to use the `Unconfined` profile:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    securityContext:
      seccompProfile:
        type: Unconfined
```

{{% /details %}}
{{%details "Restrict Volume Types (restrict-volume-types)" %}}
Policy source: https://kyverno.io/policies/pod-security/restricted/restrict-volume-types/restrict-volume-types/

This policy restricts the types of volumes a Pod may use to a list of pre-approved types.

__Note__: The Baseline PSS policy `disallow-host-path` forbids only HostPath volumes. This policy further restricts the types of approved volumes.

#### Examples

This Pod satisfies the policy, because it does not use any volumes:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
```

This Pod also satisfies the policy, because the `configMap` volume type is permitted:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    volumeMounts:
    - mountPath: /etc/config
      name: config
  volumes:
  - name: config
    configMap:
      name: my-configmap
```

This Pod does NOT satisfy the policy, because it uses a `gitRepo` type volume, which is not permitted by the policy:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    volumeMounts:
    - mountPath: /repo
      name: my-git-repo
  volumes:
  - name: my-git-repo
    gitRepo:
      repository: "git@danger.git"
      revision: "abc123"
```

{{% /details %}}

## Policy Exceptions

If a workload requires an exception, for example because it has a legitimate reason to run with a less secure configuration, the workload can be excluded from enforcement of a particular policy.

__Note__: under most circumstances, only a cluster administrator will be able to grant an exception. Your organization may have a predefined process or offer an automated self-service portal to request one.

To exclude a workload from a policy, create a `PolicyException` resource for that workload-policy combination.

There are different ways to structure a `PolicyException`, and your cluster administrator may have a preferred format.

Giant Swarm currently uses a "PolicyException per Workload" approach, which looks like this:

```yaml
apiVersion: kyverno.io/v2alpha1
kind: PolicyException
metadata:
  name: my-workload-exceptions
  namespace: my-namespace
spec:
  exceptions:
  - policyName: disallow-host-path
    ruleNames:
    - host-path
    - autogen-host-path
  - policyName: restrict-volume-types
    ruleNames:
    - restricted-volumes
    - autogen-restricted-volumes
  match:
    any:
    - resources:
        kinds:
        - Deployment
        - ReplicaSet
        - Pod
        namespaces:
        - my-namespace
        names:
        - my-workload*
```

This example allows a Deployment (and the ReplicaSet and Pods it creates) named `my-workload` in the namespace `my-namespace` to be admitted even though it violates the `disallow-host-path` and `restrict-volume-types` policies.

Noteworthy pieces of this example:

- Kyverno policy rules are usually written at the Pod level. For convenience, Kyverno automatically generates equivalent rules for Pod controllers like Deployments and DaemonSets. Such rules are prefaced with the value `autogen-` and added to the policy automatically (two such rules are visible in the example). When writing a `PolicyException`, any applicable `autogen` rules must also be listed if a workload should be exempt from them.
- Similarly, when listing resource kinds to be matched in a `PolicyException`, every subresource controller must be listed as well. For example: If a Policy is written at the CronJob level (and autogen policies are enabled for it), then the Job and Pod resources created from the CronJob also need to be explicitly matched in the `PolicyException`. The same happens with Deployments, where the ReplicaSet and Pod controllers will need to be excluded as well.
- A policy can contain multiple rules -- exceptions can be applied to individual rules so that the others remain in effect. Here, the workload is allowed to fail the `host-path` and `restricted-volumes` rules (and their automatically generated equivalents). A workload is only exempt from the rules listed in a `ruleNames` list. If a policy contains other rules not listed in the `PolicyException`, and the workload does not satisfy those rules, the workload will be rejected.
- Cluster administrators can choose the namespace(s) where `PolicyExceptions` are stored. The correct namespace for a `PolicyException` might be different than the namespace for the Pod itself.

[k8s-pss]: https://kubernetes.io/docs/concepts/security/pod-security-standards/
[k8s-sysctl]: https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/
[kyverno-docs]: https://kyverno.io/docs/
