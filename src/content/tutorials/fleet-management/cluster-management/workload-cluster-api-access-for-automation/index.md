---
linkTitle: Automation access
title: Access your workload cluster API via automation
description: Access your cluster API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to obtain a service account token to use in such a scenario.
weight: 20
menu:
  principal:
    identifier: tutorials-fleet-management-clusters-automation
    parent: tutorials-fleet-management-clusters
user_questions:
  - How can I use the workload Cluster API in a programmatic way?
  - How do I grant access to Kubernetes API from my CI system?
last_review_date: 2025-11-28
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

## Introduction

A `Kubernetes` cluster allows you to interact with its API server securely by using service account tokens. These tokens are primarily used for automation purposes, allowing scripts and applications to perform tasks on the cluster without the need for user intervention. Though they're commonly used by pods to get easy access to the API within the cluster the same method can be reused for automation running out of the cluster.

This documentation entry provides step-by-step instructions on how to access the `Kubernetes` cluster API using service account tokens.

## Prerequisites

Before you proceed, make sure you have the following prerequisites:

1. [Make sure you are logged in the right workload cluster]({{< relref "/tutorials/access-management/authentication/user" >}}).
2. The [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) command-line tool installed on your local machine.
3. The necessary permissions to create and manage service accounts within the cluster.

## Create a service account

You need to create a `ServiceAccount` that represents your automation task. Ideally you select the right namespace to live in (you could create a `automation` namespace):

```bash
kubectl create serviceaccount <service-account-name> -n <namespace>
```

Since Kubernetes 1.30 version, the API does not create the token automatically for service accounts. You need to explicitly annotate a secret with `kubernetes.io/service-account.name` opting to the service account. Now Kubernetes uses [TokenRequest](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) to obtain that credentials.

Since you want a token for a external system to automate actions on the Kubernetes API, you can just use the `create token` command with the optional `--duration` flag to generate a token representing the service account.

```bash
kubectl create token <service-account-name> (--duration 3600h)
```

The token will be returned by not saved as Kubernetes secret anymore, it makes easier also to rotate those credentials for your external system.

## Assign a role to the service account

To grant the necessary permissions to your service account, create a role or cluster role. Additionally, you need to bind the role to the service account. For example, if you want to grant full access within a specific namespace:

Create a `Role` (namespace wide) or `ClusterRole`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: <role-name>
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["get", "list", "watch", "create", "update", "delete"]
```

Create a `RoleBinding` (namespace wide) or `ClusterRoleBinding`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: <rolebinding-name>
subjects:
- kind: ServiceAccount
  name: <service-account-name>
  namespace: <namespace>
roleRef:
  kind: ClusterRole
  name: <role-name>
  apiGroup: rbac.authorization.k8s.io
```

### Configure authentication in your tool

In case you use the [a `Kubernetes` client](https://kubernetes.io/docs/reference/using-api/client-libraries/) you can set the `TOKEN` obtained in the step before to grant access to the API. The exact steps may vary depending on the programming language and Kubernetes client library you are using. Usually the best is to generate a `kubeconfig` and pass it to the client build function.

For generating a `kubeconfig` for the hypothetic `jenkins` service account, you can use this script:

```bash
#!/bin/bash

# Read cluster argument
CLUSTER=$1

# Init env vars
TOKEN=$(kubectl create token jenkins')
CA_CERT=$(kubectl config view --raw -o jsonpath='{.clusters[0].cluster.certificate-authority-data}')
API_URL=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')

# Get CA from secret
echo $CA_CERT | base64 -D > /tmp/$CLUSTER-ca.pem

# Create kubeconfig
kubectl --kubeconfig /tmp/kubeconfig_$CLUSTER.yaml config set-cluster default \
  --server $API_URL \
  --embed-certs \
  --certificate-authority /tmp/$CLUSTER-ca.pem
kubectl --kubeconfig /tmp/kubeconfig_$CLUSTER.yaml config set-credentials default --token $TOKEN
kubectl --kubeconfig /tmp/kubeconfig_$CLUSTER.yaml config set-context gs-$CLUSTER \
  --cluster default \
  --user default
kubectl --kubeconfig /tmp/kubeconfig_$CLUSTER.yaml config use-context gs-$CLUSTER

cat /tmp/kubeconfig_$CLUSTER.yaml
```

**Note**: You have to be already logged in the cluster with enough permissions to generate the token and access to the `ServiceAccount`. The CA is obtained from the current kubeconfig. [More info how to access the platform API and login into the workload cluster API](https://docs.giantswarm.io/getting-started/access-to-platform-api/).

You can save the script as `kubeconfig-sa.sh` and run it passing a cluster ID to get the `kubeconfig` content as result.

```bash
./kubeconfig-sa.sh <cluster-ID>
---
apiVersion: v1
kind: Config
clusters: [...]
contexts:
- context:
    cluster: default
    user: default
  name: cluster-ID
current-context: cluster-ID
preferences: {}
users:
- name: default
  user:
    token: <...>
```

Now you can query the API to check it works passing the `--kubeconfig` argument as part of the `kubectl`.

```bash
kubectl --kubeconfig ./<cluster-id>.yaml get nodes
```

Learn how to [access the platform API]({{< relref "/tutorials/access-management/authentication/automation" >}}) for your automation.
