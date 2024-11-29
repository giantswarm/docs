---
linkTitle: Authorization
title: Authorization in the platform API
description: Granting users specific permission to certain resources is what authorization is all about. The Platform API uses Kubernetes' role based access control (RBAC) primitives and provides automation on top of it to make authorization easy for most real-life use cases. Here we explain them in detail.
weight: 30
menu:
  principal:
    identifier: tutorials-access-management-authorization
    parent: tutorials-access-management
last_review_date: 2024-10-28
user_questions:
  - What automation is working in a management cluster to ensure RBAC permissions?
  - How can I set up access to resources in the management cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

Once your users are [authenticated]({{< relref "/tutorials/access-management/authentication" >}}) for the platform API, you want to define which permissions they will have assigned. That's what we'll explain in more detail in this article.

Some remarks before we dive in:

As authorization in the management cluster is based on some fundamental `kubernetes` concepts, we assume basic knowledge of:

- [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and
- [Role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

Also be aware that this article deals with permissions in the management cluster only. Handling authorization in workload clusters isn't covered here, however we provide a comprehensive article on [RBAC and PSPs in workload clusters]({{< relref "/vintage/getting-started/security" >}}).

If you are mostly interested in how to set up access for certain types of users, we recommend to skip to the [typical use cases](#typical-use-cases) section. You can always catch up on the basics later, as needed. Alternatively, if you work through this page from top to bottom, you'll pick up the pieces in a more logical order and put them together later.

## Where resources reside

For controlling access to resources in a management cluster, it's vital to understand

1. whether a resource is cluster-scoped or namespace-scoped
2. if it's namespace-scoped, in which namespace they're to be found

We'll explain next which resources are to be found in which scope or namespace.

### Cluster scope

In Giant Swarm management clusters in particular, three resource types are cluster-scoped, so they're not residing in any namespace:

- [`Organization`]({{< relref "/reference/platform-api/crd/organizations.security.giantswarm.io.md" >}}) defines, well, an organization
- [`Release`]({{< relref "/reference/platform-api/crd/releases.release.giantswarm.io.md" >}}) defines a workload cluster release to use when creating a new workload cluster, or to upgrade a workload cluster to.
- [`RoleBindingTemplate`]({{< relref "/reference/platform-api/crd/rolebindingtemplates.auth.giantswarm.io.md" >}}) a template for role bindings that are applied to certain or all organizations

### Namespace `default` {#default-namespace}

Next, the following resources reside in the `default` namespace:

- App catalogs ([`Catalog`]({{< relref "/reference/platform-api/crd/catalogs.application.giantswarm.io.md" >}}) and [`AppCatalogEntry`]({{< relref "/reference/platform-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) resources) provided by Giant Swarm

### Organization namespaces {#org-namespaces}

For each [organization]({{< relref "/overview/fleet-management/multi-tenancy" >}}) there is a namespace to be used as the standard location for storing resources. In these namespaces you will usually find:

- Resources defining [workload clusters and node pools]({{< relref "/getting-started/provision-your-first-workload-cluster" >}})
- [Cloud provider credentials]({{< relref "/getting-started/prepare-your-provider-infrastructure#configure-cluster-role-identity" >}}) in the form of `Secret` resources
- [`App`]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) which defines an app to be installed in a workload clusters
- `ConfigMap` which optionally provides configuration for such an app
- `Secret` which provides additional (confidential) configuration for such an app

## Pre-defined roles {#pre-defined-roles}

Giant Swarm provides some pre-defined cluster roles (`ClusterRole` resources) which allow to grant certain permissions to common sets of resources. The most important ones are:

- __cluster-admin__: Grants all permissions to all resource types. When bound to a subject in an organization namespace, the subject will also get full permissions to resources in all [workload cluster namespaces](#wc-namespaces) belonging to that organization.
- __read-all__: Grants read permissions (verbs: get, list, watch) to most known resource types, with the exception of `Secret` and `ConfigMap`. When bound to a subject in an organization namespace, the subject will also get _read_ (get, list, watch) permissions to resources in all [workload cluster namespaces](#wc-namespaces) belonging to that organization.

Since these are `ClusterRole` resources, they can be bound either in a namespace or in the cluster scope, depending on the use case. In the [typical use cases](#typical-use-cases) section we will show some examples.

In addition there are two special cluster roles which don't define any permissions by themselves, but which allow to assign certain permissions for resources in a [workload cluster namespace](#wc-namespaces).

- __read-in-cluster-ns__: Used to assign read permissions to resources in all workload cluster namespaces belonging to the organization.
- __write-in-cluster-ns__: Used to assign full permissions to resources in all workload cluster namespaces belonging to the organization.

We'll explain the effect of binding these roles in the next section on RBAC automation.

## Role automation {#rbac-automation}

As explained previously, various resources reside in different scopes and namespaces, and in the case of the workload cluster namespaces, they even come and go as clusters are created and deleted. To simplify authorization under these circumstances, we've some automation in place, provided by [rbac-operator](https://github.com/giantswarm/rbac-operator) running in the management cluster. Here is what it does.

- __Grant admin permissions to a default group__. Where customers own a Giant Swarm installation exclusively (which is the opposite case of using a [shared installation]({{< relref "/meta/shared-installation" >}})), they name a group from their identity provider to gain admin permissions. This group will automatically be bound to the `cluster-admin` role in all namespaces and in the cluster scope.

- __Provide service accounts with admin privileges__. Service accounts named `automation` are created in the `default` namespace and in all organization namespaces, bound to the pre-defined `cluster-admin` role.

- __Grant access to releases and app catalogs__. For every subject (user, group, service account) bound to any role (`Role` or `ClusterRole`) in an organization namespace, we ensure that read permissions are granted to workload cluster releases (in the cluster scope) and app catalogs provided by Giant Swarm (in the `default` namespace).

- __Grant access to resources in workload cluster namespaces__. For every subject bound to the `read-in-cluster-ns` role in an organization namespace, we ensure read access to `App`, `ConfigMap` and `Secret` resources in the workload cluster namespaces belonging to the organization. Likewise, for subjects bound to the role `write-in-cluster-ns`, we ensure full permissions to these resources.

- __Grant access to the organization__. For every subject bound to any role in an organization's namespace, we ensure that the subject also has `get` permission to the `Organization` resource defining that organization. (Why? As this allows clients like our web UI to detect which organizations a user has access to, without requiring `list` permissions for organizations.)

### Role Binding Templates {#role-binding-templates}

In addition to the above automation, [rbac-operator](https://github.com/giantswarm/rbac-operator) reconciles the [`RoleBindingTemplate`]({{< relref "/reference/platform-api/crd/rolebindingtemplates.auth.giantswarm.io.md" >}}) custom resource.
This custom resource allows users to dynamically apply and remove `RoleBindings` across organizations.

The `spec.template` property is used to define the desired `RoleBinding` while the `spec.scopes` property allows to specify where it should be applied.
It's possible to dynamically apply `RoleBindings` to a specific set of organizations using a label matcher in `spec.scopes.organizationSelector.matchLabels`.
Furthermore, `spec.scopes.organizationSelector.matchExpressions` can be used for more advanced label matching. (for example excluding all organizations with a certain label)
If a matcher is defined, the `RoleBinding` will be applied within the organization scopes of all `Organization` CRs with matching labels.
If no matcher is defined, the `RoleBinding` will be maintained across all organization scopes.
An organization scope refers to the organization namespace as well as namespaces associated with clusters within the organization.

## Typical use cases {#typical-use-cases}

For the purpose of this documentation article we'll introduce a few example cases and then explain how to configure access for them, starting with the least permissions and ending with the highest privileges. Chances are that you can use them as a starting point for your own requirements.

1. __Read-only user__: allowed to "browse" most resources in specific organizations.

2. __Developer__: allowed to install, configure, upgrade and uninstall certain apps in/from workload clusters of a certain organization. In order to discovers clusters and navigate the web UI, users of this type also require read permission to various resources like clusters, node pools, releases, and app catalogs.

3. __Organization admin__: users who have full permissions to resources belonging to a specific [organization]({{< relref "/overview/fleet-management/multi-tenancy" >}}).

4. __Admin__: a type of user that has permission to create, modify, and delete most types of resources in the management cluster.

Next we show how to configure access for these example cases. Please take into account these remarks for all example manifests:

- You can set the resource names (for `RoleBinding` and `ClusterRoleBinding` resources) to whatever suits you and is available.
- Make sure to replace `GROUPNAME` with the exact name of your group as defined in your identity provider.
- Replace `ORGANIZATION` with the name of your organization (without `org-` prefix).
- To assign a user instead of a group, replace `kind: Group` with `kind: User` in the subject entry and set `name` the exact email address of the users as set in your identity provider.

### Configure access for read-only users {#configure-read-only}

A read-only user in the sense of the Platform API is one that can discover or, in the Giant Swarm web UI, browse resources in order to find out about existing clusters and their configuration, as well as apps installed and available.

To enable a group or user for read access to resources of one organization, you only have to bind them to the `read-all` cluster roles within the namespace of the organization.

More details on this role are given in the [pre-defined roles](#pre-defined-roles) section.

The manifest below shows how the according role bindings could be created.

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: bind-read-all-to-group
  namespace: org-ORGANIZATION
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: read-all
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: customer:GROUPNAME
```

### Configure access for app developers {#configure-app-developer}

Compared to a read-only user, this type of user would gain permission to install apps in workload clusters, change any app's configuration, and remove the app. To achieve this, we bind the pre-defined role `write-in-cluster-ns` in addition.

The according example manifest:

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: bind-read-all-to-group
  namespace: org-ORGANIZATION
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: read-all
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: customer:GROUPNAME
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: bind-write-in-cluster-ns-to-group
  namespace: org-ORGANIZATION
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: write-in-cluster-ns
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: customer:GROUPNAME
```

Like in the case of the read-only user, these bindings can be set up easily via the web UI.

### Configure access for organization admins {#configure-org-admins}

To grant full permissions to a group of users in the context of a particular organization, bind the pre-defined `cluster-admin` role to that group. Here is an example manifest:

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: bind-cluster-admin-to-group
  namespace: org-ORGANIZATION
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: customer:GROUPNAME
```

Again, this can be achieved easily via our web UI.

### Configure access for admins {#configure-admins}

As explained in [RBAC automation](#rbac-automotion), one default group is automatically assigned to the `cluster-admin` role.

In case you want to configure additional groups or users from your identity provider with admin privileges, you'll have to create an additional `ClusterRoleBinding` like this:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: assign-group-to-cluster-admin-role
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: customer:GROUPNAME
```

Be aware that it's currently not possible to configure additional admins via our web UI.

### Configure access automatically across organizations {#configure-across-organizations}

As described above, a `RoleBindingTemplate` can be applied whenever identical access needs to be maintained across several or all organizations dynamically.

The following template will create a `RoleBinding` that binds a role to a service account in all organization namespaces dynamically.
Since it's filled in dynamically, we don't give a namespace for the service account.

```yaml
apiVersion: auth.giantswarm.io/v1alpha1
kind: RoleBindingTemplate
metadata:
  name: bind-my-role-to-my-service-account
spec:
  template:
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: my-role
    subjects:
    - kind: ServiceAccount
      name: my-service-account
  scopes:
    organizationSelector: {}
```

The following template will create a `RoleBinding` that grants admin access to particular subjects in namespaces belonging to organizations which carry the `add-additional-admins=true` label.
Please note that in the below example we want to give access to a specific `ServiceAccount` so we need to include its namespace explicitly.

```yaml
apiVersion: auth.giantswarm.io/v1alpha1
kind: RoleBindingTemplate
metadata:
  name: bind-cluster-admin-in-organizations
spec:
  template:
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - kind: ServiceAccount
      name: my-service-account
      namespace: default
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: customer:GROUPNAME
  scopes:
    organizationSelector:
      matchLabels:
        add-additional-admins: true
```

Alternatively, the following scopes will result the role binding to be applied in namespaces belonging to organizations which __not__ carry the `add-additional-admins=false` label.

```yaml
...
  scopes:
    organizationSelector:
      matchExpressions:
      - key: add-additional-admins
        operator: NotIn
        values:
        - false
```

`matchExpressions` supports `In`, `NotIn`, `Exists` and `DoesNotExist` as operators for advanced selectors.
