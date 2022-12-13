---
linkTitle: add encryption
title: "'kubectl gs gitops add encryption' command reference"
description: Reference documentation on how to configure encryption for the GitOps repository.
weight: 40
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2022-09-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I configure encryption for the GitOps repository?
---

This command configures encryption for the GitOps repository.

## Prerequisites

Your GitOps repository should provide the following structural layers:

- Basic structure (see [`init`]({{< relref "/use-the-api/kubectl-gs/gitops/init" >}}))
- Management cluster (see [`add management-cluster`]({{< relref "/use-the-api/kubectl-gs/gitops/add-mc" >}}))
- Organization (see [`add organization`]({{< relref "/use-the-api/kubectl-gs/gitops/add-org" >}}))
- Workload cluster (see [`add workload-cluster`]({{< relref "/use-the-api/kubectl-gs/gitops/add-wc" >}}))
- Apps (see [`add app`]({{< relref "/use-the-api/kubectl-gs/gitops/add-app" >}}))

## Description

The structure created by this command is presented below. Resources enclosed in a square brackets `[]` are considered optional.

```nohighlight
.
├── .sops.yaml
└── management-clusters
    ├── [MC_NAME.yaml]
    ├── .sops.keys
    │   ├── [MC_NAME.KEY_FINGERPRINT.asc]
    │   └── [WC_NAME.KEY_FINGERPRINT.asc]
    ├── secrets
    │   ├── [MC_NAME.gpgkey.enc.yaml]
    │   └── [WC_NAME.gpgkey.enc.yaml]
    └── organizations
        └── ORG_NAME
            └── workload-clusters
                └── [WC_NAME.yaml]
```

Encryption can be configured for multiple layers of the repository depending on the set of the flags passed to the command.
As stated in the [init command]({{< relref "/use-the-api/kubectl-gs/gitops/init" >}}), the `kubectl-gs` does not perform encryption on behalf of the user, hence user is
obliged to run the `sops` binary on his own. The command will however instruct user of how to import the public key into his
keychain.

## Usage

Basic command syntax: `kubectl gs gitops add encryption FLAGS`

### Flags

- `--generate` -- generate new key pair (required)
- `--management-cluster` -- management cluster to configure the encryption for (required)
- `--organization` -- organization in the management cluster to configure the encryption for
- `--target` -- relative directory to configure the encryption for (default "secrets/")
- `--workload-cluster` -- workload cluster in the Organization to configure the encryption for

{{% kubectl_gs_gitops_common_flags %}}


### Examples

In each of the examples below it is assumed the `protected-dir` directory exists at the layer being configured.

{{< tabs >}}
{{< tab id="mc-enc" title="Management Cluster" >}}

