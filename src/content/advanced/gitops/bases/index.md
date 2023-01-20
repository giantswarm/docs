---
linkTitle: Creating a base template clusters
title: Creating a base template for workload clusters
description: How to create a base template to create workload clusters with different configurations.
weight: 70
menu:
  main:
    parent: advanced-gitops
    identifier: advanced-gitops-bases
user_questions:
  - How can I create an base template for workload clusters in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-01-20
---

# Add a CAPx (CAPI) Workload Cluster template (cluster App based)

Our CAPx (CAPI provider-specific clusters) are delivered by Giant Swarm as a set of two applications. The first one is an [App Custom Resource](https://docs.giantswarm.io/platform-overview/app-platform/)(CR) with a Cluster instance definition, while the second one is an App CR containing all the default applications needed for a cluster to run correctly. As such, creating a CAPx cluster means that you need to deliver two configured App CRs to the Management Cluster.

Adding definitions can be done on two levels: shared cluster template and version-specific template, see
[create shared template base](#create-shared-template-base) and [create versioned base](#create-versioned-base-optional).


**IMPORTANT**, CAPx configuration utilizes the
[App Platform Configuration Levels](/getting-started/app-platform/app-configuration/#levels),
in the following manner:

- cluster templates provide default configuration via App' `config` field,
- cluster instances provide custom configuration via App' `userConfig` field, that is overlaid on top of `config`.

See more about this approach [here](https://github.com/giantswarm/rfc/tree/main/merging-configmaps-gitops).

## Choose bases

In order to avoid code duplication, it is advised to utilize the
[bases and overlays](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#bases-and-overlays)
of Kustomize in order to configure the cluster.

## Create shared cluster template base {#create-shared-template-base}

**IMPORTANT:** shared cluster template base should not serve as a standalone base for cluster creation, it is there only to abstract
App CRs that are common to all clusters versions, and to provide basic configuration for default apps App.
It is then used as a base to other bases, which provide an overlay with a specific configuration. This is to avoid
code duplication across bases.

**Bear in mind**, this is not a complete guide of how to create a perfect base, but rather a mere summary of basic
steps needed to move forward. Hence, instructions here will not always be precise in telling you what to change,
as this can strongly depend on resources involved, how much of them you would like to include into a base, etc.

We provide a command to create bases for CAPI clusters in an easy way. A base can be created by running:

```nohighlight
kubectl gs gitops add base --provider capa
```

This command will create the folder structure and the specific folder for the provider capa, including the template files in the `template` folder. The structure would be:

```nohighlight
bases
└── clusters
    └── capa
        └── template
            ├── cluster_config.yaml
            ├── cluster.yaml
            ├── default_apps_config.yaml
            ├── default_apps.yaml
            └── kustomization.yaml
```

The current possible values for the providers can be checked in the [command reference]({{< relref "/use-the-api/kubectl-gs/gitops/add-base" >}})

## Create versioned base (optional) {#create-versioned-base-optional}

**IMPORTANT**, versioned cluster template bases use a shared cluster template base and overlay it with a preferably generic configuration for a given cluster version. Versioning comes from the fact that `values.yaml` schema may change over multiple releases, and although minor differences can be handled on the `userConfig` level, it is advised for the bases to follow major `values.yaml` schema versions to avoid confusion.

There is one example of a versioned base in the `gitops-template` repository for capo [v0.6.0](https://github.com/giantswarm/gitops-template/tree/main/bases/clusters/capo/>=v0.6.0) as major changes were introduced to the `values.yaml` in the [cluster-openstack v0.6.0 release](https://github.com/giantswarm/cluster-openstack/releases/tag/v0.6.0).

**IMPORTANT**, despite the below instructions referencing `kubectl-gs` for templating configuration, `kubectl-gs` generates configuration for the most recent schema only. If you configure a base for older versions of cluster app, it is advised to check what is generated against the version-specific `values.yaml`.

In this example we are creating a custom version for capa base:

1. Create a directory structure:

    ```nohighlight
    mkdir -p bases/clusters/capa/v0.21.0
    ```

1. Use the [kubectl gs template cluster](/use-the-api/kubectl-gs/template-cluster/) to template
cluster resources, see example for the `capa` provider below. Use arbitrary values for the mandatory fields, we
will configure them later in our process:

    ```nohighlight
    kubectl gs template cluster \
    --name mywcl \
    --organization myorg \
    --provider capa | yq -s '.metadata.name' 
    ```

1. This creates four files but we are only interested in the cluster userconfig file `mywcl-userconfig.yml`. We will extract the values and create a new `cluster-config.yaml` file in our version folder:

    ```nohighlight
    cat mywcl-userconfig.yml|yq eval '.data.values' > bases/clusters/capa/v0.21.0/cluster_config.yaml
    ```

    The content of the file will be something like this:

    ```nohighlight
    aws: {}
    bastion: {}
    clusterName: mywcl
    controlPlane:
      replicas: 3
    machinePools:
    - instanceType: m5.xlarge
      maxSize: 10
      minSize: 3
      name: machine-pool0
      rootVolumeSizeGB: 300
    network:
      availabilityZoneUsageLimit: 3
    organization: myorg
    ```

1. Replace `mywcl`, `myorg` values from the previous step with variables:

    ```nohighlight
    sed -i "s/myorg/${organization}/g" bases/clusters/capa/0.21.0/cluster_config.yaml
    sed -i "s/mywcl/${cluster_name}/g" bases/clusters/capa/0.21.0/cluster_config.yaml
    ```

1. Check `cluster_config.yaml` against the version-specific `values.yaml`, and tweak it if necessary to match the
expected schema. At this point you may also provide extra configuration, like additional availability zones, node
pools, etc. If you used `kubectl gs template` to get the values, this should be aligned with the latest version. If you were trying to create a different version, you might need to check proper values for that version.

1. Create a patch for the cluster App CR to provide the newly created configuration. For this create a file `patch_config.yaml` with this content:

    ```nohighlight
    apiVersion: application.giantswarm.io/v1alpha1
    kind: App
    metadata:
      name: ${cluster_name}
      namespace: org-${organization}
    spec:
      extraConfigs:
        - kind: configMap
          name: ${cluster_name}-config
          namespace: org-${organization}
          priority: 1
    ```

1. Create the `kustomization.yaml`, referencing the template, and generating the ConfigMap out of `cluster_config.yaml`:

    ```nohighlight
    apiVersion: kustomize.config.k8s.io/v1beta1
    configMapGenerator:
      - files:
        - values=cluster_config.yaml
        name: ${cluster_name}-config
        namespace: org-${organization}
    generatorOptions:
      disableNameSuffixHash: true
    kind: Kustomization
    patchesStrategicMerge:
      - patch_config.yaml
    resources:
      - ../template
    ```

With these steps you have created a new base, built upon the original template which you can use to create workload clusters with the `kubectl gs gitops add workload-cluster --base` command as it is explained in the [workload cluster creation tutorial](/advanced/gitops/manage-workload-clusters/#managing-workload-clusters).
