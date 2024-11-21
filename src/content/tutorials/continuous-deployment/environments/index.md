---
linkTitle: Environments
title: Creating environments for GitOps resources
description: How to deploy resources, with different configurations or versions across several environments.
weight: 70
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-environments
user_questions:
  - How can I manage different environments with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-12
---

On many occasions, you need to set good defaults for your workload clusters but have the ability to change some values depending on the type of environment: development, staging or production for example. In such a case, you can rely on specific `bases` defined on your GitOps repository. Let's see in this document how you can create a `/bases/environments` folder structure.

## General note

It's possible to solve the environment propagation problem in multiple ways, notably by:

- Using a multi-directory structure, where each environment is represented as a directory in a `main` branch of a single repository.
- Using a multi-branch approach, where each branch corresponds to one environment, but they're in the same repository.
- Using a multi-repository setup, where there's one root repository providing all the necessary templates, and then there is another repository per environment.

Each of these approaches has pros and cons. Giant Swarm relies on the multi-directory approach for multiple reasons. It's a single repository and single branch which serves as the source of truth for all the environments. Easy for template sharing and a relatively simple way to compare and promote configuration across environments. On the other hand, it needs extra work for access control management, template versioning or environment drift detection.

## Environment types

There are many ways to separate your cluster configuration but based in our experience there are two main factors: stages and regions. You can always adapt further this to your own requirements following the same principles described below.

Lets start creating a new folder in our `bases` root directory. You will call it `environments`m then you can add two new folders `stages` and `regions`.

The `stages` folder groups environment specifications. You can have a variety of clusters - like the development, staging and production - based on the same template but with different values.

The `regions` folder groups specifications for configurations referred to different locations or regions in the different cloud providers or data centers.

In order to avoid possible collisions in the configuration, you can define different changes in the configuration across several environment folders. For example:

- `stages` should refer to versions of the cluster and apps running, and different configurations associated to the stage.
- `regions` should contain configurations referred to the locality, like networking or DNS zones.

Let's assume all the clusters following this environment's pattern should look similar across all the environments. Even so, each layer introduces some key differences, like the app version being deployed for `dev/staging/prod` environments or a specific IP range.

In order to create a new environment template, you need to make a directory in `environments` that describes the best differentiating factor for that kind of environment. Then, you create a child folder with different values inside.

For example, in the case of multiple regions, the recommendation is to put region-specific configurations into `/bases/environments/regions` directory (like`eu_central` or `us_west`).

Once your environment templates are ready, you can create new clusters by placing the definitions in `/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters` and referencing the template as shown in the example below.

### Stages

Now, let's create two cluster stage templates under `/bases/environments/stages`.

```sh
mkdir -p bases/environments/stages/dev
mkdir -p bases/environments/stages/prod
```

For each stage, you create a `kustomization.yaml` file. This file has a reference to the `base` template. The goal is just to overwrite or add the values specific to this stage.

Let's see how to create these files for the different environments.

#### The development cluster

In the development cluster `kustomization.yaml` file you find three main sections. First, the block generates the `ConfigMaps` with the development configuration values. The second one is the patch structure adding a reference to these `ConfigMaps` in the cluster app customer resource. Finally the reference to the `base` template where defaults for a cluster live.

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

Next to the `kustomization`, you create the development configuration for the cluster. Use `cluster_config.yaml` as name. It only contains the values specific for this stage:

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

Now you do the same for the defaults app configuration creating the file `default_apps_config.yaml`:

```yaml
userConfig:
  apps:
    cilium:
      version: 0.6.1
    coreDNS:
      version: 1.13.0
```

The final structure of this folder would be:

```text
bases/environments/stages/dev
└── cluster_config.yaml
└── default_apps_config.yaml
└── kustomization.yaml
```

You are done with the development cluster. Let's have a look at how to define a production template with some minor differences.

#### The production cluster

You will create the same structure as the development one but with some different values for the cluster and default apps:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
    - values=cluster_config.yaml
    name: ${cluster_name}-prod-config
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
resources:
  - ../../../../../../../../bases/clusters/capa/v0.21.0/
```

__Warning__: For the sake of simplicity both reference the same base template, but in some occasions where there are breaking changes you might need to link a different template. [Read more about bases here](/advanced/gitops/bases/).

Now, you define the production configuration in a new file `cluster_config.yaml`. You can configure this time a completely different value set, even override new configurations from default.

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

The final structure of our stages is:

```nohighlight
bases/environments/stages/
├── dev
│       ├── cluster_config.yaml
│       └── kustomization.yaml
└── prod
        ├── cluster_config.yaml
        └── kustomization.yaml
```

__Note__: In a similar way, you could base your environments on different cluster templates from bases. You can create as many levels as you want, but take into account always to set the right priorities of the configuration files.

#### Regions

Following the same structure as stage environments, you can create a new folder `regions` under the `environments` bases directory.

```sh
mkdir -p bases/environments/regions/eu_central
mkdir -p bases/environments/regions/us_west

cd bases/environments/regions
```

Let's define a `eu-central` region where you describe some specifics related to the zone. For that, you create a `kustomization.yaml` file and `cluster_config.yaml` file same as you did in previous step.

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

The `Kustomize` plugin in `Flux` will create the new `ConfigMap` with the region values. Note that priority is set to `120` which will precede over the stage values.

In case you have other region, for example `us-west`, create a `cluster_config.yaml` file with the different configuration.

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

## Use environment templates

After having learnt how to create your own environment templates, lets create a cluster based one those. First, you need to get the cluster `App` resource running this command:

```sh
kubectl gs gitops add workload-cluster \
--management-cluster $MC_NAME \
--name $WC_NAME \
--organization $ORG_NAME \
--repository-name ${MC_NAME}-git-repository \
--base bases/environments/stages/dev \
--release 0.21.0
```

In this case, you decide to use the `development` stage template. [Read more about creating workload clusters]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters/#creating-your-repo-structure" >}}). In this example, you just need to tweak the `kustomization.yaml` on `/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/mapi/cluster/` to include `region` and `stage` template references:

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

__Note__:  It uses the extra configuration feature of `App` resource to patch additional layers of configurations. [Read more here]({{< relref "/tutorials/fleet-management/app-platform/app-configuration/#extra-configs" >}}).

## Tips for developing environments

For complex clusters, you can end up merging a lot of layers of templates and configurations. In order to keep sanity, it's very important to establish a good priority system and respect it every time. As an example, reserve priority values for different levels:

- 100 for cluster base
- 110 for stage environment
- 120 for the regional environment
- 130 for specific cluster configuration

Look at our [gitops-template](https://github.com/giantswarm/gitops-template/tree/main/) repository which contains several examples of cluster bases and configuration layers.

Further, [you can find tooling to verify your resources]({{< relref "/tutorials/continuous-deployment/tools/" >}}) and ensure that the configuration is correct.
