#!/bin/bash

echo `date +"%Y%m%d%H%M"` > swarmdocs/layouts/partials/cache_datestamp.html

rm -rf swarmdocs/public/*
rm -rf swarmdocs/content
rm -rf swarmdocs/static/img
cp -r docs-content/content swarmdocs/
cp -r docs-content/img swarmdocs/static/
mkdir -p swarmdocs/content/api
cat api/frontmatter.txt > swarmdocs/content/api/methods.md
cat ../api/docs/api.md >> swarmdocs/content/api/methods.md

cd swarmdocs && hugo server -ws .
