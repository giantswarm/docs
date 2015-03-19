#!/bin/bash

echo `date +"%Y%m%d%H%M"` > swarmdocs/layouts/partials/cache_datestamp.html

rm -rf swarmdocs/public/*
rm -rf swarmdocs/content
rm -rf swarmdocs/static/img
cp -r docs-content/content swarmdocs/
cp -r docs-content/img swarmdocs/static/

cd swarmdocs && hugo server -ws .
