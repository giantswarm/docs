---
linkTitle: Platform Security
title: Platform Security
description: Architecture and configuration information for the collection of security related platform features.
weight: 30
menu:
  main:
    parent: platform-overview-security
aliases:
  - /developer-platform/security/
  - /app-platform/apps/security/
#   - /guides/managed-security-stack/
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
last_review_date: 2022-03-15
user_questions:
  - How do I view and manage vulnerabilities in my cluster?
  - What UI options are there for vulnerability and policy reports?
  - What is included in the Security Pack?
  - How do I enforce admission policies in my cluster?
  - What can I do to keep my clusters secure?
  - What security services and tools does Giant Swarm offer?
---

## Overview

Giant Swarm integrates a collection of open-source security tools which extend the basic security considerations outlined in our [RBAC and PSP tutorial][rbac-psp], [Network Policy tutorial][net-pols], and [security guide][security] and help you gain deeper observability and control over your developer platform.

The stack consists of multiple distinct components which are independently installable and configurable based on the user's security requirements.

| Feature | Component | State | Source(s) |
|---|---|---|---|
| Image Scanning | Trivy + Starboard | In Catalog | [Trivy][trivy-app] / [Starboard][starboard-app]  |
| Policy Enforcement | Kyverno | In Catalog | [Kyverno][kyverno-app]  |
| CIS Benchmarks | Starboard | In Catalog | [Starboard][starboard-app]  |
| Image Provenance | Cosign + Fulcio | Planned |   |
| Cloud Security Posture | Cloud Custodian | Planned |   |
| Runtime Anomalies | Falco | In Catalog | [Falco][falco-app]  |
| In-Cluster Registry | Harbor | In Catalog | [Harbor][harbor-app]  |
| Log Alerting | Supported by our [managed Observability Stack][observability-stack] offering. | In Catalog | [Loki][loki-app]  |
| Log Shipping + Storage | Supported by our [managed EFK Stack][efk-stack] offering. | In Catalog | [EFK Stack][efk-app]  |
| Advanced Network Capabilities* | Supported by our managed Connectivity Stack offering. | In Catalog | [Linkerd][linkerd-app] / [Linkerd CNI][linkerd-cni-app] / [Linkerd Visualization][linkerd-viz-app]  |

\* mTLS, DNS-based egress policies, and other advanced network capabilities are available through a separately-managed service mesh.

Components with a state of "In Catalog" are available for installation via our [App Platform][app-platform]. We are working to improve centralized installation and configuration across components.

A high-level overview of each component is included below. Please refer to the GitHub repository for each individual app for more detailed technical information.

## Trivy

Trivy is a vulnerability scanner created by [Aqua Security][trivy-upstream]. It can be run as a command-line tool (for example, in a CI/CD pipeline) or as a Kubernetes operator, which we deploy from our [Trivy App][trivy-app]. When running as an operator, Trivy can be used as the scanning backend for a Harbor container registry as well as the scanner used by Starboard.

Within our managed security stack, Trivy is deployed in-cluster as the backend for Starboard and Harbor (if in use). We also recommend customers enable vulnerability scanning in their CI/CD pipelines and include support for that integration as part of our managed offering.

## Starboard

Starboard is another open-source project developed by [Aqua Security][starboard-upstream]. Starboard runs as an operator (deployed from our [Starboard App][starboard-app]) and performs several ongoing functions in the cluster, including scanning Pods for vulnerabilities, running Kubernetes CIS benchmarks with [`kube-bench`][kube-bench], and auditing Kubernetes resources against best practices and other policies using [Polaris][polaris]. These functions can all be configured independently. Though not required, Starboard can use an existing Trivy server running in the cluster as its vulnerability scanner. Starboard stores the results of its scans inside the cluster as Kubernetes custom resources.

