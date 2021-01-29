---
linkTitle: info
title: "'gsctl info' command reference"
description: The 'gsctl info' command lets you display information on your current status and configuration.
weight: 110
menu:
  main:
    parent: uiapi-gsctl
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl info`

The `gsctl info` command lets you display information on your current status
your configuration, and on the Giant Swarm installation in use.

## Usage

The usage is straight forward. Just execute `gsctl info`. To activate printing
of the current authentication token (if available), add the `-v` or `--verbose`
flag.

The details printed depend on your current login status and on the provider
used in the installation (AWS, Azure, or KVM).

When not logged in, a limited information set like this will be displayed:

```nohighlight
gsctl version:        0.11.2
gsctl build:          2018-04-26T07:33:33Z
Config path:          /Users/marian/.config/gsctl/config.yaml
kubectl config path:  /Users/marian/.kube/config
API endpoint:         https://api.g8s.gollum.westeurope.azure.gigantic.io
API endpoint alias:   gollum
Email:                somebody@example.com
Logged in:            no
Provider:             n/a
```

When logged in with an AWS installation, these additional details will appear:

```nohighlight
...
Provider:                      aws
Worker instance type options:  m3.xlarge, m3.2xlarge, r3.xlarge, r3.2xlarge, r3.4xlarge, r3.8xlarge, m4.xlarge, m4.2xlarge, m4.4xlarge, m5.xlarge, m5.2xlarge, m5.4xlarge, t2.xlarge, t2.2xlarge, c5.2xlarge, i3.xlarge
Default worker instance type:  m4.xlarge
Default workers per cluster:   3
Maximum workers per cluster:   20
```

Similarly, with an Azure installation, these additional lines will appear:

```nohighlight
...
Provider:                     azure
Worker VM size options:       Standard_A2_v2, Standard_A4_v2, Standard_A8_v2, Standard_D2_v3, Standard_D4_v3, Standard_D8_v3, Standard_D16_v3, Standard_D32_v3, Standard_D2s_v3, Standard_D4s_v3, Standard_D8s_v3, Standard_D16s_v3, Standard_D32s_v3, Standard_F4s_v2, Standard_F8s_v2, Standard_F16s_v2, Standard_F32s_v2, Standard_E4s_v3, Standard_E8s_v3, Standard_E16s_v3, Standard_E32s_v3
Default worker VM size:       Standard_DS2_v2
Default workers per cluster:  3
Maximum workers per cluster:  20
```

## Output details

- `gsctl version`: The gsctl version you are using.
- `gsctl build`: Date and time when your copy of gsctl has been built.
- `Config path`: Path to the currently used configuration file.
- `kubectl config path`: Path to the kubectl configuration file in use.
- `API endpoint`: The API endpoint URL you are currently using.
- `API endpoint alias`: The alias of the endpoint. See
  [`gsctl select endpoint`]({{< relref "/ui-api/gsctl/select-endpoint#alias" >}}) for details
- `Email`: Your email address. If this isn't displayed, you are not logged in.
- `Logged in`: Whether or not you are authenticated against the API endpoint.
- `Auth token`: Current authentication token, if activated and you are logged in. Only displayed when `-v/--verbose` is used.
- `Default workers per cluster`: Number of workers new clusters will have if not specified on creation
- `Maximum workers per cluster`: The maximum number of workers each cluster in this installation can have

### AWS specific

- `Default worker instance type`: The EC2 instance type to use for worker nodes by default
- `Worker instance type options`: EC2 instance types available for worker nodes

### Azure Specific

- `Default worker VM size`: The virtual machine size to use for worker nodes by default
- `Worker VM size options`: Virtual machine sizes available for worker nodes

## Related

- [`gsctl select endpoint`]({{< relref "/ui-api/gsctl/select-endpoint" >}})
- [API: Get information on the installation](/api/#operation/getInfo)
