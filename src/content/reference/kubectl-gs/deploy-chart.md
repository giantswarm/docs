---
linkTitle: deploy chart
title: "'kubectl gs deploy chart' command reference"
description: Reference documentation on how to deploy a Helm chart using 'kubectl gs'.
weight: 15
menu:
  principal:
    parent: reference-kubectlgs
last_review_date: 2026-03-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I deploy a Helm chart using kubectl gs?
---

The `deploy chart` command allows to deploy a Helm chart in a Giant Swarm workload or management cluster.

The command makes two key assumptions:

1. Your current kubectl context is the Giant Swarm management cluster of the installation to deploy to (regardless whether you deploy to a workload cluster or the management cluster).
2. You use an OCI registry as the source of the chart.

It creates Flux OCIRepository and HelmRelease resources. If access credentials are needed for the registry, it also creates a Secret.

If the chart provides a values schema, the command can validate the provided configuration.

## Usage

The command to execute is `kubectl gs deploy chart`.

It requires the following flags:

- `--chart-name` - Name of the chart (OCI repository) to deploy.
- `--organization` - Giant Swarm organization name owning the target cluster.
- `--management-cluster` - Deploy to the management cluster itself. Cluster name is derived from the current kubectl context.
- `--target-cluster` - Name of the target workload cluster.
- `--target-namespace` - Target namespace in the workload cluster.

These flags are optional:

- `--auto-upgrade` - Auto-upgrade strategy (one of: `all`, `minor`, `patch`).
- `--dry-run` - Perform server-side validation and configuration validation against schema without applying. Prints manifests to stdout.
- `--interval` - Reconciliation interval for OCIRepository and HelmRelease (default: `10m`).
- `--name` - Override the resource name (default: `<cluster>-<chart-name>`).
- `--oci-url-prefix` - OCI URL prefix for the chart registry (default: `oci://gsoci.azurecr.io/charts/giantswarm/`).
- `--registry-provider` - Cloud provider for registry authentication via workload identity (one of: `aws`, `azure`, `gcp`). When set, no registry Secret is created.
- `--registry-username` - Username for private OCI registry authentication. Password is read from `KUBECTL_GS_REGISTRY_PASSWORD` or prompted interactively.
- `--values-file` - Path to a YAML file with chart values.
- `--values-from` - Reference to a ConfigMap or Secret containing chart values (format: `ConfigMap/name` or `Secret/name`). Can be specified multiple times.
- `--version` - Chart version to deploy. If not specified, the latest version found in the registry is used.

## Output

The command prints the latest version found and reports once resources are created. Example:

```
Resolved latest version: 0.2.11
Applied Secret org-marian/mg23c-mychart-registry
Applied OCIRepository org-marian/mg23c-mychart
Applied HelmRelease org-marian/mg23c-mychart
```

With the `--dry-run` flag set, the command will print the manifest to STDOUT instead of creating resources. Progress output is written to STDERR.

## Configuration

Using the `--values-file` with a YAML file path as value, you can pass configuration values for the deployed chart to the command. These values will be stored as part of the HelmRelease resource, in the so-called [inline values](https://fluxcd.io/flux/components/helm/helmreleases/#inline-values).

In addition, you can pre-create ConfigMap and Secret resources in the same namespace that you will be using with this command (your organization namespace) and reference these using the `--values-from` flag. You can reference any number of these resources, simply by specifying the flag as often as needed. Note the specific syntax for this flag's value. Take a look at the [example below](#ex-cm-secret).

### Validation

If the command knows the values schema of the chart to deploy, it will use it to validate the configuration set via `--values-file`.

**Note**: Values in ConfigMap and Secret resources referenced via `--values-from` are not validated by the command.

To find the values schema for the chart, the command looks for the annotation `io.giantswarm.application.values-schema` in the chart's OCI repository manifest, specifically for the tag specified via the `--version` flag (or the latest, if not given). The command expects to find an HTTP(s) URL pointing to the schema.

For example, the chart `oci://gsoci.azurecr.io/charts/giantswarm/hello-world:3.0.0` has this annotation:

```nohighlight
"io.giantswarm.application.values-schema": "https://raw.githubusercontent.com/giantswarm/hello-world-app/refs/tags/v3.0.0/helm/hello-world/values.schema.json"
```

For charts that don't provide this annotation, the validation is skipped.

## Examples

### Deploy a chart with a specific version

```nohighlight
kubectl gs deploy chart \
  --chart-name hello-world \
  --version 1.2.3 \
  --organization acme \
  --target-cluster mycluster01 \
  --target-namespace hello
```

**Note:** If the `--version` flag is omitted, the latest version will be found and deployed. "Latest" here means the highest version number in the [Semantic Versioning](https://semver.org/) sense.

### Deploy a chart from a custom registry

```nohighlight
kubectl gs deploy chart \
  --oci-url-prefix oci://example.com/charts/ \
  --chart-name my-chart \
  ...
```

### Deploy with auto-upgrade on patch versions

```nohighlight
kubectl gs deploy chart \
  --chart-name hello-world \
  --version 3.0.0 \
  --auto-upgrade patch \
  ...
```

The result is an OCIRepository resource that automatically matches 3.0.1, 3.0.2, and so on, but not 3.1.0 or higher.

### Deploy with custom values

```nohighlight
kubectl gs deploy chart \
  --chart-name hello-world \
  --organization acme \
  --target-cluster mycluster01 \
  --target-namespace hello \
  --values-file hello-values.yaml
```

### Server-side dry-run (validate without applying)

```nohighlight
kubectl gs deploy chart \
  --chart-name hello-world \
  --organization acme \
  --target-cluster mycluster01 \
  --target-namespace hello \
  --dry-run
```

### Deploy with values from a ConfigMap and a Secret {#ex-cm-secret}

```nohighlight
kubectl gs deploy chart \
  --chart-name hello-world \
  --organization acme \
  --target-cluster mycluster01 \
  --target-namespace hello \
  --values-from ConfigMap/my-config \
  --values-from Secret/my-secret
```

### Deploy to the management cluster itself

```nohighlight
kubectl gs deploy chart \
  --chart-name hello-world \
  --organization acme \
  --target-namespace hello \
  --management-cluster
```

## Related

- [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
