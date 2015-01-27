+++
title = "Stopping an application or service"
description = "The reference page for the 'swarm stop' command, which is used to stop entire applications or specific services."
date = "2014-12-18"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm stop"]
weight = 100
+++

# Stopping an application or service

Using the `swarm stop` command you can stop an entire application or a specific service of an application. The applications or service remains existent and can be started again when needed.

Stopping a service means that all components defined within this service will be stopped. Stopping an entire application means thatt all services defined within an application will be stopped, which of course includes all components.

<i class="fa fa-exclamation-triangle"></i> When a component is stopped, the __data stored inside the according container is lost__. If you want to persist data throughout stops and starts, you can use volumes. Find out more about volumes in the [application configuration reference](../swarm-json/#volumes).

## Stopping an application

To stop an application, you simply call `swarm stop` with the application name as an argument. The application name is defined in your application configuration file (`swarm.json`). Example:

    $ swarm stop myapp

When in a terminal, you will see a little activity indicator until the application is actually stopped.

## Stopping a service

To stop a service, provide the name of the service as defined in your application configuration (`swarm.json`), prefixed with the application name and a slash (`/`). Example:

    $ swarm stop myapp/myservice

## Non-blocking execution

Stopping an application or service usually takes a few seconds at most. By default the `swarm stop` command waits until the application or service is actually stopped.

To execute the command in a non-blocking or "detached" way, you can use the `-d` or `--detach` flag:

    $ swarm stop -d myapp
    $ swarm stop -d myapp/myservice


## Further reading

* [Starting an application or service](../start/)
* [Application configuration](../swarm-json/)
