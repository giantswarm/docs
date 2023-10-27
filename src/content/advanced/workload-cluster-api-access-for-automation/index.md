---
linkTitle: Automation Workload Cluster API access
title: Authentication for the Workload Cluster API in automation
description: Using the Workload Cluster API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to obtain a service account token to use in such a scenario.
weight: 20
menu:
  main:
    identifier: workload-cluster-api-access-for-automation
    parent: advanced
last_review_date: 2023-10-27
user_questions:
  - How can I use the Workload Cluster API in a programmatic way?
  - How do I grant access to Kubernetes API from my CI system?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

## Introduction

Kubernetes allows you to interact with its API server securely by using service account tokens. These tokens are primarily used for automation purposes, allowing scripts and applications to perform tasks on the Kubernetes cluster without the need for user intervention. Though they are commonly used by pods to get easy access to the API within the cluster the same method can be reused for automation running out of the cluster.

This documentation entry provides step-by-step instructions on how to access the Kubernetes cluster API using service account tokens.

## Prerequisites

Before you proceed, make sure you have the following prerequisites:

1. [Make sure you are logged in the right Workload Cluster]({{< relref "/getting-started/create-workload-cluster#step-4-log-in-to-the-workload-cluster" >}}).
2. The [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) command-line tool installed on your local machine.
3. The necessary permissions to create and manage service accounts within the Kubernetes cluster.

## Steps to Access the Kubernetes Cluster API using Service Account Tokens

### Create a Service Account

You need to create a service account that represents your automation task. Ideally you select the right namespace to live in (you could create a `automation` namespace):

```bash
kubectl create serviceaccount <service-account-name> -n <namespace>
```

### Assign RBAC to the Service Account

To grant the necessary permissions to your service account, create a Role or ClusterRole and a RoleBinding or ClusterRoleBinding. For example, if you want to grant full access within a specific namespace:

Create a Role/ClusterRole:

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

Create a RoleBinding/ClusterRoleBinding:

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

### Retrieve the Service Account Token

Use the following command to get the service account token for your automation task:

```bash
SECRET=$(kubectl get serviceaccount <service-account-name> -n <namespace> -o jsonpath='{.secrets[0].name}')
TOKEN=$(kubectl get secret $SECRET -n <namespace> -o jsonpath='{.data.token}' | base64 -d)
```

### Configure Authentication in your tool or script

In case you use the [a Kubernetes client](https://kubernetes.io/docs/reference/using-api/client-libraries/) you can set the `TOKEN` obtained in the step before to grant access to the API. The exact steps may vary depending on the programming language and Kubernetes client library you are using. Usually the best is to generate a `kubeconfig` and pass it to the client build function.

For generating a `kubeconfig` you can use this script:

```bash
#!/bin/bash

# Read cluster argument
CLUSTER=$1

# Init env vars
SECRET=$(kubectl --namespace default get sa jenkins -o jsonpath='{.secrets[0].name}')
TOKEN=$(kubectl --namespace default get secret $SECRET -o jsonpath='{.data.token}' | base64 --decode)
CA_CERT=$(kubectl --namespace default get secret $SECRET -o jsonpath='{.data.ca\.crt}')
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

## Further reading

- [Management API access for automation]({{< relref "/use-the-api/management-api/authentication/automation" >}}) explains how to authenticate in the Management API as an automation tool
- [Authentication as a user]({{< relref "/use-the-api/management-api/authentication/user" >}}) explains how to authenticate in the Management API as an interactive user
- [Authorization in the Management API]({{< relref "/use-the-api/management-api/authorization" >}}) explains how to assign permissions in the Management API to authenticated users