In our stack, we deploy Starboard alongside Trivy in the cluster to initiate vulnerability scans for running Pods and to perform CIS benchmarks. Users may also choose to enable Polaris configuration scans in addition to our recommended Kyverno policy enforcement. To support monitoring and better observability of the scan results, we have also created a [custom Prometheus exporter][starboard-exporter] which reads the `VulnerabilityReport` and `CISKubeBenchReport` custom resources created by Starboard and exposes the data as Prometheus metrics.

### Working with Starboard Scan Results

The authoritative source of truth for Starboard scans are the in-cluster custom resources. However, scan results, especially `VulnerabilityReport`s, can be lengthy and difficult to read.

There are several available options for viewing and distilling the results of Starboard scans as well as UI integrations to make them easier to work with.

Scan data can be accessed:

- using `kubectl`
- from the Starboard Grafana dashboard
- directly in Prometheus
- using the [Starboard extension for K8s Lens][lens-extension]
- using the [Starboard plugin for Octant][octant-plugin]
- using the [Trivy extension for VS Code][vscode-trivy] (for working with Trivy scans offline)

#### Using kubectl

Authoritative scan results are stored in the cluster and can be retrieved using `kubectl`:

```bash
$ kubectl get vulnerabilityreport -n argocd
NAME                                       REPOSITORY      TAG            SCANNER   AGE
...
replicaset-argocd-redis-74d8c6db65-redis   library/redis   6.2.4-alpine   Trivy     23d
replicaset-argocd-redis-759b6bc7f4-redis   library/redis   6.2.1-alpine   Trivy     23d
...
```

To see detailed vulnerability information, `describe` the resource or use `get -o yaml`, for example:

```bash
$ kubectl describe vulnerabilityreport -n argocd replicaset-argocd-redis-74d8c6db65-redis
Name:         replicaset-argocd-redis-74d8c6db65-redis
Namespace:    argocd
Labels:       pod-spec-hash=94c6f9fbb
              starboard.container.name=redis
              starboard.resource.kind=ReplicaSet
              starboard.resource.name=argocd-redis-74d8c6db65
              starboard.resource.namespace=argocd
Annotations:  <none>
API Version:  aquasecurity.github.io/v1alpha1
Kind:         VulnerabilityReport
Report:
  Artifact:
    Repository:  library/redis
    Tag:         6.2.4-alpine
  Registry:
    Server:  index.docker.io
  Scanner:
    Name:     Trivy
    Vendor:   Aqua Security
    Version:  0.19.2
  Summary:
    Critical Count:  3
    High Count:      2
    Low Count:       0
    Medium Count:    0
    Unknown Count:   0
  Update Timestamp:  2021-10-30T03:09:37Z
  Vulnerabilities:
    ...
```

Kubernetes CIS benchmark reports can similarly be retrieved with `$ kubectl get ciskubebenchreport -A` and `kubectl describe`.

### Reporting and Monitoring

For convenience, data from the in-cluster CRs is exported to Prometheus, where it can be queried, used for alerting, or included in dashboards.

