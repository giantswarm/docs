---
linkTitle: Cluster access control
title: Cluster access control with RBAC and Pod Security Standards
description: Introduction to using role-based access control (RBAC) and pod security standards (PSS) to secure your cluster and manage access control.
weight: 10
menu:
  principal:
    parent: tutorials-security
    identifier: tutorials-security-rbac
user_questions:
  - How can I add permissions to a service account?
  - How can I give my container permission to access a persistent volume?
  - How can I run a container as a certain user?
  - How can I run a container as privileged?
  - How can I specify which permissions are associated with a key pair?
  - Why are my containers failing to access some resources?
  - Why is my container lacking permission to use a persistent volume?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
last_review_date: 2024-11-28
mermaid: true
---

Two of the most central mechanisms to secure your cluster in `Kubernetes` are `Role Based Access Control` (RBAC) and `Pod Security Standards` (PSS). Together, they allow you to create fine-grained roles and policies to manage access control for users and software running on your cluster. Both are enabled by default on Giant Swarm clusters.

## Role based access control

The `RBAC` API defines both roles and bindings on either namespace or cluster level. Like any other `Kubernetes` API object, these can be defined by writing YAML (or JSON) manifests.

__Note__: that to apply these manifests, you need a user with higher level access than the access you want to set up. When in doubt, use a `cluster-admin` account to apply `RBAC` manifests.

### The role resources {#role-resources}

The `Role` and `ClusterRole` allow a cluster administrator to define a reusable set of permissions. While a `Role` is used to grant permissions within a single namespace, a `ClusterRole` can grant the same permissions, but can be bound on a cluster-scope.

If you want to grant access to a resource that isn't namespaced you have to use a `ClusterRole`.

As an example, the following `Role` grants read access to pods in the `default` namespace.

```yaml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: default
  name: pod-reader
rules:
  - apiGroups: [""] # "" indicates the core API group
    resources:
      - pods
    verbs:
      - get
      - watch
      - list
```

As you can see, the list of `resources` accessible only contains the value `pods`. The `verbs` entries define what the subject can do to pods. The three verbs listed in the example above allow for read-only access. Other verbs available for use are `create`, `update`, `patch`, and `delete`.

On to another example. With a `ClusterRole` like the following you can grant read access to secrets.

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  # "namespace" omitted since ClusterRoles aren't namespaced
  name: secret-reader
rules:
  - apiGroups: [""]
    resources:
      - secrets
    verbs:
      - get
      - watch
      - list
```

Since a `ClusterRole` isn't namespaced, you can use it either in a particular namespace or across all namespaces, depending on how it's bound. This will be explained in the next section.

#### Aggregated ClusterRoles

You can also create ClusterRoles by combining other cluster roles using an `aggregationRule`. The permissions of aggregated cluster roles are controller-managed, and filled in by joining the rules of any `ClusterRole` that matches the provided label selector.

You can use this to create meta cluster roles that you fill with `sub-cluster-roles` like following:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: monitoring
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      rbac.example.com/aggregate-to-monitoring: "true"
rules: [] # Rules are automatically filled in by the controller manager.
```

Now any `ClusterRole` you create that carries the `rbac.example.com/aggregate-to-monitoring: "true"` label will automatically get added to the `monitoring` cluster role, for example:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: monitoring-endpoints
  labels:
    rbac.example.com/aggregate-to-monitoring: "true"
rules:
- apiGroups: [""]
  Resources: ["services", "endpoints", "pods"]
  verbs: ["get", "list", "watch"]
```

You can further use this feature to extend already existing cluster roles, if you feel an existing role is too restrictive or want to include access to new custom resources. The default cluster roles (`admin`, `edit`, `view`) are already prepared to be extended through aggregation rules.

For example, you could extend the `admin` cluster role to include access to some custom `PodSecurityPolicy`:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: aggregate-admin
  labels:
    # Add these permissions to the "admin" default ClusterRole.
    rbac.authorization.k8s.io/aggregate-to-admin: "true"
rules:
- apiGroups:
  - policy
  resources:
  - podsecuritypolicies
  resourceNames:
  - admin-psp
  verbs:
  - use
```

After applying above `ClusterRole` to the cluster, everyone with the cluster role `admin` will be able to use the `admin-psp` policy.

### Binding a roles {#binding-role}

With bindings you can bind a `Role` or `ClusterRole` to subjects like users, groups, or service accounts. There are again two different resource types available:

