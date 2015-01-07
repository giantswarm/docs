description: This is the reference page for the 'swarm user' command, which allows you to change your password or email address and get the current user name.

# Modify user settings

<p class="lastmod">Last edited on January 7, 2015 by Marian Steinbach</p>

The `swarm user` command allows you to fiddle with a few things regarding your user account.

Note: In case you __lost your password__, the CLI _does not allow you_ to restore your password. Please contact us at [support@giantswarm](mailto:support@giantswarm) to help you in this case.

In addition, please be aware that it is currently not possible to change your _user name_.

## Printing your user name

Use this command to print out your own user name:

    $ swarm user

## Setting a new password

You can change your password while logged in with the CLI. Use the following command:

    $ swarm user -u password

You will be prompted to enter the current password first, then the new password and then once again the new password.

## Changing your email address

To change the email address associated with your account, use this command:

    $ swarm user -u email

You will prompted to enter the new email address on the prompt interactively.

## Print your user name

You can use the `swarm user` command without arguments to print out your user name if you are logged in. This might be useful expecially when scripting the use of the swarm CLI.

## Further reading

 * [Getting basic information](../info/)
 * [Companies](../company/)