![Diagram illustrating the flow of data from Starboard's scan through an exporter to Prometheus and Grafana](Starboard-Scanning-Monitoring.svg)

Data flow:

1. Starboard scans a Pod.
2. Starboard creates a `VulnerabilityReport` CR.
3. `starboard-exporter` reads the `VulnerabilityReport` CR and exposes metrics.
4. Prometheus scrapes the metrics from `starboard-exporter`. Data can then be queried in Prometheus or seen in the Grafana vulnerability dashboard.

## Kyverno

Kyverno is a [CNCF project][kyverno-upstream] originally created by Nirmata which acts as an admission controller and enforces policies for Kubernetes resources. It loads policies from Kubernetes custom resources and similarly stores reports about policy violations as additional resources within the cluster. It can be used to enforce a wide range of policies including Kubernetes best practices and Pod Security Standards (PSS), as well as custom user-defined policies.

As part of the security offering, Kyverno provides enforcement for PSS policies and image signing as well as custom policies provided by customers using the stack.

Policy violations are stored in `PolicyReport` CRs and exposed as Prometheus metrics via [policy-reporter][policy-reporter-upstream]. You can retrieve the reports via `kubectl`:

```bash
$ kubectl get polr -A
NAMESPACE          NAME                       PASS   FAIL   WARN   ERROR   SKIP   AGE
argocd             polr-ns-argocd             35     1      0      0       0      14d
default            polr-ns-default            9      0      0      0       0      14d
flux-system        polr-ns-flux-system        54     0      0      0       0      14d
hello-world        polr-ns-hello-world        0      0      0      0       0      6d23h
kube-system        polr-ns-kube-system        0      0      0      0       0      14d
monitoring         polr-ns-monitoring         185    5      0      0       0      14d
replex-k8s-agent   polr-ns-replex-k8s-agent   9      0      0      0       0      14d
```

Simply `kubectl get -o yaml` a report to see detailed information about the policies in place as well as any recorded violations. Reports can also be visualized through the included web UI by port forwarding it to your local machine:

```bash
$ kubectl port-forward service/kyverno-ui 8080:8080 -n <kyverno namespace>
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
...
```

Open your browser to `localhost:8080` to view the reports.

## Falco

Falco is a [CNCF project][falco-upstream] originally created by Sysdig which enables rule-based detection of runtime anomalies in a container or on a host Node. Falco watches Linux system calls (syscalls) for events matching a predefined set of suspicious or malicious activities, for example the reading of a sensitive file or the execution of a shell inside a container.

We include Falco in our managed security stack as a detection mechanism for malicious activity once a Pod has already started. It is deployed from our [Falco App][falco-app], which includes helper components for exposing Prometheus metrics and forwarding events to various other channels, such as Elasticsearch and various messages queues and alerting backends.

[app-platform]: {{< relref "/platform-overview/app-platform/overview" >}}
[efk-app]: https://github.com/giantswarm/efk-stack-app/
[efk-stack]: {{< relref "/platform-overview/observability/elastic-stack" >}}
[falco-app]: https://github.com/giantswarm/falco-app
[falco-upstream]: https://github.com/falcosecurity/falco
[harbor-app]: https://github.com/giantswarm/harbor-app
[kube-bench]: https://github.com/aquasecurity/kube-bench
[kyverno-app]: https://github.com/giantswarm/kyverno-app
[kyverno-upstream]: https://github.com/kyverno/kyverno/
[lens-extension]: https://github.com/aquasecurity/starboard-lens-extension
[linkerd-app]: https://github.com/giantswarm/linkerd2-app
[linkerd-cni-app]: https://github.com/giantswarm/linkerd2-cni-app
[linkerd-viz-app]: https://github.com/giantswarm/linkerd-viz-app
[loki-app]: https://github.com/giantswarm/loki-app
[net-pols]: {{< relref "/getting-started/network-policies" >}}
[polaris]: https://github.com/FairwindsOps/polaris
[policy-reporter-upstream]: https://github.com/kyverno/policy-reporter
[observability-stack]: {{< relref "/platform-overview/observability" >}}
[octant-plugin]: https://github.com/aquasecurity/starboard-octant-plugin
[rbac-psp]: {{< relref "/getting-started/rbac-and-psp" >}}
[security]: {{< relref "/platform-overview/security/" >}}
[starboard-app]: https://github.com/giantswarm/starboard-app
[starboard-exporter]: https://github.com/giantswarm/starboard-exporter/
[starboard-upstream]: https://github.com/aquasecurity/starboard
[trivy-app]: https://github.com/giantswarm/trivy-app/
[trivy-upstream]: https://github.com/aquasecurity/trivy
[vscode-trivy]: https://github.com/aquasecurity/trivy-vscode-extension [The nginx-ingress-controller helm chart on Github](https://github.com/giantswarm/nginx-ingress-controller-app)
