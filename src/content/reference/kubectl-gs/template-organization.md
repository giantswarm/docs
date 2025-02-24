---
linkTitle: template organization
title: "'kubectl gs template organization' command reference"
description: Reference documentation on how to create a manifest for an organization using 'kubectl gs'.
weight: 110
menu:
  principal:
    parent: reference-kubectlgs
last_review_date: 2024-11-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an organization manifest for the platform API?
aliases:
  - /vintage/use-the-api/kubectl-gs/template-organization/
---
The `template organization` command creates an [organization]({{< relref "/overview/fleet-management/multi-tenancy" >}})
manifest which can be applied to a management cluster, e. g. via `kubectl apply`.
The manifest will define an [`Organization`]({{< relref "/reference/platform-api/crd/organizations.security.giantswarm.io.md" >}})
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
