description: The reference page for the 'swarm ls' command, which is used to show a list of applications in an environment.

# Listing applications

<p class="lastmod">Last edited on December 18, 2014 by Marian Steinbach</p>

The `swarm ls` helps you to find out which applications are configured in your current environment and what their status is.

The command is simply called without any arguments, like this:

    $ swarm ls

You get a table-like output of your applications. Here is an example:

    2 apps available:

    app              env  company  created              status
    graphhopper-cgn  dev  marian   2014-12-09 11:07:45  up
    twofishes        dev  marian   2014-12-18 06:43:11  down

The columns in detail:

 * `app`: The application name as defined in your application configuration
 * `env`: The environment name the application is running in
 * `company`: The company owning the environment and thus the application
 * `created`: The UTC date and time when the application has been created
 * `status`: The overall status of the application

## Application status

The application status is an aggregate of the statuses of all component instances within that application. When reported on an application level, the possible statuses and their meaning are:

 * `up`: All component instances are running.
 * `starting`: One or more component instances, possibly all of them, are currently being started, some might already be up.
 * `down`: At least one component instances is currently down (meaning neither running nor started. This might as well mean. Any number of other instances might be up or starting.
 * `failed`: At least one component instance has a failure. Any number of other instances might be down, starting or up.


## Further reading

* [Getting an application's status](../status/)