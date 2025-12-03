---
linkTitle: Deploy app via HelmRelease
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

Giant Swarm management clusters use Flux and Helm to deliver resources to clusters. To deploy workloads in workload clusters, the preferred method as of **TODO** is the use of Flux [HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/) resources in combination with Flux [OCIRespository](https://fluxcd.io/flux/components/source/ocirepositories/) resources as a source. For a general explanation on how the Giant Swarm app platform works, please check [our overview]({{< relref "/overview/fleet-management/app-management" >}}).

**Note:** While Giant Swarm supports other Flux sources, OCIRepository is the method by the recommended by Flux project and by Giant Swarm. This guide focuses on that method only.

## Prerequisites

- Access to a **Giant Swarm management cluster**
- Access to an **organization namespace** in the management cluster
- A **cluster** belonging to that same organization
- **Helm chart in an OCI repository**. Giant Swarm offers a variety of managed and unmanaged applications. In this guide we use the [hello-world](https://github.com/giantswarm/hello-world-app) application provided by Giant Swarm for testing purposes.
- **Configuration** for the chart, often referred to as `values.yaml` file
- the [Flux CLI](https://fluxcd.io/flux/cmd/) installed

**Note:** It is important that you use the correct minor version of the Flux CLI, to be compatible with the server side. When in doubt about the version used on the server side, please contact our support.

## Logical steps

To deploy an application, we follow this high-level plan:

1. Select the chart to deploy
2. Prepare configuration
3. Create OCIRepository
4. Create HelmRelease

The OCIRepository resource informs Flux about a chart in an [OCI](https://opencontainers.org/)-compliant registry. Based on how you configure the OCIRepository, Flux will decide which version (tag) of the chart to install, and whether it will automatically update the deployment once a new version (tag) of the chart appears in the registry.

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

Assuming that we want to deploy the most recent release, which is [v2.9.1](https://github.com/giantswarm/hello-world-app/releases/tag/v2.9.1) as of the writing of this guide, we can browse the repository content at tag `v2.9.1` and find its default configuration in the [`values.yaml`](https://github.com/giantswarm/hello-world-app/blob/v2.9.1/helm/hello-world/values.yaml) file inside the `helm/hello-world` folder.

We don't have to deal with most of the configuration options in this case, however in order to get the application fully working and see a little demo website deployed too our server, we have to adapt the host name in the ingress configuration. Based on our assumptions for this example case, we create a new `values.ymal` file like this:

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
- The `--tag` field to specify which exact version (OCI tag) to use. Watch out: OCI tags are not necessarily identical with git tags in the source repository. In fact, in our example, the git tag is `v2.9.1`, but the OCI tag is `2.9.1` without the `v` prefix. We recommend to use a CLI like [crane](https://michaelsauter.github.io/crane/) or a service like [oci.dag.dev](https://oci.dag.dev/?repo=gsoci.azurecr.io%2Fcharts%2Fgiantswarm%2Fhello-world) to verify which tags are actually available.
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
- `--namespace` is the same as above.
- `--chart-ref` is a reference to the OCIRepository resource we created in the previous step.
- `--values` points to the configuration file we prepared earlier.
- `--kubeconfig-secret-ref` is a reference to a kubeconfig as a Secret resource that Flux will use to deploy the chart in the workload cluster. This is always present in the owner organization's namespace and follows the naming convention `<clustername>-kubeconfig`.
- `--target-namespace` tells Helm in which namespace the chart's resources should be deployed, in the workload cluster.
- With `--create-target-namespace=true` we instruct Helm to create this namespace if it doesn't exist.
- The `--labels` flag adds a label to the created resource. We set the `giantswarm.io/cluster` label to the cluster name in order to be able to display all HelmRelease for a particular cluster in Giant Swarm user interfaces.
- The `--interval` serves the same purpose as explained above.

### Inspecting resource status

TODO

1. inspect OCIRepository status

```nohighlight
flux get sources oci --namespace org-acmedev dev01-hello-world
```

2. inspect HelmRelease status

```nohighlight
flux get helmreleases --namespace org-acmedev dev01-hello-world
```
