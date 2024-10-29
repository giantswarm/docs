---
linkTitle: In automation
title: Authentication for the platform API in automation
description: Using the platform API from an automation requires a hands-free way to provide credentials to kubectl or any `kubernetes` client. This article explains how to obtain a service account token to use in such a scenario.
weight: 20
menu:
  main:
    identifier: tutorials-access-management-authentication-automation
    parent: tutorials-access-management-authentication
last_review_date: 2024-10-28
user_questions:
  - How can I use the platform API in a programmatic way?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

Using the platform API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to make use of a service account and create a self-contained `kubeconfig` file to use in such a scenario.

To learn about authentication as a user who can complete an interactive authentication flow in the browser, please head to our [according article]({{< relref "/tutorials/access-management/authentication/user" >}}).

__Note__: In the context of this article we're assuming that you want to connect to the platform API from outside the management cluster. In case your automation is running in the management cluster, using a service for authentication becomes much simpler.

## Step by step

__Note__: If you want to skip the lengthy explanations, you can jump directly to the section below where we [put it all together](#script) in a script.

Every Giant Swarm management cluster provides a service account named `automation` in the `default` namespace. This service account's token and additional information as the API endpoint and `CA` certificate can then be extracted into a self-contained kubectl configuration file.

__Note__: This `automation` service account comes with a powerful set of permissions, thus **we strongly recommend you create a specific service account for each application**, binding it to specific roles granting only the required permissions in the required namespaces.

These instructions assume the `automation` service account name. You'll have to replace this one with the name of the service account you are using.

### 1. Authenticate for the platform API

Make sure that you have an authenticated `kubectl` context for your platform API. We provide extensive documentation on [how to authenticate as a user]({{< relref "/tutorials/access-management/authentication/user" >}}).

### 2. Find the service account's secret

Every service account comes with a `Secret` resource that contains the credentials and some additional details we need. To obtain that resource, we must look up its name first.

Here, `INSTALLATION` is a placeholder for the name of your installation. The default service account name is `automation`. You can use a custom service account name, but you have to replace `automation` with your custom name in the following commands.

```sh
export INSTALLATION=mymc
kubectl --context gs-INSTALLATION --namespace default get serviceaccount automation -o jsonpath='{.secrets[0].name}'
```

### 3. Extract details from the service account secret

With `SECRET_NAME` being the name of the service account `Secret` found in the previous step, we now extract the authentication token.

```sh
kubectl --context gs-INSTALLATION --namespace default get secret SECRET_NAME -o jsonpath='{.data.token}' | base64 --decode
```

The `CA` certificate, which we store in a file.

```sh
kubectl --context gs-INSTALLATION --namespace default get secret SECRET_NAME -o jsonpath='{.data.ca\.crt}' | base64 --decode > ca.pem
```

### 4. Get your platform API endpoint

It's already in your kubectl configuration and can be extracted from there like this:

```sh
kubectl --context gs-INSTALLATION config view --minify -o jsonpath='{.clusters[0].cluster.server}'
```

### 5. Create a self-contained configuration

Here, let `FILE` be the path of a file that doesn't yet exist, e. g. `kubeconfig.yaml`. `API_ENDPOINT` is the platform API endpoint from step 4. `CA_CERTIFICATE_PATH` is the path of the CA file created in step 3.

```sh
kubectl --kubeconfig FILE config set-cluster default \
  --server API_ENDPOINT \
  --embed-certs \
  --certificate-authority CA_CERTIFICATE_PATH
```

Now replace `TOKEN` with the service account token obtained in step 3 and execute:

```sh
kubectl --kubeconfig FILE config set-credentials default \
  --token TOKEN
```

Then execute this command with `INSTALLATION` being your installation's name, as in all the previous steps.

```sh
kubectl --kubeconfig FILE config set-context gs-INSTALLATION \
  --cluster default \
  --user default
```

Last, select the only context in the `kubeconfig` as the current one.

```sh
kubectl --kubeconfig FILE config use-context gs-INSTALLATION
```

As a result, in the path `FILE` you have a self-contained `kubeconfig` file for the platform API. This file includes the service account's authentication token.

### 8. Test the new file configuration

```sh
kubectl --kubeconfig FILE cluster-info
```

That command should give you some cluster details and shouldn't result in any errors.

## Security considerations

Service account tokens don't expire automatically. So the self-contained `kubeconfig` file you are creating could become a security threat. To avoid this, you can take these precautions:

- Create service accounts specifically for each use case. By the use of RBAC, grant only the permissions required for that use case.
- Rotate service account credentials often. This can be done simply by deleting the service account's secret.

## Putting it all together {#script}

Our step by step instructions above might give you a good understanding of what has to be done to create a self-contained `kubeconfig` for an service account. To make that fast and more fail-safe, you can use this script.

Make sure to be logged in with the platform API, and set the variables `INSTALLATION` and `SERVICE_ACCOUNT_NAME`, before executing this script.

```bash
#!/bin/bash

# Adapt these two variables:
INSTALLATION=mymc
SERVICE_ACCOUNT_NAME=automation

# Find the secret associated with the service account
SECRET=$(kubectl --context gs-$INSTALLATION --namespace default get sa $SERVICE_ACCOUNT_NAME -o jsonpath='{.secrets[0].name}')

# Fetch the service account token and the Kubernetes CA certificate from the secret
TOKEN=$(kubectl --context gs-$INSTALLATION --namespace default get secret $SECRET -o jsonpath='{.data.token}' | base64 --decode)
CA_CERT=$(kubectl --context gs-$INSTALLATION --namespace default get secret $SECRET -o jsonpath='{.data.ca\.crt}')

# Fetch the platform API endpoint
API_URL=$(kubectl --context gs-$INSTALLATION config view --minify -o jsonpath='{.clusters[0].cluster.server}')

# Save the CA in a file
echo $CA_CERT | base64 -D > $INSTALLATION-ca.pem

# Create the kubeconfig file
kubectl --kubeconfig kubeconfig_$INSTALLATION.yaml config set-cluster default \
  --server $API_URL \
  --embed-certs \
  --certificate-authority $INSTALLATION-ca.pem

kubectl --kubeconfig kubeconfig_$INSTALLATION.yaml config set-credentials default \
  --token $TOKEN

kubectl --kubeconfig kubeconfig_$INSTALLATION.yaml config set-context gs-$INSTALLATION \
  --cluster default \
  --user default

kubectl --kubeconfig kubeconfig_$INSTALLATION.yaml config use-context gs-$INSTALLATION
```

## Further reading

- [Authentication as a user]({{< relref "/tutorials/access-management/authentication/user" >}}) explains how to authenticate as an interactive user
- [Authorization in the platform API]({{< relref "/tutorials/access-management/authorization" >}}) explains how to assign permissions to authenticated users
