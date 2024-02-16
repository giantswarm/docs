---
title: Access to the management cluster
description: The Giant Swarm Management API is easily accessible by means of kubectl-gs, a kubectl plugin developed by Giant Swarm. This tutorial guides you throughout some of the most important features of the tool.
weight: 30
aliases:
  - /getting-started/management-cluster
menu:
  main:
    parent: getting-started
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I access the management cluster?
  - How can I access the Giant Swarm Management API?
last_review_date: 2023-06-12
---

Giant Swarm provides customers with their own _management cluster (MC)_. You can have multiple management clusters, for example if different cloud providers are used. Each management cluster runs Kubernetes plus operators that create and manage all the workload clusters (WCs). On workload clusters, you deploy and run actual business applications.

To create workload clusters – or install managed apps (such as ingress-nginx) on them – you need to access the management cluster. Alternatively, you can also deploy workload clusters or managed apps with GitOps, but we still recommend that you first start out by manually accessing the management cluster since you may need this for manual investigation or deployments.

## Step 1: Install the necessary tools

Select your operating system:

{{< tabs >}}
{{< tab title="Any">}}

1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
2. Install [krew](https://krew.sigs.k8s.io/)
3. Install `kubectl-gs` by running: `kubectl krew install gs`

{{< /tab >}}
{{< tab title="macOS (Homebrew)">}}

```sh
brew install kubernetes-cli krew
kubectl krew install gs
```

{{< /tab >}}
{{< /tabs >}}

## Step 2: Log in to your management cluster

For the purpose of this tutorial, we will start from Giant Swarm's _Web UI_, reachable via the URL that we provide to customers when we finish setting up a cluster. The hostname in the URL usually starts with `happa` (our internal name of the Web UI).

The web interface shows an overview of the clusters belonging to the organization selected in the top-right corner (in the screenshot: `testing`).

![Clusters listed in the Web UI](happa-clusters.png)

Click "List clusters via the Management API" on the bottom to see which command to run for logging into your cluster.

**Run this command in your shell.** The command performs authentication, creates a kubectl context and prints a message similar to this:

```text
$ kubectl gs login "https://api.<management cluster domain>/"
[...]
A new kubectl context has been created named 'gs-wombat' and selected. To switch back to this context later, use either of these commands:
  kubectl gs login wombat
  kubectl config use-context gs-wombat
```

When logging in, you have to authenticate in your browser using the configured identity provider (for example by signing into an Active Directory or GitHub user account).

## Step 3: View resources on the management cluster

Let's run some commands and understand what's happening under the hood.

The first command is `kubectl get nodes`. This will show us the nodes making up our management cluster.

```text
$ kubectl get nodes
NAME                                          STATUS   ROLES                  AGE   VERSION
ip-10-0-5-103.eu-central-1.compute.internal   Ready    worker                 19h   v1.24.10
ip-10-0-5-121.eu-central-1.compute.internal   Ready    control-plane,master   19h   v1.24.10
ip-10-0-5-14.eu-central-1.compute.internal    Ready    control-plane,master   19h   v1.24.10
ip-10-0-5-163.eu-central-1.compute.internal   Ready    control-plane,master   19h   v1.24.10
ip-10-0-5-183.eu-central-1.compute.internal   Ready    worker                 19h   v1.24.10
ip-10-0-5-5.eu-central-1.compute.internal     Ready    worker                 19h   v1.24.10
ip-10-0-5-53.eu-central-1.compute.internal    Ready    worker                 19h   v1.24.10
```

There are two kinds of roles: `control-plane` and `worker`. Note that this still relates to the management cluster. None of your business applications should ever run on the management cluster's nodes, unless you want to run custom operators.

The second command we suggest running is `kubectl get orgs`. This will show the organizations that are defined in your management cluster.

```text
$ kubectl get orgs
NAME                    AGE
production              97d
testing                 97d
giantswarm              97d
```

Organizations are a way to isolate clusters, apps, etc. between different teams or environments. More information can be found in [Multi-tenancy]({{< relref "/vintage/platform-overview/multi-tenancy" >}}).

Finally, run the `kubectl gs get clusters -A` command, which will show you all the clusters managed by your management cluster. The `-A` flag stands for _all namespaces_.

```text
$ kubectl gs get clusters -A
NAMESPACE          NAME    AGE    CONDITION   SERVICE PRIORITY  RELEASE   ORGANIZATION  DESCRIPTION
org-testing        rfjh2   84d    UPDATED     lowest            18.4.0    testing       n/a
org-production     jn88t   91d    CREATED     highest           18.0.1    production    n/a
```

You may notice some important points:

1. A cluster belonging to an organization called `x` will be represented in the Kubernetes namespace `org-x` in the management cluster (that's why we use the `-A` flag to see all the namespaces)
2. Organizations may not have any clusters attached to them (yet)
3. There is a `giantswarm` organization in which we define the management cluster and its own configuration. Customers are not supported to make changes in here.

Finally, you can see the YAML definition of a cluster (in this example, cluster `rfjh2` in organization `testing`) by running:

```sh
kubectl get cluster rfjh2 -n org-testing -o yaml
```

## Next steps

You can follow along the "Getting started" articles in order. Most likely, you want to [create a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}) now.
