---
linkTitle: TLS certificates for ingress
title: Obtaining TLS certificates for ingress traffic
description: Configure cert-manager to automatically obtain TLS certificates for ingress traffic
weight: 50
menu:
  principal:
    parent: tutorials-security
    identifier: tutorials-security-rbac
user_questions:
  - How do I obtain TLS certificates?
last_review_date: 2024-12-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

Exposing `HTTP` services using an [`Ingress` resource]({{< relref "/tutorials/connectivity/ingress/exposing-workloads" >}}) is a pretty straightforward task in `Kubernetes`. However, you should always make sure that the traffic is encrypted. Relying on `cert-manager` provides a simple approach to obtain declaratively TLS certificates automatically.

Our [app platform]({{< relref "/overview/fleet-management/app-management/" >}}) provides a [`cert-manager-app`](https://github.com/giantswarm/cert-manager-app) that users can install. By default, `cert-manager` creates a `ClusterIssuer` using the `HTTP` challenge. It works fine for obtaining certificates in most cases. However, not creating the default issuer and instead creating a custom one solving DNS challenges is required for pure internal environments or for issuing wildcard certificates. In other words: it is not needed to disable the creation of the default issuer. However, if needed, you can disable its creation by providing the following user values:

```yaml
global:
  install: false
```

Then, it is possible to create a new `ClusterIssuer` that solves `DNS` challenges. The following example shows how to create a for Azure and AWS:

{{< tabs >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2">}}

You need to create a user in AWS IAM with a IAM policy that allows the user to manage Route53 records like the following:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "route53:GetChange",
        "route53:ChangeResourceRecordSets",
        "route53:GetHostedZone"
      ],
      "Resource": "arn:aws:route53:::hostedzone/*"
    },
    {
      "Effect": "Allow",
      "Action": "route53:ListHostedZonesByName",
      "Resource": "*"
    }
  ]
}
```

Then create a `Secret` with the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: route53-credentials-secret
type: Opaque
stringData:
  access-key: AWS_ACCESS_KEY_ID
  secret-access-key: AWS_SECRET_ACCESS_KEY
```

Finally, create the `ClusterIssuer`:

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod-dns
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: email@example.com
    privateKeySecretRef:
      name: letsencrypt-giantswarm
    solvers:
    - dns01:
        route53:
          region: AWS_REGION
          hostedZoneID: HOSTED_ZONE_ID
          accessKeyID: AWS_ACCESS_KEY_ID
          secretAccessKeySecretRef:
            name: route53-credentials-secret
            key: secret-access-key
      selector:
        dnsZones:
        - "{cluster-name}.installation.region.provider.gigantic.io"
```

{{< /tab >}}
{{< tab id="cluster-capz-azure-vms" for-impl="capz_vms">}}

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
          hostedZoneName: cluster-id.installation.region.provider.gigantic.io
```

{{< /tab >}}
{{< /tabs >}}

Finally, you can simply create an `Ingress` resource that contains the `tls` configuration like below:

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

__Note__: It is important to specify the correct `spec.ingressClassName` (which will likely be either `nginx` or `nginx-internal`) and `spec.tls` fields.

It is also possible to obtain wildcard certificates, which can be useful in some cases. Please note that wildcard certificates can only be obtained via a `DNS` challenge such as the one set up in this example - they can _not_ be obtained via `HTTP` challenges.

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

this certificate can then be used by setting the following `spec.tls` field in an `Ingress`resource:

```yaml
spec:
  tls:
  - hosts:
    - example.cluster.k8s.installation.region.provider.gigantic.io
    secretName: wildcard-tls
```

__Note__: In this case, since you are using an already existing certificate, remember to remove the `kubernetes.io/tls-acme: "true"` annotation from the `Ingress` resource.

If you want to learn more about [`Ingress` connectivity]({{< relref "/tutorials/connectivity/ingress/" >}}), please check our tutorials.
