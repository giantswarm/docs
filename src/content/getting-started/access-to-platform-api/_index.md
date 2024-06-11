---
title: Access to the platform API
description: How engineers can access the platform API to provision new workload clusters or deploy applications.
weight: 30
last_review_date: 2024-06-07
menu:
  principal:
    parent: getting-started
    identifier: getting-started-access
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How can I access the platform API?
  - What do I need to do to access the platform API?
---

Giant Swarm provides customers with a platform API to manage the cluster and workload resources. The platform API is not more than a Kubernetes API that runs on the [management cluster]({{< relref "/overview/architecture#management-cluster" >}}). The API has some extra features and custom resources allowing you to perform actions like creating a new cluster, updating a cluster, or deploying applications.

You can have multiple management clusters, for example if different cloud providers are used. Each management cluster has its own API endpoint and is isolated from the others. In this guide, you learn how to access the platform API of one of these management clusters.

To interact with the platform API, you have three options:

1. Use GitOps flavour using Flux
2. Use the `kubectl`  command-line tool with our custom plugin
3. Use the [Giant Swarm Web UI](https://docs.giantswarm.io/ui-api/)

In this guide, we focus on the second option, using the `kubectl` command-line tool. But you can find more information about the other options in the [tutorials](https://docs.giantswarm.io/tutorials/).

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

## Step 2: Log in to the platform API

There is a special command to log in to the platform API. It's called `kubectl gs login`. You need to provide the URL of the management cluster's API endpoint. The URL is usually provided by Giant Swarm.

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
