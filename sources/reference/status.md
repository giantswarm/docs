# Getting an app's status

<p class="lastmod">Last edited on November 9, 2014 by Marian Steinbach</p>

The `swarm` command line tool provides the `status` command for you to fetch information on a specific app as well as it's services and components.

## Syntax and output

The command needs the name of your app which you have set in the app configuration with the `app_name` key as an argument. The syntax is:

    $ swarm status <app_name>

For example, for an app named "onlineshop", we would use this command:

    $ swarm status onlineshop

Here is an example output:

```
App onlineshop is up

service          component      instanceid                            status
appserver        nginx          962fac1c-e9ba-42b6-9223-6edec84f003f  up
appserver        gunicorn       b4405a86-958e-4a46-ac14-41404c5e17bd  up
appserver        redis          863fac2c-e8ba-42a3-9223-6edec84f003f  up
appserver        mongodb        2370a56c-0e5a-4b82-9e25-07ffa915988b  up
appserver        elasticsearch  9c79161b-baec-447b-9a8e-230206268570  up
payments         payments       71481fdf-1fa1-49f0-9320-d29df5297ae5  up
imageserver      nginx          d29df528-0e5a-4b82-9223-6ed0626817bd  up
```

The first line of the output shows as a summary the status of the app. The second part is a table of all components within all services of that app. The table columns show which service the component belongs to, the component name, the ID of the instance the component is running on and the component status.

TODO: Clarify instance ID

## Statuses and their meaning

TODO: Add complete list of all statuses