- The `RoleBinding` grants access _within a certain namespace_ and can bind either a `Role` or a `ClusterRole` to subjects.
- The `ClusterRoleBinding` grants access _cluster-wide_ and can only bind a `ClusterRole` to subjects.

#### RoleBinding

A `RoleBinding` can either reference a `Role` or a `ClusterRole`, but will only grant permissions on the namespace it's applied to.

The following `RoleBinding` binds the `Role` named “pod-reader” to the user “jane” within the “default” namespace. This grants “jane” read access to pods in the “default” namespace.

```yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-pods
  namespace: default
subjects:
  - kind: User
    name: jane
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

In contrast, binding a `ClusterRole` (instead of a `Role`) with a `RoleBinding` allows cluster administrators to define a set of common roles for the entire cluster, then reuse them within _multiple namespaces_.

For instance, even though the following `RoleBinding` refers to a `ClusterRole`, user `dave` will only be able read secrets in the “development” namespace (the namespace of the `RoleBinding`).

```yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-secrets
  namespace: development # This only grants permissions within the "development" namespace.
subjects:
  - kind: User
    name: dave
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

#### ClusterRoleBinding

Finally, a `ClusterRoleBinding` may be used to grant permission at the cluster level and in all namespaces. The following `ClusterRoleBinding` allows any user in the group “manager” to read secrets in any namespace.

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-secrets-global
subjects:
  - kind: Group
    name: manager
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

#### Referring to subjects

Bindings can refer to subjects that are either single users, groups, or service accounts. The latter are needed to grant API access (and with `PSPs` also `Pod` privileges) to certain `Pods`, for example monitoring and logging agents.

For a detailed explanation of how to refer to subjects in bindings you can read the [official RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-subjects).

#### Default role bindings {#default-roles-bindings}

Your `Kubernetes` cluster comes by default with a set of roles and cluster roles as well as some default bindings. These are automatically reconciled and thus can't be changed or deleted.

You can use the `Role` and `ClusterRole` resources to create bindings for your users. Following example would grant all users in the group `mynamespace-admin` full permissions to resources in the `mynamespace` namespace.

See how it references a `ClusterRole` named `admin`, which comes with `Kubernetes` by default.

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: mynamespace-admin
  namespace: mynamespace
subjects:
  - kind: Group
    name: mynamespace-admin
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

##### A super-user role binding

One of the most important default role bindings is for the `cluster-admin` role, which depicts a super-user in the cluster. By default, it's bound to the `system:masters` group. Thus, if you need cluster admin access to your `Kubernetes` cluster, you need to [generate user credentials]({{< relref "/getting-started/access-to-platform-api" >}}) that includes the group.

For a complete overview of default roles and bindings you can read the [official RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings).

__Warning:__ Be careful assigning super-user as a default role. Giving `cluster-admin` role to every user means letting them perform any action in the cluster. As an analogy, it's like you giving root access to every user in a Linux system. Consequently think twice which role your users will have in the system. For `Kubernetes`, it translates in selecting a proper username and group name. Read [the authentication documentation]({{< relref "/overview/architecture/authentication/" >}}) to know more.

### Verifying if you Have Access

If you aren't sure if your (or another) user is allowed to do a certain action, you can verify that with the `kubectl auth can-i` command.

```nohighlight
$ kubectl auth can-i create deployments \
  --namespace production
yes
```

You can also impersonate users to check their access:

```nohighlight
$ kubectl auth can-i create deployments \
  --namespace production \
  --as jane
no
```

or impersonate a `ServiceAccount` to check if it's set up right:

```nohighlight
$ kubectl auth can-i use podsecuritypolicies/privileged \
  -n kube-system \
  --as=system:serviceaccount:kube-system:calico-node
yes
```

You can also verify access for a whole group:

```nohighlight
$ kubectl auth can-i get pods --as-group=system:masters
yes
```

## Pod Security Standards

The Kubernetes maintainers publish a set of policies called `Pod Security Standards` (PSS), which describe acceptable pod configurations for different levels of risk. The policies apply to several pod and container specification-level fields which have security implications for the workload, and are grouped into three increasingly restrictive levels.

For example, the `baseline` policy level limits the capabilities a pod can use to a limited subset (~14 possibilities). The `restricted` level takes this policy further and requires each pod to explicitly drop all capabilities in its Pod spec, and allows adding back only a single capability (`NET_BIND_SERVICE`). The least restrictive level, `privileged`, is a no-op policy which doesn't perform any validation or impose any rules. Refer to the [official Pod Security Standards docs](https://kubernetes.io/docs/concepts/security/pod-security-standards/) for more information.

