---
linkTitle: Getting started
title: Getting started with Linkerd
description: TBD
last_review_date: 2023-04-03
weight: 10
menu:
  main:
    parent: service-mesh
user_questions:
  - How can I install a Service Mesh on my cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

## Installation

### Preparing your cluster

For security reasons Giant Swarm by default forbids the usage of emptyDir volumes as storage for pods. Linkerd needs this functionality to run the proxy containers in any deployment that is going to be included in the service mesh. Enabling emptyDir volumes poses a risk that a pod will create such big emptyDir that the underlying cluster node will run out of disk space. If you're OK with this potential issue, the easiest way to allow for emptyDir for all the deployments is to edit the default PSP of your workload cluster by running the command:

```
kubectl patch psp restricted --type='json' -p='[{"op": "add", "path": "/spec/volumes/-", "value": "emptyDir"}]'
```

### Ceritificates

To successful install Linkerd you will require to generate a trust anchor and issuer certificate. The following steps loosely follow the official instructions.

Obtain the step cli (you can download the binaries from [here](https://github.com/smallstep/cli/releases/tag/v0.23.4)) and execute the following commands. 
Take note of the --not-after flag. We recommend 10 years (87600h) for the trust anchor and 3 years (26280h) for the issuer certificate.

```
step certificate create root.linkerd.cluster.local ca.crt ca.key --profile root-ca --no-password --insecure --not-after=87600h
step certificate create identity.linkerd.cluster.local issuer.crt issuer.key --profile intermediate-ca --not-after=26280h --no-password --insecure --ca ca.crt --ca-key ca.key
```
Finally construct your user secrets file by filling this template and saving it as my-linkerd-certificates.yaml:

```
apps:
  linkerd-control-plane:
    userConfig:
      secret:
        values: |
          identity:
            issuer:
              tls:
                crtPEM: |
                keyPEM: |
          identityTrustAnchorsPEM: |
```

### App installation

We recommend deploying linkerd using the `linkerd-bundle`, which includes `linkerd2-cni`, `linkerd-control-plane` and `linkerd-viz` by default. You can apply the following App CR (Custom Resource) onto your management cluster to start with a minimal configuration.

```
apiVersion: v1
stringData:
  values: |
    clusterID: <your-cluster-id>
    organization: <your-org>
    apps:
      linkerd-control-plane:
        userConfig:
          secret:
            values: | 
              identity:
                issuer:
                  tls:
                    crtPEM: |
                      <contents of the issuer.crt file>
                    keyPEM: |
                      <contents of the issuer.key file>
              identityTrustAnchorsPEM: |
                <contents of the ca.crt file>
kind: Secret
metadata:
  name: <your-cluster-id>-linkerd-bundle-user-values
  namespace: <your-cluster-id>
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app.kubernetes.io/name: linkerd-bundle
    app-operator.giantswarm.io/version: 0.0.0
  name: <your-cluster-id>-linkerd-bundle
  namespace: <your-cluster-id>
spec:
  catalog: giantswarm-playground
  kubeConfig:
    inCluster: true
  name: linkerd-bundle
  namespace: <your-cluster-id>
  userConfig:
    secret:
      name: <your-cluster-id>-linkerd-bundle-user-values
      namespace: <your-cluster-id>
  version: 0.3.0
```

You can find more configuration examples [here](https://github.com/giantswarm/linkerd-bundle/tree/main/examples).

## Workload configuration

### Mesh your apps

After installation, linkerd looks for a `linkerd.io/inject: enabled` annotation on Namespaces or other workload resources. Adding this annotation to your workload namespaces will trigger automatic proxy container injection to your pods. You can use the spec.namespaceConfig.annotations field of your other apps App CR to automatically apply the required annotation.

More information on proxy injection can be found on the "Automatic Proxy Injection" page in the upstream documentation.

Attention: Proxy containers are using EmptyDir volumes for storing ephemeral data, so all of your workload pods meshed by linkerd require a PodSecurityPolicy which allows use of EmptyDir volumes.

## Further reading

- [Linkerd Official documentation](https://linkerd.io/2.12/overview/)
- [Automatic Proxy Injection](https://linkerd.io/2.12/features/proxy-injection/)
- [linkerd Bundle](https://github.com/giantswarm/linkerd-bundle)
- [linkerd2-cni App](https://github.com/giantswarm/linkerd2-cni-app)
- [linkerd-control-plane App](https://github.com/giantswarm/linkerd-control-plane-app)
- [linkerd-viz App](https://github.com/giantswarm/linkerd-viz-app)
