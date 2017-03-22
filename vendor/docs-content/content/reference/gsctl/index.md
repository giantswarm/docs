+++
title = "gsctl Reference"
description = "Documentation on gsctl, the Giant Swarm command line utility"
date = "2016-12-01"
type = "page"
weight = 10
+++

# `gsctl` Reference

## Command Reference {#commands}

- `create`: Create things, like kubectl configuration, or key-pairs
- `info`: Print some information
- `list`: List things, like organizations, clusters, key-pairs
- `login`: Sign in as a user
- `logout`: Sign the current user out
- `ping`: Check API connection
- `version`: Print version number

Check `gsctl <command> --help` for details.

## Installing and Updating {#install}

`gsctl` comes as a self-contained binary for Mac, Linux, and Windows. Below you find installation instructions for different platforms. If you want to build `gsctl` from source, find everything you need in its [GitHub repository](https://github.com/giantswarm/gsctl).

The current `gsctl` version is **{{% gsctl_version %}}**. Find details in the [release notes](https://github.com/giantswarm/gsctl/releases/tag/{{% gsctl_version %}}).

<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#install-mac-brew" data-toggle="tab">Mac OS (Homebrew)</a></li>
  <li role="presentation"><a href="#install-mac" data-toggle="tab">Mac OS</a></li>
  <li role="presentation"><a href="#install-linux" data-toggle="tab">Linux</a></li>
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

  <pre><code class="language-nohighlight">curl -O http://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-darwin-amd64.tar.gz
tar xzf gsctl-{{% gsctl_version %}}-darwin-amd64.tar.gz
sudo cp gsctl-{{% gsctl_version %}}-darwin-amd64/gsctl /usr/local/bin/</code></pre>

</div>
<div class="tab-pane" id="install-linux">

  <p>Execute the commands below to install the latest released version. The same commands work for upgrading from a previously installed version.</p>

  <pre><code class="language-nohighlight">curl -O http://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-linux-amd64.tar.gz
tar xzf gsctl-{{% gsctl_version %}}-linux-amd64.tar.gz
sudo cp gsctl-{{% gsctl_version %}}-linux-amd64/gsctl /usr/local/bin/</code></pre>

</div>
<div class="tab-pane" id="install-win">

  <ul>
    <li>Download the <a href="http://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-windows-amd64.zip">64 bit</a> or <a href="http://downloads.giantswarm.io/gsctl/{{% gsctl_version %}}/gsctl-{{% gsctl_version %}}-windows-386.zip">32 bit</a> version of <code>gsctl</code> for Windows</li>
    <li>Copy the contained <code>gsctl.exe</code> to a convenient location that's in your <code>%PATH%</code>, or add the <code>gsctl.exe</code> location to your <code>%PATH%</code></li>
  </ul>

</div>
</div>

## Configuration {#configuration}

`gsctl` keeps it's own settings under `$HOME/.gsctl/config.yaml`. Note that manual changes to this file will likely be overwritten.

Additionally, the following environment variables can be used:

- `GSCTL_DISABLE_COLORS`: When this variable is set to any non-empty string, all terminal output will be monochrome.
- `GSCTL_DISABLE_CMDLINE_TRACKING`: When this variable is set to any non-empty string, command lines won't be submitted to the API. Otherwise command lines are submitted to learn about the tool's usage and find ways to improve.

## Known Bugs and Limitations {#known-limitations}

- [gsctl#7](https://github.com/giantswarm/gsctl/issues/7): No colored output on Windows
- Not all API responses (error cases) are handled properly. If you experience a "Unknown Status code" or similar error message, please report this [in an issue](https://github.com/giantswarm/gsctl/issues/new). Thanks!
- Check our [issues](https://github.com/giantswarm/gsctl/issues?q=is%3Aopen+is%3Aissue+label%3Akind%2Fbug) for more

## Changelog {#changelog}

You'll find info on changes in the [release description](https://github.com/giantswarm/gsctl/releases).

## Feedback {#feedback}

We welcome your feedback on `gsctl`. If you feel like sharing openly, use the GitHub repository and create an [issue](https://github.com/giantswarm/gsctl/issues), so other users can participate. Otherwise please use the common Giant Swarm support channels.
