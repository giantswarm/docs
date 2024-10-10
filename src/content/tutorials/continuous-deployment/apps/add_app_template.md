---
linkTitle: Add a new app template
title: Add a new app template
description: Learn how to create application templates to deploy apps using GitOps.
weight: 70
aliases:
  - /advanced/gitops/apps
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-template
    parent: tutorials-continuous-deployment-apps
last_review_date: 2024-10-10
user_questions:
  - How can I create an template for app deployment in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "/overview/fleet-management/app-management/" >}}).

# Add a new app template to the repository

To avoid duplication caused by adding the same application from scratch across all your clusters, you can prepare app templates providing a pre-configured version of an `App`. This also allows you to manage and version an app's configuration even if the app itself isn't yet installed in any cluster.

## Example

An example of an app template is available in the [gitops-template repository "bases/apps/ingress-nginx"](https://github.com/giantswarm/gitops-template/tree/main/bases/apps/ingress-nginx).

## Export environment variables

__Note__: Management Cluster codename, Organization name, workload cluster name and several app-related values are needed in multiple places across these instructions. The least error prone way of providing them is by exporting them as environment variables:

```nohighlight
export WC_NAME=CLUSTER_NAME
export APP_NAME="${WC_NAME}-APP_NAME"
export APP_VERSION=APP_VERSION
export APP_CATALOG=APP_CATALOG
export APP_NAMESPACE=APP_NAMESPACE
# OPTIONAL more info about app configuration can be found at https://docs.giantswarm.io/getting-started/app-platform/app-configuration/#basic-values-merging-example
export APP_USER_VALUES=CONFIGMAP_OR_SECRET_PATH
```

## Setting up directory tree structure for managing apps

1. Go to the `bases/apps` directory and create a new directory for the new app template:

    ```nohighlight
    cd bases/apps/
    mkdir ${APP_NAME}
    ```

2. Navigate to the newly created directory and use [the kubectl-gs plugin](https://github.com/giantswarm/kubectl-gs) to generate the [App CR](https://docs.giantswarm.io/ui-api/kubectl-gs/template-app/):

    ```nohighlight
    cd ${APP_NAME}/
    kubectl gs template app \
    --app-name ${APP_NAME} \
    --catalog ${APP_CATALOG} \
    --cluster-name ${WC_NAME} \
    --name ${APP_NAME} \
    --target-namespace ${APP_NAMESPACE} \
    --version ${APP_VERSION} > appcr.yaml
    ```

    __Note__: you most likely want to provide a default configuration, and optionally additional secrets for your application. The flags below can be used to achieve this by adding them to the previous command:

    ```nohighlight
    --user-configmap ${APP_USER_VALUES}
    --user-secret ${APP_USER_VALUES}
    ```

    __Note__: We're including `${cluster_name}` in the app name to avoid a problem when two or more clusters in the same organization want to deploy the same app with its default name.

    Reference [the app configuration]({{< relref "/tutorials/app-platform/app-configuration/" >}}) for more details about how to create the respective configmaps or secrets.

    In case you used `kubectl gs` command you realized the output is an `App` custom resource plus the configmap. In case you want to manage the values in plain YAML, you could rely on the configmap generator feature of [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#generating-resources).

    __Warning__: It can't be used for the secrets as they need to be encrypted before commit into the Git Repository. Refer to our [adding an app](./add_appcr.md) docs to check how to add and encrypt a secret.

3. Now it's time to create the `kustomization.yaml` file, adding the optional secret or configmap as resources and/or using a configmap generator to manage plain configuration:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    buildMetadata: [originAnnotations]
    # default config block start - include if you provide default config
    configMapGenerator:
      - files:
        - values=default_config.yaml
        name: ${cluster_name}-ingress-nginx-values
    generatorOptions:
      disableNameSuffixHash: true
    # default config block end
    resources:
      - appcr.yaml
      - secret.enc.yaml # only if you provide the default secret
      # You can add here the configmap in case of generate it via kubectl gs command or manually
    ```

At this point, you should have a ready app template. You can use it to [add a new app to a workload cluster](/advanced/gitops/apps/add_appcr/).

## Recommended next steps

- [Add a new app to a workload cluster](/advanced/gitops/apps/add_appcr/)
- [Creating and using app sets](/advanced/gitops/apps/app_sets/)
