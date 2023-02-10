---
linkTitle: Creating environments for GitOps
title: Creating environments for GitOps resources
description: How to create different environments to deploy different resources, configurations or versions in different stages.
weight: 70
menu:
  main:
    parent: advanced-gitops
    identifier: advanced-gitops-environments
user_questions:
  - How can I create an environment for gitops resources?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-02-10
---

# Add Workload Cluster environments

You might want to set up multiple, similar Workload Clusters that serve as for example development,
staging and production environments. You can utilize `bases` to achieve that. Let's take a look at the
`/bases/environments` folder structure.

## General note

It is possible to solve the environment and environment propagation problem in multiple ways, notably by:

- using a multi-directory structure, where each environment is represented as a directory in a `main` branch of a single
  repository
- using a multi-branch approach, where each branch corresponds to one environment, but they are in the same repo
- using a multi-repo setup, where there's one root repository providing all the necessary templates, then there is one another
  repository per environment.

Each of these approaches has pros and cons. We propose the multi-directory approach. The pros of it are:
a single repo and branch serving as the source of truth for all the environments, very easy template sharing and
relatively easy way to compare and promote configuration across environments. On the other hand, it might not be the
best solution for access control, template versioning and also easy comparing of environments.

## Environments

We are creating a new `base` type called environment. Inside there will be two folders.

The `stages` folder is how we propose to group environment specifications.
There is a good reason for this additional layer of grouping. You can use this approach to have multiple
different clusters - like the dev, staging, production - but also to have multiple different
regions where you want to spin these clusters up.

The `regions` folder is how we propose to group specifications for configurations referred to different locations or regions in the different cloud providers or datacenters.

> Please note that if you want to use multiple environment templates to create a single cluster
that uses `App CR`s for deployments, like you would like to use `dev` out of `staging` layout to set app configuration
and then use `east` from the `data-centers` to set the IP ranges, you will run into issues around merging
configurations, as currently one configuration source (i.e. `ConfigMap` in `spec.config.configMap`) completely
overrides the whole value of the same attribute coming from the other base. We're working to remove this limitation.

In order to avoid config collisions, we are specifying different config changes in different environment folders. In our case:

- `stages` should refer to versions of the cluster and apps running, and different configurations associated to the stage.
- `regions` should contain configurations referred to locality, like netwroking or DNS zones.

We're assuming that all the clusters using this environments pattern should in many regards look the same
across all the environments. Still, each environment layer introduces some key differences, like app version being deployed
for `dev/staging/prod` environments or a specific IP range, availability zones, certificates or ingresses config
for regions like `eu-central/us-west`.

To create an environment template, you need to make a  directory in `environments` that describes the best the
differentiating factor for that kind of environment, then you should create sub folder there for different possible values.
For example, for multiple regions, we recommend putting region specific configuration into
`/bases/environments/regions` folder and under there create e.g. `eu_central`, `us_west` folders.

Once your environment templates are ready, you can use them to create new clusters by placing cluster definitions
in `/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters`

### Stages

Let's create 2 example type of clusters under `/bases/environments/stages`. Each of these contain a `example_cluster` folder with an example.

```nohighlight
mkdir -p bases/environments/stages/dev/example_cluster
mkdir -p bases/environments/stages/prod/example_cluster
```

Inside each folder we will create a `kustomization.yaml` file. This file will reference an already existent `base` to get the cluster creation resources and then add some extra confiurations or resources that will conform the cluster template for the environment.

Let's see how to create these files for the different environments.

#### The development cluster

Let's create the `kustomization.yaml` file for the development cluster.

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
    - values=cluster_config.yaml
    name: ${cluster_name}-dev-config
    namespace: org-${organization}
  - files:
    - values=default_apps_config.yaml
    name: ${cluster_name}-default-apps-dev-config
    namespace: org-${organization}
generatorOptions:
  disableNameSuffixHash: true