```nohighlight
kubectl gs gitops add encryption \
  --local-path /tmp/gitops-demo \
  --generate \
  --management-cluster demomc \
  --target protected-dir \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/.sops.keys/demomc.25c90481570b4a46176dc453f7bf506e0ad50d47.asc
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GopenPGP 2.4.8
Comment: https://gopenpgp.org

xjMEYw9EiBYJKwYBBAHaRw8BAQdAOgoOLS0o+rQZRfCj8FzUu0FnshqYcbNwkP1y
ho+SZEjNEmRlbW9tYyBGbHV4IG1hc3RlcsKMBBMWCAA+BQJjD0SICZD3v1BuCtUN
RxYhBCXJBIFXC0pGF23EU/e/UG4K1Q1HAhsDAh4BAhkBAwsJBwIVCAMWAAICIgEA
AKonAQDN5iNQmp9fT4BMKT8B7tAnmE3J0VBHkIW1zDTM0q5NHwEA6Ui7UVF4pSc5
4ayCGD0f7u+kQyQIN8Frs6pg43/iEgrOOARjD0SIEgorBgEEAZdVAQUBAQdAce+j
c36NrdwiggksgoEf5h/zwz94XbEe/rPh0Dk+1ikDAQoJwngEGBYIACoFAmMPRIgJ
kPe/UG4K1Q1HFiEEJckEgVcLSkYXbcRT979QbgrVDUcCGwwAABA9AP0bj+wt+bVc
TmFWSIdjoKZ2ODvLKDyIYWfj2LlVdcBdnAD/aqZpGYu73pqV3jmW7/eCg2betERa
l4tii6CxXhmtEgs=
=rRlD
-----END PGP PUBLIC KEY BLOCK-----


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/demomc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-gitops
  namespace: default
spec:
  decryption:
    provider: sops
    secretRef:
      name: sops-gpg-master
  interval: 1m
  path: ./management-clusters/demomc
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/.sops.yaml
creation_rules:
- encrypted_regex: ^(data|stringData)$
  path_regex: management-clusters/demomc/protected-dir/.*\.enc\.yaml
  pgp: 25c90481570b4a46176dc453f7bf506e0ad50d47

/tmp/gitops-demo/management-clusters/demomc/secrets/demomc.gpgkey.enc.yaml
apiVersion: v1
data:
  demomc.25c90481570b4a46176dc453f7bf506e0ad50d47.asc: LS0tLS1CRUdJTiBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tLQpWZXJzaW9uOiBHb3BlblBHUCAyLjQuOApDb21tZW50OiBodHRwczovL2dvcGVucGdwLm9yZwoKeFZjRVl3OUVpQllKS3dZQkJBSGFSdzhCQVFkQU9nb09MUzBvK3JRWlJmQ2o4RnpVdTBGbnNocVljYk53a1AxeQpobytTWkVnQUFQWWd4VDEyNVcxVThkSnIrWXNOemlRMTl0aEM2eUh6RE9tUUhwZEZkRUErRUpyTkVtUmxiVzl0Cll5QkdiSFY0SUcxaGMzUmxjc0tNQkJNV0NBQStCUUpqRDBTSUNaRDN2MUJ1Q3RVTlJ4WWhCQ1hKQklGWEMwcEcKRjIzRVUvZS9VRzRLMVExSEFoc0RBaDRCQWhrQkF3c0pCd0lWQ0FNV0FBSUNJZ0VBQUtvbkFRRE41aU5RbXA5ZgpUNEJNS1Q4Qjd0QW5tRTNKMFZCSGtJVzF6RFRNMHE1Tkh3RUE2VWk3VVZGNHBTYzU0YXlDR0QwZjd1K2tReVFJCk44RnJzNnBnNDMvaUVnckhYUVJqRDBTSUVnb3JCZ0VFQVpkVkFRVUJBUWRBY2UramMzNk5yZHdpZ2drc2dvRWYKNWgvend6OTRYYkVlL3JQaDBEaysxaWtEQVFvSkFBRC9SSE5TSWk5M3E1T2RTck9vZjdSbzVFRTUrVUV0b0dGMwpITmpRMUsyNFlRQVFoc0o0QkJnV0NBQXFCUUpqRDBTSUNaRDN2MUJ1Q3RVTlJ4WWhCQ1hKQklGWEMwcEdGMjNFClUvZS9VRzRLMVExSEFoc01BQUFRUFFEOUc0L3NMZm0xWEU1aFZraUhZNkNtZGpnN3l5ZzhpR0ZuNDlpNVZYWEEKWFp3QS8ycW1hUm1MdTk2YWxkNDVsdS8zZ29ObTNyUkVXcGVMWW91Z3NWNFpyUklMCj12UGtGCi0tLS0tRU5EIFBHUCBQUklWQVRFIEtFWSBCTE9DSy0tLS0t
kind: Secret
metadata:
  name: sops-gpg-master


Please run

gpg --import /tmp/gitops-demo/management-clusters/demomc/.sops.keys/demomc.25c90481570b4a46176dc453f7bf506e0ad50d47.asc

to load the public key into the keychain for SOPS to work.
```

{{< /tab >}}
{{< tab id="org-enc" title="Organization" >}}

