+++
title = "Scaling down a component"
description = "Reference page for the 'swarm scaledown' command, which allows you to reduce the number of instances running for a particular component."
date = "2015-01-12"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm scaledown"]
weight = 100
+++

# Scaling down a component

The `swarm scaledown` command is used to decrease the number of instances running a service component.

## Command syntax

The command requires a service component name as argument. Optionally, the number of instances to be added can be given. If no number is given, `1` is assumed.

```nohighlight
$ swarm scaledown <app/service/component> [num-to-remove]
```

For example, if you have an "onlineshop" app with a service called "imageserver" and a component called "nginx", use the following command to __take away one__ instance from this component:

```nohighlight
$ swarm scaledown onlineshop/imageserver/nginx
```

To remove two instances, use this syntax:

```nohighlight
$ swarm scaledown onlineshop/imageserver/nginx 2
```

## Further reading

 * [Scaling up a component](../scaleup/)
