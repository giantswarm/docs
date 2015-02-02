#!/bin/bash

# This script runs the content server in production.
# If a link to the search service exists, it runs
# the search indexer before starting the server, to
# push new content to the search engine.

# Run indexer (if ElasticSearch address is configured)
[ -z "$SITESEARCH_PORT_9200_TCP_ADDR" ] || {
	echo "SITESEARCH_PORT_9200_TCP_ADDR is set. Indexing.";
	# start indexing content for search
	sleep 10
	cd /docs/search && python ./indexer.py
}


cd /docs/swarmdocs

echo "DEVELOPMENT_MODE: ${DEVELOPMENT_MODE}"
echo "BASE_URL: ${BASE_URL}"


if [ -z ${DEVELOPMENT_MODE+x} ];
then
	exec hugo server --port=80 --baseUrl=${BASE_URL}
else 
	exec hugo server --port=80 --baseUrl=${BASE_URL} --watch
fi
