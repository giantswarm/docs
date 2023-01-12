---
linkTitle: init
title: "'kubectl gs gitops init' command reference"
description: Reference documentation on how to initialize an empty GitOps repository, so that it can be used with the `kubectl-gs` plugin.
weight: 10
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2022-09-29
aliases:
  - /reference/kubectl-gs/gitops/init
  - /ui-api/kubectl-gs/gitops/init
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What I need for a start in the GitOps repository?
---

This command creates the initial files and directories in your GitOps repository the other commands rely on.

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

The security architecture of the GitOps repository relies on [Mozilla SOPS](https://github.com/mozilla/sops),
however the encryption is not performed automatically by `kubectl-gs`. Please download and run the `sops`
binary to be able to decrypt and encrypt secrets.

In order to aid security, the `init` command also creates a pre-commit git hook. It is a simple shell script that
checks for unencrypted manifests before pushing any local commits.

**Note:** the `.git/hooks` directory is not propagated to the repository upon pushing, hence the pre-commit
hook configured for a cloned copy is not shared with other users of the repository. We encourage you to run
the `init` command each time you clone the repository.

## Usage

Basic command syntax: `kubectl gs gitops init [FLAGS]`.

### Flags

{{% kubectl_gs_gitops_common_flags %}}

## Example

```nohighlight
kubectl gs gitops init \
  --local-path /tmp/gitops-demo \
  --dry-run
```

will generate this output:

```nohighlight
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

The same executed without `--dry-run` will write these changes to the target directory.
