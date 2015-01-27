+++
title = "Scaling up a component"
description = "Reference page for the 'swarm scaleup' command, which allows you to increase the number of instances running for a particular component."
date = "2015-01-12"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm scaleup"]
weight = 100
+++

# Scaling up a component

The `swarm scaleup` command is used to increase the number of instances running a service component.

## Command syntax

The command requires a service component name as argument. Optionally, the number of instances to be added can be given. If no number is given, `1` is assumed.

    $ swarm scaleup <app/service/component> [num-to-add]

For example, if you have an "onlineshop" app with a service called "imageserver" and a component called "nginx", use the following command to __add one__ instance for this component:

    $ swarm scaleup onlineshop/imageserver/nginx

To add two new instances, use this syntax:

    $ swarm scaleup onlineshop/imageserver/nginx 2

## Related reading

 * [Scaling down a component](../scaledown/)