kind: Kustomization
patches:
  - patch: |
      - type: merge
        op: add
        path: /spec/extraConfigs/0
        value:
          name: ${cluster_name}-dev-config
          namespace: org-${organization}
          priority: 110
    target:
      group: application.giantswarm.io
      kind: App
      name: ${cluster_name}
      namespace: org-\${organization}
  - patch: |
      - type: merge
        op: add
        path: /spec/extraConfigs/0
        value:
          name: ${cluster_name}-default-apps-dev-config
          namespace: org-${organization}
          priority: 110
    target:
      group: application.giantswarm.io
      kind: App
      name: ${cluster_name}-defaul-apps
      namespace: org-\${organization}
resources:
  - ../../../../../../../../bases/clusters/capa/template/
```

In addition, we are creating a configuration file `cluster_config.yaml` with the values we are changing from the cluster base:

```yaml
controlPlane:
  replicas: 1
machinePools:
- instanceType: m5.large
  maxSize: 5
  minSize: 3
  name: machine-dev-pool0
  rootVolumeSizeGB: 100
network:
  availabilityZoneUsageLimit: 1
```

We want to set an specific version for some default apps installed in the cluster too, so we create a file `default_apps_config.yaml` with the specific values.

```yaml
userConfig:
  apps:
    cilium:
      version: 0.6.1
    coreDNS:
      version: 1.13.0
```

The final structure of this folder would be:

```nohighlight
bases/environments/stages/dev
└── example_cluster
    ├── cluster_config.yaml
    ├── default_apps_config.yaml
    └── kustomization.yaml
```

And pretty much that is it for the development cluster. Let's look at the production cluster next, created with minor differences.

#### The production cluster

Let's create the `Kustomization` for the production cluster environment template.

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
    - values=cluster_config.yaml
    name: ${cluster_name}-prod-config
    namespace: org-${organization}
  - files:
    - values=default_apps_config.yaml
    name: ${cluster_name}-default-apps-prod-config
    namespace: org-${organization}
generatorOptions:
  disableNameSuffixHash: true
kind: Kustomization
patches:
  - patch: |
      - type: merge
        op: add
        path: /spec/extraConfigs/0
        value:
          name: ${cluster_name}-prod-config
          namespace: org-${organization}
          priority: 110
    target:
      group: application.giantswarm.io
      kind: App
      name: ${cluster_name}
      namespace: org-\${organization}
  - patch: |
      - type: merge
        op: add
        path: /spec/extraConfigs/0
        value:
          name: ${cluster_name}-default-apps-prod-config
          namespace: org-${organization}
          priority: 110
    target:
      group: application.giantswarm.io
      kind: App
      name: ${cluster_name}-defaul-apps
      namespace: org-\${organization}
resources:
  - ../../../../../../../../bases/clusters/capa/v0.21.0/
```
In this case we are setting the version of the base that we are using. See how to create versioned bases in the ["How to create bases" article](/advanced/gitops/bases/).

Now, we are creating a configuration file `cluster_config.yaml` with the values we are changing from the cluster base for production. We can configure a complete different value set, even override new configurations from default.

```yaml
controlPlane:
  replicas: 3
machinePools:
- instanceType: m5.2xlarge
  maxSize: 10
  minSize: 5
  name: machine-prod-pool0
  rootVolumeSizeGB: 300
network:
  availabilityZoneUsageLimit: 3
```

We want now to set an different version for some default apps installed in the cluster (for example, we want to use a known stable version). Like in dev environment, we create a file `default_apps_config.yaml` with the specific values.

```yaml
userConfig:
  apps:
    cilium:
      version: 0.6.0
    coreDNS:
      version: 1.12.0
```

It is similar to the development cluster in the following manners:

- We are using a base and modifying values with an overlay configuration.
- We can change values in the cluster config and in the default apps.

The final structure of our stages is:

```nohighlight
bases/environments/stages/
├── dev
│   └── example_cluster
│       ├── cluster_config.yaml
│       ├── default_apps_config.yaml
│       └── kustomization.yaml
└── prod
    └── example_cluster
        ├── cluster_config.yaml
        ├── default_apps_config.yaml
        └── kustomization.yaml
```

