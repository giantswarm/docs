---
linkTitle: Enable automatic updates for HelmRelease
title: Enable automatic updates for HelmRelease
description: Configure Flux to pull and apply new chart versions for a HelmRelease, either via a SemVer range on the OCIRepository or via image automation committing version bumps to Git.
weight: 50
menu:
  principal:
    identifier: tutorials-continuous-deployment-helm-releases-auto-updates
    parent: tutorials-continuous-deployment-helm-releases
user_questions:
  - How do I get Flux to update HelmRelease chart versions without manual work?
  - What's the difference between SemVer ranges and ImageUpdateAutomation for chart updates?
  - How do I commit chart version bumps to my Git repository?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2026-06-17
---

Flux can roll new chart versions for a HelmRelease without manual tag bumps. Two approaches:

1. **SemVer range on the `OCIRepository`** (recommended). Flux scans the OCI registry on its interval, picks the highest tag matching your range, and reconciles the HelmRelease. Nothing is committed back to Git: the chart selection is set by the `OCIRepository` resource alone.
2. **Image automation with Git commits.** Flux watches a registry for new tags, writes the selected tag back into your `ocirepository.yaml`, and commits the change. Adds an audit trail in Git at the cost of more moving parts.

The App CR equivalent of this guide is [Enable automatic updates in Apps]({{< relref "/tutorials/continuous-deployment/apps/automatic-updates-appcr" >}}).

## Pick up versions via OCIRepository range

Edit `ocirepository.yaml` and replace the `tag` field with a `semver` field that matches the versions you want Flux to pick up:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: my-app
  namespace: org-acmedev
spec:
  url: oci://gsoci.azurecr.io/charts/giantswarm/my-app
  ref:
    semver: ">=2.0.0 <3.0.0"   # was tag: "2.9.1"
  interval: 5m
```

On each reconciliation interval (`5m` above), Flux fetches the tag list from the registry, picks the highest version satisfying the range, and updates the OCIRepository's status. The HelmRelease detects the chart revision change and reconciles a Helm upgrade.

Common ranges:

- `">=2.0.0 <3.0.0"`: any minor or patch in the 2.x line. Rolls minors and patches as they ship.
- `"~2.9.0"`: patch updates only (2.9.x).
- `">=2.0.0"`: any version greater than or equal to 2.0.0, including 3.x.

Set the interval based on how fast you want updates to flow through, balanced against registry traffic. `1m` is fine for most cases. For quieter scanning, use `1h` or longer.

For more patterns, see the [OCIRepository SemVer example](https://fluxcd.io/flux/components/source/ocirepositories/#semver-example).

## Commit version bumps via image automation

If you want every chart version change committed to your Git repository (for audit, change review, or revert), use Flux's image automation with three resources: `ImageRepository`, `ImagePolicy`, and `ImageUpdateAutomation`.

### Export environment variables

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME=APP_NAME
export CHART_REGISTRY=gsoci.azurecr.io/charts/giantswarm/CHART_NAME
```

### Create the Flux automation resources

Create the `automatic-updates` directory if it doesn't exist:

```sh
cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi
mkdir -p automatic-updates
cd automatic-updates
```

Define the update automation in `imageupdate.yaml`. This resource watches your Git repository and pushes commits when policies match:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageUpdateAutomation
metadata:
  name: ${WC_NAME}-updates
  namespace: default
spec:
  interval: 1m
  sourceRef:
    kind: GitRepository
    name: YOUR_REPO
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        email: fluxcdbot@users.noreply.github.com
        name: fluxcdbot
      messageTemplate: '{{range .Updated.Images}}{{println .}}{{end}}'
    push:
      branch: main
  update:
    path: ./management-clusters/${MC_NAME}
    strategy: Setters
```

In the app folder, create `imagerepository.yaml` to register the chart's OCI source as a scanned repository:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: ${APP_NAME}
  namespace: default
spec:
  image: ${CHART_REGISTRY}
  interval: 1m
```

Create `imagepolicy.yaml` with tag selection rules:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: ${APP_NAME}
  namespace: flux-system
spec:
  imageRepositoryRef:
    name: ${APP_NAME}
  filterTags:
    extract: \$version
    pattern: ^v?(?P<version>.*)$
  policy:
    semver:
      range: ">=2.0.0 <3.0.0"
```

**Note**: `filterTags` strips an optional leading `v` so that `v2.10.0` and `2.10.0` both work against the policy. Adjust if your chart uses a different tag convention.

Add the new resources to `kustomization.yaml`:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  ...
  - ${APP_NAME}/imagepolicy.yaml
  - ${APP_NAME}/imagerepository.yaml
```

### Mark the OCIRepository tag

Edit `ocirepository.yaml` and add a setter comment to the `tag` field so ImageUpdateAutomation knows where to write new versions:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: ${APP_NAME}
  namespace: org-${ORG_NAME}
spec:
  url: oci://${CHART_REGISTRY}
  ref:
    tag: "2.9.1" # {"$imagepolicy": "default:${APP_NAME}:tag"}
  interval: 60m
```

When ImagePolicy selects a new version, ImageUpdateAutomation commits the new tag into `ocirepository.yaml` and Flux reconciles the HelmRelease.

### Private registries

If your chart registry requires authentication, create a Kubernetes Secret with registry credentials and reference it from `ImageRepository`.

In the management cluster secrets folder (`management-clusters/${MC_NAME}/secrets`), create the Secret:

```sh
export DOCKER_CONFIG_JSON=<path_to_docker_config_json>
kubectl create secret docker-registry \
  flux-pull-secrets \
  --namespace default \
  --from-file .dockerconfigjson=${DOCKER_CONFIG_JSON} \
  --dry-run=client \
  -o yaml > pullsecrets.enc.yaml
```

Encrypt with the management cluster's master `GPG` key:

```sh
gpg --import management-clusters/${MC_NAME}/.sops.keys/.sops.master.asc
sops --encrypt --in-place pullsecrets.enc.yaml
```

Add the encrypted Secret to `kustomization.yaml`:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  ...
  - pullsecrets.enc.yaml
```

Reference the Secret from `imagerepository.yaml`:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: ${APP_NAME}
  namespace: default
spec:
  image: ${CHART_REGISTRY}
  interval: 1m
  secretRef:
    name: flux-pull-secrets
```

For more, see [Using private registries with Flux](https://fluxcd.io/flux/guides/image-update/#using-private-registries).
