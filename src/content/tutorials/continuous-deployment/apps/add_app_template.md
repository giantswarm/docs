---
linkTitle: Add a new app template
title: Add a new app template
description: Learn how to create application templates to deploy apps using GitOps.
weight: 70
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-template
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I create an template for app deployment in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-19
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "/overview/fleet-management/app-management/" >}}).

# Add a new app template to the repository

To avoid duplication caused by adding the same application from scratch across all your clusters, you can prepare app templates providing a pre-configured version of an `App`. This also allows you to manage and version an app's configuration even if the app itself isn't yet installed in any cluster.

## Example

An example of an app template is available in the [gitops-template repository "bases/apps/ingress-nginx"](https://github.com/giantswarm/gitops-template/tree/main/bases/apps/ingress-nginx).

## Export environment variables

The management cluster, the organization and the workload cluster names are needed during the process. Also, the app name, catalog and namespace should be provided. The easiest way of providing them is by exporting them as environment variables:

```sh
export WC_NAME=CLUSTER_NAME
export APP_NAME="${WC_NAME}-APP_NAME"
export APP_VERSION=APP_VERSION
export APP_CATALOG=APP_CATALOG
export APP_NAMESPACE=APP_NAMESPACE
```

## Setting up directory tree structure for managing apps

Go to the `bases/apps` directory and create a new directory for the new app template:

```sh
cd bases/apps/
mkdir ${APP_NAME}
```

Now, navigate to the newly created directory and use [the kubectl-gs plugin](https://github.com/giantswarm/kubectl-gs) to generate the [`App` resource](https://docs.giantswarm.io/ui-api/kubectl-gs/template-app/):

```sh
cd ${APP_NAME}/
kubectl gs template app \
--app-name ${APP_NAME} \
--catalog ${APP_CATALOG} \
--cluster-name ${WC_NAME} \
--name ${APP_NAME} \
--target-namespace ${APP_NAMESPACE} \
--version ${APP_VERSION} > appcr.yaml
```

Additionally you can provide a default configuration, and additional secrets for your application. Adding them to the previous command as follows:

```text
--user-configmap <my-configmap-name>
--user-secret <my-secret-name>
```

__Note__: Including `${cluster_name}` in the app name avoids collision between clusters running same apps within the same organization.

Reference [the app configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration/" >}}) for more details about how to create the respective `ConfigMaps` or secrets.

After running the `kubectl gs` command you can observe the output has an `App` resource together with the `ConfigMap`. Instead, you could rely on the `ConfigMap` generator feature of [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#generating-resources) to generate it on the fly.

__Warning__: `Kustomize` can't be used for the secrets as they need to be encrypted before commit. Refer to our [adding an app](./add_appcr.md) docs to check how to do it.

In the last step it's time to create the `kustomization.yaml` file, adding the optional `Secret` or `ConfigMap` as resources and/or using a `ConfigMap` generator to manage plain configuration:

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

At this point, you should have an app template ready. Now, you can [add a new app to a workload cluster using the template]({{< relref "/tutorials/continuous-deployment/apps/add_appcr" >}}).
