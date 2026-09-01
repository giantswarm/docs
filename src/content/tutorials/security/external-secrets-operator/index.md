---
linkTitle: External Secrets Operator
title: Using External Secrets Operator
diataxis_content_type: how-to-guide
description: How to install External Secrets Operator on a workload cluster and wire up SecretStore and ExternalSecret resources.
weight: 20
menu:
  principal:
    parent: tutorials-security
    identifier: tutorials-security-eso
user_questions:
- How do I use External Secrets Operator?
- How do I install External Secrets Operator on my cluster?
- What resources does external secrets operator consume on my cluster?
aliases:
  - /advanced/security/external-secrets-operator
  - /guides/external-secrets-operator/
  - /advanced/external-secrets-operator/
last_review_date: 2026-08-19
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
---

External Secrets Operator (ESO) reads secrets from an external secret manager and delivers them as Kubernetes secrets. This guide covers installing it on a workload cluster and creating the two resources you need to start pulling secrets.

For what ESO is, how it compares to SOPS, and the risks of depending on it, read [External Secrets Operator]({{< relref "/overview/security/external-secrets-operator/" >}}).

**Note**: ESO needs three additional pods, 300m of CPU, and 1.5GiB of memory once running. Installs and upgrades temporarily need up to 1.5GiB more, because the CRD installer pod caches Kubernetes resources. That extra usage is released as soon as the install job completes.

## Install ESO

Install ESO on your workload cluster as a managed app from our catalogs. No special or additional configuration is required. Create an `App` resource (or a Flux HelmRelease) against the cluster using our GitOps approach, or use our web UI.

**Note:** The `App` custom resource shown below is being phased out in favor of Flux HelmRelease. For new deployments, see [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}).

### Example App resource

```yaml
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: external-secrets
  namespace: abc123
spec:
  catalog: giantswarm-catalog
  kubeConfig:
    inCluster: false
  name: external-secrets
  namespace: org-example
  userConfig:
    configMap:
      name: external-secrets-userconfig-abc123
      namespace: abc123
  version: 0.4.2
```

To configure specific parts of the values yourself, start from the application chart at [giantswarm/external-secrets](https://github.com/giantswarm/external-secrets). For the configuration options the app platform offers, see [app configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration" >}}).

## Create a SecretStore

Using ESO requires two resources on your cluster. Create the [`SecretStore`](https://external-secrets.io/latest/introduction/overview/#secretstore) first.

The secret store binds ESO to your secret manager, whether that's AWS KMS, Azure Key Vault, Hashicorp Vault, or another of the [many supported secret providers](https://external-secrets.io/latest/provider/aws-secrets-manager/).

You can define multiple `SecretStores` on the cluster. This works best inside a multi-tenant environment. Different teams may have different secret providers, or only have restricted access to part of the secret provider, as is the case with Hashicorp Vault Enterprise.

## Create an ExternalSecret

Next, create the [`ExternalSecret`](https://external-secrets.io/latest/api/externalsecret/). Here you bind one or many external secrets to the Kubernetes secret that this resource manages.

An `ExternalSecret` may bind several secrets to one Kubernetes secret. Where it does, it may only reference a single `SecretStore`. For details, see [binding multiple secrets](https://external-secrets.io/latest/guides/getallsecrets/).
