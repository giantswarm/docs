---
linkTitle: Managing workload clusters
title: Managing workload clusters with GitOps
description: A guide to create workload clusters in Giant Swarm platform with FluxCD.
weight: 20
menu:
  main:
    parent: advanced-gitops
    identifier: advanced-gitops-manage-workload-clusters
user_questions:
  - How to manage workload clusters with GitOps?
  - How to prepare repositories for use with FluxCD?
  - How to ensure security by combining FluxCD with the Management API permission model?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-01-25
---

In this document you will learn how to manage infrastructure and applications by utilizing Flux CD - a set of GitOps operators installed in Giant Swarm management clusters.

## Managing resources with Flux

In this section, we will guide you through an example Flux setup on a Giant Swarm Management Cluster. You will create resources locally. Mentions of _example resources_ or _example repository_ refers to [giantswarm/gitops-template](https://github.com/giantswarm/gitops-template), where you can find all resources used in this section in full, unabbreviated forms and Flux will use these to sync with.

We will be using [Flux CLI](https://fluxcd.io/docs/cmd/) and [kubectl-gs](https://github.com/giantswarm/kubectl-gs). Please make sure you have both installed on your machine. If you would rather follow the guide without them, use the example resources provided.

## Restrictions in the web UI {#web-ui-restrictions}

The [Giant Swarm web UI]({{<relref "/platform-overview/web-interface">}}) allows editing and deleting resources like clusters and apps in an interactive way. However, for resources managed through GitOps, these capabilities are restricted. Otherwise changes and even deletions would get reverted through FluxCD.

The UI will indicate this by showing something like this:

<img src="managed-through-gitops.png" alt="" width="339" height="47" />

The restrictions in particular are:

- **Organizations** managed by FluxCD cannot be deleted via the web UI.

- **Clusters** managed by FluxCD cannot be edited, upgraded, or deleted via the web UI.

- **Node pools** managed by FluxCD cannot be edited or deleted via the web UI.

- **Apps** managed by FluxCD cannot be edited or uninstalled via the web UI.

As a signal that a resource is managed through FluxCD, the web UI relies on the existence of these two resource labels:

- `kustomize.toolkit.fluxcd.io/name`
- `kustomize.toolkit.fluxcd.io/namespace`

## Access control for organizations

To proceed with this tutorial, you need to use a ServiceAccount with a set of permissions that allows you to create and reconcile Flux resources. All the examples are using `default` namespace and `automation` ServiceAccount in that namespace. You will find them in every Management Cluster and they are already assigned with the required privileges.

If you wish to proceed by creating the resources in one of the Organization namespaces (`org-*`), you will need to create a ServiceAccount there and assign the following roles to it:

- `read-all-customer`
- `write-client-certificates-customer`
- `write-flux-resources-customer`
- `write-nodepools-customer`
- `write-organizations-customer`
- `write-silences-customer`

To learn how to view and assign roles, please refer to [Access control for organizations in the web user interface]({{< relref "/platform-overview/web-interface/organizations/access-control/index.md" >}}).

## GiantSwarm Management Cluster security policies

If you are creating any of the resources we talk about in this document on a GiantSwarm Management Cluster, you may see the following error:

```nohighlight
resource Kustomization... was blocked due to the following policies

flux-multi-tenancy:
  serviceAccountName: 'validation error: .spec.serviceAccountName is required. Rule
    serviceAccountName failed at path /spec/serviceAccountName/'
  sourceRefNamespace: preconditions not met
```

Due to extra security policies enforced by Kyverno, setting `.spec.serviceAccountName` for `Kustomization`/`HelmRelease` resources in our Management Clusters is mandatory. Usually, you will want to use `serviceAccountName: "automation"`.

## Creating your repo structure

Whilst a GitOps repository can have any arbitrary layout, which provides flexibility in adapting the repository to your own infrastructure, at Giant Swarm we recommend a clear hierarchical structure which provides a number of advantages:

- The general layout of the repository closely mirrors the infrastructure defined within Giant Swarm.
- It's easy to locate resources and know what they are and where they are deployed.
- Our engineers are familiar with the layout which saves time during support requests.

The recommended structure (simplified) is:

```text
bases
├── clusters
└── ...
management-clusters
└── MC_NAME
    ├── secrets
    └── organizations
        └── ORG_NAME
            └── workload-clusters
                ├── WC_NAME1
                │   ├── mapi                installed from the MC
                │   │    ├── apps
                │   │    │    └── APP1
                │   │    └── cluster
                │   └── [out-of-band]       installed directly in the WC
                └── WC_NAME2
```

We provide a template repository where this structure is elaborated and explained in detail in [giantswarm/gitops-template](https://github.com/giantswarm/gitops-template). It is not necessary to clone the repository to follow this guide, but it can provide a good reference for every possible use case. We recommend copying, at least, the bases folder from that repository to your own repository because cluster creation uses them as templates as we will see later in this document.

### Setting up sources

First thing's first - create a bare-bones repository where we will store the resources that will be deployed. In this repository we need to create the structure described in the last section, and copy the bases for workload clusters and other apps in the Giant Swarm catalog. Follow these steps:

1. Copy bases folder from [giantswarm/gitops-template](https://github.com/giantswarm/gitops-template)

2. Init the repository in order to create the first part of the structure and some git hooks. This will create a folder `management-clusters`. Use the command:

```nohighlight
kubectl gs gitops init
```

**Note**: To learn more about Giant Swarm's kubectl plugin, visit [kubectl-gs documentation]({{< relref "/use-the-api/kubectl-gs/" >}}).

### Attach the repo to a management cluster

Now we create the structure for the management clusters we are going to deploy to. Run this command for every management cluster.

```nohighlight
kubectl gs gitops add management-cluster --name MC_NAME --repository-name MC_NAME-git-repo --gen-master-key
```

This command creates the folder for the management cluster, the `Kustomization` file for the MC, `organizations` folder and `secrets` folder, already populated with an encoding key.

Then, we create a Flux `GitRepository` resource that points to the repository. We need a `GitRepository` resource for every management cluster we want to manage. In the `GitRepository` resource we define the URL where our repository is stored.

Now, we need to [create a secret](https://fluxcd.io/flux/cmd/flux_create_secret_git/) (we will refer to it as GIT_CREDENTIALS_SECRET, please, replace with the chosen name) with the credentials to access the repository. This will allow Flux to download the repo files in order to apply all resources. If your repo is public you don't need the secret and can safely delete the parameter `secret-ref` of the next command.
This process is different depending on the git platform used (ssh-keys, token, user/password). Check documentation of every provider to create the secret.

```nohighlight
flux create source git MC_NAME-git-repo \
        --url=YOUR_REPO_URL \
        --branch=main \
        --interval=30s \
        --namespace=default \
        --ignore-paths='**,!management-clusters/MC_NAME/**,!bases/**,**.md' \
        --secret-ref=GIT_CREDENTIALS_SECRET \
        --export > management-clusters/MC_NAME/MC_NAME-git-repo.yaml
```

This command creates the Custom Resource for us and exports it to a YAML file in the `management-clusters` folder.

Time to apply the generated YAML:

```nohighlight
kubectl create -f management-clusters/MC_NAME/MC_NAME-git-repo.yaml
```

We can see if the change was applied using `kubectl` (names will differ):

```nohiglight
kubectl get gitrepositories -n default
NAME        URL                                       READY   STATUS                                                            AGE
flux-demo   https://github.com/giantswarm/flux-demo   True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f   27s
```

or Flux CLI - `flux`:

```nohighlight
 flux get sources git -n default
NAME            READY   MESSAGE                                                         REVISION                                        SUSPENDED
flux-demo       True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f main/74f8d19cc2ac9bee6f45660236344a054c63b71f   False
```

Next, we configure the keys that will be used in the management cluster Flux to decipher secrets so they can be safely stored in the repository.

In this example we are using `sops` with `pgp` key management and creating a master key for all the kustomizations in this management cluster.

This master key is created automatically by the `kubectl gs gitops add management-cluster` command so we only need to apply the secret in the cluster and safely store the private GPG key so we can use it to encrypt files before pushing them to the repo.

To import the private key (replace X's by the specific file name):

```nohighlight
gpg --import ./management-clusters/grizzly/.sops.keys/master.XXXXXXXXXXXXXXXXXXXX.asc
```

> Important! You must safely store the private key and keep it secret!

To create the secret in the cluster we run:

```nohighlight
kubectl create -f management-clusters/MC_NAME/secrets/MC_NAME.gpgkey.enc.yaml
```

Now, in order to safely store the key in the repo we can encode the YAML file using `sops`:

```nohighlight
sops --encrypt --in-place management-clusters/MC_NAME/secrets/${MC_NAME}.gpgkey.enc.yaml
```

Now we are applying the `Kustomization` file to the management cluster so the files in this repo will be monitored and the resources created accordingly. After this, any resource creation in the cluster doesn't need kubectl access. Now, if you add any more CRs inside the folders managed by the `Kustomization` they will be picked up by Flux automatically once it's committed and pushed.

```nohighlight
kubectl create -f management-clusters/MC_NAME/MC_NAME.yaml
```

### Managing organizations

The highest level Giant Swarm custom resource you can create is an [Organization]({{< relref "/use-the-api/management-api/crd/organizations.security.giantswarm.io.md" >}}).

In order to create the files in the repository, run the command (in the root of the repo):

```nohighlight
kubectl gs gitops add organization --name ORG_NAME --management-cluster MC_NAME
```

This is enough to create the Organization on our own. It creates automatically the organization namespace where your cluster resources will be applied.

```nohighlight
kubectl get namespaces (names will difer)
NAME            STATUS   AGE
org-acme   Active   2m29s
```

### Managing workload clusters

In the next step, we have the organization created so now we can define some workload clusters inside it to run our applications. In Giant Swarm, we have developed several providers where clusters can be provisioned. Every provider has a different syntax for the infrastructure definition and to reduce the complexity we have defined some [`bases`](https://github.com/giantswarm/gitops-template/tree/main/bases) that helps to configure the clusters.

The configuration is structured in such a way that each layer can modify the configuration and create a custom and very powerful structure. The different possible layers would be:

- Base with fundamental cluster creation manifests
- Base versions with different modifications
- Environments that implement config modifications in the bases
- Clusters that implement specific configurations

There are a bunch of advantages to creating clusters starting from a base (using different versions):

- We can group clusters in logical groups that match our infra (dev, pre, prod...)
- Modifying the base, we modify all the clusters that implement it (batch update)
- We can change the clusters between different environments easily

In this tutorial we are implementing a cluster from a base without applying any extra configuration. In order to create a base for the provider you are using, you can follow the tutorial of [base creation]({{< relref "/advanced/gitops/bases" >}}).

In order to create a workload cluster in our repository we run the command:

```nohighlight
kubectl gs gitops add workload-cluster \
--management-cluster MC_NAME \
--name WL_NAME \
--organization ORG_NAME \
--repository-name MC_NAME-git-repo \
--base bases/cluster/PROVIDER/template \
--cluster-release 0.21.0 \
--default-apps-release 0.15.0
```

In order to get current `cluster-release` and `default-apps-release` version you can get them from the catalog with the command:

```nohighlight
kubectl gs get catalog -n giantswarm cluster
```

Depending on the provider of the cluster you are connected the return will vary, but you should get there at least the version for `cluster-PROVIDER` and `default-apps-PROVIDER`.

An example of the output would be:

```nohighlight
CATALOG   APP NAME                    VERSION   UPSTREAM VERSION   AGE   DESCRIPTION
cluster   capa-internal-proxy-stack   0.1.0     0.1.0              64d   repository to aggregate CRs necessery to create capa internal outgoing proxy clu...
cluster   cluster-aws                 0.21.0                       23h   A helm chart for creating Cluster API clusters with the AWS infrastructure provi...
cluster   cluster-shared              0.6.4     0.0.1              64d   A library chart of shared CAPI cluster helpers
cluster   default-apps-aws            0.15.0                       2d    A Helm chart for default-apps-aws
cluster   default-apps-azure          0.0.8     0.0.1              47h   A Helm chart defining the preinstalled apps running in all Giant Swarm Azure clu...
cluster   outgoing-proxy-stack        0.2.4     0.1.0              26d   repository to aggregate CRs necessery to create capa internal outgoing proxy clu...
```

Where we can extract that the current version of `cluster-aws` is `0.21.0` and `default-apps-aws` is `0.15.0`.

This will create the folders and the files needed. If you already applied the management cluster `Kustomization`, the cluster will start to be created as you commit and push the files.

You can add user configurations to the cluster created including different config maps and add them to the manifests.

### Installing managed apps

It is just as easy to install managed apps in existing workload clusters. In this part of the guide, we will assume you have completed the previous steps and have both an organization and a cluster running.

We are showing the process installing `Grafana` from the `GiantSwarm` app catalog in the namespace `monitoring`.
In order to add the manifest files to the repo, we run the command (check version numbers for latest releases):

```nohighlight
kubectl gs gitops add app --management-cluster MC_NAME --workload-cluster WL_NAME --organization ORG_NAME --app grafana --catalog giantswarm --target-namespace monitoring --version 2.0.2
```

The latest version number can be retrieved from the catalog using `helm search repo giantswarm/grafana`

Commit the newly generated files back to your git repository and push the changes to the remote. After a few minutes you should see the application resources appear on your workload cluster.

To learn more about how to utilize and configure Managed Apps, please refer to [the documentation]({{< relref "/platform-overview/app-platform">}}).

This completes the guide. If you no longer need them, you can delete the organization and cluster.
