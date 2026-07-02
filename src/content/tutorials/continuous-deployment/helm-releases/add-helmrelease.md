---
linkTitle: Add a HelmRelease to a workload cluster
title: Add a HelmRelease to a workload cluster
diataxis_content_type: how-to-guide
description: Deploy and configure an application into a workload cluster using a Flux HelmRelease and OCIRepository, managed through GitOps.
weight: 90
menu:
  principal:
    identifier: tutorials-continuous-deployment-helm-releases-wc
    parent: tutorials-continuous-deployment-helm-releases
user_questions:
  - How can I add a HelmRelease to a workload cluster with GitOps?
  - How do I structure a Flux HelmRelease in the Giant Swarm GitOps template?
  - How do I pass values to a HelmRelease via ConfigMap or Secret?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2026-06-17
---

This guide shows how to deploy an application to a workload cluster using a Flux `HelmRelease` and `OCIRepository`, managed through GitOps. For the conceptual overview, see [App management]({{< relref "/overview/fleet-management/app-management" >}}). For an imperative version that applies resources directly to the cluster, see [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}).

If you have existing GitOps deployments using Giant Swarm `App` custom resources, the equivalent guide is [Add a new App to a workload cluster]({{< relref "/tutorials/continuous-deployment/apps/add-appcr" >}}). Flux HelmRelease is the recommended path for new deployments.

## Common steps

### Export environment variables

The management cluster, the organization, the workload cluster, and the resource name are needed throughout. Export them once:

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME="${WC_NAME}-APP_NAME"
```

### Set up the directory structure

Create a new directory in the apps directory of your workload cluster, named after the HelmRelease:

```sh
cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps
mkdir ${APP_NAME}
cd ${APP_NAME}
```

## Render the OCIRepository and HelmRelease

Set the chart variables:

```sh
export CHART_URL=oci://gsoci.azurecr.io/charts/giantswarm/CHART_NAME
export CHART_VERSION=CHART_VERSION
export APP_NAMESPACE=APP_NAMESPACE
```

Render the OCIRepository manifest with `--export` so it lands as YAML in your repository:

```sh
flux create source oci ${APP_NAME} \
  --url ${CHART_URL} \
  --tag ${CHART_VERSION} \
  --namespace org-${ORG_NAME} \
  --interval 60m \
  --export > ocirepository.yaml
```

Render the HelmRelease manifest:

```sh
flux create helmrelease ${APP_NAME} \
  --namespace org-${ORG_NAME} \
  --chart-ref OCIRepository/${APP_NAME} \
  --kubeconfig-secret-ref ${WC_NAME}-kubeconfig \
  --target-namespace ${APP_NAMESPACE} \
  --label giantswarm.io/cluster=${WC_NAME} \
  --release-name ${APP_NAME} \
  --interval 60m \
  --export > helmrelease.yaml
```

The `--kubeconfig-secret-ref` flag tells Flux to install the chart into the workload cluster (not the management cluster). The Secret follows the `<cluster>-kubeconfig` naming convention and is created for you alongside the cluster.

**Note**: Including `${WC_NAME}` in the resource name avoids collisions between clusters running the same chart inside the same organization.

## Add configuration

Most charts need configuration values. Pass them through the HelmRelease using a `ConfigMap` (for non-secret values) and a `Secret` (for credentials).

### Non-secret values

Create `configmap.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ${APP_NAME}-values
  namespace: org-${ORG_NAME}
data:
  values.yaml: |
    # Your chart values here
    image:
      tag: v1.2.3
```

Reference it in `helmrelease.yaml` by adding a `valuesFrom` entry:

```yaml
spec:
  valuesFrom:
    - kind: ConfigMap
      name: ${APP_NAME}-values
```

### Encrypted secrets

For credentials and other sensitive values, create `secret.enc.yaml`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ${APP_NAME}-secret
  namespace: org-${ORG_NAME}
stringData:
  values.yaml: |
    database:
      password: changeme
```

Encrypt it with `sops` using the workload cluster's `GPG` key before committing:

```sh
gpg --import management-clusters/${MC_NAME}/.sops.keys/.sops.${WC_NAME}.asc
sops --encrypt --in-place secret.enc.yaml
```

For more on secrets encrypted with `sops` in GitOps, see [the gitops-template docs](https://github.com/giantswarm/gitops-template/blob/main/docs/add_mc.md#flux-gpg-master-key-pair).

Add the Secret to `helmrelease.yaml` next to the `ConfigMap` entry:

```yaml
spec:
  valuesFrom:
    - kind: ConfigMap
      name: ${APP_NAME}-values
    - kind: Secret
      name: ${APP_NAME}-secret
```

Flux merges the entries in order, with later ones overriding earlier ones. See [the Flux HelmRelease values reference](https://fluxcd.io/flux/components/helm/helmreleases/#values) for the full semantics.

## Wire up Kustomization

Edit `kustomization.yaml` in the apps folder to include the new files:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  ...
  - ${APP_NAME}/ocirepository.yaml
  - ${APP_NAME}/helmrelease.yaml
  - ${APP_NAME}/configmap.yaml
  - ${APP_NAME}/secret.enc.yaml
```

If you've completed [the workload cluster configuration guide]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters" >}}), all the Flux resources needed to reconcile this directory are already in place. Commit the changes and Flux applies them on its next reconciliation.

## Next steps

Once the HelmRelease is reconciled, common follow-ups are updating its version or values, and letting Flux pick up new chart versions via a SemVer range on the OCIRepository. Companion guides for those workflows are coming as part of the HelmRelease migration. For now, see the [Flux HelmRelease documentation](https://fluxcd.io/flux/components/helm/helmreleases/) for the full API and patterns.

For the App CR equivalent of this guide, see [Add a new App to a workload cluster]({{< relref "/tutorials/continuous-deployment/apps/add-appcr" >}}).
