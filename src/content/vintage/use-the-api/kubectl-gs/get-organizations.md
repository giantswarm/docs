---
linkTitle: get organizations
title: "'kubectl gs get organizations' command reference"
description: Reference documentation on how to list organizations and get details for a single organization using 'kubectl gs'.
weight: 50
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-organizations/
  - /ui-api/kubectl-gs/get-organizations/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I list organizations in the management API using kubectl?
  - How can I inspect organizations using kubectl?
last_review_date: 2023-09-14
---

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, an organization in this case, or list several of them.

The command is an improvement over `kubectl get organizations`, for several reasons. First, it is usable by all users who have access to the management API, not only admins, as it does not require permission to list Organization resources on the cluster scope. Second, it provides slightly more details in the list output.

## Usage

### Get a list of organizations {#list}

Execute

```nohighlight
kubectl gs get organizations
```

to list some information on all organizations available to you in the current installation.

Note: The command also has a shorter version and can be executed as `kubectl gs get orgs`.

Here is some example output:

```nohighlight
NAME                  ORG NAMESPACE             AGE
acme                  org-acme                  20d
conformance-testing   org-conformance-testing   185d
giantswarm            org-giantswarm            489d
multi-project         org-multi-project         379d
```

### Get specific organization

When used with an organization name as additional argument, the command will show details for a single organization. Example:

```nohighlight
kubectl gs get organizations acme
```

Note: As an alternative to `get organizations`, `get organization`, `get orgs` and `get org` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `NAME`: Name of the organization.
- `ORG NAMESPACE`: Namespace created for the organization
- `AGE`: How long ago was the organization created.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get organizations` command. Use `kubectl gs get organizations --help` for a full list.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get organizations` is no different.
Similar to other `get` subcommands, you can specify the output format of `kubectl gs get organizations` using the `--output` flag.

#### YAML output {#yaml}

To inspect an organization's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for organization `acme`.

```nohighlight
kubectl gs get organizations acme --output yaml
```

When applied without an organization name argument, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get organizations --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: security.giantswarm.io/v1alpha1
  kind: Organization
...
```

## Related

- [`kubectl gs login`]({{< relref "/vintage/use-the-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
