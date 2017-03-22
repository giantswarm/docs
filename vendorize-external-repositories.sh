#!/bin/bash

# Here we pull in content from external repositories. While doing so we do
# - copy images (png, jpg)to a special folder
# - copy markdown content to another folder
# - Rewrite image references in the markdown
# - add a link to the recipe repository for collaboration
#
# This assumes:
# - list of repository URLs in docs-content/external-repositories.txt
# - recipe repositories have a "docs" subfolder
# - In the "docs" folder is an "index.md" file
# - This index.md file has HUGO frontmatter
# - There may be additional markdown files in that folder
# - There may be PNG and/or JPG images in that folder

cat ./vendor/docs-content/external-repositories.txt | while read repoline
do

  # split line into repository URL, target path
  parts=(${repoline// / })
  repourl=${parts[0]}
  targetpath=${parts[1]}

  echo "\Vendorizing ${repourl}"

  # derive reponame from repourl
  filename=$(basename ${repourl})
  parts=(${filename//./ })
  reponame=${parts[0]}

  # Empty sub-folder for this repo here in the build folder
  rm -rf ${reponame}

  # Clone the repository from github
  git clone --depth 1 https://github.com/giantswarm/${reponame}.git vendor/${reponame}

  # Delete .git folder so that git doesn't commit this as a subproject, but as actual files in the repo
  rm -rf vendor/${reponame}/.git
done
