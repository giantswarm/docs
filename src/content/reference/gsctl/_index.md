+++
title = "gsctl Reference"
description = "Documentation on gsctl, the Giant Swarm command line utility to create and delete clusters, create key pairs and more."
date = "2018-09-11"
layout = "subsection"
weight = 10
+++

# `gsctl` Reference

gsctl is the command line utility to manage your Giant Swarm clusters.

## Commands {#commands}

Follow the links below for detailed documentation, where available. You can also always use `gsctl <command> --help`.

| Command                               | Description
|---------------------------------------|------------
| `create cluster`                      | [Create a new cluster](create-cluster/)
| `create keypair`                      | [Create and download new key pair](create-keypair/)
| `create kubeconfig`                   | [Create/download new key pair and update `kubectl` configuration](create-kubeconfig/)
| `delete cluster`                      | [Delete cluster](delete-cluster/)
| `info`                                | [Print information on status, configuration, and the installation](info/)
| `list endpoints`                      | [List endpoints](list-endpoints/)
| `list clusters`                       | [List clusters](list-clusters/)
| `list organizations`                  | List organizations
| `list keypairs`                       | [List key pairs](list-keypairs/)
| `list releases`                       | [List releases](list-releases/)
| `login`                               | [Sign in as a user](login/)
| `logout`                              | Sign out
| `ping`                                | Check API connection
| `scale cluster`                       | [Add or remove worker nodes of a cluster](scale-cluster/)
| `select endpoint`                     | [Select an endpoint](select-endpoint/)
| `show cluster`                        | [Show cluster details](show-cluster/)
| `update organization set-credentials` | [Set provider credentials for an organization](update-org-set-credentials/)
| `version`                             | Print version number


## Installing and Updating {#install}

`gsctl` comes as a self-contained binary for Mac, Linux, and Windows. Below you find installation instructions for different platforms. If you want to build `gsctl` from source, find everything you need in its [GitHub repository](https://github.com/giantswarm/gsctl).

The current `gsctl` version is **{{% gsctl_version %}}**. Find details in the [release notes](https://github.com/giantswarm/gsctl/releases/tag/{{% gsctl_version %}}).

<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#install-mac-brew" data-toggle="tab">Mac OS (Homebrew)</a></li>
  <li role="presentation"><a href="#install-mac" data-toggle="tab">Mac OS</a></li>
  <li role="presentation"><a href="#install-linux" data-toggle="tab">Linux</a></li>
  <li role="presentation"><a href="#install-win-scoop" data-toggle="tab">Windows (scoop)</a></li>
  <li role="presentation"><a href="#install-win" data-toggle="tab">Windows</a></li>
</ul>

<div class="tab-content clearfix">
<div class="tab-pane active" id="install-mac-brew">

  <p>Homebrew provides the most convenient way to install <code>gsctl</code> and keep it up to date. To install, use this command:</p>

  <pre><code class="language-nohighlight">brew tap giantswarm/giantswarm
brew install gsctl</code></pre>

  <p>For updating:</p>

  <pre><code class="language-nohighlight">brew upgrade gsctl</code></pre>

</div>
<div class="tab-pane" id="install-mac">

  <p>Execute the commands below to install the latest released version. The same commands work for upgrading from a previously installed version.</p>

  <pre><code class="language-nohighlight">curl -O https://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-darwin-amd64.tar.gz
tar xzf gsctl-{{% gsctl_version %}}-darwin-amd64.tar.gz
sudo cp gsctl-{{% gsctl_version %}}-darwin-amd64/gsctl /usr/local/bin/</code></pre>

</div>
<div class="tab-pane" id="install-linux">

  <p>Execute the commands below to install the latest released version. The same commands work for upgrading from a previously installed version.</p>

  <pre><code class="language-nohighlight">curl -O https://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-linux-amd64.tar.gz
tar xzf gsctl-{{% gsctl_version %}}-linux-amd64.tar.gz
sudo cp gsctl-{{% gsctl_version %}}-linux-amd64/gsctl /usr/local/bin/</code></pre>

</div>
<div class="tab-pane" id="install-win-scoop">

  <p><a href="http://scoop.sh/" target="_blank">scoop</a> enables convenient installs and updates for Windows PowerShell users. Before you can install <code>gsctl</code> for the first time, execute this:</p>

  <pre><code class="language-nohighlight">scoop bucket add giantswarm https://github.com/giantswarm/scoop-bucket.git</code></pre>

  <p>To install:</p>

  <pre><code class="language-nohighlight">scoop install gsctl</code></pre>

  <p>To update:</p>

  <pre><code class="language-nohighlight">scoop update gsctl</code></pre>
</div>
<div class="tab-pane" id="install-win">

  <ul>
    <li>Download the <a href="https://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-windows-amd64.zip">64 bit</a> or <a href="https://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-windows-386.zip">32 bit</a> version of <code>gsctl</code> for Windows</li>
    <li>Copy the contained <code>gsctl.exe</code> to a convenient location that's in your <code>%PATH%</code>, or add the <code>gsctl.exe</code> location to your <code>%PATH%</code></li>
  </ul>

</div>
</div>

## Configuration {#configuration}

`gsctl` keeps it's own settings under `$HOME/.config/gsctl/`. There is a [configuration file](configuration-file) called `config.yaml`. Key pairs are stored in the `certs` subdirectory.

The following environment variables can be used to affect some behaviour:

- `GSCTL_ENDPOINT`: This can be used to specify an API endpoint URL.
- `GSCTL_CAFILE`: If your Giant Swarm API endpoint uses a certificate signed by an authority not known to your operating system, this variable can be set to the path of a custom CA (certification authority) bundle. A CA bundle is a text file containing one or more CA certificates in PEM format.
- `GSCTL_CAPATH`: Similar to `GSCTL_CAFILE`, but `GSCTL_CAPATH` is expected to point to a directory containing one or more PEM files.
- `GSCTL_DISABLE_COLORS`: When this variable is set to any non-empty string, all terminal output will be monochrome.
- `GSCTL_DISABLE_CMDLINE_TRACKING`: When this variable is set to any non-empty string, command lines won't be submitted to the API. Otherwise command lines are submitted to learn about the tool's usage and find ways to improve.

In addition, [global command-line options](global-options/) are available.

## Known Bugs and Limitations {#known-limitations}

Check our [issues](https://github.com/giantswarm/gsctl/issues?q=is%3Aopen+is%3Aissue+label%3Akind%2Fbug) with label `kind/bug`.

## Changelog {#changelog}

You'll find info on changes in the [release description](https://github.com/giantswarm/gsctl/releases).

## Feedback {#feedback}

We welcome your feedback on `gsctl`. If you feel like sharing openly, use the GitHub repository and create an [issue](https://github.com/giantswarm/gsctl/issues), so other users can participate. Otherwise please use the common Giant Swarm support channels.
