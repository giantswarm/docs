---
linkTitle: Update an existing App
title: Update an existing App
description: Learn how to update an App already deployed in a workload cluster with GitOps.
weight: 60
aliases:
  - /advanced/gitops/apps
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-updating-app
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I update an existent app deployed with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-10-22
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "overview/fleet-management/app-management/" >}}).

# Update an existing App

Follow the below instructions to update an existing `App`.

## Export environment variables

The management cluster codename, organization name, workload cluster name and App name are needed in multiple places across this instruction, the least error prone way of providing them is by exporting them as environment variables:

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME=APP_NAME
```

## Updating App

App update and reconfiguration must be done in the correct resource. If you want to reconfigure a property of `App` resource, like the application version, you have to edit the `appcr.yaml` file. If you want to edit the plain text or encrypted configuration, you have to edit the relevant resource type.

### Updating App resource

1. Go to the `App` directory:

    ```sh
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}
    ```

2. Edit the `appcr.yaml` if you want to update the `App` resource fields, like version, catalog, etc. For all the supported fields reference [the App CRD schema](https://docs.giantswarm.io/use-the-api/management-api/crd/apps.application.giantswarm.io/)

### Updating configmap user values

1. Go to the `App` directory:

    ```sh
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}
    ```

2. Edit the `configmap.yaml` if you want to update a non-secret user configuration

### Updating secret user values

1. Go to the App directory:

    ```sh
    cd management-clusters/${MC_NAME}/organizations/${ORG_NAME}/workload-clusters/${WC_NAME}/mapi/apps/${APP_NAME}
    ```

2. Import the workload cluster regular GPG private key from your safe storage into your key chain. In our example, we're gonna use `LastPass` for that:

    ```sh
    gpg --import \
    <(lpass show --notes "Shared-Dev Common/GPG private key (${MC_NAME}, ${WC_NAME}, Flux)")
    ```

3. Decrypt the `secret.enc.yaml` file with SOPS:

    ```sh
    sops --decrypt --in-place secret.enc.yaml
    ```

4. Grab the `.data.values` field from the secret and `base64` decode it:

    ```sh
    yq eval .data.values secret.enc.yaml | base64 -d > values.tmp.yaml
    ```

5. Edit the `values.tmp.yaml` if you want to update a secret user configuration

6. Save the `base64` encoded `values.tmp.yaml` into variable:

    ```sh
    export NEW_USER_VALUES=$(cat values.tmp.yaml | base64)
    ```

7. Replace secret's `.data.values` with new value:

    ```sh
    yq -i eval ".data.values = \"${NEW_USER_VALUES}\"" secret.enc.yaml
    ```

8. Remove the `values.tmp.yaml`:

    ```sh
    rm values.tmp.yaml
    ```

9. Re-encrypt the `Kubernetes` secret:

    ```sh
    sops --encrypt --in-place secret.enc.yaml
    ```

10. Remove the private GPG key from your keychain and submit a pull request.

    ```sh
    gpg --delete-secret-keys "${KEY_FP}"
    ```
