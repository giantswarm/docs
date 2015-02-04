+++
title = "Getting basic information"
description = "Reference page for the `swarm info` command, which allows you to get some basic information on your login and environment status."
date = "2015-01-29"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm info"]
weight = 100
+++

# Getting basic information

The `swarm info` command is available to access some very basic information on your current status and settings.

## Command syntax

The comand is called without any arguments, like this:

```nohighlight
$ swarm info
```

## Output

Here is an example output:

```nohighlight
Cluster status:      reachable
Logged in as user:   someuser
Current environment: acmecorp/dev
```

What does this information tell you?

* __Cluster status__: This is the general platform health and should say `reachable`.
* __Logged in as user__: Here you find the username you are currently logged in with. Hint: If you are only interested in the current user name, you can use the [`swarm user`](../user/) command for that.
* __Current environment__: The currently selected environment you are working in. Hint: Your can also get this information using [`swarm env`](../env/).

## Further reading

* [Environments](../env/)
* [Companies](../companies/)
