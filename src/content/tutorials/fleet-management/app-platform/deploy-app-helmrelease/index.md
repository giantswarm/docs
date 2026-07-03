---
linkTitle: Deploy chart via HelmRelease
title: Deploying an application via a Flux HelmRelease
diataxis_content_type: how-to-guide
description: Full tutorial on deploying an application that is published as a Helm chart in an OCI registry to a workload cluster, via Flux OCIRepository and HelmRelease resources.
weight: 10
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-deployapp-helmrelease
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I deploy an app using a HelmRelease?
  - How does HelmRelease compare to the Giant Swarm App custom resource?
  - How do I deploy a chart from an OCI registry to a workload cluster?
last_review_date: 2026-06-17
---

**Note:** The CLI command [kubectl gs deploy chart]({{< relref "/reference/kubectl-gs/deploy-chart" >}}) simplifies deploying a chart as described on this page. We recommend looking into that CLI command first and coming back here if your use case isn't covered.

## Background

Flux HelmRelease is the recommended way to deploy applications on Giant Swarm. Every management cluster runs Flux, so there's nothing extra to install on the platform side. HelmRelease is the upstream Kubernetes API for declaring Helm releases.

To deploy workloads to workload clusters, Flux [HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/) resources work together with Flux [OCIRepository](https://fluxcd.io/flux/components/source/ocirepositories/) resources. If you have existing deployments using the Giant Swarm `App` custom resource, see [App Platform deprecation]({{< relref "/overview/fleet-management/app-management/app-platform-deprecation" >}}) for the migration path and the [legacy guide]({{< relref "/tutorials/fleet-management/app-platform/deploy-app" >}}) for documentation on that mechanism.

**Note:** While Giant Swarm supports other Flux sources, OCIRepository is the method recommended by the Flux project and by Giant Swarm. This guide focuses on that method only.

### How this compares to the App CR

| Feature | App CR | HelmRelease |
|---|---|---|
| API group | `application.giantswarm.io` (Giant Swarm-specific) | `helm.toolkit.fluxcd.io` (upstream Flux) |
| Chart source | `Catalog` + `AppCatalog` resources | `OCIRepository`, `HelmRepository`, `GitRepository`, `Bucket` |
| Automatic version updates | Requires Flux `ImageUpdateAutomation` on `.spec.version` | Native via a SemVer range on the source |
| Configuration | `config` + `userConfig` (Giant Swarm convention) | `values` + `valuesFrom` with explicit merge order |
| Cross-release ordering | Not modelled | `dependsOn` |
| Drift detection | App-operator reconciliation | Native Flux drift detection |
| Pause and resume | Annotation-based | `flux suspend` and `flux resume` |
| Post-render patches | Not supported | Native post-renderers (Kustomize) |

## Prerequisites

- Access to a **Giant Swarm management cluster**
- Access to an **organization namespace** in the management cluster
- A **cluster** belonging to that same organization
- **Helm chart in an OCI repository**. Giant Swarm offers a variety of managed and unmanaged applications. In this guide we use the [hello-world](https://github.com/giantswarm/hello-world-app) application provided by Giant Swarm for testing purposes.
- **Configuration** for the chart, often referred to as `values.yaml` file
- the [Flux CLI](https://fluxcd.io/flux/cmd/) installed

**Note:** It is important that you use the correct minor version of the Flux CLI, to be compatible with the server side. When in doubt about the version used on the server side, please visit your [developer portal]({{< relref "/overview/developer-portal" >}}) and open the page _Clusters_, then select the right management cluster, and then find the version number in the _Flux status_ panel. Alternatively, contact our support.

## Logical steps

To deploy an application, we follow this high-level plan:

1. Select the chart to deploy
2. Prepare configuration
3. Create OCIRepository
4. Create HelmRelease
5. Verify result

The OCIRepository resource informs Flux about a chart in an [OCI (Open Container Initiative)](https://opencontainers.org/)-compliant registry. Based on how you configure the OCIRepository, Flux decides which version (tag) of the chart to install. It also determines whether to automatically update the deployment once a new version (tag) of the chart appears in the registry.

The HelmRelease resource references the OCIRepository resource. It specifies the details on where to deploy the chart to.

## Example

For the following example we make a few assumptions:

- Our management cluster is named `hogweed`
- The management cluster's base ingress domain is `hogweed.gaws.gigantic.io`
- Our organization is called `acmedev`
- The cluster to deploy to is called `dev01`
- The chart to deploy is [hello-world](https://github.com/giantswarm/hello-world-app) by Giant Swarm

### Configuration

To determine what configuration values of our chart accepts, let's take a look at the source repository. Our application's source lives in the GitHub repository [giantswarm/hello-world](https://github.com/giantswarm/hello-world-app).

Assuming that we want to deploy the most recent release, which is [v3.0.2](https://github.com/giantswarm/hello-world-app/releases/tag/v3.0.2) as of the writing of this guide, and at the same time we want to have automatic upgrades for minor and patch versions, we use `v3.x.x`.

We don't have to deal with most of the configuration options in this case. However, to get the application fully working and see a little demo website deployed to our server, we need to expose it through the cluster's [Envoy Gateway]({{< relref "/tutorials/connectivity/gateway-api" >}}) using a Gateway API `HTTPRoute`. The chart's `route` block renders that `HTTPRoute` for us. Based on our assumptions for this example case, we create a new `values.yaml` file like this:

```yaml
ingress:
  enabled: false

route:
  enabled: true
  kind: HTTPRoute
  hostnames:
    - hello.dev01.hogweed.gaws.gigantic.io
  parentRefs:
    - name: giantswarm-default
      namespace: envoy-gateway-system
```

The chart defaults `ingress.enabled` to `true`, so we set it to `false` explicitly to avoid rendering both an `Ingress` and an `HTTPRoute` for the same service. The `parentRefs` entry points at `giantswarm-default` in `envoy-gateway-system`, the shared gateway provided by the [Gateway API bundle]({{< relref "/tutorials/connectivity/gateway-api/installation" >}}). If your cluster doesn't have that bundle installed yet, install it first, or point `parentRefs` at whichever gateway you use. For TLS on your hostname, see the [certificate management notes]({{< relref "/tutorials/connectivity/gateway-api/installation#certificate-management-with-cert-manager" >}}) in the Gateway API installation guide.

### Creating the OCIRepository resource

To create the Flux OCIRepository resource, we use the Flux CLI with the [`flux create source oci`](https://fluxcd.io/flux/cmd/flux_create_source_oci/) command.

Here is the command we'll use. Hold on, we'll explain the details next.

```nohighlight
flux create source oci dev01-hello-world \
    --url oci://gsoci.azurecr.io/charts/giantswarm/hello-world \
    --tag 3.x.x \
    --namespace org-acmedev \
    --interval 60m
```

About the argument and flags:

- By convention, we prefix the resource name with the cluster name and a dash: `dev01-hello-world`. The second part of the name should simply remind us what chart this is for.
- The `--url` flag is needed to specify URL of the chart repository in the registry. Giant Swarm's public registry has the domain `gsoci.azurecr.io`. Our charts have the namespace prefix `charts/giantswarm/`. The chart itself is named `hello-world`. And as a protocol prefix, `oci://` is required. This results in the URL `oci://gsoci.azurecr.io/charts/giantswarm/hello-world`.
- The `--tag` field specifies which exact version (OCI (Open Container Initiative) tag) to use. Watch out: OCI (Open Container Initiative) tags aren't necessarily identical to git tags in the source repository. In fact, in our example, the git tag is `v3.0.2`, but the OCI (Open Container Initiative) tag follows the format `X.Y.Z` without the `v` prefix. We recommend using a CLI like [crane](https://michaelsauter.github.io/crane/) or a service like [OCI.dag.dev](https://oci.dag.dev/?repo=gsoci.azurecr.io%2Fcharts%2Fgiantswarm%2Fhello-world) to verify which tags are available.
- We also set the `--namespace` flag to make sure the resource is created in the right namespace. `org-acmedev` is the namespace of the `acmedev` organisation and all resources related to its workload clusters are by convention placed in that namespace.
- Lastly, we add the `--interval` flag with a value of `60m`, so that Flux only checks for updates once per hour. By default, it would check every minute.

After executing this command, you should see status information like this:

```nohighlight
✔ OCIRepository created
◎ waiting for OCIRepository reconciliation
✔ OCIRepository dev01-hello-world is ready
```

So we are ready to continue with the next step.

### Creating the HelmRelease resource

For creating the HelmRelease resource, we again use the Flux CLI. This time we use the `flux create helmrelease` command. Again, we'll explain the details below the command.

```nohighlight
flux create helmrelease dev01-hello-world \
    --namespace org-acmedev \
    --chart-ref OCIRepository/dev01-hello-world \
    --values ./values.yaml \
    --kubeconfig-secret-ref dev01-kubeconfig \
    --target-namespace helloworld \
    --create-target-namespace=true \
    --label giantswarm.io/cluster=dev01 \
    --release-name dev01-hello-world \
    --interval 60m
```

- The name argument again should start with the cluster name and a dash, by convention, to keep resources belonging to the same workload cluster together.
- `--namespace` is the same as in the previous step.
- `--chart-ref` is a reference to the OCIRepository resource we created in the previous step.
- `--values` points to the configuration file we prepared earlier.
- `--kubeconfig-secret-ref` is a reference to a kubeconfig as a Secret resource that Flux will use to deploy the chart in the workload cluster. This is always present in the owner organization's namespace and follows the naming convention `<clustername>-kubeconfig`.
- `--target-namespace` tells Helm in which namespace the chart's resources should be deployed, in the workload cluster.
- With `--create-target-namespace=true` we instruct Helm to create this namespace if it doesn't exist.
- The `--label` flag adds a label to the created resource. We set the `giantswarm.io/cluster` label to the cluster name to display all HelmRelease for a particular cluster in Giant Swarm user interfaces.
- The `--release-name` flag sets the name of the Helm release to the same name as the Flux HelmRelease resource.
- The `--interval` serves the same purpose as in the previous step.

### Inspecting resource status

During the creation of our resource, the Flux CLI already gave some feedback. If you'd like to use separate commands which delivery up-to-date status information separate from the creation, we'll look at some ways here.

On the command line, we have the choice between using the `flux` CLI or `kubectl`.

#### Inspect OCIRepository status

We keep using the resource names from our example, for simplicity reasons.

```nohighlight
flux get sources oci \
    --namespace org-acmedev \
    dev01-hello-world

kubectl describe ocirepository \
    --namespace org-acmedev \
    dev01-hello-world
```

#### Inspect HelmRelease status

```nohighlight
flux get helmreleases \
    --namespace org-acmedev \
    dev01-hello-world

kubectl describe helmrelease \
    --namespace org-acmedev \
    helloworld-marian
```

### Cleaning up

Since we don't want you to keep a test application around, we cover the final cleanup here, too.

To remove the deployed application, you'll have to delete the HelmRelease and the OCIRepository created earlier, in reverse order. Here are the commands, using our example naming:

```nohighlight
flux delete helmrelease \
    --namespace org-acmedev \
    helloworld-marian

flux delete source oci \
    --namespace org-acmedev \
    helloworld-marian
```

## Git-driven workflow

To manage these resources from a Git repository instead of applying them directly, render the YAML with the `--export` flag. Both `flux create source oci` and `flux create helmrelease` print the resource manifest to standard output when given `--export`:

```nohighlight
flux create source oci dev01-hello-world \
    --url oci://gsoci.azurecr.io/charts/giantswarm/hello-world \
    --tag 3.x.x \
    --namespace org-acmedev \
    --interval 60m \
    --export > sources/dev01-hello-world.yaml

flux create helmrelease dev01-hello-world \
    --namespace org-acmedev \
    --chart-ref OCIRepository/dev01-hello-world \
    --values ./values.yaml \
    --kubeconfig-secret-ref dev01-kubeconfig \
    --target-namespace helloworld \
    --create-target-namespace=true \
    --label giantswarm.io/cluster=dev01 \
    --release-name dev01-hello-world \
    --interval 60m \
    --export > releases/dev01-hello-world.yaml
```

Commit both files to your Git repository. Once Flux reconciles your repository through a Kustomization or GitRepository source, the resources are applied. From then on, edits to the YAML in Git become the only way to change the deployment, and Flux reverts manual edits as drift.

For an end-to-end GitOps setup, see [FluxCD]({{< relref "/tutorials/continuous-deployment/flux" >}}) and the [continuous deployment tutorials]({{< relref "/tutorials/continuous-deployment/" >}}).

## Next steps

Now that you completed this guide, here are some suggestions for useful next things to pick up.

- Configure OCIRepository for **automatic updates**. In this guide we configured the OCIRepository to provide a pinned version of the chart, using the `--tag` CLI flag. Flux also supports specifying version ranges, so that Flux updates the deployed chart whenever a greater (in SemVer terms) version is found. Look for the `--tag-semver` flag in the [`flux create source oci` docs](https://fluxcd.io/flux/cmd/flux_create_source_oci/) and for the [SemVer example](https://fluxcd.io/flux/components/source/ocirepositories/#semver-example) in the OCIRepository API reference.
- You may need **secrets and credentials** in your chart configuration. Check the [`flux create helmrelease` docs](https://fluxcd.io/flux/cmd/flux_create_helmrelease/) and look for the `--values-from` example with a value starting with `Secret/`. This way, you can reference a Secret resource in the same namespace. This approach can be combined with passing non-secret values via `--values`, and with referencing `ConfigMap` resources via `--values-from`. The configuration is the merged combination of all sources.
