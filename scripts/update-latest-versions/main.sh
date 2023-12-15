#!/bin/bash

# This script updates the latest version numbers of
#
# - gsctl
# - kubectl-gs
#
# displayed in docs.

set -e

docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner \
    -c "curl -sSL --fail-with-body https://api.github.com/repos/giantswarm/gsctl/releases/latest | jq -er .tag_name | tr -d '\n'" \
    > src/layouts/shortcodes/gsctl_version.html

# For kubectl-gs, we have to cut the leading 'v' from the tag
docker run --rm --entrypoint /bin/sh quay.io/giantswarm/docs-scriptrunner \
    -c "curl -sSL --fail-with-body https://api.github.com/repos/giantswarm/kubectl-gs/releases/latest | jq -er .tag_name | sed 's/^v//' | tr -d '\n'" \
    > src/layouts/shortcodes/kubectl_gs_version.html
