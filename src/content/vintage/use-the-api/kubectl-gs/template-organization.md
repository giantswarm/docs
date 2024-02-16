---
linkTitle: template organization
title: "'kubectl gs template organization' command reference"
description: Reference documentation on how to create a manifest for an organization using 'kubectl gs'.
weight: 110
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /use-the-api/kubectl-gs
  - /reference/kubectl-gs/template-organization/
  - /ui-api/kubectl-gs/template-organization/
last_review_date: 2024-01-18
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an organization manifest for the Management API?
---
The `template organization` command creates an [organization]({{< relref "/vintage/platform-overview/multi-tenancy/index.md" >}})
manifest which can be applied to a management cluster, e. g. via `kubectl apply`.
The manifest will define an [`Organization`]({{< relref "/vintage/use-the-api/management-api/crd/organizations.security.giantswarm.io.md" >}})
resource (API group/version `security.giantswarm.io/v1alpha1`).

## Usage

The command to execute is `kubectl gs template organization`.

It supports the following required flag:

- `--name` - Organization name.
- `--output` - Output file path. If not set, output is written to STDOUT.

Example command:

```nohighlight
kubectl gs template organization \
  --name example-organization
```

## Output

As a result, the command will produce a YAML document of the `Organization` resource.

The following example illustrates the output generated:

```yaml
apiVersion: security.giantswarm.io/v1alpha1
kind: Organization
metadata:
  name: example-organization
spec: {}
status: {}
```
