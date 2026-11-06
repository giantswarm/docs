---
linkTitle: Base templates
title: Creating a base template for your workload cluster
diataxis_content_type: how-to-guide
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
last_review_date: 2026-11-06
---

In Giant Swarm the interface to define a workload cluster is built on top of `Helm` and [Flux](https://fluxcd.io/flux/components/helm/helmreleases/). A Flux `HelmRelease` installs the release chart of your provider, for example `release-aws`, and an `OCIRepository` pulls that chart from `oci://gsoci.azurecr.io/charts/giantswarm/release-aws`. The chart version is the Giant Swarm release version. The `HelmRelease` contains the specification and configuration of the cluster in this format:

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: mycluster
  namespace: org-myorg
spec:
  chartRef:
    kind: OCIRepository
    name: mycluster
    namespace: org-myorg
  valuesFrom:
  - kind: ConfigMap
    name: mycluster-config
    valuesKey: values
  ...
```

So creating a cluster means delivering an `OCIRepository` and a configured `HelmRelease` to the platform API, also known as the management cluster API, where your cluster will run.

The release chart provides the defaults, and you layer your own values on top through the `HelmRelease` resource's `valuesFrom` list. Flux merges the entries in the order of the list, so a later entry overrides an earlier one. To learn how the `cluster-<provider>` chart chain produces the defaults, read [cluster configuration]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/cluster-configuration/" >}}).

If your bases still deploy clusters with an `App` resource, read [App Platform deprecation]({{< relref "/overview/fleet-management/app-management/app-platform-deprecation" >}}) to learn how to move them to a `HelmRelease`.

To avoid code duplication, the [bases and overlays](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#bases-and-overlays) pattern uses Kustomize to enhance the cluster configuration.

## Create a cluster template base {#create-template-base}

The shared cluster template base shouldn't serve as a standalone base for cluster creation, it's only abstracting the `OCIRepository` and `HelmRelease` resources common to all clusters versions. It's then used as a base for other bases, which provide an overlay with a specific configuration. That way you avoid code duplication across bases.

**Note**: This isn't a complete guide of how to create a perfect base, but a summary of the basic steps needed to move forward. Instructions here won't always be precise in telling you what to change. The right answer depends on the resources involved and how much of them you want to include in a base.

You can create bases for workload clusters easily thanks to the `kubectl gs` command:

```sh
kubectl gs gitops add base --provider capa
```

This command will create the folder structure and the specific folder for the provider `capa` (AWS flavour), including the template files in the `template` folder. `cluster.yaml` holds the `OCIRepository` and the `HelmRelease`, and `cluster_config.yaml` holds the cluster values that `kustomization.yaml` turns into the `${cluster_name}-config` ConfigMap. The structure would be:

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

The `kubectl-gs` base command for templating configuration only generates configuration for the most recent schema. If you configure a base for an older release, it's advised to check what's generated against the version-specific `values.yaml`.

In this example you create a custom version for AWS base:

1. Create a directory structure:

    ```nohighlight
    mkdir -p bases/clusters/capa/v36.1.1
    ```

2. Use the [kubectl gs template cluster]({{< relref "/reference/kubectl-gs/template-cluster" >}}) to template cluster resources, see an example for the `capa` provider below. Use arbitrary values for the mandatory fields, we will configure them later in our process. Set `--release` to a release that's published as a `release-aws` chart, so the values match the release chart and leave out the release version. The command renders a `ConfigMap` with the cluster values, an `OCIRepository` and a `HelmRelease`. Keep only the values of the `ConfigMap` in a new `cluster_config.yaml` file in your version folder:

    ```nohighlight
    kubectl gs template cluster \
    --name mywcl \
    --organization myorg \
    --release 36.1.1 \
    --provider capa \
    | yq 'select(.kind == "ConfigMap") | .data.values' > bases/clusters/capa/v36.1.1/cluster_config.yaml
    ```

3. Check the content of the file. It looks like this:

    ```nohighlight
    global:
      connectivity:
        availabilityZoneUsageLimit: 3
        network: {}
        topology: {}
      controlPlane: {}
      metadata:
        name: mywcl
        organization: myorg
        preventDeletion: false
        servicePriority: highest
      nodePools:
        nodepool0:
          instanceType: m5.xlarge
          maxSize: 10
          minSize: 3
          rootVolumeSizeGB: 8
      providerSpecific: {}
    ```

4. Replace `mywcl`, `myorg` values from the previous step with variables. The single quotes keep your shell from expanding the variables, as Flux substitutes them later:

    ```nohighlight
    sed -i 's/myorg/${organization}/g' bases/clusters/capa/v36.1.1/cluster_config.yaml
    sed -i 's/mywcl/${cluster_name}/g' bases/clusters/capa/v36.1.1/cluster_config.yaml
    ```

    Note that on macOS, `sed -i` needs an empty suffix argument: `sed -i '' 's/myorg/${organization}/g' ...`.

5. Check `cluster_config.yaml` against the version-specific `values.yaml`, and tweak it if necessary to match the expected schema. At this point you may also provide extra configuration, like additional availability zones, node pools, etc. If you used `kubectl gs template` to get the values, this should be aligned with the latest version. If you were trying to create a different version, you might need to check proper values for that version.

6. Create a patch for the cluster `HelmRelease` resource to provide the newly created configuration. For this create a file `patch_config.yaml` with this content:

    ```nohighlight
    - op: add
      path: /spec/valuesFrom/-
      value:
        kind: ConfigMap
        name: ${cluster_name}-version-config
        valuesKey: values
    ```

    This JSON 6902 patch appends the ConfigMap to the end of `valuesFrom`, so its values override the values of the template. Note that a merge patch would replace the whole `valuesFrom` list instead.

7. Create the `kustomization.yaml`, referencing the template, and generating the ConfigMap out of `cluster_config.yaml`:

    ```nohighlight
    apiVersion: kustomize.config.k8s.io/v1beta1
    configMapGenerator:
      - files:
        - values=cluster_config.yaml
        name: ${cluster_name}-version-config
        namespace: org-${organization}
    generatorOptions:
      disableNameSuffixHash: true
    kind: Kustomization
    patches:
      - path: patch_config.yaml
        target:
          group: helm.toolkit.fluxcd.io
          kind: HelmRelease
          name: \$\{cluster_name\}
    resources:
      - ../template
    ```

    The ConfigMap gets its own name, because the template already generates `${cluster_name}-config`. The patch target name is a regular expression, so it escapes the `${cluster_name}` variable that Flux substitutes later.

Now learn [how to create workload clusters]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters/" >}}) using these bases.
