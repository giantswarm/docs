---
linkTitle: Enable automatic updates in Apps
title: Enable automatic updates in Apps
description: Learn how to enable and configure automatic updates in Apps deployed using GitOps.
weight: 50
menu:
  main:
    identifier: advanced-gitops-apps-automatic-update
    parent: advanced-gitops-apps
last_review_date: 2023-02-10
user_questions:
  - How can I enable and configure auto update for apps deployment with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

This document is part of the documentation to use GitOps with Giant Swarm App Platform. You can find more information about the [App Platform in our docs](/platform-overview/app-platform/).

# Enable automatic updates of an existing App

Follow the below instructions to instruct Flux on how to automatically update an existing App. Automatic update means Flux will scan a remote repository and automatically update your deployed application version while also creating commits in your repository to reflect these changes.

Configuring automated version updates requires a few additional Flux API objects to be defined, namely:

- `ImageUpdateAutomation`, which defines the core update properties, like the git repo where the commits are to be made, commit messages structure and how to update files in the repository,
- `ImageRepository` to configure where images are stored and new versions can be detected,
- `ImagePolicy` to configure which of the detected new tags will be considered as possible to update to.
- Additionally, you have to edit your existing App manifest to include a marker showing the manifest's property you want to have auto updated by Flux (usually App version property).

Flux will watch for new Docker image tags for your App and use them to update the `.spec.version` field in the App CR. It will do it by pushing commits to this repository.

__Note__: in order to use this mechanism you have to make sure that the image tags of your App correspond to its version, otherwise this process will result in setting a meaningless version in the `.spec.version` field.

## Example

An example of an App automated update is available in the [gitops-template repository in "WC_NAME/apps/hello-world-automatic-updates"](https://github.com/giantswarm/gitops-template/tree/main/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/mapi/apps/hello-world-automatic-updates/).

## Export environment variables

__Note__: Management Cluster codename, Organization name, Workload Cluster name and some App-related values are needed in multiple places across this instruction, the least error prone way of providing them is by exporting them as environment variables:

```nohighlight
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME=APP_NAME
export APP_IMAGE_REGISTRY=APP_IMAGE_REGISTRY
```

## Directory tree

1. Go to the Workload Cluster directory:

    ```nohighlight
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi
    ```

2. Create the `automatic-updates` directory there and enter it:

    ```nohighlight
    mkdir automatic-updates
    cd automatic-updates
    ```

3. Create the `imageupdate.yaml` file that defines an automation process for updating Git repository:

    ```nohighlight
    cat <<EOF > imageupdate.yaml
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
    EOF
    ```

4. Leave `automatic-updates` directory and go into the App directory:

    ```nohighlight
    cd ../apps/${APP_NAME}
    ```

5. Create the [ImageRepository CR](https://fluxcd.io/docs/components/image/imagerepositories/) to configure registry to
scan for new tags:

    ```nohighlight
    cat <<EOF > imagerepository.yaml
    apiVersion: image.toolkit.fluxcd.io/v1beta1
    kind: ImageRepository
    metadata:
      name: ${APP_NAME}
      namespace: default
    spec:
      image: ${APP_IMAGE_REGISTRY}
      interval: 1m0s
    EOF
    ```

6. Create the [ImagePolicy CR](https://fluxcd.io/docs/components/image/imagepolicies/) with rules for tags selection:

    ```nohighlight
    cat <<EOF > imagepolicy.yaml
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
    EOF
    ```

    __Note__: the `filterTags` is processed first and gives the opportunity to filter the image tags before they are considered by the policy rule. Here, it is used to skip the heading `v` in the version upon passing it to the policy.

    Check [Flux docs](https://fluxcd.io/docs/components/image/imagepolicies/#examples) for more examples of possible policies.

7. Go back to the `apps` directory:

    ```nohighlight
    cd ..
    ```

8. Edit the `kustomization.yaml` file listing newly created files:

    ```nohighlight
    yq -i eval ".resources += [\"${APP_NAME}/imagepolicy.yaml\",\"${APP_NAME}/imagerepository.yaml\"] | .resources style=\"\"" kustomization.yaml
    ```

    The resultant file should looks similar to this:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    resources:
    - ${APP_NAME}/imagepolicy.yaml
    - ${APP_NAME}/imagerepository.yaml
    ```

9. Edit the `kustomization.yaml` file again, and add a patch for placing Flux' resources in the default namespace or one of your organization namespaces:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    patches:
    - patch: |-
      - op: replace
        path: "/metadata/namespace"
        value: default
    target:
      kind: 'ImagePolicy|ImageRepository'
    ```

## App CR version field mark

1. Go to the App directory:

    ```nohighlight
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}
    ```

2. Mark the `.spec.version` field for update in the App CR:

    ```nohighlight
    sed -i "s/version:.*$/& # {\"\$imagepolicy\": \"default:${APP_NAME}:tag\"}/" appcr.yaml
    ```

   The resultant file should looks similar to this:

   ```yaml
   piVersion: application.giantswarm.io/v1alpha1
   kind: App
   metadata:
     name: hello-world
   spec:
     version: 0.1.2 # {"$imagepolicy": "default:hello-world:tag"}
   ```

## Secrets for scanning private images (optional)

1. Export path to the Docker registry config with secrets:

    ```nohighlight
    export DOCKER_CONFIG_JSON=PATH
    ```

2. Go to the Management Cluster secrets directory:

    ```nohighlight
    cd management-clusters/${MC_NAME}/secrets
    ```

3. Create Kubernetes Secret with Docker Registry credentials and save it into a file:

    ```nohighlight
    kubectl create secret docker-registry \
    flux-pull-secrets \
    --namespace default \
    --from-file .dockerconfigjson=${DOCKER_CONFIG_JSON} \
    --dry-run=client \
    -o yaml > pullsecrets.enc.yaml
    ```

4. Import the master GPG public key and encrypt the Kubernetes Secret with it:

    ```nohighlight
    gpg --import management-clusters/${MC_NAME}/.sops.keys/.sops.master.asc
    sops --encrypt --in-place pullsecrets.enc.yaml
    ```

5. Edit `kustomization.yaml` and list newly created secret as resource:

    ```nohighlight
    yq -i eval '.resources += "pullsecrets.enc.yaml" | .resources style=""' kustomization.yaml
    ```

6. Go to the App directory:

    ```nohighlight
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}
    ```

7. Edit the `imagerepository.yaml` file and reference the newly created secrets there:

    ```nohighlight
    yq -i eval '.spec.secretRef.name = "flux-pull-secrets"' imagerepository.yaml
    ```
