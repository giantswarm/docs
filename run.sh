#!/bin/bash

# This script runs the content server in production.
# If a link to the search service exists, it runs
# the search indexer before starting the server, to
# push new content to the search engine.


# start indexing content for search
sleep 3
cd /docs/search && python ./indexer.py


cd /docs/swarmdocs

echo "BASE_URL: ${BASE_URL}"
exec hugo server --port=80 --baseUrl=${BASE_URL} --appendPort=false
