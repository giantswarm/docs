description: Reference page for the 'swarm scaleup' command, which allows you to increase the number of instances running for a particular component.

# Scaling up a component

<p class="lastmod">Last edited on January 6, 2015 by Ewout Prangsma</p>

The `swarm scaleup` command is used to increase the number of instances running a service component.

## Command syntax

The command requires a service component name as well as the number of instances to be added as arguments.

    $ swarm scaleup <app/service/component> <num-to-add>

For example, if you have an "onlineshop" app with a service called "imageserver" and a component called "nginx", use the following command to __add one__ instance for this component:

    $ swarm scaleup onlineshop/imageserver/nginx 1

## Related reading

 * [Scaling down a component](../scaledown/)
