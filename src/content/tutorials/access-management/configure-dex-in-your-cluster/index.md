---
linkTitle: OIDC for workload clusters
title: Configure OIDC using Dex to access your clusters
description: How to install and configure Dex to work as an authenticator mechanism to provide OpenID tokens via OpenID Connect (OIDC).
weight: 40
menu:
  principal:
    parent: tutorials-access-management
    identifier: tutorials-access-management-oidc
user_questions:
  - How can I configure OIDC in my cluster?
  - How can I add a new OIDC connector?
last_review_date: 2025-01-09
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

## Introduction

At Giant Swarm, the platform automatically configure `Dex` in the management cluster to allow you to authenticate using your own identity providers, towards allowing you to manage your infrastructure using the platform API (management cluster `Kubernetes` API).

For workload clusters - where you run your applications - there is no default OpenID Connect (OIDC) tool to enable single sign-on (SSO). In this article, you will learn how to configure [`Dex`](https://dexidp.io/) in those clusters, to provide `SSO` using `OIDC`.

![Multi cluster Dex architecture](dex-architecture.png)
<!-- Source: https://drive.google.com/file/d/12Li9z2cqS8uWo1f9bGk6nwV6PLgty9g_ -->

## Why `Dex`

There are other projects that help to configure `OIDC` to access clusters, but our team considers [`Dex`](https://dexidp.io/) to be the most feature-rich. First of all, it's not tied to `Kubernetes`, so you can use it to handle authentication and authorization for your own apps as well. Secondly, `Dex` can act like an identity provider hub, where you can plug in different providers via different connectors, and choose between them when you want to log in.

## OpenID Connect in Kubernetes

The `Kubernetes` API allows users to authenticate using the `OIDC` protocol, making it possible to enforce multi-factor authentication (MFA) or password policies by delegating to your identity provider. The API will use the field named `id_token` from the response as a bearer token to authenticate users.

## Configure the OpenID Connect values on the cluster resource

You need to set values for the OpenID Connect (OIDC) issuer address and client ID. You can define those values in the cluster custom resource. These values will then be set as flags on the `Kubernetes` API server (specifically, `--oidc-issuer-url` and `--oidc-client-id`).

{{< tabs >}}
{{< tab title="Cluster API (any)">}}

```yaml
# Config map with values for the Workload Cluster app
apiVersion: v1
kind: ConfigMap
data:
  values: |
    ...
    global:
      controlPlane:
        oidc:
          issuerUrl: https://dex.CLUSTER_NAME.BASE_DOMAIN
          clientId: dex-k8s-authenticator
          usernameClaim: email
          groupsClaim: groups
```

{{< /tab >}}
{{< tab title="Cluster API (AWS EKS)">}}

```yaml
# Config map with values for the Workload Cluster app
apiVersion: v1
kind: ConfigMap
data:
  values: |
    ...
    global:
      controlPlane:
        oidcIdentityProviderConfig:
          issuerUrl: https://dex.CLUSTER_NAME.BASE_DOMAIN
          clientId: dex-k8s-authenticator
          usernameClaim: email
          groupsClaim: groups
          identityProviderConfigName: dex-k8s-authenticator
```

{{< /tab >}}
{{< /tabs >}}

__Note__: In the above snippets you need to replace the `CLUSTER_NAME` and `BASE_DOMAIN` placeholder with the correct values, which is the name of the workload cluster you are configuring, and the base domain that you use for your installation. You can also derive them from the workload cluster's `Kubernetes` API endpoint, which has an address in the format of `https://api.CLUSTER_NAME.BASE_DOMAIN`.

## Deploy the app to your cluster

In this guide, you will use a single app deployment for each cluster that you want to authenticate towards. There are different ways to set up how you authenticate towards your Kubernetes API with Dex, but in our opinion, using a single deployment per cluster is more resilient than having a common Dex deployment for all your workload clusters.

You will use the [app platform]({{< relref "/overview/fleet-management/app-management" >}}) to deploy the app, as it allows you to deploy apps across workload clusters using a single API endpoint. In this example, you create an `App` custom resource (CR) with the parameters to install your [`dex-app`](https://github.com/giantswarm/dex-app) in the desired cluster, and a `Secret` with the configuration values. The app platform also supports providing the configuration values in a `ConfigMap`, but in the case of Dex, some configuration values are credentials; therefore, using a `Secret` is the preferred method. It's also possible to split the configuration values, provide the public part in a `ConfigMap` and the credentials in a `Secret`, but in this example, you will provide the entire configuration in a `Secret`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: dex-app-user-values
  namespace: CLUSTER_NAMESPACE_NAME
data:
  values: ... # base64 encoded connector config
```

The format of the `connector config` content can look different depending on the OpenID Connect provider you want to use. Some examples can be found below.
Details on all connectors and their respective configuration is available in the [Dex documentation](https://dexidp.io/docs/connectors/).

{{< tabs >}}
{{< tab title="Keycloak">}}

```yaml
isWorkloadCluster: true
oidc:
  expiry:
    signingKeys: 6h
    idTokens: 30m
  customer:
    enabled: true
    connectors:
    - id: customer
      connectorName: test
      connectorType: oidc
      connectorConfig: |
        clientID: CLIENT_ID
        clientSecret: CLIENT_SECRET
        insecureEnableGroups: true
        scopes:
        - email
        - groups
        - profile
        issuer: https://KEYCLOAK_HOST/realms/master
        redirectURI: https://dex.CLUSTER_NAME.BASE_DOMAIN/callback
```

The values for `CLIENT_ID` and `CLIENT_SECRET` are created/defined in the `Keycloak` OpenID Connect client configuration. `KEYCLOAK_HOST` is the fully qualified `hostname` of your `Keycloak` instance.

{{< /tab >}}
{{< tab title="GitHub">}}

```yaml
isWorkloadCluster: true
oidc:
  expiry:
    signingKeys: 6h
    idTokens: 30m
  customer:
    enabled: true
    connectors:
    - id: customer
      connectorName: test
      connectorType: github
      connectorConfig: |
        clientID: CLIENT_ID
        clientSecret: CLIENT_SECRET
        loadAllGroups: false
        teamNameField: slug
        redirectURI: https://dex.CLUSTER_NAME.BASE_DOMAIN/callback
        orgs:
        - name: GITHUB_ORGANIZATION
          teams:
          - GITHUB_TEAM_SLUG
```

The value for `CLIENT_ID` is automatically generated by GitHub after the creation of an `OAuth` app. Please also generate a client secret for that app and replace `CLIENT_SECRET` with the contents of that secret.

In the above example you see how to configure access for a certain GitHub team (named `GITHUB_TEAM_SLUG`, belonging to the `GITHUB_ORGANIZATION` organization). To restrict access in this way, make sure to list the team's _slug_ as it appears in the handle and team address. For example, for a team named `Team Infra`, the handle may be `@my-organization/team-infra`, and the slug used here would be `team-infra`.

Specifying `teams` enables Dex's [group filtering]({{< relref "/tutorials/access-management/configure-dex-in-your-cluster#dex-group-filtering" >}}).

{{< /tab >}}
{{< tab title="Active Directory">}}

```yaml
isWorkloadCluster: true
oidc:
  expiry:
    signingKeys: 6h
    idTokens: 30m
  customer:
    enabled: true
    connectors:
    - id: customer
      connectorName: test
      connectorType: microsoft
      connectorConfig: |
        clientID: CLIENT_ID
        clientSecret: CLIENT_SECRET
        tenant: TENANT
        redirectURI: https://dex.CLUSTER_NAME.BASE_DOMAIN/callback
        useGroupsAsWhitelist: true
        groups:
          - AD_GROUP_NAME
```

The values to be filled in as `CLIENT_ID` and `CLIENT_SECRET` are obtained when creating a client application in Active Directory. Please replace `TENANT` with your Azure AD tenant ID.

Specifying `groups` and `useGroupsAsWhitelist` enables Dex's [group filtering]({{< relref "/tutorials/access-management/configure-dex-in-your-cluster#dex-group-filtering" >}}).

{{< /tab >}}
{{< tab title="Okta">}}

```yaml
isWorkloadCluster: true
oidc:
  expiry:
    signingKeys: 6h
    idTokens: 30m
  customer:
    enabled: true
    connectors:
    - id: customer
      connectorName: test
      connectorType: oidc
      connectorConfig: |
        clientID: CLIENT_ID
        clientSecret: CLIENT_SECRET
        insecureEnableGroups: true
        getUserInfo: true
        scopes:
        - email
        - groups
        - profile
        issuer: https://OKTA_OIDC_ENDPOINT
        redirectURI: https://dex.CLUSTER_NAME.BASE_DOMAIN/callback
```

The values for `CLIENT_ID` and `CLIENT_SECRET` must be created in the `Okta` configuration. `OKTA_OIDC_ENDPOINT` must be replaced with the fully qualified host name of your `Okta` instance.

{{< /tab >}}
{{< /tabs >}}

__Warning__: With `oidc` connector you might need to add `getUserInfo` in the connector configuration to force a second call to the identity provider in order to get groups. This is required for example by `Okta`. More info on this can be found in [dexidp/dex#1065](https://github.com/dexidp/dex/issues/1065).

__Note__: In the above snippet you have to replace the `CLUSTER_NAME` variable and select a connector. Here you see examples for `Keycloak`, `Active Directory`, and `GitHub`.
You can use more than one connector, but they need to have a different `id` value. Our advice is to use `- id: customer` for your primary connector.

After you have applied the `Secret` manifest to the platform API you have to submit the `App` custom resource that defines the intent to install the `Dex` app in the given cluster. You can directly apply it to the platform API.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app.kubernetes.io/name: dex-app
  name: dex-app
  namespace: CLUSTER_NAMESPACE_NAME
spec:
  catalog: giantswarm
  kubeConfig:
    context:
      name: CLUSTER_NAME
    secret:
      name: CLUSTER_NAME-kubeconfig
      namespace: CLUSTER_NAMESPACE_NAME
  name: dex-app
  namespace: dex
  userConfig:
    secret:
      name: dex-app-user-values
      namespace: CLUSTER_NAMESPACE_NAME
  version: 1.22.2
```

__Note__: When applying the example in the snippet above, please replace the `CLUSTER_NAME` placeholder with the name of the workload cluster which you are configuring and the `CLUSTER_NAMESPACE_NAME` placeholder with the name of the namespace which contains the cluster.

Then submit the resource to the management API and the app operator will manage it to make the actual installation and configuration. You can log in now into the cluster API with your identity provider using the login endpoint that `Dex` creates for you. By default, it will be `https://login.CLUSTER_NAME.BASE_DOMAIN`.

__Warning__: It's assumed that you have an [ingress controller and cert-manager]({{< relref "/getting-started/install-an-application" >}}) running in your cluster in order to make Dex available for the callback request made by your identity provider securely. Both of these apps are offered in our managed app catalog. If you supply custom certificates when deploying `Dex`, then you can skip cert-manager installation.

### Using Dex group filtering {#dex-group-filtering}

Group or team filtering is a valuable mechanism that instructs Dex to selectively include only a specific set of groups in the ID tokens' group claims.

Our recommendation is to use group filtering as the default setting for two compelling reasons:

- Users who aren't part of any pre-configured groups will be unable to acquire an ID token, ensuring tighter security.
- Extensive group memberships can result in larger ID tokens, causing issues such as oversized `HTTP` headers.

The disadvantage of using group filtering is that each time you want to use a new group, you will have to update the `Dex` connector configuration.

### Deploying Dex with custom certificates

`Dex` gets certificates from the cert-manager by default. In case the cert-manager is configured to use a custom certification authority, which isn't publicly trusted, `Dex` needs to be configured to trust it.
The custom certification authority needs to be stored in a `Secret` and referenced in the `trustedRootCA` section of the `Secret` or `ConfigMap` with configuration values for the Dex app.

```yaml
trustedRootCA:
  secretName: ... # Name of the secret, which contains the custom CA
  name: ... # Name of the property inside the secret
```

It's also possible to disable retrieving certificates from the cert-manager and supply custom certificates to `Dex` directly. They can be configured in the `ingress` section of the `Secret` or `ConfigMap` with the configuration values for the `Dex` app:

```yaml
ingress:
  tls:
    letsencrypt: false
    caPemB64: ...
    crtPemB64: ...
    keyPemB64: ...
```

### Running Dex in a private workload cluster

When deploying `Dex` to a private workload cluster, it's required to specify a proxy configuration in order to ensure that `Dex` has access to the outside network. Proxy setup can be provided in the `cluster.proxy` section of the `Secret` or `ConfigMap` with configuration values for the `Dex` app.

It's required to specify the address of the `HTTPS` proxy in the `https` property and exclude Kubernetes API from running through the proxy by adding its IP address or network to the `noProxy` property.

```yaml
cluster:
  proxy:
    http: ... # HTTP proxy URL
    https: ... # HTTPS proxy URL
    noProxy: ... # Hostnames or networks/IP ranges excluded from going through the proxy

```

## Dex observability

To get an overview on the authentication success and error rates of your `Dex` instances, our product offers a Grafana dashboard named "Dex" as part of our [observability setup]({{< relref "/overview/observability/data-management/data-exploration/" >}}).

## Logging into your workload cluster via `kubectl gs` with `Athena`

Once `Dex` is set up in your workload cluster, you can enable access via OIDC through our `kubectl` plugin [kubectl gs]({{< relref "/reference/kubectl-gs" >}}).

In order to communicate with the API, `kubectl gs` needs the cluster's `CA` certificate as well as some cluster-specific information, such as the management cluster name and the dex issuer address.

On all Giant Swarm management clusters, there is a public service called `Athena` to expose the `CA` certificate and some information on the installation to the client.

For easy integration with `kubectl gs` you can install [Athena](https://github.com/giantswarm/athena) on your workload cluster via the [app platform]({{< relref "/getting-started/install-an-application" >}}).

Other than the app itself, you will need to provide a `values.yaml` configuration.

The management cluster name is needed as minimal configuration for `Athena`.

```yaml
managementCluster:
  name: test
```

It's also possible to override the api and issuer addresses,`CA` as well as the cluster name and provider in case it's needed:

```yaml
managementCluster:
  name: test
clusterID: example
provider:
  kind: aws
kubernetes:
  caPem: |
    -----BEGIN CERTIFICATE-----
    M...=
    -----END CERTIFICATE-----
  api:
    address: https://api.test.example.io:6443
oidc:
  issuerAddress: https://dex.test.example.io
```

__Note__: For workload cluster using [Cluster API `AWS`](https://github.com/giantswarm/cluster-aws) (CAPA) provider, use `443` instead of `6443` for the API address port.

__Warning__: For workload cluster using [Cluster API `EKS`](https://github.com/giantswarm/cluster-eks) provider, you'll need to configure Athena to use an AWS-managed EKS API server endpoint. This API server endpoint is uniquely allocated to your EKS cluster and can be easily accessed through the AWS EKS console by navigating to the `Overview` tab and under the `Details` section from the EKS cluster information page. For example:

```yaml
kubernetes:
  api:
    address: https://6EAE2F2E28XUD92EXZF54DFEF7C37081D.gr7.eu-central-1.eks.amazonaws.com
```

Access to `Athena` can be restricted to certain `CIDRs`.

```yaml
security:
  subnet:
    customer:
      public: x.x.x.x/x,x.x.x.x/x
      private: x.x.x.x/x
    restrictAccess:
      gsAPI: true
```

Athena also supports custom certificates, same as the `Dex` app.
The certificates need to be provided in the `ingress` section of the configuration:

```yaml
ingress:
  tls:
    letsencrypt: false
    caPemB64: ...
    crtPemB64: ...
    keyPemB64: ...
```

If both `Dex` and `Athena` are configured correctly and you have installed `kubectl gs` on your machine, you can create a kubectl context using the platform API address.

```sh
kubectl gs login https://api.test.example.io
```

## Assign Users or Groups to Roles

The following YAML examples showcase how to assign roles to users or groups in the cluster, granting them specific access permissions. Refer to the [Kubernetes RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) for a deeper understanding of RBAC concepts.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: dex-user-to-cluster-role
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: User
  name: you@example.io
  apiGroup: rbac.authorization.k8s.io
```

__Warning__: This example assigns the `cluster-admin` role to the user `you@example.io`. The `cluster-admin` is a powerful role granting extensive access to the cluster and should only be used with caution and for specific purposes.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: dex-group-to-cluster-role
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: Group
  name: customer:example-admin
  apiGroup: rbac.authorization.k8s.io
```

This example assigns the `cluster-admin` role to members of the group `customer:example-admin`.

__Want to simplify initial access setup?__ Use our [RBAC bootstrap app](https://github.com/giantswarm/rbac-bootstrap-app). This app helps you easily configure the users and groups that will initially have access to the cluster.

Learn how to [use `ServiceAccount` to authenticate against platform API]({{< relref "/tutorials/access-management/authentication/automation" >}}).
