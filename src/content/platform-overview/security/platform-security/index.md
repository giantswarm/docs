---
linkTitle: Platform Security
title: Platform Security
description: Architecture and configuration information for the collection of security-related platform features.
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
last_review_date: 2023-11-10
user_questions:
  - How do I view and manage vulnerabilities in my cluster?
  - What UI options are there for vulnerability and policy reports?
  - What is included in the Security Bundle?
  - How do I enforce admission policies in my cluster?
  - What can I do to keep my clusters secure?
  - What security services and tools does Giant Swarm offer?
---

## Overview

Giant Swarm integrates a collection of open-source security tools which extend the basic security considerations outlined in our [RBAC and PSS tutorial][rbac-psp], [Network Policy tutorial][net-pols], and [Security Guide][security] and help you gain deeper observability and control over your developer platform.

The stack consists of multiple distinct components which are independently installable and configurable based on the user's security requirements.

| Feature | Component | State | Source(s) |
|---|---|---|---|
| Image Vulnerability Scanning | Trivy + Trivy Operator | In Catalog | [Trivy][trivy-app] / [Trivy Operator][trivy-operator-app]  |
| Policy Enforcement | Kyverno | In Catalog | [Kyverno][kyverno-app]  |
| CIS Benchmarks | Trivy Operator | In Catalog | [Trivy Operator][trivy-operator-app]  |
| Cloud Security Posture | Evaluating | Planned |   |
| Runtime Anomalies | Falco | In Catalog | [Falco][falco-app]  |
| In-Cluster Registry | Harbor | In Catalog | [Harbor][harbor-app]  |
| Log Alerting | Supported by both Falco and our [managed Observability Bundle][observability-bundle] offering. | In Catalog | [Loki][loki-app] / [Falco][falco-app] |
| Log Shipping + Storage | Supported by our [managed Loki][loki-app] offering. | In Catalog | [Loki][loki-app]  |
| Advanced Network Capabilities* | Supported by our managed Connectivity Bundle offering. | In Catalog | [Cilium][cilium-app] / [Linkerd][linkerd-app] / [Linkerd CNI][linkerd-cni-app] / [Linkerd Visualization][linkerd-viz-app]  |
| Image Provenance | Sigstore (`cosign`) | Policies supported |   |

\* mTLS, DNS-based egress policies, and other advanced network capabilities are available through separately-managed components.

Components with a state of "In Catalog" are available for installation via our [App Platform][app-platform]. We are working to improve centralized installation and configuration across components.

A high-level overview of each component is included below. Please refer to the GitHub repository for each individual app for more detailed technical information.

## Trivy

Trivy is a vulnerability scanner created by [Aqua Security][trivy-upstream]. It can be run as a command-line tool (for example, in a CI/CD pipeline) or as a Kubernetes operator, which we deploy from our [Trivy App][trivy-app]. When running as an operator, Trivy can be used as the scanning backend for a Harbor container registry as well as the scanner used by Trivy Operator.

Within our managed security stack, Trivy is deployed in-cluster as the backend for Trivy Operator and Harbor (if in use). We also recommend customers enable vulnerability scanning in their CI/CD pipelines and include support for that integration as part of our managed offering.

## Trivy Operator

Trivy Operator is another open-source project developed by [Aqua Security][trivy-operator-upstream]. It was previously based on an earlier project named Starboard, but has now diverged significantly. As the name suggests, it is an operator (deployed from our [Trivy Operator App][trivy-operator-app]) and performs several continuous functions in the cluster, including scanning Pods for vulnerabilities, running Kubernetes CIS (or NSA) benchmarks, and auditing Kubernetes resources against best practices and other policies. These functions can all be configured independently. Trivy Operator uses an existing Trivy server running in the cluster as its vulnerability scanner, and stores the results of its scans inside the cluster as Kubernetes custom resources.

In our stack, we deploy Trivy Operator alongside Trivy in the cluster to initiate vulnerability scans for running Pods and to perform CIS benchmarks. Users may also choose to enable additional configuration scans in addition to our recommended Kyverno policy enforcement. To support monitoring and better observability of the scan results, we have also created a [custom Prometheus exporter][starboard-exporter] which reads the `VulnerabilityReport` and other custom resources created by Trivy Operator and exposes the data as Prometheus metrics.

### Working with Trivy Operator Scan Results

The authoritative source of truth for Trivy Operator scans are the in-cluster custom resources. However, scan results, especially `VulnerabilityReport`s, can be lengthy and difficult to read.

There are several available options for viewing and distilling the results of Trivy Operator scans as well as UI integrations to make them easier to work with.

Scan data can be accessed:

- using `kubectl`
- from the Trivy Operator Grafana dashboard
- directly in Prometheus
- using the [Trivy Operator extension for K8s Lens][lens-extension]
- using the [Trivy extension for VS Code][vscode-trivy] (for working with Trivy scans offline)

#### Using kubectl

Authoritative scan results are stored in the cluster and can be retrieved using `kubectl`:

