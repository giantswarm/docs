# Shell command completion

<p class="lastmod">Last edited on November 7, 2014 by Marian Steinbach</p>

The `swarm` command line client allows you to use tab-completion in the Bash shell for faster input of command names and some arguments.

## Prerequisites

### 1. Bash completion software

Your Bash environment needs support for smart completion. On most common Unix and Linux systems, this requires a specific software package to be installed. This package is often called `bash-completion`, but that may vary depending on the distribution you use.

On __Ubuntu__ and __Debian__, for example, you can install the software package named `bash-completion` via `apt-get`.

    $ sudo apt-get install bash-completion

On __RHEL__ or __CentOS__, the according command is

    $ sudo yum install bash-completion

On __Mac OS X__ you can install this package using [Homebrew](http://brew.sh/), with the following command:

    $ brew install bash-completion

### 2. Know your 'bash_completion' path

After installing the required software, please make sure that you know the path of your `bash_completion.d` directory. The standard location for this is `/etc/bash_completion.d`. However, systems might use a different path. For example, Homebrew on Mac OS X defaults to `/usr/local/etc/bash_completion.d`.

This directory is accompanied by a shell script of similar name, usually `/etc/bash_completion`. Make sure you know the path of that file, since you will need it in the next step.


### 3. Check your bash_profile

For bash completion to work, the scripts inside the `bash_completion.d` directory have to be read for each new shell session. This requires some code in your Bash profile. The bash profile is usually a file in you home directory, named `.bash_profile` or `.bashrc`.

Assuming that `/etc/bash_completion` is the correct path of your bash completion script, you would need some code like this in your profile:

```
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi
```

## Installing shell completion using swarm

The `swarm` command line client provides a command named `completion` for installing the necessary script in the right place (the bash_completionn.d` directory mentioned before). Call it like this:

    $ swarm completion bash

This is it. In order to actually use the completion mechanism, you need to open a new shell session.

To try it out, simply type `swarm scale` and hit Enter.
