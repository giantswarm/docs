---
linkTitle: Installation
title: Installing kubectl-gs
description: How to obtain kubectl gs, the Giant Swarm kubectl plugin, how to keep it up to date, and where to find the Docker image.
weight: 10
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /use-the-api/kubectl-gs
  - /reference/kubectl-gs/installation/
  - /ui-api/kubectl-gs/installation/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-12-21
user_questions:
  - Where can I find the Giant Swarm plugin for kubectl?
  - How can I install the Giant Swarm plugin for kubectl?
  - How can I keep the Giant Swarm plugin for kubectl up to date?
  - How can I install kubectl-gs?
  - Is there an official Docker image for kubectl-gs?
---

`kubectl-gs` is the Giant Swarm plug-in for `kubectl` with the official plug-in name `gs`.

## Install using Krew

The simplest way to manage `kubectl` plug-ins across platforms is using [Krew](https://krew.sigs.k8s.io/). If you don't have Krew installed, check the [Krew installation docs](https://krew.sigs.k8s.io/docs/user-guide/setup/install/) on how to get it installed.

To install the `kubectl-gs` plug-in, execute this command:

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

## Install manually (without Krew)

{{< tabs >}}
{{< tab id="unix" title="Linux/macOS">}}

1. Download the release package by going to the [latest kubectl-gs release](https://github.com/giantswarm/kubectl-gs/releases/latest) and selecting the right package for your architecture:

    - Linux and Intel/AMD-based processor – filename ends with `linux-amd64.tar.gz`
    - Linux and ARM processor – filename ends with `linux-arm64.tar.gz`
    - macOS and Intel-based processor – filename ends with `darwin-amd64.tar.gz`
    - macOS and ARM processor (M1, M2, M3, and newer) – filename ends with `darwin-arm64.tar.gz`

2. Unpack the downloaded package

    ```nohighlight
    tar xzf kubectl-gs-*.tar.gz
    ```

3. Copy the executable into a directory included in your `PATH`

    ```nohighlight
    sudo cp kubectl-gs-*/kubectl-gs /usr/local/bin/.
    ```

{{< /tab >}}
{{< tab id="windows-amd64" title="Windows">}}

1. Download the release package by going to the [latest kubectl-gs release](https://github.com/giantswarm/kubectl-gs/releases/latest) and selecting the package filename ending with `windows-amd64.zip`.

2. Extract the downloaded ZIP file

3. Copy `kubectl-gs.exe` to a location that is included in your `%PATH%`. For example:

    ```nohighlight
    %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
    ```

{{< /tab >}}
{{< tab id="windows-wsl2" title="Windows (WSL2)">}}

1. Install the kubectl-gs binary for Linux first. You can use the instructions using Krew shown above, or follow the Linux instructions without Krew.

2. Run the following command so that `kubectl gs login` can open your browser:

    ```nohighlight
    sudo ln -s $(which wslview) /usr/local/bin/xdg-open
    ```

{{< /tab >}}
{{< /tabs >}}

## Docker

We offer a Docker image via our public repository. The semantic release version number is used to tag images.

1. Pull the image

    ```nohighlight
    docker pull gsoci.azurecr.io/giantswarm/kubectl-gs:latest
    ```

2. Execute a command

    ```nohighlight
    docker run --rm -ti gsoci.azurecr.io/giantswarm/kubectl-gs:latest help
    ```
