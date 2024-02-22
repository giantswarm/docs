---
title: Security
description: Introduction to using role-based access control (RBAC) and pod security standards (PSS) to secure your cluster and manage access control.
weight: 110
menu:
  main:
    parent: getting-started
user_questions:
  - How can I add permissions to a service account?
  - How can I give my container permission to access a persistent volume?
  - How can I run a container as a certain user?
  - How can I run a container as privileged?
  - How can I specify which permissions are associated with a key pair?
  - Why are my containers failing to access some resources?
  - Why is my container lacking permission to use a persistent volume?
aliases:
  - /getting-started/security
  - /guides/securing-with-rbac-and-psp/
  - /getting-started/rbac-and-psp/
  - /getting-started/securing-your-cluster
owner:
  - https://github.com/orgs/giantswarm/teams/sig-security
last_review_date: 2023-11-27
mermaid: true
---

Two of the most central mechanisms to secure your cluster in Kubernetes are Role Based Access Control (RBAC) and Pod Security Standards (PSS). Together, they allow you to create fine-grained roles and policies to manage access control for users and software running on your cluster. Both are enabled by default on Giant Swarm clusters.

## Role based access control

The RBAC API defines both roles and bindings on either namespace or cluster level. Like any other Kubernetes API object, these can be defined by writing YAML (or JSON) manifests.

__Note__ that to apply these manifests, you need a user with higher level access than the access you want to set up. When in doubt, use a Cluster Admin account to apply RBAC manifests.

### The Role and ClusterRole resource {#role-resources}

The `Role` and `ClusterRole` allow a cluster administrator to define a reusable set of permissions. While a `Role` is used to grant permissions within a single namespace, a `ClusterRole` can grant the same permissions, but can be bound on a cluster-scope.

If you want to grant access to a resource that is not namespaced you have to use a `ClusterRole`.

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
  # "namespace" omitted since ClusterRoles are not namespaced
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

Since a `ClusterRole` is not namespaced, you can use it either in a particular namespace or across all namespaces, depending on how it is bound. This will be explained in the next section.

#### Aggregated ClusterRoles

You can also create ClusterRoles by combining other ClusterRoles using an `aggregationRule`. The permissions of aggregated ClusterRoles are controller-managed, and filled in by unioning the rules of any `ClusterRole` that matches the provided label selector.

You can use this to create meta-ClusterRoles that you fill with sub-ClusterRoles like following:

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

Now any ClusterRole you create that carries the `rbac.example.com/aggregate-to-monitoring: "true"` label will automatically get added to the `monitoring` ClusterRole, e.g.:

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

You can further use this feature to extend already existing ClusterRoles, if you feel an existing role is too restrictive or want to include access to new custom resources. The default ClusterRoles (`admin`, `edit`, `view`) are already prepared to be extended through aggregation rules.

For example we could extend the `admin` ClusterRole to include access to some custom PodSecurityPolicy we created:

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

After applying above `ClusterRole` to the cluster, everyone with the ClusterRole `admin` will be able to use the `admin-psp` PodSecurityPolicy.

### Binding a Role and ClusterRole {#binding-role}

With bindings you can bind a `Role` or `ClusterRole` to subjects like users, groups, or service accounts. There are again two different resource types available:

- The `RoleBinding` grants access _within a certain namespace_ and can bind either a `Role` or a `ClusterRole` to subjects.
- The `ClusterRoleBinding` grants access _cluster-wide_ and can only bind a `ClusterRole` to subjects.

#### RoleBinding

A `RoleBinding` can either reference a `Role` or a `ClusterRole`, but will only grant permissions on the namespace it is applied to.

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

For instance, even though the following `RoleBinding` refers to a `ClusterRole`, user “dave” will only be able read secrets in the “development” namespace (the namespace of the `RoleBinding`).

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

Bindings can refer to subjects that are either single users, groups, or service accounts. The latter are needed to grant API access (and with PSPs also Pod privileges) to certain Pods, e.g. for monitoring and logging agents.

For a detailed explanation of how to refer to subjects in Bindings we defer to the [official RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-subjects).

#### Default Roles and Role Bindings {#default-roles-bindings}

Your Kubernetes cluster comes by default with a set of Roles and Cluster Roles as well as some default Bindings. These are automatically reconciled and thus cannot be changed or deleted.

You can use the `Role` and `ClusterRole` resources to create bindings for your users. Following example would grant all users in the group `mynamespace-admin` full permissions to resources in the `mynamespace` namespace. See how it references a `ClusterRole` named "admin", which comes with Kubernetes by default.

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

