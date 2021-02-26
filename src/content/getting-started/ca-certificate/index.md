---
linkTitle: Accepting your cluster’s CA certificate
title: Establishing trust to your cluster's CA and importing certificates
description: To access the API of your server as well as services like the Kubernetes Dashboard using a web browser, you need to import the CA certificate for the cluster and your key pair. Here we show how to do this for several platforms and clients.
weight: 80
menu:
  main:
    parent: getting-started
aliases:
  - /guides/importing-certificates/
owner:
  - https://github.com/orgs/giantswarm/teams/team-ludacris
---

# Establishing Trust to Your Cluster's CA and Importing Certificates

In this tutorial we explain to you how to establish trust to your cluster's Certificate Authority (CA) and how to import a key pair to enable client authentication against the API to enable access to the Kubernetes API of your cluster.

This is not only useful for developing applications accessing the API, but for authenticated access to services via the API proxy. For example, the Kubernetes Dashboard is usually accessed in this way.

## Introduction

As a user of a Giant Swarm Kubernetes cluster, when you access services on the cluster like, for example, the Kubernetes Dashboard, you are directly using the Kubernetes API. For this to work, two basic conditions have to be met:

1. Your HTTP client (e. g. the browser) must accept the TLS certificate presented by the API server, which means that it has to trust the Certificate Authority (CA) that issued this certificate.
2. Your HTTP client must present a valid client certificate accepted by the server.

The CA that issued the server certificate is one created by Giant Swarm exclusively for your cluster, so it is unknown to your browser.

Both the CA file for your cluster and a personal key pair, consisting of a client certificate and a private key, can be obtained using either our [web user interface]({{< relref "/ui-api/web/" >}}) or [gsctl]({{< relref "/ui-api/gsctl" >}}).

In the tutorial we assume that you have done this and obtained three files:

- The CA file
- Your private key
- Your client certificate

## Creating a PKCS12 bundle {#creating-pkcs12-bundle}

We currently provide your key pair as a set of two PEM files, the private key and the certificate. As most platforms/browsers want to import the key pair as one PKCS12 bundle (also known as P12 or PFX file), you'll have to create an importable bundle first. This can be done using OpenSSL, which is free software and available for a wide range of platforms.

A command like shown in the example below will create the bundle as a file named `client.p12`. The `-inkey` argument points to your private key file, the `-in` argument to your certificate.

```nohighlight
openssl pkcs12 -export -clcerts \
  -inkey client.key \
  -in client.crt \
  -out client.p12 \
  -passout pass:giantswarm \
  -name "Key pair for Giant Swarm cluster"
```

The `-passout` argument sets a password to encrypt the bundle. In our examples here, we use the password `giantswarm`. Feel free to pick your own password when following the tutorial, but make sure to prepend the `pass:` prefix as shown above. If you prefer to enter a password via a prompt instead of passing it as a clear text argument, you can completely omit the `-passout pass:<your-password>` part.

Also note that we give a freely chosen name for the bundle using the `-name` argument. You can pick whatever name suits you. However, most platforms don't display this name in any meaningful place, so don't put too much effort in coming up with a good name.

## Working with curl

curl is often used during development of an application to issue requests against an API. The ways how curl can manage a list of trusted CAs are manifold and depend on a lot of parameters, for example compile-time configuration. Covering all possible options would go beyond the scope of this tutorial.

Nevertheless, there is a way to set a CA to trusted, independent of any permanent CA bundle and store configuration, using the `CURL_CA_BUNDLE` environment variable. By setting this variable to the path of the CA file, curl will trust the CA described in that file. Example:

```nohighlight
export CURL_CA_BUNDLE=/path/to/ca.crt
```

The personal certificate has to be applied with every request. Here is an example curl command:

```nohighlight
curl \
  --cert path/to/client.crt \
  --key path/to/client.key \
  https://api.mycluster.k8s.gigantic.io/api/v1
```

## Importing CA and certificate {#importing}

Operating systems and HTTP clients have a variety of ways to manage CAs and certificates. Even on one platform there are often several ways to achieve the same thing. We focus here on the more popular combinations of operating system and client, and we opt for ways using command line utilities, as we think this will mostly suit the target audience of this tutorial.

### Shortcut by client

