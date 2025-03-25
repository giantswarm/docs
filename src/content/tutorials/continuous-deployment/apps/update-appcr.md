---
linkTitle: Update an existing App
title: Update an existing App
description: Learn how to update an App already deployed in a workload cluster with GitOps.
weight: 60
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-updating-app
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I update an existent app deployed with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2025-03-25
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "/overview/fleet-management/app-management/" >}}).

# Update an existing App

In order to update an existing app, you need to edit the `App` resource and/or the `ConfigMap` or `Secret` resources that are associated with it. In the following sections, you will find instructions on how to do that.

## Export environment variables

The management cluster, the organization, the workload cluster and the app names are needed during the process. The easiest way of providing them is by exporting them as environment variables:

```sh
export MC_NAME=CODENAME
export ORG_NAME=ORGANIZATION
export WC_NAME=CLUSTER_NAME
export APP_NAME=APP_NAME
```

## Updating the App

There are three resources that you might need to update:

- The `App` resource itself.
- The `ConfigMap` resource that holds the user values.
- The `Secret` resource that holds the user values.

### Updating App resource

When you want to update the version of the app, the catalog, or any other field of the `App` resource, you need to edit the `appcr.yaml` file.

Edit the `appcr.yaml` following always [the `App` resource schema](https://docs.giantswarm.io/use-the-api/management-api/crd/apps.application.giantswarm.io/) and apply the changes to the `Git` repository.

### Updating configuration

In case you just want to update the configuration of the app, you need to edit the `configmap.yaml` with the new values. As soon as you apply the changes to the `Git` repository, the `Flux` operator will apply the changes to the workload cluster.

### Updating secrets

In this case, you need to decrypt the `secret.enc.yaml` file before editing it. Then you perform the changes and encrypt the file again.

Import the workload cluster private `GPG` key from your keychain tool. In our example, you see `1Password` for this purpose:

```sh
eval $(op signin)
gpg --import \
<(op item get --vault 'Dev Common' "Shared-Dev Common/GPG private key (${MC_NAME}, ${WC_NAME}, Flux)" --reveal --fields notesPlain)
```

Then you can decrypt the `secret.enc.yaml` file and decode the `values` field:

```sh
sops --decrypt --in-place secret.enc.yaml
yq eval .data.values secret.enc.yaml | base64 -d > values.tmp.yaml
```

Now you can edit the `values.tmp.yaml` file with the new values. After that, you need to encode the file back to `base64` and replace the `values` field in the `secret.enc.yaml` file:

```sh
export NEW_USER_VALUES=$(cat values.tmp.yaml | base64)
yq -i eval ".data.values = \"${NEW_USER_VALUES}\"" secret.enc.yaml
```

Finally, you can re-encrypt the `secret.enc.yaml` file:

```sh
sops --encrypt --in-place secret.enc.yaml
```

It's a good practice to remove the decrypted file as follows:

```sh
gpg --delete-secret-keys "${KEY_FP}"
```

Now applying the changes to the `Git` repository will trigger the `Flux` operator to apply the changes to the workload cluster.
