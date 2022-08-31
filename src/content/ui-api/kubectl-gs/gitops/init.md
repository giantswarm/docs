---
linkTitle: init
title: "'kubectl gs gitops init' command reference"
description: Reference documentation on how to initialize an empty GitOps repository, so that it can be used with `kubectl-gs` plugin.
weight: 10
menu:
  main:
    parent: kubectlgs-gitops
aliases:
  - /reference/kubectl-gs/gitops/init/
last_review_date: 2022-08-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What I need for a start in the GitOps repository?
---

This command creates initial files and directories in your GitOps repository the other commands rely on.

## Description

The structure created by the command is presented below.

```nohighlight
.
├── .git
│   └── hooks
│       └── pre-commit
├── .sops.yaml
└── management-clusters
```

The security architecture of GitOps repository relies on the [Mozilla SOPS](https://github.com/mozilla/sops),
however the encryption is not performed automatically by the `kubectl-gs`, hence user is obliged to download and run the `sops`
binary on his own. However, in order to aid security and help user the `pre-commit` hook, which is a simple shell script, has
been introduced as a security measure for checking for unencrypted manifests before pushing the local commits.

**Important note**, the `.git/hooks` directory is not propagated to the repository upon pushing, hence `pre-commit`
hook configured for a cloned copy is not shared with other Github users. Users are thus strongly encouraged to run
the `init` command each time they clone the repository.

## Usage

The command to execute is the `kubectl gs gitops init`.

To preview the objects to be created by the command, run it with the `--dry-run` flag. Example:

```nohighlight
kubectl gs gitops init \
--local-path /tmp/gitops-demo \
--dry-run

## CREATE ##
/tmp/gitops-demo/management-clusters
/tmp/gitops-demo/.sops.yaml
creation_rules: []

/tmp/gitops-demo/.git/hooks/pre-commit
#!/bin/sh
#
# The script looks for the *.enc.yaml files that suppose to be encrypted,
# and verifies the encryption has happened.

files=""

while read line
do
	if [ ! -n "$line" ]
	then
		continue
	fi

	grep -q "^sops:$" $line
	if [ $? -ne 0 ]
	then
		files="${files}\n${line}"
	fi
done <<< "$(find . -type f -name '*.enc.yaml')"

if [ -n "$files" ]
then
	cat <<\EOF
!! WARNING !!

Detected files missing the `sops` metadata key on them.

Please run the `sops --encrypt --in-place <path>` command against them to secure the repository.

Find the list of affected files below.
EOF
	echo $files
	exit 1
fi
```

Remove the `--dry-run` flag and re-run it to apply the changes.
