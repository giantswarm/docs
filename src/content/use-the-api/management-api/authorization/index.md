---
linkTitle: Authorization
title: Authorization in the Management API
description: Granting users specific permission to certain resources is what authorization is all about. The Management API uses Kubernetes' role based access control (RBAC) primitives and provides automation on top of it to make authorization easy for most real-life use cases. Here we explain them in detail.
weight: 20
menu:
  main:
    identifier: uiapi-managementapi-authorization
    parent: uiapi-managementapi
last_review_date: 2022-02-24
aliases:
  - /reference/management-api/authorization/
  - /ui-api/management-api/authorization/
user_questions:
  - What automation is working in a management cluster to ensure RBAC permissions?
  - How can I set up access to resources in the management cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

Once your users are [authenticated]({{< relref "/use-the-api/management-api/authentication" >}}) for the Management API, you want to define which permissions they will have assigned. That's what we'll explain in more detail in this article.

Some remarks before we dive in:

As authorization in the management cluster is based on some fundamental Kubernetes concepts, we assume basic knowledge of:

- [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and
- [Role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

Also be aware that this article deals with permissions **in the management cluster only**. Handling authorization in workload clusters is not covered here, however we provide a comprehensive article on [RBAC and PSPs in workload clusters]({{< relref "/getting-started/rbac-and-psp" >}}).

If you are mostly interested in how to set up access for certain types of users, we recommend to skip to the [typical use cases](#typical-use-cases) section. You can always catch up on the basics later, as needed. Alternatively, if you work through this page from top to bottom, you'll pick up the pieces in a more logical order and put them together later.

## Where resources reside

For controlling access to resources in a management cluster, it is vital to understand

1. whether a resource is **cluster-scoped** or **namespace-scoped**
2. if it is namespace-scoped, **in which namespace** they are to be found

We'll explain next which resources are to be found in which scope or namespace.

### Cluster scope

In Giant Swarm management clusters in particular, three resource types are cluster-scoped, so they are not residing in any namespace:

- [`Organization`]({{< relref "/use-the-api/management-api/crd/organizations.security.giantswarm.io.md" >}}) defines, well, an organization
- [`Release`]({{< relref "/use-the-api/management-api/crd/releases.release.giantswarm.io.md" >}}) defines a workload cluster release to use when creating a new workload cluster, or to upgrade a workload cluster to.
- [`RoleBindingTemplate`]({{< relref "/use-the-api/management-api/crd/rolebindingtemplates.auth.giantswarm.io.md" >}}) a template for roleBindings that are applied to certain or all organizations

### Namespace `default` {#default-namespace}

Next, the following resources reside in the `default` namespace:

- App catalogs ([`Catalog`]({{< relref "/use-the-api/management-api/crd/catalogs.application.giantswarm.io.md" >}}) and [`AppCatalogEntry`]({{< relref "/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) resources) provided by Giant Swarm

### Organization namespaces {#org-namespaces}

For each [organization]({{< relref "/platform-overview/multi-tenancy" >}}) there is a namespace to be used as the standard location for storing resources. In these namespaces you will usually find:

- Resources defining [workload clusters and node pools]({{< relref "/use-the-api/management-api/creating-workload-clusters" >}})
- [Cloud provider credentials]({{< relref "/use-the-api/management-api/credentials" >}}) in the form of `Secret` resources

### Workload cluster namespaces {#wc-namespaces}

For every workload cluster, there is a namespace with a name identical to the workload cluster name. In this namespace, resources related to apps installed in the workload cluster are located. The resources are of these types:

- [`App`]({{< relref "/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) which defines an app to be installed in a workload clusters
- `ConfigMap` which optionally provides configuration for such an app
- `Secret` which provides additional (confidential) configuration for such an app

## Pre-defined roles {#pre-defined-roles}

Giant Swarm provides some pre-defined cluster roles (`ClusterRole` resources) which allow to grant certain permissions to common sets of resources. The most important ones are:

- **cluster-admin**: Grants all permissions to all resource types. When bound to a subject in an organization namespace, the subject will also get full permissions to resources in all [workload cluster namespaces](#wc-namespaces) belonging to that organization.
- **read-all**: Grants read permissions (verbs: get, list, watch) to most known resource types, with the exception of `Secret` and `ConfigMap`. When bound to a subject in an organization namespace, the subject will also get _read_ (get, list, watch) permissions to resources in all [workload cluster namespaces](#wc-namespaces) belonging to that organization.

Since these are `ClusterRole` resources, they can be bound either in a namespace or in the cluster scope, depending on the use case. In the [typical use cases](#typical-use-cases) section we will show some examples.

In addition there are two special cluster roles which don't define any permissions by themselves, but which allow to assign certain permissions for resources in a [workload cluster namespace](#wc-namespaces).

- **read-in-cluster-ns**: Used to assign read permissions to resources in all workload cluster namespaces belonging to the organization.
- **write-in-cluster-ns**: Used to assign full permissions to resources in all workload cluster namespaces belonging to the organization.

We'll explain the effect of binding these roles in the next section on RBAC automation.

## RBAC automation {#rbac-automation}

As explained previously, various resources reside in different scopes and namespaces, and in the case of the workload cluster namespaces, they even come and go as clusters are created and deleted. To simplify authorization under these circumstances, we have some automation in place, provided by [rbac-operator](https://github.com/giantswarm/rbac-operator) running in the management cluster. Here is what it does.

**Grant admin permissions to a default group**. Where customers own a Giant Swarm installation exclusively (which is the opposite case of using a [shared installation]({{< relref "/support/shared-installation" >}})), they name a group from their identity provider to gain admin permissions. This group will automatically be bound to the `cluster-admin` role in all namespaces and in the cluster scope.

**Provide service accounts with admin privileges**. Service accounts named `automation` are created in the `default` namespace and in all organization namespaces, bound to the pre-defined `cluster-admin` role.

**Grant access to releases and app catalogs**. For every subject (user, group, service account) bound to any role (`Role` or `ClusterRole`) in an organization namespace, we ensure that read permissions are granted to workload cluster releases (in the cluster scope) and app catalogs provided by Giant Swarm (in the `default` namespace).

**Grant access to resources in workload cluster namespaces**. For every subject bound to the `read-in-cluster-ns` role in an organization namespace, we ensure read access to `App`, `ConfigMap` and `Secret` resources in the workload cluster namespaces belonging to the organization. Likewise, for subjects bound to the role `write-in-cluster-ns`, we ensure full permissions to these resources.

**Grant access to the organization**. For every subject bound to any role in an organization's namespace, we ensure that the subject also has `get` permission to the `Organization` resource defining that organization. (Why? As this allows clients like our web UI to detect which organizations a user has access to, without requiring `list` permissions for organizations.)

### Role Binding Templates {#role-binding-templates}

In addition to the above automation, [rbac-operator](https://github.com/giantswarm/rbac-operator) reconciles the [`RoleBindingTemplate`]({{< relref "/use-the-api/management-api/crd/rolebindingtemplates.auth.giantswarm.io.md" >}}) custom resource. 
This custom resource allows users to dynamically apply and remove `RoleBindings` across organizations.


The `spec.template` property is used to define the desired `RoleBinding` while the `spec.scopes` property allows to specify where it should be applied.
It is possible to dynamically apply `RoleBindings` to a specific set of organizations using a label matcher in `spec.scopes.OrganizationSelector.matchLabels`.
If the label matcher is defined, the `RoleBinding` will be applied within the organization scopes of all `Organization` CRs that carry the label.
If no label matcher is defined, the `RoleBinding` will be maintained across all organization scopes.
An organization scope refers to the organization namespace as well as namespaces associated with clusters within the organization.

## Typical use cases {#typical-use-cases}

For the purpose of this documentation article we'll introduce a few example cases and then explain how to configure access for them, starting with the least permissions and ending with the highest privileges. Chances are that you can use them as a starting point for your own requirements.

1. **Read-only user**: allowed to "browse" most resources in specific organizations.

2. **App developer**: allowed to install, configure, upgrade and uninstall certain apps in/from workload clusters of a certain organization. In order to discovers clusters and navigate the web UI, users of this type also require read permission to various resources like clusters, node pools, releases, and app catalogs.

3. **Organization admin**: users who have full permissions to resources belonging to a specific [organization]({{< relref "/platform-overview/multi-tenancy" >}}).

4. **Admin**: a type of user that has permission to create, modify, and delete most types of resources in the management cluster.

Next we show how to configure access for these example cases. Please take into account these remarks for all example manifests:

- You can set the resource names (for `RoleBinding` and `ClusterRoleBinding` resources) to whatever suits you and is available.
- Make sure to replace `GROUPNAME` with the exact name of your group as defined in your identity provider.
- Replace `ORGANIZATION` with the name of your organization (without `org-` prefix).
- To assign a user instead of a group, replace `kind: Group` with `kind: User` in the subject entry and set `name` the exact email address of the users as set in your identity provider.

### Configure access for read-only users {#configure-read-only}

A read-only user in the sense of the Management API is one that can discover or, in the Giant Swarm web UI, browse resources in order to find out about existing clusters and their configuration, as well as apps installed and available.

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

Our [web UI]({{< relref "/platform-overview/web-interface/organizations/access-control" >}}) makes it easy to create these role bindings interactively. Go to **Organizations**, select the organization, and navigate to the **Access control** tab. Then, one by one, select the pre-defined roles in the left column and add the user or group in the **Subjects** tab on the right.

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

Be aware that it is currently not possible to configure additional admins via our web UI.

### Configure access automatically across organizations {#configure-across-organizations}

As described above, a `RoleBindingTemplate` can be applied whenever identical access needs to be maintained across several or all organizations dynamically.

The following template will create a `RoleBinding` that binds a role to a service account in all organizations dynamically.
Since it is filled in dynamically, we do not give a namespace for the service account.

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

The following template will create a `RoleBinding` that grants admin access to particular subjects in each organization which carries the `add-additional-admins=true` label.
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
