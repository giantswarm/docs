# Creating an app

<p class="lastmod">Last edited on November 27, 2014 by Marian Steinbach</p>

Services running on Giant Swarm are grouped as *apps* which are described in `swarm.json` files. Creation of apps is done via the `swarm create` command.

## Basic app creation

The basic command syntax is:

    $ swarm create [<app-config-file>]

Assuming that your app configuration file is called `swarm.json` and resides in the current directory, simply call the `swarm create` command like this:

    $ swarm create

For further information about the app configuration file, please refer to the [swarm.json reference page](../swarm-json/).

<!-- TODO: Explain what this actually does in the background or alternatively link to the architecture overview article which explains this in more detail. -->

## Using variable definitions

You can use an app configuration file like `swarm.json` as a template with variables instead of actual values in them. Variables act as placeholder keys, which are then replaced by values, which you pass to the `swarm create` command.

Variable names in the app configuration file have to start with a *dollar sign* (`$`).

When creating a new app, you can pass values for your variables in two different ways:

 * as command line options
 * as a variable definition file

Also, both approaches can be combined.

### Passing variables on the command line

If you want to define variable values directly on the command line, you can use the `--var` option. Here is the basic format:

    $ swarm create --var=<key=value>

If, for example, your app configuration file `swarm.json` contains the two variables `$var1` and `$var2`, you can assign values in the following way:

    $ swarm create --var=var1=foo --var=var2=bar

### Passing variables in a file

For frequent re-use you can store your app creation variables in a JSON variables file. Here is an example illustrating the required format:

```json
{
    "mycompany/dev": {
        "redis_port": 8080
    }
    "mycompany/production": {
        "redis_port": 6397
    }
}
```

As you can see, the file contains a single JSON object, which on the top level defines keys that are named after your [environments](../env/). This structure allows you to assign different values to variables for each of your environments.

With the example above, you would now use a variable name `$redis_port` (dont forget the dollar sign!) where appropriate in your app configuration file (`swarm.json`).

Here is how you make use of your variables file when calling `swarm create`:

    $ swarm create [<app-config-file>] --var-file=<var-file-path>

So, if your application config is called `swarm.json` and the variables file is `swarmvars.json`, the command would be:

    $ swarm create swarm.json --var-file=swarmvars.json

or simply

    $ swarm create

Note that if your variables file is in the current directory _and_ has the name `swarmvars.json`, it is used automatically. So there is actually no need to specify the `--var-file` option in the case shown above. And since the configuration file is assumed to be `swarm.json`, you don't have to specify this either.

## Combining command line options and file

It is possible to combine both approaches of passing variable values described above. In this case, whenever a variable is defined both in the file and via the command line option, the value assigned via the command line is used.

Here is an example:

    $ swarm create --var-file=swarmvars.json --var=var1=foo --var=var2=bar

The order of the command line options is not important.

## Further reading

* [swarm.json reference page](../swarm-json/)
* [Global command line options](../global-options/)
