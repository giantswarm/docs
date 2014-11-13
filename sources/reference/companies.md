# Companies

<p class="lastmod">Last edited on October 28, 2014 by Matthias Lübken</p>

Companies allow to share resources between users. Users belonging to the same company can, for example, control applications of that company or access the companie's docker images on our [registry](../registry/).

## Creating a company

To create a company, call `swarm company` and enter the company name when prompted:

    $ swarm company
    Company: mygreatcompany


## Listing company membership

To list the companies you belong to, use the `-l` switch:

    $ swarm company -l
    giantswarm
    luebken
    mygreatcompany


## Adding a user to a company

In order to make a user a member of a certain company, the initial creator of the company can issue a `swarm company add-user` command with the company name and the user name as additional arguments:

    $ swarm company add-user mycompany myuser

## Using companies

To see and use applications from colleagues you have to use the right environment. See the [environments](/reference/env) reference for details. 
