---
linkTitle: In automation
title: Authentication for the Management API in automation
description: Using the Management API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to obtain a service account token to use in such a scenario.
weight: 20
menu:
  main:
    identifier: uiapi-managementapi-authentication-automation
    parent: uiapi-managementapi-authentication
last_review_date: 2022-04-28
user_questions:
  - How can I use the Management API in a programmatic way?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
---

Outline

- Inside cluster: cross reference to https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/
- Assumption that this is happening outside the management cluster.
- Basic explanation of what's happening
  - Service account
  - Service account token
- Example for applying the token to a kubectl command

---

Using the Management API from an automation requires a hands-free way to provide credentials to kubectl or any Kubernetes client. This article explains how to obtain a service account token to use in such a scenario.

To learn about authentication as a user who can complete an interactive authentication flow in the browser, please head to our [according article]({{< relref "/ui-api/management-api/authentication/user" >}}).

### Remote access to the management cluster {#remote-mc}

Each Giant Swarm management cluster provides a service account named `automation` in the `default` namespace that may be used for creating a self-contained `kubeconfig` file. **Note however**, this account comes with a powerful set of permissions, thus **we strongly recommend you create a specific service account for each application**, binding it to specific roles granting only the required permissions in the required namespaces.

Regardless of which service account you decide to use. From the management cluster, you can utilize the step below to create a config file.

1. Export the Service Account name:

```bash
SA_NAME=automation
```

2. Find Kubernetes Secret associated with the service account:

```bash
SECRET=$(kubectl get sa $SA_NAME -o jsonpath='{.secrets[0].name}')
```

3. Find the service account's token:

```bash
TOKEN=$(kubectl get secret $SECRET -o jsonpath='{.data.token}' | base64 --decode)
```

4. Find Kubernetes CA certificate:

```bash
CA_CERT=$(kubectl get secret $SECRET -o jsonpath='{.data.ca\.crt}')
```

5. Grab installation's API endpoint:

```bash
API_URL=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')
```

6. Grab installation's name:

```bash
MC_NAME=$(kubectl config view --minify -o jsonpath='{.clusters[0].name}')
```

7. Generate kubectl configuration:

```bash
cat <<EOF > kubeconfig
apiVersion: v1
kind: Config
clusters:
  - name: $MC_NAME
    cluster:
      certificate-authority-data: $CA_CERT
      server: $API_URL
users:
  - name: $SA_NAME
    user:
      token: $TOKEN
current-context: $MC_NAME
contexts:
- context:
    cluster: $MC_NAME
    user: $SA_NAME
  name: $MC_NAME
EOF
```

8. Test newly created file:

```nohighlight
kubectl --kubeconfig kubeconfig cluster-info
```

## Full script

```bash

```

## Further reading

- [Authentication as a user]({{< relref "/ui-api/management-api/authentication/user" >}}) explains how to authenticate as an interactive user
- [Authorization in the Management API]({{< relref "/ui-api/management-api/authorization" >}}) explains how to assign permissions to authenticated users
