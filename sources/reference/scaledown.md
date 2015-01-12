description: Reference page for the 'swarm scaledown' command, which allows you to reduce the number of instances running for a particular component.

# Scaling down a component

<p class="lastmod">Last edited on January 12, 2015 by Marian Steinbach</p>

The `swarm scaledown` command is used to decrease the number of instances running a service component.

## Command syntax

The command requires a service component name as argument. Optionally, the number of instances to be added can be given. If no number is given, `1` is assumed.

    $ swarm scaledown <app/service/component> [num-to-remove]

For example, if you have an "onlineshop" app with a service called "imageserver" and a component called "nginx", use the following command to __take away one__ instance from this component:

    $ swarm scaledown onlineshop/imageserver/nginx

To remove two instances, use this syntax:

    $ swarm scaledown onlineshop/imageserver/nginx 2

## Related reading

 * [Scaling up a component](../scaleup/)
