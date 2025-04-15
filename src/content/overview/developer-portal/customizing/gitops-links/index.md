---
title: Enabling GitOps links
linkTitle: GitOps links
description: How to configure the developer portal to show GitOps links for resources managed by Flux, so that users can jump directly to the source code.
weight: 20
menu:
  principal:
    parent: overview-developer-portal-customizing
    identifier: overview-developer-portal-customizing-gitopslinks
last_review_date: 2025-04-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I have links to GitOps sources in the developer portal?
---

The developer portal can be configured to show links to the GitOps source code for resources managed by [Flux](https://fluxcd.io/). This is useful for users who want to quickly jump to the source code of a resource, and who want to check which revision of the source code is currently applied in the cluster.

![Screenshot showing a GitOps indicator with link](./gitops-link.png)

The screenshot above shows an example of how the GitOps indicator may appear in the developer portal. The source link is only shown if the developer portal is configured like explained below to provide according links.

## How the developer portal detects GitOps resources

To detect that a cluster, for example, is managed by Flux, the developer portal looks for `kustomize.toolkit.fluxcd.io/name` and `kustomize.toolkit.fluxcd.io/namespace` labels in the cluster's defining App resource. This information is already sufficient to show the GitOps indicator in the developer portal, however it is not enough to provide a link to the source code.

## How the developer portal finds the GitOps source

The name and namespace combination found in the App resource (see above) points to a Kustomization (`kustomize.toolkit.fluxcd.io/v1`) resource in the cluster. This Kustomization usually has a `.spec.sourceRef` pointing to a GitRepository (`source.toolkit.fluxcd.io/v1`) resource. Also a `.spec.path` field is set to indicate the path in the Git repository for which this Kustomization is responsible.

This GitRepository resource has a `.spec.url` field that contains the URL of the Git repository where the source code is stored. In addition, the GitRepository provides a commit reference (or similar, e. g. a branch or tag) in the `.status.artifact.revision` field.

The combination of these details (URL, path, and commit/tag/branch reference), can be used to create a link displayed in the user interface, if the configuration is set up correctly as explained below.

### Example

Partial example of a Kustomization resource:

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: demotech-gitops
  namespace: default
spec:
  path: ./management-clusters/gazelle
  sourceRef:
    kind: GitRepository
    name: demotech-gitops
```

Partial example of a GitRepository resource:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: demotech-gitops
  namespace: default
spec:
  url: ssh://git@github.com/demotechinc/demotech-gitops
status:
  artifact:
    revision: main@sha1:299de19645659b14421992d059b6c2435486694d
```

## Configuration

In order to provide links which end users can use to navigate to the source of a GitOps resource, we need two things:

1. Understand the URL found in the GitRepository resource. This is configured using the `gitRepositoryUrlPattern` field.
2. The URL pattern used by the source code management system UI (for example GitHub, GitLab, Bitbucket) that we want to link to. To be configured via the `targetUrl` field.

The Giant Swarm Backstage plugin allows you to specify any number of combinations of the two above in the `app-config.yaml` file under the `gs.gitopsRepositories` section, to handle a variety of different cases.

### `gitRepositoryUrlPattern`

With this field, you specify a regular expression (ECMAScript/JavaScript flavour) used to extract values from the GitRepository's `.spec.url` property. The names of the capturing groups (for example: `HOSTNAME`, `PROJECT_NAME`) allow to reference the matched parts when creating a link URL via the according `targetUrl` template.

For example, to parse the URL `ssh://git@github.com/demotechinc/demotech-gitops`, you could configure the following regex:

```nohighlight
^ssh:\/\/git@(?<HOSTNAME>github.+?)\/(?<REPO_PATH>.+?)(\.git)?$
```

[Try this regex in regex101.com](https://regex101.com/r/KGnXQg/1)

As a result, the `HOSTNAME` group will contain `github.com`, and the `REPO_PATH` group will contain `demotechinc/demotech-gitops`.

### `targetUrl`

With the `targetUrl` field you specify how to create a link URL based on the parts captured via the regex `gitRepositoryUrlPattern` (see above) and additional details (path and revision).

Using the example regex above, you could use `${{HOSTNAME}}` and `${{REPO_PATH}}` in your URL template. In addition, you can use the following details independent of the regex:

- `${{PATH}}`: Directory path in the source repository. The value is taken from `.spec.path` field of the corresponding Kustomization resource.
- `${{REVISION}}`: Revision reference. The value is taken from the `.status.artifact.revision` field of the corresponding GitRepository resource.

As an example, given the `gitRepositoryUrlPattern` regex example above, the following `targetUrl` could be used to create a link to the GitHub UI:

```nohighlight
https://${{HOSTNAME}}/${{REPO_PATH}}/blob/${{REVISION}}/${{PATH}}
```

The resulting URL would look like this:

```nohighlight
https://github.com/demotechinc/demotech-gitops/blob/299de19645659b14421992d059b6c2435486694d/management-clusters/gazelle
```

## Default Configuration

By default, the system is pre-configured with two GitHub repository patterns. These defaults are hardcoded into the system and are always applied, even if no `gitopsRepositories` configuration is provided in the `app-config.yaml` file. The default entries are:

- **Default GitHub (SSH):**

  ```yaml
  gitRepositoryUrlPattern: '^ssh:\/\/git@(ssh\.)?(?<HOSTNAME>github.+?)(:443)?\/(?<REPO_PATH>.+?)(\.git)?$'
  targetUrl: 'https://${{HOSTNAME}}/${{REPO_PATH}}/blob/${{REVISION}}/${{PATH}}'
  ```

- **Default GitHub (HTTPS):**

  ```yaml
  gitRepositoryUrlPattern: '^https:\/\/(?<HOSTNAME>github.+?)\/(?<REPO_PATH>.+?)$'
  targetUrl: 'https://${{HOSTNAME}}/${{REPO_PATH}}/blob/${{REVISION}}/${{PATH}}'
  ```

These default patterns ensure that links to GitHub repositories can be generated out of the box without requiring any additional configuration.

When custom `gitopsRepositories` entries are provided in the `app-config.yaml` file, they are appended to the default GitHub configurations. The system evaluates all entries (default and custom) in the order they are defined, and the first matching entry is used to generate the link.

## Full example

In this section we demonstrate how a complete configuration could look like, covering a variety of cases and different source code management systems.

Backstage `app-config.yaml` snippet, configuring two additional pairs of `gitRepositoryUrlPattern` and `targetUrl`:

```yaml
gs:
  gitopsRepositories:
    # BitBucket
    - gitRepositoryUrlPattern: '^https:\/\/(?<HOSTNAME>bitbucket.+?)\/scm\/(?<PROJECT_NAME>.+?)\/(?<REPO_NAME>.+?)(\.git)?$'
      targetUrl: 'https://${{HOSTNAME}}/projects/${{PROJECT_NAME}}/repos/${{REPO_NAME}}/browse/${{PATH}}?at=${{REVISION}}'

    # GitLab
    - gitRepositoryUrlPattern: '^ssh:\/\/git@(?<HOSTNAME>gitlab.+?)\/(?<REPO_PATH>.+?)(\.git)?$'
      targetUrl: 'https://${{HOSTNAME}}/${{REPO_PATH}}/-/tree/${{REVISION}}/${{PATH}}'
```

Note that with multiple entries, the first matching entry is used to create a link, so the order of the entries is important. In this case, the system will first evaluate the default GitHub configurations, followed by the custom Bitbucket and GitLab configurations.

See below how this applies to different repository URLs.

### BitBucket

Given a repository URL of `https://bitbucket.example.net/scm/some-project/gitops-repo.git`, a path `dir/subdir`, and a revision of `1234567890`, the resulting link is:

```nohighlight
https://bitbucket.example.net/projects/some-project/repos/gitops-repo/browse/dir/subdir?at=1234567890
        --------------------           ------------       -----------        ----------    ----------
             HOSTNAME                  PROJECT_NAME        REPO_NAME           PATH        REVISION
```

### GitLab

With a repository URL `ssh://git@gitlab.example.com/myorg/gitops-repo.git`, a path `dir/subdir`, and a revision of `1234567890`, the resulting link is:

```nohighlight
https://gitlab.example.com/myorg/gitops-repo/-/tree/1234567890/dir/subdir
        ------------------ -----------------        ---------- ----------
             HOSTNAME          REPO_PATH             REVISION     PATH
```

### GitHub

With repository URLs such as

- `ssh://git@github.example.com:443/myorg/gitops-repo.git`
- `ssh://git@github.example.com/myorg/gitops-repo`
- `https://github.example.com/myorg/gitops-repo`  

and a path `dir/subdir`, and a revision of `1234567890`, the URL becomes:

```nohighlight
https://github.example.com/myorg/gitops-repo/blob/1234567890/dir/subdir
        ------------------ -----------------      ---------- ----------
             HOSTNAME          REPO_PATH           REVISION     PATH
```
