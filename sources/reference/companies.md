description: This is the reference page for the 'swarm company' command, which allows you to manage teams of users.

# Companies

<p class="lastmod">Last edited on January 6, 2015 by Marian Steinbach</p>

Companies allow for sharing resources between users. Users belonging to the same company can, for example, control applications of that company or access the company's docker images on our [registry](../registry/).

## Creating a company

To create a company, call `swarm company create <company-name>`:

    $ swarm company create mygreatcompany
    Company mygreatcompany has been created

Note that company names are unique within Giant Swarm, so if the company has been already created, additional users have to be [added](#adding-a-user-to-a-company) by the initial creator of the company.

## Listing company membership

To list the companies you belong to, use the `-l` switch:

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

To see and use applications from colleagues you have to use the right environment. See the [environments](/reference/env) reference for details. 
