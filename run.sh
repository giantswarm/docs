#!/bin/bash

# start indexing content for search
#cd search && python ./searchindexer.py &
cd search && python indexer.py

# use mkdocs server to publish pages
cd /docs && exec mkdocs serve
