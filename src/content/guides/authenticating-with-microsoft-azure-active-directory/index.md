---
title: Authenticating with Microsoft Azure Active Directory
description: Tutorial on how to setup Authentication with Microsoft Azure Active Directory in kubectl.
type: page
weight: 30
tags: ["tutorial"]
user_questions:
  - How can I use Azure Active Directory to authenticate cluster access?
  - How to use OIDC for cluster authentication?
---

# Authenticating with Microsoft Azure Active Directory

A Giant Swarm installation can be configured to authenticate with Microsoft Azure Active Directory (AAD). This setting has to be enabled by Giant Swarm staff once per installation. After that all tenant clusters will be set up to authenticate against AAD using OpenID Connect (OIDC).

On the user side, you can then authenticate using the Azure Auth Provider of `kubectl`. Your access to a cluster is decided by RBAC roles mapped to your user or group.

## Setting up `kubectl` for Azure auth

### 1. Set up a user

```nohighlight
kubectl config \
  set-credentials "<username>" \
  --auth-provider=azure \
  --auth-provider-arg=environment=AzurePublicCloud \
  --auth-provider-arg=client-id=<kubectl-app-id> \
  --auth-provider-arg=tenant-id=<tenant-id> \
  --auth-provider-arg=apiserver-id=<apiserver-app-id>
```

- `username` can be freely chosen, but must be unique within your local `kubeconfig`.
- The 3 IDs are global settings that are set by your company. You should be able to obtain those internally.

### 2. Set up a cluster

```nohighlight
kubectl config \
  set-cluster <clustername> \
  --server=https://<api-server-endpoint> \
  --certificate-authority=/path/to/ca.crt
```

- `clustername` can be freely chosen, but must be unique within your local `kubeconfig`.
- Kubernetes API Server endpoint and CA you can get from the web UI (Happa) or using `gsctl`.

### 3. Set up a context

```nohighlight
kubectl config \
  set-context <contextname> \
  --cluster=<clustername> \
  --user=<username>
```

- `contextname` can be freely chosen, but must be unique within your local `kubeconfig`.
- `clustername` and `username` are the names chosen in step 1 and 2.

### 4. Authenticate on your first command

When you run your first `kubectl` command you will see something like the following:

```nohighlight
$ kubectl get node
To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code DEHTRY693 to authenticate.
```

This step needs to be done only once and will register your kubectl as an authenticated device. From then on you can freely run commands against the cluster (limited only by the roles given to you on said cluster).

__Note__ that in some cases (depending on AD settings) the device authentication can only be done in a Browser running on a Windows machine.

## Creating a `kubeconfig` for general usage

If you are a Cluster Admin and want to create `kubeconfig` files to give out to your users you can use following template:

```yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
  name: <clustername>
    certificate-authority: /path/to/ca.crt
    server: https://<api-server-endpoint>
users:
- name: <username>
  user:
    auth-provider:
      name: azure
      config:
        apiserver-id: <apiserver-app-id>
        client-id: <kubectl-app-id>
        tenant-id: <tenant-id>
contexts:
- context:
    cluster: <clustername>
    user: <username>
  name: <contextname>
current-context: <contextname>
```

If you set all the above names to something generic, you can send the same file to all your users. The actual identification of each user will happen through the device authentication request done with their first `kubectl` command.

Furthermore, to make the `kubeconfig` self-contained, you can replace `/path/to/ca.crt` with an inline representation of the file. For that you need to base64-encode the contents of `ca.crt` and paste them into the `kubeconfig`.

## Binding roles to users and groups coming from AAD

When authenticating with AAD your user identifies to Kubernetes with a username and the groups you are a member of in AAD. A Cluster Admin can bind roles to these to grant access on a specific cluster.

As explained in [Securing your Cluster with RBAC and PSP
](/guides/securing-with-rbac-and-psp/) you can either use the default roles or define custom `Role` or `ClusterRole` resources to bind to subjects.

In the following examples we'll use one of the default cluster roles.

__Note__ that you can only bind roles if your own role is wider defined than the role you want to bind for others. When in doubt use `cluster-admin` to apply bindings.

### Binding a single user

AAD prefixes usernames so that they look like the following:

```nohighlight
https://sts.windows.net/<tenant-id>/#<username>
```

__Note:__ Here, `username` is not the freely chosen username you set in `kubectl`, but the username claim set to a specific attribute of your AAD user. Usually this will be set to your username attribute in AAD.

Based on that, we bind the user like the following:

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: username-global-admin
subjects:
  - kind: User
    name: https://sts.windows.net/<tenant-id>/#<username>
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

### Binding a group of users

Unlike usernames, groups are not prefixed. You can identify them by the Object ID of the group in AAD.

Based on that, we bind a group like the following:

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: username-global-admin
subjects:
  - kind: Group
    name: <group-oid>
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

### Revoking access

Access is revoked as soon as the user has either been removed from a bound group or completely from the AAD tenant.

## Further reading

- [Securing your Cluster with RBAC and PSP
](/guides/securing-with-rbac-and-psp/)
- [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Azure Active Directory plugin for client authentication](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/client-go/plugin/pkg/client/auth/azure/README.md)
