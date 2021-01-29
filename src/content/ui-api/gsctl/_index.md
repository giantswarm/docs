---
linkTitle: gsctl
title: gsctl CLI reference
description: Documentation on gsctl, the Giant Swarm command line utility to create and delete clusters, create key pairs and more.
weight: 20
menu:
  main:
    identifier: uiapi-gsctl
    parent: ui-api
# TODO: remove "layout: single" and let the page be rendered by a specific section template.
layout: single
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# gsctl CLI reference

gsctl is the command line utility to manage your Giant Swarm clusters.

## Commands {#commands}

Follow the links below for a detailed documentation, where available. You can also always use `gsctl <command> --help`.

| Command                               | Description
|---------------------------------------|------------
| `completion`                          | Create completion scripts for Bash and Zsh
| `create cluster`                      | [Create a new cluster](create-cluster/)
| `create keypair`                      | [Create and download new key pair](create-keypair/)
| `create kubeconfig`                   | [Create/download new key pair and update `kubectl` configuration](create-kubeconfig/)
| `create nodepool`                     | [Create a new node pool](create-nodepool/)
| `delete cluster`                      | [Delete a cluster](delete-cluster/)
| `delete nodepool`                     | [Delete a node pool](delete-nodepool/)
| `delete endpoint`                     | [Delete endpoint](delete-endpoint/)
| `info`                                | [Print information on status, configuration, and the installation](info/)
| `list endpoints`                      | [List endpoints](list-endpoints/)
| `list clusters`                       | [List clusters](list-clusters/)
| `list organizations`                  | List organizations
| `list keypairs`                       | [List key pairs](list-keypairs/)
| `list nodepools`                      | [List node pools](list-nodepools/)
| `list releases`                       | [List workload cluster releases](list-releases/)
| `login`                               | [Sign in as a user](login/)
| `logout`                              | Sign out
| `ping`                                | Check API connection
| `scale cluster`                       | [Add or remove worker nodes of a cluster](scale-cluster/)
| `select endpoint`                     | [Select an endpoint](select-endpoint/)
| `show cluster`                        | [Show cluster details](show-cluster/)
| `show nodepool`                       | [Show node pool details](show-nodepool/)
| `show release`                        | [Show details on a workload cluster release](show-release/)
| `update cluster`                      | [Modify cluster details (name, labels)](update-cluster/)
| `update nodepool`                     | [Modify (rename, scale) a node pool](update-nodepool/)
| `update organization set-credentials` | [Set provider credentials for an organization](update-org-set-credentials/)
| `upgrade cluster`                     | [Upgrade a cluster](upgrade-cluster/)

For finding out which version of `gsctl` you currently have installed, and other useful information about the build, use the `gsctl --version` command.

## Installing and updating {#install}

`gsctl` comes as a self-contained binary for Mac, Linux, and Windows. Below you find installation instructions for different platforms. If you want to build `gsctl` from source, find everything you need in its [GitHub repository](https://github.com/giantswarm/gsctl).

<!-- markdownlint-disable no-bare-urls -->
The current `gsctl` version is **{{% gsctl_version %}}**. Find details in the [release notes](https://github.com/giantswarm/gsctl/releases/tag/{{% gsctl_version %}}).
<!-- markdownlint-enable no-bare-urls -->

<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#install-mac" data-toggle="tab">Mac OS</a></li>
  <li role="presentation"><a href="#install-linux" data-toggle="tab">Linux</a></li>
  <li role="presentation"><a href="#install-win" data-toggle="tab">Windows</a></li>
</ul>

<div class="tab-content clearfix">
<div class="tab-pane active" id="install-mac">

  <p>Homebrew provides the most convenient way to install <code>gsctl</code> and keep it up to date. To install, use this command:</p>

  <pre><code class="language-nohighlight">brew tap giantswarm/giantswarm
brew install gsctl</code></pre>

  <p>For updating:</p>

  <pre><code class="language-nohighlight">brew upgrade gsctl</code></pre>

  <p>To install without homebrew, download the latest release <a href="https://github.com/giantswarm/gsctl/releases">from GitHub</a>, unpack the binary and move it to a location covered by your `PATH` environment variable.</p>
</div>
<div class="tab-pane" id="install-linux">

  <h3>Arch Linux</h3>

  <p><code>gsctl</code> can be installed using an AUR helper, such as <code>yay</code> or <code>pacaur</code>:

  <pre><code class="language-nohighlight">yay -S gsctl-bin</code></pre>

  <h3>Other Distributions</h3>

  <p>Download the latest release <a href="https://github.com/giantswarm/gsctl/releases" target="_blank" rel="noreferrer noopener">from GitHub</a>, unpack the binary and move it to a location covered by your `PATH` environment variable.</p>

</div>
<div class="tab-pane" id="install-win">

  <p><a href="https://scoop.sh/" target="_blank" rel="noreferrer noopener">scoop</a> enables convenient installs and updates for Windows PowerShell users. Before you can install <code>gsctl</code> for the first time, execute this:</p>

  <pre><code class="language-nohighlight">scoop bucket add giantswarm https://github.com/giantswarm/scoop-bucket.git</code></pre>

  <p>To install:</p>

  <pre><code class="language-nohighlight">scoop install gsctl</code></pre>

  <p>To update:</p>

  <pre><code class="language-nohighlight">scoop update gsctl</code></pre>

  <p>To install without scoop, download the latest release <a href="https://github.com/giantswarm/gsctl/releases" target="_blank" rel="noreferrer noopener">from GitHub</a>, unpack the binary and move it to a location covered by your `PATH` environment variable.</p>
</div>
</div>

## Configuration {#configuration}

`gsctl` keeps its own settings under `$HOME/.config/gsctl/`. There is a [configuration file](/reference/gsctl/configuration-file/) called `config.yaml`. Key pairs are stored in the `certs` subdirectory.

The following environment variables can be used to affect some behavior:

- `GSCTL_ENDPOINT`: This can be used to specify an API endpoint URL.
- `GSCTL_AUTH_TOKEN`: This can be used to specify an authentication token.
- `GSCTL_CAFILE`: If your Giant Swarm API endpoint uses a certificate signed by an authority not known to your operating system, this variable can be set to the path of a custom CA (certification authority) bundle. A CA bundle is a text file containing one or more CA certificates in PEM format.
- `GSCTL_CAPATH`: Similar to `GSCTL_CAFILE`, but `GSCTL_CAPATH` is expected to point to a directory containing one or more PEM files.
- `GSCTL_DISABLE_COLORS`: When this variable is set to any non-empty string, all terminal output will be monochrome.
- `GSCTL_DISABLE_CMDLINE_TRACKING`: When this variable is set to any non-empty string, command lines won't be submitted to the API. Otherwise, command lines are submitted to learn about the tool's usage and find ways to improve.
- `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` can be used to define proxy server usage as detailed in the [Go net/http ProxyFromEnvironment docs](https://golang.org/pkg/net/http/#ProxyFromEnvironment).

In addition, [global command-line options](global-options/) are available.

## Known bugs and limitations {#known-limitations}

Check our [issues](https://github.com/giantswarm/gsctl/issues?q=is%3Aopen+is%3Aissue+label%3Akind%2Fbug) with label `kind/bug`.

## Changelog {#changelog}

You'll find info on changes in the [release description](https://github.com/giantswarm/gsctl/releases).

## Feedback {#feedback}

We welcome your feedback on `gsctl`. If you feel like sharing openly, use the GitHub repository and create an [issue](https://github.com/giantswarm/gsctl/issues), so other users can participate. Otherwise, please use the common Giant Swarm support channels.
