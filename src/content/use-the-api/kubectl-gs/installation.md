---
linkTitle: Installation
title: Installing kubectl-gs
description: How to obtain kubectl gs, the Giant Swarm kubectl plugin, how to keep it up to date, and where to find the Docker image.
weight: 10
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/installation/
  - /ui-api/kubectl-gs/installation/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-05-03
user_questions:
  - Where can I find the Giant Swarm plugin for kubectl?
  - How can I install the Giant Swarm plugin for kubectl?
  - How can I keep the Giant Swarm plugin for kubectl up to date?
  - How can I install kubectl-gs?
  - Is there an official Docker image for kubectl-gs?
---

`kubectl-gs` is the Giant Swarm plug-in for `kubectl` with the official plug-in name `gs`.

The latest version is v{{% kubectl_gs_version %}}.

The simplest way to manage `kubectl` plug-ins across platforms is using [Krew](https://krew.sigs.k8s.io/). If you don't have Krew installed, check the [Krew installation docs](https://krew.sigs.k8s.io/docs/user-guide/setup/install/) on how to get it installed.

Further down you will also find instructions on installing kubectl-gs [without Krew](#without-krew) and additional platform-specific instructions.

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

For platform-specific instuctions, please select a platform below.

{{< tabs >}}
{{< tab id="linux-amd64" title="Linux">}}

1. Download the release binary

    ```nohighlight
    curl -L https://github.com/giantswarm/kubectl-gs/releases/download/v{{% kubectl_gs_version %}}/kubectl-gs-v{{% kubectl_gs_version %}}-linux-amd64.tar.gz -o kubectl-gs-v{{% kubectl_gs_version %}}-linux-amd64.tar.gz
    ```

2. Unpack the downloaded package

    ```nohighlight
    tar xzf kubectl-gs-v{{% kubectl_gs_version %}}-linux-amd64.tar.gz
    ```

3. Copy the executable into a folder included in your `PATH`

    ```nohighlight
    sudo cp kubectl-gs-v{{% kubectl_gs_version %}}-linux-amd64/kubectl-gs /usr/local/bin/
    ```

{{< /tab >}}
{{< tab id="linux-arm64" title="Linux ARM">}}

1. Download the release binary

    ```nohighlight
    curl -L https://github.com/giantswarm/kubectl-gs/releases/download/v{{% kubectl_gs_version %}}/kubectl-gs-v{{% kubectl_gs_version %}}-linux-arm64.tar.gz -o kubectl-gs-v{{% kubectl_gs_version %}}-linux-arm64.tar.gz
    ```

2. Unpack the downloaded package

    ```nohighlight
    tar xzf kubectl-gs-v{{% kubectl_gs_version %}}-linux-arm64.tar.gz
    ```

3. Copy the executable into a folder included in your `PATH`

    ```nohighlight
    sudo cp kubectl-gs-v{{% kubectl_gs_version %}}-linux-arm64/kubectl-gs /usr/local/bin/
    ```

{{< /tab >}}
{{< tab id="darwin-amd64" title="macOS">}}

1. Download the release binary

    ```nohighlight
    curl -L https://github.com/giantswarm/kubectl-gs/releases/download/v{{% kubectl_gs_version %}}/kubectl-gs-v{{% kubectl_gs_version %}}-darwin-amd64.tar.gz -o kubectl-gs-v{{% kubectl_gs_version %}}-darwin-amd64.tar.gz
    ```

2. Unpack the downloaded package

    ```nohighlight
    tar xzf kubectl-gs-v{{% kubectl_gs_version %}}-darwin-amd64.tar.gz
    ```

3. Copy the executable into a folder included in your `PATH`

    ```nohighlight
    sudo cp kubectl-gs-v{{% kubectl_gs_version %}}-darwin-amd64/kubectl-gs /usr/local/bin/
    ```

{{< /tab >}}
{{< tab id="darwin-arm64" title="macOS M1">}}

1. Download the release binary

    ```nohighlight
    curl -L https://github.com/giantswarm/kubectl-gs/releases/download/v{{% kubectl_gs_version %}}/kubectl-gs-v{{% kubectl_gs_version %}}-darwin-arm64.tar.gz -o kubectl-gs-v{{% kubectl_gs_version %}}-darwin-arm64.tar.gz
    ```

2. Unpack the downloaded package

    ```nohighlight
    tar xzf kubectl-gs-v{{% kubectl_gs_version %}}-darwin-arm64.tar.gz
    ```

3. Copy the executable into a folder included in your `PATH`

    ```nohighlight
    sudo cp kubectl-gs-v{{% kubectl_gs_version %}}-darwin-arm64/kubectl-gs /usr/local/bin/
    ```

{{< /tab >}}
{{< tab id="windows-amd64" title="Windows">}}

Please note that we only provide a 64bit release.

1. Download the [release ZIP file](https://github.com/giantswarm/kubectl-gs/releases/download/v{{% kubectl_gs_version %}}/kubectl-gs-v{{% kubectl_gs_version %}}-windows-amd64.zip)

2. Extract the downloaded ZIP file

2. Copy `kubectl-gs.exe` to a location that is included in your `%PATH%`. For example:

    ```nohighlight
    %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
    ```

{{< /tab >}}
{{< tab id="windows-wsl2" title="WSL2">}}

1. Install the kubectl-gs binary for Linux first. You can use the instructions using Krew shown above, or follow the Linux instructions without Krew.

2. Run the following command so that `kubectl gs login` can open your browser:

    ```nohighlight
    sudo ln -s $(which wslview) /usr/local/bin/xdg-open
    ```

{{< /tab >}}
{{< /tabs >}}

## Docker

We offer a Docker image via our public [Quay](https://quay.io/repository/giantswarm/kubectl-gs?tab=info) repository. The semantic release version number is used to tag images.

1. Pull the image

    ```nohighlight
    docker pull quay.io/giantswarm/kubectl-gs:{{% kubectl_gs_version %}}
    ```

2. Execute a command

    ```nohighlight
    docker run --rm -ti quay.io/giantswarm/kubectl-gs:{{% kubectl_gs_version %}} help
    ```
