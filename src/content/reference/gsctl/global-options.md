---
title = "Global command line options in gsctl"
description = "Documentation for gsctl options that can be passed on the command line for almost all commands. Plus some tips on how you can use them to switch environments."
date = "2018-01-26"
type = "page"
weight = 20
---

# Global Command Line Options

`gsctl` supports the following global command line options. These are options that can be used in combination with all commands.

*Note:* Some global options might not have an effect with every command.

## Overview

- `--endpoint`/`-e`: Using this option you can override the endpoint temporarily for a given command. For interactive use however it's more convenient to switch endpoints using the [`gsctl select endpoint`](../select-endpoint/) command.
- `--auth-token`: Can be used to pass an authentication token for the use in single command, as an alternative to a permanent login in via `gsctl login`.
- `--config-dir`: This option allows to override the directory path to use for storing your configuration file and key pairs. By default, they get stored in `$HOME/.config/gsctl`.
- `--verbose`, `-v`: Print more detailed output

## Easily switching between environments {#switching-environments}

When working with more than one Giant Swarm installation, you will want to
switch the API endpoint you are using with `gsctl` every now end then. Here are
a few tips to make that as convenient as possible.

`gsctl` (starting with version 0.8) maintains a list of all endpoints you have
successfully logged in with. The command
[`gsctl list endpoints`](../list-endpoints/) lets you show that list. You can
be in fact logged in with all your endpoints at the same time. All you have to
do to switch between them is run the `select endpoint` command.

```nohighlight
$ gsctl select endpoint <endpoint-url-or-alias>
```

This requires the API URL or an endpoint alias to be given as argument.

Aliases greatly simplify the selection of an endpoint.

As shown in the list above, an endpoint can also be set per command, using
the `--endpoint` or `-e` flag. If you have an endpoint with alias `cloud` and
another one with `onprem`, this allows you to list clusters on both without
permanently selecting an endpoint:

```nohighlight
$ gsctl list clusters -e cloud
...
$ gsctl list clusters -e onprem
...
```
