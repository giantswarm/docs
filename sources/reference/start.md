description: This is the reference page for the 'swarm start' command, which allows you to start an application or service.

# Starting an application or service

<p class="lastmod">Last edited on December 11, 2014 by Marian Steinbach</p>

Using the `swarm start` command you can start an application or a specific service inside an application.

Before you can actually start an application it has to be created in the selected environment before. You can learn more about this on the [environments reference page](../env/) and the reference page on [Creating an application](../create/).

## General syntax

The overall syntax of the `swarm start` command is as follows:

    $ swarm start [-d|--detach] [app_name[/service_name]]

The optional `app_name` argument specifies the application to be started. It refers to the name you see when running `swarm ls` to list applications. Using the additional `service_name`, seperated by `/`, you can specify a service to be started.

If the `app_name` (and `service_name`) argument is ommitted, the CLI looks if there is a `swarm.json` [application configuration](../swarm-json/) file in the current directory. If this is the case, the application defined in that configuration file is started.

The flag `-d` or `--detach` can be used to immediately exit the command after issuing the command to the API. When immitted, the command is running until the application is either running an error occurs.

## Starting an application

For example, if you have created an application called "onlineshop" in your current environment, you can start it this way:

    $ swarm start onlineshop

The name `onlineshop` refers to the `app_name` directive in your application configuration (namely `swarm.json` file).

Remember, if the `swarm.json` file for that application is in your current directory, all you have to run is this:

    $ swarm start

## Starting a service

Say you have, for example, a service called "payment" in your app called "onlineshop", you could start this specific service using the following command:

    $ swarm start onlineshop/payment

## Further reading

* [Environments](../env/)
* [Application configuration](../swarm-json/)
* [Global command line options](../global-options/)