```bash
$ kubectl get vulnerabilityreport -n flux-system
NAME                                       REPOSITORY      TAG            SCANNER   AGE
...
replicaset-notification-controller-7f6f8b76c4-manager             giantswarm/fluxcd-notification-controller             v0.33.0                Trivy     5d22h
replicaset-source-controller-76d9b66f5f-manager                   giantswarm/fluxcd-source-controller                   v0.36.1                Trivy     5d23h

...
```

To see detailed vulnerability information, `describe` the resource or use `get -o yaml`, for example:

```bash
$ k describe vulnerabilityreports.aquasecurity.github.io -n flux-system replicaset-source-controller-76d9b66f5f-manager
Name:         replicaset-source-controller-76d9b66f5f-manager
Namespace:    flux-system
Labels:       resource-spec-hash=7b4f847d9b
              starboard-exporter.giantswarm.io/shard-owner=100.64.9.67
              trivy-operator.container.name=manager
              trivy-operator.resource.kind=ReplicaSet
              trivy-operator.resource.name=source-controller-76d9b66f5f
              trivy-operator.resource.namespace=flux-system
Annotations:  trivy-operator.aquasecurity.github.io/report-ttl: 168h0m0s
API Version:  aquasecurity.github.io/v1alpha1
Kind:         VulnerabilityReport
Metadata:
  ...
Report:
  Artifact:
    Repository:  giantswarm/fluxcd-source-controller
    Tag:         v0.36.1
  Registry:
    Server:  index.docker.io
  Scanner:
    Name:     Trivy
    Vendor:   Aqua Security
    Version:  0.40.0
  Summary:
    Critical Count:  0
    High Count:      7
    Low Count:       0
    Medium Count:    10
    None Count:      0
    Unknown Count:   0
  Update Timestamp:  2023-06-28T09:44:08Z
  Vulnerabilities:
    ...
```

Kubernetes CIS benchmark reports can similarly be retrieved with `$ kubectl get ciskubebenchreport -A` and `kubectl describe`.

### Reporting and Monitoring

For convenience, data from the in-cluster CRs is exported to Prometheus, where it can be queried, used for alerting, or included in dashboards.

![Diagram illustrating the flow of data from Trivy Operator's scan through an exporter to Prometheus and Grafana](Starboard-Scanning-Monitoring.svg)

Data flow:

1. Trivy Operator scans a Pod.
2. Trivy Operator creates a `VulnerabilityReport` CR.
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

More detailed information about the use of Kyverno for Pod Security Standards (PSS) policy enforcement, including exception management is available in our separate [policy enforcement documentation][policy-enforcement].

## Falco

Falco is a [CNCF project][falco-upstream] originally created by Sysdig which enables rule-based detection of runtime anomalies in a container or on a host Node. Falco watches Linux system calls (syscalls) for events matching a predefined set of suspicious or malicious activities, for example the reading of a sensitive file or the execution of a shell inside a container.

We include Falco in our managed security stack as a detection mechanism for malicious activity once a Pod has already started. It is deployed from our [Falco App][falco-app], which includes helper components for exposing Prometheus metrics and forwarding events to various other channels, such as Elasticsearch and various messages queues and alerting backends.

[app-platform]: {{< relref "/platform-overview/app-platform" >}}
[cilium-app]: https://github.com/giantswarm/cilium-app/
[falco-app]: https://github.com/giantswarm/falco-app
[falco-upstream]: https://github.com/falcosecurity/falco
[harbor-app]: https://github.com/giantswarm/harbor-app
[kube-bench]: https://github.com/aquasecurity/kube-bench
[kyverno-app]: https://github.com/giantswarm/kyverno-app
[kyverno-upstream]: https://github.com/kyverno/kyverno/
[lens-extension]: https://github.com/aquasecurity/trivy-operator-lens-extension
[linkerd-app]: https://github.com/giantswarm/linkerd2-app
[linkerd-cni-app]: https://github.com/giantswarm/linkerd2-cni-app
[linkerd-viz-app]: https://github.com/giantswarm/linkerd-viz-app
[loki-app]: https://github.com/giantswarm/loki-app
[net-pols]: {{< relref "/getting-started/network-policies" >}}
[policy-enforcement]: {{< relref "/advanced/security/security-policy-enforcement" >}}
[policy-reporter-upstream]: https://github.com/kyverno/policy-reporter
[observability-bundle]: {{< relref "/platform-overview/observability" >}}
[rbac-psp]: {{< relref "/getting-started/rbac-and-psp" >}}
[security]: {{< relref "/platform-overview/security/" >}}
[starboard-exporter]: https://github.com/giantswarm/starboard-exporter/
[trivy-app]: https://github.com/giantswarm/trivy-app/
[trivy-upstream]: https://github.com/aquasecurity/trivy
[trivy-operator-app]: https://github.com/giantswarm/trivy-operator-app
[trivy-operator-upstream]: https://github.com/aquasecurity/trivy-operator
[vscode-trivy]: https://github.com/aquasecurity/trivy-vscode-extension
[ingress-nginx-app]: (https://github.com/giantswarm/ingress-nginx-app)
