#!/bin/sh

# Adapt image paths in markdown files.

# This file si supposed to be executed via
# build-external-repositories.sh inside a Docker container.
# with current path "/workdir"

targetfolder="/workdir/$1"
reponame=$2

echo "---"
echo "Fixing image references in ${targetfolder}/${reponame}/"
for markdownfile in ${targetfolder}/${reponame}/*.md; do
  echo "  ${markdownfile}"
  sed -i -E "s:\(([^\(]+\.)(png|jpg|jpeg|gif):\(/img/${reponame}/\1\2:g" "${markdownfile}"
done
