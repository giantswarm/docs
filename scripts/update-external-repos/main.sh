#!/bin/bash

# Here we pull in content from external repositories. While doing so we do
# - copy images (png, jpg) to a special folder
# - copy markdown content to another folder
# - Rewrite image references in the markdown
# - add a link to the recipe repository for collaboration
#
# This assumes:
# - list of repository URLs in repositories.txt
# - recipe repositories have a "docs" subfolder
# - In the "docs" folder is an "index.md" file
# - This index.md file has HUGO frontmatter
# - There may be additional markdown files in that folder
# - There may be PNG and/or JPG images in that folder

mytmpdir=$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')
echo "Temp dir: $mytmpdir"

cat ./scripts/update-external-repos/repositories.txt | while read repoline
do

  # split line into repository URL, target path
  parts=(${repoline// / })
  repourl=${parts[0]}
  targetpath=${parts[1]}

  echo "Copying repo ${repourl} to ${targetpath}"

  # derive reponame from repourl
  filename=$(basename ${repourl})
  parts=(${filename//./ })
  reponame=${parts[0]}

  # Empty sub-folder for this repo here in the build folder
  rm -rf ${reponame}

  # Clone the repository from github
  git clone --depth 1 https://github.com/giantswarm/${reponame}.git $mytmpdir/${reponame}

  # Copy content into src tree
  if [ -d "$mytmpdir/${reponame}/docs" ]; then
    rm -rf ${targetpath}
    mkdir ${targetpath}
    cp $mytmpdir/${reponame}/docs/*.md ${targetpath}/ || echo "WARN: no Markdown files"
    cp $mytmpdir/${reponame}/docs/*.png ${targetpath}/ || echo "INFO: no PNG files"
    cp $mytmpdir/${reponame}/docs/*.jpg ${targetpath}/ || echo "INFO: no JPG files"
  fi
done
