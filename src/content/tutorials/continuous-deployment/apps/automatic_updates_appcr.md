---
linkTitle: Enable automatic updates in Apps
title: Enable automatic updates in Apps
description: Learn how to enable and configure automatic updates in Apps deployed using GitOps.
weight: 50
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-updates
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I enable and configure auto update for apps deployment with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-19
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "/overview/fleet-management/app-management/" >}}).

# Enable automatic updates for your app

Let's use `Flux` to automate the update of `App` resources. `Flux` will scan a remote repository and continuously update your deployed application version while also creating commits in your repository to reflect these changes.

Enabling automated updates requires a few additional `Flux` resources to be defined, namely:

- `ImageUpdateAutomation`, which defines the core update properties, like the `Git` repository where the commits are to be made, commit messages structure and how to update files in the repository,
- `ImageRepository` to configure where images are stored and new versions can be detected,
- `ImagePolicy` to configure which of the detected new versions should be used to update the `App` resource.
- Additionally, you have to edit your existing `App` manifest to include a comment that will be used to mark the field that should be updated with the new version.

`Flux` will watch for new docker image tags for your `App` and use them to update the `.spec.version` field in the `App` resource. It will do it by pushing commits to this repository.

__Note__: in order to use this mechanism you have to make sure the image tags of your `App` correspond to its version, otherwise this process will result in setting a meaningless version in the `.spec.version` field.

## Example

An example of an `App` automated update is available in the [gitops-template repository in `WC_NAME/apps/hello-world-automatic-updates`](https://github.com/giantswarm/gitops-template/tree/main/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME_OUT_OF_BAND_FLUX_APP/mapi/automatic-updates).

## Export environment variables

The management cluster, the organization, the workload cluster and the app names are needed during the process. The easiest way of providing them is by exporting them as environment variables:

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME=APP_NAME
export APP_IMAGE_REGISTRY=APP_IMAGE_REGISTRY
```

## Create Flux resources

First, create the `automatic-updates` directory:

```sh
cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi
mkdir automatic-updates
```

Later on, define the image update configuration in the `imageupdate.yaml` file on the new folder:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageUpdateAutomation
metadata:
  name: ${WC_NAME}-updates
  namespace: default
spec:
  interval: 1m0s
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

Now, in the app folder create the `imagerepository.yaml` file to configure registry to scan for new tags:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageRepository
metadata:
  name: ${APP_NAME}
  namespace: default
spec:
  image: ${APP_IMAGE_REGISTRY}
  interval: 1m0s
```

In the same app folder also create the `imagepolicy.yaml` file with tag selection rules:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
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
      range: '>=0.0.1'
```

__Note__: the `filterTags` allows you to filter the image tags before those are considered by the policy rule. Here, it's used to skip the heading `v` in the version upon passing it to the policy.

Check [`Flux` docs](https://fluxcd.io/docs/components/image/imagepolicies/#examples) for more examples of possible policies.

Lastly, add the new resources to the `kustomization.yaml` file:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
...
- ${APP_NAME}/imagepolicy.yaml
- ${APP_NAME}/imagerepository.yaml
```

## Mark the App resource

Open the `App` resource file and mark the field that should be updated with the new version. This is done by adding a comment with the `"$imagepolicy"` key and the `App` name and field name as values.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: hello-world
spec:
  ...
  version: 0.1.2 # {"$imagepolicy": "default:hello-world:tag"}
```

Now, the `Flux` will update the `App` resource with the new version of the image tag.

## Secrets for scanning private images (optional)

When the images are stored in a private registry, you need to provide the credentials to access them. You can do it by creating a `Kubernetes` secret with the registry credentials and referencing it in the `ImageRepository` resource.

In the management cluster secret folder (`management-clusters/${MC_NAME}/secrets`), create `Kubernetes` secret with registry credentials and save it into a file too:

```sh
export DOCKER_CONFIG_JSON=<path_to_docker_config_json>
kubectl create secret docker-registry \
  flux-pull-secrets \
  --namespace default \
  --from-file .dockerconfigjson=${DOCKER_CONFIG_JSON} \
  --dry-run=client \
  -o yaml > pullsecrets.enc.yaml
```

After, import the master `GPG` public key and encrypt the `Kubernetes` secret with it:

```sh
gpg --import management-clusters/${MC_NAME}/.sops.keys/.sops.master.asc
sops --encrypt --in-place pullsecrets.enc.yaml
```

Now, add in the `kustomization.yaml` the newly created secret as resource:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  ...
  pullsecrets.enc.yaml
```

Last step, you can create the `imagerepository.yaml` file referencing the newly created secret:

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageRepository
metadata:
  name: ${cluster_name}-hello-world
  namespace: org-${organization}
spec:
  ...
  secretRef:
    name: flux-pull-secrets
```

Now your secret is stored in the cluster and in the repository encrypted. `Flux` will use it to pull the images from the private registry thanks to the reference in the `ImageRepository` resource.

Learn more about [using private registries with `Flux`](https://fluxcd.io/docs/guides/image-update/#using-private-registries).
