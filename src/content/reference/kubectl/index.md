+++
title = "Install kubectl"
description = "Installation documentation for kubectl, the Kubernetes command line interface."
date = "2017-01-02"
type = "page"
weight = 100
+++

# Installing and Updating `kubectl`

`kubectl` comes as a self-contained binary for Mac, Linux, and Windows. Below you find installation instructions for different platforms.

Always, make sure that your local `kubectl` version is as close as possible to the version of your Kubernetes cluster.

Please select your platform:

<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#install-mac-brew" data-toggle="tab">Mac OS (Homebrew)</a></li>
  <li role="presentation"><a href="#install-mac" data-toggle="tab">Mac OS</a></li>
  <li role="presentation"><a href="#install-linux" data-toggle="tab">Linux</a></li>
  <li role="presentation"><a href="#install-win" data-toggle="tab">Windows</a></li>
</ul>


<div class="tab-content clearfix">
<div class="tab-pane active" id="install-mac-brew">

  <p>Homebrew provides the most convenient way to install <code>kubectl</code> and keep it up to date. To install, use this command:</p>

  <pre><code class="language-nohighlight">brew install kubectl</code></pre>

  <p>For updating:</p>

  <pre><code class="language-nohighlight">brew upgrade kubectl</code></pre>

</div>
<div class="tab-pane" id="install-mac">

  <p>Execute the commands below to install a specific released version. The same commands work for upgrading from a previously installed version.</p>

  <pre><code class="language-nohighlight">curl -O https://storage.googleapis.com/kubernetes-release/release/v{{% kubectl_version %}}/bin/darwin/amd64/kubectl
chmod +x kubectl
sudo cp kubectl /usr/local/bin/kubectl</code></pre>

</div>
<div class="tab-pane" id="install-linux">

  <p>Execute the commands below to install a specific released version. The same commands work for upgrading from a previously installed version.</p>

  <pre><code class="language-nohighlight">curl -O https://storage.googleapis.com/kubernetes-release/release/v{{% kubectl_version %}}/bin/linux/amd64/kubectl
chmod +x kubectl
sudo cp kubectl /usr/local/bin/kubectl</code></pre>

</div>
<div class="tab-pane" id="install-win">

  <p>Download Kubernetes client of your desired version after following the <code>CHANGELOG</code> link of the respective <a href="https://github.com/kubernetes/kubernetes/releases">Kubernetes GitHub release</a>, extract it to a folder of your choice, and make the <code>kubectl.exe</code> available in your environment PATH variable.</p>

</div>
</div>

## Next steps {#next}

- You can use [gsctl](https://docs.giantswarm.io/reference/gsctl/#configuration) to set up kubectl for use with a Giant Swarm cluster.
- For an overview over the functionality of `kubectl` please refer to the [official kubectl reference](http://kubernetes.io/docs/user-guide/kubectl-overview/)
