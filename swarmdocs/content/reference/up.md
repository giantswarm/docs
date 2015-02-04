+++
title = "Creating and starting an application in one step"
description = "This is the reference page for the 'swarm up' command, which allows you to create and start an application in one step."
date = "2015-01-29"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm up"]
weight = 100
+++

# Creating and starting an application in one step

The `swarm up` command allows you to create a new application based on your configuration and start it immediately afterwards.

In other words, it does what [`swarm create`](../create/) and [`swarm start`](../start/) do, but with one command call.

## General syntax

The general syntax is this:

```nohighlight
$ swarm up [-d|--detach] [config_filepath] [--var-file=<filepath>] [--var=<key=value>]
```

By default the `swarm up` exits after the application has been started successfully (or an error has occurred). Alternatively you can make it exit immediately after issuing the command to the API. That's what the `-d` (or `--detach`) flag is for.

The optional `config_filepath` argument can be used to define which application configuration file should be used. If not given, this defaults to `./swarm.json`.

The `--var-file` argument allows to set the path of variables file to be used with your application configuration file. If not given, `./swarmvars.json` is automatically checked and used of present. In addition (or as an alternative to the variables file), an arbitrary number of '--var' arguments can be used to set variables for use in the application configuration.

If you want to know more about using variables in your application configuration, also check out [Creating an application](../create/).

## Straightforward use

The easiest is to run this command without any further arguments:

```nohighlight
$ swarm up
```

This assumes that your application configuration file is in the current directory and it is called `swarm.json`. Optional configuration variables in `swarmvars.json` are read from the same directory, too, if present.

## Further reading

* [Creating an application (`swarm create`)](../create/)
* [Starting an application (`swarm start`)](../start/)
* [Application configuration](../swarm-json/)
