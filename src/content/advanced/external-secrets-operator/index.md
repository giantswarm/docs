---
title: External Secrets Operator
linkTitle: External Secrets Operator
description: External Secrets Operator is a managed application within our platform and this is what you need to know.
weight: 20
menu:
user_questions:
- What is External Secrets Operator?
- How do I use External Secrets Operator?
- What are the risks of running External Secrets Operator?
- What resources does external secrets operator consume on my cluster?
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-03-23
---

## What is External Secrets Operator

External secrets operator (ESO) is a kubernetes operator that reads secrets
from an external source and deliver them securely as kubernetes secrets for
your workloads to consume.

As part of our offering, we make External Secrets Operator available on all
management clusters, and also as a managed application for you to deploy on
your workload clusters.

ESO can be used either alongside, or in place of Mozilla SOPs to bind secrets
into the cluster that may otherwise have required you to commit to source
control or deploy manually to the cluster.

Full documentation on ESO can be found on the website at [https://external-secrets.io/](https://external-secrets.io/)

## Resource requirements

Once running, ESO has a small footprint on your cluster, requiring only the
inclusion of 3 additional pods with a CPU requirement of 300m and a memory
requirement of 1.5GiB.

During the installation process, we require a little more as the CRD installer
pod needs to cache kubernetes resources as part of its deployment.

This may require an additional 1.5GiB of memory to be consumed whilst we
install and upgrade ESO. However, this usage is ephemeral and will be released
back to the cluster as soon as the install job is complete.

## Usage

To begin using ESO, it requires the inclusion of two resources to your cluster.

The first resource that needs to be created is the [`SecretStore`](https://external-secrets.io/v0.8.1/introduction/overview/#secretstore).

The secret store binds ESO to your secret manager, whether that be AWS KMS,
Azure Key Vault, Hashicorp Vault or another of the [many supported secret
providers](https://external-secrets.io/v0.8.1/provider/aws-secrets-manager/).

The second resource that needs to be created is the [`ExternalSecret`](https://external-secrets.io/v0.8.1/api/externalsecret/).
Here, you will bind one or many external secrets to the kubernetes secret that
will be managed by this resource.

It is possible to define multiple `SecretStores` on the cluster which works best
inside a multi-tenant environment where different teams may have different
secret providers, or only have restricted access to part of the secret provider
as may be the case when using Hashicorp Vault Enterprise.

An External Secret may bind one or many secrets to the kubernetes secret however
where this is the case, only a single SecretStore may be referenced in the
ExternalSecret. You can find more information on [binding multiple secrets
here](https://external-secrets.io/v0.8.1/guides/getallsecrets/).

## Installation

ESO can be installed to your workload cluster as a managed app from our
catalogs. There is no special or additional configuration required to install
and it can be installed directly by creating an AppCR against the cluster
using our `GitOps` approach or through our web UI.

### Example AppCR

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

More advanced users may wish to configure specific parts of the values
themselves and can find the application chart at
[https://github.com/giantswarm/external-secrets](https://github.com/giantswarm/external-secrets)

For more information on configuring apps within the Giant Swarm App Platform,
please follow the documentation at
[https://docs.giantswarm.io/getting-started/app-platform/app-configuration/](https://docs.giantswarm.io/getting-started/app-platform/app-configuration/)

### Combining ESO and SOPs

There is no hard and fast rule around you needing to choose one over the other
here. Both ESO and SOPs can happily coexist on the server as long as the
secrets they manage are independant of one another. If you create a secret with
sops, it should not be updated or managed with ESO and vice-versa. In instances
such as these, the two tools would end up "fighting" with each other with no
one tool then becoming the source of truth for that secret.

It may be that you have many secrets currently handled by SOPs and you wish to
migrate them to a different provider; ESO allows you to do that as long as the
provider is in the supported list of providers, and SOPs works to your
advantage here as it's embedded into Flux, providing you with time to migrate
without harming your platform.

### What are the risks of using ESO

With any application there are risks to using it, the primary one here is if ESO
fails for any reason and credentials are rotated in your secret provider whilst
ESO is not running, your applications may fail on deployment or scale.
