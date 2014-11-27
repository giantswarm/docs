# Environments

<p class="lastmod">Last edited on October 28, 2014 by Matthias Lübken</p>

Environments allow you to deploy your apps in __multiple independent contexts__ for different purposes. As an example, you might want to have one environment for development purposes and another for production.

Environments are managed with the swarm client using the `swarm env` command. In order to list all available options, use:

    $ swarm help env

Environments are distinguished by a __distinct name__. The name is a compound of two parts, seperated by a forward slash:

1. The company name
2. The actual environment name

## The default environment

When you start working with the swarm client, you are automatically assigned to a default environment named after your username as the company name part and "dev" as the second part. For a user named "luebken", this would be:

    luebken/dev

Note that you are free to set up environments with arbitrary names. Read on for details on creating environments.

To find out which environment you are currently working in (i.e. your selected environment), simply use the `swarm env` command without any argument:

    $ swarm env

## Creating and selecting an environment

To select an environment, use the `swarm env` command with the respective environment name as argument. This will create the environment if it didn't exist already. To select/create an environment called "luebken/prod" your command would look like this:
    
    $ swarm env luebken/prod

If the environment already existed, it is now the selected environment. If it didn't exist, yet, it is created and then selected.
<!--
TODO: explain what actually happens when creating an environment)
-->

## Showing available environments

To lists all environments, use the `swarm env` command with the `-a` switch:

    $ swarm env -a
        luebken/dev
     *  luebken/prod

Here, the names of all environments are printed. In addition, the selected environment is marked with an asterisk.

## Deleting an environment

Deleting an environment removes that environment from the list of known environments which you see when you issue the `swarm env` command without argument.

Be aware that deleting an environment does not delete or stop any applications you (or someone else in your company) might have deployed in that environment.

To delete an environment, use the `swarm env` command with the `-d` switch and the respective env name:

    $ swarm env -d mycompany/test

If you delete the currently selected environment this way, your default environment (see above) will be selected.
