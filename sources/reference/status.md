# Getting an app's status

<p class="lastmod">Last edited on November 9, 2014 by Marian Steinbach</p>

The `swarm` command line tool provides the `status` command for you to fetch information on a specific app as well as its services and components.

## Syntax and output

The command needs the name of your app, which you have to set with the `app_name` key as an argument. Here, `<app_name>` is the name you used in your app configuration file (`swarm.json`) when [creating](../create/) the app. The syntax is:

    $ swarm status <app_name>

For example, for an app named "onlineshop", we would use this command:

    $ swarm status onlineshop

Here is an example output:

```
App onlineshop is up

service      component      instanceid                            status
appserver    elasticsearch  9c79161b-baec-447b-9a8e-230206268570  up
appserver    gunicorn       b4405a86-958e-4a46-ac14-41404c5e17bd  up
appserver    gunicorn       c4a38g02-472d-4c38-a5b1-1b3a69cdc3d2  up
appserver    mongodb        2370a56c-0e5a-4b82-9e25-07ffa915988b  up
appserver    nginx          962fac1c-e9ba-42b6-9223-6edec84f003f  up
appserver    redis          863fac2c-e8ba-42a3-9223-6edec84f003f  up
imageserver  nginx          d29df528-0e5a-4b82-9223-6ed0626817bd  up
payments     payments       71481fdf-1fa1-49f0-9320-d29df5297ae5  up
```

The first line of the output shows the status of the app as a summary. This status is an aggregation of the individual component's statuses, with the "worst" status of all components being reported. This means that if even one component is `down`, the entire app is considered `down`, too.

The second part is a table of all components within all services of that app. The table columns show which service the component belongs to, the component name, the ID of the instance the component is running on, and the component status. If a component is running on more than one instance, each instance is represented in an individual row.

<!-- TODO: Create reference page on instance IDs and link from here. -->

## Statuses and their meaning

Your components can have either of the following statuses:

 * `up`: The component is currently running
 * `starting`: The component is currently starting
 * `down`: The component is currently not running
 * `failed`: An error occurred during the attempt to start the component and it's currently not running

<!-- ## Further reading

TODO: Give hint on how to debug a component or get more information about why a component might be "failed".
-->