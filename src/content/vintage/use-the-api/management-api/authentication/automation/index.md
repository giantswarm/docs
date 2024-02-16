---
linkTitle: In automation
title: Authentication for the Management API in automation
description: Using the Management API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to obtain a service account token to use in such a scenario.
weight: 20
menu:
  main:
    identifier: uiapi-managementapi-authentication-automation
    parent: uiapi-managementapi-authentication
last_review_date: 2023-05-02
aliases:
  - /use-the-api/management-api/authentication/automation
  - /reference/management-api/authentication/automation
  - /ui-api/management-api/authentication/automation
user_questions:
  - How can I use the Management API in a programmatic way?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

Using the Management API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to make use of a service account and create a self-contained kubeconfig file to use in such a scenario.

To learn about authentication as a user who can complete an interactive authentication flow in the browser, please head to our [according article]({{< relref "/vintage/use-the-api/management-api/authentication/user" >}}).

**Note:** In the context of this article we are assuming that you want to connect to the Management API from outside the management cluster. In case your automation is running in the management cluster, using a service for authentication becomes much simpler.

## Step by step

**Note:** If you want to skip the lengthy explanations, you can jump directly to the section below where we [put it all together](#script) in a script.

Each Giant Swarm management cluster provides a service account named `automation` in the `default` namespace. This service account's token and additional information as the API endpoint and CA certificate can then be extracted into a self-contained kubectl configuration file.

**Note:** This `automation` service account comes with a powerful set of permissions, thus **we strongly recommend you create a specific service account for each application**, binding it to specific roles granting only the required permissions in the required namespaces.

These instructions assume the `automation` service account name. You'll have to replace this one with the name of the service account you are using.

### 1. Authenticate for the Management API

Make sure that you have an authenticated `kubectl` context for your Management API. We provide extensive documentation on [how to authenticate as a user]({{< relref "/vintage/use-the-api/management-api/authentication/user" >}}).

### 2. Find the service account's secret

Every service account comes with a `Secret` resource that contains the credentials and some additional details we need. To obtain that resource, we must look up its name first.

Here, `INSTALLATION` is a placeholder for the name of your installation. `SERVICE_ACCOUNT_NAME` is the name of the service account you want to use.

```nohighlight
kubectl --context gs-INSTALLATION --namespace default get serviceaccount SERVICE_ACCOUNT_NAME -o jsonpath='{.secrets[0].name}'
```

### 3. Extract details from the service account secret

With `SECRET_NAME` being the name of the service account secret found in the previous step, we now extract the authentication token ...

```nohighlight
kubectl --context gs-INSTALLATION --namespace default get secret SECRET_NAME -o jsonpath='{.data.token}' | base64 --decode
```

... and the CA certificate, which we store in a file.

```nohighlight
kubectl --context gs-INSTALLATION --namespace default get secret SECRET_NAME -o jsonpath='{.data.ca\.crt}' | base64 --decode > ca.pem
```

### 4. Get your Management API endpoint

It's already in your kubectl configuration and can be extracted from there like this:

```nohighlight
kubectl --context gs-INSTALLATION config view --minify -o jsonpath='{.clusters[0].cluster.server}'
```

### 5. Create a self-contained kubeconfig

Here, let `FILE` be the path of a file that does not yet exist, e. g. `kubeconfig.yaml`. `API_ENDPOINT` is the Management API endpoint from step 4. `CA_CERTIFICATE_PATH` is the path of the CA file created in step 3.

```nohighlight
kubectl --kubeconfig FILE config set-cluster default \
  --server API_ENDPOINT \
  --embed-certs \
  --certificate-authority CA_CERTIFICATE_PATH
```

Now replace `TOKEN` with the service account token obtained in step 3 and execute:

```nohighlight
kubectl --kubeconfig FILE config set-credentials default \
  --token TOKEN
```

Then execute this command with `INSTALLATION` being your installation's name, as in all the previous steps.

```nohighlight
kubectl --kubeconfig FILE config set-context gs-INSTALLATION \
  --cluster default \
  --user default
```

Last, select the only context in the kubeconfig as the current one.

```nohighlight
kubectl --kubeconfig FILE config use-context gs-INSTALLATION
```

As a result, in the path `FILE` you have a self-contained kubeconfig file for the Management API. This file includes the service account's authentication token.

### 8. Test the new kubeconfig

```nohighlight
kubectl --kubeconfig FILE cluster-info
```

That command should give you some cluster details and should not result in any errors.

## Security considerations

Service account tokens do not expire automatically. So the self-contained kubeconfig file you are creating could become a security threat. To avoid this, you can take these precautions:

- Create service accounts specifically for each use case. By the use of RBAC, grant only the permissions required for that use case.
- Rotate service account credentials regularly. This can be done simply by deleting the service account's secret.

## Putting it all together {#script}

Our step by step instructions above might give you a good understanding of what has to be done to create a self-contained kubeconfig for an automation. To make that fast and more fail-safe, you can use this script.

Make sure to be logged in with the Management API, and set the variables `INSTALLATION` and `SERVICE_ACCOUNT_NAME`, before executing this script.

```bash
#!/bin/bash

# Adapt these two variables:
INSTALLATION=example
SERVICE_ACCOUNT_NAME=example-sa

# Find the secret associated with the service account
SECRET=$(kubectl --context gs-$INSTALLATION --namespace default get sa $SERVICE_ACCOUNT_NAME -o jsonpath='{.secrets[0].name}')

# Fetch the service account token and the Kubernetes CA certificate from the secret
TOKEN=$(kubectl --context gs-$INSTALLATION --namespace default get secret $SECRET -o jsonpath='{.data.token}' | base64 --decode)
CA_CERT=$(kubectl --context gs-$INSTALLATION --namespace default get secret $SECRET -o jsonpath='{.data.ca\.crt}')

# Fetch the Management API endpoint
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

- [Authentication as a user]({{< relref "/vintage/use-the-api/management-api/authentication/user" >}}) explains how to authenticate as an interactive user
- [Authorization in the Management API]({{< relref "/vintage/use-the-api/management-api/authorization" >}}) explains how to assign permissions to authenticated users
