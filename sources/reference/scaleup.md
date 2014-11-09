# Scaling up a component

<p class="lastmod">Last edited on November 9, 2014 by Marian Steinbach</p>

The `swarm scaleup` command is used to increase the number of instances running a service component.

## Command syntax

The command requires a service component name as well as the number of instances to be added as arguments.

    $ swarm scaleup <app/service/component> --count=<num-to-add>

For example, if you have an "onlineshop" app with a service called "imageserver" and a component called "nginx", use the following command to __add one__ instance for this component:

    $ swarm scaleup onlineshop/imageserver/nginx --count=1

## Further reading

 * [Scaling down a component](../scaledown/)
