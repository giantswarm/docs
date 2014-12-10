description: Reference page for 'swarm logs' which allows to access logs of your component instances.

# Accessing process logs

<p class="lastmod">Last edited on November 10, 2014 by Marian Steinbach</p>

Logs of processes running on Giant Swarm can be accessed using the `swarm logs` command.

Note: For logs to be accessible in this way, processes have to send their log messages to STDOUT or STDERR. This is the standard with Docker containers running single processes each.

## Returning all log messages

The command requires an instance ID for the instance your component is running on. If the component you are interested in is running on multiple instances, you have to inquire the logs for each instance seperately.

<!-- TODO link instance IDs reference page here once it's created -->

    $ swarm logs <instance_id>

As a result, all log entries recorded so far will be printed to your console.

Note that, depending on the amount of log messages collected, you might experience some delay before you start to get an output.

## Only return the latest log messages

To make log access faster and more efficient, you can specify a number of lines to be returned from the end. This is very similar to piping a log file into the popular `tail` program, hence the according command line option here is called `--tail` or `-t` in short.

Here is how to use it:

    $ swarm logs <instance_id> -t <num-lines>

Or

    $ swarm logs <instance_id> --tail=<num-lines>

## Continuous output

You can print out new log messages as they occur. For this purpose, add the `--follow` or `-f` switch to the command.

    $ swarm logs <instance_id> -f

Or

    $ swarm logs <instance_id> --follow

You can also combine the `--tail`/`-t` and the `--follow`/`-f` switches to first cap the log output returned and then follow new messages as they come up. An example:

    $ swarm logs b4405a86-958e-4a46-ac14-41404c5e17bd -t 100 -f

## Further reading

 * [Getting instance statistics](../status/)
 * [Getting an app's status](../status/)