One of the most important default Role Bindings is for the "cluster-admin" role, which depicts a super-user in the cluster. By default it is bound to the `system:masters` group. Thus, if you need cluster admin access to your Kubernetes cluster, you need to create user credentials (e.g. by [creating a key pair with gsctl]({{< relref "/vintage/use-the-api/gsctl/create-keypair" >}}) or the Giant Swarm Web UI) that include that group.

For a complete overview of default roles and bindings we defer to the [official RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings).

__Warning:__ Be careful assigning super-user as a default role. Giving `cluster-admin` role to every user means letting them perform any action in the cluster. As an analogy, it is like you giving root access to every user in a Linux system. Consequently think twice which role your users will have in the system. For Kubernetes, it translates in selecting a username and group name properly. In case you use authentication based on certs, [common name and organization would be those respectively]({{< relref "/vintage/use-the-api/gsctl/create-keypair#rbac-cn-org" >}}). If you are using an external authentication system then be sure it returns the correct user and group name to the Kubernetes API.

### Verifying if you Have Access

If you are not sure if your (or another) user is allowed to do a certain action, you can verify that with the `kubectl auth can-i` command.

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

or impersonate a Service Account to check if it is set up right:

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

## Pod Security Standards (PSS)

__Note__: Prior to Kubernetes v1.25, pod-level security configuration was controlled by Pod Security Policies (PSP). PSPs were a Kubernetes API resource which allowed cluster administrators to restrict the values a pod could use for certain security-relevant configuration. Due to limitations of the specification, the PSP type was deprecated in v1.21 and removed in v1.25.

The Kubernetes maintainers publish a set of policies called Pod Security Standards, which describe acceptable pod configurations for different levels of risk. The policies apply to several pod and container specification-level fields which have security implications for the workload, and are grouped into three increasingly restrictive levels.

For example, the `baseline` policy level limits the capabilities a pod can use to a limited subset (~14 possibilities). The `restricted` level takes this policy further and requires each pod to explicitly drop all capabilities in its Pod spec, and allows adding back only a single capability (`NET_BIND_SERVICE`). The least restrictive level, `privileged`, is a no-op policy which does not perform any validation or impose any rules. Refer to the [official Pod Security Standards docs][upstream-pss] for more information.

The Pod Security Standards provide only a set of suggested policies intended to be enforced by other implementations of actual controls which validate pods against the PSS rules.

### Pod Security Admission (PSA)

The Kubernetes API includes a built-in admission controller called Pod Security Admission, which a specific implementation of a technical control for the Pod Security Standards. It is an admission controller which is built into the API server, and can be configured using labels on cluster namespaces.

Due to perceived limitations in the initial implementation of PSA and to keep feature parity with PSPs for our customers, Giant Swarm uses an external admission controller to enforce these policies instead of PSA.

To learn more about builtin PSA, please refer to the [upstream Kubernetes Pod Security Admission documentation][upstream-psa]. We've also written [a blog post outlining our decision not to use PSA][farewell-psp-blog].

### Pod Security Standards with Kyverno

Instead of the Pod Security Admission controller, Giant Swarm clusters use Kyverno along with a set of Kyverno ClusterPolicies which map to the Kubernetes Pod Security Standards.

{{< mermaid >}}
flowchart TD
    A["Pod Security Standards (PSS)"] -->|Enforced by| B("Kyverno <br/> (outside API Server)")
    A --> |Enforced by| C("Pod Security Admission (PSA) <br/> (inside API Server)")
{{< /mermaid >}}

By default, Giant Swarm clusters enforce the `restricted` level Pod Security Standards. This level aligns with our "secure by default" principle, and is intended to ensure our clusters are hardened according to community best practices.

Cluster administrators have complete flexibility and control over their policy enforcement, and may choose to ease their security requirements or enforce additional policies to suit their risk tolerance and business needs.

[A detailed guide to working with Kyverno PSS Policies and PolicyExceptions][policy-enforcement-guide] is available as a standalone resource.

## User management with Giant Swarm

If you are managing users through the Giant Swarm REST API or its clients, `gsctl` or the Web UI, you can specify a Common Name Prefix and Organizations when you create key-pairs of kubeconfigs.

### Using common name as username in Kubernetes

Setting a Common Name Prefix results in a username like the following:

```nohighlight
<cn-prefix>.user.api.<cluster-domain>
```

where `<cn-prefix>` is a username of your choice and `<cluster-domain>` is your cluster's domain, e.g. `w6wn8.k8s.example.eu-central-1.aws.gigantic.io`.

When binding roles to a user you need to use the full username mentioned above.

### Using organizations as groups in Kubernetes

Organizations you set when creating key-pairs or kubeconfigs get mapped to groups inside Kubernetes.