```nohighlight
kubectl gs gitops add encryption \
  --local-path /tmp/gitops-demo \
  --generate \
  --management-cluster demomc \
  --organization demoorg \
  --target protected-dir \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/.sops.keys/demomc.5286137ee4a4890c0cae093a3df892dbc5f532ca.asc
-----BEGIN PGP PUBLIC KEY BLOCK-----
Comment: https://gopenpgp.org
Version: GopenPGP 2.4.8

xjMEYw9FYhYJKwYBBAHaRw8BAQdA0k0ggz15z4Ce2BnW/T2Wqm4IGRiAHSPVuQM9
kesHghvNH2RlbW9vcmcgT3JnYW5pemF0aW9uIGVuY3J5cHRpb27CjAQTFggAPgUC
Yw9FYgmQPfiS28X1MsoWIQRShhN+5KSJDAyuCTo9+JLbxfUyygIbAwIeAQIZAQML
CQcCFQgDFgACAiIBAADZsAD5AYhpEIEwmVORSCoPaLLgJWDvfkYQF4ZGFCLSBijv
N/cBAKsmsW2itWtBOAw117kW2HSIb8PtEM2mGczhj0HzWJAJzjgEYw9FYhIKKwYB
BAGXVQEFAQEHQIKwqhsEZ1uUcG145ss+EgeT+JzmgKoVOuXpyNeNeB1zAwEKCcJ4
BBgWCAAqBQJjD0ViCZA9+JLbxfUyyhYhBFKGE37kpIkMDK4JOj34ktvF9TLKAhsM
AABIqwD+JZtCM0e1diCgQrD29HXMFeiJMk4CZ+4BXm4GoIqA8bkBAIxxdWFJRFfA
xlzSVtnIuti5D38GFBmPf5a90osTT/QD
=eC2r
-----END PGP PUBLIC KEY BLOCK-----


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/secrets/demomc.gpgkey.enc.yaml
apiVersion: v1
data:
  demomc.5286137ee4a4890c0cae093a3df892dbc5f532ca.asc: LS0tLS1CRUdJTiBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tLQpWZXJzaW9uOiBHb3BlblBHUCAyLjQuOApDb21tZW50OiBodHRwczovL2dvcGVucGdwLm9yZwoKeFZnRVl3OUZZaFlKS3dZQkJBSGFSdzhCQVFkQTBrMGdnejE1ejRDZTJCblcvVDJXcW00SUdSaUFIU1BWdVFNOQprZXNIZ2hzQUFQNDk4RC9GamlRbjNtcnJmb2NmbzhuczU4eVdka056VGdubU41WU9yd3RGNUJFbnpSOWtaVzF2CmIzSm5JRTl5WjJGdWFYcGhkR2x2YmlCbGJtTnllWEIwYVc5dXdvd0VFeFlJQUQ0RkFtTVBSV0lKa0QzNGt0dkYKOVRMS0ZpRUVVb1lUZnVTa2lRd01yZ2s2UGZpUzI4WDFNc29DR3dNQ0hnRUNHUUVEQ3drSEFoVUlBeFlBQWdJaQpBUUFBMmJBQStRR0lhUkNCTUpsVGtVZ3FEMml5NENWZzczNUdFQmVHUmhRaTBnWW83emYzQVFDckpyRnRvclZyClFUZ01OZGU1RnRoMGlHL0Q3UkROcGhuTTRZOUI4MWlRQ2NkZEJHTVBSV0lTQ2lzR0FRUUJsMVVCQlFFQkIwQ0MKc0tvYkJHZGJsSEJ0ZU9iTFBoSUhrL2ljNW9DcUZUcmw2Y2pYalhnZGN3TUJDZ2tBQVA5M3RBQkR0WHlRZHE0awptak1yZ1I3bzEvRHpHNm4wSzRTc29hM2o5TmxoQUJJaHduZ0VHQllJQUNvRkFtTVBSV0lKa0QzNGt0dkY5VExLCkZpRUVVb1lUZnVTa2lRd01yZ2s2UGZpUzI4WDFNc29DR3d3QUFFaXJBUDRsbTBJelI3VjJJS0JDc1BiMGRjd1YKNklreVRnSm43Z0ZlYmdhZ2lvRHh1UUVBakhGMVlVbEVWOERHWE5KVzJjaTYyTGtQZndZVUdZOS9scjNTaXhOUAo5QU09Cj1jZzdUCi0tLS0tRU5EIFBHUCBQUklWQVRFIEtFWSBCTE9DSy0tLS0t
kind: Secret
metadata:
  name: sops-gpg-master

/tmp/gitops-demo/management-clusters/demomc/demomc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-gitops
  namespace: default
spec:
  decryption:
    provider: sops
    secretRef:
      name: sops-gpg-master
  interval: 1m
  path: ./management-clusters/demomc
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/.sops.yaml
creation_rules:
- encrypted_regex: ^(data|stringData)$
  path_regex: management-clusters/demomc/organizations/demoorg/protected-dir/.*\.enc\.yaml
  pgp: 5286137ee4a4890c0cae093a3df892dbc5f532ca


Please run

gpg --import /tmp/gitops-demo/management-clusters/demomc/.sops.keys/demomc.5286137ee4a4890c0cae093a3df892dbc5f532ca.asc

to load the public key into the keychain for SOPS to work.
```

{{< /tab >}}
{{< tab id="wc-enc" title="Workload Cluster" >}}

