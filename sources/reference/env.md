## Working with environments

    $ swarm help env

With `swarm env` you can manage different environments (envs) to which you want to deploy your applications. 

Env is made up of a company and an env (*) itself. E.g. `luebken/dev`. We have choosen your 'username' and 'dev' as the default.

To add a new or choose an env, simple use the `swarm env` command:
    
    $ swarm env luebken/prod

To lists all envs:

    $ swarm env -a
        luebken/dev
     *  luebken/prod

## Working with companies
If you choose a different company in your env make sure you are part of the company. Let the initial creator of the company add your username:

    $ swarm company add-user giantswarm marian

To create a company simply:

    $ swarm company
    Company: mygreatcompany

To list the current companies you belong to:
    $ swarm company -l
    giantswarm
    luebken
    mygreatcompany

(*) No it's not recursive. ;-)