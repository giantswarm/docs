# Shell command completion

<p class="lastmod">Last edited on November 4, 2014 by Marian Steinbach</p>

The `swarm` command line client allows you to use tab-completion in the Bash shell for faster input of command names and some arguments.

## Prerequisites

Your Bash environment needs support for smart completion. On most common Unix systems, this requires installing an additional software package.

On __Ubuntu Linux__, for example, you can install the software package named `bash-completion` via `apt-get`.

    $ sudo apt-get install bash-completion

Note that we currently only support `/etc/bash_completion.d` as a target directory for completion files. Systems like Mac OS X with the homebrew bash-completion package use a different directory and are thus not currently supported.

Additionaly, you should make sure that the completion files form the target directory mentioned above are actually read when a new shell session is started. This requires some code in `~/.bashrc`, `~/.bashr_profile` or `~/.profile`, depending on your system. Please refer to you systems's documentation for further information.

## Installing shell completion using swarm

The `swarm` command line client provides a command named `completion`for installing the necessary script in the right place. Call it like this:

    $ swarm completion bash

