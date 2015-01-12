#!/bin/bash

[ -z "$SITESEARCH_PORT_9200_TCP_ADDR" ] || {
	echo "SITESEARCH_PORT_9200_TCP_ADDR is set. Indexing.";
	# set SITESEARCH ip/port for search indexer
	echo "- ${SITESEARCH_PORT_9200_TCP_ADDR}:${SITESEARCH_PORT_9200_TCP_PORT}" > search/hosts.yml;
	# start indexing content for search
	cd search && python indexer.py &
}

# use mkdocs server to publish pages
cd /docs && exec mkdocs serve
