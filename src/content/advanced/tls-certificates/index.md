---
linkTitle: TLS certificates with cert-manager
title: Obtaining TLS certificates for Ingresses with cert-manager
description: Configure cert-manager to automatically obtain TLS certificates for Ingresses.
weight: 20
menu:
  main:
    parent: advanced
user_questions:
  - How do I install cert-manager?
  - How do I obtain TLS certificates?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2022-07-19
---

Exposing HTTP services using an Ingress is a pretty straightforward task in Kubernetes. Using plain HTTP is, however, discouraged in favor of using HTTPS. `cert-manager` provides a simple, declarative way to automatically obtain TLS certificates for the endpoints we expose.

Our App Platform provides a [`cert-manager-app`](https://github.com/giantswarm/cert-manager-app) that users can install. By default, `cert-manager` creates a `ClusterIsser` using the HTTP challenge. This works fine for obtaining certificates in most cases. However, not creating the default issuer and instead creating a custom one solving DNS challenges is required for pure internal environments or for issuing wildcard certificates. In other words: generally, it is not needed to disable the creation of the default issuer. However, if needed, you can disable its creation by providing the following user values:

```yaml
global:
  giantSwarmClusterIssuer:
    install: false
```

Then, it is possible to create a new `ClusterIssuer` that solves DNS challenges. For instance, on Azure:

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-giantswarm
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: test@customer.com
    privateKeySecretRef:
      name: letsencrypt-giantswarm
    solvers:
    - dns01:
        azureDNS:
          subscriptionID: subscription-id
          resourceGroupName: cluster-id
          hostedZoneName: cluster-id.k8s.installation.region.provider.gigantic.io
```

Finally, we can simply create an Ingress. It is important to specify the correct `spec.ingressClassName` (which will likely be either `nginx` or `nginx-internal`) and `spec.tls` fields.

An example Ingress would look like this:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test
  annotations:
    kubernetes.io/tls-acme: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - test.cluster.k8s.installation.region.provider.gigantic.io
    secretName: test-tls
  rules:
  - host: test.cluster.k8s.installation.region.provider.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: hello-world-service
            port:
              number: 8080
```

It is also possible to obtain wildcard certificates, which can be useful in some cases. Please note that wildcard certificates can only be obtained via a DNS challenge such as the one set up in this example - they can _not_ be obtained via HTTP challenges.

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: wildcard
spec:
  commonName: "*.cluster.k8s.installation.region.provider.gigantic.io"
  dnsNames:
  - "*.cluster.k8s.installation.region.provider.gigantic.io"
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: letsencrypt-giantswarm
  secretName: wildcard-tls
```

this certificate can then be used by setting the following `spec.tls` field in an Ingress:

```yaml
spec:
  tls:
  - hosts:
    - example.cluster.k8s.installation.region.provider.gigantic.io
    secretName: wildcard-tls
```

In this case, since we are using an already existing certificate, remember to remove the `kubernetes.io/tls-acme: "true"` annotation from the Ingress.
