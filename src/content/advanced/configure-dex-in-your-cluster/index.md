---
linkTitle: OIDC auth for workload clusters
title: Configure OIDC using Dex to access your clusters
description: A general explanation on how to install and configure Dex to work as an authenticator mechanism to provide OpenID tokens.
weight: 100
menu:
  main:
    parent: advanced
user_questions:
  - How can I configure OIDC in my cluster?
  - How can I add a new OIDC connector?
last_review_date: 2021-10-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
---

# Configure OpenID Connect (OIDC) with Dex to access your clusters

## Introduction

At Giant Swarm, we automatically configure Dex in management clusters to allow you to authenticate using your own identity providers, towards allowing you to manage your infrastructure using the management cluster's Kubernetes API.

For workload clusters - where you run your applications - we do not enforce any specific OpenID Connect (OIDC) tool to enable single sign-on (SSO). Here, we're going to detail how to configure [Dex](https://dexidp.io/) in those clusters, to provide SSO using OIDC.

![Multi cluster Dex architecture](dex-architecture.png)
<!-- Source: https://drive.google.com/file/d/12Li9z2cqS8uWo1f9bGk6nwV6PLgty9g_ -->

## Why Dex

There are other projects that help to configure OIDC to access Kubernetes clusters, but we consider [Dex](https://dexidp.io/) to be the most feature-rich. First of all, it is not tied to Kubernetes, so you can use Dex to handle authentication and authorization for your own apps as well. Secondly, Dex can act like an identity provider hub, where you can plug in different providers via different connectors, and choose between them when you want to log in.

## OIDC in Kubernetes

The Kubernetes API allows users to authenticate using the OIDC protocol, making it possible to enforce multi-factor authentication (MFA) or password policies by delegating to your identity provider. The API will use the field named `id_token` from the response as a bearer token to authenticate users.

## Configure the OIDC values on the cluster resource

We need to set values for the OIDC Issuer URL and Client ID. You can define those values in the cluster custom resource. These values will then be set as flags on the Kubernetes API Server (specifically, `--oidc-issuer-url` and `--oidc-client-id`).

{{< tabs >}}
{{< tab title="Azure">}}

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:  
    oidc.giantswarm.io/client-id: dex-k8s-authenticator
    oidc.giantswarm.io/issuer-url: https://dex.<CLUSTERID>.<BASEDOMAIN>
    oidc.giantswarm.io/group-claim: groups
    oidc.giantswarm.io/username-claim: email
  ...
```

{{< /tab >}}
{{< tab title="AWS">}}

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
spec:
  cluster:
    ...
    oidc:
      claims:
        groups: groups
        username: email
      clientID: dex-k8s-authenticator
      issuerURL: https://dex.<CLUSTERID>.<BASEDOMAIN>
```

{{< /tab >}}
{{< /tabs >}}

__Note__: In the above snippets you need to change the `<CLUSTERID>` and `<BASEDOMAIN>` variables to the correct values - the cluster ID of the workload cluster you are configuring, and the base domain that you use for your installation, respectively.

## Deploy the app to your cluster

In this guide, we will use a single app deployment for each cluster that you want to authenticate towards. There are different ways to set up how you authenticate towards your Kubernetes API with Dex, but in our opinion, using a single deployment per cluster is more resilient than having a common Dex deployment for all your workload clusters.

We'll use the [app platform](https://docs.giantswarm.io/app-platform/) to deploy the app, as it allows us to deploy apps across workload clusters using a single API endpoint. In this example, we create an `App` custom resource (CR) with the parameters to install our [`dex-app`](https://github.com/giantswarm/dex-app) in the desired cluster, and a `ConfigMap` with the configuration values.

{{< tabs >}}
{{< tab title="Keycloak">}}

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dex-app-user-values
  namespace: <CLUSTERID>
data:
  values: |
    isWorkloadCluster: true
    services:
      kubernetes:
        api:
          caPem: |
            -----BEGIN CERTIFICATE-----
            M...=
            -----END CERTIFICATE-----
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
          connectorConfig: >-
            clientID: <CLIENT-ID-SET-IN-YOUR-IdP>
            clientSecret: <CLIENT-SECRET-SET-IN--YOUR-IdP>
            insecureEnableGroups: true
            scopes:
            - email
            - groups
            - profile
            issuer: https://<IDP_ENDPOINT>/auth/realms/master
            redirectURI: https://dex.<CLUSTERID>.<BASEDOMAIN>/callback
```

{{< /tab >}}
{{< tab title="Github">}}

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dex-app-user-values
  namespace: <CLUSTERID>
data:
  values: |
    isWorkloadCluster: true
    services:
      kubernetes:
        api:
          caPem: |
            -----BEGIN CERTIFICATE-----
            M...=
            -----END CERTIFICATE-----
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
          connectorConfig: >-
            clientID: <CLIENT-ID-SET-IN-YOUR-IdP>
            clientSecret: <CLIENT-SECRET-SET-IN--YOUR-IdP>
            tenant: <TENANT-SET-SET-IN--YOUR-IdP>
            redirectURI: https://dex.<CLUSTERID>.<BASEDOMAIN>/callback
```

{{< /tab >}}
{{< tab title="Active Directory">}}

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dex-app-user-values
  namespace: <CLUSTERID>
data:
  values: |
    isWorkloadCluster: true
    services:
      kubernetes:
        api:
          caPem: |
            -----BEGIN CERTIFICATE-----
            M...=
            -----END CERTIFICATE-----
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
          connectorConfig: >-
            clientID: <CLIENT-ID-SET-IN-YOUR-IdP>
            clientSecret: <CLIENT-SECRET-SET-IN--YOUR-IdP>
            tenant: <TENANT-SET-SET-IN--YOUR-IdP>
            redirectURI: https://dex.<CLUSTERID>.<BASEDOMAIN>/callback
```

{{< /tab >}}
{{< /tabs >}}

__Note__: In the above snippet you have to replace the `<CLUSTERID>` variable and add the Kubernetes Certificate Authority to ensure Dex can trust the API endpoint. Finally you have to use a connector. Here we show examples for Keycloak, Active Directory, and GitHub.
You can use more than one connector, but they need to have a different `id` value. We advice to use `- id: customer` for your primary connector.

After you have applied the `ConfigMap` manifest to the Management API you have to submit the App custom resource that defines the intent to install the Dex app in the given cluster.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app.kubernetes.io/name: dex-app
  name: dex-app
  namespace: <CLUSTERID>
spec:
  catalog: giantswarm-playground
  name: dex-app
  namespace: dex
  userConfig:
    configMap:
      name: dex-app-user-values
      namespace: <CLUSTERID>
```

__Note__: When applying the example in the snippet above, please change the `<CLUSTERID>` variable to the cluster ID of the workload cluster you are configuring,

Then submit the resource to the management API and the App operator will manage it to make the actual installation and configuration. You can log in now into the cluster API with your identity provider using the login endpoint that Dex creates for you. By default, it will be `https://login.<CLUSTERID>.<BASEDOMAIN>`.

## Further reading

- [Authenticating with Microsoft Azure Active Directory]({{< relref "/advanced/authentication-azure-ad" >}})
- [App platform overview](https://docs.giantswarm.io/app-platform/)
