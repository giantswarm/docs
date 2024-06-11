---
title: Access to the platform API
description: How engineers can access the platform API to provision new workload clusters or deploy applications.
weight: 30
last_review_date: 2024-06-11
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

Giant Swarm's platform API, a Kubernetes API that operates on the management cluster, offers unique features and custom resources. These enable you to perform a range of actions, from creating and updating clusters to deploying applications, enhancing your cluster and workload resource management capabilities.

You can have multiple management clusters, for example, if different cloud providers are used. Each management cluster has its own API endpoint and is isolated from the others. In this guide, you learn how to access the platform API of one of these management clusters.

To interact with the platform API, you have three options:

1. Use GitOps flavour using Flux
2. Use the `kubectl` command-line tool with our custom plugin
3. Use the [Giant Swarm Web UI](https://docs.giantswarm.io/ui-api/)

This guide focuses on the second option, using the `kubectl` command-line tool. However, you can find more information about the other options in the [tutorials](https://docs.giantswarm.io/tutorials/).

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

A special command to log in to the platform API is `kubectl gs login`. You need to provide the URL of the management cluster's API endpoint, which is usually provided by Giant Swarm.

```text
$ kubectl gs login "https://api.<management cluster domain>/"
[...]
A new kubectl context named 'gs-wombat' has been created and selected. To switch back to this context later, use either of these commands:
 kubectl gs login wombat
 kubectl config use-context gs-wombat
```

When logging in, you must authenticate in your browser using the configured identity provider (for example, by signing into an Active Directory or GitHub user account).

## Step 3: View resources on the management cluster

Let's run some commands and understand what's happening under the hood.

The first command is `kubectl get nodes`, which shows how the nodes make up our management cluster.

```text
$ kubectl get nodes
NAME                                          STATUS   ROLES                  AGE   VERSION
ip-10-0-106-27.eu-west-2.compute.internal    Ready    control-plane,master   32d     v1.25.16
ip-10-0-152-147.eu-west-2.compute.internal   Ready    control-plane,master   47d     v1.25.16
ip-10-0-227-255.eu-west-2.compute.internal   Ready    control-plane,master   47d     v1.25.16
ip-10-0-69-91.eu-west-2.compute.internal     Ready    worker                 21h     v1.25.16
ip-10-0-82-78.eu-west-2.compute.internal     Ready    worker                 13h     v1.25.16
ip-10-0-97-66.eu-west-2.compute.internal     Ready    worker                 19m     v1.25.16
```

There are two roles: `control-plane` and `worker`. Note that this still relates to the management cluster. None of your business applications should ever run on the management cluster's nodes, unless you want to run custom operators.

The second command we suggest running is `kubectl get orgs`, which lists the organizations defined in your management cluster.

```text
$ kubectl get orgs
NAME                    AGE
production              97d
testing                 97d
giantswarm              97d
```

Organizations are a way to separate and isolate clusters, apps, etc., between different teams or environments. More information can be found in [multi-tenancy page]({{< relref "/vintage/platform-overview/multi-tenancy" >}}).

Finally, run the `kubectl gs get clusters -A` command, which shows all the clusters managed by your management cluster—the `-A` flag stands for all namespaces.

```text
$ kubectl gs get clusters -A
NAMESPACE          NAME    AGE    CONDITION   SERVICE PRIORITY  RELEASE   ORGANIZATION  DESCRIPTION
org-testing        rfjh2   84d    UPDATED     lowest            25.1.0    testing       Testing cluster
org-production     jn88t   91d    CREATED     highest           25.0.1    production    Production cluster
```

You may notice some important points:

1. A cluster belonging to an organization called `x` will be represented in the Kubernetes namespace `org-x` in the management cluster (that's why we use the `-A` flag to see all the namespaces)
2. Organizations may not have any clusters attached to them (yet)
3. There is a `giantswarm` organization in which we define the management cluster and its configuration. Customers are not supported to make changes in here.

Finally, you can see the YAML definition of a cluster (in this example, cluster `rfjh2` in organization `testing`) by running:

```sh
kubectl get cluster rfjh2 -n org-testing -o yaml
```

## Next step

Now that access to the platform API is verified, you are ready to [create a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}).