The `Pod Security Standards` provide only a set of suggested policies intended to be enforced by other implementations of actual controls which validate pods against the `PSS` rules.

### Pod Security Admission

The `Kubernetes` API includes a built-in admission controller called `Pod Security Admission` (PSA), which a specific implementation of a technical control for the `Pod Security Standards`. It's an admission controller which is built into the API server, and can be configured using labels on cluster namespaces.

Due to perceived limitations in the initial implementation of `PSA`, Giant Swarm uses an external admission controller to enforce these policies instead of the `Kubernetes` built-in PSA.

To learn more about built-in `PSA`, please refer to the [upstream Kubernetes Pod Security Admission documentation](https://kubernetes.io/docs/concepts/security/pod-security-admission/). You can read [a blog post outlining our decision not to use PSA](https://www.giantswarm.io/blog/giant-swarms-farewell-to-psp).

### Pod Security Standards with Kyverno

Instead of the `Pod Security Admission` controller, Giant Swarm clusters use `Kyverno` along with a set of Kyverno cluster policies which map to the `Pod Security Standards`.

{{< mermaid >}}
flowchart TD
    A["Pod Security Standards (PSS)"] -->|Enforced by| B("Kyverno <br/> (outside API Server)")
    A --> |Enforced by| C("Pod Security Admission (PSA) <br/> (inside API Server)")
{{< /mermaid >}}

By default, Giant Swarm clusters enforce the `restricted` level `Pod Security Standards`. This level aligns with our "secure by default" principle, and is intended to ensure our clusters are hardened according to community best practices.

Cluster administrators have complete flexibility and control over their policy enforcement, and may choose to ease their security requirements or enforce additional policies to suit their risk tolerance and business needs.

[A detailed guide to working with `Kyverno` PSS policies and exceptions]({{< relref "/tutorials/security/policy-enforcement" >}}) is available as a standalone resource.

## User management

Though our recommendation is to integrate your `Identity Provider` with the platform API, you can also manage users using certificates and `RBAC` bindings.

### Using common name as username

Setting a `Common Name` prefix results in a username like the following:

```nohighlight
<cn-prefix>.user.api.<cluster-domain>
```

where `<cn-prefix>` is a username of your choice and `<cluster-domain>` is your cluster's domain, for example `w6wn8.k8s.example.eu-central-1.aws.gigantic.io`.

When binding roles to a user you need to use the full username mentioned above.

### Using organizations

Organizations you set when creating `key-pairs` get mapped to groups inside `Kubernetes`. You can then assign roles to a whole group of users. A user can be part of multiple groups and thus be assigned multiple roles, too.

There is only a single predefined user group inside Kubernetes. Members of the `system:masters` group will directly be assigned the default `cluster-admin` role inside your cluster, which is allowed to do anything. Our recommendation is to only use this kind of user, when bootstrapping security settings for the cluster.

### Default settings

The `<cn-prefix>` defaults to the email you sign in with at Giant Swarm. The default organization is empty. Thus, a user that's created without any additional `CN` prefix and/or Organizations won't have any rights on the cluster unless you bind a role to their specific username.

## Bootstrapping and managing access rights

For bootstrapping and managing access rights on your `Kubernetes` cluster you first need a user that already has all rights that you want to give out. The easiest way to get such a user is creating a user that's in the `system:masters` group and thus carries Cluster Admin rights.

To create such a user with `kubectl gs` for a cluster with id `w6wn8` just run following command:

```sh
export PLATFORM_API=https://api.capi.aws.k8s.gigantic.io # your platform API
kubectl gs login $PLATFORM_API \
  --workload-cluster w6wn8 \
  --organization acme \
  --certificate-group "system:masters" \
  --certificate-ttl 3h
```

This will create a `kubeconfig` with a `cluster-admin` user that's valid for a three hours (as you don't want to yield that power for too long).

With this user you can now start creating roles and bindings for your users and apps. Let's go through some examples.

Note that in these examples you are assuming you are creating users through platform API. If you have plugged in your `Identity Provider` you can skip the user creation step and directly bind roles to your users.

### Giving admin access to a specific namespace

