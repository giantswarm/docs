description: This is the reference page for the 'swarm company' command, which allows you to manage teams of users.

# Companies

<p class="lastmod">Last edited on January 6, 2015 by Ewout Prangsma</p>

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

In order to add a user as a member of a certain existing company, the initial creator of the company can issue a `swarm company add-user` command with the company name and the user name as arguments:

    $ swarm company add-user mycompany myuser

## Using companies

To see and use applications from colleagues you have to use the right environment. See the [environments](/reference/env) reference for details. 
