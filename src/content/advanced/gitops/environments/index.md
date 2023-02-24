---
linkTitle: Creating environments for GitOps
title: Creating environments for GitOps resources
description: How to deploy resources, with different configurations or versions across several environments.
weight: 70
menu:
  main:
    parent: advanced-gitops
    identifier: advanced-gitops-environments
user_questions:
  - How can I manage different environments with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-02-10
---

# Add Workload Cluster environments

On many occasions, you need to set good defaults for your Workload Clusters but have the ability to change some values depending on the type of environment: development, staging or production for example. In such a case, you can rely on specific `bases` defined on your GitOps repository.  Let's see in this document how you can create a `/bases/environments` folder structure.

## General note

It is possible to solve the environment propagation problem in multiple ways, notably by:

- using a multi-directory structure, where each environment is represented as a directory in a `main` branch of a single
  repository
- using a multi-branch approach, where each branch corresponds to one environment, but they are in the same repo
- using a multi-repo setup, where there's one root repository providing all the necessary templates, and then there is another repository per environment.

Each of these approaches has pros and cons. Giant Swarm relies on the multi-directory approach for multiple reasons. It is a single repo and single branch which serves as the source of truth for all the environments. Easy for template sharing and a relatively simple way to compare and promote configuration across environments. On the other hand, it needs extra work for access control management, template versioning or environment drift detection.

## Environments types

There are many ways to separete your cluster configuration but over the years we have seen in most cases there are two main factors: stages and regions. You can always adapt further this to your own requirements following the same principles described below.

Lets start creating a new folder in our `bases` root directory. We will call it `environments and we will add two new folders `stages` and `regions`.

The `stages` folder is how we propose to group environment specifications. There is a good reason for this additional layer. You can use it for having multiple different clusters - like the dev, staging and production - but also to have multiple different regions where you want to spin these clusters up.

The `regions` folder is how we propose to group specifications for configurations referred to different locations or regions in the different cloud providers or datacenters.

__Note__: If you want to use multiple environment templates to create a single cluster that uses `App CR`s for deployments, for example, you would like to use `dev` layout to set app configuration and then use `east` from the `data-centers` to set the IP ranges, you might run into issues around merging configurations, as currently one configuration source (i.e. `ConfigMap` in `spec.config.configMap`) completely overrides the whole value of the same attribute coming from the other base. We're working to remove this limitation. This means for example that setting `machinePools` in several files will result on selecting only the full block of the file with higher priority.

In order to avoid possible collisions in the configuration, we define the different changes in the configuration across several environment folders. In our case:

- `stages` should refer to versions of the cluster and apps running, and different configurations associated to the stage.
- `regions` should contain configurations referred to the locality, like networking or DNS zones.

We are assuming all the clusters following this environment's pattern should look similar across all the environments. Even so, each layer introduces some key differences, like the app version being deployed for `dev/staging/prod` environments or a specific IP range.

In order to create a new environment template, you need to make a directory in `environments` that describes the best differentiating factor for that kind of environment. Then, you create a subfolder with different values inside.

For example, in the case of multiple regions, we recommend putting region-specific configurations into `/bases/environments/regions` directory in specific folders (e.g. `eu_central`, and `us_west`).

Once your environment templates are ready, you can create new clusters by placing the definitions in `/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters` and referencing the template as we will see below.

### Stages

Now, let's see how to put the explanation into practice. We create two cluster stage templates under `/bases/environments/stages`. 

```nohighlight
mkdir -p bases/environments/stages/dev
mkdir -p bases/environments/stages/prod
```

For each stage, we create a `kustomization.yaml` file. This file has a reference to the `base` template. Our goal is just to overwrite or add the values specific to this stage.

Let's see how to create these files for the different environments.

#### The development cluster

In the development `kustomization.yaml` file for the development cluster you find three main sections. First, the block generates the Config Maps with the development configuration values. The second one is the patch structure adding a reference to these Config Maps in the cluster app customer resource. Finally the reference to the `base` template where defaults for a cluster live.

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

Next to the kustomization, we are creating the development configuration for the cluster. We call it `cluster_config.yaml`. It only contains the values specific for this stage:

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

Now we do the same for the defaults app configuration creating the file `default_apps_config.yaml`:

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
└── cluster_config.yaml
└── default_apps_config.yaml
└── kustomization.yaml
```

