#!/bin/bash

# This script updates the latest version numbers of
#
# - gsctl
# - kubectl-gs
#
# displayed in docs.

set -e

docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner \
    -c "curl --silent https://api.github.com/repos/giantswarm/gsctl/releases/latest|jq -j .tag_name" \
    > src/layouts/shortcodes/gsctl_version.html

# For kubectl-gs, we have to cut the leading 'v' from the tag
docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner \
    -c "curl --silent https://api.github.com/repos/giantswarm/kubectl-gs/releases/latest|jq -j .tag_name | cut -c 2- | tr -d '\n'" \
    > src/layouts/shortcodes/kubectl_gs_version.html
