---
linkTitle: Base templates
title: Creating a base template for your workload cluster
description: How to create a base templates for your workload clusters with different configurations.
weight: 40
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-bases
user_questions:
  - How can I create an base template for workload clusters in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-11
---

In Giant Swarm the interface to define a workload cluster is built on top of `Helm` and [the app platform]({{< relref "/overview/fleet-management/app-management/" >}}). The application custom resource contains the specification and configuration of the cluster in this format:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
  name: mycluster
spec:
  catalog: cluster
  name: cluster-aws
  namespace: org-myorg
  ...
```

As such, creating cluster means that you need to deliver a configured `App` resource to the platform API also known as the management cluster API where your cluster will run.

Adding definitions is done via the [cluster provider `Helm` template](https://github.com/giantswarm/cluster-aws) (AWS example). The chart definition contains a basic provider agnostic definition which is a dependency and points to the [cluster generic template](https://github.com/giantswarm/cluster). Also, it has another dependency which contains all the common resources running by default within a cluster, it's called [cluster shared](https://github.com/giantswarm/cluster-shared).

As consequence, the cluster configuration leverages the [app platform configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration/#levels" >}}), in the following manner:

- The cluster template has a default configuration via `App` `config` field.
- User can add additional custom configuration via `App` `extraConfig` field, which is overlaid on top of the default `config`. The file set with higher priority will prevail in case of colliding configuration values.

__Note__: [Here](https://github.com/giantswarm/rfc/tree/main/merging-configmaps-gitops) you can find more information why this approach was chosen.

In order to avoid code duplication, the [bases and overlays](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#bases-and-overlays) use Kustomize to enhance the cluster configuration.

## Create a cluster template base {#create-template-base}

The shared cluster template base shouldn't serve as a standalone base for cluster creation, it's only abstracting `App` resources common to all clusters versions. It's then used as a base for other bases, which provide an overlay with a specific configuration. That way you avoid code duplication across bases.

__Note__: This isn't a complete guide of how to create a perfect base, but rather a mere summary of basic steps needed to move forward. Hence, instructions here won't always be precise in telling you what to change, as this can strongly depend on the resources involved, how much of them you would like to include in a base, etc.

You can create bases for workload clusters easily thanks to the `kubectl gs` command:

```sh
kubectl gs gitops add base --provider capa
```

This command will create the folder structure and the specific folder for the provider `capa` (AWS flavour), including the template files in the `template` folder. The structure would be:

```text
bases
└── clusters
    └── capa
        └── template
            ├── cluster_config.yaml
            ├── cluster.yaml
            └── kustomization.yaml
```

The current possible values for the providers can be checked in the [command reference]({{< relref "/reference/kubectl-gs/gitops/add-base" >}}).

## Create versioned base (optional) {#create-versioned-base-optional}

Versioning cluster template bases is a good practice to avoid breaking changes in `values.yaml` schema affecting your clusters.

The `kubectl-gs` base command for templating configuration only generates configuration for the most recent schema. If you configure a base for older versions of the cluster app, it's advised to check what's generated against the version-specific `values.yaml`.

In this example you create a custom version for AWS base:

1. Create a directory structure:

    ```nohighlight
    mkdir -p bases/clusters/capa/v0.21.0
    ```

2. Use the [kubectl gs template cluster]({{< relref "/reference/kubectl-gs/template-cluster" >}}) to template cluster resources, see an example for the `capa` provider below. Use arbitrary values for the mandatory fields, we will configure them later in our process:

    ```nohighlight
    kubectl gs template cluster \
    --name mywcl \
    --organization myorg \
    --provider capa | yq -s '.metadata.name'
    ```

3. The above command generates four files, though in the current example you are only interested in the cluster user configuration file `mywcl-userconfig.yaml`.Extract the values and create a new `cluster-config.yaml` file in our version folder:

    ```nohighlight
    cat mywcl-userconfig.yaml | yq eval '.data.values' > bases/clusters/capa/v0.21.0/cluster_config.yaml
    ```

    The content of the file will be something like this:

    ```nohighlight
    aws: {}
    bastion: {}
    clusterName: mywcl
    controlPlane:
      replicas: 3
    machinePools:
      machine-pool0:
        availabilityZones:
        - eu-central-1a
        instanceType: m5.xlarge
        maxSize: 10
        minSize: 3
        rootVolumeSizeGB: 300
    network:
      availabilityZoneUsageLimit: 3
    organization: myorg
    ```

4. Replace `mywcl`, `myorg` values from the previous step with variables:

    ```nohighlight
    sed -i "s/myorg/${organization}/g" bases/clusters/capa/0.21.0/cluster_config.yaml
    sed -i "s/mywcl/${cluster_name}/g" bases/clusters/capa/0.21.0/cluster_config.yaml
    ```

5. Check `cluster_config.yaml` against the version-specific `values.yaml`, and tweak it if necessary to match the expected schema. At this point you may also provide extra configuration, like additional availability zones, node pools, etc. If you used `kubectl gs template` to get the values, this should be aligned with the latest version. If you were trying to create a different version, you might need to check proper values for that version.

6. Create a patch for the cluster `App` resource to provide the newly created configuration. For this create a file `patch_config.yaml` with this content:

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
          priority: 55
    ```

7. Create the `kustomization.yaml`, referencing the template, and generating the ConfigMap out of `cluster_config.yaml`:

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

Now learn [how to create workload clusters]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters/" >}}) using these bases.
