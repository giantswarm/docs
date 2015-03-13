+++
title = "Getting an applications's status"
description = "Reference page for the 'swarm status' command, which prints out the status of a particular application and its services and components."
date = "2015-01-29"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm status"]
weight = 84
+++

# Getting an applications's status

The `swarm` command line tool provides the `status` command for you to fetch information on a specific application as well as its services and components.

## Syntax and output

The command needs the name of your application, which you have to set with the `app_name` key as an argument. Here, `<app_name>` is the name you used in your application configuration file (`swarm.json`) when [creating](../create/) the app. The syntax is:

```nohighlight
$ swarm status [app_name]
```

For example, for an application named "onlineshop", we would use this command:

```nohighlight
$ swarm status onlineshop
```

Here is an example output:

```nohighlight
App onlineshop is up

service      component      instanceid                            created              status
appserver    elasticsearch  9c79161b-baec-447b-9a8e-230206268570  2015-01-06 10:28 UTC  up
appserver    gunicorn       b4405a86-958e-4a46-ac14-41404c5e17bd  2015-01-06 10:28 UTC  up
appserver    gunicorn       c4a38g02-472d-4c38-a5b1-1b3a69cdc3d2  2015-01-06 10:28 UTC  up
appserver    mongodb        2370a56c-0e5a-4b82-9e25-07ffa915988b  2015-01-06 10:28 UTC  up
appserver    nginx          962fac1c-e9ba-42b6-9223-6edec84f003f  2015-01-06 10:28 UTC  up
appserver    redis          863fac2c-e8ba-42a3-9223-6edec84f003f  2015-01-06 10:28 UTC  up
imageserver  nginx          d29df528-0e5a-4b82-9223-6ed0626817bd  2015-01-06 10:28 UTC  up
payments     payments       71481fdf-1fa1-49f0-9320-d29df5297ae5  2015-01-06 10:28 UTC  up
```

The first line of the output shows the status of the application as a summary. This status is an aggregation of the individual component's statuses, with the "worst" status of all components being reported. This means that if even one component is `down`, the entire application is considered `down`, too.

The second part is a table of all components within all services of that application. The table columns show which service the component belongs to, the component name, the ID of the instance the component is running on, the date and time when the instance of the component was first started, and the component status. If a component is running on more than one instance, each instance is represented in an individual row.

<!-- TODO: Create reference page on instance IDs and link from here. -->

## Statuses and their meaning

Your components can have either of the following statuses:

 * `up`: The component is currently running
 * `starting`: The component is currently starting
 * `down`: The component is currently not running
 * `failed`: An error occurred during the attempt to start the component and it's currently not running

## Further reading

* [List applications](../ls/)
* [Accessing process logs](../logs/)
* [Getting instance statistics](../stats/)
* [Getting basic information](../info/)
