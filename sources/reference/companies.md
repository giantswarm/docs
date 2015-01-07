description: This is the reference page for the 'swarm company' command, which allows you to manage teams of users.

# Companies

<p class="lastmod">Last edited on January 7, 2015 by Marian Steinbach</p>

Companies allow for sharing resources between users. Users belonging to the same company can, for example, control applications of that company or access the company's docker images on our [registry](../registry/).

## Your default company

As a Giant Swarm user you automatically have a _default company_ assigned to you. This is named after your user name. So if your user name is `yourname`, your default company name is `yourname`, too.

This is especially relevant for two reasons:

* All your applications on Giant Swarm are associated with a distinct [environment](../env/). When you first login with the `swarm` CLI as user `yourname`, an environment is automatically created and selected. This default environment is called `yourname/dev` and belongs to your default company.

* When using our [private registry](../registry/) for your Docker images, company names are used as namespace identifiers. When starting with Giant Swarm, simply use your default company name (your user name) as image namespace.

## Creating a company

To create a company, call `swarm company create <company-name>`:

    $ swarm company create mygreatcompany
    Company mygreatcompany has been created

Note that company names are unique within Giant Swarm, so if the company has been already created, additional users have to be [added](#adding-a-user-to-a-company) by the initial creator of the company.

## Listing company membership

As a user you can be part of any number of companies. To list the companies you belong to, use the `-l` switch:

    $ swarm company -l
    giantswarm
    luebken
    mygreatcompany


## Adding a user to a company

In order to add a user as a member of a certain existing company, the initial creator of the company can issue a `swarm company add-user` command with the company name and the user name as arguments. The general syntax is like this:

    $ swarm company add-user <company> <user>

Example:

    $ swarm company add-user mycompany myuser

## Removing a user from a company

To end a user's company membership, use the `remove-user` subcommand. The syntax is pretty much the same as with the `add-user` subcommand:

    $ swarm company remove-user <company> <username>

## Show company members

To find out who is member of a company, use the `show` subcommand with this syntax:

    $ swarm company show <company>

Example:

    $ swarm company show giants
    Company giants

    Username:
    mel.hein
    frank.gifford
    ya.tittle
    lawrence.taylor

<!-- TODO: Deleting a company (cannot yet explain this well) -->

## Using companies

As the member of a company, you can control all existing applications and create new applications within any environment of that company. Have a look at the [environments](../env/) reference for details.

You can also push images to the namespaces of any of your companies in the private registry and use all images with your companies namespaces in your applications. Please refer to the [registry reference](../registry/) for further information.

## Further Reading

* [Environments](../env/)
* [Using the registry](../registry/)
