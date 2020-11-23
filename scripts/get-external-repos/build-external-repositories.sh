#!/bin/bash

# Here we pull in content from external repositories. While doing so we do
# - copy images (png, jpg)to a special folder
# - copy markdown content to another folder
# - Rewrite image references in the markdown
# - add a link to the recipe repository for collaboration
#
# This assumes:
# - list of repository URLs in src/external-repositories.txt
# - recipe repositories have a "docs" subfolder
# - In the "docs" folder is an "index.md" file
# - This index.md file has HUGO frontmatter
# - There may be additional markdown files in that folder
# - There may be PNG and/or JPG images in that folder

# Path to where recipe content should be placed in the docs site
CONTENT_BASE_DIR=$(pwd)/build

# Path to where images should be copied to
IMG_BASE_DIR=$(pwd)/build/static/img

cat ./src/external-repositories.txt | while read repoline
do

	# split line into repository URL, target path
	parts=(${repoline// / })
	repourl=${parts[0]}
	targetpath=${parts[1]}

	echo "\nImporting content from ${repourl} to ${targetpath}"

	# derive reponame from repourl
	filename=$(basename ${repourl})
	parts=(${filename//./ })
	reponame=${parts[0]}

	# Create folders for markdown and images
	mkdir -p ${CONTENT_BASE_DIR}/${targetpath}/${reponame}
	mkdir -p ${IMG_BASE_DIR}/${reponame}

	# Copy repo content to target location
	cp vendor/${reponame}/docs/*.md ${CONTENT_BASE_DIR}/${targetpath}/${reponame}/
	cp vendor/${reponame}/docs/*.png ${IMG_BASE_DIR}/${reponame}/ || echo "no PNG files"
	cp vendor/${reponame}/docs/*.jpg ${IMG_BASE_DIR}/${reponame}/ || echo "no JPG files"

	# Adapt image paths.
	# To avoid sed incompatibilities, we are doing this in a Docker container.
	docker run --rm -v $(pwd):/workdir quay.io/giantswarm/alpine:3.12 /workdir/fix-image-paths.sh build/${targetpath} ${reponame}

	echo "<hr>" >> ${CONTENT_BASE_DIR}/${targetpath}/${reponame}/index.md
	echo "You can collaborate on this recipe on [GitHub](https://github.com/giantswarm/${reponame})." >> ${CONTENT_BASE_DIR}/${targetpath}/${reponame}/index.md
done