> In a similar way, we can base our stages in different cluster templates that we create from bases. We can create as many levels as we want, always keeping in mind properly setting the priorities of the config files.

#### Region specific settings for the production cluster

Let's create some bases for our region setup. Relative to root of the repository let's execute the following commands.

```nohighlight
mkdir -p bases/environments/regions/eu_central
mkdir -p bases/environments/regions/us_west

cd bases/environments/regions
```

For the `eu-central` region, we are creating a `cluster_config.yaml` file and a `kustomization.yaml` file. 

`cluster_config.yaml`

```yaml
controlPlane:
  availabilityZones:
    - eu-central-1
    - eu-central-2
    - eu-central-3
nodeCIDR: "10.32.0.0/24"
```

> These values are examples and need to be replaced by real values of the user account.

`kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
    - values=cluster_config.yaml
    name: ${cluster_name}-region-config
    namespace: org-${organization}
generatorOptions:
  disableNameSuffixHash: true
patches:
  - patch: |
      - op: add
        path: /spec/extraConfigs/0
        value:
          - name: "${cluster_name}-region-config"
            namespace: org-${organization}
            priority: 120
    target:
      group: application.giantswarm.io
      kind: App
      name: ${cluster_name}
      namespace: org-${organization}
kind: Kustomization
```

With these files we are creating a new `configmap` and adding it as an extra config in the cluster app that will create the cluster resources.

Now, for the `us-west` region we create a `cluster_config.yaml` file with different configuration. We can copy the `kustomization.yaml` file from the other region as it will be the same.

`cluster_config.yaml`

```yaml
controlPlane:
  availabilityZones:
    - us-west-1
    - us-west-2
nodeCIDR: "10.64.0.0/24"
```

We can use these as a second layer of configuration for our different clysers clusters.

The folder structure resulting from this is:

```nohighlight
bases/environments/regions
├── eu-central
│   ├── cluster_config.yaml
│   └── kustomization.yaml
└── us_west
    ├── cluster_config.yaml
    └── kustomization.yaml
```

## Add Workload Clusters based on the environment cluster templates

Now, we are using the environments created as a base for a workload cluster. In order to create a workload cluster in our repository we run the command:

```nohighlight
kubectl gs gitops add workload-cluster \
--management-cluster MC_NAME \
--name WL_NAME \
--organization ORG_NAME \
--repository-name MC_NAME-git-repo \
--base bases/environments/stages/dev \
--cluster-release 0.21.0 \
--default-apps-release 0.15.0
```

In this case, we have specified to use the `dev` stage we just created as a base. This will generate all the folders and files needed to create the cluster with the default settings of that stage.

In order to include now the `region` setting, we need to edit the file `/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WL_NAME/mapi/cluster/kustomization.yaml` and include:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
commonLabels:
  giantswarm.io/managed-by: flux
kind: Kustomization
resources:
  - ../../../../../../../../bases/environments/stages/dev
# Include a new line with the resources that provide region configuration
  - ../../../../../../../../bases/environments/regions/eu-central
```

> Note that we use the extra configs feature of App CR to patch in additional layers of configurations for out Application.
You can read more about this feature [here](https://docs.giantswarm.io/app-platform/app-configuration/#extra-configs).

## Tips for developing environments

For complex clusters, you can end up merging a lot of layers of templates and configurations. In order to keep sanity, it's very important to stablish a good priority system and respect it every time.

For example, reserve priority values for different levels:

- 100 for cluster base
- 110 for environment stage
- 120 for environment region
- 130 for cluster config

You can check the [gitops-template](https://github.com/giantswarm/gitops-template/tree/main/) repository that contains severa examples of cluster bases and configuration layers. Under `tools` folder in this repository you can find the `fake-flux-build` script that helps
you render and inspect the final result. For more information check `tools/README.md`.
