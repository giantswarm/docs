---
linkTitle: Update an existing HelmRelease
title: Update an existing HelmRelease
description: Update the chart version, configuration, or install behavior of a HelmRelease already deployed in a workload cluster via GitOps.
weight: 60
menu:
  principal:
    identifier: tutorials-continuous-deployment-helm-releases-updating
    parent: tutorials-continuous-deployment-helm-releases
user_questions:
  - How do I update a HelmRelease already deployed with GitOps?
  - How do I bump the chart version on a Flux HelmRelease?
  - How do I change values or secrets for an existing HelmRelease?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2026-06-17
---

To update an existing HelmRelease deployment you edit one or more of four files. The `OCIRepository` handles chart version changes. The `HelmRelease` handles install or upgrade behavior. The values `ConfigMap` and the encrypted Secret hold the chart values. Commit the change and Flux applies it on the next reconciliation.

For the App CR equivalent of this guide, see [Update an existing App]({{< relref "/tutorials/continuous-deployment/apps/update-appcr" >}}).

## Export environment variables

The management cluster, the organization, the workload cluster, and the resource name are needed throughout. Export them once:

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME=APP_NAME
cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}
```

## Bump the chart version

With HelmRelease, the chart source is a separate resource from the release itself. The chart version lives on the `OCIRepository`, not on the HelmRelease. To roll out a new chart version, edit `ocirepository.yaml` and change the tag:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: my-app
  namespace: org-acmedev
spec:
  url: oci://gsoci.azurecr.io/charts/giantswarm/my-app
  ref:
    tag: "2.10.0"   # was 2.9.1
  interval: 60m
```

Commit and push. Flux notices the tag change, pulls the new chart artifact, and the HelmRelease reconciles it onto the workload cluster.

**Note:** If you want Flux to roll patches and minor versions on its own without manual tag bumps, use a SemVer range instead of a pinned tag. That's covered in the upcoming automatic-updates guide. For now see the [OCIRepository SemVer example](https://fluxcd.io/flux/components/source/ocirepositories/#semver-example).

## Change install or upgrade behavior

To change how the chart is installed (target namespace, release name, install retries, upgrade policy, dependencies, drift detection mode), edit `helmrelease.yaml`. The full schema is in the [Flux HelmRelease reference](https://fluxcd.io/flux/components/helm/helmreleases/).

A few common edits:

```yaml
spec:
  install:
    remediation:
      retries: 3
  upgrade:
    remediation:
      retries: 3
    cleanupOnFail: true
  dependsOn:
    - name: cert-manager
      namespace: org-acmedev
```

Commit, push, reconcile.

## Change non-secret values

If the values your chart needs are in `configmap.yaml`, edit them directly and commit. Flux applies the updated `ConfigMap`, the HelmRelease detects the values change, and Helm performs an upgrade on the workload cluster.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-values
  namespace: org-acmedev
data:
  values.yaml: |
    image:
      tag: v1.2.4   # was v1.2.3
    replicaCount: 3
```

## Change secret values

For values stored in the `sops`-encrypted Secret, you have to decrypt, edit, then re-encrypt before committing.

Import the workload cluster's private `GPG` key. The exact command depends on where you store the key. If you keep it in 1Password:

```sh
eval $(op signin)
gpg --import \
<(op read "Dev Common/GPG private key (${MC_NAME}, ${WC_NAME}, Flux)/notesPlain")
```

Decrypt the Secret in place and pull the values out into a temporary file you can edit:

```sh
sops --decrypt --in-place secret.enc.yaml
yq eval .data.values secret.enc.yaml | base64 -d > values.tmp.yaml
```

Edit `values.tmp.yaml`, then encode the new contents back into the Secret's `data.values` field:

```sh
export NEW_USER_VALUES=$(cat values.tmp.yaml | base64)
yq -i eval ".data.values = \"${NEW_USER_VALUES}\"" secret.enc.yaml
```

Re-encrypt the file:

```sh
sops --encrypt --in-place secret.enc.yaml
```

It's a good practice to clear the imported private key from your keyring afterward:

```sh
gpg --delete-secret-keys "${KEY_FP}"
```

Commit `secret.enc.yaml` (and only the encrypted form). Flux applies the change and Helm picks up the new values on the next reconciliation.

## Force an immediate reconciliation

By default the HelmRelease and OCIRepository reconcile on their `--interval`. If you want to apply a change right away without waiting for the interval, trigger Flux from your local machine:

```sh
flux reconcile source oci --namespace org-${ORG_NAME} ${APP_NAME}
flux reconcile helmrelease --namespace org-${ORG_NAME} ${APP_NAME}
```

For background, see the [Flux reconcile documentation](https://fluxcd.io/flux/cmd/flux_reconcile/).
