+++
title = "Installing the Giant Swarm CLI"
description = "A detailed description of how to install Giant Swarm client software on various platforms"
date = "2015-02-01"
type = "page"
weight = 10
+++

# Installing the Giant Swarm CLI

<p class="lead">Instructions for installing the `swarm` command line interface on the supported platforms. By the way, the latest version is <strong>{{% cli_latest_version %}}</strong>.</p>

## Mac OS X

If you're on a Mac, the recommended way to install the `swarm` command line interface (CLI) is to use [Homebrew](http://brew.sh/).

Once Homebrew is set up, these commands will install the latest swarm <abbr title="command line interface">CLI</abbr> in your PATH.

```nohighlight
$ brew tap giantswarm/swarm
$ brew install swarm-client
```

In order to update the swarm <abbr title="command line interface">CLI</abbr> to the latest version, use these commands: 

```nohighlight
$ brew update
$ brew upgrade swarm-client
```

## Linux

Please note that the `swarm` <abbr title="command line interface">CLI</abbr> requires a 64 bit system.

First, download the tarball and unpack it:

```nohighlight
$ curl -O http://downloads.giantswarm.io/swarm/clients/{{% cli_latest_version %}}/swarm-{{% cli_latest_version %}}-linux-amd64.tar.gz
$ tar xzf swarm-{{% cli_latest_version %}}-linux-amd64.tar.gz
```

We recommend to make the `swarm` binary available in your PATH by copying it to a directory that's already contained in your PATH. For example:

```nohighlight
$ sudo cp swarm /usr/local/bin/
```

## Next steps

* [The Annotated Hello World Example](/guides/annotated-helloworld/): A quick check that everything is working fine
* [Your First Application - in Your Language](/guides/your-first-application/): Learn how to create your first application on Giant Swarm on your prefered technology