You can then assign roles to a whole group of users.

A user can be part of multiple groups and thus be assigned multiple roles, too.

There is only a single predefined user group inside Kubernetes. Members of the `system:masters` group will directly be assigned the default `cluster-admin` role inside your cluster, which is allowed to do anything. We recommend only using this kind of user, when bootstrapping security settings for the cluster.

### Default settings

The `<cn-prefix>` defaults to the email you sign in with at Giant Swarm. The default organization is empty. Thus, a user that is created without any additional CN Prefix and/or Organizations won't have any rights on the cluster unless you bind a role to their specific username.

## Bootstrapping and managing access rights

For bootstrapping and managing access rights on your Kubernetes cluster you first need a user that already has all rights that you want to give out. The easiest way to get such a user is creating a user that is in the `system:masters` group and thus carries Cluster Admin rights.

To create such a user with `gsctl` for a cluster with id `w6wn8` just run following command:

```nohighlight
gsctl create kubeconfig \
  -c w6wn8 \
  -d "Access Management" \
  --ttl 1d \
  --certificate-organizations "system:masters"
```

This will create a kubeconfig with a Cluster Admin user that is valid for a day (as we don't want to yield that power for too long).

With this user we can now start creating Roles and Bindings for our users and apps. For this we will look at some examples.

Note that in these examples we are assuming you are creating users through Giant Swarm's API.

### Giving admin access to a specific namespace

There is a default admin role defined inside Kubernetes. You can bind that role to a user or group of users for a specific namespace with a Role Binding similar to following.

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

The above YAML gives admin rights to the `development` namespace to both the user with CN Prefix `jane` and all users within the `dev-admin` group.

You could create kubeconfigs for such users like following.

```nohighlight
gsctl create kubeconfig -c w6wn8 -d "Jane" --cn-prefix "jane"
```

or

```nohighlight
gsctl create kubeconfig -c w6wn8 -d "Marc" --cn-prefix "marc" --certificate-organizations "dev-admin"
```

Note that even when we don't need a specific username for giving Marc Admin rights, we should still set a CN Prefix so we can identify Marc's actions on the cluster.

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

Above YAML gives view rights to the whole cluster to both the user with CN Prefix `jane` and all users within the `cluster-view` group.

Let's assume we already created both users from the example above. As Jane's username has not changed, she automatically gets the new rights using her existing credentials.

However, Marc is only part of the `dev-admin` group, so if we want to give him view access to the cluster we need to give him new credentials.

```nohighlight
gsctl create kubeconfig \
  -c w6wn8 \
  -d "Marc" \
  --cn-prefix "marc" \
  --certificate-organizations "dev-admin, cluster-view"
```

With the above Marc would now be part of both groups and thus be bound by both bindings.

### Running applications that need API access

Applications running inside your cluster that need access to the Kubernetes API need the right permissions bound to them. For this the Pods need to use a Service Account.

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

This is done by adding a line referncing the Service Account to the Pod spec of your Deployment or Daemonset. To be sure  you have the right place in the YAML you can put it right above the line `containers:` at the same intendation level. The section should look similar to following:

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

This role should be very specific to the needs of your app and not allow anything more than what the app needs to work. In this example fluentd needs a Cluster Role that can get, watch, and list Pods and Namespaces in the whole cluster.

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

Now we bind the role we created above to the Service Account we're using.

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

You can revoke access from any user or group of users by either completely removing the binding(s) they are part of or, in case of bindings that bind to several subjects, removing them specifically from the list of subjects in that binding.

Note that bindings that come with the cluster by default like `system:masters` cannot be removed as they are reconciled. We highly recommend you only create short-lived users (i.e. certificates with a TTL of a day or less) for this kind of access.

## Further reading

- [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/)
- [Pod Security Admission][upstream-psa]
- [Pod Security Standards][upstream-pss]
- [Giant Swarm's farewell to PSP blog][farewell-psp-blog]
- [Configuring Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
- [Creating a kubeconfig with gsctl]({{< relref "/vintage/use-the-api/gsctl/create-kubeconfig" >}})
- [Creating a key pair with gsctl]({{< relref "/vintage/use-the-api/gsctl/create-keypair" >}})

[farewell-psp-blog]: https://www.giantswarm.io/blog/giant-swarms-farewell-to-psp
[upstream-psa]: https://kubernetes.io/docs/concepts/security/pod-security-admission/
[upstream-pss]: https://kubernetes.io/docs/concepts/security/pod-security-standards/
[policy-enforcement-guide]: {{< relref "/vintage/advanced/security/security-policy-enforcement" >}}
