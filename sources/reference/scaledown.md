# Scaling down a component

<p class="lastmod">Last edited on November 9, 2014 by Marian Steinbach</p>

The `swarm scaledown` command is used to decrease the number of instances running a service component.

## Command syntax

The command requires a service component name as well as the number of instances to be subtracted as arguments.

    $ swarm scaledown <app/service/component> --count=<num-to-add>

For example, if you have an "onlineshop" app with a service called "imageserver" and a component called "nginx", use the following command to __take away one__ instance from this component:

    $ swarm scaledown onlineshop/imageserver/nginx --count=1

## Further reading

 * [Scaling up a component](../scaleup/)
