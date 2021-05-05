#!/bin/bash

# This script updates the latest version numbers of
#
# - gsctl
#
# displayed in docs.

set -e

docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner \
    -c "curl --silent https://api.github.com/repos/giantswarm/gsctl/releases/latest|jq -r .tag_name|tr -d '\n'" \
    > src/layouts/shortcodes/gsctl_version.html

docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner \
    -c "curl --silent https://api.github.com/repos/giantswarm/kubectl-gs/releases/latest|jq -r .tag_name|tr -d '\n'" \
    > src/layouts/shortcodes/kubectl_gs_version.html
