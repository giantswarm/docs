---
linkTitle: Add a new App Template
title: Add a new App Template
description: Learn how to create application templates to deploy apps using GitOps.
weight: 50
menu:
  main:
    identifier: advanced-gitops-apps-add-app-template
    parent: advanced-gitops-apps
last_review_date: 2024-02-16
user_questions:
  - How can I create an template for app deployment in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

This document is part of the documentation to use GitOps with Giant Swarm App Platform. You can find more information about the [App Platform in our docs](/platform-overview/app-platform/).

# Add a new app template to the repository

To avoid duplication caused by adding the same application from scratch across all your clusters, you can prepare App Templates providing a pre-configured version of an App. This also allows you to manage and version an app's configuration even if the app itself is not yet installed in any cluster.

## Example

An example of an app template is available in the [gitops-template repository "bases/apps/ingress-nginx"](https://github.com/giantswarm/gitops-template/tree/main/bases/apps/ingress-nginx).

## Export environment variables

__Note__: Management Cluster codename, Organization name, Workload Cluster name and several App-related values are needed in multiple places across these instructions. The least error prone way of providing them is by exporting them as environment variables:

```nohighlight
export WC_NAME=CLUSTER_NAME
export APP_NAME="${WC_NAME}-APP_NAME"
export APP_VERSION=APP_VERSION
export APP_CATALOG=APP_CATALOG
export APP_NAMESPACE=APP_NAMESPACE
# OPTIONAL more info about App Configuration can be found at https://docs.giantswarm.io/getting-started/app-platform/app-configuration/#basic-values-merging-example
export APP_USER_VALUES=CONFIGMAP_OR_SECRET_PATH
```

## Setting up directory tree structure for managing apps

1. Go to the `bases/apps` directory and create a new directory for the new App Template:

    ```nohighlight
    cd bases/apps/
    mkdir ${APP_NAME}
    ```

2. Navigate to the newly created directory and use [the kubectl-gs plugin](https://github.com/giantswarm/kubectl-gs) to generate the [App CR]({{< relref "/reference/kubectl-gs/template-app/" >}}):

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

    Reference [the App Configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration" >}}) for more details about how to properly create the respective ConfigMaps or Secrets.

    In case you used `kubectl gs` command you realized the output is an App Custom Resource plus the ConfigMap. In case you want to manage the values in plain YAML, you could rely on the ConfigMap generator feature of [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#generating-resources).

    __Warning__: It can not be used for the Secrets as they need to be encrypted before commit into the Git Repository. Refer to our [adding an App]({{< relref "/vintage/advanced/gitops/apps/add-appcr" >}}) docs to check how to add and encrypt a Secret.

3. Now it is time to create the `kustomization.yaml` file, adding the optional Secret/ConfigMap as resources and/or using a ConfigMapGenerator to manage plain configuration:

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
      - secret.enc.yaml # only if you provide the default Secret
      # You can add here the config map in case of generate it via kubectl gs command or manually
    ```

At this point, you should have a ready app template. You can use it to [add a new App to a Workload Cluster]({{< relref "/vintage/advanced/gitops/apps/add-appcr" >}}).

## Recommended next steps

- [Add a new App to a Workload Cluster]({{< relref "/vintage/advanced/gitops/apps/add-appcr" >}})
- [Creating and using App Sets]({{< relref "/vintage/advanced/gitops/apps/app-sets" >}})