- macOS
    - Safari and Chrome use the [macOS Keychain](#mac-os-keychain)
    - [Firefox](#mac-os-firefox)
- Linux
    - [Chrome, Chromium](#linux-chromium)
    - [Firefox](#linux-firefox)
- Windows
    - Edge, IE, Chrome, and Chromium use the [certificate store](#win-cert-store) provided by the operating system
    - [Firefox](#win-firefox)

### macOS

#### macOS keychain {#mac-os-keychain}

On macOS, browsers like **Safari** and **Chrome** rely on the system keychain for CA information and certificates. Firefox can be configured to support this, too, which is explained in a [separate section](#mac-os-firefox).

Importing certificates on macOS can be done interactively through the Keychain app, or via the command line. We explain the latter option here.

With the keychain path `$HOME/Library/Keychains/login.keychain` and the CA file under the path `path/to/ca.crt`, this command would import the CA and set it to trusted:

```nohighlight
security add-trusted-cert \
  -r trustRoot \
  -k "$HOME/Library/Keychains/login.keychain" \
  path/to/ca.crt
```

Now to importing your client certificate. With `path/to/bundle.p12` being the path to your PKCS12 bundle file generated earlier and `giantswarm` being the password you used then, this command will import the certificate into your personal keychain:

```nohighlight
security import \
  path/to/bundle.p12 \
  -k "$HOME/Library/Keychains/login.keychain" \
  -P giantswarm
```

#### Firefox on macOS {#mac-os-firefox}

By default, Firefox does not use the system keychain, but provides its own certificate manager. You can manually add the CA file and key pair via the _Preferences / Advanced / Certificates / View Certificates / Import_ function.

However, a possible simpler alternative is to let Firefox use the system keychain in addition. To enable this

1. open the advanced preferences by typing the pseudo-URL `about:config` into the location bar.
2. Set the following two configuration variables to `true`:
   - `security.enterprise_roots.enabled`
   - `security.osclientcerts.autoload`

Restarting Firefox may be required after changing these preferences.

### Linux

#### Chromium and Google Chrome on Linux {#linux-chromium}

Chromium and Google Chrome behave the same way when it comes to CA/certificate import on Linux. They use a [shared NSS DB](https://wiki.mozilla.org/NSS_Shared_DB_And_LINUX) stored in the directory `$HOME/.pki/nssdb`.

Let's test if you actually have that directory.

```nohighlight
ls $HOME/.pki/nssdb
```

You should get a listing for some files.

Now make sure you have the `certutil` and `pk12util` utilities available. On Debian based distributions, like Ubuntu, these can be installed using

```nohighlight
sudo apt-get install libnss3-tools
```

**Important:** Please close Chrome/Chromium before you proceed.

Assuming that your CA file to import is in `path/to/ca.crt`, do this to import it and establish trust:

```nohighlight
certutil -A \
  -n "Name of certificate" \
  -t "TC,," \
  -d sql:$HOME/.pki/nssdb \
  -i path/to/ca.crt
```

Now we can import the PKCS12 key bundle. The example below again assumes the PKCS12 bundle at `path/to/bundle.p12`. The password given via the `-W` switch has to match the one you set when [creating the bundle](#creating-pkcs12-bundle).

```nohighlight
pk12util -i path/to/bundle.p12 \
  -d sql:$HOME/.pki/nssdb \
  -W giantswarm
```

#### Firefox on Linux {#linux-firefox}

Firefox maintains its certificate information in the personal profile folder. Every user who has used Firefox once should have such a profile.

As the naming of this folder has a random component, we first need to find the actual path. The command below should ideally yield exactly one path entry for you:

```nohighlight
find ~/.mozilla/firefox -name "cert8.db"|xargs dirname
```

For the next steps you'll need the `certutil` and `pk12util` utilities. On Debian based distributions, like Ubuntu, these can be installed using

```nohighlight
sudo apt-get install libnss3-tools
```

**Important:** Before you proceed, please **shut down Firefox** in case it is running.

Now let's import the CA and set it to trusted. Assuming that your Firefox profile folder is `~/.mozilla/firefox/6eozd6kv.default` and the CA file is at `path/to/ca.crt`, this command will do both for you:

```nohighlight
certutil -A \
  -n "Name of certificate" \
  -t "TC,," \
  -d ~/.mozilla/firefox/6eozd6kv.default \
  -i path/to/ca.crt
```

Of course you can change `Name of certificate` to whatever name or description you like.

Now we can import the PKCS12 key bundle. The example below again assumes your Firefox profile to be found at `~/.mozilla/firefox/6eozd6kv.default` and the PKCS12 bundle at `path/to/bundle.p12`. The password given via the `-W` switch has to match the one you set when [creating the bundle](#creating-pkcs12-bundle).

```nohighlight
pk12util -i path/to/bundle.p12 \
  -d ~/.mozilla/firefox/6eozd6kv.default \
  -W giantswarm
```

### Windows

#### Common certificate store {#win-cert-store}

Browsers like Edge, Internet Explorer, Chrome, and Chromium use the certificate store provided by the operating system.

You'll need a command prompt with Administrator permissions. In Windows 10, use the search input next to the Windows menu button to search for `cmd`. Right-click the "Command Prompt" entry and select the context menu item "Run as administrator".

To install the CA using the file path `path\to\ca.crt`:

```nohighlight
certutil.exe -addstore "Root" path\to\ca.crt
```

Assuming that your PKCS12 bundle is in `path\to\bundle.p12`, run this command to import your client certificate:

```nohighlight
certutil.exe -p password -user -importPFX path\to\bundle.p12
```

#### Firefox on Windows {#win-firefox}

As on all other operating systems, Firefox uses it's own certificate store also on Windows. Managing this store via the command line requires NSS utilities, which are not regularly released for the Windows platform.

You can manually add the CA file and key pair via the _Tools / Options / Advanced / Certificates / View Certificates / Import_ function.

## Related

- [Accessing pods and services from the outside]({{< relref "/getting-started/exposing-workloads" >}})
