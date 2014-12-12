description: Reference page for the 'swarm stats' command, which allows you to access basic statistics about the resource usage of your components.

# Getting instance statistics

<p class="lastmod">Last edited on November 9, 2014 by Marian Steinbach</p>

The `swarm stats` command allows you to get information on the current system load for a specific instance.

## Command syntax

The command requires an instance ID as the first argument.

    $ swarm stats <instance_id>

<!-- TODO: Create reference page on instance IDs and link from here. -->

Here is an example output:

```
component               memory usage (mb)  memory capacity (mb)  memory usage (%)  cpu usage (%)
docs/docsservice/nginx  16.19              3956.24               0.41              2
```

## Further reading

 * [Accessing process logs](../logs/)
 * [Getting an app's status](../status/)
