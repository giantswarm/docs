---
linkTitle: Add a new App Template
title: Add a new App Template
description: Learn how to create application templates to deploy apps using GitOps.
weight: 50
menu:
  main:
    identifier: advanced-gitops-apps-add-app-template
    parent: advanced-gitops-apps
last_review_date: 2023-02-10
user_questions:
  - How can I create an template for app deployment in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

# Add a new App Template to the repository

In order to avoid adding the same application from scratch across all your clusters, you can prepare App Templates providing a pre-configured version of an App. This also allows you to manage and version an app's configuration even if the app itself is not yet installed in any cluster.

## Example

An example of an App Template is available in the [gitops-template repository "bases/apps/nginx-ingress-controller"](https://github.com/giantswarm/gitops-template/tree/main/bases/apps/nginx-ingress-controller).

## Export environment variables

__Note__: Management Cluster codename, Organization name, Workload Cluster name and several App-related values are needed in multiple places across this instructions, the least error prone way of providing them is by exporting them as environment variables:

```nohighlight
export WC_NAME=CLUSTER_NAME
export APP_NAME="\${cluster_name}-APP_NAME"
export APP_VERSION=APP_VERSION
export APP_CATALOG=APP_CATALOG
export APP_NAMESPACE=APP_NAMESPACE
# OPTIONAL
export APP_USER_VALUES=CONFIGMAP_OR_SECRET_PATH
```

## Setting up directory tree structure for managing apps

1. Go to the `apps` directory and prepare a directory for the new App Template:

    ```nohighlight
    cd bases/apps/
    mkdir ${APP_NAME}
    ```

1. Go to the newly created directory and use [the kubectl-gs plugin](https://github.com/giantswarm/kubectl-gs) to generate the [App CR](https://docs.giantswarm.io/ui-api/kubectl-gs/template-app/):

    ```nohighlight
    cd ${APP_NAME}/
    kubectl gs template app \
    --app-name ${APP_NAME} \
    --catalog ${APP_CATALOG} \
    --cluster ${WC_NAME} \
    --name ${APP_NAME} \
    --namespace ${APP_NAMESPACE} \
    --version ${APP_VERSION} > appcr.yaml
    ```

**__Note__**, you most likely want to provide a default configuration, so add any of the below flags to the previous command:

    ```nohighlight
    --user-configmap ${APP_USER_VALUES}
    --user-secret ${APP_USER_VALUES}
    ```

**__Note__**, We're including `${cluster_name}` in the app name to avoid a problem when two or more clusters in the same organization want to deploy the same app with its default name.

    Reference [the App Configuration](https://docs.giantswarm.io/app-platform/app-configuration/) for more details about
    how to properly create the respective ConfigMaps or Secrets.

    If you want to provide a default config, we can use use the ConfigMap generator feature of `kustomize`. This allows us to use a pure YAML file for the configuration, without wrapping it into a ConfigMap. Still, for Secrets we need to encrypt them as a Secret object and the generator approach won't work. Refer to our [adding an App](./add_appcr.md) docs to check how to add and encrypt a Secret. For configuration that can be used as a ConfigMap, just add the content to a `default_config.yaml` file.

1. Add the `kustomization.yaml` file, adding an optional Secret as a resource and a ConfigMapGenerator for plain text config:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    buildMetadata: [originAnnotations]
    # default config block start - include if you provide default config
    configMapGenerator:
      - files:
        - values=default_config.yaml
        name: ${cluster_name}-nginx-ingress-controller-values
    generatorOptions:
      disableNameSuffixHash: true
    # default config block end
    resources:
      - appcr.yaml
      - secret.enc.yaml # only if you provide default Secret
    ```

At this point, you should have a ready App Template.

## Recommended next steps

- [Add a new App to a Workload Cluster](/advanced/gitops/apps/add_appcr/)
- [Creating and using App Sets](/advanced/gitops/apps/app_sets/)
