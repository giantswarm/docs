# Starting an environment, app or service

<p class="lastmod">Last edited on November 8, 2014 by Marian Steinbach</p>

Using the `swarm start` command you can start all apps in the current environment, one specific app or one service inside an app.

Since all of these commands require you to be aware of the current environment, when in doubt, read more about dealing with environments on the [environments reference page](../env/).

## Starting an environment

To start all apps existing within the current environment, all you have to do is run the command

    $ swarm start

## Starting an app

If you only want to start a specific app inside the current environment, you can use the name of the app as an argument for the `swarm start` command.

    $ swarm start <app_name>

Here, `<app_name>` is the name you used in your app configuration file (`swarm.json`) when [creating](../create/) the app.

For example, if your app is called "onlineshop":

    $ swarm start onlineshop

## Starting a service

You can even become more specific and only start a specific service of one of your apps. This again uses the definition in your app configuration file. In addition to the `app_name`, here the `service_name` is referenced. The command syntax:

    $ swarm start <app_name>/<service_name>

So if you had, for example, a service called "payment" in your app called "onlineshop", you could use this command to start that service:

    $ swarm start onlineshop/payment

## Further reading

* [Environments](../env/)
* [App configuration](../swarm-json/)
* [Global command line options](../global-options/)
