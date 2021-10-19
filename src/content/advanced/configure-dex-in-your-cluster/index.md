---
linkTitle: OIDC with Dex to access your clusters
title: Configure OIDC with Dex to access your clusters
description: A general explanation on how to install and configure Dex to work as authenticator mechanism to provide OpenID tokens.
weight: 100
menu:
  main:
    parent: advanced
user_questions:
  - How can I configure OIDC in my cluster?
  - How can I add a new OIDC connector?
aliases:
  - /basics/configure-dex-in-your-cluster/
last_review_date: 2021-10-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
---

# Configure OpenID Connect (OIDC) with Dex to access your clusters

## Introduction

In Giant Swarm we automatically configure Dex in our management clusters to allow you to authenticate using their own identity providers and manage their infrastructure using Kubernetes API.

For the workload clusters, where you run their applications, we do not enforce any OpenID Connect (OIDC) tool to enable single sign-on (SSO). Here we are going to expose the steps to follow in order to configure [dex](https://dexidp.io/) in those clusters.

![Multi Cluster Dex Architecture](dex-architecture.png)
<! Source: https://drive.google.com/file/d/12Li9z2cqS8uWo1f9bGk6nwV6PLgty9g_>

## Why dex

There are other projects that help to configure OIDC to access Kubernetes cluster APIs, but [dex](https://dexidp.io/) stands out about the others. First of all, it is not tied to Kubernetes, you can use `dex` to handle authentication and authorization for your apps. But the most impressive feature is how to handle different connectors. In reality `dex` acts like an identity provider `hub`, you can plug in different providers and allow you to choose between them when they want to log in.

## OIDC in Kubernetes

Kubernetes API allows the users to authenticate using OIDC protocol making possible to enforce MFA or password policies thanks to your Identity Provider service. The API will use the `id_token` from the response as bearer token to authenticate the users.

## Configure the OIDC values on the cluster resource

The first steps is to set the right values in the Kubernetes API (`--oidc-issuer-url` and `--oidc-client-id`) of the cluster. At Giant Swarm, we allow the user to define those values in the AWS/Azure cluster custom resource.

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

__Note__: In the above snippet you need to change the `<CLUSTERID>` and `<BASEDOMAIN>` variables for the real values, the cluster ID that represent your cluster and the base domain that you use for your installation respectively.

## Deploy Dex app to your cluster

In this guide, we will use a `dex` deployment for each cluster that we want to authenticate against. There are different ways to architecture how your authenticate against your Kubernetes API with an OIDC tool, but in my opinion using a single `dex` deployment by cluster offers to be more resilient and independent that having a single Dex instance for all.

In Giant Swarm, we built an [App Platform](https://docs.giantswarm.io/app-platform/) that helps us deploy apps across clusters using a single API endpoint. In this example, we define a configmap with the `dex` values configuration and an App custom resource with the parameters to install the application in the desired cluster.

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
        connectorName: test

        ## For Keyclock
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

        ## For Active Directory
        connectorType: microsoft
        connectorConfig: >-
          clientID: <CLIENT-ID-SET-IN-YOUR-IdP>
          clientSecret: <CLIENT-SECRET-SET-IN--YOUR-IdP>
          tenant: <TENANT-SET-SET-IN--YOUR-IdP>
          redirectURI: https://dex.<CLUSTERID>.<BASEDOMAIN>/callback

        ## For Github  
        connectorType: github
        connectorConfig: >-
          clientID: <CLIENT-ID-SET-IN-YOUR-IdP>
          clientSecret: <CLIENT-SECRET-SET-IN--YOUR-IdP>
          loadAllGroups: false
          orgs:
          - name: <GITHUB_ORG_NAME>
            teams:
            - <GITHUB_TEAM_NAME>
          redirectURI: https://dex.<CLUSTERID>.<BASEDOMAIN>/callback

```

__Note__: In the above snippet you have to replace the `<CLUSTERID>` variable and add the Kubernetes Certificate Authority to ensure Dex can trust the API endpoint. Finally you have to use a connector. Here we show three example values.

After you have applied the configmap to the management API you have to submit the App custom resource that defines the intent to install the Dex app in the given cluster.

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

__Note__: When applying the example in the snippet above, please replace the `<CLUSTERID>` variable for the cluster ID that represent your cluster.

Then submit the resource to the management API and the App operator will manage it to make the actual installation and configuration. You can log in now into the cluster API with your identity provider using the login endpoint that Dex creates for you. By default, it will be `https://login.<CLUSTERID>.<BASEDOMAIN>`.

## Further reading

- [App Platform](https://docs.giantswarm.io/app-platform/)
- [Authenticating with Microsoft Azure Active Directory](https://medium.com/@GiantSwarm/authenticating-with-microsoft-azure-active-directory-2039b5f69fca)
