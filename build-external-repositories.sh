#!/bin/sh

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

# Path to where recipe content should be placed in the docs site
CONTENT_BASE_DIR=$(pwd)/build

# Path to where images should be copied to
IMG_BASE_DIR=$(pwd)/build/static/img

cat ../vendor/docs-content/external-repositories.txt | while read repoline
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
	cp vendor/${reponame}/docs/*.png ${IMG_BASE_DIR}/${reponame}/
	cp vendor/${reponame}/docs/*.jpg ${IMG_BASE_DIR}/${reponame}/

	# adapt image paths
	for markdownfile in ${CONTENT_BASE_DIR}/${targetpath}/${reponame}/*.md; do
		sed -i ".bak" -E "s:\(([^\(]+\.)(png|jpg|jpeg|gif):\(/img/${reponame}/\1\2:g" "${markdownfile}"
		rm -f "${markdownfile}.bak"
	done

	echo "<hr>\n" >> ${CONTENT_BASE_DIR}/${targetpath}/${reponame}/index.md
	echo "You can collaborate on this recipe on [GitHub](https://github.com/giantswarm/${reponame})." >> ${CONTENT_BASE_DIR}/${targetpath}/${reponame}/index.md
done