```nohighlight
kubectl gs gitops add encryption \
  --local-path /tmp/gitops-demo \
  --generate \
  --management-cluster demomc \
  --organization demoorg \
  --workload-cluster demowc \
  --target protected-dir \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/.sops.keys/demowc.5ee3687ce2ef2ee94dc671d11483c46dbf667bf2.asc
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GopenPGP 2.4.8
Comment: https://gopenpgp.org

xjMEYw9F4hYJKwYBBAHaRw8BAQdANFNtpzEPlOd/ZxepXa+ofhI6TpB2Mdu1U+zc
gdq0G7HNImRlbW93YyBXb3JrbG9hZCBDbHVzdGVyIGVuY3J5cHRpb27CjAQTFggA
PgUCYw9F4gmQFIPEbb9me/IWIQRe42h84u8u6U3GcdEUg8Rtv2Z78gIbAwIeAQIZ
AQMLCQcCFQgDFgACAiIBAADyCQEAt43DEMnf9BsSSWTy5nSncYKygMuNXck+Ddcs
wGe4QcoBAMhgJvwJpiWcOszsSp7/34TBAtvOcATuVmRFKMHM8Q4PzjgEYw9F4hIK
KwYBBAGXVQEFAQEHQLrToOfOf+6R8bwfWCINpLhZhQXyfiHDqb9r05vk7kBfAwEK
CcJ4BBgWCAAqBQJjD0XiCZAUg8Rtv2Z78hYhBF7jaHzi7y7pTcZx0RSDxG2/Znvy
AhsMAACE2wD/SfCSxE5yPB/RdwdhZSdbXBHDdnB5pMh653Xwaj+SgPYA/iPTolJV
OhnEQXue/wpeFDYg7fzq0vXnZX4sdoLCSVIG
=5Fcp
-----END PGP PUBLIC KEY BLOCK-----


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/secrets/demowc.gpgkey.enc.yaml
apiVersion: v1
data:
  demowc.5ee3687ce2ef2ee94dc671d11483c46dbf667bf2.asc: LS0tLS1CRUdJTiBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tLQpWZXJzaW9uOiBHb3BlblBHUCAyLjQuOApDb21tZW50OiBodHRwczovL2dvcGVucGdwLm9yZwoKeFZnRVl3OUY0aFlKS3dZQkJBSGFSdzhCQVFkQU5GTnRwekVQbE9kL1p4ZXBYYStvZmhJNlRwQjJNZHUxVSt6YwpnZHEwRzdFQUFQc0hLVDl6TEUwdVQ1ZkNua1ZmUCtkb2FhbmhYVks5c0lvSXh6cXc4aWg1cUErSnpTSmtaVzF2CmQyTWdWMjl5YTJ4dllXUWdRMngxYzNSbGNpQmxibU55ZVhCMGFXOXV3b3dFRXhZSUFENEZBbU1QUmVJSmtCU0QKeEcyL1pudnlGaUVFWHVOb2ZPTHZMdWxOeG5IUkZJUEViYjltZS9JQ0d3TUNIZ0VDR1FFREN3a0hBaFVJQXhZQQpBZ0lpQVFBQThna0JBTGVOd3hESjMvUWJFa2xrOHVaMHAzR0Nzb0RMalYzSlBnM1hMTUJudUVIS0FRRElZQ2I4CkNhWWxuRHJNN0VxZS85K0V3UUxiem5BRTdsWmtSU2pCelBFT0Q4ZGRCR01QUmVJU0Npc0dBUVFCbDFVQkJRRUIKQjBDNjA2RG56bi91a2ZHOEgxZ2lEYVM0V1lVRjhuNGh3Nm0vYTlPYjVPNUFYd01CQ2drQUFQOU05b2Urd2FzcQpVb3dTYWVsMGIvVzdXa09kdkdkV2Y0cjZFSzFLSjlmeUNCR213bmdFR0JZSUFDb0ZBbU1QUmVJSmtCU0R4RzIvClpudnlGaUVFWHVOb2ZPTHZMdWxOeG5IUkZJUEViYjltZS9JQ0d3d0FBSVRiQVA5SjhKTEVUbkk4SDlGM0IyRmwKSjF0Y0VjTjJjSG1reUhybmRmQnFQNUtBOWdEK0k5T2lVbFU2R2NSQmU1Ny9DbDRVTmlEdC9PclM5ZWRsZml4Mgpnc0pKVWdZPQo9ckRoVgotLS0tLUVORCBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tLQ==
kind: Secret
metadata:
  name: sops-gpg-demowc

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  decryption:
    provider: sops
    secretRef:
      name: sops-gpg-demowc
  interval: 1m
  path: ./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
  postBuild:
    substitute:
      cluster_name: demowc
      cluster_release: 1.0.0
      default_apps_release: 2.0.0
      organization: demoorg
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/.sops.yaml
creation_rules:
- encrypted_regex: ^(data|stringData)$
  path_regex: management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/protected-dir/.*\.enc\.yaml
  pgp: 5ee3687ce2ef2ee94dc671d11483c46dbf667bf2


Please run

gpg --import /tmp/gitops-demo/management-clusters/demomc/.sops.keys/demowc.5ee3687ce2ef2ee94dc671d11483c46dbf667bf2.asc

to load the public key into the keychain for SOPS to work.
```

{{< /tab >}}
{{< /tabs >}}

Remove the `--dry-run` flag and re-run it to apply the changes.
