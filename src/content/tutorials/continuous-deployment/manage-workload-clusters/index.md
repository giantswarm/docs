---
linkTitle: Managing workload clusters
title: Managing workload clusters with GitOps
description: A guide to create workload clusters in Giant Swarm platform with Flux.
weight: 40
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-manage-wc
user_questions:
  - How to manage workload clusters with GitOps?
  - How to prepare repositories for use with Flux?
  - How to ensure security by combining Flux with the platform API permission model?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-10-22
---

Below you will learn how to manage infrastructure and applications in the Giant Swarm `Flux` setup.

## Requirements

In the following example, based on the [`GitOps template`](https://github.com/giantswarm/gitops-template), you will find all the resources used in this section.

It's necessary to have [`Flux` CLI](https://fluxcd.io/docs/cmd/) and [`kubectl-gs`](https://github.com/giantswarm/kubectl-gs) installed in your machine. Also you installed [`gpg`](https://gnupg.org/) to encrypt and decrypt secrets.

## Organization access control

To proceed with this tutorial, you will use a `ServiceAccount` that has a set of permissions allowing you to create and reconcile `Flux` resources. All the examples are using the organization namespace and automation `ServiceAccount`. All our management clusters have the resources already configured with the required privileges.

The `automation` `ServiceAccount` has assigned the `cluster-admin` role in the organization namespace. This role allows `Flux` to create and manage resources in the organization namespace.

__Note__: To learn more about managing roles, please read the [introduction to platform API]({{< relref "/getting-started/access-to-platform-api" >}}).

## Creating your repository structure

At Giant Swarm we recommend to have a clear hierarchical structure in your GitOps repository because:

- The general layout of the repository mirrors the infrastructure defined within Giant Swarm.
- It's easy to locate resources and know what they're and where they're deployed.
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

Our team provides a template repository where [this structure is elaborated and explained in detail](https://github.com/giantswarm/gitops-template). It's not necessary to clone the repository to follow this guide, but it can provide a good reference for every possible use case. We recommend copying, at least, the bases folder from that repository to your own repository because cluster creation uses them as templates as we will see later in this document.

### Setting up the repository

First, let's create the repository skeleton to store the resources that will be deployed. In this repository, let's create the structure described in the last section, and copy the bases for workload clusters and other apps in the Giant Swarm catalog. Follow these steps:

1. Copy bases folder from [GitOps template](https://github.com/giantswarm/gitops-template)

```sh
git clone https://github.com/giantswarm/gitops-template.git /tmp/gitops-template  && \
cp -r /tmp/gitops-template/bases . && \
rm -rf /tmp/gitops-template
```

2. Use our plugin to init the repository to set the basic structure and some `Git` hooks. This will create a folder `management-clusters`.

```sh
kubectl gs gitops init
```

### Adding a management cluster

Now, let's create the structure for the management cluster you would like to use. You can set multiple management clusters in the same repository.

```sh
export MC_NAME=mymc
kubectl gs gitops add management-cluster --name $MC_NAME --repository-name ${MC_NAME}-git-repository
```

This command creates the folder for the management cluster, the `Kustomization` file for the management cluster, `organizations` folder and `secrets` folder, already populated with an encoding key.

Then, let's create a `GitRepository` resource that points to the repository. It's needed a `GitRepository` resource for every management cluster to manage. There, the address of the repository is configured.

Now, we need to [create a secret](https://fluxcd.io/flux/cmd/flux_create_secret_git/) (we will refer to it as `GIT_CREDENTIALS_TOKEN`, please, replace with the chosen name) with the credentials to access the repository. This allows `Flux` to download the repository files in order to apply all resources. If your repository is public you don't need the secret and can delete the parameter `secret-ref` of the next command.
This process is different depending on the git platform used (ssh-keys, token, user/password). Check documentation of every provider to create the secret.

```sh
export YOUR_REPO_URL="https://github.com/<your_org>/<your_repo>.git"
flux create source git ${MC_NAME}-git-repository \
        --url=${YOUR_REPO_URL} \
        --branch=main \
        --interval=30s \
        --namespace=default \
        --ignore-paths='**,!management-clusters/MC_NAME/**,!bases/**,**.md' \
        --secret-ref=GIT_CREDENTIALS_TOKEN \
        --export > management-clusters/MC_NAME/MC_NAME-git-repo.yaml
```

Now, the `Git` repository resource is created and exported in the `management-clusters` folder. Next, you apply the resource towards the [management cluster API]({{< relref "/getting-started/access-to-platform-api" >}}) where the resources will run:

```sh
kubectl create -f management-clusters/MC_NAME/MC_NAME-git-repo.yaml
```

Observe the changes applied using `kubectl` (names will differ):

```text
kubectl get gitrepositories -n default
NAME        URL                                       READY   STATUS                                                            AGE
flux-demo   https://github.com/giantswarm/flux-demo   True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f   27s
```

Alternatively you can use `Flux` CLI too:

```text
 flux get sources git -n default
NAME            READY   MESSAGE                                                         REVISION                                        SUSPENDED
flux-demo       True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f main/74f8d19cc2ac9bee6f45660236344a054c63b71f   False
```

### Setting up secrets {#setting-up-secrets}

The next step, you configure the keys used by `Flux` in the management cluster to decipher secrets kept in the repository. Our recommendation is to keep secrets encrypted in the repository together with your applications but if your company policy does not allow it you can use [`external secret operator`](https://docs.giantswarm.io/vintage/advanced/security/external-secrets-operator/) to use different sources.

Giant Swarm uses `sops` with `pgp` for key management, creating master keys for all the `kustomizations` in the management cluster. In `kubectl-gs` you can generate a master and public key for the management cluster.

```sh
kubectl gs gitops add encryption --generate --management-cluster $MC_NAME
```

__Warning__: Please be sure you store the private key in a safe place. Losing the key will make it impossible to decrypt the secrets. The private key is stored in `./management-clusters/$MC_NAME/.sops.keys` folder.

Now, you apply the private key to the management cluster to let `Flux` decrypt the secrets.

```sh
export ORG_NAME=myorg
kubectl create secret generic sops-gpg-master \
--namespace=${ORG_NAME}t \
--from-file=${MC_NAME}.master.asc=/dev/stdin
```

Since you have the private key in a safe place and applied to the cluster, now it can be encrypted and added to the repository.

First, you import the public key in `gpg`  (replace X's by the specific file name):

```sh
gpg --import ./management-clusters/${MC_NAME}/.sops.keys/${MC_NAME}.XXXXXXXX.asc
```

And later you use it to encrypt the master key, so it can be pushed to the repository:

```sh
sops --encrypt --in-place management-clusters/MC_NAME/secrets/${MC_NAME}.gpgkey.enc.yaml
```

Finally let's apply the `Kustomization` to the management cluster API to start the GitOps process:

```sh
kubectl create -f management-clusters/MC_NAME/MC_NAME.yaml
```

From now on, any resource can be managed using `Git`, using proper `pull-requests` and reviewing the changes. The `Flux` controller will maintain the resources in the desired state.

### Managing organizations

The `organization` resource is the main entity to enable [multi-tenancy]({{< relref "/overview/fleet-management/multi-tenancy" >}}) in management clusters.

Using `kubectl-gs` you can create an organization and the structure for your workload clusters like this:

```sh
kubectl gs gitops add organization --name ORG_NAME --management-cluster MC_NAME
```

When you commit and push the changes to the repository, the organization will be created in the management cluster. You can check the organization created by running:

```text
kubectl get namespaces (names will difer)
NAME            STATUS   AGE
org-acme   Active   2m29s
```

### Managing workload clusters

In the next step, we've the organization created so now we can define some workload clusters inside it to run our applications. In Giant Swarm, we've developed several providers where clusters can be provisioned. Every provider has a different syntax for the infrastructure definition and to reduce the complexity we've defined some [`bases`](https://github.com/giantswarm/gitops-template/tree/main/bases) that helps to configure the clusters.

The configuration is structured in such a way that each layer can modify the configuration and create a custom and very powerful structure. The different possible layers would be:

- Base with fundamental cluster creation manifests
- Base versions with different modifications
- Environments that implement configuration modifications in the bases
- Clusters that implement specific configurations

There are a bunch of advantages to creating clusters starting from a base (using different versions):

- We can group clusters in logical groups that match our infra (development, staging, production)
- Modifying the base, we modify all the clusters that implement it (batch update)
- We can change the clusters between different environments easily

In this tutorial we're implementing a cluster from a base without applying any extra configuration. In order to create a base for the provider you are using, you can follow the tutorial of [base creation]({{< relref "/tutorials/continuous-deployment/bases" >}}).

In order to create a workload cluster in our repository we run the command:

```sh
kubectl gs gitops add workload-cluster \
--management-cluster MC_NAME \
--name WL_NAME \
--organization ORG_NAME \
--repository-name MC_NAME-git-repository\
--base bases/cluster/PROVIDER/template \
--cluster-release 0.21.0 \
--default-apps-release 0.15.0
```

In order to get current `cluster-release` and `default-apps-release` version you can get them from the catalog with the command:

```sh
kubectl gs get catalog -n giantswarm cluster
```

Depending on the provider of the cluster you are connected the return will vary, but you should get there at least the version for `cluster-PROVIDER` and `default-apps-PROVIDER`.

An example of the output would be:

```text
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

You can add user configurations to the cluster created including different configmaps and add them to the manifests.

### Installing managed apps

It's just as easy to install managed apps in existing workload clusters. In this part of the guide, we will assume you have completed the previous steps and have both an organization and a cluster running.

We're showing the process installing `Grafana` from the `GiantSwarm` app catalog in the namespace `monitoring`.
In order to add the manifest files to the repository, we run the command (check version numbers for latest releases):

```sh
kubectl gs gitops add app --management-cluster MC_NAME --workload-cluster WL_NAME --organization ORG_NAME --app grafana --catalog giantswarm --target-namespace monitoring --version 2.0.2
```

The latest version number can be retrieved from the catalog using `helm search repository giantswarm/grafana`

Commit the newly generated files back to your git repository and push the changes to the remote. After a few minutes you should see the application resources appear on your workload cluster.

To learn more about how to utilize and configure Managed Apps, please refer to [the documentation]({{< relref "/overview/fleet-management/app-management">}}).

This completes the guide. If you no longer need them, you can delete the organization and cluster.

To learn more about Giant Swarm's `kubectl` plugin, visit [`kubectl-gs` documentation]({{< relref "/vintage/use-the-api/kubectl-gs/" >}}).

## Troubleshooting

It's common to find errors like the following when trying to apply resources:

```nohighlight
resource Kustomization... was blocked due to the following policies

flux-multi-tenancy:
  serviceAccountName: 'validation error: .spec.serviceAccountName is required. Rule
    serviceAccountName failed at path /spec/serviceAccountName/'
  sourceRefNamespace: preconditions not met
```

For security reasons, our platform enforces the definition of `.spec.serviceAccountName` for `Kustomization`/`HelmRelease` resources to ensure that the resources are created with the correct permissions. In this case, let's define the `serviceAccountName` equal to `automation` to allow the controller to manage resources.
