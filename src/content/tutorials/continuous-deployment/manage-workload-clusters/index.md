---
linkTitle: Managing workload clusters
title: Managing workload clusters with GitOps
description: A guide to create workload clusters in Giant Swarm platform with Flux.
weight: 50
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
last_review_date: 2024-12-12
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

At Giant Swarm, the recommendation is to have a clear hierarchical structure in your repository so you will benefit from the following:

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

Our team provides a template repository where [the structure is explained in detail](https://github.com/giantswarm/gitops-template). Cloning the entire repository to follow this guide isn't required, but it can provide a good reference for every possible use case. You can copy, at least, the `bases` folder to your repository because the cluster creation uses them as templates, as described later.

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

Now, you need to [create a secret](https://fluxcd.io/flux/cmd/flux_create_secret_git/) (referred as `GIT_CREDENTIALS_TOKEN`) with the credentials to access the repository. It enables `Flux` to download the repository files in order to apply all resources. In case your repository is public you don't need the secret and can delete the parameter `secret-ref` of the next command.

__Note__: This process is different depending on the git platform used (ssh-keys, token, user/password). Check documentation of every provider to create the secret.

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

Now, the `GitRepository` resource is created and exported in the `management-clusters` folder. Next, you apply the resource towards the [management cluster API]({{< relref "/getting-started/access-to-platform-api" >}}) where the resources will run:

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

The next step, you configure the keys used by `Flux` in the management cluster to decipher secrets kept in the repository. Our recommendation is to keep secrets encrypted in the repository together with your applications but if your company policy doesn't allow it you can use [`external secret operator`]({{< relref "/vintage/advanced/security/external-secrets-operator/" >}}) to use different sources.

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

In the next step, you will create a workload cluster for running your applications. In Giant Swarm, there are several providers supported. Every provider has a different syntax for the infrastructure definition. In order to reduce complexity you can use the [`bases`](https://github.com/giantswarm/gitops-template/tree/main/bases) which abstract some of those details.

The configuration is structured in layers, and each layer has the ability to modify the previous layer. The different layers would be:

- Base layer with the fundamental cluster manifests
- Base version layer with different modifications by version
- Environment layer with modifications for your different stages
- Clusters specific layer with modifications for each cluster

Those layers give us the advantage of group clusters by type of stage, modify all the clusters of certain type at once, or even promote a cluster from one environment to another.

Read the [base creation tutorial]({{< relref "/tutorials/continuous-deployment/bases" >}}) if you want to create your own base. Otherwise, you can use the bases provided by Giant Swarm.

The next command will create a workload cluster in the organization using the base from the `gitops-template`:

```sh
export WC_NAME=mywc
kubectl gs gitops add workload-cluster \
--management-cluster ${MC_NAME} \
--name ${WC_NAME} \
--organization ORG_NAME \
--repository-name ${MC_NAME}-git-repository\
--base bases/cluster/capa/template \
--release 29.0.0
```

__Note__: The `--release` flag is optional. If you don't provide it, the latest version of the base will be used. If you want to use a specific version, you can check the check the releases page of the cluster provider.

The command will create the folders and the files needed. If you already applied the management cluster `Kustomization`, the cluster will start to be created as you commit and push the files.

Alternatively, you can add the flag `--cluster-user-config` with the values you want to add to the cluster and it will generate a `ConfigMap` with the values.

#### Upgrading workload clusters

To upgrade a workload cluster, you need to change the `release.version` field in the `cluster-user-config` file. After that, you commit and push the changes to the repository. The `Flux` controller will detect the changes and the cluster will be upgraded to the new version. The release version can be found by running `kubectl get releases` in the management cluster. You only need to set the version in the `release.version` field.

Example: 

`kubectl get releases`:

```sh
NAME         KUBERNETES VERSION   FLATCAR VERSION   AGE     STATE
aws-29.4.0   1.29.10              3975.2.2          29d     active
```

You set the `release.version` in the `cluster-user-config` file to `29.4.0` and commit and push the changes.

### Installing managed apps

Installing applications is easy now that you have the GitOps structure in place. In this tutorial you are going to install `Grafana` to understand the process.

In the next command, you will add the `Grafana` application to the repository structure, setting the version and namespace:

```sh
kubectl gs gitops add app --management-cluster ${MC_NAME} --workload-cluster ${WC_NAME} --organization ${ORG_NAME} --app grafana --catalog giantswarm --target-namespace monitoring --version 2.0.2
```

__Note__: To inspect which `Grafana` versions are available, you can use the `helm search repository giantswarm/grafana` command.

The output for the previous command will be the following:

```text
management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/mapi/
└── apps
    ├── grafana
    │   └── appcr.yaml
    └── kustomization.yaml
```

Committing and pushing the changes to the repository will trigger the creation of the `Grafana` application in the workload cluster. Now you can check the status of the app in the platform API:

```text
kubectl get app -n $ORG_NAME
alba-grafana-agent    2.0.2    10s    deployed
```

In the workload cluster the `Helm` release and all the resources applied should be created in the `monitoring` namespace.

## Troubleshooting

In case you have any issues with the creation of the resources, you can check the logs of the `Flux` controller to understand what's happening. You can use the following command to check the logs:

```sh

```nohighlight
resource Kustomization... was blocked due to the following policies

flux-multi-tenancy:
  serviceAccountName: 'validation error: .spec.serviceAccountName is required. Rule
    serviceAccountName failed at path /spec/serviceAccountName/'
  sourceRefNamespace: preconditions not met
```

For security reasons, our platform enforces the definition of `.spec.serviceAccountName` for `Kustomization`/`HelmRelease` resources to ensure that the resources are created with the correct permissions. In this case, let's define the `serviceAccountName` equal to `automation` to allow the controller to manage resources.

Keep learning GitOps [reading how to use different configuration by environment]({{< relref "/tutorials/continuous-deployment/environments/" >}}).
