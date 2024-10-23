---
linkTitle: Add a new App to a workload cluster
title: Add a new App to a workload cluster
description: Learn how to deploy and configure applications into workload clusters using GitOps.
weight: 90
aliases:
  - /advanced/gitops/apps
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-wc
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I add an app to a workload cluster with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-10-22
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "overview/fleet-management/app-management/" >}}).

# Add a new app to a workload cluster

Follow the instructions below to add a new `App` to a workload cluster managed in this repository. You can add an `App` directly (without any intermediate step) or use an [app template]({{< relref "/tutorials/continuous-deployment/apps/add_app_template/" >}}). The documentation below shows common steps as well as what's different in both cases.

## Examples

Examples of creating apps are available in following locations:

- An example of a directly configured app (the simplest use case - no configuration): an [app without configuration](https://github.com/giantswarm/gitops-template/tree/main//management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/apps/hello-world/)
- An example of a directly configured app (with configuration): an [app that uses a configuration configmap](https://github.com/giantswarm/gitops-template/tree/main//management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/apps/ingress-nginx/)
- An example of an app created from an app template is available in [WC_NAME/apps/ingress-nginx-from-template](https://github.com/giantswarm/gitops-template/tree/main//management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/apps/ingress-nginx-from-template/).

## Common steps

Please follow these steps when installing an app directly as well as using app template.

### Export environment variables

__Note__: Management Cluster codename, Organization name, workload cluster name and several app-related values are needed in multiple places across this instruction, the least error prone way of providing them is by exporting them as environment variables:

```nohighlight
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME="${WC_NAME}-APP_NAME"
```

### Setting up directory tree structure for managing apps

1. Go to the `apps` directory:

    ```nohighlight
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps
    ```

2. Create new directory with a name corresponding to the App name:

    ```nohighlight
    mkdir ${APP_NAME}
    ```

## Adding App directly

1. Set remaining environment variables

    ```nohighlight
    export APP_VERSION=APP_VERSION
    export APP_CATALOG=APP_CATALOG
    export APP_NAMESPACE=APP_NAMESPACE
    # OPTIONAL
    export APP_USER_VALUES=CONFIGMAP_OR_SECRET_PATH
    ```

2. Go to the newly created directory and use [the kubectl-gs plugin](https://github.com/giantswarm/kubectl-gs) to generate the [App CR](https://docs.giantswarm.io/ui-api/kubectl-gs/template-app/):

    ```nohighlight
    cd ${APP_NAME}/
    kubectl gs template app \
    --app-name "\${cluster_name}-${APP_NAME}" \
    --catalog ${APP_CATALOG} \
    --cluster ${WC_NAME} \
    --name ${APP_NAME} \
    --namespace ${APP_NAMESPACE} \
    --version ${APP_VERSION} > appcr.yaml
    ```

    __Note__: you can optionally configure App with the user-provided values by adding the below flags to the previous command:

    ```nohighlight
    --user-configmap ${APP_USER_VALUES}
    --user-secret ${APP_USER_VALUES}
    ```

    __Note__: We're including `${cluster_name}` in the app name to avoid a problem when two or more clusters in the same organization want to deploy the same app with its default name.

    Reference [the App Configuration](https://docs.giantswarm.io/app-platform/app-configuration/) for more details on how to create respective configmaps or secrets.

3. (optional - if adding configuration) Place configmap and secrets with values as the `configmap.yaml` and `secret.enc.yaml` files respectively:

    ```nohighlight
    # Use one of the two for respective kind
    cp ${APP_USER_VALUES} ./configmap.yaml
    # cp ${APP_USER_VALUES} ./secret.enc.yaml
    ```

4. (optional - if encrypting secrets) Import the regular GPG public key of the workload cluster and encrypt the `secret.enc.yaml` file:

    ```nohighlight
    gpg --import management-clusters/${MC_NAME}/.sops.keys/.sops.${WC_NAME}.asc
    sops --encrypt --in-place secret.enc.yaml
    ```

    You can find more information on encrypting secrets in [this document](https://github.com/giantswarm/gitops-template/blob/main/docs/add_mc.md#flux-gpg-master-key-pair).

5. Go back to the `apps` directory:

    ```nohighlight
    cd ..
    ```

6. Edit the `kustomization.yaml` there adding all the newly created files as resources:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    resources:
    - ${APP_NAME}/appcr.yaml
    - ${APP_NAME}/secret.enc.yaml
    - ${APP_NAME}/configmap.yaml
    ```

  At this point, if you have followed [the WC configuration guide]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters/" >}}), all the necessary Flux resources should already be configured.

## Adding App using App Template

1. First, you need to pick a directory with an App Template from the `bases/apps` dir created in the [template creation page]({{< relref "/tutorials/continuous-deployment/apps/add_app_template/" >}}). Export the path to the directory in an environment variable:

    ```nohighlight
    export APP_TEMPLATE_DIR=[YOUR_BASE_PATH]
    ```

    Make sure your `APP_NAME` variable is set to the exact same name as used for the app in the App Template you're pointing to.

2. In the current directory (`management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}`) create a new `kustomization.yaml` with the following content:

    ```nohighlight
    cat <<EOF > kustomization.yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    buildMetadata: [originAnnotations]
    ## CONFIGURATION OVERRIDE BLOCK START - include only if overriding default config from the Template
    configMapGenerator:
      - files:
          - values=override_config.yaml
        name: \${cluster_name}-${APP_NAME}-user-values
    generatorOptions:
      disableNameSuffixHash: true
    ## CONFIGURATION OVERRIDE BLOCK END
    kind: Kustomization
    patchesStrategicMerge:
      - config_patch.yaml
    resources:
      - ../../../../../../../../../${APP_TEMPLATE_PATH}
      - secret.enc.yaml ## ONLY IF INCLUDING SECRET
    EOF
    ```

Please note, that the block marked "configuration override block" is needed only if you override the default configuration and/or the secret configmap (from the template). In case you don't override any, skip both parts in `kustomization.yaml` and also the next three configuration points below.

1. (optional - if you override either configmap or secret) Create a patch configuration file, that will enhance your App Template with a `userConfig` attribute (refer to [the App Configuration](https://docs.giantswarm.io/app-platform/app-configuration/) for more details about how `config` and `userConfig` properties of App CR are used).

    ```nohighlight
    cat <<EOF > config_patch.yaml
    apiVersion: application.giantswarm.io/v1alpha1
    kind: App
    metadata:
      name: \${cluster_name}-${APP_NAME}
    spec:
      userConfig:
        configMap: # include if you override the config from Template
          name: \${cluster_name}-${APP_NAME}-user-values
        secret: # include if you override the secret from Template
          name: \${cluster_name}-${APP_NAME}-user-secret
    EOF
    ```

2. Additional notes

    If you want to, you can use the same idea of App Templates to override any property (like app version) of base App Template by using [`Kustomize` patches](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patches/).

3. Everything is ready, commit the changes to the branch your Flux is using.

## Recommended next steps

- [Enable automatic updates of an existing App]({{< relref "/tutorials/continuous-deployment/apps/automatic_updates_appcr/" >}})
- [Update an existing App]({{< relref "/tutorials/continuous-deployment/apps/update_appcr/" >}})
