## Working with environments

    $ swarm help env

With `swarm env` you can manage different environments (envs) to which you want to deploy your applications. 

The env name is made up of a company and an env (*) itself. E.g. `luebken/dev`. We have choosen your username and the name 'dev' as the default.

To add a new env or make an env the current default, simply use the `swarm env` command with the respective env name:
    
    $ swarm env luebken/prod

To lists all envs, use the `-a` switch:

    $ swarm env -a
        luebken/dev
     *  luebken/prod

## Working with companies

If you choose a different company in your env, make sure you are part of the company. Let the initial creator of the company add your username:

    $ swarm company add-user giantswarm marian

To create a company, simply call `swarm company` and enter the company name when prompted:

    $ swarm company
    Company: mygreatcompany

To list the current companies you belong to, use the `-l` switch:

    $ swarm company -l
    giantswarm
    luebken
    mygreatcompany

(*) No, it's not recursive. ;-)