We are done with the development cluster. Let's have a look at how to define a production template with some minor differences.

#### The production cluster

We are creating the same structure as the development one but with some different values for the cluster and default apps:

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

__Warning__: for the sake of simplicity we are referencing the same base template, but in some occasions where there are breaking changes you might need to link a different template. ["You can check complex scenarios here" article](/advanced/gitops/bases/).

Now, we are creating a configuration file `cluster_config.yaml` with the values we are changing from the cluster base for production. We can configure a completely different value set, even override new configurations from default.

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

We want now to set a different version for some default apps installed in the cluster (for example, we want to use a known stable version). Like in the dev environment, we create a file `default_apps_config.yaml` with the specific values.

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
│       ├── cluster_config.yaml
│       ├── default_apps_config.yaml
│       └── kustomization.yaml
└── prod
        ├── cluster_config.yaml
        ├── default_apps_config.yaml
        └── kustomization.yaml
```

__Note__: In a similar way, we can base our stages on different cluster templates that we create from bases. We can create as many levels as we want, but take into account always to set the right priorities of the config files.

#### Regions 

Following the same structure as stage environments, we create a new folder `regions` under the `environments` bases directory.

```nohighlight
mkdir -p bases/environments/regions/eu_central
mkdir -p bases/environments/regions/us_west

cd bases/environments/regions
```

Let's say we want to define a `eu-central` region where we describe some specifics related to that zone. For that, we create a `kustomization.yaml` file and `cluster_config.yaml` file same as we did with stages.

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

```yaml
controlPlane:
  availabilityZones:
    - eu-central-1
    - eu-central-2
    - eu-central-3
nodeCIDR: "10.32.0.0/24"
```
__Note__: These values are examples and need to be replaced by real values of the user account.


The kustomize plugin in Flux will create the new Config Map with the region values. Note that priority is set to `120` which will precede over the stage values.

In case we have other region, for example `us-west`, we can create a `cluster_config.yaml` file with the different configuration. 

```yaml
controlPlane:
  availabilityZones:
    - us-west-1
    - us-west-2
nodeCIDR: "10.64.0.0/24"
```

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

## Use environment templates for your Workload Clusters 

After having learnt how to create our own environment templates, lets create a cluster based one those. First, we need to get the cluster App custom resource running this command:

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

In this case, we have decided to use the `development` stage template. [We have already explained where to define your workload resources](https://docs.giantswarm.io/advanced/gitops/manage-workload-clusters/#creating-your-repo-structure), now we just need to tweak the `kustomization.yaml` on `/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/mapi/cluster/` to include `region` and `stage` template references:

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

__Note__:  We use the 'extra configs` feature of App CR to patch additional layers of configurations for our Application. You can read more about this feature [here](https://docs.giantswarm.io/app-platform/app-configuration/#extra-configs).

## Tips for developing environments

For complex clusters, you can end up merging a lot of layers of templates and configurations. In order to keep sanity, it's very important to establish a good priority system and respect it every time. As an example, reserve priority values for different levels:

- 100 for cluster base
- 110 for stage environment 
- 120 for the regional environment 
- 130 for specific cluster config

We have published [gitops-template](https://github.com/giantswarm/gitops-template/tree/main/) repository which contains several examples of cluster bases and configuration layers. 

Furtherlly, you can find some helpers in the`tools` folder. For example, we have developed `fake-flux-build` scrip to render and inspect the final resources merging all values. For more information check `tools/README.md`.
