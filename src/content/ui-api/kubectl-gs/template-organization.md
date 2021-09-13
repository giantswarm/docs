---
linkTitle: template organization
title: "'kubectl gs template organization' command reference"
description: Reference documentation on how to create a manifest for an organization using 'kubectl gs'.
weight: 80
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-organization/
last_review_date: 2021-09-09
owner:
  - https://github.com/orgs/giantswarm/teams/team-biscuit
user_questions:
  - How can I create an organization manifest for the Management API?
---

# `kubectl gs template organization`

In order to create an [organization]({{< relref "/general/organizations/index.md" >}}) using a custom resource, `kubectl-gs` will help you create the manifest for the resource type:

- [`Organization`]({{< relref "/ui-api/management-api/crd/organizations.security.giantswarm.io.md" >}}) (API group/version `security.giantswarm.io/v1alpha1`) - holds the base organization specification.

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