There is a default admin role defined inside `Kubernetes`. You can bind that role to a user or group of users for a specific namespace with a role binding similar to following.

```yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: development-admin
  namespace: development
subjects:
  - kind: User
    name: jane.w6wn8.k8s.example.eu-central-1.aws.gigantic.io
    apiGroup: rbac.authorization.k8s.io
  - kind: Group
    name: dev-admin
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

The above YAML gives admin rights to the `development` namespace to both the user with `CN` prefix `jane` and all users within the `dev-admin` group.

You could create `kubeconfigs` for such users like following:

```sh
export PLATFORM_API=https://api.capi.aws.k8s.gigantic.io # your platform API
kubectl gs login $PLATFORM_API --workload-cluster w6wn8 --cn-prefix "jane"
```

or

```sh
export PLATFORM_API=https://api.capi.aws.k8s.gigantic.io # your platform API
kubectl gs login $PLATFORM_API --workload-cluster w6wn8 --cn-prefix "marc" --certificate-organizations "dev-admin"
```

Note that even when you don't need a specific username for giving Marc admin rights, you should still set a `CN` prefix to identify Marc's actions on the cluster.

### Giving read access to the whole cluster

There is a default view role defined inside Kubernetes. You can bind that role to a user or group of users for the whole cluster with a Cluster Role Binding similar to following.

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: cluster-viewer
subjects:
  - kind: User
    name: jane.w6wn8.k8s.example.eu-central-1.aws.gigantic.io
    apiGroup: rbac.authorization.k8s.io
  - kind: Group
    name: cluster-view
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: view
  apiGroup: rbac.authorization.k8s.io
```

Above YAML gives view rights to the whole cluster to both the user with `CN` prefix `jane` and all users within the `cluster-view` group.

Let's assume you have already created both users from the example above. As Jane's username hasn't changed, she automatically gets the new rights using her existing credentials.

However, Marc is only part of the `dev-admin` group, so if you want to give him view access to the cluster, you need to give him new credentials.

```sh
export PLATFORM_API=https://api.capi.aws.k8s.gigantic.io # your platform API
kubectl gs login $PLATFORM_API \
  --workload-cluster w6wn8 \
  --organization acme \
  --cn-prefix "marc" \
  --certificate-group "dev-admin, cluster-view"
```

With the above Marc would now be part of both groups and thus be bound by both bindings.

### Running applications with API access

Applications running inside your cluster that need access to the `Kubernetes` API need the right permissions bound to them. For this the Pods need to use a `ServiceAccount`.

The typical process looks like following example:

#### 1. Create a Service Account for your app {#app-api-create-sa}

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: fluentd
  namespace: logging
```

#### 2. Add the Service Account to your app {#app-api-add-sa}

This is done by adding a line referencing the `ServiceAccount` to the `Pod` spec of your `Deployment` or `Daemonset`. To be sure  you have the right place in the YAML you can put it right above the line `containers:` at the same indentation level. The section should look similar to following:

```yaml
[...]
spec:
  template:
        metadata:
          name: fluentd
          labels:
            component: fluentd
        spec:
          serviceAccountName: fluentd
          containers:
    [...]
```

#### 3. Create a Role for your app {#app-api-create-role}

This role should be very specific to the needs of your app and not allow anything more than what the app needs to work. In this example `fluentd` needs a cluster role that can get, watch, and list `Pods` and `Namespaces` in the whole cluster.

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: fluentd
rules:
- apiGroups: [""] # core API group
  resources: ["pods", "namespaces"]
  verbs: ["get", "watch", "list"]
```

#### 4. Bind the Role to the Service Account {#app-api-bind-role-sa}

Now, you bind the role created above to the `ServiceAccount`:

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: fluentd
subjects:
- kind: ServiceAccount
  name: fluentd
  namespace: logging
roleRef:
  kind: ClusterRole
  name: fluentd
  apiGroup: rbac.authorization.k8s.io
```

### Revoking access

You can revoke access from any user or group of users by either completely removing the bindings they're part of or, in case of bindings that bind to several subjects, removing them specifically from the list of subjects in that binding.

Note that bindings that come with the cluster by default like `system:masters` can't be removed as they're reconciled. Our team highly recommend to use OIDC integration to manage users and groups. Otherwise, you rely on short-lived users access (for example certificates with a TTL of a day or less) as optional security measure.

Learn more about [policies]({{< relref "/tutorials/security/policy-enforcement" >}}) and how to enforce security them through the platform.