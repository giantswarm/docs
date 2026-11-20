---
linkTitle: update cluster
title: "'kubectl gs update cluster' command reference (cluster upgrades)"
diataxis_content_type: reference
description: Reference documentation on how to upgrade a workload cluster using kubectl-gs.
weight: 130
menu:
  principal:
    parent: reference-kubectlgs
    identifier: reference-kubectlgs-updatecluster
last_review_date: 2026-11-19
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I upgrade a workload cluster from the command line?
  - How can I schedule a workload cluster upgrade from the command line?
  - How can I upgrade a workload cluster deployed as a HelmRelease?
aliases:
  - /vintage/use-the-api/kubectl-gs/update-cluster/
---

This command's purpose is to modify details of a workload cluster. Currently it allows to upgrade a workload cluster to a newer [release]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/releases" >}}).

## Usage

### Upgrading a workload cluster {#cluster-upgrade}

**Note:** This feature is currently only working when the cluster configuration is **not stored** via GitOps.

Upgrades can either be triggered immediately, or the upgrade can be scheduled to happen at a specific date and time.

The following example shows how to upgrade a workload cluster to the release specified via the `--release-version` flag.

```nohighlight
kubectl gs update cluster \
  --provider capa \
  --namespace org-acme \
  --name a1b2c \
  --release-version 26.2.0
```

To schedule a workload cluster upgrade in the future, the `--scheduled-time` flag is used, like in the example below:

```nohighlight
kubectl gs update cluster \
  --provider capa \
  --name a1b2c \
  --namespace org-acme \
  --release-version 29.0.0 \
  --scheduled-time "2024-08-28 12:10"
```

This adds annotations to the cluster resource, triggering the upgrade to the specified version at the scheduled time.

### What the command changes {#what-changes}

What the command changes depends on how the cluster is deployed:

- **HelmRelease of a `release-<provider>` chart**, such as `release-aws`: the command sets the `spec.ref.tag` of the `OCIRepository` the `HelmRelease` takes its chart from. The release chart's version is the release version, and the chart sets `global.release.version` itself, so the command leaves the values alone. This needs kubectl-gs v7.0.0 or newer.
- **HelmRelease of a `cluster-<provider>` chart**, such as `cluster-aws`, or an **`App` resource**: the command sets `global.release.version` in the `<cluster-name>-userconfig` ConfigMap. The chart version stays as it is, so you manage it yourself.

For a `release-<provider>` chart, the command refuses the upgrade in these cases:

- `--scheduled-time` is set. Nothing applies a scheduled tag change, so run the command at the time you want the upgrade to happen instead.
- Flux applies the `OCIRepository`, for example through a `Kustomization`. Change the tag in the source Flux applies instead, as Flux would revert the change.
- The `OCIRepository` sets `spec.ref.semver` or `spec.ref.digest`. Flux follows these over the tag, so change `spec.ref` yourself.
- Another `HelmRelease` takes its chart from the same `OCIRepository`, so changing the tag would upgrade it too. Give the cluster's `HelmRelease` an `OCIRepository` of its own.
- The `HelmRelease` values set `global.release.version`, in `spec.values`, in a ConfigMap of `spec.valuesFrom`, or through a `valuesFrom` `targetPath`. Those values override the release chart's, so remove them first.

When Flux applies the `<cluster-name>-userconfig` ConfigMap, the command refuses the upgrade for the same reason. Upgrade such a cluster in your GitOps repository, as described in [Cluster upgrades]({{< relref "/tutorials/fleet-management/cluster-management/cluster-upgrades" >}}).

## Flags

- `--provider` - The infrastructure provider of the installation, `capa`, `capz`, `vsphere`, or `cloud-director`.
- `--name` - Name of the cluster.
- `--namespace` - Namespace of the cluster resource.
- `--release-version` - Version of the release the cluster should be upgraded to.
- `--scheduled-time` (optional): Scheduled time when the cluster should be updated, in the format `YYYY-MM-DD HH:MM`. Timezone UTC is assumed. If not given, the upgrade happens as soon as possible. Not supported for clusters deployed as a `HelmRelease` of a `release-<provider>` chart.

## Related

- [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
- [`cluster-upgrades`]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/cluster-upgrades" >}}) - Cluster upgrades.
