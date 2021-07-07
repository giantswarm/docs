---
linkTitle: Installation
title: kubectl gs installation
description: How to obtain kubectl gs, the Giant Swarm kubectl plugin and how to keep it up to date.
weight: 10
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/installation/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - Where can I find the Giant Swarm plugin for kubectl?
  - How can I install the Giant Swarm plugin for kubectl?
  - How can I keep the Giant Swarm plugin for kubectl up to date?
  - What is kubectl gs?
  - How can I install kubectl gs?
---

# Installing the kubectl gs plugin

`kubectl-gs` is the Giant Swarm plug-in for `kubectl` with the official plug-in name `gs`.

The latest version is {{% kubectl_gs_version %}}.

The simplest way to manage `kubectl` plug-ins across platforms is using [Krew](https://krew.sigs.k8s.io/). If you don't have Krew installed, check the [Krew installation docs](https://krew.sigs.k8s.io/docs/user-guide/setup/install/) on how to get it installed.

Further down you will also find instructions on installing the plug-in [without Krew](#without-krew) and additional [instructions for WSL2](#windows-subsystem-for-linux-2-wsl2).

## Using Krew

To install the `gs` plug-in, simply execute this command:

```nohighlight
kubectl krew install gs
```

Lastly, let's check that the plug-in is working as it's supposed to.

```nohighlight
kubectl gs
```

You should see information regarding the commands available.

To upgrade to the latest version of the plug-in, use this command:

```nohighlight
kubectl krew upgrade gs
```

## Without Krew

The platform-agnostic description:

1. Download the [latest release](https://github.com/giantswarm/kubectl-gs/releases/latest) archive for your platform
2. Unpack the archive
3. Copy the executable to a location included in your `$PATH`
4. Check if it's working by executing `kubectl gs`

### Linux

```bash
# Determine the latest version
VERSION=$(curl -I -sS https://github.com/giantswarm/kubectl-gs/releases/latest|grep 'location:'|awk -F '/' '{print $NF}'|tr -d '\n'|tr -d '\r')

# Download
wget https://github.com/giantswarm/kubectl-gs/releases/download/${VERSION}/kubectl-gs-${VERSION}-linux-amd64.tar.gz

# Unpack
tar xzf kubectl-gs-${VERSION}-linux-amd64.tar.gz

# Copy to a dir in $PATH
cp kubectl-gs-${VERSION}-linux-amd64/kubectl-gs /usr/local/bin/

# Check
kubectl gs
```

### Mac OS

```bash
# Determine the latest version
VERSION=$(curl -I -sS https://github.com/giantswarm/kubectl-gs/releases/latest|grep 'location:'|awk -F '/' '{print $NF}'|tr -d '\n'|tr -d '\r')

# Download
wget https://github.com/giantswarm/kubectl-gs/releases/download/${VERSION}/kubectl-gs-${VERSION}-darwin-amd64.tar.gz

# Unpack
tar xzf kubectl-gs-${VERSION}-darwin-amd64.tar.gz

# Copy to a dir in $PATH
cp kubectl-gs-${VERSION}-darwin-amd64/kubectl-gs /usr/local/bin/

# Check
kubectl gs
```

## Windows Subsystem for Linux 2 (WSL2)

Follow the Linux installation instructions with or without Krew first. After successfully installing `kubectl-gs` run the following command so that `kubectl gs login` can open your browser.

```bash
sudo ln -s $(which wslview) /usr/local/bin/xdg-open
```
