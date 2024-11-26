---
linkTitle: Add a new App to a workload cluster
title: Add a new App to a workload cluster
description: Learn how to deploy and configure applications into workload clusters using GitOps.
weight: 90
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-wc
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I add an app to a workload cluster with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-19
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "/overview/fleet-management/app-management/" >}}).

# Add a new app to a workload cluster

You can add an `App` resource directly or based it on an [app template]({{< relref "/tutorials/continuous-deployment/apps/add_app_template/" >}}). The documentation below shows common steps as well as what's different in both cases.

## Examples

Examples of creating apps are available in following locations:

- An example of a directly configured app (the simplest use case - no configuration): an [app without configuration](https://github.com/giantswarm/gitops-template/tree/main/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME_OUT_OF_BAND_NO_FLUX_APP/mapi/apps/hello-world)
- An example of a directly configured app (with configuration): an [app that uses a configuration `ConfigMap`](https://github.com/giantswarm/gitops-template/tree/main/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME_OUT_OF_BAND_NO_FLUX_APP/mapi/apps/ingress-nginx)
- An example of an app created from an app template is available in [WC_NAME/apps/ingress-nginx-from-template](https://github.com/giantswarm/gitops-template/tree/main/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME_OUT_OF_BAND_NO_FLUX_APP/mapi/apps/ingress-nginx-from-template).

## Common steps

Please follow these steps when installing an app directly as well as using app template.

### Export environment variables

The management cluster, the organization, the workload cluster and the app names are needed during the process. The easiest way of providing them is by exporting them as environment variables:

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME="${WC_NAME}-APP_NAME"
```

### Setting up the directory structure

Create a new directory with a name corresponding to the `App` name in the apps directory of your workload cluster (recommended path):

```sh
cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps
mkdir ${APP_NAME}
```

## Adding the app directly

Extend the environment variables with the app version, catalog and namespace:

```sh
export APP_VERSION=APP_VERSION
export APP_CATALOG=APP_CATALOG
export APP_NAMESPACE=APP_NAMESPACE
```

Go to the newly created directory and use [the kubectl-gs plugin](https://github.com/giantswarm/kubectl-gs) to generate the [`App` resource](https://docs.giantswarm.io/ui-api/kubectl-gs/template-app/):

```sh
cd ${APP_NAME}/
kubectl gs template app \
--app-name "\${cluster_name}-${APP_NAME}" \
--catalog ${APP_CATALOG} \
--cluster ${WC_NAME} \
--name ${APP_NAME} \
--namespace ${APP_NAMESPACE} \
--version ${APP_VERSION} > appcr.yaml
```

Additionally you can provide a default configuration adding these flags to the previous command:

```nohighlight
--user-configmap ${APP_USER_VALUES}
--user-secret ${APP_USER_VALUES}
```

__Note__: Including `${cluster_name}` in the app name avoids collision between clusters running same apps within the same organization.

Reference [the app configuration](https://docs.giantswarm.io/app-platform/app-configuration/) for more details on how to create respective `ConfigMaps` or secrets.

As optional step, you can place the `ConfigMap` and `Secret` with values as the `configmap.yaml` and `secret.enc.yaml` files respectively:

```sh
# Use one of the two for respective kind
cp ${APP_USER_VALUES} ./configmap.yaml
# cp ${APP_USER_VALUES} ./secret.enc.yaml
```

Then, import the regular `GPG` public key of the workload cluster and encrypt the `secret.enc.yaml` file:

```sh
gpg --import management-clusters/${MC_NAME}/.sops.keys/.sops.${WC_NAME}.asc
sops --encrypt --in-place secret.enc.yaml
```

You can find more information on encrypting secrets in [this document](https://github.com/giantswarm/gitops-template/blob/main/docs/add_mc.md#flux-gpg-master-key-pair).

Lastly, edit the `kustomization.yaml` in the apps folder adding all the newly created files as resources:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
...
- ${APP_NAME}/appcr.yaml
- ${APP_NAME}/secret.enc.yaml
- ${APP_NAME}/configmap.yaml
```

At this point, if you have completed [the workload cluster configuration guide]({{< relref "/tutorials/continuous-deployment/manage-workload-clusters/" >}}), all the necessary `Flux` resources should already be configured.

## Adding apps using a template

When using templates you need to pick a directory where templates live, as example `bases/apps`. Follow the [template creation tutorial]({{< relref "/tutorials/continuous-deployment/apps/add_app_template/" >}}) to learn how. Export the path to the directory in an environment variable:

```sh
export APP_TEMPLATE_DIR=<your_base_directory>
```

Make sure your `APP_NAME` variable is set to the exact same name as used for the app in the app template you're pointing to.

In the current directory (`management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}`) create a new `kustomization.yaml` with the following content:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
## CONFIGURATION OVERRIDE BLOCK START
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
```

Please note, that the block marked with `configuration override` block is only needed in case you override the default configuration. In case you don't override any, skip that YAML block and you are ready to create the app.

Otherwise, you need to patch the configuration, that will extend the app template configuration via `extraConfigs` attribute. Here you see the content of `config_patch.yaml` file. Refer to [the app configuration]({{< relref "/overview/fleet-management/app-management" >}}) for more details about how configuration properties of `App` resource are used).

```yaml
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
```

__Note__: Alternatively, you can rely on [`Kustomize` patches](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patches/) to extend the `App` resource configuration instead.

At this point, everything is prepared and you can commit the changes to the branch to force `Flux` to apply the changes. Further you can learn how to [enable automatic updates for your apps]({{< relref "/tutorials/continuous-deployment/apps/automatic_updates_appcr/" >}}).
