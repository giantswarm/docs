---
linkTitle: Deploy chart via HelmRelease
title: Deploying an application via a Flux HelmRelease
description: Full tutorial on deploying an application that is published as a Helm chart in an OCI registry to a workload cluster, via Flux OCIRepository and HelmRelease resources.
weight: 21
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-deployapp-helmrelease
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I deploy an app using a HelmRelease?
last_review_date: 2025-12-03
---

## Background

Giant Swarm management clusters use Flux and Helm to deliver resources to clusters. This may be used as an alternative to [App resources]({{< relref "/tutorials/fleet-management/app-platform/deploy-app" >}}) for more advanced control.

To deploy workloads in workload clusters, Flux [HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/) resources can be used in combination with Flux [OCIRespository](https://fluxcd.io/flux/components/source/ocirepositories/) resources.

**Note:** While Giant Swarm supports other Flux sources, OCIRepository is the method recommended by the Flux project and by Giant Swarm. This guide focuses on that method only.

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

Assuming that we want to deploy the most recent release, which is [v2.9.1](https://github.com/giantswarm/hello-world-app/releases/tag/v2.9.1) as of the writing of this guide, we can browse the repository content at tag `v2.9.1`. We find its default configuration in the [`values.yaml`](https://github.com/giantswarm/hello-world-app/blob/v2.9.1/helm/hello-world/values.yaml) file inside the `helm/hello-world` folder.

We don't have to deal with most of the configuration options in this case. However, to get the application fully working and see a little demo website deployed to our server, we have to adapt the host name in the ingress configuration. Based on our assumptions for this example case, we create a new `values.yaml` file like this:

```yaml
ingress:
  hosts:
    - host: hello.dev01.hogweed.gaws.gigantic.io
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: hello-world-tls
      hosts:
        - hello.dev01.hogweed.gaws.gigantic.io
```

### Creating the OCIRepository resource

To create the Flux OCIRepository resource, we use the Flux CLI with the [`flux create source oci`](https://fluxcd.io/flux/cmd/flux_create_source_oci/) command.

Here is the command we'll use. Hold on, we'll explain the details next.

```nohighlight
flux create source oci dev01-hello-world \
    --url oci://gsoci.azurecr.io/charts/giantswarm/hello-world \
    --tag 2.9.1 \
    --namespace org-acmedev \
    --interval 60m
```

About the argument and flags:

- By convention, we prefix the resource name with the cluster name and a dash: `dev01-hello-world`. The second part of the name should simply remind us what chart this is for.
- The `--url` flag is needed to specify URL of the chart repository in the registry. Giant Swarm's public registry has the domain `gsoci.azurecr.io`. Our charts have the namespace prefix `charts/giantswarm/`. The chart itself is named `hello-world`. And as a protocol prefix, `oci://` is required. This results in the URL `oci://gsoci.azurecr.io/charts/giantswarm/hello-world`.
- The `--tag` field specifies which exact version (OCI (Open Container Initiative) tag) to use. Watch out: OCI (Open Container Initiative) tags are not necessarily identical with git tags in the source repository. In fact, in our example, the git tag is `v2.9.1`, but the OCI (Open Container Initiative) tag is `2.9.1` without the `v` prefix. We recommend using a CLI like [crane](https://michaelsauter.github.io/crane/) or a service like [OCI.dag.dev](https://oci.dag.dev/?repo=gsoci.azurecr.io%2Fcharts%2Fgiantswarm%2Fhello-world) to verify which tags are available.
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
    --labels giantswarm.io/cluster=dev01 \
    --interval 60m
```

- The name argument again should start with the cluster name and a dash, by convention, to keep resources belonging to the same workload cluster together.
- `--namespace` is the same as in the previous step.
- `--chart-ref` is a reference to the OCIRepository resource we created in the previous step.
- `--values` points to the configuration file we prepared earlier.
- `--kubeconfig-secret-ref` is a reference to a kubeconfig as a Secret resource that Flux will use to deploy the chart in the workload cluster. This is always present in the owner organization's namespace and follows the naming convention `<clustername>-kubeconfig`.
- `--target-namespace` tells Helm in which namespace the chart's resources should be deployed, in the workload cluster.
- With `--create-target-namespace=true` we instruct Helm to create this namespace if it doesn't exist.
- The `--labels` flag adds a label to the created resource. We set the `giantswarm.io/cluster` label to the cluster name to display all HelmRelease for a particular cluster in Giant Swarm user interfaces.
- The `--interval` serves the same purpose as in the previous step.

### Inspecting resource status

During the creation of our resource, the Flux CLI already gave some feedback. If you'd like to use separate commands which delivery up-to-date status information separate from the creation, we'll look at some ways here.

On the command line, we have the choice between using the `flux` CLI or `kubectl`.

**Inspect OCIRepository status**

We keep using the resource names from our example, for simplicity reasons.

```nohighlight
flux get sources oci \
    --namespace org-acmedev \
    dev01-hello-world

kubectl describe ocirepository \
    --namespace org-acmedev \
    dev01-hello-world
```

**Inspect HelmRelease status**

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

## Next steps

Now that you completed this guide, here are some suggestion for useful next things to pick up.

- Configure OCIRepository for **automatic updates**. In this guide we configured the OCIRepository to provide a pinned version of the chart, using the `--tag` CLI flag. However, Flux also supports specifying version ranges, so that Flux will update the deployed chart whenever a greater (in SemVer terms) version is found. Look for the `--tag-semver` flag in the [flux create source oci](https://fluxcd.io/flux/cmd/flux_create_source_oci/) docs and for the [SemVer example](https://fluxcd.io/flux/components/source/ocirepositories/#semver-example) in the OCIRepository API reference.
- Deploying a chart via a HelmRelease using **GitOps**. Both `flux create ...` commands used above support YAML output as an alternative to directly applying the resource. Simply add the `--export` flag.
